# glass-tile-click (A03)

## What it is
"With [tile] Tidewell": a headline where a glass tile pops between two words (the words slide apart), and a glass pointer arrives, rests, presses the tile once with a single ripple ring, then the words leave and the tile glides to the frame centre at 1.5x for the next scene to match. Used to introduce the product name, a partner ("Pay with [Stripe tile] Stripe") or a button press. Font size auto-fits so the finished line fills the safe width; in 9x16, 1x1 and 4x5 the line stacks vertically (before / tile / word) so it stays big.

## Sources (refs + timestamps)
- Glow DesrDGAoX_Q 4.3-5.0: tile pops between two words, back.out(1.6), words pushed apart with a motion-blur ghost, glass pointer from the right, press 0.9, ring ripple, inside a 0.22 s silence.
- CodeRabbit DdcEQPOstOH 3.7-5.5: pointer 0.15 s arrival, 0.5 s decel, press 0.92, ripple 0.2 + 0.2 s.
- Brutalist DeDaXyYoRTG 8.9-9.8 (ring ripple) and Figma DeM5Co3uEul 9.6-11.4 (toggle click).
- v2 reel `compositions/s03-with.html` and `tidewell-motion-reel-2026-10-20/compositions/s03-with.html` (glass tile recipe, pointer path, ghost trail).

## Duration and easing
3.72 s (3.0 s without click, hand-off at 2.9 s). Camera pull-back scale 1.2 to 1 over 3.7 s power2.out with a drift from lower left (2.4 s). Letters expo.out 0.55 s + blur 14 px to 0 over 0.85 s, 0.04 s stagger, "With" at 0.1 s, word at 0.62 s. Tile pop back.out(1.6) 0.6 s at 1.85 s (words slide apart power3.out 0.62 s). Pointer: travel 2.3-2.95 s power3.out on a curve, 0.05 s rest then 0.15 s slide, press at 3.10 s (scale 0.93 in 0.08 s, spring back back.out(2.4)). Ring 0.6 s power2.out at 3.10 s. Hand-off: words blur out 0.24 s at 3.28 s, tile to centre power3.out 0.3 s at 3.40 s. The only overshoot is on the tile and press.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| before | string | With | text before the tile |
| word | string | BRAND.name | text after the tile (runs from light accent to paper) |
| tile | string | logo | `logo` (BRAND.logo.tile) or a BRAND.partners key (whatsapp, stripe, docusign) on a paper plate |
| click | boolean | true | pointer clicks the tile, ripple ring once |
| handoff | boolean | true | words leave, tile grows to the frame centre |

## Formats
- 16x9: one line, centred in the safe rect, font up to 170 px, width up to 1440 px.
- 9x16, 1x1, 4x5: stacked column centred in the safe rect (before, tile 1.3 x font, word), font up to 230 px; pointer comes from the right edge to the tile.
Everything is laid out from BRAND.format.safe; nothing is cropped.

## Flash risk
None. No flood; the sheen across the tile is a small soft band (under 10% of the frame) and the ring is a thin outline at 60% opacity for 0.6 s.

## SFX cues (local time, kind)
- 0.10 s: soft whoosh as the words resolve (optional, quiet).
- 1.85 s: tile pop (glass tick, back.out feel).
- 2.30-2.95 s: pointer glide (very quiet air).
- 3.10 s: pointer press tap with a short glass click (silence dip 0.22 s before it: 2.88-3.10 s).
- 3.28-3.70 s: soft swish as the words leave and the tile settles.
Without click the tap and ring are absent; the only cue is the pop at 1.85 s.

## Hand-off
First frame: nothing (letters at opacity 0, camera at 1.2x). Last frame with handoff: a glass tile (1.5 x the line tile size: about 175 px in 16x9, about 195 px in 9x16) centred on the safe-rect centre, no words, pointer gone. A following scene should start on that tile (match-cut) or the glass slab can rise behind it. With handoff off the finished line stays.

## Verified
Tidewell 16x9 t=0.4, 1.2, 2.3, 2.8, 3.12, 3.3, 3.7, 3.14 s; 9x16 stacked t=1.2, 2.9, 3.14, 3.7 s and a "Pay with / Stripe" partner tile (click off) t=2.9 s; demo re-theme (tide, Tidewell tile) t=3.14 s; lint 0 errors. Note: the "Pay with" space survives because letter spans use `white-space: pre`. The font is measured at 100 px and again on `document.fonts.ready`.

Reviewer pass (2026-10-21): contract greps clean (only white SVG gradient stops, neutral glass); lint 0 errors; 16x9 x3 and 9x16 x2 snapshots checked; 60 fps draft flashcheck PASS (0 flashes/s, 0 floods).
