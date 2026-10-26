# checklist-fix (A15)

## What it is
Proof of follow-through. A rental application checklist card floats on a glass slab over a real, softly defocused photo plate. Rows: Application sent, Viewed, Signed, Fee requested, Paid. The first rows tick off, one row goes amber with a slow spinner and "Waiting on signature", then flips to green with a tick draw while the real application row in the header changes Waiting to Signed and a DocuSign status chip steps Sent, Delivered, Viewed, Signed. Fee requested then ticks; Paid stays open (hand-off to stripe-paid).

## Sources
- OpenAI Dcn6EINyzaa 15.5-21.0 (STUDY/Dcn6EINyzaa.md, shots 14-15): floating window over a misty photo with a slow drift, window rises with a power4 curve (top edge 77 to 23 percent in 16 frames, no overshoot), green gradient bars slide behind rows, one row turns the error colour then is fixed. Adapted: not code; the amber row is the "error", the fix is the signature; the wash is a local row bar (under 25% of the frame), no red flood, no glyph scramble.
- Blackbox DdCmsxptRdM 4.4-4.9 (speed-ramp stretch) informs the quick rise.
- Real UI: `RU.application` (the header row, both states), app tokens for rows (`--app-green`, `--app-amber`, `--app-raised`, `--app-hair`).

## Duration and easing
5.0 s. Slab rise power4.out 0.9 s with blur 12 px to 0; rows stagger 0.1 s power3.out 0.5 s; tick draw power2.out 0.3 s; marker pop back.out(1.6) (small living object); wash bars expo.out 0.7 s; chip expo.out 0.6 s and label swaps 0.3 s; plate drift scale 1.1 to 1.0 over the whole scene (sine.out); optional blur-out 0.45 s.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| rows | string | Application sent\|Viewed\|Signed\|Fee requested\|Paid | row labels, | separated (4 to 6 rows) |
| times | string | 11:20 AM\|11:26 AM\|11:38 AM\|11:42 AM\|11:44 AM | one time per row; matches the stripe-paid receipt (requested 11:42, paid 11:44) |
| fixRow | number | 2 | 0-based row that waits then flips (1 to 3) |
| waiting | string | Waiting on signature | text on the waiting row |
| signer | string | "" (first BRAND.cast lead) | applicant in the header row |
| photo | string | "" (BRAND.photos.hero) | project-relative plate image |
| fadeOut | boolean | true | blur out at 4.55 s |

## Formats
- 16x9: slab scaled to the frame height; chip hangs off the top-right corner (1.35x).
- 9x16 / 4x5 / 1x1: slab scaled to the safe width (x 70-940) and height; chip centred on the top edge, inside y 270. The plate is cover-fitted, so portrait shows the house itself, not a crop of a landscape layout.

## Flash risk
None. No flood; the amber and green washes are row-sized bars (about 6% of the frame) that ramp over 0.7 s; the plate is dimmed (brightness .55) and steady.

## SFX cues (local time: kind)
- 0.10: soft whoosh (slab rises)
- 0.65: faint UI tick (chip appears); 0.85 / 1.25 / 1.65: status ticks (Sent, Delivered, Viewed)
- 0.95: tick pop (Application sent); 1.75: tick pop (Viewed)
- 1.85: low hold tone, quiet (the row goes amber and the spinner starts)
- 3.05: signed chime (row flips green, chip locks to Signed, header says Signed); 3.15 tick draw
- 3.65: tick pop (Fee requested)

## Hand-off
First frame: dark plate, nothing else. Last frame (fadeOut false, 5.0 s): card with four green rows and an open Paid row, Signed chip on the corner. The next scene (stripe-paid) can open on the Paid row: the receipt slab rises from the same spot.

## Verified
Lint 0 errors. Snapshots 16x9 at 0.6/1.6/2.8/3.4/4.4 s and 9x16 at 2.8/4.4 s: card, chip and plate inside safe insets, rows legible at full size, spinner visible at 2.8 s, flip complete at 4.4 s. Demo brand (Tidewell): palette, fonts, signer, wash colours re-theme; the demo brand has no photo plate (renders dark) and no DocuSign mark (the chip shows a document glyph). Limits: the checklist rows are archetype-owned (no such screen exists in the app) but built from app tokens and the real application row.
- Reviewer pass 2026-10-21: lint 0 errors; 16x9 and 9x16 snapshots plus 4x5 and 1x1 at 3.9 s; 60 fps draft renders in 16x9 and 9x16 pass flashcheck (0 flashes/s, 0 floods) and safezone PASS. Fixed: 9x16 slab edge reached x 949 with the camera drift, scaled to 0.94 in vertical; preview.png regenerated.
