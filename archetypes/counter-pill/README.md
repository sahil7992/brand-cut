# counter-pill (A30)

## What it is
A glass capsule that enters from beyond the left edge and grows to the right while a concrete number counts up inside it, with a label above ("Texts answered tonight") and a small unit ("of 22"). Behind it a sheaf of 13 thin contour lines sweeps up from the lower left and a soft, capped glow band lies only along the lines. A specular band crosses the capsule when the count locks. Never a bare percentage: the label and the unit make the number a real, countable thing.

## Sources (refs + timestamps)
- Glow DesrDGAoX_Q 11.2-12.5: glass capsule enters from the left with its left end off-frame, number counts with expo decay, contour curves sweep, specular sweep at the end.
- Pulse DeOxEFsItr5 0.0-1.9 (count-up chip, tabular figures) and Brutalist DeDaXyYoRTG 9.8-10.5 (digit rolls).
- v2 reel `tidewell-motion-reel-2026-10-20/compositions/s07-pill.html` (capsule recipe, contour curve family, mask reveal). Changed: the cream core and the yellow band that brightened most of the frame are removed; the band is a blurred strip along the lines at opacity 0.4-0.55.
- PATTERNS A30 fit note: "22 texts tonight, 22 answered", not "100%".

## Duration and easing
3.6 s. Capsule enters x -0.4 W to 0, power3.out 0.7 s with a horizontal motion blur 26 px to 0 (filter removed at 0.72 s). Count and capsule end share one eased value u: power3.out 2.95 s from 0.15 s (geometric decay, the last numbers arrive slowly), tabular figures, number blur-in 0.95 s. Contour lines draw in 1.3 s power2.out, 0.05 s stagger from 1.05 s; band opacity 0 to 0.4 (1.25 s) to 0.55 (2.45-3.85 s). Camera drift scale 1 to 0.97 over 3.6 s. Specular sweep 0.45 s at 3.0 s. Optional blur-out at 3.3 s.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| label | string | Texts answered tonight | concrete label above the number |
| from | number | 0 | count start |
| to | number | 22 | count end |
| suffix | string | "" | appended to the number (k, %) |
| unit | string | of 22 | small text after the number |
| fadeOut | boolean | false | blur out at 3.3 s |
Numbers use `toLocaleString("en-US")` (thousands separators).

## Formats
- 16x9: capsule 270 px high from off-frame left to the safe right edge (1728); label 46 px, number 135 px; centred vertically in the safe rect.
- 9x16: capsule 320 px high ending at x 940, number 160 px, label 51 px, centred in y 270-1240; contours sweep up the right side.
- 1x1 and 4x5: capsule 270 px high inside the safe rect.
Capsule end, number and label are all computed from `BRAND.format.safe`.

## Flash risk
Low. The contour band is local: blurred strip along the lines, max opacity 0.55, the lines are 1.6-2.5 px. Measured mean sRGB luma over the harness (with a pool-centre glow behind): 0.22 (16:9) and 0.16 (9:16) at the end of the count, no frame-to-frame step. The specular sweep covers about 22% of the capsule width.

## SFX cues (local time, kind)
- 0.05 s: whoosh (capsule enters, ends 0.75 s).
- 0.15-2.0 s: soft tick roll (counter ticks, thinning out as the count decays; at most 8 per second, no beat).
- 1.05-2.4 s: very quiet line-draw shimmer.
- 3.00 s: glass sweep (specular pass) with a small lock chime when the count reaches `to`.
Leave 0.2 s of silence before the lock chime (2.8-3.0 s).

## Hand-off
First frame: black or the plate behind (capsule off-frame). Last frame (no fadeOut): the capsule fully extended to the safe right edge with "22 of 22", contour sheaf in place; the next scene can push-through blur or match-cut onto the number. With fadeOut the whole scene blurs and fades from 3.3 s.

## Verified
Tidewell 16x9 t=0.3, 0.9, 1.6, 2.4, 3.3 s; 9x16 t=0.7, 3.3 s; 1x1 t=3.3 s; demo re-theme (tide, label "Patient calls answered today", to 14, unit "of 14") t=3.3 s; mean luma measured as above; lint 0 errors. Over the demo palette the text stays legible (white on blue glass).

Reviewer pass (2026-10-21): flashcheck WARN (3 flashes/s over 27% at 1.33 s: crisp text sliding with the capsule edge) fixed by speed-proportional horizontal motion blur on the pill group (filter now held until 3.1 s, removed at the lock); re-run flashcheck PASS (0 flashes/s, 0 floods); lint 0 errors; 16x9 and 9x16 snapshots checked.
