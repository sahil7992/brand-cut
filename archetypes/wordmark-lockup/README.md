# wordmark-lockup (A08 Giant wordmark truck to lockup)

## What it is
A giant extruded mixed-case wordmark (14 stacked translateZ layers, cream face, cordovan side walls, lit from the top left) that the camera trucks across with a 2-frame ghost, then one expo.inOut pull-back (with motion blur at peak speed) into the lockup. The yaw returns to 0 and the extrusion fades as the face lands, so the giant word and the lockup word are the same element in the same colour: the match cut on colour, with no cut at all. The brand tile (BRAND.logo.tile) pops in beside it, the word slides to its place, and the tagline types with irregular gaps. `endTheme: paper` wipes the lockup onto a paper plate in 0.5 s. Open or close a film with it.

## Sources (refs + timestamps)
- Wise DesrXMCIq-o 0.0-1.65 s: extruded WISE wordmark fills the frame, truck left to right with slight yaw (extrusion changes), 2-frame motion blur, hard cut to the small logo at 0.65 s (replaced here by a continuous pull-back), and 18.6-20.8 s: logo on dark then on light (replaced here by a 0.5 s wipe). Study: STUDY/DesrXMCIq-o.md shots 1, 2, 12-13.
- Our v2 reel s12-wordmark (giant wordmark truck, expo.inOut pull-back at 2.0-3.0 s) and s13-end (lockup on paper, tagline and url blur in).
- OpenAI Dcn6EINyzaa 9.6-11.3 s and Pulse DeOxEFsItr5 47.2-49.1 s for the typed tagline cadence.

## Duration and easing
Truck 0-1.55 s power2.out (x +0.2 W to -0.2 W, i.e. 384 px at 16x9; flashcheck-safe, yaw -15 to +11 degrees, scale 4.0). Ghost copy 2 frames behind at 28% opacity. Pull-back 1.5-2.45 s expo.inOut (scale to 1, x to centred, yaw 0), blur 0 to 7 px at 1.58-1.88 and back by 2.28 s, extrusion fades 2.03-2.37 s. Tile pop 2.33 s (0.55 s back.out 1.5), word slides to its place 2.33-2.93 s expo.out. Tagline types from 2.88 s, each letter 0.2 s tinted accent cooling to ink, gaps 0.028-0.078 s (seeded), caret on the newest letter, then blinks 3 times. Soft pool behind rises 0-1.4 s to 55% opacity. Paper wipe (if on) 5.53-6.03 s power2.inOut with a soft edge, then the dark layer is removed. Slow drift 1 to 0.97 from 2.33 s. Clip length 6.4 s (6.3 s without paper).

## Variables
| id | type | default | meaning |
|---|---|---|---|
| word | string | empty = BRAND.logo.wordmarkText | The wordmark text (mixed case). |
| tagline | string | empty = BRAND.endline | Typed under the lockup; wraps to two lines on vertical. |
| endTheme | string | dark | dark or paper. paper wipes onto a paper plate in 0.5 s, never a hard cut. |
| flood | boolean | false | With paper: true = the paper covers the full frame (a flood, ramped by the wipe, once per 8 s); false = a paper plate about half the frame. |

## Formats
- 16x9: row [tile][word] centred in the safe box, word 250 px, tagline 52 px under it on one line; giant word 4.0x.
- 9x16: column [tile above word] centred in the safe box (so on y 755, the platform-safe centre, not y 960), word up to 270 px fitted to 870 px, tagline wraps to two lines; the paper plate is sized to hug the content (about 94% wide).
- 1x1 and 4x5: the vertical (column) layout when the frame is taller than 1.1 x its width, otherwise the row; both fitted to their safe boxes (verified at 1x1 and 4x5).
Needs a brand with logo.tile and logo.wordmarkText (demo brand verified).

## Flash risk
Low. The truck has no luminance step; the pool is 55% of a dark red glow under a quarter of the frame. The paper wipe is a 0.5 s soft-edge wipe (plate about 0.48 of the frame area; flood=true covers the full frame and counts as the film's one flood for 8 s). Do not follow it with another light scene within 8 s.

## SFX cues (local time: sound kind)
- 0.00: low whoosh swell under the truck (to 1.5 s).
- 1.50: pull-back whoosh (rising, 0.9 s) with a low thud at the landing 2.40.
- 2.33: soft pop (tile).
- 2.33: short slide whoosh (word moves, 0.4 s, quiet).
- 2.88-5.1: typing ticks, one per letter on the letter times (soft, 4 dB under UI clicks), none on spaces.
- 5.53: wipe whoosh (only with paper, 0.5 s, soft).

## Hand-off
First frame: black (the giant word enters at 0 s with a 0.25 s fade). Last frame: the lockup centred in the safe box on the pool with the full tagline and a quiet caret (dark), or the same on the paper plate or paper frame, drifted to 0.97. It is an end card: hold it, or hard-stop the film. Use the first 2.4 s alone as an opener by clipping the scene at 2.9 s.

## Verified
`hyperframes check` 0 errors. 16x9 at 0.15, 0.6, 1.1, 1.6, 1.9, 2.2, 2.6, 3.4, 4.2, 4.4, 4.6, 4.8, 5.0, 5.3-5.8 s (truck, ghost, blur, flatten, tile, typing, wipe edge at 5.4, plate at 5.6). 9x16 at 0.4, 1.2, 1.9, 2.6, 4.6, 5.9 s (column layout, plate hugs content), 1x1 at 5.9 s, 4x5 at 2.9 s, flood=true at 5.9 s. Demo (Tidewell, wave tile) at 2.9 and 4.4 s: tile and wordmark re-themed, extrusion colours follow brand-lit/brand-deep. Fixes found by looking: filter on the 3D element flattened the extrusion (blur moved to an outer wrapper), SVG/plate outside the root, paper layer flagged as occluding text (opacity 0 until the wipe), vertical plate centred on the safe box.

Reviewer pass 2026-10-21: contract grep clean, lint 0/0, 16x9 and 9x16 snapshots inside safe bands, deterministic (HF.rng seeded). flashcheck FAILed (4/s over 100% at 0.77 s: giant strokes trucking 2240 px); fixed with truck travel 0.2 W each way, the whole lockup fading in over 0.5 s power2.in, and the word pulling back straight to its lockup place (the second centre-to-lockup slide removed). flashcheck PASS at 16x9, 9x16, 1x1, 4x5, endTheme=paper, paper+flood. The first-second fade-in of the huge cream word registers as one house flood at 0.37 s (README flood rule: one per film opening, fine).
