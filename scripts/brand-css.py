#!/usr/bin/env python3
"""Theme a film project from its brand kit.

usage: brand-css.py <project-dir>

Reads <project>/film.json ({"brand", "palette", "format"}), the brand's brand.json and
formats/presets.json, then rewrites the block between <!-- brand:start --> and
<!-- brand:end --> in <project>/index.html with:
  - @font-face for every font file (in-file, so hyperframes lint is satisfied)
  - :root CSS variables (palette, app tokens, fonts, format size and safe insets)
  - window.BRAND (resolved palette, cast, story, logos, ui, format) for scene scripts
Swapping film.json "brand" or "palette" and re-running re-themes every archetype.
"""
import json, re, sys
from pathlib import Path

SKILL = Path(__file__).resolve().parent.parent


def kebab(k):
    return re.sub(r"([a-z0-9])([A-Z])", r"\1-\2", k).lower()


def main(project):
    project = Path(project)
    film = json.loads((project / "film.json").read_text())
    brand = json.loads((SKILL / "brands" / film["brand"] / "brand.json").read_text())
    fonts = {k: v for k, v in brand["fonts"].items() if isinstance(v, dict)}
    fmt_id = film["format"]
    fmt = json.loads((SKILL / "formats" / "presets.json").read_text())[fmt_id]
    pal_id = film.get("palette") or brand["palettes"]["default"]
    pal = brand["palettes"][pal_id]

    css = [":root {"]
    for k, v in pal.items():
        if k == "glowRamp":
            css += [f"  --glow-{i}: {c};" for i, c in enumerate(v)]
        else:
            css.append(f"  --{kebab(k)}: {v};")
    for k, v in brand.get("app", {}).items():
        if isinstance(v, str) and v.startswith(("#", "rgba", "-")):
            css.append(f"  --app-{kebab(k)}: {v};")
    for role, f in fonts.items():
        css.append(f'  --font-{role}: "{f["family"]}", sans-serif;')
        css.append(f"  --w-{role}: {f.get('weight', 500)};")
        css.append(f"  --track-{role}: {f.get('tracking', '0em')};")
    wm = brand["logo"].get("wordmark")
    if wm:
        css.append(f'  --logo-word-font: var(--font-{wm.get("font", "display")}); --logo-word-weight: {wm.get("weight", 600)}; --logo-word-tracking: {wm.get("tracking", "-0.02em")};')
        css.append(f'  --logo-word-dark: {wm.get("onDark", "#FFFFFF")}; --logo-word-light: {wm.get("onLight", "#000000")};')
    mc = brand["logo"].get("markColors", {})
    for k in ("ink", "reply", "onLightInk", "onLightReply"):
        if k in mc:
            css.append(f"  --logo-{kebab(k)}: {mc[k]};")
    css.append(f"  --fw: {fmt['w']}; --fh: {fmt['h']};")
    for side, px in fmt["safe"].items():
        css.append(f"  --safe-{side}: {px}px;")
    css.append("}")

    faces = []
    for f in fonts.values():
        if f.get("url"):
            faces.append(f'@import url("{f["url"]}");')
        for w, path in f.get("files", {}).items():
            kind = {"woff2": "woff2", "woff": "woff", "ttf": "truetype", "otf": "opentype"}[path.rsplit(".", 1)[1]]
            faces.append(f'@font-face {{ font-family: "{f["family"]}"; src: url("{path}") format("{kind}"); font-weight: {w}; font-display: block; }}')

    data = {
        "id": brand["id"], "name": brand["name"], "tagline": brand["tagline"], "endline": brand.get("endline", ""),
        "url": brand.get("url", ""), "palette": dict(pal, id=pal_id), "app": brand.get("app", {}),
        "logo": brand["logo"], "partners": brand.get("partners", {}), "ui": brand.get("ui", {}),
        "phone": brand.get("phone", {}), "faces": brand.get("faces", {}), "photos": brand.get("photos", {}),
        "cast": brand.get("cast", {}), "story": brand.get("story", {}),
        "format": {"id": fmt_id, "w": fmt["w"], "h": fmt["h"], "safe": fmt["safe"]},
    }
    kit = brand.get("kit", {})
    links = "".join(f'<link rel="stylesheet" href="{c}" />\n' for c in kit.get("css", []))
    scripts = "".join(f'<script src="{j}"></script>\n' for j in ["shared/hf.js", "shared/phone.js", "shared/type.js"] + kit.get("js", []))
    block = (
        "<!-- brand:start -->\n<style>\n" + "\n".join(faces) + "\n" + "\n".join(css) + "\n</style>\n"
        "<script>window.BRAND = " + json.dumps(data, ensure_ascii=False) + ";</script>\n" + links + scripts + "<!-- brand:end -->"
    )
    idx = project / "index.html"
    html = idx.read_text()
    html, n = re.subn(r"<!-- brand:start -->.*?<!-- brand:end -->", lambda m: block, html, flags=re.S)
    if n != 1:
        sys.exit("index.html has no <!-- brand:start --><!-- brand:end --> block")
    html = re.sub(r'data-brand="[^"]*"', f'data-brand="{brand["id"]}"', html)
    idx.write_text(html)
    print(f"themed {project.name}: brand={brand['id']} palette={pal_id} format={fmt_id} ({fmt['w']}x{fmt['h']})")


if __name__ == "__main__":
    main(sys.argv[1])
