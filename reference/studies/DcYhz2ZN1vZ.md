# DcYhz2ZN1vZ - diegotomasfx, "POV: you know how to make it Feel Premium" (Cursor product film shot on a monitor)

- Creator: Diego Tomas (@diegotomasfx). Caption: "POV: you know how to make it feel premium" with #motiondesign #animation #aftereffects #motiondesigner.
- URL: https://www.instagram.com/reel/DcYhz2ZN1vZ/
- Duration 13.1 s (video), 60 fps, 1440x2560 (9:16 vertical), 786 frames.
- Source type: vertical camera footage of a desk with an ultrawide monitor running After Effects; the animation plays in the composition viewer. It is NOT a screen recording. The analysis crop is the viewer rect: `crop=800:470:340:ceil(973-10.2*t)` in source pixels (x 340..1140, y moves from 973 at t=0 to 840 at t=13, because the plate drifts upward at a constant 10.2 source px per second). A fixed-rect equivalent at t=5 is x 320..1160, y 910..1410 (840x500). Everything below was measured on this crop. The room plate, caption and lamp were analysed on the full 1440x2560 frame.
- Song: "MONTAGEM ALQUIMIA" (per brief). Measured with librosa: 129.2 BPM (beat period 0.464 s), beats at 1.53, 2.00, 2.48, 2.95 ... 12.63 s, grid extends back to 0.14 s.
- Piece being shown: a motion-design film for the code editor Cursor ("Cursor" window, cube logo, "CURSOR" wordmark), displayed on a real monitor so the whole reel carries the proof "this is real motion work in After Effects" (timeline bars are visible at the monitor edge).

## Summary

A 13 s demonstration of how little it takes to make a product film feel premium. The camera looks at a real monitor in a warm, dim room (bar lamp on the wall, warm speaker glow, keyboard, mouse). The viewer plays a Cursor film: an orange isometric cube launches up from the bottom with an expo-out ease, is hit by a cursor arrow, a red-orange turbulent ring blasts out and the cube goes white. A card "IN PROGRESS 3 / Build Landing Page / Reading docs" appears, a scale match-cut opens it to the full Cursor window where a prompt types, the agent "reads" two files, answers and a code panel types in with a bloom on the active lines. A punch-in zoom onto the sidebar shows a warm highlight bar sliding between rows as statuses flip (IN PROGRESS 3 to READY FOR REVIEW 3 to IN PROGRESS 1, "Plan Mission Control"), a text bloom turns into orange neon light-strokes that write "Mission control interface" in a composer, a mode dropdown (Agent, Plan, Debug, Ask) picks Plan, the send button is pressed, the composer floods orange and collapses back into the cube, and the letters of "CURSOR" wipe in. The last frame is the first frame (the film loops). The caption sits on screen for exactly the first 5.6 s and disappears on the zoom punch.

## Shot list

| # | in | out | on screen | construction | camera | transition out (type, duration) | cut on beat? |
|---|----|-----|-----------|--------------|--------|--------------------------------|--------------|
| 1 | 0.00 | 0.05 | CURSOR lockup (loop frame) | last frame of the loop | locked | hard cut, 0 frames | 0.14 beat, -0.09 s |
| 2 | 0.05 | 0.65 | orange isometric cube launches from the bottom, cursor arrow sweeps in from bottom-left | 3D cube render (3 lit faces, orange #f77209) with glow, white arrow sprite with motion trail | locked | arrow hits cube, cube is nudged | 0.60 beat, +0.05 s |
| 3 | 0.65 | 1.00 | impact: red wash (#c62601), turbulent ring, cube turns white | radial wash plus noise-displaced ring (about 12 px displacement), hot-white cube | locked | wash decays over 0.25 s | beat 0.60/1.07: lands between, impact 0.70 |
| 4 | 1.00 | 1.45 | white cube holds with two soft bloom pulses (1.0 and 1.4) | glow layer pulses 1.0 to 1.6x | locked | card enters | 1.07 beat, +-0.07 |
| 5 | 1.45 | 2.20 | zoomed "IN PROGRESS 3" card: Build Landing Page, Reading docs | recreated UI card with traffic lights, spinner, 3x scale | slide up and push | scale match-cut to wide (3 frames cross-dissolve) | 2.00 beat passes; cut at 2.20, onset 2.23 |
| 6 | 2.20 | 5.70 | full Cursor window: prompt typed, agent reads files, answer, code panel with glow | recreated Cursor UI (sidebar, chat, browser/code panel), glow on typed code lines | locked, 1.0x | hard punch-in at 5.70 | 5.69 beat, exact |
| 7 | 5.70 | 7.90 | zoomed sidebar: highlight bar sliding rows, statuses flip, "Plan Mission Control" appears | 3.3x punch-in then ease-out pan; warm highlight bar #95835b | punch-in, pan down | bloom on text at 7.90 | 6.15 beat: first row-flip, 7.08 beat: "IN PROGRESS 1" |
| 8 | 7.90 | 9.45 | text blooms into orange neon strokes, composer box appears, "Mission control interface" typed | light-stroke paths (#f6611b) with trails and glow, text appearing by stroke wipes | slow push | strokes die out | 8.01 beat |
| 9 | 9.45 | 11.40 | composer with Agent chip and "Composer 1.5"; dropdown Agent (check), Plan, Debug, Ask; Plan selected | recreated UI popover, check moves from Agent to Plan, chip turns orange | locked | dropdown closes | 9.40, 10.31 beats |
| 10 | 11.40 | 12.00 | send button glows, composer fills orange, collapses to a glowing cube | orange rounded rect (blur 30 px, #e65100) scales down into the cube | scale down | cube cools | 11.70 beat |
| 11 | 12.00 | 13.10 | "CURSOR" letters wipe in from behind the cube; hold; loop | mask wipe L to R with 6-frame blur edge, white on near-black | locked | loop back to shot 1 | 12.17 beat |

## Per-shot detail

### The room plate (all shots)
- Real dim room, lens vignette, deep blacks (#0c0c0e), warm key from a bar lamp on the monitor top (a visible hot bar at about 32 percent of frame height, bright band #cac6b8), wall posters, two warm-lit speakers, keyboard and mouse at the bottom, a second monitor with a forest wallpaper at left, a Mac Studio at right. Lighting never changes with the on-screen glow (a red flood on the monitor does not tint the desk), which is how you know the viewer content is composited or is an emissive screen that is exposed away: the bright shot-3 red wash only reaches 0.1 mean luminance in the viewer.
- Constant slow drift: the lamp bar rises from y 214 to y 181 (of 640) over 13 s, i.e. 5.2 percent of frame height in 13 s, perfectly linear (about 10 source pixels per second); no hand shake (consecutive wall-pixel difference 0.6 grey levels). This is a keyframed constant-velocity push over a stable plate, so every frame feels alive but nothing wobbles.
- Caption: white rounded rectangles, black bold sans, 2 lines "POV: you know how to make / it feel premium", box x 18-82 percent, y 61-70 percent. It is a platform text overlay with no animation: on at 0.067 s and off at 5.70 s, both as hard cuts. The off cut coincides with the punch-in zoom on beat 5.69.
- Sound: bass kicks at 0.67, 0.78, 0.94, 1.09, 1.21, 1.43 (a stutter during the cube launch and impact), high-frequency ticks every 0.25-0.3 s from 3.0 to 7.5 s (typing and agent reads), kick cluster 8.19-9.88 (neon writing), kicks at 11.13, 11.84, 11.98 (collapse and cube). Silence gaps are short (rms -20 to -25 dB between).

### 2-4. Cube launch and impact (0.05-1.45 s)
- The cube is an isometric three-face render (orange #f77209 faces lit top-brightest, glow radius about 4 percent of viewer height) that starts below the frame, passes up the centre column (x 47.3 percent held within 0.7 point: pure vertical travel).
- Launch ease measured every 2 frames (cy in percent of viewer height): 91.9, 84.0, 78.7, 70.5, 64.8, 61.6, 58.9, 56.6, 54.8, 53.2, 51.9, 51.1, 50.2, 49.4, 49.1, 48.8, 48.1, 47.6. Per 2-frame step travel: 7.9, 5.3, 8.2, 5.7, 3.2, 2.7, 2.3, 1.8, 1.6, 1.3, 0.8, 0.9, 0.8, 0.3, 0.3, 0.7, 0.5. 63 percent of the 44-point move happens in the first 8 frames; 90 percent by frame 20 (0.33 s); a long tail to 0.6 s. That is a strong expo/power4 out with no overshoot. While rising, apparent size shrinks 28 px to 15.7 px (0.56x), so the cube recedes as it rises (depth cue).
- At the start the cube is yellow-hot (#ffc400) for 3 frames then settles orange: a color temperature "cooling" on the ease.
- A white cursor arrow sprite with a 3-frame motion trail sweeps in from the bottom-left (0.40-0.65) on a diagonal ease-out and hits the cube; the cube is displaced (cx 47.2 to 37.9 percent and cy 47.6 to 56.3 percent in 6 frames) and spins once.
- 0.70-0.85: a red radial wash (#c62601 / #751809 mid) floods the viewer, a ring of turbulent displacement (a ring of noise-warped glow, 8 px edge wobble) expands from the cube to the viewer edge in about 10 frames; the cube becomes white-hot (#fff) with a white halo. The viewer mean luminance goes 0.010 at 0.70 s, 0.067 at 0.75, 0.099 at 0.80, 0.040 at 0.90, 0.018 at 1.00: single-frame max step 0.033. No whole-frame flash.
- 1.0-1.45: white cube with 2 soft bloom pulses (peaks at 1.0 and 1.4), each 8 frames up and 14 frames down (asymmetric: quick attack, slow decay).

### 5-6. Card, match-cut, window (1.45-5.70 s)
- Card "IN PROGRESS 3" slides up from below the viewer (left edge x 42.2, 40.0, 39.0 percent in the first 3 frames, then 40.2-40.5 percent: ease-out with a 3-point settle). Contents: traffic-light dots, cube mark, "IN PROGRESS 3", row "Build Landing Page" with a spinner and subtitle "Reading docs", on a dark card #1b1b1f with a lighter active row #2a2824. 3x scale in the viewer (the card text is 4 percent of viewer height).
- 2.20-2.35 scale match-cut: the zoomed card hold, then 3 frames of cross-dissolve to the same card at 1x inside the full Cursor window (the card is aligned so "Build Landing Page" lands on the sidebar item). Two text layers ghost for 2 frames. This is a designed cut, not a camera pull.
- Window (1x): title "Cursor", traffic lights, sidebar with "IN PROGRESS 3": Build Landing Page (Reading docs), Analyze Tab vs Agent Usag... (Fetching data), Bioinformatics Tools (+135 -21 in green and red); main panel header "Build Landing Page". Prompt: "make a landing page based on attached docs explaining what we do". Agent: "Read about-acme.md", "Read brand-guidelines.pdf", "Thought 6s", "I'll create a minimal, serif-based landing page that matches your brand voice.", file chips "app/page.tsx +52 -0" and "app/globals.css +18 -0", "Done. Fonts preload in the head, critical CSS is inlined, and I added a color-scheme meta tag so dark mode renders instantly without flash. 280ms first paint." Right panel: browser bar "http://localhost:3000" with back/forward/reload and code `import { CursorLogoSvg } from "@/components/CursorLogoSvg";` ... `We are an applied research lab working on the future of programming.` Typed text arrives line by line with a warm yellow bloom (#d5ba7a core, #ffd34d glow, a purple/pink edge on some tokens) that peaks on the active line and fades in about 0.4 s: the bloom is attached to the caret, never to the full block.
- Typing cadence: prompt 2.4-3.0 (about 22 characters per second), file reads staggered every 0.4 s, answer 3.8-4.3, "Done." paragraph 4.5-5.3; the code panel scrolls 3.3-5.5.
- Window region is crisp, rest of the frame is plate; the viewer never shows pixel structure or moire because the viewer is exposed low (blacks stay near #0a0a0e).

### 7. Punch-in on the sidebar (5.70-7.90 s)
- 5.70: hard zoom from 1x to about 3.3x (frame 5.6 shows the small window, 5.7 the zoomed sidebar): a match-cut punch-in, landing on beat 5.69 and onset 5.67/5.69. The caption disappears on the same frame.
- 5.95-6.5: a warm highlight bar (#95835b at 40 percent) slides down the sidebar rows (about 5 frames per row) over "Build Landing Page", "Analyze Tab vs Agent Usag...", "Bioinformatics Tools"; leading icons flip spinner to check one by one; header changes from "IN PROGRESS 3" to "READY FOR REVIEW 3". The bar leaves a soft glow trail.
- 6.5-7.5: the list pans up (ease-out) and a new group "IN PROGRESS 1" appears with "Plan Mission Control / Generating plan" highlighted. 7.55-7.90: the text "Plan Mission Control" gets a white bloom that grows over 8 frames.

### 8. Neon strokes and composer (7.90-9.45 s)
- 7.95: the bloom detonates into 3-4 orange light-strokes (#f6611b core, orange glow) that draw like light-painting: stroke length extends in 6 frames with a bright head and a fading tail; strokes rotate and cross; a dark rounded composer box fades in under them (x 1-2 percent border glow in orange). The strokes are the "writing" of "Mission control interface": as each stroke dies a word appears, first "Interface" (8.7), then "Mission" (8.9), then "control" (9.1), with an orange highlight on the new word that cools to white in 6 frames.
- The viewer goes slightly red again; mean luminance stays under 0.06 here, never above 0.10 anywhere.
- Sound: 8.19-9.88 has 8 sub hits that follow stroke starts.

### 9. Mode dropdown (9.45-11.40 s)
- Composer: "Mission control interface", chips "Agent v" and "Composer 1.5 v", up arrow send. At 9.9 the "Agent" chip is pressed (chip fill lightens, 3-frame press), a popover opens upward (slide 8 px and fade, 6 frames, ease-out): Agent (checked, infinity icon), Plan, Debug, Ask. At 10.5-10.9 hover moves to Plan with a highlight row, the check mark moves from Agent to Plan with a bloom on the check; popover closes at 11.0 and the chip becomes orange "Plan" (#ff8a1a) with the send button turning amber.

### 10. Send and collapse (11.40-12.00 s)
- 11.50: send button glows; the composer fills with orange from the left in 6 frames (#e65100 to #ff6a00) with a blurred halo (halo about 30 px); at 11.62 the filled rectangle scales down and rounds into the cube (11.70, on beat), which flares white with a halo then cools to the logo cube by 12.0. This is the same cube as shot 2, so the film resolves where it began.

### 11. Logo wipe (12.00-13.10 s)
- The cube holds, drifts left 12 percent, "CURSOR" wipes in from behind it left to right over 8 frames with a blurred leading edge and a 1-frame chromatic fringe; wordmark in an extended geometric display face (white), cap height about 6 percent of viewer height, tracking +4 percent. Hold 12.35-13.1, then the file loops to the first frame (logo).
- Background gets a slight cool shift (#04090d) in the hold; the glow of the cube dies at 12.3.

## Flash profile

Computed on the viewer crop at 160 px, relative luminance, 60 fps (786 frames), and on the full frame.

- Strict floods (mean jump >= 0.1 and changed >= 0.25, up and back): none. Largest single-frame mean step 0.033 (0.77 s, the red wash). Peak viewer mean luminance 0.104 at 0.78 s; min 0.004. Max changed fraction (any frame, pixels moving >= 0.1) 0.22 at 5.72 s (the punch-in zoom). Whole frame mean luminance stays between 0.110 and 0.151 for 13 s.
- Max opposing flood transitions in any 1 s window: 0.
- Soft light events only: red wash 0.70-0.95 s (peak 0.104), sidebar highlight bar 5.95-6.5, text bloom 7.55-7.9, orange composer fill 11.5-11.7, cube flare 11.7-12.0. None is a flash in WCAG terms; all use asymmetric attack/decay (quick up, slow down).
- This is the safest film of the three and the model for our flash rule: emphasise with local bloom (a few percent of the frame), never with full-frame white.

## Copy structure

- Hook (0-0.1): caption "POV: you know how to make it feel premium" (fixed for 5.6 s) over a launching cube.
- Product moment (1.45-5.7): "IN PROGRESS 3", "Build Landing Page", prompt "make a landing page based on attached docs explaining what we do", agent answer "Done. Fonts preload in the head, critical CSS is inlined ... 280ms first paint."
- Proof (5.7-7.9): "READY FOR REVIEW 3", "Plan Mission Control / Generating plan".
- Interaction (7.9-11.4): "Mission control interface", Agent / Plan / Debug / Ask, "Composer 1.5".
- CTA: the CURSOR wordmark (no spoken or written call to action; the reel's call is the caption).

## Why this does not look AI-generated

1. It is a real room: warm lamp falloff, visible shadow-side wall posters, two speakers with a small warm light, a lens vignette, and a keyboard. Nothing synthetic carries the first-impression of authenticity.
2. The plate drifts at a perfectly constant 10 px/s; nothing is handheld or random, so a viewer reads it as a deliberate camera.
3. Each moving element has its own ease: cube expo-out (63 percent in 8 frames, 0.56x scale while rising), card ease-out with a 3-point settle, bloom pulses asymmetric (8 frames up, 14 down), neon strokes with bright heads and decaying tails, collapse that scales down with an overshoot-free ease-in.
4. The cuts are hidden by matching elements: the zoomed card cross-dissolves into the same card in the sidebar; the orange composer collapses into the same cube that launched at 0.05 s; the film loops to its own first frame.
5. Glow is spent where the story is: the active code line, the check mark, the send button; the viewer's mean luminance never exceeds 0.104.
6. Microcopy is real and specific ("+135 -21 Bioinformatics Tools", "Thought 6s", "280ms first paint", "app/page.tsx +52 -0").
7. Beat discipline: punch-in at 5.70 (beat 5.69), first row flip at 6.15 (beat 6.15), strokes at 8.0 (beat 8.01), Plan toggle ~10.3 (beat 10.31), collapse 11.7 (beat 11.70), logo wipe 12.17 (beat 12.17).
8. Asymmetric audio: kick stutter in the launch, ticks for typing, silence between clusters. The sound is a score for the animation, not a loop under it.
9. Restraint: 70 percent of the viewer is #0e0e10 dark, one accent hue (orange-red, #f77209 / #c62601), everything else grey UI.

## What would make it look AI

1. A generated room (inconsistent keycaps, melted poster text, doubled cables). Here every object is distinct at the resolution checked (720 px wide frames).
2. Whole-viewer glow on every beat, or bloom on all text at once.
3. UI with plausible but unreadable pseudo-text; the Cursor window text is readable at 2x.
4. Linear or uniform easing and constant-size motion (nothing shrinks as it rises, nothing settles).
5. A caption with an animated pop-in and random emoji (the 3 text boxes here are static, with no emoji).
6. Cube and logo morphing through generated shapes instead of a real scale-down and mask.
7. A camera that wanders with random noise instead of a constant drift.

## Archetypes

| name | t_in | t_out | construction recipe | duration | easing | flash risk | HyperFrames plan | Tidewell fit |
|------|------|-------|---------------------|----------|--------|-----------|-----------------|-----------|
| premium polish (filmed-monitor proof plate) | 0.0 | 13.1 | real or photoreal room plate, constant 5 percent push, product film on a monitor, 70 percent dark | 13 s | linear drift | none | `<video>`/`(frames not redistributed; see the original reel)` plate scaled over time; UI composite as a CSS-3D corner-pinned plane (matrix3d) over the monitor | A real agent's desk with a laptop showing Tidewell: texts arriving, Tidewell replying; reads as authentic. |
| logo/object launch + impact ring | 0.05 | 1.45 | 3D cube or icon rises from below with expo out and 0.56x scale-down, arrow hits it, turbulent ring and red wash, hot-white core | 1.4 s | expo/power4 out | low (local wash, max step 0.033) | CSS 3D cube or SVG isometric faces, GSAP; ring as radial-gradient with feTurbulence displacement; wash as a blurred div | Tidewell "E" mark launches, a text-message arrow hits it, ring pulse = "reply sent". |
| scale match cut (zoom-in punch) | 5.70 | 5.72 | the zoomed card or sidebar is aligned with its wide counterpart; 3-frame cross-dissolve | 0.05 s | hard cut | low | two scenes with identical element position, GSAP crossfade 3 frames, scale 3.3x | Jump from the zoomed "Showing booked" card into the whole inbox. |
| glow bloom (low-flash version) | 3.3 | 5.5 | warm text-shadow bloom attached to the active line only; 8-frame attack, 14-frame decay | continuous | power2 out | none | CSS text-shadow keyed by GSAP on the active span | Bloom on the "Sat 2:00 pm" reply as Tidewell types it. |
| list with swapping UI cards + toggle on | 5.95 | 7.5 | warm highlight bar slides between rows, icons flip spinner to check, header counts flip (IN PROGRESS 3 to READY FOR REVIEW 3) | 1.6 s | ease-out per row (5 frames per row) | none | absolutely positioned bar tweened with GSAP; row states via classes | Lead rows: Maria K. (Booked), Dev P. (Application sent), Jo W. (Fee paid), with a status header flipping 3 in progress to 3 ready. |
| dot -> pill -> status stack | 1.45 | 2.35 | cube becomes a pill card with spinner then a stack of status rows | 0.9 s | ease-out | none | HTML card with GSAP morph | A single "New lead" dot expands into the Tidewell status stack. |
| neon light-writing strokes | 7.95 | 9.45 | 3-4 orange light strokes with bright heads and decaying tails write words; each new word has an orange highlight cooling to white | 1.5 s | ease-out strokes, 6 frame cool | low | SVG paths with stroke-dashoffset and filter blur glow, GSAP; text appears under a mask | "Booking confirmed" written by strokes into the composer. |
| composer typing + mode dropdown + send | 9.45 | 11.7 | composer with chips, popover (Agent, Plan, Debug, Ask), check moves, chip turns orange, send glows, composer collapses into the logo | 2.3 s | popover ease-out 6 frames | low | HTML popover with GSAP; collapse via scale and border-radius | Tidewell composer: mode Reply / Book / Collect with the active mode chip turning accent; send; collapse into the Tidewell mark. |
| giant wordmark mask reveal -> lockup | 12.0 | 13.1 | letters wipe from behind the logo with a 6-frame blurred leading edge | 1.1 s | expo out | none | CSS clip-path wipe plus blur filter ramp | "Tidewell" wordmark wipes out from the E mark. |
| SaaS explainer structure (13 s) | 0 | 13.1 | hook, product moment, proof, interaction, brand lockup, loop | 13 s | n/a | none | single composition | A 13 s vertical Tidewell spot (9:16) with the same bones. |

## Frames
(frames not redistributed; see the original reel)