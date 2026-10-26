# logo-sting (A28 Logo sting / end card)

## What it is
The mark builds the way the product works: for the Tidewell Tidewell mark an incoming bar slides in (0.32 s), the countersign dot springs (0.16 s), the reply bar draws out (0.38 s), exactly the timings in the product's own `the mark component`/`globals.css`. The mark is inline SVG built from `BRAND.logo.markColors` (ink, reply, tile) so it re-themes. It builds large (1.55x) in a soft pool of light, then glides to its lockup place while the wordmark blurs in, the endline and the url follow. For a brand that is not Tidewell (the demo brand) the tile (BRAND.logo.tile) scales in with back.out instead, then the same lockup. `theme: paper` ends on paper through a 0.5 s soft wipe.

## Sources (refs + timestamps)
- Our v2 reel s10-logo (mark build, glide, wordmark blur-in, end url) and the brand animation in `git -C ~/tidewell.ai show origin/main:apps/web/src/components/the mark component` and `.../globals.css` (`tidewell-mark-animate`: arrive 320 ms, countersign 160 ms at 380 ms, reply 380 ms at 540 ms; read 2026-10-21).
- Glow DesrDGAoX_Q 12.8-14.9 s (mark in a deep pool, then a light card; we replace the hard cut with a wipe), Pulse DeOxEFsItr5 9.0-10.7 s (mark, then wordmark), SDS DYrpr7iztRy 16.4-18.8 s (parts settle into the mark), AirPods DbsyEbSR5c1 9.8-11.1 s (1.3 s hold on the end card).

## Duration and easing
Pool rises 0-1.3 s sine.out to 60%. Mark build starts 0.25 s: incoming x -8 units to 0 and opacity, 0.32 s power4.out (the product's cubic-bezier 0.22,1,0.36,1); dot scale 0 to 1, 0.22 s back.out(1.2) [softened from 0.16 s back.out(1.7), flashcheck]; was: back.out(1.7) at +0.38; reply scaleX 0 to 1, 0.38 s power4.out at +0.54 (done by 1.17 s). Hold 0.38 s. Glide 1.55-2.55 s power2.inOut (mark 1.3x to 1x, centred to lockup place). Word 1.80-2.50 s power3.out (blur 14 to 0, 36 px). Endline 2.45-3.25 s, url 2.85-3.65 s (blur 12/10 px to 0, y 14/10 px). Paper wipe 4.0-4.5 s power2.inOut, soft edge. Camera 1.0 to 1.03 over 1.75 s sine.out, then 1.03 to 0.97 sine.inOut to the end. Clip length 4.8 s dark, 5.6 s paper.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| endline | string | empty = BRAND.endline | Sentence-case line under the lockup (wraps to two lines on vertical). |
| url | string | empty = BRAND.url | Shown last, muted, small. |
| theme | string | dark | dark or paper. paper wipes onto a paper plate after the url; never a hard cut. |
| flood | boolean | false | With paper: true = the plate becomes the full frame (a flood: once per 8 s, ramped by the wipe); false = a paper plate hugging the content (about half the frame). |

Kit change suggested: add `logo.markAnim: "countersign" | "tile"` to brand.json; the scene currently detects the Tidewell mark by the path containing "countersign".

## Formats
- 16x9: row [mark][word] centred in the safe box, word 210 px, mark 1.0 x 1.8 of the word size; endline 50 px, url 36 px under it.
- 9x16: column [mark above word], word up to 250 px fitted to 870 px; the composition is centred on the platform-safe box (y 755, x 505); endline wraps to two lines at 50 px.
- 1x1 and 4x5: row or column by aspect (column when height > 1.1 x width), fitted to the safe boxes.

## Flash risk
Low. The pool is a dark red glow under a quarter of the frame (peak mean luminance well under 0.1 of the frame). The paper wipe is 0.5 s with a soft edge; a plate is about 0.45 of the frame (vertical 0.5), flood=true is the full frame and counts as the film's one flood for 8 s.

## SFX cues (local time: sound kind)
- 0.25: soft slide-in whoosh (incoming bar).
- 0.63: small pop/tick (countersign dot).
- 0.79: short draw whoosh (reply bar, 0.38 s), the build's "send" sound.
- 1.55: low swell start under the glide (1.0 s).
- 1.80: soft whoosh (wordmark arrives, quiet).
- 4.00: wipe whoosh (paper only, 0.5 s, soft).
Silence dip of 0.2 s before 0.25 is recommended (the previous scene's tail ends first).

## Hand-off
First frame: black with the pool at 0%, nothing on screen. If a dot hands off from brutal-type or tracking-collapse, the first frame can start with that 120 px dot at the lockup centre and let the countersign dot grow from it. Last frame: lockup (mark, wordmark, endline, url) centred in the safe box on the pool, drifted to 0.97 (dark), or the same on the paper plate. It is an end card: hold it 1.3 s or more, then stop.

## Verified
`hyperframes check` 0 errors. 16x9 at 0.3, 0.5, 0.75, 1.2, 1.7, 2.1, 2.8, 3.6, 4.4 s (build, glide, wordmark, endline, url; each build step lands on its time). 9x16 at 0.5, 1.2, 2.4, 3.4, 4.3, 5.0 s with theme paper (column layout, wipe edge at 4.3 s, plate hugs content). Demo (Tidewell, tile path) at 0.3, 0.45, 1.0, 1.9, 2.6, 3.8 s: tile scales in centred, glides, wordmark Tidewell, endline and url from the demo brand. Fixed by looking: GSAP scale on the tile overwrote the centring transform (the pop now runs on an inner wrapper). One contrast probe flags the paper layer for a single frame at the wipe start (dark ink on the not-yet-revealed dark ground at 4.04 s); it is the wipe itself.

Reviewer pass 2026-10-21: contract grep clean, fixed lint warning gsap_callback_dom_measurement (word width measured once at build time), 16x9 and 9x16 snapshots inside safe bands. flashcheck WARNed (3 red flashes/s over 29% at 1.68 s; 25% at 1.17 s in 4x5: bars crossing the red pool); fixed with the mark glide 1.3x to 1.0x over 1.0 s power2.inOut (was 1.55x, 0.7 s power3.out) and a softer dot spring. flashcheck PASS at 16x9, 9x16, 1x1, 4x5, theme=paper, paper+flood.
