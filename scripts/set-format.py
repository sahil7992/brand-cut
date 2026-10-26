#!/usr/bin/env python3
"""Switch a film project to another format, in place.

usage: set-format.py <project-dir> <16x9|9x16|1x1|4x5>

Rewrites the canvas size everywhere it is declared (html data-resolution/data-format,
viewport meta, html/body px size, every data-width/data-height in index.html and
compositions/*.html), stores the format in film.json, and re-runs brand-css.py so
--fw/--fh/--safe-* and window.BRAND.format follow. Scenes branch their layout on
html[data-format=...] (CSS) or window.BRAND.format (JS); nothing is cropped.
"""
import json, re, subprocess, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent


def main(project, fmt_id):
    project = Path(project)
    fmt = json.loads((SKILL / "formats" / "presets.json").read_text())[fmt_id]
    W, H = fmt["w"], fmt["h"]
    files = [project / "index.html"] + sorted((project / "compositions").glob("*.html"))
    for f in files:
        s = f.read_text()
        s = re.sub(r'data-width="\d+"', f'data-width="{W}"', s)
        s = re.sub(r'data-height="\d+"', f'data-height="{H}"', s)
        if f.name == "index.html":
            s = re.sub(r'data-resolution="[^"]*"', f'data-resolution="{fmt["resolution"]}"', s)
            s = re.sub(r'data-format="[^"]*"', f'data-format="{fmt_id}"', s)
            s = re.sub(r'content="width=\d+, height=\d+"', f'content="width={W}, height={H}"', s)
            s = re.sub(r"(html,\s*body\s*\{[^}]*?width:\s*)\d+px", rf"\g<1>{W}px", s)
            s = re.sub(r"(html,\s*body\s*\{[^}]*?height:\s*)\d+px", rf"\g<1>{H}px", s)
        f.write_text(s)
    fj = project / "film.json"
    film = json.loads(fj.read_text())
    film["format"] = fmt_id
    fj.write_text(json.dumps(film, indent=2))
    subprocess.run([sys.executable, str(SKILL / "scripts" / "brand-css.py"), str(project)], check=True)
    print(f"format -> {fmt_id} {W}x{H} ({len(files)} files)")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
