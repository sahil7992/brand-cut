# branch-tree (A29): branch connector tree

## What it is
A dark parent pill (brand tile + name) on a grain-gradient field built from the brand palette. Orthogonal 2 px lines with rounded elbows leave its right edge, run to a trunk x per child and drop to the child's right edge; the white child pills (real logos: SMS, WhatsApp, Calendar, DocuSign, Stripe) step diagonally down and right and pop in as each line arrives. Use for the "connected to what you already use" beat or the hero end section.

## Sources
- ElevenLabs still DeaW0PvMe8j (STUDY/DeaW0PvMe8j.md, STUDY/img/DeaW0PvMe8j/post_1.jpg): black parent pill, four white child pills stepped +121 px down and +120-150 px right, 1 px #e1c2d1 connectors with about 16 px elbows and one trunk per child at child right edge + 58 px, grain gradient field, bottom 450 px empty for platform UI. Motion timing from PATTERNS.md A29.

## Duration and easing
4.6 s (host clip 4.6). Field fades in 0-0.6 s power2.out; parent power3.out 0.5 s from 0.3 s (y 40 to 0, scale .96 to 1); trunk k draws power2.inOut 0.35 s at 1.0 + 0.12 k; child pops back.out(1.4) 0.3 s (scale .92 to 1) from 1.3 + 0.12 k, origin at its right edge; a soft light band drifts across the field (sine.inOut); scene drift 1.0 to 1.03. Grain is one static 384 px tile at 8.5% overlay (no animated noise).

## Variables
| id | type | default | meaning |
|---|---|---|---|
| parent | string | "" | parent pill label; empty uses BRAND.name (with the brand tile as its icon). |
| children | string | sms~SMS, whatsapp~WhatsApp, calendar~Calendar, docusign~DocuSign, stripe~Stripe (joined with a vertical bar) | vertical-bar separated, each `icon~label`. Icons: whatsapp, stripe, docusign (brand partner logos), sms, calendar, mark, anything else gives a generic document glyph. |
| fadeOut | boolean | false | blur out in the last 0.5 s; default hands off the finished tree. |

## Formats
- 16x9: pills 130 px tall, 52 px type, group centred in the frame, children step by about 1.35 pill heights.
- 9x16: pills 115 px tall, 46 px type, step reduced so the whole group (trunks included) fits x 70-940; group sits at y 300-1180, the bottom 680 px stay quiet for platform UI.
- 1x1 and 4x5: pills 100 / 110 px, same rule inside the format safe box.
Pill widths come from a character-width estimate (General Sans or the brand font) so lines meet pill edges exactly.

## Flash risk
None. The field fades up from black over 0.6 s (mean luminance about 0.2, a fade, not a flood); no sweeps.

## SFX cues (local time: sound kind)
- 0.30: soft glass pop (parent lands)
- 1.00, 1.12, 1.24, 1.36, 1.48: thin line-draw ticks (trunks)
- 1.30, 1.42, 1.54, 1.66, 1.78: small pops (child pills land)

## Hand-off
First frame: field fading up, empty. Last frame (fadeOut=false): finished tree, parent top-left, children stepping to the lower right, with all five lines drawn; the next scene can push through the field or match the parent pill.

## Verified
Lint 0 errors. 16x9 at 0.6, 0.8, 1.2, 1.3, 1.6, 3.0 s; 9x16 at 0.8, 1.3, 3.0 s; 1x1 and 4x5 at 3.0 s; demo brand (Tidewell tile, blue field, fonts; no demo DocuSign logo so it falls back to a generic document glyph) at 1.3 and 3.0 s. Grain PNG generated deterministically (seeded noise). No text clipped, all pills inside the safe boxes. No Math.random or Date.
- Reviewed 2026-10-21 (reviewer-fixer): no change needed. Contract grep clean; lint 0 errors; 16x9 and 9x16 snapshots checked at 0.8, 1.6, 3.0 s (9x16 at 1.3, 3.0 s), final tree inside x 76-931, y 295-1187 after drift in 9x16; no clipped text. flashcheck at 60 fps: 16x9 PASS, 9x16 PASS (the 0.6 s field fade-in is not a flood). The preview.png is unchanged.
