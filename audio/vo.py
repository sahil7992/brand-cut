#!/usr/bin/env python3
"""ElevenLabs voice pipeline with a hard character budget guard.

usage:
  vo.py budget                                   live usage vs the job cap in audio/budget.json
  vo.py voices                                   account voices (ElevenLabs key) or Kokoro voices (no key)
  vo.py say <project> [--provider auto|elevenlabs|kokoro|system] [--voice ID] [--model M] [--speed 1.1] [--stability .6] [--similarity .8]
                      [--style .35] [--seed N] [--take NAME] [--dry]
        one full-script generation of <project>/audio/vo/script.txt via /with-timestamps,
        then split per line, filler + pause cleanup, light polish -> audio/vo/<take>/
  vo.py post <project> <take>                    redo split/cleanup on an existing take (free)
  vo.py sfx "<prompt>" <out.mp3> [--dur 1.0] [--influence .4]   no key: copies the closest bundled SFX
  vo.py music "<prompt>" <out.mp3> [--ms 30000]  Eleven Music, instrumental only (needs a key)

Providers (see VOICE.md): auto = elevenlabs if ELEVENLABS_API_KEY is set, else kokoro (local, open source),
else system (macOS say / espeak-ng). All write the same audio/vo/<take>/L01.wav + lines.json layout.

script.txt: one VO line per line; '#' lines and blanks ignored; an optional "@12.5 " prefix gives
the line's start on the film timeline (written to lines.json for mix.py). No ellipses, no dashes,
no audio tags with v2-family models. Defaults (proven 2026-10-17/18): eleven_turbo_v2_5, speed 1.1,
stability 0.6, similarity 0.8, style 0.35, speaker boost, output mp3_44100_128 (Starter max).

Guard: before every paid call the live character_count is read; the call is refused when
(count - baseline) + estimate > job_cap (audio/budget.json). After the call the real cost is
measured from the counter delta and appended to the ledger file. Never buys credits.
Key: macOS Keychain service "elevenlabs-api-key" (never written to disk).
"""
import argparse, base64, datetime, json, os, re, shutil, subprocess, sys, tempfile, urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
SKILL = HERE.parent
API = "https://api.elevenlabs.io"
FILLERS = {"um", "uh", "uhm", "erm", "er", "ah", "aah", "aha", "ahh", "hmm", "mm", "mhm", "huh", "eh", "oh"}


def key():
    k = os.environ.get("ELEVENLABS_API_KEY")
    if not k:
        sys.exit("set ELEVENLABS_API_KEY in your environment")
    return k


def call(method, path, body=None, raw=False):
    req = urllib.request.Request(API + path, method=method, headers={"xi-api-key": key(), "Content-Type": "application/json"},
                                 data=json.dumps(body).encode() if body is not None else None)
    with urllib.request.urlopen(req, timeout=300) as r:
        data = r.read()
    return data if raw else json.loads(data)


def cfg():
    p = HERE / "budget.json"
    if not p.exists():
        used, _limit, _tier = usage()
        p.write_text(json.dumps({"baseline_character_count": used, "job_cap": 20000, "local_spent": 0, "ledger": str(HERE / "LEDGER.md")}, indent=2))
        print(f"created {p} (baseline {used}, job_cap 20000 characters; edit job_cap to taste)")
    return json.loads(p.read_text())


def usage():
    s = call("GET", "/v1/user/subscription")
    return s["character_count"], s["character_limit"], s.get("tier")


def guard(estimate, what):
    c = cfg()
    used, limit, tier = usage()
    spent = max(used - c["baseline_character_count"], c.get("local_spent", 0))
    if spent + estimate > c["job_cap"]:
        sys.exit(f"REFUSED {what}: job spent {spent} + estimate {estimate} > cap {c['job_cap']} (account {used}/{limit}). Use the fallback path.")
    if used + estimate > limit:
        sys.exit(f"REFUSED {what}: account would exceed its plan limit ({used}+{estimate}>{limit}). Never buy credits.")
    return used


def ledger(before, what, est):
    import time
    for _ in range(8):
        after, limit, _t = usage()
        if after > before:
            break
        time.sleep(5)
    cost = after - before if after > before else est
    c = cfg()
    c["local_spent"] = c.get("local_spent", 0) + cost
    (HERE / "budget.json").write_text(json.dumps(c, indent=2))
    job = max(after - c["baseline_character_count"], c["local_spent"])
    row = f"| {datetime.datetime.now():%Y-%m-%d %H:%M} | {what} | {cost}{'' if after > before else ' (estimate; counter lagging)'} | {job} | {after:,} |\n"
    lp = Path(c["ledger"]).expanduser()
    if lp.exists():
        s = lp.read_text()
        marker = "\n## Disk"
        s = s.replace(marker, row.rstrip("\n") + "\n" + marker, 1) if marker in s else s + row
        lp.write_text(s)
    print(f"cost {cost} credits; job total {job}/{c['job_cap']}; account counter {after}/{limit}")
    return cost


def read_script(project):
    lines = []
    for raw in (Path(project) / "audio/vo/script.txt").read_text().splitlines():
        s = raw.strip()
        if not s or s.startswith("#"):
            continue
        at = None
        m = re.match(r"@([\d.]+)\s+(.*)", s)
        if m:
            at, s = float(m.group(1)), m.group(2)
        if re.search(r"\.\.\.|…|—|–| - ", s):
            sys.exit(f"script line has an ellipsis or dash (they slow the read): {s}")
        lines.append({"text": s, "at": at})
    return lines


def brand_alias(project):
    try:
        film = json.loads((Path(project) / "film.json").read_text())
        b = json.loads((SKILL / "brands" / film["brand"] / "brand.json").read_text())
        return b.get("voice", {}).get("tts_alias", {}), b.get("voice", {})
    except Exception:
        return {}, {}


def ff(*args):
    subprocess.run(["ffmpeg", "-v", "error", "-y", *args], check=True)


def post(project, take):
    """Split a take per line from the alignment, cut fillers/voiced gaps found by whisper, cap pauses, polish."""
    d = Path(project) / "audio/vo" / take
    meta = json.loads((d / "take.json").read_text())
    al = meta["alignment"]
    chars, st, en = al["characters"], al["character_start_times_seconds"], al["character_end_times_seconds"]
    full = d / "full.wav"
    ff("-i", str(d / "full.mp3"), "-ac", "1", "-ar", "48000", str(full))
    # whisper on the full take for fillers outside the script
    tdir = d / "whisper"
    tdir.mkdir(exist_ok=True)
    subprocess.run(["npx", "-y", "hyperframes@0.8.183", "transcribe", str(full), "--json", "-d", str(tdir)], capture_output=True)
    words = json.loads((tdir / "transcript.json").read_text()) if (tdir / "transcript.json").exists() else []
    fillers = [w for w in words if re.sub(r"[^a-z]", "", w["text"].lower()) in FILLERS]
    out, pos = [], 0
    text = "".join(chars)
    for i, ln in enumerate(meta["lines"]):
        spoken = ln["tts_text"]
        k = text.find(spoken, pos)
        if k < 0:
            sys.exit(f"line {i} not found in alignment")
        pos = k + len(spoken)
        idx = [j for j in range(k, k + len(spoken)) if chars[j].strip()]
        t0, t1 = max(0.0, st[idx[0]] - 0.02), en[idx[-1]] + 0.06
        cut = [(f["start"], f["end"]) for f in fillers if t0 - 0.3 <= f["start"] <= t1]
        t0 = max([t0] + [e for s_, e in cut if s_ <= t0 + 0.05])
        segs, cur = [], t0
        # cap pauses: word gaps inside the line > 0.22 s at sentence ends, > 0.14 s elsewhere
        wb = [(st[j], en[j], chars[j]) for j in idx]
        for a, b in zip(wb, wb[1:]):
            gap = b[0] - a[1]
            cap = 0.22 if a[2] in ".?!" else 0.14
            if gap > cap + 0.02:
                segs.append((cur, a[1] + cap / 2)); cur = b[0] - cap / 2
        segs.append((cur, t1))
        for s_, e in cut:
            segs = [x for seg in segs for x in ([seg] if e <= seg[0] or s_ >= seg[1] else [(seg[0], s_), (e, seg[1])]) if x[1] - x[0] > 0.03]
        parts = "".join(f"[0:a]atrim={a:.3f}:{b:.3f},asetpts=PTS-STARTPTS[p{n}];" for n, (a, b) in enumerate(segs))
        concat = "".join(f"[p{n}]" for n in range(len(segs))) + f"concat=n={len(segs)}:v=0:a=1,"
        polish = "highpass=f=70,equalizer=f=4000:t=q:w=1:g=2,acompressor=threshold=-20dB:ratio=2:attack=8:release=120,afade=t=in:d=0.015,areverse,afade=t=in:d=0.03,areverse,alimiter=limit=0.7[o]"
        dst = d / f"L{i + 1:02d}.wav"
        ff("-i", str(full), "-filter_complex", parts + concat + polish, "-map", "[o]", "-ar", "48000", "-ac", "1", str(dst))
        dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(dst)], capture_output=True, text=True).stdout)
        out.append({"i": i + 1, "file": str(dst.relative_to(Path(project))), "text": ln["text"], "at": ln["at"], "dur": round(dur, 3),
                    "src": [round(t0, 3), round(t1, 3)], "fillers_cut": len(cut)})
    (d / "lines.json").write_text(json.dumps(out, indent=2))
    print(f"{take}: {len(out)} lines, {sum(o['fillers_cut'] for o in out)} filler cuts, total speech {sum(o['dur'] for o in out):.2f} s -> {d}/lines.json")


KOKORO_VOICES = {
    "af_heart": "American female, warm (default)", "af_bella": "American female, bright", "af_nicole": "American female, soft",
    "af_sarah": "American female, neutral", "am_michael": "American male, steady (default male)", "am_adam": "American male, deep",
    "am_fenrir": "American male, strong", "bf_emma": "British female", "bm_george": "British male",
}


def kokoro_cmd(*args):
    return ["uvx", "--python", "3.12", "--with", "kokoro>=0.9.4", "--with", "soundfile", "--with", "pip",
            "python", "-I", str(HERE / "tts_kokoro.py"), *map(str, args)]


def pick_provider(a):
    p = a.provider
    if p != "auto":
        return p, f"--provider {p}"
    if os.environ.get("ELEVENLABS_API_KEY"):
        return "elevenlabs", "ELEVENLABS_API_KEY is set"
    if shutil.which("uvx"):
        return "kokoro", "no ELEVENLABS_API_KEY; uvx found, running Kokoro-82M locally"
    return "system", "no ELEVENLABS_API_KEY and no uvx for Kokoro; using the OS voice"


def finish_local(project, take, lines, raws, meta):
    """raw per-line audio -> L01.wav (48 kHz mono, same polish as the ElevenLabs path) + lines.json."""
    d = Path(project) / "audio/vo" / take
    out = []
    for i, (ln, raw) in enumerate(zip(lines, raws), 1):
        dst = d / f"L{i:02d}.wav"
        ff("-i", str(raw), "-af", "silenceremove=start_periods=1:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse,"
           "highpass=f=70,acompressor=threshold=-20dB:ratio=2:attack=8:release=120,afade=t=in:d=0.015,areverse,afade=t=in:d=0.03,areverse,alimiter=limit=0.7",
           "-ar", "48000", "-ac", "1", str(dst))
        dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(dst)], capture_output=True, text=True).stdout)
        out.append({"i": i, "file": str(dst.relative_to(Path(project))), "text": ln["text"], "at": ln["at"], "dur": round(dur, 3), "fillers_cut": 0})
    (d / "lines.json").write_text(json.dumps(out, indent=2))
    (d / "take.json").write_text(json.dumps({**meta, "lines": lines}, indent=2))
    print(f"{take}: {len(out)} lines, total speech {sum(o['dur'] for o in out):.2f} s -> {d}/lines.json")


def say_kokoro(a, lines, take):
    voice = a.voice if a.voice in KOKORO_VOICES or re.match(r"^[a-z]{2}_[a-z]+$", a.voice or "") else "af_heart"
    if a.voice and voice != a.voice:
        print(f"voice {a.voice!r} is not a Kokoro id; using {voice}")
    d = Path(a.project) / "audio/vo" / take
    d.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp())
    (tmp / "lines.json").write_text(json.dumps([ln["tts_text"] for ln in lines]))
    print(f"kokoro: voice {voice}, speed {a.speed} (first run downloads ~330 MB of weights)")
    r = subprocess.run(kokoro_cmd(tmp / "lines.json", tmp, voice, a.speed), capture_output=True, text=True)
    raws = [tmp / f"raw{i:02d}.wav" for i in range(1, len(lines) + 1)]
    if r.returncode or not all(x.exists() for x in raws):
        print("kokoro failed:", (r.stderr or r.stdout).strip()[-600:], file=sys.stderr)
        if "espeak" in (r.stderr + r.stdout).lower():
            print("espeak-ng is missing; install it yourself (brew install espeak-ng / apt install espeak-ng)", file=sys.stderr)
        return False
    finish_local(a.project, take, lines, raws, {"provider": "kokoro", "voice": voice, "speed": a.speed})
    shutil.rmtree(tmp, ignore_errors=True)
    return True


def say_system(a, lines, take):
    d = Path(a.project) / "audio/vo" / take
    d.mkdir(parents=True, exist_ok=True)
    tmp = Path(tempfile.mkdtemp())
    raws = []
    for i, ln in enumerate(lines, 1):
        raw = tmp / f"raw{i:02d}.wav"
        if shutil.which("say"):
            aiff = tmp / f"raw{i:02d}.aiff"
            subprocess.run(["say", *(["-v", a.voice] if a.voice else []), "-r", str(int(175 * a.speed)), "-o", str(aiff), ln["tts_text"]], check=True)
            ff("-i", str(aiff), str(raw))
        elif shutil.which("espeak-ng"):
            subprocess.run(["espeak-ng", *(["-v", a.voice] if a.voice else []), "-s", str(int(160 * a.speed)), "-w", str(raw), ln["tts_text"]], check=True)
        else:
            sys.exit("no TTS available: need uvx (Kokoro), macOS say, or espeak-ng")
        raws.append(raw)
    finish_local(a.project, take, lines, raws, {"provider": "system", "voice": a.voice, "speed": a.speed})
    shutil.rmtree(tmp, ignore_errors=True)


def say(a):
    lines = read_script(a.project)
    alias, vcfg = brand_alias(a.project)
    provider, why = pick_provider(a)
    print(f"provider: {provider} ({why})")
    for ln in lines:
        t = ln["text"]
        for k, v in alias.items():
            t = re.sub(rf"\b{re.escape(k)}\b", v, t)
        ln["tts_text"] = t
    if provider != "elevenlabs":
        take = a.take or f"{provider}-{datetime.datetime.now():%H%M%S}"
        if a.dry:
            print("\n".join(ln["tts_text"] for ln in lines)); return
        if provider == "kokoro" and not say_kokoro(a, lines, take):
            print("falling through to the system voice", file=sys.stderr)
            provider = "system"
        if provider == "system":
            say_system(a, lines, take)
        return
    voice = a.voice or vcfg.get("default_voice_id")
    if not voice:
        sys.exit("no --voice and brand.json voice.default_voice_id is empty")
    text = " ".join(ln["tts_text"] for ln in lines)
    est = len(text)
    take = a.take or f"{a.model.split('_')[1]}-{voice[:6]}-{datetime.datetime.now():%H%M%S}"
    print(f"{len(lines)} lines, {est} characters, model {a.model}, voice {voice}, speed {a.speed}, take {take}")
    if a.dry:
        print(text); return
    before = guard(est, f"TTS {take}")
    vs = {"stability": a.stability, "similarity_boost": a.similarity, "use_speaker_boost": True}
    if not a.model.startswith("eleven_v"):
        vs.update(style=a.style, speed=a.speed)
    body = {"text": text, "model_id": a.model, "voice_settings": vs, "apply_text_normalization": "auto"}
    if a.seed is not None:
        body["seed"] = a.seed
    r = call("POST", f"/v1/text-to-speech/{voice}/with-timestamps?output_format=mp3_44100_128", body)
    d = Path(a.project) / "audio/vo" / take
    d.mkdir(parents=True, exist_ok=True)
    (d / "full.mp3").write_bytes(base64.b64decode(r["audio_base64"]))
    cost = ledger(before, f"TTS {Path(a.project).name}/{take} ({a.model}, {est} chars)", est)
    (d / "take.json").write_text(json.dumps({"voice": voice, "model": a.model, "settings": vs, "seed": a.seed, "cost": cost,
                                              "lines": lines, "alignment": r["alignment"]}, indent=2))
    post(a.project, take)


def sfx(a):
    if not os.environ.get("ELEVENLABS_API_KEY"):
        idx = json.loads((HERE / "sfx/INDEX.json").read_text())
        words = set(re.findall(r"[a-z]+", a.prompt.lower()))
        score = lambda n, v: len(words & set(re.findall(r"[a-z]+", f"{n} {v['kind']}".lower())))
        name, v = max(idx.items(), key=lambda kv: score(*kv))
        shutil.copy(HERE / v["file"], a.out)
        print(f"no ELEVENLABS_API_KEY: copied bundled SFX '{name}' ({v['kind']}, {v['dur']} s) -> {a.out}" + ("" if score(name, v) else " (no keyword match, first entry)"))
        return
    est = 200
    before = guard(est, "SFX")
    body = {"text": a.prompt, "prompt_influence": a.influence, "model_id": "eleven_text_to_sound_v2"}
    if a.dur:
        body["duration_seconds"] = a.dur
    Path(a.out).write_bytes(call("POST", "/v1/sound-generation?output_format=mp3_44100_128", body, raw=True))
    ledger(before, f"SFX {Path(a.out).name} ({a.dur or 'auto'} s)", est)


def music(a):
    if not os.environ.get("ELEVENLABS_API_KEY"):
        sys.exit("music generation needs ELEVENLABS_API_KEY. Without one, drop a track into $MOTION_LIBRARY/music (see audio/music.md) and point events.json at it.")
    est = int(round(900 * a.ms / 60000))
    before = guard(est, "music")
    body = {"prompt": a.prompt, "music_length_ms": a.ms, "model_id": "music_v1", "force_instrumental": True}
    Path(a.out).write_bytes(call("POST", "/v1/music?output_format=mp3_44100_128", body, raw=True))
    ledger(before, f"Music {Path(a.out).name} ({a.ms / 1000:g} s)", est)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("budget"); sub.add_parser("voices")
    s = sub.add_parser("say"); s.add_argument("project"); s.add_argument("--provider", choices=["auto", "elevenlabs", "kokoro", "system"], default="auto"); s.add_argument("--voice"); s.add_argument("--model", default="eleven_turbo_v2_5")
    s.add_argument("--speed", type=float, default=1.1); s.add_argument("--stability", type=float, default=0.6)
    s.add_argument("--similarity", type=float, default=0.8); s.add_argument("--style", type=float, default=0.35)
    s.add_argument("--seed", type=int); s.add_argument("--take"); s.add_argument("--dry", action="store_true")
    p = sub.add_parser("post"); p.add_argument("project"); p.add_argument("take")
    x = sub.add_parser("sfx"); x.add_argument("prompt"); x.add_argument("out"); x.add_argument("--dur", type=float); x.add_argument("--influence", type=float, default=0.4)
    m = sub.add_parser("music"); m.add_argument("prompt"); m.add_argument("out"); m.add_argument("--ms", type=int, default=30000)
    a = ap.parse_args()
    if a.cmd == "budget":
        c = cfg(); used, limit, tier = usage()
        job = max(used - c['baseline_character_count'], c.get('local_spent', 0))
        print(f"{tier}: account {used:,}/{limit:,}; job {job:,}/{c['job_cap']:,} spent (counter {used - c['baseline_character_count']:,}, ledger {c.get('local_spent', 0):,}); {c['job_cap'] - job:,} left for this job")
    elif a.cmd == "voices" and not os.environ.get("ELEVENLABS_API_KEY"):
        print("no ELEVENLABS_API_KEY; Kokoro voices (any Kokoro id works, see github.com/hexgrad/kokoro):")
        for k, v in KOKORO_VOICES.items():
            print(f"{k:12s} {v}")
    elif a.cmd == "voices":
        for v in call("GET", "/v1/voices")["voices"]:
            lb = v.get("labels", {})
            print(f"{v['voice_id']}  {v['name'][:28]:28s} {lb.get('gender', ''):7s} {lb.get('age', ''):12s} {lb.get('accent', ''):10s} {v.get('category', '')}")
    elif a.cmd == "say":
        say(a)
    elif a.cmd == "post":
        post(a.project, a.take)
    elif a.cmd == "sfx":
        sfx(a)
    elif a.cmd == "music":
        music(a)


if __name__ == "__main__":
    main()
