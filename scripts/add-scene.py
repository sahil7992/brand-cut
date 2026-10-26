#!/usr/bin/env python3
"""Drop an archetype into a film as a scene.

usage: add-scene.py <project> <archetype> <scene-id> <start> <duration> [--track N] [--vars '{"k":"v"}']

Copies archetypes/<archetype>/scene.html to compositions/<scene-id>.html with every
__ID__ token replaced by the scene id (ids, composition id, timeline key), copies the
archetype's assets/ (if any) to assets/<scene-id>/, and inserts the host clip between
<!-- scenes:start --> and <!-- scenes:end --> in index.html. Extends the root
data-duration when the scene ends past it. Re-adding the same scene id replaces it.
"""
import argparse, json, re, shutil
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent

ap = argparse.ArgumentParser()
ap.add_argument("project"); ap.add_argument("archetype"); ap.add_argument("scene_id")
ap.add_argument("start", type=float); ap.add_argument("duration", type=float)
ap.add_argument("--track", type=int, default=None); ap.add_argument("--vars", default=None)
a = ap.parse_args()

project = Path(a.project)
src = SKILL / "archetypes" / a.archetype
html = (src / "scene.html").read_text().replace("__ID__", a.scene_id)
idx_p = project / "index.html"
idx = idx_p.read_text()
W = re.search(r'id="root"[^>]*data-width="(\d+)"', idx, re.S).group(1)
H = re.search(r'id="root"[^>]*data-height="(\d+)"', idx, re.S).group(1)
html = re.sub(r'data-width="\d+"', f'data-width="{W}"', html)
html = re.sub(r'data-height="\d+"', f'data-height="{H}"', html)
(project / "compositions").mkdir(exist_ok=True)
(project / "compositions" / f"{a.scene_id}.html").write_text(html)
if (src / "assets").is_dir():
    shutil.copytree(src / "assets", project / "assets" / a.scene_id, dirs_exist_ok=True)

idx = re.sub(rf'\n\s*<div id="{re.escape(a.scene_id)}" class="clip"[^>]*></div>', "", idx)
existing = re.findall(r'data-track-index="(\d+)"', idx.split("<!-- scenes:start -->")[1].split("<!-- scenes:end -->")[0])
track = a.track if a.track is not None else (max(map(int, existing)) + 1 if existing else 1)
vv = f" data-variable-values='{json.dumps(json.loads(a.vars), ensure_ascii=False).replace(chr(39), '&#39;')}'" if a.vars else ""
host = (f'      <div id="{a.scene_id}" class="clip" data-composition-id="{a.scene_id}" '
        f'data-composition-src="compositions/{a.scene_id}.html" data-start="{a.start:g}" data-duration="{a.duration:g}" '
        f'data-track-index="{track}" data-width="{W}" data-height="{H}"{vv} style="z-index:{track}"></div>')
idx = idx.replace("<!-- scenes:end -->", host + "\n      <!-- scenes:end -->")
end = a.start + a.duration
m = re.search(r'(id="root"[^>]*data-duration=")([\d.]+)"', idx, re.S)
if end > float(m.group(2)):
    idx = idx[:m.start(2)] + f"{end:g}" + idx[m.end(2):]
idx_p.write_text(idx)
print(f"{a.scene_id} <- {a.archetype} @ {a.start:g}s for {a.duration:g}s, track {track}")
