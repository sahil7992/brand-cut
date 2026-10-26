#!/usr/bin/env python3
"""safezone.py <video> <format> [--frames 8] [--out sheet.png] [--make-overlays]

Run: uvx --python 3.12 --with numpy --with pillow python -I safezone.py <video> 9x16

Samples frames, composites the platform-UI overlay (unsafe bands tinted + labelled), writes a contact
sheet PNG (default: <video>-safezone.png next to the video), and runs a heuristic: fraction of
strong-edge pixels (Sobel on luminance, magnitude > 0.25 of full scale, i.e. crisp type or UI edges, not
glow gradients) inside each unsafe band. A band over 3 % edge density in a frame counts as text-like detail;
WARN lists the frame times. The soft band (9x16 y 1240..1360) is tinted amber and not checked.
Safe rects come from formats/presets.json (px at the 1080-class canvas, scaled to the video).
exit: 0 PASS, 1 WARN.   --make-overlays writes formats/safe-<fmt>.png (transparent) and exits.
"""
import argparse, json, subprocess, sys
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont

SKILL = Path(__file__).resolve().parent.parent
PRESETS = json.loads((SKILL / "formats" / "presets.json").read_text())
LABELS = {
    "9x16": {"top": "Top bar and account row", "bottom": "Caption, audio row, nav bar", "right": "Actions", "left": ""},
    "4x5": {"top": "Feed header and crop", "bottom": "Feed actions and crop", "right": "Crop", "left": "Crop"},
    "1x1": {"top": "Feed crop", "bottom": "Feed crop", "right": "Crop", "left": "Crop"},
    "16x9": {"top": "Title safe", "bottom": "Title safe", "right": "Safe", "left": "Safe"},
}
TINT = (255, 40, 40, 85)
SOFT = (255, 190, 40, 55)
DENSITY_WARN = 0.03
EDGE_THR = 0.25


def font(size):
    return ImageFont.load_default(size=size)


def bands(fmt, w, h, scale=1.0):
    """name -> (x0, y0, x1, y1) of the unsafe bands, and the safe rect, at canvas px * scale."""
    p = PRESETS[fmt]
    s = p["safe"]
    W, H = p["w"], p["h"]
    t, b, l, r = s["top"], s["bottom"], s["left"], s["right"]
    k = scale
    return ({"top": (0, 0, W * k, t * k), "bottom": (0, (H - b) * k, W * k, H * k),
             "left": (0, t * k, l * k, (H - b) * k), "right": ((W - r) * k, t * k, W * k, (H - b) * k)},
            (l * k, t * k, (W - r) * k, (H - b) * k),
            ((0, (H - b) * k, W * k, p["soft_bottom"] * k) if "soft_bottom" in p else None))


def overlay(fmt, w, h):
    p = PRESETS[fmt]
    k = w / p["w"]
    bd, safe, soft = bands(fmt, w, h, k)
    im = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    d = ImageDraw.Draw(im)
    for name, box in bd.items():
        d.rectangle(box, fill=TINT)
    if soft:
        # soft band: bottom 1240..1360 is allowed for non-essential text, drawn over the bottom tint
        d.rectangle((0, soft[1], w, soft[3]), fill=SOFT)
    d.rectangle(safe, outline=(255, 255, 255, 230), width=max(2, int(3 * k)))
    f = font(max(12, int(26 * k)))
    for name, (x0, y0, x1, y1) in bd.items():
        if (x1 - x0) * (y1 - y0) < 1:
            continue
        txt = LABELS[fmt][name]
        if not txt or (name in ("left", "right") and tw_est(txt, k) > (x1 - x0)):
            continue
        tw = d.textlength(txt, font=f)
        d.text((x0 + (x1 - x0 - tw) / 2 if name in ("top", "bottom") else x0 + 6, (y0 + y1) / 2 - 12 * k if name in ("top", "bottom") else y0 + 20 * k),
               txt, font=f, fill=(255, 255, 255, 235))
    if soft:
        d.text((12, soft[1] + 6), "Soft zone: non-essential text only", font=f, fill=(110, 60, 0, 255))
    return im


def tw_est(txt, k):
    return len(txt) * 15 * k


def make_overlays():
    for fmt in ("9x16", "4x5", "1x1", "16x9"):
        p = PRESETS[fmt]
        overlay(fmt, p["w"], p["h"]).save(SKILL / "formats" / f"safe-{fmt}.png")
        print("wrote", SKILL / "formats" / f"safe-{fmt}.png")


def probe(video):
    o = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height:format=duration",
                        "-of", "json", str(video)], capture_output=True, text=True, check=True).stdout
    j = json.loads(o)
    return j["streams"][0]["width"], j["streams"][0]["height"], float(j["format"]["duration"])


def grab(video, t, w, h):
    r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.3f}", "-i", str(video), "-frames:v", "1", "-vf", f"scale={w}:{h}",
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True)
    if len(r.stdout) < w * h * 3:
        return None
    return Image.frombytes("RGB", (w, h), r.stdout)


def sobel_density(lum, box, thr=EDGE_THR):
    x0, y0, x1, y1 = [int(round(v)) for v in box]
    if x1 - x0 < 3 or y1 - y0 < 3:
        return 0.0
    g = lum
    gx = (g[:-2, 2:] + 2 * g[1:-1, 2:] + g[2:, 2:]) - (g[:-2, :-2] + 2 * g[1:-1, :-2] + g[2:, :-2])
    gy = (g[2:, :-2] + 2 * g[2:, 1:-1] + g[2:, 2:]) - (g[:-2, :-2] + 2 * g[:-2, 1:-1] + g[:-2, 2:])
    mag = np.hypot(gx, gy) / 4.0  # full-scale step = 1.0
    sub = mag[max(0, y0 - 1):max(1, y1 - 1), max(0, x0 - 1):max(1, x1 - 1)]
    return float((sub > thr).mean()) if sub.size else 0.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video", nargs="?")
    ap.add_argument("format", nargs="?")
    ap.add_argument("--frames", type=int, default=8)
    ap.add_argument("--out")
    ap.add_argument("--make-overlays", action="store_true")
    a = ap.parse_args()
    if a.make_overlays:
        return make_overlays() or 0
    if not a.video or a.format not in PRESETS or a.format == "loudness":
        sys.exit("usage: safezone.py <video> <9x16|4x5|1x1|16x9> [--frames 8] [--out sheet.png]")
    video = Path(a.video)
    vw, vh, dur = probe(video)
    AW = 540 if vw <= vh else 960   # analysis width (px) keeps type edges crisp but cheap
    AH = round(AW * vh / vw)
    k = AW / PRESETS[a.format]["w"]
    bd, safe, soft = bands(a.format, AW, AH, k)
    if soft:  # soft band is allowed for non-essential text: check only below it
        bd["bottom"] = (0, soft[3], AW, AH)
    ov = overlay(a.format, AW, AH)
    thumbs, hits = [], {n: [] for n in bd}
    dens_all = {n: [] for n in bd}
    for i in range(a.frames):
        t = (i + 0.5) * dur / a.frames
        im = grab(video, t, AW, AH)
        if im is None:
            continue
        lum = np.asarray(im.convert("L"), np.float32) / 255.0
        for n, box in bd.items():
            den = sobel_density(lum, box)
            dens_all[n].append(den)
            if den > DENSITY_WARN:
                hits[n].append(round(t, 2))
        th = Image.alpha_composite(im.convert("RGBA"), ov).convert("RGB")
        ImageDraw.Draw(th).text((8, 6), f"{t:.2f}s", font=font(max(14, AW // 30)), fill=(255, 255, 0))
        thumbs.append(th)
    if not thumbs:
        sys.exit("no frames decoded")
    cols = 4 if vw <= vh or len(thumbs) < 4 else 4
    cols = min(cols, len(thumbs))
    rows = -(-len(thumbs) // cols)
    sheet = Image.new("RGB", (cols * AW, rows * AH), (20, 20, 20))
    for i, th in enumerate(thumbs):
        sheet.paste(th, ((i % cols) * AW, (i // cols) * AH))
    out = Path(a.out) if a.out else video.with_name(video.stem + "-safezone.png")
    sheet.save(out)
    print("contact sheet:", out)
    warn = False
    for n in bd:
        if not dens_all[n]:
            continue
        mx = max(dens_all[n])
        if hits[n]:
            warn = True
            print(f"WARN band {n}: text-like detail at {hits[n]} s (edge density up to {mx*100:.1f} %, limit {DENSITY_WARN*100:.0f} %)")
        else:
            print(f"ok   band {n}: max edge density {mx*100:.1f} %")
    print("WARN" if warn else "PASS")
    return 1 if warn else 0


if __name__ == "__main__":
    sys.exit(main())
