# chip-marquee (A06)

## What it is
Four real lead chips (face, name, channel glyph, the lead's message, Tidewell's real reply, an Answered tick) fly in on curves around a headline, each gets answered, then the cluster travels into 3 marquee rows (9:16 and 4:5: 5 rows, 1:1: 4 rows) that scroll in opposite directions. The cluster chips are the same elements as the row chips, so the move is a shared-element transition, not a cut. Use for "every lead, answered": many leads at once.

## Sources
- Wise DesrXMCIq-o 3.4-5.5 s: chips fly in on curves with ghosting, headline above, then 3 rows overflow the frame.
- Pulse DeOxEFsItr5 38.3-40.7 s: chain scrolls as it grows. Holo Deq1nUPMqtr 3.1-4.9 s: glass items around the focus.
- Reel v2 s05-texts.html (lead chip anatomy and glass recipe).

## Duration and easing
Recommended 5.6 s (cluster 0-2.4, travel 2.25-3.4, marquee to 5.5, blur out 5.5-6.0 if fadeOut; set duration 6.0 with fadeOut). Arrivals expo.out 0.85 s on x and power3.out 0.95 s on y (curved path), blur 18 px to 0; tick pop back.out(1.6); cluster to row power3.inOut 0.95 s; marquee eases in with an exponential start then runs linear at 7% of the width per second, alternating direction and +-12% speed per row; slow camera drift scale 1 to 1.035.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| headline | string | Every lead, answered. | Headline (dissolves and resolves in the head zone when the rows start) |
| messages | string | six question=>reply pairs, "|" separated | `{address}` is replaced with BRAND.cast.listing.address. Lead faces and names come from BRAND.cast.leads in order (message k uses lead k mod leads) |
| fadeOut | boolean | true | Blur and fade out at the end |

## Formats
- 16x9: 3 rows, chip 650x156, cluster at the four corners of the safe rect, headline 108 px.
- 9x16: 5 narrower rows (chip 140 px high), cluster stacks 2 above and 2 below a two-line headline inside x 70-940, y 270-1240. Rows bleed horizontally to the canvas edge (decoration); all chips start inside the safe rect.
- 1x1: 4 rows inside y 86-994; cluster inside the centre 810 px. 4x5: 5 rows.
Chip size is derived from the pitch (em = chip height / 6), so text stays as large as the format allows.

## Flash risk
None. No floods; sheen bands are 3.4 em wide and soft; no luminance steps.

## SFX cues (local time, sound kind)
- 0.28, 0.45, 0.62, 0.79: soft whoosh as each chip flies in (one per chip, slight pitch rise).
- 1.20, 1.44, 1.68, 1.92: tick (Answered pop) for each chip.
- 2.25-2.9: one light whoosh for the cluster moving into the rows.
- 2.9: low soft riser start for the marquee (optional).

## Hand-off
First frame: transparent scene, empty. Last frame (fadeOut false, t=5.5): three/five rows mid-scroll under the small headline at the top of the safe rect. With fadeOut true the scene ends blurred and fully transparent.

## Verified
Lint 0 errors. Snapshots in 16x9 (1.9, 2.4-3.2, 4.2), 9x16 (1.9, 2.9, 4.2), 1x1 (1.9, 4.2), 4x5 (4.2): no clipped text inside chips (long replies end in an ellipsis by design), nothing under the 9:16 safe insets, headline never overlaps a chip (it dissolves at 2.23 s before chips cross). Re-theme with the demo brand at 4.2 s: faces, names, fonts and colours follow the brand.

Reviewed 2026-10-21: contract grep clean; lint 0 errors; 16x9 at 1.9/3.0/4.6 and 9x16 at 2.9/4.6 fine (real chips with faces, channel glyphs and replies; headline clear of chips; the 9:16 marquee rows bleed past x 940 by design as decoration, all cluster chips start inside the safe rect). flashcheck on the 60 fps draft: PASS (0 flashes). No changes needed.
