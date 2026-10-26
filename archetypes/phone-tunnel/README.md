# phone-tunnel (A09)

## What it is
Four photoreal phones fly in on the four walls of a 3D box (left, ceiling, right, floor) with real app captures on their screens, a big centre line sits in the middle, the camera pushes in with a slow roll, the centre line blur-crosses to a second line, then the walls part and the floor phone tilts up and sweeps off with heavy directional blur. Use it for "all in one app" and as a high-energy middle beat. Transparent: no backdrop, it sits on the film's glow field.

## Sources
- Glow `DesrDGAoX_Q` 8.4-10.8 s (four phone planes on the walls, expo.out staggered fly-in, centre text blur swap, push in, walls part, floor phone sweeps off).
- Our own port: `~/videos/tidewell-motion-reel-v2-2026-10-20/compositions/s06-tunnel.html` (and the v1 file). Rebuilt with `HF.phone` instead of per-wall phone PNGs, brand-token lighting, and per-format geometry.

## Duration and easing
4.4 s (default). Fly-in 0-1.15 s: power4.out position (expo-like), back.out(1.5) roll settle on its own tween, directional blur 96 px to 0 over 0.8 s. Push-in power1.inOut 0-2.8 s then sine.in to 4.1 s; camera roll -0.9 to +0.9 deg sine.inOut. Text in 0.25 s (blur 14 px to 0, 0.09 s word stagger), swap at 2.35 s, walls part 3.0-4.1 s power2.in, floor phone power2.inOut tilt/rise/pass, blur 12 px then 74 px. Nothing pulses on a beat.

## Variables
| id | type | default | meaning |
|---|---|---|---|
| screens | string | `thread\|home\|ask\|showings` | four `BRAND.ui` keys for left, top (ceiling), right, floor (home, thread, ask, askOpen, showings, showingsMonth); fewer keys cycle |
| text | string | `All in one app.` | centre line |
| text2 | string | `Built for realtors.` | line it blur-crosses to at 2.35 s; empty string = no swap |
| fadeOut | boolean | true | blur the last line out in the final 0.4 s (scene ends empty) |

## Formats
- 16x9: box half-width 600 / half-height 370, phones scale 0.80, text 112 px on one line.
- 9x16: a tall tunnel (box 455 x 450), side-wall phones larger (scale 1.02 vs 0.80), text 120 px on two lines inside x 70-940, y 270-1240. Ceiling and floor phones bleed past the safe insets by design (they are scenery, the header of each screen sits inside the safe area).
- 1x1 and 4x5: own geometry table (`G` in the script), text 104 / 112 px, centre line max width 560 / 600.
Native layouts, never crops.

## Flash risk
Low. No flood, no full-frame light. The only bright items are small screen sheens (under a quarter of the frame, soft) and the warm bounce glow on screen glass. `qa/flashcheck.py` on a 16x9 draft: PASS, 0 flashes, 0 floods.

## SFX cues (local time: sound kind)
- 0.00: whoosh, heavy (floor phone arrives)
- 0.05: whoosh, mid (left phone)
- 0.10: whoosh, mid (ceiling phone)
- 0.15: whoosh, mid (right phone)
- 0.25-0.9: soft word ticks under the centre line (optional, quiet)
- 1.00: soft thump (phones settle)
- 2.35: whoosh, short and airy (line swaps)
- 3.00: whoosh, wide (walls part)
- 3.05-3.7: whoosh with doppler/downward sweep (floor phone passes the lens)

## Hand-off
First frame: empty, transparent (phones off-frame). Last frame: empty, transparent (everything off, text blurred out) when `fadeOut` is true; with `fadeOut` false the last frame is text2 centred at 1.03x. Next scene can start from a centred line.

## Verified
- `hyperframes lint`: 0 errors, 0 warnings.
- 16x9 snapshots at 0.5, 0.6, 1.0, 1.4, 1.6, 2.0, 2.8, 3.0, 3.4, 3.5, 3.6, 4.3 s: phones big and legible, text centred, floor phone sweeps clear of the frame, last frame clean.
- 9x16 at 1.0, 1.4, 1.8, 2.9, 3.5 s: centre line inside safe insets, tall tunnel, side phones larger.
- 1x1 and 4x5 at 1.6 s: layout holds.
- Demo brand re-theme at 1.6 s: tokens, glow and captures switch, no edits.
- Draft render 16x9 30 fps (4.4 s) renders without errors; flashcheck PASS.
- Reviewer pass 2026-10-21: contract grep clean (tokens, no brand literals, no uppercase/italic/emoji, one paused timeline); lint 0 errors; 16x9 x3 and 9x16 x2 snapshots checked; 60 fps draft render flashcheck PASS (0 flashes, 0 floods). Fix: walls and floor phone dim to 0 opacity as they leave (at 60 fps the fast text-edge streaks hit WARN, 3 flashes/s over 39 percent at 3.8 s).
