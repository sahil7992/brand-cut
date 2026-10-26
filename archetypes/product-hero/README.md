# product-hero (A22)

## What it is
The "Blender product shot" without Blender: the photoreal phone (`HF.phone`) with a real app capture is the hero object. It starts small and out of focus, rack-focuses sharp in 3 frames, dollies in to 75 percent of frame height, settles its yaw, then pulls back to its final place while four real UI chips burst out of it in an exploded lineup (new lead, showing booked, application signed, fee paid). Transparent: sits on the film's glow field.

## Sources
- AirPods `DbsyEbSR5c1` 2.4-3.8 s (soft key upper left, fill from the right, dolly 28.8 to 76 percent of frame height in 1.1 s expo.inOut, parts move separately), 4.6-4.9 s (rack focus: 10-12 px defocus resolving in 3 frames), 5.9-7.1 s (exploded part lineup). Study: `STUDY/DbsyEbSR5c1.md`.
- Wise `DesrXMCIq-o` 15.0-17.7 s (glossy object tilts, pulls back, then pushes in). Study: `STUDY/DesrXMCIq-o.md`.

## Duration and easing
4.6 s default. 0-0.5 s small phone (30 percent H) with yaw drift -26 to -21 deg; rack focus 0.32-0.42 s (blur 12 px to 0, linear, 3 frames at 30 fps, 6 at 60); dolly 0.5-1.7 s expo.inOut to 75 percent H with yaw settling to -9 deg on power4.out; glass sweep at 1.0 s; pull-back and slide 1.9-2.7 s expo.inOut to 60 percent H at the left; chips burst from behind the phone at 2.15 + 0.14 i s (expo.out 0.7 s, blur 10 px to 0, scale 0.25 to 1), then float 8 px on sine.inOut; whole-scene drift 1.0 to 1.045; exit blur out 4.2-4.6 s (power2.in).

## Variables
| id | type | default | meaning |
|---|---|---|---|
| screen | string | `home` | `BRAND.ui` key on the phone (home, thread, ask, askOpen, showings, showingsMonth) |
| chips | string | `lead\|slot\|application\|fee` | up to 4 chip kinds in burst order (lead, slot, application, fee, pay) |
| rack | boolean | true | start defocused and rack in |
| fadeOut | boolean | true | blur out in the last 0.4 s |

Chip content comes from `BRAND.cast`, `BRAND.story.sampleFee`; labels are sentence case.

## Formats
- 16x9: phone at the left (x 470), chips in two columns on the right (450 px wide boxes, real UI scaled about 1.2x), every box inside safe x 192-1728.
- 9x16: dolly to 52 percent H centred in the safe box, then the phone shrinks to the top (y 270-625) and the chips form a 2x2 grid below it, x 77-933, y 625-1195 (all inside x 70-940, y 270-1240).
- 1x1: phone small at the top, 2x2 chips below (box 330 px). 4x5: same, box 360 px.
Native layouts, never crops.

## Flash risk
None. No flood, no bloom; the key light is a soft gradient and a thin rim on the phone, the glass sweep is under a quarter of the frame. `qa/flashcheck.py` on a 16x9 draft: PASS, 0 flashes, 0 floods.

## SFX cues (local time: sound kind)
- 0.32: soft lens "thunk" (rack focus resolves)
- 0.50: whoosh, low and long (dolly in)
- 1.00: glass glint, quiet (sweep)
- 1.90: whoosh, short (pull back)
- 2.15, 2.29, 2.43, 2.57: pop with a tiny whoosh, rising pitch (chips burst out: lead, slot, application, fee)
- 4.20: soft whoosh out

## Hand-off
First frame: empty (phone is visible but tiny and blurred from 0.0 s; opacity is 1, so the previous scene should fade or blur into it). Last frame with `fadeOut`: empty. With `fadeOut` false: phone left and four chips right at rest.

## Verified
- `hyperframes lint`: 0 errors, 0 warnings.
- 16x9 snapshots at 0.2, 0.5, 0.9, 1.4, 1.9, 2.4, 3.4, 3.6 s: rack, dolly size (about 815 px = 75 percent H), burst, final layout, text legible.
- 9x16 at 0.2, 1.0, 1.4, 2.3, 3.6 s: chips grid inside the safe box; 1x1 and 4x5 at 3.6 s.
- Demo brand re-theme at 3.6 s (blue palette, mono font, other cast): renders, no edits (the mono font makes the Directions button touch the chip edge).
- Draft render 16x9 30 fps (4.6 s) OK; flashcheck PASS.
- Reviewer pass 2026-10-21: contract grep clean; lint 0 errors; 16x9 x3 and 9x16 x2 snapshots checked; 60 fps draft flashcheck PASS. Fix: 9x16 dolly-peak phone scale 0.52 to 0.50 so the bezel stays inside y 270-1240.
