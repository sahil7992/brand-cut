# docusign-sign (A26)

## What it is
A realistic rental application page rises on a paper-lit glass slab. A DocuSign status chip steps Sent, Delivered, Viewed (the real DocuSign statuses), the yellow Sign tag points at the signature box, the applicant's signature draws on (variable speed, 0.8 s), the date fills, and the chip locks to Signed with a tick. Landscape adds a four-node status track under the chip. Copy says "Rental application"; never "lease".

## Sources
- Our v2 s09-sign (`videos/tidewell-motion-reel-v2-2026-10-20/compositions/s09-sign.html`): paper construction, 3-phase signature mask path (the Jordan Tate path is reused), tick draw; commercial s09-application.
- Wise 15.0-17.7 (glossy card tilt and pull-back, used for the page's rise from y +520 with rotateX 34): PATTERNS A26; Change 0.9-2.0 (pressure pen stroke, the variable-speed signature).
- Real DocuSign statuses from `BRAND.truths`: Sent, Delivered, Viewed, Signed.

## Duration and easing
4.6 s. Page rise power4.out 1.15 s with blur 16 px to 0 and a slow sine settle; chip expo.out 0.6 s; status label swaps power3.out 0.35 s in, power2.in 0.25 s out; Sign tag back.out(1.6) 0.4 s (small living object); signature 0.8 s as power1.in 0.3 + sine.inOut 0.36 + power2.out 0.14; Signed lock power2.out 0.4 s; blur-out 0.45 s.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| signer | string | "" (first BRAND.cast lead, Jordan Tate) | applicant. Jordan Tate gets the full cursive signature; any other name gets a seeded scribble from the name |
| address | string | "" (BRAND.cast.listing.address) | listing address |
| title | string | Rental application | document title |
| date | string | Oct 24, 2026 | date signed |
| track | boolean | true | status track under the chip (landscape only) |
| fadeOut | boolean | true | blur out at 4.15 s |

## Formats
- 16x9: page left of centre (scale fits height), big chip (1.9x) right with the four-node track under it.
- 9x16: chip above the page, centred, page fitted to the safe box (x 70-940, y 270-1240); no track.
- 1x1 / 4x5: same stack as 9x16, page scaled to the safe box.

## Flash risk
None. Brightest element is the paper (steady); the sheen is soft-light under 15% of the frame; no flood.

## SFX cues (local time: kind)
- 0.00: paper slide whoosh
- 0.55: soft status tick (Sent); 1.05 tick (Delivered); 1.50 tick (Viewed)
- 1.75: tag click (Sign tag pops)
- 2.40 to 3.20: pen scribble (continuous, rises with the strokes)
- 3.20: signed chime (chip locks to Signed, tick draws 3.35)
- 3.20: faint paper settle thud

## Hand-off
First frame: nothing (page enters from below, blurred). Last frame (fadeOut false, 4.6 s): the signed page on the left, Signed chip with green tick on the right (landscape) or above the page (vertical). The next scene can push into the chip (Fee requested).

## Verified
Lint 0 errors. Snapshots 16x9 at 0.9/1.8/2.6/3.9/4.0 s, 9x16 at 1.9/3.0/4.0 s (signer Marcus Lee for the fallback signature) and Jordan Tate default; page inside safe insets, nothing clipped, fields legible. Demo brand (Tidewell): colours, fonts, wordmark, signer, address re-theme; when a brand has no `partners.docusign` the chip shows a document glyph instead of the DocuSign mark (a brand using this archetype for real should supply the mark). Limitation: Jordan Tate's cursive signature is the only name-matching signature.
- Reviewer pass 2026-10-21: lint 0 errors; 16x9 and 9x16 snapshots plus 4x5 and 1x1 at 3.9 s; 60 fps draft renders in 16x9 and 9x16 pass flashcheck (0 flashes/s, 0 floods, 2 large-area changes below the flood threshold) and safezone PASS. No changes needed. The baked signature path is keyed to the default cast lead name; any other signer gets a generated path.
