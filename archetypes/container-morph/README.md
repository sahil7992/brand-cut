# container-morph (A24)

## What it is
An iOS-style notification (`HF.realui.notif`) drops in, is tapped, and grows into the full Tidewell thread view (`HF.realui.thread`). The banner text is a shared element: a ghost copy of it flies from the banner position to the first bubble, interpolating rect, font size, line height and colour, and is swapped for the real bubble text on a single frame. Optional typing dots close the scene so it hands off to `chat-thread`.

## Sources (refs + timestamps)
- CodeRabbit DdcEQPOstOH 5.45-7.40 (one rect from pill to window in 0.5 s, chrome cross-fades, content appears as the window grows).
- Pulse DeOxEFsItr5 1.9-2.3 (chip becomes a square and grows).
- PATTERNS.md A24 and section 4 item 1 (shared-element morph, flash none).

## Duration and easing
Default 4.5 s. Banner drop 0.7 s expo.out (scale 0.96 to 1); tap press scale 0.972 (0.09 s) and release (0.14 s) at 1.25; morph 0.8 s expo.inOut at 1.45 (visible motion about 1.7-2.05); banner chrome fades 0.18 s at 1.65; header 0.25 s at 1.87; bubble 0.2 s at 1.95; composer 0.3 s at 1.95; text swap on the frame at 2.25; meta 0.4 s; dots back.out(1.7) at 2.35 bouncing for 1.1 s; camera drift scale 1.0 to 1.04; a soft warm pool of `--glow-5` (34%) fades in behind the card from 1.3 s over 1.6 s so the dark card is lit.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| lead | string | jordan | id in `BRAND.cast.leads` |
| text | string | empty | banner text and first bubble; empty = first lead message of `BRAND.story.sampleThread` |
| channel | enum auto, sms, whatsapp | auto | channel label (auto = lead's own) |
| dots | boolean | true | end on the typing indicator |
| fadeOut | boolean | false | blur out at the end |

## Formats
Design space is the real app size (365-460 px wide) scaled by Z so the final card fills 80% of the safe height or the full safe width: 16x9 card 865 x 620 (width 460 design), 9x16 and 4x5 card the full safe width (870) with the banner at its top edge, 1x1 from its safe box. Everything is laid out inside the safe insets (9:16 x 70-940, y 270-1240). Nothing is cropped.

## Flash risk
None. Dark-to-dark morph; no flood, no sweeps.

## SFX cues (local time: sound kind)
- 0.20: notification ding (banner lands)
- 1.30: tap (press)
- 1.85: soft whoosh/expand (morph peak)
- 2.25: msg_pop quiet (text lands as the bubble)
- 2.35: typing tick (dots)

## Hand-off
First frame: empty (banner above its slot, opacity 0). Last frame: the thread card centred with the lead bubble, "9:04 PM" and Tidewell typing dots, identical in position to `chat-thread` flat mode only when the film sets the same size, so cut with a short blur push (use fadeOut true) or cross-dissolve.

## Verified
Harness `arch-container-morph`: lint 0 errors, 1 warning (`gsap_callback_dom_measurement`, intentional: the morph re-reads static layout offsets on each update because fonts can load after build; no transforms or bounding rects are read, and computed styles are read once at build). Snapshots 16:9 at 0.45, 1.0, 1.75, 1.85, 1.95, 2.05, 2.15, 2.35, 3.6, 9:16 at 1.9, 2.0, 3.6; demo re-theme at 1.0 and 3.6 (3-line banner, mono fonts, blue ground, all flowed through). Bug found and fixed: apply ran before the morph progress tween on forward seeks, leaving a stale clip; the morph tween now owns an onUpdate.

Reviewer pass 2026-10-21: contract grep clean, lint 0 errors (1 intentional measurement warning), snapshots 16:9 x3 and 9:16 x2; fixed the flat black frame by adding a soft `--glow-5` pool behind the card. flashcheck PASS (60 fps draft, 0 flashes, 0 floods).
