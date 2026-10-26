# card-burst (A14): radial card burst

## What it is
A dark glass brand tile sits in the middle. Two thin ripple rings leave it, then real home photos, real lead notification cards (HF.realui.notif) and glass text chips fly out to polar positions: duotone in the brand ramp at launch, settling to natural colour, back.out about 6% on the scale, then a slow float. After a hold, the photos implode into a small ring around the hub while notifications and chips fold into it. The hub never glows. Use for the "every listing, every lead" abundance beat.

## Sources
- OpenAI Dcn6EINyzaa 13.3-14.4 s: send tap, 14 cards fan round a hub with tilt jitter and shadows, concentric ripple rings, back.out about 6%.
- Holo Deq1nUPMqtr 4.9-7.2 s: 8 photo cards plus chips fly from the centre to polar positions (expo.out 10 frames), orange duotone settling to natural colour by 5.1 s, then implode into a ring at 7.0-7.15 s.
- Coralarya 8.4-9.7 s, Blackbox 10.1-11.8 s (secondary).

## Duration and easing
5.2 s (host clip 5.2). Hub pop back.out(1.4) 0-0.55 s; ripples 0.45 and 0.62 s, 1.1 s each; cards from 0.5 s, 0.04 s apart in a seeded random order: position expo.out 0.85 s, scale back.out(1) 0.8 s, duotone fade power2.out 0.9 s, tilt settles over 1.1 s, motion blur 9 px that clears with the move; float 4-7 px sine; implode from 3.4 s, power2.in 0.7 s (all cards together, 7 px blur and a dip to 50% opacity mid-travel, no stagger); the ring then turns about 11 deg/s; hub thump 4.5% at 4.1-4.55 s. Scene drift 1.0 to 1.04. Pure function of one time value, so it seeks exactly.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| count | number | 12 | home photo cards (4-17). Vertical and square formats show about two thirds. Photos come from BRAND.photos.dir (home-1..5, u01..u12). |
| chips | string | "" | text chips, "|" separated. Empty uses the listing facts from BRAND.cast.listing (address, rent, beds and baths, pets, parking). Vertical shows the first 3. |
| notifs | number | 3 | real lead notification cards (0 turns them off, 2 in vertical formats). Names and channels from BRAND.cast.leads. |
| fadeOut | boolean | true | blur out in the last 0.5 s; false hands off the hub with its photo ring. |

## Formats
- 16x9: ellipse of about 1760 x 960 around the hub, photos 250 px wide, 12 photos, 3 notifications, 5 chips.
- 9x16: everything inside x 70-940, y 270-1240 (clamped with a 14 px float margin), photos 212 px wide, 8 photos, 2 notifications, 3 chips; bigger ring at the end.
- 1x1 and 4x5: same clamp to the format safe box, photos 175 px.
Positions come from seeded polar slots plus a 90 pass overlap relaxation that also keeps the hub clear.

## Flash risk
None to low. The hub stays dark, ripples are 1.5 px rings at 50% opacity, no light sweep. Brightest full-frame change is a photo card entering (under 12% of the frame area).

## SFX cues (local time: sound kind)
- 0.00: soft glass pop (hub appears)
- 0.50: whoosh (the burst, 0.8 s)
- 0.55 to 1.6: light card taps as each card lands, one every 0.04 s in a random order (use 5 to 6 of them, not 20)
- 0.45 and 0.62: faint ripple airs
- 3.40: reverse whoosh (implode, 0.6 s)
- 4.10: soft thump (ring locks, hub thump)

## Hand-off
First frame: hub only (a dark glass tile at the centre), so cut in from a dark scene. Last frame (fadeOut=false): hub at the centre with 12 (8 vertical) small natural-colour photo cards in a ring around it, slowly turning; the next scene can scale the ring away or match the tile.

## Verified
Lint 0 errors. 16x9 snapshots at 0.2, 0.9, 1.3, 2.5, 2.6, 3.7, 4.5 s; 9x16 at 1.3, 2.6, 4.6 s; 1x1 and 4x5 at 2.6 and 4.6 s; demo brand (Tidewell tile, fonts, chips from its own cast, notifications from its own leads) at 2.6 s. Duotone verified at 0.9 s (orange ramp), natural colour at 2.5 s. Falls short: the demo brand reuses the Tidewell home photos because it ships only one; give a brand its own photos dir. No Math.random or Date.
- Reviewed 2026-10-21 (reviewer-fixer): contract grep clean (no hardcoded hex outside var fallbacks, no brand literals, no Math.random/Date, no uppercase/italic/emoji); 16x9, 9x16, 1x1 renders at 60 fps. Fixes: vertical box now placed in pre-drift coordinates so cards stay inside y 270-1240 and x 70-940 after the 1.04 drift; final ring enlarged (land 175 px, vertical 160 px past the hub) and photos in the ring 150-180 px; the implode (cards crossing in and out over the same pixels, 4 flashes/s over 25-38% area) is now one coherent 0.7 s move with blur and a dip, flashcheck 16x9 PASS, 9x16 PASS, 1x1 PASS (before: WARN/FAIL at 4.5 s); chip text uses var(--ink), photo ground var(--bg2). preview.png regenerated (2.6 s).
