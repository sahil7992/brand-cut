# list-swap-toggle (A17)

## What it is
A feature tour in one shot. A list (Texts / Showings / Applications / Fees) with an active dot that glides, and a glass card that swaps real Tidewell UI for each item: the thread (HF.realui thread with the brand's sample thread and a real AI answer), the Next showing card, two DocuSign application rows, the Stripe fee receipt. The card resizes to each panel, then collapses into a pill toggle labelled "Tidewell replies" that switches on. The showing panel uses the Next showing component (not the week calendar) because the calendar's new block has a hardcoded name that would not match the thread.

## Sources
- Holo Deq1nUPMqtr 15.3-23.6 s: 4-word list, active dark with gradient dot, glass card right, slide-up swaps (0.25 out / 0.35 in), card collapses into a toggle that switches on.
- Premium DcYhz2ZN1vZ 6.0-7.9 s: highlight slides about 5 frames per row. CodeRabbit 18-22 s: active row full, others 55%.

## Duration and easing
Default 8.2 s. Card in 0.35 (expo.out 0.85); messages arrive 0.75, 1.05, 1.35, 1.65 (power3.out); swaps every 1.0 s from 2.5: old panel out 0.25 power2.in, new in 0.35 expo.out at +0.2, dot glide 0.27 power3.inOut, card resize 0.45 power3.inOut; collapse 5.7-6.4 power3.inOut; toggle label in 6.3; knob throws 6.7 (0.3 power3.out, track fills green); hold; blur out 7.6-8.1.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| items | string | Texts\|Showings\|Applications\|Fees | List labels; panel k uses builder k mod 4 (thread, showing, application, fee) |
| toggleLabel | string | Tidewell replies | Label on the closing toggle |
| fadeOut | boolean | true | Blur out at the end |
Names, amounts, address, thread text come from BRAND (cast.leads, story.sampleThread, story.sampleFee, cast.listing).

## Formats
- 16x9: list left in 80 px type, 700 px glass card at the right of the safe rect, vertically centred.
- 9x16, 1x1, 4x5: the list becomes a horizontal tab row at the top of the safe rect (dot glides sideways), card 84% of the safe width centred below, panels zoomed to fit; the toggle ends in the centre of the card region.

## Flash risk
None. Soft halo behind the card at 24% accent, constant; no luminance steps.

## SFX cues (local time, sound kind)
- 0.35: soft whoosh (card arrives). 0.75, 1.05, 1.35, 1.65: message pop (in, out, in, out; the out ones a lighter chime).
- 2.5, 3.5, 4.5: slide swap (short whoosh) with a tick as the dot lands (+0.27).
- 5.7: low whoosh (card collapsing). 6.7: switch click, then a soft success tick at 6.85.

## Hand-off
First frame empty. Last frame (fadeOut false, t=7.6): list dimmed with Fees active, the green "Tidewell replies" toggle on in a glass pill at the card position. With fadeOut it ends blurred and transparent.

## Verified
Lint 0 errors. 16x9 at 1.4, 2.2, 2.6, 3.0, 3.9, 4.9, 5.0, 5.9, 6.8, 7.4, 7.7, 8.0 s; 9x16 at 1.2, 3.9 and 7.95 s; demo brand at 2.6 s (other thread, face, colours and font follow). Panels never clip, thread text stays legible, every element inside the 9:16 safe rect.

Reviewed 2026-10-21: fixed a hardcoded brand literal (the thread meta line said "Tidewell · 9s"; now B.name + " · 9s"); lint 0 errors; 16x9 at 1.9/4.0/6.9 and 9x16 at 3.5/6.9 fine (real thread, DocuSign rows, toggle; card inside the safe rect). flashcheck on the 60 fps draft: PASS (0 flashes).
