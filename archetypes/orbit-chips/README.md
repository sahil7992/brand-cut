# orbit-chips (A16): hub with orbiting chips

## What it is
The brand tile in glass (a dark, warm-rimmed plate with a soft light pool under it, not a glowing orb) sits in the middle of a tilted elliptical orbit. Chips with real logos (SMS, WhatsApp, Calendar, DocuSign, Stripe) travel the ellipse: chips in front are larger, sharp and pass over the hub; chips behind are smaller, blurred, dimmer and pass behind it. The chip passing the front-centre slot lights up (paper glass), grows 42% and reveals its state line ("Answered in 9s", "Showing booked", "Application signed", "Fee paid"). Use for "works where you already work".

## Sources
- Holo Deq1nUPMqtr 8.3-10.4 s: about 12 chips on an ellipse (axes 1.6x and 0.9x the orb diameter), scale 0.6-1.0 by depth, active chip enlarges to a white pill; orbit 25-35 deg/s.
- Pulse DeOxEFsItr5 9.0-10.7 s: rings and sting around a hub, rings turn about 20 deg/s.
- Blackbox DdCmsxptRdM 5.1-7.4 s (orbiting dots).

## Duration and easing
5.6 s (host clip 5.6). Hub back.out(1.4) 0.6 s; chips fly out of the hub expo.out 0.8 s, 0.09 s apart from 0.35 s; orbit linear at `speed` deg/s (default 36), chip scale 0.74 + 0.3 depth; active window plus or minus 34 deg, smoothstepped, so the grow and state reveal ease in and out by themselves; depth blur up to 3.6 px. Whole scene drifts 1.0 to 1.04. Pure function of one time value, so it seeks exactly.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| chips | string | sms~SMS~Answered in 9s, whatsapp~WhatsApp~Answered in 9s, calendar~Calendar~Showing booked, docusign~DocuSign~Application signed, stripe~Stripe~Fee paid (joined with a vertical bar) | vertical-bar separated, each `icon~label~state`. Icons: whatsapp, stripe, docusign (brand partner logos), sms, calendar, mark (the brand tile); anything else gives a generic document glyph. |
| speed | number | 36 | orbit speed, degrees per second. Chip i is at the front at 1.0 s + i x 72 / speed (5 chips). |
| fadeOut | boolean | true | blur out in the last 0.5 s; false hands off the orbiting hub. |

## Formats
- 16x9: hub 340 px, ellipse 560 x 250 px tilted -7 deg, chips 1.3x.
- 9x16: hub 300 px, ellipse 215 x 330 px (near circle seen from above), chips 1.2x, inside x 70-940 and y 270-1240.
- 1x1 and 4x5: hub 250 px, ellipse 235 x 230 px, chips 1.1x, inside the format safe box.

## Flash risk
None. No flood or sweep; the paper highlight on the active chip is under 3% of the frame and fades in over about 0.4 s.

## SFX cues (local time: sound kind)
- 0.00: soft glass pop (hub)
- 0.35, 0.44, 0.53, 0.62, 0.71: tiny pops as the chips leave the hub (one soft whoosh is enough)
- 1.00: soft chime, first active chip (SMS lights up); 3.00 (WhatsApp); 5.00 (Calendar). Formula: 1.0 + i x 72 / speed
- no sound for the orbiting itself (a quiet low air bed under the scene is fine)

## Hand-off
First frame: empty (hub scales up from 0, chips leave it from 0.35 s). Last frame (fadeOut=false): hub centre, chips on the orbit with one chip lit near the front; the next scene can push into the lit chip or the hub tile.

## Verified
Lint 0 errors. 16x9 at 0.5, 1.0, 2.0, 3.0, 4.0, 5.0 s; 9x16 at 1.0, 3.0, 4.6 s; 1x1 and 4x5 at 3.0 s; demo brand (Tidewell tile, fonts, palette; no demo DocuSign logo so it falls back to a generic document glyph) at 3.0 s. Label and state do not overlap on the active chip. No Math.random or Date.
- Reviewed 2026-10-21 (reviewer-fixer): contract grep clean; lint 0 errors; 16x9, 9x16, 1x1 renders at 60 fps. Fixes: the orbit now eases to 35% speed as each chip reaches the front (phase warp, lands on the same 1.0 + i x 72 / speed times) because the fast sideways sweep of the high-contrast lit chip text gave 3 flashes/s over 26% area in 16x9 (WARN); vertical hub 250 px, ring rx 250, chip scale 1.08 so side chips fit x 70-940; side chips now pass behind the glass hub (z below the hub unless in the front 55%) so no pill covers the logo mark; chip text uses var(--ink). flashcheck: 16x9 PASS, 9x16 PASS, 1x1 PASS. preview.png regenerated (3.0 s).
