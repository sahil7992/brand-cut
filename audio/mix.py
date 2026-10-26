#!/usr/bin/env python3
"""mix.py <project> [events.json] [out.wav]: build <project>/audio/mix.wav from <project>/audio/events.json
(or another events file, e.g. audio/events-B.json for a music alternate, written to out.wav).

Run: uvx --python 3.12 --with numpy python -I mix.py <project>

events.json:
  {"music": {"file": "...", "offset": 12.3, "gain_db": -3.5, "fade_in": 0.3, "fade_out": 1.5},
   "vo": {"lines": "audio/vo/<take>/lines.json", "gain_db": 0}  |  {"clips": [{"file": "...", "at": 1.2}]},
   "sfx": [{"t": 1.23, "sound": "msg_pop", "gain_db": -4, "align": "onset"|"peak"}],
   "duck": {"under_vo_db": -8, "under_sfx_db": -4, "attack": 0.15, "release": 0.4},
   "platform": "instagram", "duration": 49.0}
Relative paths resolve against the project dir (music/vo files) or audio/sfx/INDEX.json (sfx names).
Pipeline: decode all to 48 kHz stereo float, music envelope from VO spans + SFX times (10 ms grid, one-pole
attack/release, deterministic), sum, two-pass ffmpeg loudnorm (presets.json loudness), exactly "duration" long.
"""
import json, re, subprocess, sys, tempfile
from pathlib import Path
import numpy as np

SR = 48000
SKILL = Path(__file__).resolve().parent.parent


def decode(path):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ar", str(SR), "-ac", "2", "-f", "f32le", "-"], capture_output=True)
    if r.returncode or not r.stdout:
        sys.exit(f"cannot decode {path}: {r.stderr.decode()[:200]}")
    return np.frombuffer(r.stdout, np.float32).reshape(-1, 2).copy()


def db(x):
    return 10 ** (x / 20)


def resolve(p, project):
    p = Path(p).expanduser()
    return p if p.is_absolute() else project / p


def place(buf, clip, start):
    """add clip into buf starting at `start` seconds (negative start trims the clip head)."""
    s = int(round(start * SR))
    if s < 0:
        clip = clip[-s:]
        s = 0
    n = min(len(clip), len(buf) - s)
    if n > 0:
        buf[s:s + n] += clip[:n]


def smooth(target_db, attack, release, rate):
    """one-pole follower on a dB curve: falls with `attack`, recovers with `release` (time constants in s)."""
    out = np.empty_like(target_db)
    ka = 1 - np.exp(-1 / (max(attack, 1e-3) * rate))
    kr = 1 - np.exp(-1 / (max(release, 1e-3) * rate))
    y = 0.0
    for i, t in enumerate(target_db):
        y += (ka if t < y else kr) * (t - y)
        out[i] = y
    return out


def loudnorm_stats(args_in, filt):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-i", str(args_in), "-af", filt, "-f", "null", "-"], capture_output=True, text=True)
    m = re.search(r"\{[^{}]*\}", r.stderr[r.stderr.rfind("Parsed_loudnorm"):] if "Parsed_loudnorm" in r.stderr else r.stderr, re.S)
    if not m:
        sys.exit("loudnorm pass 1 failed:\n" + r.stderr[-600:])
    return json.loads(m.group(0))


def measure(path):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", str(path), "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True)
    t = r.stderr[r.stderr.rfind("Summary:"):]
    lufs = float(re.search(r"I:\s+(-?[\d.]+) LUFS", t).group(1))
    tp = float(re.search(r"Peak:\s+(-?[\d.]+) dBFS", t).group(1))
    return lufs, tp


def main(project, events=None, outp=None):
    project = Path(project).expanduser().resolve()
    ev = json.loads((Path(events) if events else project / "audio" / "events.json").read_text())
    dur = float(ev["duration"])
    N = int(round(dur * SR))
    target = json.loads((SKILL / "formats" / "presets.json").read_text())["loudness"]
    index = json.loads((SKILL / "audio" / "sfx" / "INDEX.json").read_text())
    duck = {"under_vo_db": -8, "under_sfx_db": -4, "attack": 0.15, "release": 0.4, **ev.get("duck", {})}

    # music
    music = np.zeros((N, 2), np.float32)
    m = ev.get("music")
    if m and m.get("file"):
        clip = decode(resolve(m["file"], project))
        o = int(round(m.get("offset", 0) * SR))
        seg = clip[o:o + N]
        music[:len(seg)] = seg
        g = np.ones(N, np.float32)
        fi, fo = int(m.get("fade_in", 0) * SR), int(m.get("fade_out", 0) * SR)
        if fi:
            g[:fi] = np.linspace(0, 1, fi, dtype=np.float32) ** 2
        if fo:
            g[N - fo:] *= np.linspace(1, 0, fo, dtype=np.float32) ** 2
        music *= g[:, None] * db(m.get("gain_db", 0))
        if len(seg) < N - fo:
            print(f"warning: music ends at {len(seg)/SR:.2f}s before duration {dur}s", file=sys.stderr)

    # vo
    vo = np.zeros((N, 2), np.float32)
    spans = []
    v = ev.get("vo")
    if v:
        if "lines" in v:
            rows = json.loads(resolve(v["lines"], project).read_text())
            items = [(r["file"], r["at"]) for r in rows]
        else:
            items = [(c["file"], c["at"]) for c in v.get("clips", [])]
        vg = db(v.get("gain_db", 0))
        for f, at in items:
            clip = decode(resolve(f, project)) * vg
            place(vo, clip, at)
            spans.append((at, at + len(clip) / SR))

    # sfx
    sfx = np.zeros((N, 2), np.float32)
    cues = []
    for s in ev.get("sfx", []):
        name = s["sound"]
        if name not in index:
            sys.exit(f"unknown sfx '{name}' (see audio/sfx/INDEX.md)")
        e = index[name]
        clip = decode(SKILL / "audio" / e["file"]) * db(s.get("gain_db", 0))
        ref = e["peak"] if s.get("align", "onset") == "peak" else e["onset"]
        place(sfx, clip, s["t"] - ref)
        cues.append((s["t"], s["t"] + min(len(clip) / SR - e["onset"], 0.6)))

    # music ducking envelope on a 10 ms grid
    rate = 100
    tgt = np.zeros(int(dur * rate) + 2)
    for a, b in spans:
        tgt[int(a * rate):int(np.ceil(b * rate)) + 1] = np.minimum(tgt[int(a * rate):int(np.ceil(b * rate)) + 1], duck["under_vo_db"])
    for a, b in cues:
        i, j = max(0, int(a * rate)), int(np.ceil(b * rate)) + 1
        tgt[i:j] = np.minimum(tgt[i:j], duck["under_sfx_db"])
    env_db = smooth(tgt, duck["attack"], duck["release"], rate)
    env = db(np.interp(np.arange(N) / SR, np.arange(len(env_db)) / rate, env_db)).astype(np.float32)
    mix = music * env[:, None] + vo + sfx

    out = Path(outp) if outp else project / "audio" / "mix.wav"
    with tempfile.TemporaryDirectory() as td:
        raw = Path(td) / "pre.f32"
        mix.astype("<f4").tofile(raw)
        pre = Path(td) / "pre.wav"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", str(raw), "-c:a", "pcm_f32le", str(pre)], check=True)
        I, TP = target["integrated_lufs"], target["true_peak_dbtp"]
        st = loudnorm_stats(pre, f"loudnorm=I={I}:TP={TP}:LRA=11:print_format=json")
        filt = (f"loudnorm=I={I}:TP={TP}:LRA=11:measured_I={st['input_i']}:measured_TP={st['input_tp']}:"
                f"measured_LRA={st['input_lra']}:measured_thresh={st['input_thresh']}:offset={st['target_offset']}:linear=true,"
                f"aresample={SR},apad=whole_len={N},atrim=end_sample={N}")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(pre), "-af", filt, "-ar", str(SR), "-ac", "2", "-c:a", "pcm_s16le", str(out)], check=True)
    lufs, tp = measure(out)
    if tp > TP:  # loudnorm can overshoot true peak by ~0.5 dB after 16-bit rounding: trim the excess, loudness stays within 1 LU
        trim = tp - TP + 0.1
        tmp = out.with_suffix(".trim.wav")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(out), "-af", f"volume=-{trim:.2f}dB", "-ar", str(SR), "-c:a", "pcm_s16le", str(tmp)], check=True)
        tmp.replace(out)
        lufs, tp = measure(out)
    d = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(out)], capture_output=True, text=True).stdout)
    print(f"{out}  {d:.3f}s  {lufs:.1f} LUFS integrated  {tp:.1f} dBTP  (target {I} / {TP}, platform {ev.get('platform','-')})")
    if abs(lufs - I) > 1.0 or tp > TP + 0.1:
        print(f"WARN: outside target by more than 1 LU or peak above {TP}", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) not in (2, 3, 4):
        sys.exit(__doc__)
    main(*sys.argv[1:])
