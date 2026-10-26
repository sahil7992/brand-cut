# brutal-type (A19 Brutalist giant type)

## What it is
A poster beat: a flat brand colour field grows from a point at the frame centre (the previous scene's dot), huge mixed-case lines reveal one by one through a mask, the last word slides in from the right with horizontal motion blur and a 3.7% spring, its full stop pops in as a separate live dot (squash then circle), and with `dotHandoff` the camera zooms through that dot into the next scene, ending on the dot colour. Hooks and punchlines: "Every lead, answered instantly."

## Sources (refs + timestamps)
- Brutalist DeDaXyYoRTG 1.5-3.0 s: flat colour card grown from the dot, heavy lines clipped by a mask, last word ("IT") slides in with horizontal blur, overshoot 3.7% of the width, settles in about 7 frames; the full stop is a separate dot that pops in (ellipse then circle).
- Brutalist 2.83-2.98 s: zoom through the full stop (about 6x text, dot covers the frame in 9 frames, 12 px blur).
- Blackbox DdCmsxptRdM 12.2-14.2 s (heavy type on colour). Study: STUDY/DeDaXyYoRTG.md.
- Changed from the source: mixed case instead of caps; the field grows over 0.55 s and the zoom-through lasts 0.62 s (the source did both in 3 frames, a flash risk).

## Duration and easing
Field circle 0-0.55 s power2.inOut (radius 60 px to 0.55 of the diagonal), opacity in 0.12 s. Lines reveal 0.6 s expo.out from 118% down, start 0.32 s, stagger 0.2 s. Last word: starts after the lines, 0.42 s power3.out to -3.7% of the width (with SVG blur 70 px to 0 along x), then 0.3 s sine.inOut back to 0. Dot pop: 0.12 s scale (1.15 x 0.8) then 0.14 s back.out(2). Slow drift scale 1 to 1.03 on the text. Zoom-through: 0.62 s power2.in, exponential camera scale 1 to 14 about the dot, blur up to 10 px, dark cover circle behind it growing to full coverage between about 2.2 and 2.5 s (9-10 frames at 30 fps). Without dotHandoff: lines slide up out 0.35 s, last word slides left 0.35 s, then the field shrinks back to a point 0.5 s power3.in. For the default text (2 masked lines): last word lands at 1.57 s, hand-off 1.97-2.59 s, clip length 3.0 s.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| lines | string | Every lead,\|answered\|instantly. | Lines separated by `\|`. The last word of the last line is the spring word; a trailing `.` becomes the live dot. Sentence case. |
| field | string | accent | accent (orange, dark ink, last word in brand), paper (light field, needs flood true), brand (cordovan field, light ink, last word accent-lift). |
| size | number | 20 | Line height as percent of frame height at 16x9 (18-26 reads brutal). Fitted down so the widest line fits the safe width (longest line in characters x 0.52 em). |
| dotHandoff | boolean | true | Zoom through the full stop and end on the dot colour (on-paper, near black, matching a dark next scene). False = the field shrinks back to a point. |
| flood | boolean | false | Allow field paper (a full-frame light area ramped over 0.55 s). With flood false, paper falls back to accent. |

Apostrophe trap: the host `data-variable-values='{...}'` is single-quoted; use a typographic apostrophe in lines.

## Formats
- 16x9: left-aligned stack in the safe box (x 192-1728), 216 px lines (20% of H), field circle from centre.
- 9x16: every word gets its own line (lines are split on spaces), left aligned at x 70, size fitted to the longest word (about 186 px, roughly 10% of H, because 18-26% of 1920 cannot fit 870 px); the stack sits in y 270-1240.
- 1x1 and 4x5: same single-word-per-line logic when the frame is taller than wide; 1x1 keeps the 16x9 line breaks with the fitted size.

## Flash risk
Medium in the source, low here. Dark to orange: the field is a growing circle (about 17 frames at 30 fps); orange to dark: the dot zoom covers the frame over 9-10 frames. No step above 0.1 mean luminance per frame. Paper field is a larger swing (about 0.6): README "flood: yes" for field=paper, gated by `flood` (default false), and must not occur within 8 s of another flood.

## SFX cues (local time: sound kind)
- 0.00: low swell start (field grows), ends 0.55.
- 0.32 / 0.52: short paper-slice whoosh per line (lines reveal).
- 0.77 (last word start = lines x 0.2 + 0.37): fast whoosh with a short tail, panned right to centre.
- 1.19: light thud (the last word's spring lands, 0.42 s later).
- 1.27: tiny pop (the full stop appears), then 1.39 settle tick.
- 1.97: rising whoosh swell (zoom-through), peak at 2.5.
- 2.59: silence (hard dip) before the next scene's first sound.
Times shift by 0.2 s per masked line you add or remove.

## Hand-off
First frame: black with a 60 px orange point at the centre (match it to the previous scene's 120 px dot: scale 0.5 would be exact; the field starts as soon as the dot is in place). Last frame (dotHandoff true): solid on-paper colour (about #1A0A05 on Tidewell), hold at least 0.2 s, then the next scene's dark background. With dotHandoff false: empty (transparent) after the field has shrunk to a point.

## Verified
`hyperframes check` 0 errors (earlier runs flagged the intended text-under-cover and the pre-reveal contrast; fixed by hiding lines at 0 opacity until they reveal and by hiding the text after the cover closes). 16x9 at 0.2, 0.4, 0.7, 1.0, 1.2, 1.7, 2.0, 2.2, 2.3, 2.4, 2.5, 2.6 s: field grows, lines mask in, blurred slide with spring, dot, zoom-through to dark. 9x16 at 0.2-2.45 s: one word per line inside x 70-940, spring overshoot crosses the left inset for about 0.15 s by design. Demo (Tidewell, field brand, "Every patient, answered instantly.") at 1.7 s: blue field, light ink, accent-lift last word, dark dot. Fixed a stray dot caused by the cover circle having radius 0.92 x dot at p=0.

Reviewer pass 2026-10-21: contract grep clean (the only # in the file is #fff/#000 inside a colour-mix tint), fixed lint warning gsap_callback_dom_measurement (dot position now measured once at build time), 16x9 and 9x16 snapshots inside safe bands. flashcheck FAILed (4/s over 33% at 2.4 s: last-word slide at 1.3 W with 0.01 s opacity step, line reveals, zoom-through); fixed with the last word travelling 0.6 W with an opacity ramp, line opacity ramps 0.3 s, dive zoom 8x (was 14x) with the text dimming over 0.3 s, and the dotHandoff=false exit fading. flashcheck PASS at 16x9, 9x16, 1x1, 4x5, field=brand, field=paper+flood, dotHandoff=false.
