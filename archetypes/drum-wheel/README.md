# drum-wheel (A10)

## What it is
A static lead word ("Tidewell") beside a 3D drum of what the product does. The wheel rolls in, snaps row by row, then spins up and lands on the last item with a bullet on the focus line. One value, `wheelPos`, drives every row: rotateX, translateZ, translateY, opacity (depth fog), scale, skew and motion blur all come from the row's distance to the focus line. Rows wrap around, so the spin passes items again.

## Sources
- SDS DYrpr7iztRy 7.0-12.6 s: rows on a cylinder tilted about -10 deg, focus row at exactly 50% height, 0.1 s expo snaps then accelerando spin; the full stop becomes the bullet (7.0-8.0 s).
- Holo Deq1nUPMqtr 26.2-28.6 s: masked list, active row dark with a dot, 0.3-0.4 s steps.

## Duration and easing
Default 6.0 s (4 items, hold 0.6, fadeOut): roll-in 0.05-1.05 expo.out from 3 rows away; snaps 0.3 s expo.out at 1.5 and 2.33; spin 3.08-4.03 power2.in, final snap 4.03-4.38 expo.out (speeds match at the join, about 24 rows/s); read hold to 5.48; blur out 5.48-5.98. Holds shrink 12% per step (accelerando). Perspective 1500 px, 18 deg per row, drum radius from the row pitch. Camera drift scale 1 to 1.04.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| lead | string | "" (brand name) | Static word left of the wheel (above it in 9:16, 1:1, 4:5) |
| items | string | answers every lead\|books the showing\|sends the application\|collects the fee | Wheel rows; the wheel lands on the last one |
| hold | number | 0.6 | Seconds the focus row holds between snaps |
| fadeOut | boolean | true | Blur out at the end |
The ring is padded to a multiple of the item count (12 rows for 4 items) so the wrap never shows a duplicate in view.

## Formats
- 16x9: lead and wheel on one line, block centred in the safe rect, font up to 104 px (fitted so the longest item fits), tilt -5 deg.
- 9x16, 1x1, 4x5: lead stacked at the top-left of the safe rect at 1.7x, wheel below, left aligned at x 70 (9:16 right edge 940), font up to 84 px, tilt -2.5 deg. Faint rows (below 10% opacity) can extend toward the edge of the safe rect; all readable rows stay inside it.

## Flash risk
None. No luminance flashes; the bullet shrinks to a speck on each snap (scale only).

## SFX cues (local time, sound kind)
- 1.50 and 2.33: click (one soft detent per snap, 2 dB louder on the second).
- 3.08-4.03: rising ratchet or whoosh under the spin (accelerating clicks).
- 4.03: landing thud with a short click; bullet regrows 4.2.
- 0.05: soft whoosh for the roll-in (optional).

## Hand-off
First frame: empty. Last frame (fadeOut false, t=5.5): lead word and the final item "collects the fee" on the focus line with the bullet, faint neighbours above and below. With fadeOut it ends blurred and transparent.

## Verified
Lint 0 errors. 16x9 snapshots at 0.5, 1.2, 2.0, 3.5, 4.0, 5.2 s (roll-in, snaps, spin blur, landing); 9x16 at 2.0 and 4.9 s; demo brand re-theme at 2.0 s (name Tidewell, its font and accent bullet). Focus row sits on the exact vertical centre; no clipped text; nothing under the 9:16 insets.

Reviewed 2026-10-21: contract grep clean; lint 0 errors; 16x9 at 2.0/3.6/5.0 and 9x16 at 2.0/4.9 fine (focus row centred, no clipped text, 9:16 inside the safe rect). flashcheck on the 60 fps draft first WARNed (3 flashes/s over 31% at 4.25 s: bright rows streaming past during the fast spin); fixed by dimming row opacity to 28% while the wheel moves faster than about 5-11 rows/s (smoothstep on |vel|), so snaps and the landing are untouched; now flashcheck PASS (0 flashes).
