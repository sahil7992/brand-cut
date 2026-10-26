# network-lines (A12): chaos to connected network

## What it is
Real message chips (missed call, SMS, WhatsApp, a calendar clash) drift at three depths with depth blur. The brand tile (a glass plate, the only glowing object) appears, one 1 px wire reaches the first chip as a damped sine, then the other wires fork out about two frames apart. The chips slow to a stop, snap to tidy nodes, the noise chips dissolve, the wires relax from loose curves into clean S-curves, endpoint dots land and a green line under each chip says what Tidewell did ("Answered by Tidewell in 9s", "Alex picks the time" for the clash). Use for "your day without vs with".

## Sources
- OpenAI Dcn6EINyzaa 0.5-7.3 s: chaos hook, then blue origin dot, 1 px wire as a damped sine forking into curves staggered 2 frames, endpoints become dots. Study: STUDY/Dcn6EINyzaa.md.
- Pulse DeOxEFsItr5 16.6-19.0 s: tilted node graph settling (12 deg to 3 deg), here the chips settle from tilt 0-6 deg to 0.
- Blackbox 7.4-10.0 s (convergence), ElevenLabs still (clean elbowed connectors).

## Duration and easing
6.0 s (host clip duration 6). Chips drift p3.out over 2.0 s; hub back.out(1.6) 0.55 s; wires power2.out (0.95 s first, 0.7 s others); snap power4.out 1.0 s staggered 0.05 s; noise chips power2.in 0.75 s; stamps power3.out 0.6 s. Whole scene drifts 1.0 to 1.045 (sine.out). Everything is a pure function of one time value (a single dummy tween drives `render()`), so it seeks exactly.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| chaosLines | string | "" | chips, "|" separated, each `kind~name~text` (kinds sms, whatsapp, missed, calendar). Empty builds ten chips from BRAND.cast (leads, listing address). The first `nodes` chips are wired, the rest are noise. |
| nodes | number | 4 | chips that get a wire and become nodes (2-6). |
| fadeOut | boolean | true | blur out in the last 0.55 s; false hands off the ordered network. |

## Formats
- 16x9: hub centre, nodes in two columns (left and right, chosen by where each chip drifted so nothing crosses the hub), zoom 1.42, 2 rows.
- 9x16: hub left, one column of chips right-aligned to x 940 (zoom about 1.5), stamps right-aligned so wires never cross them; the whole group sits inside y 270-1240.
- 1x1 / 4x5: same as 9x16 with zoom limited by the safe height (1x1 1.44, 4x5 1.58).

## Flash risk
None. No flood, no light sweep. The only glow is the static hub; the blur-out ends dark to dark. Max luminance change per frame under 0.03.

## SFX cues (local time: sound kind)
- 1.25: soft glass pop (hub appears)
- 1.95: thin air draw, 0.9 s (first wire, damped sine)
- 2.05, 2.12, 2.18: three small ticks (the fork wires start, 0.066 s apart)
- 3.35: soft whoosh (chips start to snap, 1.0 s); light clack as each chip lands at 3.85, 3.90, 3.95, 4.00
- 3.90, 3.97, 4.04, 4.11: dot ticks (endpoint dots pop)
- 4.15, 4.27, 4.39, 4.51: soft success ticks (green lines fade up)
- no sound for the noise chips fading (3.35-4.1)

## Hand-off
First frame: empty (chips fade in from 0.05 s), so cut in from a dark scene or dissolve. Last frame (fadeOut=false): the ordered network, hub at centre (16x9) or left (vertical), chips and green lines on the final node grid; next scene can push through or match the hub tile.

## Verified
Lint 0 errors. Snapshots checked at 1.0, 1.5, 2.4, 2.6, 3.0, 3.7, 4.2, 5.4, 5.5 s in 16x9; 2.6 and 5.4 s in 9x16; 5.4 s in 1x1 and 4x5; 5.4 s with the demo brand (Tidewell: cast, tile, fonts, partners re-themed, no Tidewell copy). 9x16 content inside x 70-940, y 270-1240. Text legible at 4x5 and 9x16 (chips 550 px wide). No Math.random or Date.
- Reviewed 2026-10-21 (reviewer-fixer): contract grep clean (the only hex literals are var-less fallbacks for B.palette.warn/info and the neutral WhatsApp badge ground); lint 0 errors; 16x9, 9x16, 4x5 renders at 60 fps. Fixes: the final network is laid out in pre-drift coordinates (the 1.045 drift pushed the top chip to y 222 in 9x16 and the last green line to y 1273, inside the unsafe bands) and the group centring sign was reversed (it sat 35-50 px low); now the 9x16 final frame spans y 271-1213, x 75-939. flashcheck: 16x9 PASS, 9x16 PASS, 4x5 PASS. preview.png regenerated (5.4 s).
