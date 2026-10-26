#!/usr/bin/env python3
"""Rebuild audio/sfx/INDEX.json and INDEX.md from the files in audio/sfx/ (onset, peak, dur measured).
usage: uvx --python 3.12 --with numpy python -I build-sfx-index.py
Onset = first 10 ms window above 10% of the max RMS; peak = loudest 10 ms window (same as scripts/peaks.py)."""
import json, re, subprocess
from pathlib import Path
import numpy as np

D = Path(__file__).resolve().parent / "sfx"
KINDS = [  # (kind, regex on name) first match wins
    ("logo hit", r"logo_hit"), ("riser", r"riser"), ("sub boom", r"sub[-_](boom|drop)"),
    ("payment/ka-ching", r"payment|kaching"), ("pen/sign", r"pen[-_]"),
    ("calendar snap", r"calendar_snap|card_set_down"), ("paper slide", r"paper_slide"),
    ("toggle", r"confirm-tap|chime|keys_"), ("tap/press", r"ui_tap|button-press|pop-ui|pop-clean|pop-happy"),
    ("message pop", r"msg_pop|phone_buzz|notif"), ("send/whoosh", r"whoosh|swoosh|sent-"),
]
HELP = {"tap/press": "UI tap, button press", "message pop": "incoming message pop, phone buzz, notification",
        "send/whoosh": "send whoosh, swipe, push/pull", "calendar snap": "calendar block snap, card set down",
        "pen/sign": "pen scribble, signature", "payment/ka-ching": "payment chime, ka-ching",
        "logo hit": "logo hit", "riser": "riser", "sub boom": "sub boom, sub drop", "paper slide": "paper slide",
        "toggle": "toggle, confirm tick, success chime, keys"}

def kind_of(n):
    for k, r in KINDS:
        if re.search(r, n):
            return k
    return "tap/press"

idx = {}
for f in sorted(D.iterdir()):
    if f.suffix not in (".wav", ".mp3"):
        continue
    x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", str(f), "-ac", "1", "-ar", "48000", "-f", "f32le", "-"],
                                     capture_output=True).stdout, np.float32)
    w = 480
    n = len(x) // w * w
    e = np.sqrt((x[:n].reshape(-1, w) ** 2).mean(1))
    on = int(np.argmax(e > 0.1 * e.max())) * w / 48000
    pk = int(np.argmax(e)) * w / 48000
    px = f.name.startswith("px_")
    idx[f.stem] = {"file": f"sfx/{f.name}", "onset": round(on, 3), "peak": round(pk, 3), "dur": round(len(x) / 48000, 3),
                   "kind": kind_of(f.stem), "source": "ElevenLabs sound-effects",
                   "licence": "Pixabay Content License" if px else "ElevenLabs Starter commercial terms"}
(D / "INDEX.json").write_text(json.dumps(idx, indent=1))
md = ["# SFX library", "", "Names resolve through INDEX.json (mix.py `sound`). `align: onset` puts the first audible hit on the cue time, "
      "`align: peak` puts the loudest moment on it. Times in seconds. Licences: ElevenLabs-made = ElevenLabs Starter commercial terms; "
      "Pixabay = Pixabay Content License.", ""]
for k in HELP:
    rows = [(n, v) for n, v in idx.items() if v["kind"] == k]
    md += [f"## {k} ({HELP[k]})", "", "| name | onset | peak | dur | source |", "|---|---|---|---|---|"]
    md += [f"| {n} | {v['onset']:.3f} | {v['peak']:.3f} | {v['dur']:.2f} | {'Pixabay' if v['source']=='Pixabay' else 'ElevenLabs'} |" for n, v in rows]
    md.append("")
(D / "INDEX.md").write_text("\n".join(md))
print(len(idx), "sounds")
