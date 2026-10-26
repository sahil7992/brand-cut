#!/usr/bin/env python3
"""Merge per-scene SFX cue files into audio/events*.json with film times.

usage: merge-sfx.py <project> [events-file ...]   (default: every audio/events*.json)
Scene builders write audio/sfx/<scene-id>.json = [{"t": <scene-local s>, "sound": <INDEX name>, "gain_db": -6, "note": ...}].
The scene's data-start in index.html is added to each t; the merged list replaces the "sfx" key.
Unknown sound names (not in the skill's audio/sfx/INDEX.json) are reported and skipped.
"""
import json, re, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
p = Path(sys.argv[1])
idx = (p / "index.html").read_text()
starts = {m.group(1): float(m.group(2)) for m in re.finditer(r'<div id="([^"]+)" class="clip"[^>]*?data-start="([\d.]+)"', idx)}
known = json.loads((SKILL / "audio/sfx/INDEX.json").read_text()) if (SKILL / "audio/sfx/INDEX.json").exists() else {}
cues, bad = [], []
for f in sorted((p / "audio/sfx").glob("*.json")):
    sid = f.stem
    if sid not in starts:
        bad.append(f"{f.name}: no scene '{sid}' in index.html"); continue
    for c in json.loads(f.read_text()):
        if known and c["sound"] not in known:
            bad.append(f"{f.name}: unknown sound {c['sound']}"); continue
        cues.append({"t": round(starts[sid] + float(c["t"]), 3), "sound": c["sound"], "gain_db": c.get("gain_db", -6),
                     "align": c.get("align", "onset"), "note": f"{sid}: {c.get('note', '')}"})
cues.sort(key=lambda c: c["t"])
targets = [Path(a) for a in sys.argv[2:]] or sorted((p / "audio").glob("events*.json"))
for t in targets:
    ev = json.loads(t.read_text()); ev["sfx"] = cues; t.write_text(json.dumps(ev, indent=2))
print(f"{len(cues)} SFX cues -> {', '.join(x.name for x in targets)}")
for b in bad:
    print("  skipped:", b)
