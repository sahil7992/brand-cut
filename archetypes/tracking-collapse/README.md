# tracking-collapse (A05 Tracking collapse)

## What it is
A short statement that lands hard. Each word flies in from a frame side with horizontal motion blur and stops with the gaps too wide, then the gaps close in 0.3 s with two trailing ghost copies (35% and 15% opacity, 2 and 4 frames behind). The line creeps down to 0.955, then exits on an accelerating ease-in shrink with a blur. With `dotOut` a lit dot sits before the line and lifts out to the centre of the safe box at 120 px, which is the hand-off frame for status-stack (A07). Words and spans move; letter-spacing is never tweened.

## Sources (refs + timestamps)
- Wise DesrXMCIq-o 5.5-6.4 s (shot 6, "NO HIDDEN FEES"): words enter from the sides, gaps collapse in 0.35 s, slow creep, accelerating shrink exit, badge lifts out as a dot (STUDY/DesrXMCIq-o.md, shot 6 and 7). We use sentence case and the Tidewell line "No missed leads."

## Duration and easing
Fly-in 0-0.42 s power2.out from 0.45 W off-centre, opacity ramps in over the same 0.42 s power2.in so contrast is low while the words are fast (blur 60 px horizontal to 0 via an SVG blur, power3.out). Collapse 0.50-0.80 s power4.out. Ghosts lag 0.067 s and 0.133 s, fade out by 0.85. Creep 0.78-1.55 s power1.out (1 to 0.955). Exit 1.55-1.89 s power3.in (scale 0.3, blur 8 px, opacity 0). Dot pops at 0.62 s (back.out 1.6, 0.32 s), lifts out 1.51-2.21 s power3.inOut. Clip length 2.8 s (2.2 s if dotOut is false and the next scene follows at the exit).

## Variables
| id | type | default | meaning |
|---|---|---|---|
| text | string | No missed leads. | 2 to 4 short words land best. `*stars*` mark accent words (accent-lift colour). Sentence case. |
| size | number | 170 | px at 16x9; fitted down so the whole line stays inside the safe width (16 characters lands at about 146 px). Vertical uses 1.5x then fits the longest word. |
| dotOut | boolean | false | Add the badge dot and lift it out to the centre at the end. |

Apostrophe trap: `data-variable-values='{...}'` is single-quoted, so a straight `'` in text drops all variables; use a typographic apostrophe.

## Formats
- 16x9 and 1x1: one row, centred in the safe box; the dot sits to the left of the line. The gaps spread along x.
- 9x16 and 4x5: the words stack in a column (alternate words fly in from left and right, the vertical gaps spread and close); the dot sits above the stack; type about 190-240 px, longest word fitted to 66% of the safe width (x 70-940).

## Flash risk
None. Ghosts are 35% and 15% opacity white text, no full-frame change.

## SFX cues (local time: sound kind)
- 0.00: fast whoosh (words fly in, 0.4 s, pitched down).
- 0.50: short low thud (the gaps close, on the collapse start).
- 0.62: soft pop (dot appears, only if dotOut).
- 1.55: whoosh-down (accelerating exit).
- 1.51: rising whoosh swell to the dot landing (only if dotOut).
- 2.21: soft tick (dot lands at centre, only if dotOut).

## Hand-off
First frame: empty dark (words off-frame). Last frame with dotOut: one 120 px lit dot (paper to glow-6 radial, soft glow) at the centre of the safe box; status-stack's dot is the same 120 px recipe, so place the next scene's dot at that spot (16x9 centre x 960, y 540; 9x16 x 505, y 755). Without dotOut the frame is empty dark.

## Verified
`hyperframes check` 0 errors (after adding data-layout-allow-overlap to the ghost spans). 16x9 at 0.12, 0.3, 0.5, 0.7, 1.2, 1.7, 2.4 s: fly-in with blur and ghosts at 0.12 and 0.3, gaps closed by 0.7, dot centred at 2.4 s. 9x16 at 0.15, 0.35, 0.6, 1.2, 1.8, 2.4 s: stacked column inside x 70-940, ghosts vertical, dot lands at the safe centre. Demo (Tidewell) at 1.1 s: blue accent, rounded face, dot recoloured from the brand glow ramp.

Reviewer pass 2026-10-21: contract grep clean, lint 0/0, 16x9 and 9x16 snapshots inside safe bands. flashcheck FAILed (4 flashes/s over 25% at 0.98 s: words crossing the frame at full contrast); fixed by flying in from 0.45 W instead of 0.85 W, blur 60 px, ghosts 22%/10%, opacity ramped over the fly-in. flashcheck PASS at 16x9, 9x16, 1x1, 4x5 and with dotOut=true.
