# word-blur-in (A04 Kinetic word blur-in)

## What it is
One line of copy. Each word blurs in (blur 14 px to 0, scale 1.06 to 1, opacity 0 to 1) 0.14 s after the previous one, newest words tinted in the accent colour and cooling to ink. The whole line starts about 2.2x larger toward the lower left and is pulled back to centre in one continuous expo.out move, then drifts to 0.94 while it is read, and dims out. The one starred word keeps the accent colour. Use it for every on-screen line of copy ("It's 9:41 pm.", "Every lead, answered.", "You just show up.").

## Sources (refs + timestamps)
- Glow DesrDGAoX_Q 0.1-1.1 s: blur 14 px to 0, scale 1.06 to 1, stagger about 0.14 s, line pulled back from 2.4x lower-left in one expo.out move, then shrinks to 0.94.
- CodeRabbit DdcEQPOstOH 0.0-3.6 s: stagger 0.15-0.30, pivot word in the accent.
- Our own v2 reel scenes s01-any, s02-handled, s08-showup (same recipe, hard-coded words).

## Duration and easing
Word in 0.8 s expo.out, colour cool 0.6 s power2.out, stagger 0.14 s, pull-back 2.2 s expo.out (99% done by 1.2 s), drift 1.0 to 0.94 sine.out over the scene, dim-out 0.6 s power2.in starting 0.9 s after the last word lands. For 3 words the dim-out starts at 2.08 s. Recommended clip length: last word lands + 0.9 + 0.7, so 2.8-3.2 s for a three-word line, add 0.14 s per extra word.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| text | string | Every lead, *answered.* | The copy. `*stars*` wrap the accent word(s). A real newline or the two characters `\n` forces a line break. Sentence case, no ALL CAPS. |
| size | number | 132 | Font size in px on 16x9 (about 65% of the width for 21 characters). Vertical formats use 1.5x this and then shrink so the longest word fits the safe width. |
| align | string | center | left, center or right |
| pullback | boolean | true | Start zoomed and pull back to centre. False = just the drift. |
| dimOut | boolean | true | Dim and blur the line out at the end. False = hold crisp (hand-off frame below). |

Trap: the host attribute `data-variable-values='{...}'` is single-quoted, so a straight apostrophe in `text` ends the attribute and silently drops all variables. Use a typographic apostrophe (It’s) or escape it as `&#39;` when you write the host clip by hand. Do not put a literal `<` or `&` in the text.

## Formats
- 16x9: one line, centred in the safe box (x 192-1728, y 108-972), 132 px.
- 9x16: words wrap into stacked lines inside x 70-940, y 270-1240; size is 1.5x then fitted (longest word in characters x 0.6 em must fit 870 px), about 160-200 px. Pull-back starts 2x, offset 20% left and 10% down.
- 1x1 and 4x5: same wrap logic inside their safe boxes; size fitted the same way.

## Flash risk
None. No luminance change above the text itself; the dim-out is a fade to the film's own background.

## SFX cues (local time: sound kind)
- 0.10: soft whoosh (pull-back start, low, under -18 dB).
- 0.10 / 0.24 / 0.38 ...: one tiny soft tick per word (optional, 3-5 dB quieter than UI clicks). They follow the words, not the beat.
- 0.9: whoosh tail ends as the pull-back settles.
- dim-out start (last word + 0.9): none (silence dip is fine).

## Hand-off
First frame: black (the line is invisible, camera is zoomed in lower-left); the first word starts blurring in at 0.1 s. Last frame (dimOut true): the line is at 6% opacity and 12 px blur, scale about 0.94, centred, so the next scene can push in from the same point. With dimOut false it holds crisp at 0.94 scale in the centre of the safe box.

## Verified
Linted 0 errors, 0 warnings. 16x9 snapshots at 0.3, 0.7, 1.2, 2.0 s (words arrive blurred from the lower left, settled at 1.2 s, nothing clipped), 9x16 at 0.4, 1.0, 2.0, 2.9 s (stacked, inside x 70-940, y 270-1240) and a 5-word two-line text at 2.0 s (wraps, accent word on its own colour, longest line 150-880 px). Demo re-theme at 1.4 s (Tidewell blue, Open Runde). 

Reviewer pass 2026-10-21: contract grep clean (no hex/brand literals, __ID__ everywhere, no uppercase/italic/Math.random), lint 0/0, 16x9 and 9x16 snapshots inside safe bands. flashcheck on a 60 fps draft WARNed (3 flashes/s over 29% at 1.18 s: the 2.2x pull-back sweeps strokes over pixels); fixed with a 12 px camera motion blur proportional to speed and a gentler start (1.8x, offset 0.18 W). flashcheck PASS at 16x9, 9x16, 1x1, 4x5 and with pullback=false.
