# DbsyEbSR5c1 - drae.visuals, "AirPods Pro 3" Blender spec ad

- Creator: drae.visuals (Studio Atura). Caption: "what if apple hired a 19 year old with blender? ... every 3d frame is blender. after effects for the composition, the motion blur, the type, the sound design and intro. the hard part wasn't the 3d. it was the restraint ... nothing moves unless it earns it."
- URL: https://www.instagram.com/reel/DbsyEbSR5c1/
- Duration 11.10 s, 333 frames, 30 fps, 1916x1078 (16:9-ish, NOT a phone-filmed screen: native render, no crop needed).
- Source type: native render. 3D = Blender (Cycles-style grey clay-white product, no colour), composed in After Effects (type, motion blur, intro bloom, sound design).
- Song: Shazam match "Talk of the Town" (Fred again.., Sammy Virji & Reggie), librosa tempo 129.2 BPM (beat 0.464 s, bar 1.86 s). Kick/sub on the beat throughout, plus designed SFX layered on top. Treat BPM as ~129; cuts land on or within 40-80 ms after the nearest beat 5 of 7 times.

## Summary
11-second spec ad built like an Apple keynote beat sheet. Black, cyan concentric-ring bloom with "All new / Airpods Pro 3" -> black beat -> second bloom floods into a flat light-grey studio (#e5e2e6) while the charging case tumbles in -> case lid opens, buds rise and rotate, camera dollies in -> "Rebuilt from the ground up" word-by-word -> macro bud with a focus pull and orbit on a darker grey (#c8c5c9) -> ear-tip lineup "Fit, finally figured out." -> turntable -> macro stem "Touch control" with a green capacitive dot swipe -> both buds drop into the case -> hard cut to black Apple end card with disclaimer. One idea per shot, one sentence per shot, nothing decorative.

## Shot list
| # | in | out | on screen | construction | camera | transition out | on beat? |
|---|----|-----|-----------|--------------|--------|----------------|----------|
| 1 | 0.00 | 1.40 | "All new / Airpods Pro 3" in white on cyan rings | 2D: 3 concentric circles (#089eec, #08c2fa, core #a4fcfe -> white) + radial glow on #010003 black, text on top | none, rings creep outward ~1.5x radius over 1 s | 0.33 s fade of whole bloom to black (frames 1.27-1.60) | rings pop at 0.10-0.40 (kick at 0.5, +0.1 s) |
| 2 | 1.40 | 1.90 | black, faint blue base | empty beat; bloom residue fades from #000812 to #010003 | none | next bloom starts 1.87 | yes, silence in picture while kick carries (rms -10 dB at 1.4-1.5) |
| 3 | 1.90 | 2.40 | bloom 2, case tumbling in, motion-blurred | same rings, now with a 3D case (Blender, grey clay-white) rotating from side view to front | none | bloom floods to flat light grey over 0.4 s (R 43 -> 221 in 14 frames) | HF hit at 1.9 (hi band x30 spike) = bloom + case enter |
| 4 | 2.40 | 3.80 | case on #e5e2e6 | 3D: lid opens at ~2.8, two buds rise out and turn, third (left) bud rolls | dolly-in: case height 28.8% -> 76.3% of frame (2.37-3.47), then exits down 3.57-3.80 | the whole object drops out the bottom (cy 55.8 -> 65.1 -> 78.8 %) = ease-in exit | lid-open hit at 2.8 (mid band x11) |
| 5 | 3.80 | 4.60 | "Rebuilt from the ground up" | 2D type, word-stagger blur-in, black on #e5e2e6 | text line drifts down 28.8% -> 48.8% and recentres, then scales 100 -> 85% | hard cut at 4.63 to macro | cut 4.63 vs beat 4.67 (-40 ms) |
| 6 | 4.60 | 5.90 | macro bud pair, bg #c8c5c9 | 3D: two buds, strong depth-of-field; frame 1 is fully defocused then focus pulls in over ~0.2 s | pull back + orbit, upper bud flies out the top 5.4-5.6 | bud pair swapped for single bud + tips | kick 4.7, 5.1, 5.6 |
| 7 | 5.90 | 7.10 | bud + 4 ear tips + "Fit, finally figured out." | 3D bud, 4 separate silicone tips floating in a row (tips pop in 6.0-6.1), text below | static | reverse word exit 6.93-7.07, tips collapse | kick at 6.1 |
| 8 | 7.10 | 7.70 | bud turntable | 3D bud rotates 3/4 -> profile -> back, tips gone | orbit | cut 7.67 into macro (mean L -0.14) | HF spike 7.2 |
| 9 | 7.70 | 8.70 | macro of the stem "Touch control" | 3D stem with recessed touch-strip capsule; green dot (#64f902) is a 2D/emissive layer swiping up | static macro; text right of stem | stem scrolls down / camera pulls to the bud tip (8.6-8.8) | kick 7.9 = text "Touch" in; swipe peak velocity 8.10 |
| 10 | 8.70 | 9.80 | both buds + case | 3D: buds float down in 2 steps and seat into the open case; case lights its green LED | static, slow float | HARD CUT to black (mean L -0.56) | kick 9.8 vs beat 9.75 (+50 ms) |
| 11 | 9.80 | 11.10 | Apple logo + 2-line disclaimer on black | 2D white logo + 6 px type | none | end | big sub hit at 10.2 (-8 dB) |

## Per-shot detail

### Shot 1-3: ring bloom opener (0.00-2.40)
- Construction: three flat concentric discs with soft inner shading. Colours sampled: core #a4fcfe (at 0.83 s, core turning pure white by 0.4 s), ring 1 #ddfcfe, ring 2 #08c2fa, ring 3 #089eec, vignette edge #021c3b, corner #011225, frame 0 #010003. White core pixel count 240,710 at 0.30 s -> 546,218 at 1.27 s (radius x1.5 in 1 s: slow continuous zoom, not a pulse).
- Easing (mean G channel as bloom intensity): 6, 14, 24, 39, 62, 85, 106, 124, 136, 147, 155 at 0.00/0.10/0.13/0.17/0.20/0.23/0.27/0.30/0.33/0.37/0.40 s. First 0.1 s is a hold (silence at 0.3-0.5 s, -56 dB), then 0.3 s near-linear ramp that rolls into ease-out (power2.out). 83% of final at 0.40 s.
- Bloom out: mean G 150 at 1.27 s -> 10 at 1.53 s: 0.27 s fade, ease-in-out, whole group at once. This is a luminance event: mean L 0.19-0.34 -> 0.01.
- Bloom 2 (1.87-2.40): R channel 23, 43, 66, 87, 106, 117, 134, 149, 160, 171, 182, 192, 201, 211, 221 at 1.97 ... 2.40 s: 14 frames, step 20 -> 10, so ease-out linear-ish, ends exactly on the studio grey #e5e2e6. The case is already in the bloom frame (tumbling, motion blur 3-4 px along its travel).
- Type: "Airpods Pro 3" white, SF Pro Display-like, Medium (500), tracking about -1%, cap-to-descender about 7.7% of frame height, centred; "All new" same face at about 0.45x size above it. Opacity 0 -> 1 in the first 0.2 s with the rings. No italic, no all-caps.
- Sound: kick on beat 0.1, silence 0.3-0.5, kick 0.5, whoosh/shimmer high band spike 0.5-0.6 (hi 0.18), sub tail to 1.8, riser-like HF transient at 1.9-2.0 (hi 0.44, strongest HF in clip) exactly on bloom 2.

### Shot 4: case reveal (2.40-3.80)
- Real-time numbers (bounding box of non-background pixels): height % 28.8, 31.3, 32.8, 35.8, 38.7, 43.6, 52.3, 62.4, 68.6, 72.4, 74.6, 76.3 at t = 2.37, 2.47, 2.57, 2.67, 2.77, 2.87, 2.97, 3.07, 3.17, 3.27, 3.37, 3.47. Slow start (0.5 s of +2-3 %/0.1 s), peak speed ~+10 %/0.1 s at 2.9-3.1, then decay -> expo.inOut / power3.inOut dolly, no overshoot. It is a camera move, the case itself also rotates (lid opens 2.7-3.0).
- Exit: cy 55.8 (3.57), 65.1 (3.67), 78.8 (3.77): accelerating = ease-in exit, whole assembly leaves the frame bottom in 0.2 s while the text enters at 3.87.
- Materials: matte soft-touch white-grey (albedo ~#d9d9db), rounded bevels with a bright rim line on the lid edge, ao in the hinge, a green LED pin (#47d16a-ish) on the case front. No floor, no contact shadow: objects float in flat light grey, relying on form shading only (key from upper-left, large soft box, fill from right, no hard speculars except lid edge).
- Camera: slight 3/4 elevation, 85 mm look (low perspective distortion), shallow DOF visible on the rear bud.
- Sound: lid-open hit at 2.8 (mid 11.1, hi 1.5 = highest transient so far), kick 2.4, 2.8, 2.9, then a click at 3.3 (kick+hat) and a rising hat 3.7-3.8 under the exit.

### Shot 5: "Rebuilt from the ground up" (3.80-4.60)
- Words: "Rebuilt" 3.87, "from" 3.97, "the" 4.07, "ground" 4.17, "up" 4.23. Word stagger 0.07-0.10 s, each word enters with blur (about 6 px -> 0) + opacity 0->1 + about 6 px y offset (the new word sits higher than the line, settles down), colour black on #e5e2e6.
- Line translate: cy 28.8%, 31.9, 34.1, 35.4, 37.1, 38.5, 39.2, 40.4, 41.4, 41.7, 42.7, 43.6, 44.5, 45.3, 45.9, 46.5, 47.0, 47.5, 47.9, 48.2, 48.5, 48.8 over 3.87-4.57 s: steps 3.1, 2.2, 1.3, ... 0.3 = exponential decel (expo.out / power4.out), 20 % of frame height in 0.7 s and the centred line re-centres horizontally from cx 27% to 50% as words arrive.
- Scale: line width 60.2% (4.27) -> 59.6 (4.40) -> 57.2 (4.50) -> 51.5 (4.57): slow scale-down accelerating into the cut (0.85x), so the line is moving away from the viewer as the macro comes in.
- Type: SF Pro Display Semibold-ish (600), glyph height 8.0% of frame height (cap+ascender), tracking about -1.5%, sentence case, #000. No glow.
- Sound: kick at 4.2 (lo 55.8) on "ground", hat run 4.0-4.1; quiet bed 4.4-4.6 (-35 dB) = 0.2 s of near-silence before the macro hit at 4.7.

### Shot 6: macro pair (4.60-5.90)
- Frame 1 (4.63) is the cut with a 10-12 px defocus blur and +0.16 mean L recovery next frame (blur resolves in 2-3 frames = rack focus pull, ease-out). Background #c8c5c9 (darker than shot 4/5, mean L 0.52 vs 0.71).
- Buds: glossy-satin plastic, small black mic grilles with 1 px highlight; the eartip is a softer matte silicone. DOF and 10-12 px motion blur on fast rotation, derived in After Effects (user states motion blur done in AE).
- The upper bud leaves the top between 5.4 and 5.6 while the lower stays and recentres, setting up the single-bud composition of shot 7.
- Sound: kick 4.7, 5.1, 5.6; HF tick at 4.9-5.4 (hat roll).

### Shot 7: "Fit, finally figured out." (5.90-7.10)
- Four silicone ear tips (graded sizes) fly in to the right of the bud at 6.0-6.1, each with its own 1-2 frame stagger. Text line appears: "Fit," 6.07 (32 % wide), "finally" 6.13 (41.5 %), "figured" + "out." 6.20 (62.6 %): 0.13 s total, much faster than shot 5 (readability for 4 short words). Hold 6.20-6.87 (0.67 s). Exit in reverse (right to left word by word) 6.93-7.07, tips collapse toward the bud.
- Text colour #1a1a1a on #c8c5c9, bold-ish (600), glyph about 4.5% of frame height; sits below the objects, left edge aligned to the tip row.
- Sound: kick 6.1 (on text), hit 6.5 (mid 12.0, hi 1.6, the other big transient) when the tips settle.

### Shot 8-9: turntable and "Touch control" (7.10-8.70)
- Turntable 7.10-7.67: bud rotates ~140 degrees with motion blur, orbit camera; cut at 7.67 (mean L -0.14) into a macro on the stem.
- "Touch" appears 7.87 at the right of the stem, "control" blurs in 8.0-8.1 (a word later, drifting up 4 px); the pair sits at x ~ 58-70%.
- Green dot (pixel centroid, % of frame height; elongation % height): cy 98.6, 98.3, 97.5, 95.8, 93.0, 88.9, 80.7, 67.3, 53.9, 43.9, 36.8, 31.7, 27.8, 24.9, 22.9, 21.7 at 7.87-8.37 s step 0.033 s; blob height 3.3, 3.9, 5.9, 9.7, 15.5, 23.5, 30.3, 32.0, 30.7, 27.3, 25.6, 24.2, 22.4, 21.2, 20.3, 19.8. Stretch is velocity-driven: it is a velocity-based stretch (squash and stretch) with peak speed 13.4 % of frame height per frame (about 4 heights per second) at 8.10-8.13, slow start (3 frames of < 1 %), expo-out tail with ratio ~0.72 per frame. Travel 77 % in 0.5 s. It decays to a round dot at 8.40, then fades 8.40-8.50.
- Colour #64f902 (R 100, G 249, B 2), emissive with soft 12 px glow; on greyscale scene it is the only chroma accent = highest-contrast moment of the film; luminance is moderate so no flash.
- Sound: kick 7.9 (lo 58.6) aligned with "Touch"; swipe is a rising hat 8.2-8.4 (hi 0.05 -> 0.36) peaking at 8.4 with a kick (lo 45) = the swipe's top; 8.8 kick as text exits.

### Shot 10-11: lineup and end card (8.70-11.10)
- Two buds enter from above and sink into the case in two stages; the case LED glows green. Case lid hinge shows a polished metal bar. Total travel 8.8 -> 9.7 s, ease-out.
- Cut 9.80: mean L 0.47 -> 0.01 (hard cut to black, exactly one frame), kick lo 55 at 9.8 and a bigger sub hit lo 76.6 at 10.2 with the logo. End card: Apple logo white (#ffffff) on #000001, 11% of frame height wide logo at 45% height, disclaimer text 6 px grey: "This spec ad is not commissioned by Apple and is in no way associated with Apple. This is a spec ad created by user @drae.visuals, the cofounder of studio Atura".
- 1.3 s hold on black, no animation.

## Flash profile (160x90 downscale, 30 fps)
- Mean luminance range 0.001 to 0.768. Per-second mean L: 0.34, 0.19, 0.67, 0.71, 0.65, 0.54, 0.53, 0.51, 0.51, 0.47, 0.01.
- Floods (mean jump >= 0.10 and changed fraction >= 0.25): 
  - 1.37-1.40 down, -0.10 and -0.10 (46 %, 30 % of pixels): bloom fades to black.
  - 2.00-2.10 up, +0.11, +0.14, +0.14, +0.11 (38-62 %): bloom 2 floods to light grey. This is a 0.4 s ramp (L 0.19 -> 0.67), not a one-frame flash.
  - 4.63 -0.48 (99 %), 4.67 +0.16 (42 %): hard cut from light text frame to darker macro and the settling frame.
  - 7.67 -0.14 (57 %): cut to macro stem.
  - 9.80 -0.56 (100 %): hard cut to black.
- Max opposing transition pairs in any 1 s window: 1 (4.63/4.67; also 1.37 -> 2.0 within 0.66 s). Never 2 or more in 1 s, nothing near 3 Hz. Full-frame floods per 8 s: 2-3 (1.4 black, 2.0-2.4 white, 4.63 dark) in the first 5 s, i.e. denser than our 1 per 8 s rule: only acceptable because every one is a slow ramp or a single hard cut, never a strobe. Use as a data point: for a brand cap to 1 flood per 8 s and ramp at least 0.3 s.

## Copy structure
- Hook (0.0): "All new / Airpods Pro 3" (name + novelty in one frame).
- Tension / reveal (2.4): the case opening; no copy.
- Claim 1 (3.87): "Rebuilt from the ground up"
- Claim 2 (6.07): "Fit, finally figured out."
- Product moment (7.87): "Touch control" with the green swipe.
- Proof (8.8-9.7): the buds seat in the case, nothing said.
- CTA: none; end card with disclaimer. Four statements, 15 words in total, 2-3 words per second of reading time on screen.

## Why this does not look AI-generated
1. One continuous Blender camera per shot with a physically plausible dolly (28.8 -> 76 % in 1.1 s with expo in/out), not a morph or a zoom-in on a still.
2. Parts are physically separate and move with distinct timings: lid, two buds, four tips, each with its own offset and ease; AI video merges parts.
3. Depth of field and motion blur are consistent: macro frame 4.63 starts at 10-12 px blur and resolves via a focus pull; fast bud rotations have directional blur proportional to speed.
4. Flat studio grey (#e5e2e6, then #c8c5c9) without a floor or invented props; the background colour changes at a cut, never gradient noise.
5. Type is native 2D, pixel-sharp, measured to the frame: word-stagger 0.07-0.10 s, same face as the real brand, never baked into the render.
6. Single accent colour: the green dot #64f902 is the only chroma in a greyscale scene, and it is a UI-like emissive element placed exactly in the touch-strip recess.
7. Restraint: 11 shots in 11.1 s but only one thing moves at a time; 0.5 s of near-silence before the macro cut (4.4-4.6, -35 dB).
8. Sound is designed, not stock: kick + hat on the 129 BPM grid, one hit per visual event (lid at 2.8, tips at 6.5, swipe at 8.4, cut at 9.8), sub boom at the logo.
9. Honest end card: states it is a spec ad, no faux endorsement.

## What would make it look AI
1. Letting the case morph or the buds melt between shots instead of a hard cut / dolly (AI video interpolation).
2. A glossy floor with reflections and a contact shadow that does not match the key light.
3. Motion blur applied uniformly (or none) so the lid, buds and tips all smear the same way.
4. Text with a generated look: wrong kerning, ALL CAPS, italic serif, or text drawn into the 3D render so it warps with the camera.
5. Rainbow gradient rings with banding and lens-flare stars on the bloom instead of flat discs with a clean falloff.
6. Constant rotation of the product at a fixed rate in every shot (no ease, no stops), the typical turntable.
7. Green dot with a hard-edged teal bevel instead of a pure emissive blob that stretches with velocity.

## Archetypes
Names follow the library. Each: t_in-t_out | recipe | default duration | easing | flash risk | HyperFrames plan | Tidewell fit.

1. Blender product hero (photoreal grey clay hero): 2.40-3.80 and 4.60-5.90, 8.70-9.80 | Render turntable/dolly in Blender (Cycles or Eevee, soft box key, no floor), export 30/60 fps PNG or ProRes with alpha; composite type separately | 1.4 s per beat | expo.inOut dolly (no overshoot), ease-in exit | none | HF: `<video>` of the render (muted, `data-start` timed) over a flat colour div, GSAP only drives type and scale; or three.js canvas with a glTF phone model | Tidewell: a Blender iPhone with the real Tidewell Approvals screen on it rotating in as a showing request arrives; case-lid-open maps to the phone unlocking.
2. Ring bloom opener (glow bloom, low-flash version): 0.00-1.40 | 3 concentric discs (css radial-gradient, filter blur 0-2 px), brightness ramp 0.3 s, slow 1.5x scale over 1 s, then 0.3 s fade-out | 1.4 s | power2.out in, ease-in-out out | med (full-frame L 0.34 -> 0.01) | HF: 3 divs border-radius 50% + mix-blend-mode screen, GSAP scale + opacity; cap luminance peak at 0.45 mean | Tidewell: orange/maroon rings opening on "Tidewell answers in 4 seconds"; keep core cream not pure white.
3. Kinetic word blur-in (word stagger): 3.80-4.60 and 6.07-6.20 | split words, each: blur 6 px -> 0, opacity 0 -> 1, y +6 px -> 0; stagger 0.07-0.13 s | 0.5-0.8 s for 4-5 words | power3.out; line drifts with expo.out 20 % of H | none | HF: GSAP timeline, `filter: blur()`, SplitText-style manual spans; deterministic | Tidewell: "A buyer texts at 9:41 pm" / "Tidewell answers in 4 seconds" / "Showing booked".
4. Capacitive swipe dot with velocity stretch: 7.87-8.50 | emissive green blob, scaleY driven by velocity (3.3 -> 32 -> 20 % of H), travel 77 % in 0.5 s, glow blur 12 px | 0.6 s | slow-start, peak 13 %/frame, expo.out tail (ratio 0.72/frame) | low | HF: one div, GSAP y with `expo.inOut`-ish custom ease and scaleY from `onUpdate` velocity; add 1 px blur | Tidewell: accent dot dragging a "Confirm showing" slider or a toggle (Approve in Approvals) with one SFX tick.
5. Exploded part lineup (eartip row): 5.90-7.10 | 4 parts offset 20-30 px in x, staggered 1-2 frames, hold 0.7 s, collapse in reverse | 1.2 s | power3.out in / ease-in out | none | HF: 4 images with alpha + GSAP stagger | Tidewell: lead message, availability check, calendar slot, DocuSign packet as four chips in a row ("Lead", "Slot", "Application", "Fee").
6. Hard cut to black end card: 9.80-11.10 | one-frame cut + logo + 6 px disclaimer, sub hit | 1.3 s | cut | high only if previous frame bright (mean L 0.47 -> 0.01); mitigate with 0.15 s dip | HF: scene boundary, black div | Tidewell: black card with the real Tidewell wordmark and "Not a real listing" disclaimer.
7. Premium polish (restraint rules): whole | one move per beat, near-silence before the macro, 0.07-0.10 s word stagger, one accent colour | n/a | n/a | none | HF: checklist in the skill | Tidewell: 1 accent (#orange) on neutral grey scenes.
8. Rack-focus macro cut: 4.60-4.90 | cut into 10-12 px blur, resolve in 3 frames | 0.25 s | ease-out | low (cut) | HF: `filter: blur(12px)` -> 0 on a video or image layer | Tidewell: macro on a phone notification bar resolving into the real SMS bubble.

## Frames
(frames not redistributed; see the original reel)