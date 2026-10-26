# status-stack (A07)

## What it is
Dot to pill to a stack of status pills, the lifecycle of a lead in five lines: New lead, Answered, Showing booked, Application signed, Fee paid. Pills alternate dark glass and bright glow-card, zigzag a little, slide up from below with blur, each carries a real mark (WhatsApp, reply tick, calendar, DocuSign, Stripe) and a one-time light sweep; the camera scrolls so the newest pill stays near the centre.

## Sources
- Gradient opener DXzurbATRQT 6.5-19.9 s: pill from a dot with ~11% back.out overshoot, next status slides in expo.out 0.65 s, old one leaves.
- CodeRabbit DdcEQPOstOH 18-22 s (pill active state), Wise DesrXMCIq-o 0.2 s dot hold before the stretch.

## Duration and easing
Default (5 labels, step 0.46): pills arrive at 0.25 + 0.46 k. Dot pops back.out(1.6) 0.3 s; first pill stretches 120 px to full width expo.out 0.5 s; later pills y 190 to 0 with blur 14 to 0 expo.out 0.65 s plus scaleX 0.86 to 1 power3.out 0.7 s; letters stagger 30 ms; camera step power3.out 0.7 s; sheen power2.inOut 0.7 s; drift scale 1 to 1.06. End at 3.29 s of content. fadeOut: blur out 0.6 s (total about 3.9 s). loop: total 4.4 s (see below).

## Variables
| id | type | default | meaning |
|---|---|---|---|
| labels | string | New lead\|Answered\|Showing booked\|Application signed\|Fee paid | Pill texts |
| icons | string | whatsapp\|reply\|calendar\|docusign\|stripe | whatsapp, sms, reply, calendar, docusign, stripe, mark, or any brand partner key |
| step | number | 0.46 | Seconds between pills (0.25-1.2) |
| fadeOut | boolean | true | Blur out at the end (ignored when loop is on) |
| loop | boolean | false | Scroll back to the first pill, collapse it to the dot and end on the exact first frame, for a seamless feed loop |

## Formats
- 16x9: scale 1, pill pitch 156 px, wide zigzag.
- 9x16 and 4x5: stack scaled up to 1.3x, shrunk only as far as needed so the stack (with the 1.06 drift) fits the safe height and the widest pill with its zigzag fits the safe width (about 1.1x for the default labels in 9:16), centred in the safe rect (9:16: x 70-940, y 270-1240); pitch 168, narrow zigzag.
- 1x1: same rule inside the centre 810 px. The scale is a wrapper transform around the safe-rect centre, so layout maths is unchanged.

## Flash risk
None. A bright pill is about 25% of frame width and its glow is soft; no full-frame light.

## SFX cues (local time, sound kind)
- 0.00: soft pop (the dot). 0.25: pill stretch whoosh with a light tick on the icon pop (0.30).
- Pills 2-5 at 0.71, 1.17, 1.63, 2.09 (step 0.46; add k x step): soft upward whoosh, then a chime on the sheen (+0.12); bright pills (Answered, Application signed) get the brighter chime.
- loop only, from 3.29: low reverse whoosh as the stack scrolls back (3.29-4.19), soft pop as the dot collapses (4.09-4.39).

## Hand-off
First frame: empty (dot at scale 0). Last frame: with fadeOut, blurred and transparent; with fadeOut false and loop false, the five-pill stack held (t=3.29); with loop, the exact first frame (verified identical, SSIM 1.0 between 0 s and 4.5 s) so the clip can repeat without a seam.

## Verified
Lint 0 errors. 16x9 at 0, 2.3, 2.6, 3.9, 4.4, 4.5 s; 9x16, 1x1, 4x5 at 2.3 s (stack centred, widest pill inside the safe width); loop first and last frame compared pixel for pixel; demo brand re-theme at 2.6 s (blue accent, its fonts; a partner icon the demo brand lacks renders as a plain disc).

Reviewed 2026-10-21: contract grep clean; lint 0 errors (default and loop=true); 16x9 at 1.2/2.6/3.6 and 9x16 at 2.6/3.6 fine (stack centred, widest pill inside the safe width). flashcheck on the 60 fps draft first WARNed (3 flashes/s over 26% at 2.13 s: bright sheen bands plus a 190 px slide-in); fixed by sheen peak .7 to .3 and pill slide-in 190 to 100 px; now flashcheck PASS for default and loop=true.
