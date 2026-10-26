# card-carousel (A11)

## What it is
A CSS 3D ring of real app cards (thread, home, listing with a real photo, calendar capture, application, payment request, receipt, approval, stats). The ring flies in from the lower left spinning, the centre card holds while it plays its own small animation, then the ring steps one card at a time (power3.inOut) and finally rises out through the top. Neighbours are smaller and rotated, outer slivers get 40 to 60 percent black as depth fog. Use it for breadth of product surfaces ("one app, everything in it"). Transparent: sits on the film's glow field; every card is an opaque real-UI surface with a glass bevel.

## Sources
- SDS `DYrpr7iztRy` 12.6-16.3 s (ring of about 9 cards on a ring, centre card scale 1, neighbours about 0.75 and rotateY 30-40 deg, outer slivers darkened 40-60 percent, ring flies in from bottom-left with geometric decay about 0.65 s and no overshoot, each card carries its own animation, ring rises out through the top 16.2-16.4 s ease-in). Study: `STUDY/DYrpr7iztRy.md`.
- Coralarya `DeGb1XytuE1` 5.9-6.9 s (card montage; we keep constant background luminance, no hard cuts).

## Duration and easing
Default 6.3 s = 0.95 s entry (f from -2.2 to 0, power4.out; fly-in expo.out with blur 16 px to 0) + 0.55 s hold + `steps` x `step` (each ring step is 0.55 s power3.inOut, then a hold of `step - 0.55` s) + 0.8 s hold on the last card + 0.45 s rise-out (power2.in, blur 12 px) when `fadeOut`. Formula: `0.95 + 0.55 + (steps - 1) * step + 0.55 + 0.8 (+ 0.45)`. Slow scene drift scale 1.0 to 1.05 over the whole length. Nothing pulses on a beat.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| cards | string | `thread\|home\|listing\|calendar\|application\|pay\|receipt\|approval\|stats` | card kinds in ring order (kinds: thread, home, listing, calendar, application, pay, receipt, approval, stats) |
| steps | number | 4 | how many times the ring advances (max cards - 1) |
| step | number | 1.0 | seconds per step (0.6 to 1.6) |
| fadeOut | boolean | true | the ring rises out through the top at the end |

All card content comes from `window.BRAND` (`cast.leads[0]` thread and its sampleThread, `cast.listing`, `story.sampleFee`, `photos.hero`, `ui.showings`). The application/receipt copy ("Rental application", DocuSign, Stripe) is the Tidewell vocabulary of the real components.

## Formats
Ring step is `min(34, 360 / n)` degrees, perspective 3000 px (a longer lens keeps outer cards edge-on rather than culled), neighbours also scale down to 0.8.
- 16x9: cards 520 x 720 (27 percent W, 67 percent H), centre on the frame centre, five cards visible.
- 9x16: cards 650 x 960 centred in the safe box (x 70-940, y 270-1240), neighbours peek in from both edges.
- 1x1: cards 520 x 720; 4x5: cards 520 x 760. Native layouts, never crops.
Deliberate deviation from the SDS measurement (20 percent W x 52 percent H): real UI text needs the larger card to be legible.

## Flash risk
Low. No flood, no light sweeps; cards are dark and constant in luminance, the only changes are card motion and small in-card fades. `qa/flashcheck.py` on a 16x9 draft: PASS, 0 flashes, 0 floods.

## SFX cues (local time: sound kind)
- 0.00: whoosh, heavy (ring flies in)
- 0.95: soft thump (ring lands)
- 0.90: message pop, soft (third thread message)
- 1.45: message pop, soft (Tidewell reply)
- 1.50, 2.50, 3.50, 4.50: short swish with a soft click (ring step; times are `0.95 + 0.55 + s * step`)
- 1.85: pop, small (Confirmed pill on the home card)
- 2.85: tick, soft (Pets row highlights on the listing card)
- 3.95: light chime (application Signed)
- 4.85: soft count ticks, optional (fee amount counting up on the payment card, a side card by then)
- 5.85: whoosh upward (ring rises out)
(Cues after the first step shift with `step`/`steps`; the in-card ones fire at `1.85 + (cardIndex - 1) * step`.)

## Hand-off
First frame: empty (ring off-frame lower left, opacity 0). Last frame with `fadeOut`: empty again (ring gone through the top). With `fadeOut` false: the last card centred with neighbours at rest. A next scene can start with a card or a phone coming up from the bottom.

## Verified
- `hyperframes lint`: 0 errors, 0 warnings.
- 16x9 snapshots at 0.3, 0.7, 1.3, 1.4, 2.2, 2.3, 3.1, 3.3, 4.3, 5.3, 5.7, 6.1 s and with the other kinds (pay, receipt, approval, stats): all cards legible, outer slivers visible with fog, nothing clipped.
- 9x16 at 1.3, 2.3, 3.3, 4.3, 5.3, 6.1 s: card inside the safe box, neighbours peek from the sides.
- 1x1 and 4x5 at 3.3 s.
- Demo brand re-theme at 3.3 s (blue palette, mono font, other cast and photo path): renders, no edits.
- Draft render 16x9 30 fps (6.3 s) OK; flashcheck PASS.
- Reviewer pass 2026-10-21: contract grep clean; lint 0 errors; 16x9 x3 and 9x16 x2 snapshots checked (hero card inside safe insets); 60 fps draft flashcheck PASS. Fix: hardcoded 'Tidewell' sender meta and '14 Aspen Court' approval text now come from BRAND.name and BRAND.cast.listing.address.
