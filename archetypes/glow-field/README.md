# glow-field (A01)

## What it is
A full-frame WebGL glow field: one scalar light field (horizon band, pool, roaming lobe, optional columns and corner lobes) mapped through the brand's 9-stop glow ramp, with a noise warp and a triangular dither (the 8-bit banding of the references is kept). It is the "one world, one light" plate behind glass, type and UI. It never floods: strengths are capped (`fl` <= 0.3, pool/band <= 1) and the default presets stay far from full-frame brightening. Put it on track 0 for the whole film (or per section) and keep the scenes above it transparent.

## Sources (refs + timestamps)
- Glow DesrDGAoX_Q 0.0-14.9 s: molten ramp, horizon band, pool, roaming lobe (the blooms at 1.40, 3.50, 5.90, 8.00, 12.50 were NOT copied as floods; they became the single `bloom-once` swell).
- v2 reel `videos/tidewell-motion-reel-v2-2026-10-20/compositions/glow.html` (shader and monotone-Hermite keyframe table, kept) and `tidewell-motion-reel-2026-10-20/SPEC.md` section 2 (keyframe vocabulary).
- Gradient opener DXzurbATRQT 0.5-1.6 (radial pool rises, mean luminance under 0.15); Premium DcYhz2ZN1vZ 3.3-5.5 (bloom attached to the active element, fast attack, slower decay); Coralarya DeGb1XytuE1 9.7-12.6 (peach horizon under type).

## Duration and easing
Follows the host slot: the proxy tween runs for the host clip's `data-duration` (fallback 600 s) and the field is a pure function of t, so scrubbing is exact. `calm`, `pool-centre` and `horizon` are periodic (8 s loop, sine/cosine only) so any slot length works with no seam. `bloom-once` swell: rise `smoothstep` over 1.0 s, recede over 1.6 s. Start-up fade from black `fadeIn` (default 1.2 s, smoothstep). Nothing pulses on beats.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| preset | string | calm | `calm` (horizon band, pool rising under centre, one roaming lobe) / `bloom-once` (one soft swell, then rest) / `pool-centre` (single pool centred in the safe rect, slow breathing) / `horizon` (band across the lower middle, pool at the foot) |
| keys | string (JSON) | "" | optional keyframe table `[[seconds,{param:value}],...]`; when set it overrides the preset. Params: bandY bandH bandS bandW bandT tilt poolX poolY poolRX poolRY poolS colS colW colL colB lobeT lobeB rlX rlY rlR rlS fl notch rings. Geometry is sticky between keys; strengths default to 0; coordinates are authored for 16x9 and mapped per format. Strengths are capped (fl 0.3) |
| bloomAt | number | 1.6 | `bloom-once`: second of the swell peak |
| intensity | number | 1 | overall strength multiplier (0.3-1.3) |
| fadeIn | number | 1.2 | seconds to rise from black at the start (0 = already lit) |

Colour: `window.BRAND.palette.glowRamp` (hex to vec3 at init), so a brand kit or palette re-themes it with no edit (verified with `demo`, palette tide: blue pool).

## Formats
Key coordinates are in the 16x9 uv frame. For 9x16, 1x1 and 4x5 positions are mapped into the safe rect (`BRAND.format.safe`) and radii are rescaled from the safe rect size, so the pool sits centred inside x 70-940, y 270-1240 in 9x16 instead of being a thin ellipse in the middle of a tall frame. Corner lobes, rings and the roaming lobe use the real aspect ratio. Canvas is W x H of the root (4K is a render-time upscale).

## Flash risk
Low. Default presets: mean sRGB luma 0.14-0.18 (calm, horizon, pool-centre). `bloom-once` peak mean luma 0.29 (16:9) and 0.21 (9:16), which is under the 0.45 limit; one swell, 1.0 s attack, 1.6 s decay, so no more than one luminance event, no flash. Using `keys` with `fl` is the only way to a flood; `fl` is capped at 0.3.

## SFX cues
Background layer, no UI action. Optional: low-swell at `bloomAt - 0.8` for `bloom-once` (soft, no riser or hit).

## Hand-off
First frame: black (the field rises over `fadeIn`). Last frame: a lit field in the preset's resting state; there is no exit, so cut away under a push-through blur or dissolve to the next section's field. To dip to black set `intensity` keys or end the host slot with a scene that covers it.

## Verified
Tidewell 16x9: calm t=2.5 s and 6 s, bloom-once t=0.3, 1, 2, 3, 4.5 s (mean luma 0.008, 0.05, 0.39 before tuning then 0.29, 0.14, 0.06), pool-centre t=4, horizon t=4. 9x16: bloom-once t=1, 2, 3.5 s, calm t=5 (pool centred in the safe rect). 1x1 and 4x5 calm t=5. Demo re-theme (tide) t=5 s. Lint 0 errors. Cream/white core only appears inside the swell peak, over a small area.

Reviewer pass (2026-10-21): contract greps clean; lint 0 errors; 16x9 x3 and 9x16 x2 snapshots checked (legible, lit, inside safe bands, no clipping); 60 fps draft render flashcheck PASS (0 flashes/s, 0 floods).
