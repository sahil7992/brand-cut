# composer-send (A13)

## What it is
The lead's side of the story. A real listing photo plate (slow push) with a phone-style message composer (SMS or WhatsApp look, not a chatbot box): a "+" button, a frosted pill, a send button that appears with the first character, as the real apps do. The lead's first message types in with seeded irregular gaps, a caret, and the newest word in the film accent cooling to white; the pill grows a line at a time with an elastic spring. A touch indicator glides to send, a single-frame 2x match-cut zoom lands on the button, the press happens in the zoom, a single-frame cut returns to wide, the text clears and the sent bubble flies up.

## Sources (refs + timestamps)
- Coralarya DeGb1XytuE1 0.95-3.77 (composer over a photo, current words accent, box grows as text wraps, 2x zoom on send at 2.95, cut back at 3.77).
- OpenAI Dcn6EINyzaa 11.3-13.3 (prompt over a photo, zoom to the send button, dolly drift).
- Holo 12.2-13.0 (irregular typing gaps 0.05-0.14 s). PATTERNS.md A13 and section 3 (typing, pointer, match cut).

## Duration and easing
Default 6.7 s at 20 cps for the default 57-character message. Bar rises expo.out 0.7 s at 0.1; typing from 0.75 with gap = mean x (0.45-1.55) plus 0.10-0.18 s after punctuation (seeded; last character at 4.04); touch glides power4.out 0.55 s ending at 4.54; match-cut zoom 2x at 4.54 (one frame, nothing interpolated); press scale 0.9 at 4.84; cut back to wide, text clears and bubble starts at 5.09; bubble rises expo.out 0.75 s with blur 5 to 0; bar height elastic.out(1,0.5) 0.55 s per new line, spring back power3.out 0.4 s on send. Photo push 1.0 to 1.1 linear over the whole scene. Scene end 6.74 (typing time scales with message length and `cps`).

## Variables
| id | type | default | meaning |
|---|---|---|---|
| text | string | empty | message; empty = first lead message of `BRAND.story.sampleThread` |
| photo | string | assets/photos/home-2.jpg | listing photo plate (any `BRAND.photos.dir` file) |
| channel | enum sms, whatsapp | sms | composer look and sent-bubble colour (platform greens, not brand colours) |
| seed | number | 5 | seeds the irregular typing gaps (HF.rng) |
| cps | number 9-26 | 20 | average characters per second |
| fadeOut | boolean | false | blur out at the end |

## Formats
Bar and bubble live in a 390 x 560 design space scaled to the safe width (zoom 2.45 max in 16x9, about 2.2 in 9x16). The bar is bottom-anchored 36 px (16x9) or 50 px (others) above the bottom safe inset so the send button never moves while the pill grows upward. 9x16: bar at about y 1070-1160, sent bubble rests at about y 540-740, all inside y 270-1240 and x 70-940. 1x1 and 4x5 use the same rule from `BRAND.format.safe`. The bar is centred in the safe box, not the frame (9:16 right edge x 913, inside 940). The plate is `object-fit: cover`; the 1400 px stock photos are soft at 1920 px tall (use a larger plate for 4K 9:16).

## Flash risk
None. The match cut is a scale jump on the same image, not a luminance change; no sweeps beyond the shade.

## SFX cues (local time: sound kind), default text
- 0.10: soft whoosh (bar rises)
- 0.75-4.04: key tick on each word start (about 10 words, quiet; or a continuous soft keyboard bed)
- 0.75: send button pop (appears with the first character)
- 4.30: touch whoosh (finger travel, 0.55 s ending at 4.54)
- 4.84: send tap click (press, in the zoom)
- 5.09: sent whoosh up plus message-sent swoosh (cut back, bubble flies)
- 5.55: soft msg_pop (bubble lands)

## Hand-off
First frame: the photo only with the bar sliding in. Last frame: the sent bubble (channel green) resting at the upper right of the bar area, empty placeholder bar below, so the next scene (`chat-thread` or `container-morph`) can pick up the same message; pair with `fadeOut` or a push-through blur.

## Verified
Harness `arch-composer-send`: lint 0 errors, 1 warning (`gsap_callback_dom_measurement`, intentional: the clock-driven update reads static layout offsets to find line starts, caret position and wrapping so late fonts cannot desync it; transforms and bounding rects are never read). Snapshots 16:9 at 0.5, 1.6, 2.8, 3.9, 4.5, 4.8 (in the zoom), 5.2, 5.5, 6.6; 9:16 at 3.9, 4.8, 6.6; demo re-theme with WhatsApp look at 3.0 and 6.6 (blue accent word, mono font, 4-line bubble). Typing, caret, height spring and clear are pure functions of the clock, so non-linear seeks are safe. Not verified in a full render.

Reviewer pass 2026-10-21: contract grep clean (platform greens are iMessage/WhatsApp identity, not brand colours), lint 0 errors (1 intentional warning), snapshots 16:9 x3 and 9:16 x2; fixed the 9:16 bar centred on the frame so its right edge hit x 948 (now centred in the safe box). flashcheck PASS (60 fps draft, 0 flashes, 1 flood at 4.55 s from the match-cut, which is allowed).
