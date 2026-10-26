# glass-slab (A02)

## What it is
The AI moment: a big liquid-glass slab (backdrop blur, bevel rim, contact shadow, one top-left light, a soft sheen pass) carrying the REAL Ask screen. It starts in the real empty state (ribbon glyph, "Ask me anything.", the three real suggestion chips, the composer), the question types into the composer with irregular gaps, send is pressed, the empty state leaves, the question lands as a message and the real answer streams in word by word. A real "Next showing" component (HF.realui) with the lead's face floats over the composer corner once the answer is complete. Sits over a glow field (glow-field) or any dark plate; it does not depend on one.

## Sources (refs + timestamps)
- Glow DesrDGAoX_Q 5.7-7.2: slab swings in from below to rotateX, power4.out settle, rotateY drift, refracts the glow.
- Calendar DcWXXbGKzMZ 1.9-4.1: frosted card, 24 px backdrop blur, 1 px specular rim, rows fade in.
- Gradient opener DXzurbATRQT 7.0-9.2: card with rotateY drift and a fast blurred exit.
- v2 reel `compositions/s04-panel.html` (glass recipe, motion-blur filter proxy, user bubble).
- Real app captures `assets/ui/tidewell-dark.png` and `tidewell-open-dark.png` (copy, composer, chips, subtitles).

## Duration and easing
About 7.0 s to a finished answer, then it holds: rise power4.out 1.25 s; type 1.45 to 3.32 s (20 chars, seeded irregular 0.05-0.12 s gaps, caret blink); send press 3.50 s; empty state out power2.in 0.35 s; user message power3.out 0.62 s; answer head 4.12 s; words 0.075 s each from 4.32 to 7.02 s (power2.out 0.22 s, blur 5 px to 0); card expo.out 0.65 s at 7.1 s. Legible >= 2.5 s needs a slot of about 9.6 s or more (use 10). The slab eases from rotateX 7 to 2 deg while the answer is read. Long answers: stream time = 0.075 s x word count.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| q | string | BRAND.story.sampleAsk.q | question typed into the composer |
| a | string | BRAND.story.sampleAsk.a | answer streamed word by word |
| avatar | string | "" | BRAND.faces id on the answer card; empty = first lead in BRAND.cast.leads; `none` = no card |
| chips | string | the three real chips | `|` separated list, optional `Title~Subtitle` |
| time | string | 9:41 AM | timestamp on the message and answer |
| fadeOut | boolean | false | blur the slab out starting at exitAt |
| exitAt | number | 8.6 | second the exit starts (0.45 s) |

## Formats
- 16x9: slab 1300 x 864 centred; the empty state is two columns (big "Ask me anything." left, chips right); the Next showing card (with the lead's face) overlaps the bottom-right corner of the slab, 70 px outside it.
- 9x16: slab is the full safe rect (x 70-940, y 270-1240), taller, one column, type 42-47 px; the card (no avatar) overlaps the composer corner, inside the safe rect.
- 1x1 and 4x5: slab = safe rect, one column, type 36-44 px, smaller card.
Never a crop: sizes come from a per-format table in the scene.

## Flash risk
None. No flood, no full-frame light; the sheen is a soft band under a quarter of the slab at 16% white, two passes (0.8 s and about 6.6 s). Motion blur only along the rise.

## SFX cues (local time, kind)
- 0.15 s: whoosh-soft (slab rise, lands at 1.2 s: soft glass settle).
- 1.45-3.32 s: key ticks, one per character (the typed text timing is deterministic: first 1.45 s, then every 0.05-0.12 s).
- 3.50 s: tap (send press), then 3.55 s a short send blip.
- 3.7 s: swish (empty state out) and message-in pop at 3.64 s.
- 4.12 s: soft chime (Tidewell starts to answer).
- 4.32-7.02 s: optional quiet word ticks, at most every third word; nothing on a beat.
- 7.1 s: card pop (expo, no overshoot).
Keep a 0.2 s silence dip before the 3.50 s tap.

## Hand-off
First frame: transparent (slab below the frame, stage opacity 0.2); last frame (no fadeOut): slab with the finished answer, the card over the composer corner; next scene can match-cut zoom onto the card or push-through blur. With fadeOut: blur and fade from exitAt.

## Verified
Tidewell 16x9 t=0.5, 1.2, 2.2, 3.4, 4.2, 5.5, 7.4, 9 s (typing, empty state two columns, answer, card, no clipping after fixes); 9x16 t=2.4, 7.6, 8 s (inside x 70-940, y 270-1240, answer ends above the composer); 1x1 t=2.4, 8 s; 4x5 t=8 s; demo re-theme (tide, its own sampleAsk and cast) t=3 and 8 s; lint 0 errors. Note: CSS is branched with a data-fmt attribute set in JS on the content root because `html[data-format]` selectors do not match inside sub-compositions in this runtime.

Reviewer pass (2026-10-21): removed literals ("Ask Tidewell" title now "Ask " + BRAND.name, "Jordan Tate" fallback, hex stroke colours now app tokens); lint 0 errors; 16x9 x3 and 9x16 x2 snapshots checked; 60 fps draft flashcheck PASS (0 flashes/s, 0 floods).
