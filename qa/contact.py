#!/usr/bin/env python3
"""contact.py <video> <fps> <outprefix>: tiled contact sheets for review.

Run: uvx --python 3.12 --with numpy --with pillow python -I contact.py <video> 2 /tmp/film-sheet
Samples <fps> frames per second, 320 px wide, 6 columns x 5 rows (30 frames) per sheet, time stamp drawn
on each tile with Pillow. Writes <outprefix>-01.png, -02.png ... and prints their paths.
"""
import subprocess, sys
from PIL import Image, ImageDraw, ImageFont

COLS, ROWS, TW, LH = 6, 5, 320, 24


def main(video, fps, prefix):
    o = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height", "-of", "csv=p=0", video],
                       capture_output=True, text=True, check=True).stdout.strip().split(",")
    w, h = int(o[0]), int(o[1])
    th = max(2, round(TW * h / w / 2) * 2)
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", video, "-vf", f"fps={fps},scale={TW}:{th}:flags=area", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                         stdout=subprocess.PIPE)
    font = ImageFont.load_default(size=18)
    n, sheet, outs = 0, None, []
    while True:
        b = p.stdout.read(TW * th * 3)
        if len(b) < TW * th * 3:
            break
        k = n % (COLS * ROWS)
        if k == 0:
            if sheet:
                outs.append(sheet)
            sheet = Image.new("RGB", (COLS * TW, ROWS * (th + LH)), (24, 24, 24))
        im = Image.frombytes("RGB", (TW, th), b)
        x0, y0 = (k % COLS) * TW, (k // COLS) * (th + LH)
        # the time stamp sits in its own strip above the frame: drawn on the frame it hid corner content (2026-10-21)
        ImageDraw.Draw(sheet).text((x0 + 4, y0 + 2), f"{n / fps:.2f}s", font=font, fill=(255, 235, 60))
        sheet.paste(im, (x0, y0 + LH))
        n += 1
    if sheet:
        outs.append(sheet)
    p.wait()
    if not outs:
        sys.exit("no frames decoded")
    for i, s in enumerate(outs, 1):
        path = f"{prefix}-{i:02d}.png"
        s.save(path)
        print(path)
    print(f"{n} frames, {len(outs)} sheet(s)")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(sys.argv[1], float(sys.argv[2]), sys.argv[3])
