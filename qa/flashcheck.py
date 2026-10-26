#!/usr/bin/env python3
"""flashcheck: photosensitivity gate for rendered films (WCAG 2.2 SC 2.3.1 + house rules).

usage: flashcheck.py <video> [--json out.json] [--flood-gap 8] [--wcag-only]
exit:  0 PASS, 1 WARN, 2 FAIL

Conservative approximation, not a certified Harding/PEAT replacement. Thresholds
(research/flash.md, WCAG 2.2 glossary https://www.w3.org/TR/WCAG22/#dfn-general-flash-and-red-flash-thresholds):
  general flash  = a pair of opposing changes in relative luminance >= 0.10 where the darker state < 0.80
  red flash      = opposing transitions of saturated red, R/(R+G+B) >= 0.8, change in (R-G-B)x320 > 20
                   AND a CIE 1976 u'v' distance > 0.2 between the states (WCAG 2.2 wording)
  area           = flashing pixels >= 25% of the whole frame, or >= 25% of any 1/3 W x 1/3 H window
                   (WCAG's 341x256-at-1024x768 10-degree field)
  count          = FAIL when more than 3 flashes in any 1 s over that area; WARN at exactly 3
  house flood    = >= 25% of the frame jumps >= 0.10 in luminance and comes back within 2 s;
                   FAIL when two floods start less than --flood-gap seconds apart (default 8)
Per-pixel transitions use hysteresis (a direction counts once L has moved >= 0.10 from the last
extreme), flashes = transitions // 2 per 1 s window; luminance is computed in linear light and
2x2-pooled, so balanced fine patterns average out; every native frame is analysed (60 fps kept).
"""
import argparse, json, subprocess, sys
import numpy as np

def probe(path):
    out = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                          "stream=width,height,r_frame_rate", "-of", "csv=p=0", path],
                         capture_output=True, text=True, check=True).stdout.strip().split(",")
    w, h = int(out[0]), int(out[1]); n, d = out[2].split("/")
    return w, h, float(n) / float(d)

def analysis_size(w, h):
    s = 135 / min(w, h)
    return max(2, int(round(w * s / 2)) * 2), max(2, int(round(h * s / 2)) * 2)

def pool2(a):
    return 0.25 * (a[0::2, 0::2] + a[1::2, 0::2] + a[0::2, 1::2] + a[1::2, 1::2])

def frames(path, W, H):
    p = subprocess.Popen(["ffmpeg", "-v", "error", "-i", path, "-vf", f"scale={W}:{H}:flags=area,format=rgb24",
                          "-f", "rawvideo", "-"], stdout=subprocess.PIPE)
    n = W * H * 3
    while True:
        b = p.stdout.read(n)
        if len(b) < n:
            break
        yield np.frombuffer(b, np.uint8).reshape(H, W, 3)
    p.wait()

def rel_lum(rgb):
    c = rgb.astype(np.float32) / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]

def uv_chroma(rgb):
    """CIE 1976 u'v' per pixel from linear sRGB (near-black pixels take the D65 white point)."""
    c = rgb.astype(np.float32) / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    X = 0.4124 * c[..., 0] + 0.3576 * c[..., 1] + 0.1805 * c[..., 2]
    Y = 0.2126 * c[..., 0] + 0.7152 * c[..., 1] + 0.0722 * c[..., 2]
    Z = 0.0193 * c[..., 0] + 0.1192 * c[..., 1] + 0.9505 * c[..., 2]
    d = X + 15 * Y + 3 * Z
    dark = Y < 0.005
    u = np.where(dark, 0.1978, 4 * X / np.maximum(d, 1e-6)); v = np.where(dark, 0.4683, 9 * Y / np.maximum(d, 1e-6))
    return np.stack([u, v], -1).astype(np.float32)

def red_metric(rgb):
    c = rgb.astype(np.float32) / 255.0
    s = c.sum(-1)
    sat = (c[..., 0] / np.maximum(s, 1e-6) >= 0.8) & (s > 0.05)
    return np.where(sat, np.maximum(0.0, (c[..., 0] - c[..., 1] - c[..., 2]) * 320.0), 0.0).astype(np.float32)

class RedHysteresis:
    """WCAG 2.2 red flash: a transition of the saturated-red metric ((R-G-B)x320 change > 20, R/(R+G+B) >= 0.8)
    that ALSO moves more than 0.2 in CIE 1976 u'v' between the two states. A brightness pulse inside one red hue
    is not a red flash (the general luminance rule still covers it)."""
    def __init__(self, thr=20.0, uv=0.2):
        self.h, self.uv, self.ext_uv = Hysteresis(thr), uv, None
    def step(self, x, uvc):
        if self.ext_uv is None:
            self.ext_uv = uvc.copy()
        before_dir = None if self.h.dir is None else self.h.dir.copy()
        t = self.h.step(x)
        if before_dir is None:
            return t
        moved = np.linalg.norm(uvc - self.ext_uv, axis=-1) > self.uv
        turned = self.h.dir != before_dir
        self.ext_uv = np.where(turned[..., None], uvc, self.ext_uv)
        return t & moved

class Hysteresis:
    """Per-pixel transition detector: a transition is confirmed when the value moves >= thr from the
    last extreme in the opposite direction (Schmitt trigger). Two transitions = one flash."""
    def __init__(self, thr, dark_gate=None):
        self.thr, self.gate, self.ext, self.dir = thr, dark_gate, None, None
    def step(self, x):
        if self.ext is None:
            self.ext = x.copy(); self.dir = np.zeros(x.shape, np.int8)
            return np.zeros(x.shape, bool)
        up = ((x - self.ext) >= self.thr) & (self.dir != 1)
        down = ((self.ext - x) >= self.thr) & (self.dir != -1)
        trans = up | down
        counted = trans if self.gate is None else trans & (np.minimum(x, self.ext) < self.gate)
        self.dir = np.where(up, 1, np.where(down, -1, self.dir)).astype(np.int8)
        self.ext = np.where(trans, x, np.where(self.dir == 1, np.maximum(self.ext, x),
                            np.where(self.dir == -1, np.minimum(self.ext, x), self.ext)))
        return counted

def box_max_frac(mask, wh, ww):
    """Max fraction of True pixels over every wh x ww window (stride 1, integral image)."""
    ii = np.pad(mask.astype(np.int32).cumsum(0).cumsum(1), ((1, 0), (1, 0)))
    s = ii[wh:, ww:] - ii[:-wh, ww:] - ii[wh:, :-ww] + ii[:-wh, :-ww]
    return float(s.max()) / (wh * ww)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video"); ap.add_argument("--json")
    ap.add_argument("--flood-gap", type=float, default=8.0)
    ap.add_argument("--wcag-only", action="store_true", help="skip the house flood rule")
    a = ap.parse_args()
    w, h, fps = probe(a.video)
    W, H = analysis_size(w, h)
    win_h, win_w = max(1, H // 3), max(1, W // 3)
    F = int(round(fps))
    k = max(1, int(round(0.25 * fps)))
    lum_h, red_h = Hysteresis(0.10, dark_gate=0.80), RedHysteresis()
    ring_l = np.zeros((F, H, W), np.uint8); ring_r = np.zeros((F, H, W), np.uint8)
    cnt_l = np.zeros((H, W), np.int32); cnt_r = np.zeros((H, W), np.int32)
    lhist = []
    worst = {"t": 0.0, "count": 0, "area": 0.0, "kind": "general"}
    per_sec = []
    up_on = dn_on = False; onsets = []
    i = -1
    for i, rgb in enumerate(frames(a.video, 2 * W, 2 * H)):
        L = pool2(rel_lum(rgb))
        R = pool2(red_metric(rgb))
        UV = uv_chroma(rgb)
        UV = 0.25 * (UV[0::2, 0::2] + UV[1::2, 0::2] + UV[0::2, 1::2] + UV[1::2, 1::2])
        for ring, cnt, det, x in ((ring_l, cnt_l, lum_h, L), (ring_r, cnt_r, red_h, None)):
            new = (det.step(x) if x is not None else det.step(R, UV)).astype(np.uint8)
            cnt += new.astype(np.int32) - ring[i % F]
            ring[i % F] = new
        for kind, cnt in (("general", cnt_l), ("red", cnt_r)):
            for c in (4, 3):
                m = (cnt // 2) >= c
                area = max(float(m.mean()), box_max_frac(m, win_h, win_w))
                if area >= 0.25:
                    if c > worst["count"] or (c == worst["count"] and area > worst["area"]):
                        worst = {"t": round(i / fps, 3), "count": int(c), "area": round(area, 3), "kind": kind}
                    break
        # whole-frame flashes per second, for the report
        lhist.append(L)
        if len(lhist) > k:
            past = lhist.pop(0)
            up_frac = float(((L - past) >= 0.10).mean()); dn_frac = float(((past - L) >= 0.10).mean())
            if not up_on and up_frac >= 0.25: up_on = True; onsets.append(("up", i / fps))
            if up_on and up_frac < 0.10: up_on = False
            if not dn_on and dn_frac >= 0.25: dn_on = True; onsets.append(("down", i / fps))
            if dn_on and dn_frac < 0.10: dn_on = False
    n_frames = i + 1
    if n_frames <= 0:
        sys.exit("no frames decoded")
    floods, j = [], 0
    while j < len(onsets):
        d, t = onsets[j]
        back = next((m for m in range(j + 1, len(onsets)) if onsets[m][0] != d and onsets[m][1] - t <= 2.0), None)
        if back is None:
            j += 1
        else:
            floods.append(round(t, 3)); j = back + 1
    gaps = [round(b - a_, 2) for a_, b in zip(floods, floods[1:])]
    big_changes = len(onsets)
    status, reasons = "PASS", []
    if worst["count"] >= 4:
        status = "FAIL"; reasons.append(f"{worst['kind']} flashes > 3 in 1 s over {worst['area']*100:.0f}% area at {worst['t']} s")
    elif worst["count"] == 3:
        status = "WARN"; reasons.append(f"{worst['kind']} flashes = 3 in 1 s over {worst['area']*100:.0f}% area at {worst['t']} s (limit is more than 3)")
    close = [(floods[j], floods[j + 1]) for j in range(len(floods) - 1) if floods[j + 1] - floods[j] < a.flood_gap]
    if close and not a.wcag_only:
        status = "FAIL"; reasons.append(f"floods closer than {a.flood_gap:g} s: {close}")
    rep = {"file": a.video, "size": [w, h], "fps": round(fps, 3), "frames": n_frames, "analysis": [W, H],
           "status": status, "reasons": reasons, "worst": worst, "floods": floods, "flood_gaps": gaps,
           "large_area_changes": big_changes}
    if a.json:
        open(a.json, "w").write(json.dumps(rep, indent=2))
    print(f"flashcheck {status}: worst {worst['count']} {worst['kind']} flash(es)/s over {worst['area']*100:.0f}% at {worst['t']} s; "
          f"floods {len(floods)} at {floods}; large-area changes {big_changes}")
    for r in reasons:
        print("  -", r)
    sys.exit({"PASS": 0, "WARN": 1, "FAIL": 2}[status])

if __name__ == "__main__":
    main()
