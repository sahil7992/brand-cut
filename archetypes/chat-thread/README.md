# chat-thread (A23)

## What it is
The core product moment: a real Tidewell thread (real `HF.realui.thread` bubbles, avatar, channel, "AI on" pill) animating inside the photoreal phone (`HF.phone`, corner-pinned screen) or as one big flat thread card. Messages come from `BRAND.story.sampleThread`: lead bubble from the left, typing dots, Tidewell reply from the right with its "Tidewell · 4s" meta, the lead picks a time, Tidewell books it, and a "Showing booked" chip closes the scene. The thread scrolls like a real chat when it outgrows its window; the scroll is a pure function of per-message progress, targets measured live, so a late font load cannot desync it.

## Sources (refs + timestamps)
- Our v2 `s05-texts` and the 2026-10-17 commercial `s04-answers.html` (real bubbles, dots in the reply slot, 0.7 s back.out reply, accent border cooling to hair).
- CodeRabbit DdcEQPOstOH 7.5-10.9 (messages enter 0.25 s slide-up, cadence accelerates).
- Coralarya DeGb1XytuE1 2.0-2.7 (reply grows into place).
- Pulse DeOxEFsItr5 4.1-6.0 (typed question, caret, highlight).
- PATTERNS.md A23.

## Duration and easing
Default 7.8 s with phone true (about 7.55 s flat). Lead/tidewell bubbles: opacity+x expo.out 0.45 s from the sender side, scale 0.94 to 1 back.out(1.7) 0.7 s (about 4% settle), accent border cooling to hair over 1.0 s, meta power3.out 0.4 s. Dots appear back.out(1.7) 0.25 s, bounce sine.inOut 0.14 s, last `typing` seconds (0.6-1.0, default 0.8) before each Tidewell reply. Scroll power3.out 0.55 s. Phone entrance power4.out 1.1 s (y 140, rotationX 8, rotationY -10 to -4), then rotationY drifts to +3 over 8 s; whole stage drifts scale 1.0 to 1.045 (sine.out). In 9:16, 1:1 and 4:5 the drift scales about the safe top (1.02, no y shift) so the header never crosses y 270; 16:9 keeps scale 1.045 and y -16. Exit: blur 10 px + fade power2.in 0.55 s ending at the scene end (variable `fadeOut`).

## Variables
| id | type | default | meaning |
|---|---|---|---|
| lead | string | jordan | id in `BRAND.cast.leads` (jordan, priya, marcus, ana): name, face, channel |
| channel | enum auto, sms, whatsapp | auto | auto = the lead's own channel label |
| count | number 1-8 | 4 | how many messages of `BRAND.story.sampleThread` to play |
| phone | boolean | true | true = inside the photoreal phone; false = big flat card |
| chip | boolean | true | closing chip (only when the last message is Tidewell's and count >= 2) |
| chipText | string | Showing booked | chip label (the listing address from `BRAND.cast.listing` follows it) |
| typing | number 0.6-1.0 | 0.8 | seconds of dots before each Tidewell reply |
| fadeOut | boolean | true | blur out at the end |

## Formats
- 16x9: phone sized so the thread (header to the scroll anchor) runs from y 108 to 972 at most; the phone bleeds off the bottom and its top bezel stays in frame (thread top is pushed down to 30 px of bezel). Flat mode is a 560-wide thread card scaled about 1.84x.
- 9x16: phone scaled to about 0.97 (900 px wide), thread header at y 270, last message anchored above y 1240 (400 screen px visible). Flat mode is a 365-wide card scaled to the safe width (870 px).
- 1x1 and 4x5: same rule from `BRAND.format.safe`, scroll anchor 430 / 450 screen px.
Nothing is cropped from a landscape layout; sizes come from `BRAND.format`.

## Flash risk
None. No flood; the only light moves are the phone's glass sweep (a soft 55%-of-phone-width band at 0.9 s, under a quarter of the frame) and the 2.0 s accent border cooling on the newest bubble.

## SFX cues (local time: sound kind), phone true; flat mode is 0.25 s earlier
- 0.15: soft whoosh as the phone settles in
- 0.75: msg_pop (lead bubble arrives)
- 1.25: typing tick (dots appear)
- 2.05: msg_pop, warmer (Tidewell reply lands)
- 3.50: msg_pop (lead picks a time)
- 4.00: typing tick (dots)
- 4.80: msg_pop, warmer (Tidewell books it)
- 5.75: confirm chime (Showing booked chip)
Times shift with `typing` and `count`; recompute as t = 0.75, +0.5 after a lead bubble, +typing then +0.2+min(1.3, 0.6+0.004*chars) after a non-final reply, +typing+0.95 after the final reply (chip lands there).

## Hand-off
First frame: empty stage (the phone is at opacity 0, 140 px low). Last frame with `fadeOut` false: the full thread scrolled to the last reply with the Showing booked chip, phone slightly right-turned (rotationY 3). With `fadeOut` true the scene ends fully transparent, so the next scene can start on black or on its own plate.

## Verified
Harness `arch-chat-thread`: lint 0 errors 0 warnings. Snapshots at 0.4, 1.1, 2.2, 3.2, 4.6, 6.4 (16:9 phone), 6.4 (9:16 phone), 1.5 (dots visible, top-right of the future bubble), flat mode 16:9 and 9:16 at 6.4 (with lead priya on WhatsApp), demo re-theme at 6.4 (different brand text, fonts and tokens flowed through; chip wraps onto two lines when the listing name is long, scroll accounted for it). Fixed during the run: scroll targets desynced under fallback fonts (now live-measured), chip clipped in landscape flat mode (now part of the last scroll target). All text sentence case, no emoji, thread inside 9:16 safe insets (x 70-940, y 270-1240) apart from the status bar and phone body.

Reviewer pass 2026-10-21: contract grep clean (brand name now from `BRAND.name`, lead-bubble border cool-down read from the computed style, check icon ink from `B.app.ground`), lint 0 errors, snapshots 16:9 x3 and 9:16 x2; fixed 9:16 header creeping to y 223 under the centre-origin drift (now safe-top origin). flashcheck PASS (60 fps draft, 0 flashes, 0 floods).
