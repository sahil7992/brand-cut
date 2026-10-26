#!/usr/bin/env python3
"""Re-theme a film project to another brand kit or palette.

usage: set-brand.py <project-dir> <brand> [palette]
Copies brands/<brand>/assets into the project (same standard paths), stores the brand
and palette in film.json and re-runs brand-css.py. Scenes need no edits.
"""
import json, shutil, subprocess, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent
project, brand = Path(sys.argv[1]), sys.argv[2]
palette = sys.argv[3] if len(sys.argv) > 3 else None
shutil.copytree(SKILL / "brands" / brand / "assets", project / "assets", dirs_exist_ok=True)
(project / "shared").mkdir(exist_ok=True)
kit = SKILL / "brands" / brand / "kit"
kit = kit if kit.is_dir() else SKILL / "shared" / "uikit"
for f in list((SKILL / "shared").glob("*.js")) + list(kit.glob("*")):
    shutil.copy(f, project / "shared" / f.name)
fj = project / "film.json"
film = json.loads(fj.read_text())
film.update(brand=brand, palette=palette)
fj.write_text(json.dumps(film, indent=2))
subprocess.run([sys.executable, str(SKILL / "scripts" / "brand-css.py"), str(project)], check=True)
