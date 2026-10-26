#!/usr/bin/env python3
"""Calibration tests for flashcheck.py (synthetic 60 fps clips). usage: test_flashcheck.py [workdir]"""
import subprocess, sys, tempfile
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent
W, H, FPS = 960, 540, 60

def write(path, frame_fn, seconds):
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}",
                          "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-crf", "8", "-pix_fmt", "yuv444p", str(path)],
                         stdin=subprocess.PIPE)
    for i in range(int(seconds * FPS)):
        p.stdin.write(np.ascontiguousarray(frame_fn(i / FPS), np.uint8).tobytes())
    p.stdin.close(); p.wait()

def full(v):
    return np.full((H, W, 3), v, np.uint8)

def square(hz, on=255, off=0):
    return lambda t: full(on if int(t * hz * 2) % 2 == 0 else off)

def patch_strobe(hz, frac):
    def f(t):
        fr = full(20)
        if int(t * hz * 2) % 2 == 0:
            ph, pw = int(H * np.sqrt(frac)), int(W * np.sqrt(frac))
            fr[:ph, :pw] = 255
        return fr
    return f

def red(hz):
    def f(t):
        fr = full(0)
        if int(t * hz * 2) % 2 == 0:
            fr[..., 0] = 255
        return fr
    return f

def red_vs_gray(hz):
    def f(t):
        return full(127) if int(t * hz * 2) % 2 else np.tile(np.array([255, 0, 0], np.uint8), (H, W, 1))
    return f

def red_pulse(hz):
    def f(t):
        r = 220 if int(t * hz * 2) % 2 else 160  # luminance step 0.078 (< 0.10), red metric step 75 (> 20)
        return np.tile(np.array([r, 0, 0], np.uint8), (H, W, 1))
    return f

def checker(t):
    i = int(t * FPS)
    y, x = np.mgrid[0:H, 0:W]
    m = (((y // 2) + (x // 2) + i) % 2).astype(np.uint8) * 255
    return np.repeat(m[..., None], 3, -1)

def ease_once(t):
    v = 255 * (0.5 + 0.5 * np.cos(2 * np.pi * min(t, 1.0)))
    return full(int(v))

def floods(times):
    def f(t):
        for t0 in times:
            if t0 <= t <= t0 + 0.6:
                x = np.sin(np.pi * (t - t0) / 0.6)
                return full(int(15 + 225 * x))
        return full(15)
    return f

CASES = [
    ("square-2hz", square(2), 2.0, 2),
    ("square-3hz", square(3), 2.0, 2),
    ("square-4hz", square(4), 2.0, 2),
    ("patch10pct-6hz", patch_strobe(6, 0.10), 2.0, 2),
    ("patch2pct-6hz", patch_strobe(6, 0.02), 2.0, 0),
    ("ease-once", ease_once, 1.5, 0),
    ("red-5hz", red(5), 2.0, 2),
    ("checker-2px", checker, 2.0, 0),
    ("red-vs-gray-5hz", red_vs_gray(5), 2.0, 2),
    ("red-pulse-5hz", red_pulse(5), 2.0, 0),
    ("floods-4s-apart", floods([1.0, 5.0]), 7.0, 2),
    ("floods-9s-apart", floods([1.0, 10.0]), 12.0, 0),
]
# WCAG-only expectations (house flood rule off): (name, want)
WCAG = [("square-2hz", 0), ("square-3hz", 1), ("square-4hz", 2), ("floods-4s-apart", 0), ("red-5hz", 2)]

def main():
    wd = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(tempfile.mkdtemp(prefix="flashcal-"))
    wd.mkdir(parents=True, exist_ok=True)
    bad = 0
    for name, fn, secs, want in CASES:
        clip = wd / f"{name}.mp4"
        write(clip, fn, secs)
        r = subprocess.run([sys.executable, str(HERE / "flashcheck.py"), str(clip)], capture_output=True, text=True)
        ok = r.returncode == want
        bad += not ok
        print(f"{'ok  ' if ok else 'FAIL'} {name:18s} want {['PASS','WARN','FAIL'][want]} got {['PASS','WARN','FAIL'][r.returncode] if r.returncode in (0,1,2) else r.returncode} | {r.stdout.strip().splitlines()[0] if r.stdout.strip() else r.stderr.strip()[-200:]}")
    for name, want in WCAG:
        r = subprocess.run([sys.executable, str(HERE / "flashcheck.py"), str(wd / f"{name}.mp4"), "--wcag-only"], capture_output=True, text=True)
        ok = r.returncode == want
        bad += not ok
        print(f"{'ok  ' if ok else 'FAIL'} wcag:{name:13s} want {['PASS','WARN','FAIL'][want]} got {['PASS','WARN','FAIL'][r.returncode]}")
    print(f"{len(CASES) + len(WCAG) - bad}/{len(CASES) + len(WCAG)} calibration cases pass")
    sys.exit(1 if bad else 0)

if __name__ == "__main__":
    main()
