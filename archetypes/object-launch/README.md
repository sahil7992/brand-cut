# object-launch (A18)

## What it is
A real object launches out of a send button: the brand app tile in glass (default) or the photoreal phone with a real capture. A glass send button (the app's real send glyph) pops in, a glass pointer arrives, rests, presses; the object rises out of the button from 12 percent to 85 percent of its size in 0.4 s (expo.out, vertical motion blur), a soft impact ring spreads on the ground under it, it breathes during the hold, then leaves with a directional blur upward. Transparent: sits on the film's glow field.

## Sources
- Holo `Deq1nUPMqtr` 13.0-15.3 s (a 3D mascot launches from the send button, scale 12 to 85 percent in 0.4 s, breathing hold, directional blur exit). Study: `STUDY/Deq1nUPMqtr.md`.
- Premium `DcYhz2ZN1vZ` 0.1-1.4 s (object rises expo.out, a cursor hits it, displaced ring and a local wash). Study: `STUDY/DcYhz2ZN1vZ.md`.
- Tidewell has no mascot (a cartoon would read as a toy), so the launched object is the tile (`BRAND.logo.tile`) or `HF.phone`.

## Duration and easing
3.6 s default. 0.05 s button back.out(1.6) pop; pointer 0.55-1.05 s power3.out (fast arrival, long decel), press at 1.17 s (pointer 0.9, button 0.93, 3-4 frames) with a ripple ring 0.45 s; launch 1.2-1.6 s expo.out (scale 0.12 to 0.85, y from the button to the rest point), blur 48 px to 0 over 0.42 s power3.out; phone yaw -22 to -8 deg on power4.out; impact ring 1.5-2.4 s expo.out (scale 0.35 to 1.5, opacity 0.7 to 0); breathing 1.7-3.1 s sine.inOut (scale 0.85 to 0.875 and back, y -8 px); exit 3.1-3.5 s power2.in (blur 0 to 64 px vertical, y -190, scale 1.12, opacity 0).

## Variables
| id | type | default | meaning |
|---|---|---|---|
| object | string | `tile` | `tile` (brand app tile in glass) or `phone` (photoreal phone) |
| ring | boolean | true | soft impact ring under the object on landing |
| screen | string | `home` | `BRAND.ui` key on the phone when object is `phone` |
| fadeOut | boolean | true | directional blur exit at the end |

## Formats
- 16x9: button 150 px at y 905, tile 480 px (phone 820 px high) holding at y 470.
- 9x16: button 190 px at y 1160, tile 620 px (phone 800 px high) holding at y 690, all inside the safe box (x 70-940, y 270-1240).
- 1x1: tile 460 / phone 640; 4x5: tile 520 / phone 760.
Native layouts, never crops.

## Flash risk
Low. No flood. The impact ring is a thin soft ellipse (about 7 percent of the frame at its widest), the button ripple a small ring; nothing above a quarter of the frame. `qa/flashcheck.py` on a 16x9 draft: PASS, 0 flashes, 0 floods.

## SFX cues (local time: sound kind)
- 0.05: soft pop (send button appears)
- 0.55: pointer arrival, near-silent swish
- 1.17: tap (the press) with a small ripple tick
- 1.20: whoosh, rising and short (launch)
- 1.50: soft low thump (object lands, ring spreads)
- 3.10: whoosh upward (exit)

## Hand-off
First frame: empty. Last frame with `fadeOut`: empty. With `fadeOut` false: the object at rest at the centre (scale 0.85), nothing else. The ring/ripple and button are gone by 2.4 s.

## Verified
- `hyperframes lint`: 0 errors, 0 warnings (the button scale overlap warning was fixed by fading the spent button with opacity and y only).
- 16x9 snapshots at 0.5, 0.95, 1.2, 1.3, 1.45, 1.6, 1.75, 2.0, 2.2, 3.2, 3.3 s: button, press, launch blur, landed tile, ring, exit.
- 9x16 at 1.3, 1.75, 2.4 s with tile and with phone: inside the safe box.
- Demo brand re-theme at 1.75 s (blue palette, other tile art): renders, no edits.
- Draft render 16x9 30 fps (3.6 s) OK; flashcheck PASS.
- Reviewer pass 2026-10-21: contract grep clean; lint 0 errors; 16x9 x3 and 9x16 x2 snapshots checked; 60 fps draft flashcheck PASS. Fix: send glyph colour was hardcoded #ffffff, now currentColor with var(--paper).
