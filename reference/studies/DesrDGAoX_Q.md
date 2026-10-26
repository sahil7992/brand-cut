# DesrDGAoX_Q: Apple-Intelligence glow reel (xzecreative)

- Creator: xzecreative (XZE), Instagram reel. URL: https://www.instagram.com/reel/DesrDGAoX_Q/
- Caption: "Want the prompt? Comment 'Claude'... Want custom visuals for your SaaS? DM us 'video'". Burned-in overlay on the phone video: "POV: This took Claude just 30 minutes" (a creator hook line, not part of the piece).
- Duration 14.9 s, 1080x1920, 60 fps (59.97). Source type: PHONE FILMING A MONITOR (an After Effects window on a desktop display; red practical lamp ball bottom-left, keyboard and wood desk below). Screen rect: `crop=820:440:150:740` (verified on a full-res frame; the monitor bezel and AE panel edges sit just outside it, slight keystone, left edge ~2 px lower than the right).
- Song: "addiction" by LONOWN & Asenssia, 129.2 BPM (beat 0.4644 s). The reel audio is the full track starting at track time 0.46 s (cross-correlation score 1.42, next best 1.04), so reel time t = track time - 0.46. Beat grid in reel time: phase 0.295 s, beats at 4.47, 4.94, 5.40, 5.87, ... (bars of 1.858 s from the drop: 4.47, 6.33, 8.19, 10.05, 11.91, 13.76).
- Analysis method: crop, 10 fps strips (2 s each), 60 fps native-frame tracking, per-frame relative luminance, librosa onsets.

## Summary

Black screen, one living molten glow (black, deep red, red, orange, amber, cream) that morphs between a horizon band, a radial pool and two vertical light columns. White grotesk type blurs in word by word on the glow ("Turn Thoughts / Into Action / With Apple Intelligence"). Every scene change is a "bloom": hourglass columns punch in from top and bottom, the frame floods cream-orange for a fraction of a second, the old text dims underneath, then the light recedes into a different shape and the next text is already there. Mid-piece a glass app tile pops between two words, a glass pointer clicks it, and a big tilted glass slab (visionOS-like) swings in carrying avatar and app chips. Then "Just Ask", a tunnel of four real iPhones, a giant glass progress pill counting 7 to 100 percent over fanned contour lines, "Pro Workflow Unleashed" and the Apple mark, ending on a hard cut to a white card. Arc: promise (thoughts into action) -> product moment (tile, click, panel) -> proof/magic (phones, progress) -> sign-off.

## Shot list

Beat column uses the grid above (phase 0.295 s, period 0.4644 s). Times from 10 fps strips and the native-frame mean-luminance curve (+-0.05 s).

| # | in | out | on screen | construction | camera | transition out | cut on beat? |
|---|---|---|---|---|---|---|---|
| 1 | 0.00 | 1.50 | "Turn Thoughts" | shader/AE glow (horizon band contracting to red pool) + white type | type starts ~1.85x settled size lower-left, pulls back to centre | bloom: columns from top/bottom, cream peak at 1.40, 0.4 s rise, 0.3 s fall | no (1.40 is between beats 1.22 and 1.69) |
| 2 | 1.50 | 3.50 | "Into Action", then lone "With" at 2.70 | glow band at bottom (y 0.7 to 0.9) then orange pool under the word | slow drift | bloom, cream peak at 3.50 | yes (beat 3.55, -0.05 s) |
| 3 | 3.50 | 5.85 | "With [tile] Apple Intelligence" + pointer | type, glass tile (rounded square, glyph), glass pointer | static with slow drift; words push apart as tile pops (4.33) | column bloom 5.45-5.87 | yes (5.87) |
| 4 | 5.85 | 7.25 | glass slab with avatar ring, chips, search field, tile | perspective glass slab (CSS/WebGL), refracting the glow | slab swings down from above to rotateX ~25-30 deg, then drifts | slab sinks and blurs into a pool at 7.25 | no |
| 5 | 7.25 | 8.00 | "Just Ask" | type on radial orange pool | slow push in | bloom, cream peak 8.00 (impact at 7.87) | near (bar 8.19 is 0.19 s later; onset 7.87) |
| 6 | 8.40 | 10.80 | "Just Ask" -> "See The Magic", four iPhones on box walls, then floor phone flies past | real phone footage/renders, 3D box, blur | phones fly in from four edges (8.4-8.8), slow push; walls part at 10.05; floor phone tilts up and sweeps left 10.2-10.8 | hard-ish: phone fills frame with heavy motion blur, glow behind recedes to band | walls part on bar 10.05 |
| 7 | 11.15 | 12.50 | glass progress pill, "7% ... 100%", contour lines | glass capsule + number, ~9 fine red contour curves over yellow-cream gradient | pill slides in from left, lines sweep up from bottom right at ~11.7 | bloom, cream peak 12.50 | mid-beat |
| 8 | 12.80 | 14.20 | "Pro" / "Pro Workflow" / "Pro Workflow Unleashed" | type, words appended, band contracts to red pool | slow shrink | dims to dark pool | "Pro" on beat 12.83 |
| 9 | 14.20 | 14.90 | Apple logo (mark only) | white vector mark in a deep-red pool, concentric dark rings | still | column bloom 14.4-14.7 then HARD CUT to white card at 14.79 | beat 14.69 |

## Per shot detail

### 1 "Turn Thoughts" (0.00-1.50)
- Background: wide horizon band (y 0.62, red edges, orange core) at t=0 contracts sideways into a radial red pool by ~1.0 (mean luminance falls 0.09 -> 0.03). Palette: #000000, #2A0303, #7A0A00, #D81E00 (SPEC ramp).
- "Turn" appears at 0.13 at lower left (bbox x 126-294, y 225-281 in the 820x440 crop), warm orange-cream because it sits in the band; "Thoughts" arrives at 0.27 (line width jumps 168 -> 509 px).
- Tracked line width (px of 820): 0.27 s 509, 0.33 472, 0.40 400, 0.47 337, 0.53 301, 0.60 276, 0.67 258, 0.73 245, 0.80 236, 0.87 228, 0.93 221, 1.00 216, 1.07 214. Fraction of the move done: 12, 37, 58, 71, 80, 85, 89, 91, 94, 97, 99 percent. That is an expo/power4 out with no overshoot, about 0.8 s, one continuous move that covers x position and scale together (start scale ~2.4x relative to the settled width, 216 px = 26 percent of picture width). Text height settles at ~34 px of 440 = 7.7 percent of frame height (letters with descender), cap height ~5.5 percent.
- Typography: medium-weight grotesk (SF Pro Display Medium look), Title Case, letter-spacing slightly negative (about -0.02em), white with a faint warm text-shadow glow, blur-in on each word (see key_0.2s.jpg).
- Sound: soft pad at -19 to -23 dB, no percussion; the first 4.2 s are a quiet bed.

### 2 "Into Action" and lone "With" (1.50-3.50)
- After the bloom (peak mean luminance 0.25 at 1.40, 0.04 at 1.0 so a rise of +0.21 in 0.4 s, back to 0.11 by 1.7), "Into Action" is already on screen and sharp as the flood recedes (the swap of words happens at the cream peak, invisible). Glow recedes from the top: dark notch top-centre, light retreats to the bottom: horizon band at y 0.75-1.0, orange #FC6C0C core.
- 2.60: band gathers into an orange pool under the centre, "With" blurs in alone at 2.70 (single-word beat, the pool brightens behind it). Column bloom from 3.0 to the peak at 3.50 (mean 0.31).
- Sound: still pad; the bloom at 3.50 sits on beat 3.55 but there is no audible hit (low band < 3 units), the bloom is purely visual.

### 3 "With [tile] Apple Intelligence" (3.50-5.85)
- After the flood the line "With Apple Intelligence" is already complete (3.6), the second word group in an orange-amber gradient (#E49C3C to #FC840C), "With" in white. Slight blur ghost on words while the line re-centres.
- Silence gap 4.25-4.47 (RMS -74 dB, a true digital silence before the drop). In that gap, 4.33: a glass app tile (rounded square, glass bevel, 3D atom glyph) pops between "With" and "Apple": scale from ~0.5 to 1.0 in about 3 frames (key_4.3s.jpg, frames at 2-frame spacing show 0.5, 0.85, 1.0, 1.0) with a mild overshoot, words slide apart (the "With" ghost-doubles during the move = motion blur/echo, not a clean tween). The tile is ~7 percent of frame height... precisely about 37 px tall in 440 = 8.4 percent.
- 4.40: a glass pointer arrow arrives from the right edge, drifting left and down (translucent white with bevelled edge), settles under the tile by 4.9 and presses (tiny press-in).
- 4.47: the drop (kick enters, low band 8-14 units from here). The glow turns from orange horizon to a deep red band at the bottom while the text stays crisp (focus is on the type).
- 5.00: a bright crash/click hit (high band spike, 1.7 vs 0.3 average) matches the click.
- Sound/visual: tile pop inside the silence, kick on the pointer entry, cymbal on the click. Strong sync design.

### 4 Glass slab (5.85-7.25)
- Columns hourglass from 5.45 (floor 0.05 at 5.5 up to 0.26 at 5.9), the slab's front edge is already at the top of frame at 5.7 and sweeps down: front edge y travels from ~8 percent to ~85 percent of frame height in about 0.5 s (decelerating, key_5.9s.jpg, 3-frame spacing), so the slab swings down from above (not up from below as the v1 SPEC assumed). It ends as a trapezoid, rotateX roughly 25-30 deg, top edge ~78 percent of the bottom edge width.
- Slab: thick bevel with bright top-left rim, refracts and blurs the orange behind it (the glow is visible through, brighter through the glass: backdrop saturate+brightness), a faint reflection sheen. Content: avatar in a circle with a glowing magenta-violet ring (a real stylised avatar, the only coloured thing), a blue app glyph top-left, a small avatar top-right, a row of 5 small coloured app icons with labels below, a search field with fine text at bottom, and the tile (same as shot 3) centre-front. All text on the slab is tiny (illegible), it is texture.
- 6.5-7.2: concentric rings pulse out from the tile (pointer on tile), 2-3 thin rings spaced by ~0.2 s.
- Slab drifts slowly (rotateY +-3 deg). Exit: slab sinks and blurs into a pool at 7.25.
- Sound: kick pattern continues; low band swell from 7.0 to 7.9 (sub riser, values 26-32 vs 10 baseline).

### 5 "Just Ask" (7.25-8.00)
- "Just" at 7.3, "Ask" at 7.4 on an orange radial pool (0.5, 0.70), blur-in, slow push-in. Column bloom peaks 8.00 (mean 0.32; rise from 0.07 at 7.4 to 0.32 at 8.0 in 0.6 s, so slower than shot 1). Impact hit at 7.87 and a crash (hi band 1.3) at 8.0-8.1: the loudest moment so far; riser runs 7.0-7.87.

### 6 Phone tunnel (8.40-10.80)
- After the flood, text "Just Ask" is already present dark-on-orange; four phones fly in at 8.4 from beyond the four edges and settle flat on the four walls of an imaginary box (top wall upside down, left and right walls on edge, floor phone). They show real light-mode iOS screens (Wallet cards with green/blue/red tickets on top, Calendar 2026 on floor, Files/Browse on left and right). White screens against a black-red tunnel give strong depth: the walls have perspective foreshortening toward a dark-red vanishing point, orange glow floor under centre text.
- Entrance ease: phones decelerate hard (expo out) with tilt-settle, ~0.4 s; motion blur visible only while moving.
- 9.10: centre text swaps by blur cross "Just Ask" -> "See" -> "See The Magic" (words blur in one by one), on beat 9.12. 
- 10.05 (bar): walls part outward and bloom starts (hourglass, mean 0.30 -> 0.38 at 10.4), the floor phone tilts up toward the camera and sweeps off left with heavy directional motion blur and rotates ~25 deg (key_10.2s.jpg, 2-frame spacing: phone top edge rises, blur trail length ~15-20 percent of its width), exit by 10.8. The phone's screen is blown out white against the dark: because the filming camera cannot expose both, exposure dips (mean 0.30 -> 0.12 at 11.4).
- Sound: onset at 9.87 (just before the walls part), another at 10.79 (floor phone gone).

### 7 Progress pill (11.15-12.50)
- Glass capsule enters from the left (left end always off-frame) at 11.15; its right end advances with the value. Pill height measured about 37 percent of frame height (72 px of 193 in the strip tiles) and number cap height about 11 percent of frame height (a 16 percent font size), far bigger than the 14 percent pill in the v1 recreation SPEC (flag: scale up when rebuilding).
- Count: 7 (11.20), 18, 43, 64, 76, 83, 88, 92, 95, 97, 98, 99, 100 at 0.1 s steps (12.40 = 100). 1 minus value decays by a factor ~0.7 per 0.1 s = expo.out with time constant ~0.28 s over 1.2 s total. Right end of the number x (px, crop 820): 187, 223, 253, 322, 364, 424, 477, 509, 530, 560, 584, 594; the pill grows 70 percent of its travel in the first 0.5 s.
- White number in the same grotesk Medium, tabular figures, % sign same size, white with soft shadow; pill is frosted glass, brighter bevel at the right end.
- Contour lines: from ~11.7, about 9 parallel red curves (#B01000-#D01010 lines, ~1-2 px) over a yellow (#FFE000) to cream gradient band that sweeps up from bottom right, brightening toward 100.
- At 99-100 the pill takes a white specular sweep; flood bloom (columns at the top) peaks 12.50 (mean 0.37, the brightest bloom of the reel).

### 8 "Pro Workflow Unleashed" (12.80-14.20)
- After the flood: "Pro" at 12.9 (on beat 12.83), "Workflow" 13.1, "Unleashed" 13.5, each appended with a blur-in while the line re-centres (the line grows from 1 to 3 words). Background: wide orange horizon band that contracts to a red pool; text slowly shrinks and dims.

### 9 Logo end (14.20-14.90)
- Apple mark white in a deep red pool with faint dark concentric rings (banding rings visible: subtle posterised glow that makes it feel analogue), column bloom 14.4-14.7, and at 14.79 a HARD CUT to a near-white card (mean luminance jumps 0.16 -> 0.48 -> 0.62 in 2 frames; this is the only per-frame full-frame change in the reel).

## Flash profile

- Measured on the monitor crop, 160 px wide, 60 fps. Mean relative luminance runs 0.03 (dark) to 0.37 (best bloom). The phone camera's auto-exposure caps what we see; the source composition probably floods higher.
- Maximum per-frame mean change in the whole reel: 0.035 (except the final cut: +0.26 then +0.13 at 14.79-14.81, changed fraction 0.94 / 0.60). No per-frame change >= 0.1 with fraction >= 0.25 anywhere else, so by the harness's definition there are NO flicker-grade floods; all blooms are smooth 0.3-0.6 s ramps.
- Blooms (cream peak, rise from the dark floor, fall): 1.40 (+0.21 in 0.4 s, -0.14 in 0.3 s), 3.50 (+0.25 in 0.4 s), 5.90 (+0.23 in 0.5 s), 8.00 (+0.25 in 0.6 s), 10.4 (smaller, +0.08), 12.50 (+0.28 in 0.5 s), 14.5 -> white cut 14.79. That is 6 big floods in 14.9 s, one every 2.1-2.5 s: THREE TIMES denser than the client's rule (one per 8 s).
- Max opposing transitions per second: 1 pair per ~0.9 s bloom (rise + fall), so about 1.1 pairs/s, never near 3/s. Danger is repetition rate (visual pumping) more than rate-per-second.
- Low-flash version for a brand: keep the shapes, but cap peak luminance at about 0.45 relative (warm amber, not cream), make the rise 0.7-1.0 s, use at most one cream flood every 8 s and use non-flood handoffs (band swell, blur dissolve, push-through) for the rest.

## Copy structure

- Hook (0.1-1.5): "Turn Thoughts"
- Tension/promise (1.5-3.5): "Into Action" / "With"
- Product moment (3.5-7.25): "With Apple Intelligence", tile click, panel with avatar and app chips
- Proof/magic (7.25-12.5): "Just Ask", "See The Magic", phone tunnel, "7% ... 100%"
- Sign-off (12.8-14.9): "Pro Workflow Unleashed", logo. No CTA on screen (CTA is in the caption: comment "Claude").
- Exact on-screen text: "Turn Thoughts", "Into Action", "With", "With Apple Intelligence", "Just", "Just Ask", "See The Magic", "7%", "18%", "43%", "64%", "76%", "83%", "88%", "92%", "95%", "97%", "98%", "99%", "100%", "Pro", "Pro Workflow", "Pro Workflow Unleashed".

## Why this does not look AI-generated

1. One sustained light source: every scene is lit by the same glow field; glass visibly refracts it (the slab is brighter where orange sits behind it), so objects feel like they sit in the same room.
2. Banding rings in the red pool at the logo end: real gradient blurs with 8-bit posterisation and layered feathered masks, not an AI-smooth diffuse.
3. Words never pop: every word is a blur-in with its own offset, the line recentres while it grows (hand-keyed text animator), and the whole line performs one continuous pull-back with an expo-out (measured 99 percent done in 1.0 s, no overshoot).
4. Type is restrained: one medium grotesk, Title Case, 7.7 percent of frame height, no gradient except one brand word; white on dark with correct optical size.
5. Sound-to-picture sync designed in: tile pop inside a 0.22 s digital silence, drop on the pointer entry, crash on the click, riser 7.0-7.87 into the 8.0 bloom.
6. Real phone footage/renders with real iOS screens in the tunnel (calendar, wallet), not procedural UI; foreshortened accurately with motion blur only while moving.
7. Easing differentiated by object: text and glass use expo-out; the counter uses an expo decay; the phones decelerate harder; pointer drifts with a lag (not a straight line).
8. The photographic wrapper (monitor, keyboard, lamp, moire, AE panels in the bezel) makes it read as a human craft process and is an authenticity cue by itself.
9. Silence and hierarchy: only one thing moves at a time except during blooms; the type is the focal point and the glow is subordinate.

## What would make it look AI

1. Adding sparkles, floating orbs, lens flares or particles to the glow instead of soft shapes.
2. Letting every word scale-pop on every beat (beat pumping) instead of blur-in arrivals timed to bars.
3. Using a generic glass card with a uniform white border and a flat CSS blur that shows no refraction of what is behind it.
4. Hard flood cuts every ~2 s with 100 percent white: reads as strobe, as an auto-generated transition pack.
5. Fake phones (flat rectangles, procedural UI, lorem ipsum) in the tunnel, or screens where the UI cannot be read.
6. Uppercase type, italic serif accents, neon outlines, purple-blue gradients instead of the molten ramp.
7. Linear or default ease-in-out on everything, no motion blur when things move fast.

## Archetypes

| name | t_in | t_out | recipe | default duration | easing | flash risk | HyperFrames plan | Tidewell fit |
|---|---|---|---|---|---|---|---|---|
| glow bloom (low-flash version) | 1.00 | 1.70 (also 3.2-3.8, 5.45-6.0, 7.4-8.2, 12.0-12.8) | black bg + 3-4 large blurred radial/linear gradient blobs animated (hourglass columns from top and bottom edges, widen, receding to a band or pool) in the SPEC ramp; old content dims and blurs underneath, content swap under the peak | 0.7-1.0 s rise+fall (reference 0.7-0.9 s total) | power2 in-out for light, expo out for recede | high in the reference (cream peak), low if peak capped at 0.45 and used once per 8 s | one `<canvas>`/WebGL shader or stacked CSS radial-gradient divs with `filter: blur(60px)`, driven by GSAP timeline state keyframes (SPEC.md section 2 table); seek-safe because it is a pure function of time | the scene-change vehicle for all Tidewell hero films; use between "Any new leads?" and the answer |
| kinetic word blur-in | 0.13 | 1.07 | each word `opacity 0->1, blur 14px->0, scale 1.06->1` staggered 0.14 s, whole line scale ~2.4x -> 1.0 and from lower left to centre, expo.out, then slow shrink to 0.94 | 0.9 s | expo.out / power4.out | none | per-word spans, GSAP timeline `fromTo`, `filter` blur, one line container carries the pull-back | headline "Every lead, answered." |
| glass tile + pointer click | 4.33 | 5.00 | tile pops between words (scale 0.5 -> 1.05 -> 1 in 0.12 s) pushing words apart; glass pointer drifts in from the right with lag and presses (scale 0.9) then ring ripple | 0.7 s | back.out(1.6) tile, power3.out pointer | none | HTML tile with glass recipe from SPEC section 3; pointer as inline SVG; GSAP flex width tween to push words | pointer clicks the Tidewell app tile or a "Book showing" button |
| liquid glass slab | 5.70 | 7.25 | large rounded glass panel with bevel, swings in from above in perspective to rotateX 25-30 deg, drift rotateY +-3 deg, content avatar ring + chips + search field | 1.5 s settle + 1.4 s drift | power4.out | none | CSS 3D (`perspective:1600px`, `transform-style`), `backdrop-filter: blur(22px) saturate(1.5)`, gradient-border pseudo-element; fake refraction layer if backdrop capture fails | Ask Tidewell panel with a real thread/answer inside |
| photoreal phone tunnel | 8.40 | 10.80 | four phone PNG+screenshot planes on the four walls of a CSS 3D box, fly in from edges (expo.out) staggered, push in, then walls part and the floor phone tilts up and sweeps off with blur | 2.4 s | expo.out entrance, power2.in exit | low | CSS 3D scene or Three.js with real iPhone frame + real Tidewell screens (thread, calendar, approvals); directional blur via duplicated ghost layers | "All in one app": thread, calendar, approvals, payments on four phones |
| progress pill counter | 11.15 | 12.50 | glass capsule enters from left, number counts 7->100 via expo decay, contour curves sweep up, specular sweep at 100 | 1.3 s | expo.out | low | HTML capsule, counter as GSAP `onUpdate` with textContent rounded, SVG paths with stroke-dashoffset | "Leads answered" or "Application fee collected" progress to 100 percent |
| gradient opener | 0.00 | 1.50 | glow band contracting to pool under type | 1.5 s | power2.out | none | same glow canvas | opening title frame |
| premium polish | 12.80 | 14.90 | final slow shrink, mark in deep red pool with ring banding, hard cut to white card | 2 s | linear/slow sine | high only at the white cut (single frame, +0.5 luminance); soften with a 0.4 s ramp | logo SVG over radial gradient, white card via opacity ramp | end card for every product film |

## Frames
(frames not redistributed; see the original reel)