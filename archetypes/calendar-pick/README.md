# calendar-pick (A21)

## What it is
The real Tidewell web calendar (HF.realui.calendar, week time grid) rises on a glass slab. The lead's reply arrives as a real notification ("Saturday at 11 AM works for me"), the free slot glows, the showing card drops into it with a contact shadow, and a "Confirmed" chip checks in (free-time bookings confirm on the spot; never an approval step). A slow camera push lands on the new showing.

## Sources
- Our v2 s07-calendar (`videos/tidewell-motion-reel-v2-2026-10-20/compositions/s07-calendar.html`, card rises, chip drops, Confirmed badge) and the commercial s06-showing.
- dija reel DcWXXbGKzMZ 2.3-4.1 (STUDY/DcWXXbGKzMZ.md): long-decel arrival then rest then press; pick-up and drop into a date; slow tracking camera. Adapted: no cursor (nothing is clicked in Tidewell, the booking is automatic), the drop plus camera push carry the same beat.
- Real captures: `BRAND.ui.showings` (mobile week strip, used for the 3-day vertical view order Thu Fri Sat).

## Duration and easing
4.3 s. Slab rise power4.out 1.0 s then sine settle; notification expo.out 0.65 s; slot glow power2.out 0.45 s; drop power4.out 0.5 s (y -90, scale 1.2 to 1, blur 8 px to 0); chip back.out(1.6) 0.45 s (only small living object); camera push power3.inOut 1.1 s to 1.10 (1.04 vertical) then slow linear drift; exits power2.in 0.35 s; optional blur-out 0.4 s.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| day | string | Sat | column: Sun..Sat (any events at that time in the column are cleared so the slot is free) |
| time | string | 11:00 AM | showing time, 09:00 to 14:00 |
| lead | string | "" (BRAND.cast.leads[0]) | name; a cast lead name or id gets face and channel |
| address | string | "" (BRAND.cast.listing.address) | listing address in the card |
| message | string | "" | notification text; blank builds "<Day> at <time> works for me" |
| notif | boolean | true | show the lead reply notification |
| fadeOut | boolean | true | blur out at 3.9 s; false holds the hand-off frame |

## Formats
- 16x9: 4 day columns (Wed to Sat), 4 hour rows, scale 1.3, header kept.
- 9x16: 2 columns (Fri, Sat), scale up to 1.6 fitted to the safe width (x 70-940), rows 4, header trimmed to New showing + Day/Week/Month; card sits inside y 270-1240; notification overlaps the card top for 2 s.
- 1x1 / 4x5: 3 columns, scale fitted to safe width, 4 or 5 rows.

## Flash risk
None. No flood; only local glow (slot, < 3% of frame) and a soft sheen under 20% of the frame. Luminance never steps more than a few percent.

## SFX cues (local time: kind)
- 0.00: soft whoosh (slab rises)
- 0.95: notification ping (message arrives)
- 1.25: soft rising tone, quiet (slot glows)
- 2.10: card snap / thud (showing drops in, contact shadow)
- 2.45: confirm chime (Confirmed chip, tick draws 2.55)
- 3.10: faint whoosh (notification leaves)

## Hand-off
First frame: empty (slab rises from y +120 with blur). Last frame (fadeOut false, 4.3 s): the calendar slab, camera pushed on the new showing block with the Confirmed chip above it; the next scene can match-cut zoom on that block (centre of the block is the camera origin).

## Verified
Lint 0 errors. Snapshots 16x9 at 1.4/2.1/3.7 s, 9x16 at 1.4/2.9/4.2 s, 4x5 at 1.8/2.6/3.9 s, 1x1 at 2.6 s: nothing clipped, 9x16 card inside safe insets (notification overlaps title for 2 s by design), real UI legible. Demo brand (Tidewell) at 2.6 s: lead, address, glass tint, fonts and app tokens re-theme. Limits: the kit's calendar hardcodes a few dark-theme hexes and the New showing rose button; events in the grid are the kit's sample showings (fictional).
- Reviewer pass 2026-10-21: lint 0 errors; 16x9 and 9x16 snapshots plus 4x5 and 1x1 at 3.9 s; 60 fps draft renders in 16x9 and 9x16 pass flashcheck (0 flashes/s, 0 floods) and safezone PASS. No changes needed.
