# icon-ring (A20)

## What it is
Real app and partner tiles (Tidewell tile, SMS bubble tile in app style, calendar tile, WhatsApp, DocuSign, Stripe) in a glossy glass finish ride an ellipse with contact shadows and ease-out rotation until the chosen tile stops at the front. Then one hand-drawn pen loop (two overlaid strokes, drawn on twos) circles it, the tile catches an accent rim, and a short handwritten note types underneath. Never pixel-art toys, never drawn houses, only real marks.

## Sources
- Change DeKZK_ZNbUN 0.9-2.0 s (pen strokes with pressure, signature, circle round a word, drawn on) and 6.6-8.3 s (11 glossy sprites on an ellipse with contact shadows, ease-out rotation, strokes hitting icons with an accent burst).
- Matheus DdUFf0FO7Cr (animation on twos for drawn elements).

## Duration and easing
Default 5.2 s. Tiles pop in at 0.05 + 0.07 i (back.out 1.5, 0.5 s) while the ring spins 140 deg with power3.out from 0.1 to 2.0 s; depth drives scale (0.7 back to 1.25 front), opacity and fog; motion blur follows rotation speed. Pen: power2.out over 0.85 s from 2.05 s, quantised to 12 fps (Math.floor(t*12)/12); the thin stroke starts 0.08 s after the thick one. Contact at 2.85: chosen tile scale +6% back.out(1.6), accent rim fades in, other tiles dim. Note types 2.8 to about 4.0 with irregular gaps (seeded). Hold, blur out 4.7-5.2.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| icons | string | sms\|whatsapp\|calendar\|mark\|docusign\|stripe | Tiles in ring order. Keys: mark (brand tile), sms, calendar, or any BRAND.partners key; unknown keys are skipped |
| circle | number | 3 | 0-based index of the tile that ends in front and gets circled (clamped) |
| note | string | Replies in seconds | Handwritten label under the circle, set in the display face (not a script font) |
| fadeOut | boolean | true | Blur out at the end |

## Formats
- 16x9: tile 270 px, ellipse 190 px high, front tile 337 px, note 56 px.
- 9x16: tile 220, ellipse 230 high, ring width limited to the safe width (x 70-940); everything between y 290 and y 1230.
- 1x1: tile 205, ellipse 170 high, centred inside the 810 px width. 4x5: tile 215, ellipse 210 high.
The ring group is vertically centred in the safe rect from the computed extents (back tiles to note).

## Flash risk
None. The accent rim is an inner edge, not a flood; no luminance steps.

## SFX cues (local time, sound kind)
- 0.05-0.5: soft tile pops (one light pop per tile, rising pitch).
- 0.1-2.0: smooth whoosh that decays with the spin.
- 2.05-2.9: pen scratch (paper-and-pen, 12 fps stutter in the grain), peaking 2.3.
- 2.85: soft knock on the tile (rim catches).
- 2.8-4.0: very light pen ticks for the note (optional, one per 3 letters).

## Hand-off
First frame empty. Last frame (fadeOut false, t=4.7): circled Tidewell tile at the front, others dimmed, the note complete under the circle. With fadeOut the scene ends blurred and transparent.

## Verified
Lint 0 errors. 16x9 at 0.5, 0.9, 1.2, 2.4, 2.9, 3.6, 4.4 s; 9x16, 1x1, 4x5 at 3.6 s and 9x16 at 4.4 s; the pen svg viewBox follows the canvas. Demo brand re-theme at 4.4 s (its tile, accent-coloured pen, its fonts; partner keys the demo brand lacks are skipped or render a plain tile if the file is missing).

Reviewed 2026-10-21: contract grep clean (no brand literals, no Math.random/Date, no uppercase/italic/emoji); lint 0 errors; 16x9 at 1.2/1.5/3.0/4.4 and 9x16 at 3.0/4.4 inside the safe rect, no clipped text. flashcheck on the 60 fps draft first FAILED (4 flashes/s over 32% at 1.2 s: six bright tiles sweeping through a 230 deg spin); fixed by cutting the spin to 140 deg (same timing); now flashcheck PASS (0 flashes). Note: spin is 140 deg, not 230 as written under Duration.
