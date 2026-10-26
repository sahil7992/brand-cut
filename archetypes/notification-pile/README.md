# notification-pile (A25)

## What it is
The hook: the realtor's problem in one look. A real Pexels plate (woman at a dinner table looking at her phone), graded down about 30%, with real `HF.realui.notif` cards (glass, real faces, SMS/WhatsApp, 9:41 PM style times) stacking with an accelerating stagger while a count chip ticks up. Then each card gets a green answered tick and the chip flips to "all answered".

## Sources (refs + timestamps)
- Our commercial `s01-hook.html` and `s02-flood.html` (real footage plates, real notif cards, count in the real-app chip style).
- Pulse DeOxEFsItr5 0.0-1.9 (count chip 7, 16, 20, 21, 22; geometric decay) and 31.0-33.0 (iOS notification floats in over a graded plate).
- CodeRabbit DdcEQPOstOH 0.0-10.9 (pile-up pressure then calm).
- PATTERNS.md A25.

## Duration and easing
Default 6.8 s (count 6). Cards arrive power3.out 0.45 s (y -70, scale 0.94, blur 10 to 0) at 0.75 then a steady 0.5 s gap (0.75, 1.25, 1.75, 2.25, 2.75, 3.25); a faster 0.42-0.36 s cadence tripped flashcheck (3 sliding-pile flashes in 1 s); older cards slide down one pitch power3.out 0.4 s; the chip number steps up over 0.16 s each. 0.9 s hold, then ticks (back.out(1.8) 0.35 s) every 0.16 s from 4.15 (newest card first), cards dim to 0.82, chip flips at 5.2 (label 0.2 s out, "all answered" 0.3 s in, border tints green). Plate pushes 1.0 to 1.07 over 8 s, linear. Exit blur 10 px 0.5 s (variable `fadeOut`).

## Variables
| id | type | default | meaning |
|---|---|---|---|
| count | number 3-8 | 6 | notifications in the pile |
| messages | string | 8 lead questions, `|` separated | texts, cycled if fewer than count |
| chipLabel | string | new texts | label next to the ticking number |
| doneLabel | string | all answered | label after the tick phase |
| plate | string | assets/footage/dinner-phone.mp4 | footage path via `data-var-src`; the film must copy the file into its `assets/footage/` (source: `~/videos/tidewell-commercial-2026-10-17/comp-v2/src/assets/footage/`, licences in its footage.json, Pexels licence) |
| answer | boolean | true | run the tick phase |
| fadeOut | boolean | true | blur out at the end |

People are `BRAND.cast.leads` then four extra fictional people (Chris Nolan, Devon Cole, Mei Lin, Sam Ortiz) with `BRAND.faces`. The clip starts at source second 1.6 (`data-media-start`); edit the copied scene if another plate needs another in-point.

## Formats
- 16x9: chip left, vertically centred; pile on the right, up to 1.95x zoom, centred in the safe height; ticks sit just outside the right card edge, inside the safe inset.
- 9x16 / 1x1 / 4x5: chip on top at the safe top, pile below it filling the remaining safe height (zoom about 1.5 at count 6, pitch 74 so cards overlap slightly, newest on top); everything within y 270-1240 and x 70-940 in 9:16. The plate is `object-fit: cover`, never letterboxed.

## Flash risk
None. Plate darkened with a top/bottom shade; no flood, no sweeps.

## SFX cues (local time: sound kind), count 6
- 0.75, 1.25, 1.75, 2.25, 2.75, 3.25: notification ping (one per card)
- 4.15, 4.31, 4.47, 4.63, 4.79, 4.95: soft pop (answered ticks)
- 5.26: confirm chime (chip flips to all answered)

## Hand-off
First frame: plate only with the chip fading in. Last frame (fadeOut false): the full pile of ticked cards and the "all answered" chip over the plate; with fadeOut true it blurs to transparent, ready for a push-through into the next scene.

## Verified
Harness `arch-notification-pile` with the plate copied in: lint 0 errors, 0 warnings (video with `data-var-src`, muted, no crossorigin, timing on the video only). Snapshots 16:9 at 0.6, 1.3, 2.0, 3.2, 4.0, 4.8; 9:16 at 3.2, 4.8; demo re-theme at 2.0 (different brand people, mono font, blue chip). Fixed: ticks covered the time stamp (moved outside the card edge, centred). Not checked: other plates (renter-happy etc.); the in-point 1.6 s is tuned for dinner-phone.

Reviewer pass 2026-10-21: contract grep clean, lint 0 errors 0 warnings, snapshots 16:9 x3 and 9:16 x2; fixed ticks overlapping the time stamps (right -34), 9:16 chip drifting to y 256 (drift now +14 to 0 in vertical), hard-coded tick ink (now `B.app.ground`), and a flashcheck FAIL at 2.5 s (4 flashes/s with the 0.18 s cadence; WARN at 0.36 s) by moving to a steady 0.5 s cadence. flashcheck PASS at 16:9 and 9:16 (0 flashes, 0 floods). Plate must still be copied to `assets/footage/dinner-phone.mp4` by the film.
