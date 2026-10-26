#!/usr/bin/env python3
"""ElevenLabs voice pipeline with a hard character budget guard.

usage:
  vo.py budget                                   live usage vs the job cap in audio/budget.json
  vo.py voices                                   account voices (name, id, labels, models)
  vo.py say <project> [--voice ID] [--model M] [--speed 1.1] [--stability .6] [--similarity .8]
                      [--style .35] [--seed N] [--take NAME] [--dry]
        one full-script generation of <project>/audio/vo/script.txt via /with-timestamps,
        then split per line, filler + pause cleanup, light polish -> audio/vo/<take>/
  vo.py post <project> <take>                    redo split/cleanup on an existing take (free)
  vo.py sfx "<prompt>" <out.mp3> [--dur 1.0] [--influence .4]
  vo.py music "<prompt>" <out.mp3> [--ms 30000]  Eleven Music, instrumental only

script.txt: one VO line per line; '#' lines and blanks ignored; an optional "@12.5 " prefix gives
the line's start on the film timeline (written to lines.json for mix.py). No ellipses, no dashes,
no audio tags with v2-family models. Defaults (proven 2026-10-17/18): eleven_turbo_v2_5, speed 1.1,
stability 0.6, similarity 0.8, style 0.35, speaker boost, output mp3_44100_128 (Starter max).

Guard: before every paid call the live character_count is read; the call is refused when
(count - baseline) + estimate > job_cap (audio/budget.json). After the call the real cost is
measured from the counter delta and appended to the ledger file. Never buys credits.
Key: macOS Keychain service "elevenlabs-api-key" (never written to disk).
"""
import argparse, base64, datetime, json, os, re, subprocess, sys, urllib.request
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


def say(a):
    lines = read_script(a.project)
    alias, vcfg = brand_alias(a.project)
    voice = a.voice or vcfg.get("default_voice_id")
    if not voice:
        sys.exit("no --voice and brand.json voice.default_voice_id is empty")
    for ln in lines:
        t = ln["text"]
        for k, v in alias.items():
            t = re.sub(rf"\b{re.escape(k)}\b", v, t)
        ln["tts_text"] = t
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
    est = 200
    before = guard(est, "SFX")
    body = {"text": a.prompt, "prompt_influence": a.influence, "model_id": "eleven_text_to_sound_v2"}
    if a.dur:
        body["duration_seconds"] = a.dur
    Path(a.out).write_bytes(call("POST", "/v1/sound-generation?output_format=mp3_44100_128", body, raw=True))
    ledger(before, f"SFX {Path(a.out).name} ({a.dur or 'auto'} s)", est)


def music(a):
    est = int(round(900 * a.ms / 60000))
    before = guard(est, "music")
    body = {"prompt": a.prompt, "music_length_ms": a.ms, "model_id": "music_v1", "force_instrumental": True}
    Path(a.out).write_bytes(call("POST", "/v1/music?output_format=mp3_44100_128", body, raw=True))
    ledger(before, f"Music {Path(a.out).name} ({a.ms / 1000:g} s)", est)


def main():
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("budget"); sub.add_parser("voices")
    s = sub.add_parser("say"); s.add_argument("project"); s.add_argument("--voice"); s.add_argument("--model", default="eleven_turbo_v2_5")
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
