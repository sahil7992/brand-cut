# DXzurbATRQT - youmotion.com gradient opener (After Effects template)

- Creator: youmotioncom ("ym"), template promo "Exclusively on youmotion.com #aftereffects"
- URL: https://www.instagram.com/reel/DXzurbATRQT/
- Duration 32.85 s, 60 fps, 1080x1920, NATIVE vertical (not a screen recording, no crop needed)
- Song: none identified in the metadata (uploader track field empty). Librosa: 112 BPM, beats every ~0.51-0.54 s (0.49, 0.93, 1.37, 1.86 ... 14.44 ... 22.48 ...). Tempo feels like a soft 4/4 electronic pulse. Music fades in on the first beat at 0.49 s (rms -78 dB before), fades out over the last 0.5 s.
- Scratch: /tmp/study-DXzurbATRQT, /tmp/study-scripts (flash.py, track.py, pal.py, key.sh)

## Summary

A 33 s "motion thought" template. It has two worlds. World A (0-14.4 s) is black: a light-source bloom, a lone white dot that spawns four dots, a glowing ring that morphs into a four-point star, a white pill that grows out of a dot and becomes a glossy blue-cyan glass card, then five dots turn into pins and rise. A radial white iris from the last glowing dot (14.47 s) hard-flips the whole frame to white. World B (14.5-22.3 s) is white with black pills ("Build structure", "Create rhythm", "Shape meaning") hanging off a hairline spline with a dot end; each pill takes a colour burst (purple, blue, cyan) when the line connects, slides off and the next slides in. A cyan wash from the right edge, then a hard cut back to black (22.35 s). World C (22.4-32.85 s) is black again: a dot draws an outline pill ("Connected"), the pill shoots left, three out-of-focus colour metaballs reveal "Thought in motion" as a text mask, then merge and resolve into the youmotion M mark plus "youmotion.com". A fixed caption "Project File In Description" with a travelling bold-weight sweep sits at 87.5 % height from 14.5 s to the end. Copy is one rhythm: verb or noun pair, 2-3 words, never a sentence.

## Shot list

| # | in | out | on screen | construction | camera | transition out | on beat? |
|---|----|-----|-----------|--------------|--------|----------------|----------|
| 1 | 0.10 | 1.50 | "Let's begin", rising dot + spline + volumetric elliptical light discs | 2D shader glow: radial gradient ellipses (cyan core #1594D5 to cobalt #00006C), 1 px white spline, white dots | slow descend of discs (parallax two plates) | bottom-up cyan wash 1.5-1.8 | disc appears 0.50 = beat 0.49 |
| 2 | 1.80 | 2.90 | single dot drifts, splits into 4-5 dots | pure vector dots, tiny blue bloom | none | dots become ring points | 2.9 beat |
| 3 | 2.90 | 4.40 | "With a system" inside glowing ring with 4 orbiting white dots | stroked circle with blue/teal arc glows, text under a liquid refraction (displacement map) | ring grows 83 -> 99.6 % width, settles 93 | ring-to-astroid morph | 3.0 = beat 2.9 |
| 4 | 4.40 | 5.20 | ring morphs to 4-point star shape, text blurs, shrinks into a tiny star | shape morph (concave astroid), radial/linear blur on text | rotate ~30 deg + scale 100 -> 8 % | scale to dot | 4.55 onset = beat 4.53 |
| 5 | 5.20 | 6.45 | "Finding form" + glass sparkle icon | star with glass edge (cyan/green rim, blue body), text reveals word by word | icon grows, turns to vertical bar | tiny bar | 5.83 onset |
| 6 | 6.45 | 9.25 | white pill grows from a dot, turns lavender then cobalt-cyan card "Form / Defines focus" | rounded rect with 2-stop gradient (#0A1DE6 to #01DAFA), 1 px top-left highlight, 3D tilt | card slides right, off-frame | card exits right with rotateY, star icon detaches into dot | 6.59 onset (pill peak 6.73), 9.26 onset |
| 7 | 9.30 | 14.45 | "Focus organizes motion" with 5 dots; arc swoosh hops dot to dot; dots become glowing pins; stems rise as bars; last dot climbs to centre | vector dots + gradient arc stroke (magenta #AC58E7 to cyan), bloom | none | radial white iris | 14.44 beat, strongest onset |
| 8 | 14.47 | 17.35 | WHITE. Black pill "Build structure" forms from a gradient blob, hanging from spline | gradient pill (purple to mint) resolves to #000 pill, thin grey spline 1 px, black end dot | slight sway | pill exits left (ease-in) | |
| 9 | 17.40 | 19.85 | "Create rhythm" pill slides in from right, blue burst, hold, exits left | same component, blue (#0A1DE6) fill burst from bottom edge | none | exit left | 17.74 beat |
| 10 | 19.90 | 22.00 | "Shape meaning" pill enters from top-right, cyan burst, line grows right with S-wave | same component, cyan (#00EAED) burst | none | cyan wash from right edge 22.0-22.3 | |
| 11 | 22.35 | 24.9 | BLACK. dot draws an outlined pill; "Connected" | stroke-dash trace of rounded rect, blue to green gradient glow on top edge | none | pill slides left with horizontal motion blur 24.6-25.2 | 22.48 beat (-0.13) |
| 12 | 25.3 | 29.5 | "Thought in motion" revealed by three metaballs (magenta #FF00E6-ish, blue #2C38DA, cyan #3796ED) | 3 gaussian-blurred circles with blend, text drawn then masked/dissolved word by word | blobs travel across text; then regroup | blobs contract to mark | 26.2 / 27.3 beats |
| 13 | 29.6 | 32.85 | youmotion M mark + "youmotion.com" | white vector mark, Poppins-like wordmark at 60 % grey | static | end | 28.42 onset into mark |

## Per shot detail

**Shot 1 (0.1-1.5) gradient opener.** Four tracked facts. Dot-line: the stem's bottom end y grows 66.9 -> 99.8 % in 0.6 s (linear-ish, +3 % per frame at 60 fps, ~linear), top dot holds y = 30.2 %. Two light discs (volumetric glow plates) at y 45-62 %, each an ellipse of cyan core (#1594D5 / near #00EAED) fading to cobalt (#00006C) with a hard bright underside edge, like a lamp seen from the side; they drift down (slow ease-out, ~0.8 s). "Let's begin" is Roboto-light-like, ~1.6 % frame height x-height, white at ~70 % opacity, at y 25 %, sits above the discs. Sound: first beat 0.49 coincides with the disc blooming in. Palette #000000, #000013, #00006C, #1594D5.

**Transition 1 (1.5-1.8).** Bottom-up gradient wash: blue to cyan (#00EAED 29 % of pixels at 1.7 s) rising from the bottom edge, then falling away downward in ~0.3 s leaving a lone dot. Mean luminance jump +0.13 (3-frame), changed fraction 0.59. This is the only cyan flood in World A and it never exceeds ~0.15 mean L, so it is a colour wash, not a white flash.

**Shot 3 (2.9-4.4) ring with liquid text.** 4 white dots (~1.2 % width) on a 1 px circle, with blue/teal arc "caustics" (#184959, #1DA498, #010034) that rotate. Text "With a system" arrives through a displacement-map wave (letters W..m look as if viewed through wavy glass) for ~0.5 s (3.0-3.5) then flattens to clean type. Ring width tracked in % of frame width: 83.3, 84.1, 84.8, 85.9, 88.5, 91.5, 93.0, 94.8, 96.3, 98.5, 99.6 (3.00 -> 3.73 s, 44 frames) then back to 93 by 3.93: an ease-in-out swell (slow start, fast middle, ~7 % past rest at the peak = soft overshoot, no snap). Text size ~2 % of frame height, Roboto light, white, normal tracking.

**Shot 4 (4.4-5.2) ring to star.** Ring corners pull in (concave astroid) while rotating; the text smears with directional blur (a horizontal stretch ~3x at 4.7-4.8) then everything scales to ~8 % and holds as a tiny star at 5.0-5.3. Smear is applied only during rotation (rotational motion blur), the same trick as real cameras.

**Shot 6 (6.45-9.25) dot to pill to glass card.** From the tracked bbox (bright mask, % of frame width): at 6.60 s w = 11.9, 6.633 30.4, 6.667 52.6, 6.70 70.7, 6.733 79.3 (peak), 6.80 77.8, 6.87 73.3, 6.93 71.1, then ~71.5 hold. That is ease-out with ~11 % overshoot and ~13-frame settle (back.out ~2 / spring, damped). Height 8.5 -> 11.0 -> 12.3 -> 10.6 % follows the same curve. The pill starts WHITE (#F7FCFC) with a cyan rim, cross-fades to lavender (#8F8FF0) and then to the card gradient from #0A1DE6 (left) to #01DAFA (right) in 0.3 s; text "Form" 2.4 % height, "Defines focus" smaller at ~60 % opacity, Roboto Light. A 1 px white-to-transparent stroke on the top-left edge reads as a glass bevel. Card is pushed right and partly off-frame (right edge clipped at 99.6 %), left edge at x 17.8 % moving to 24 % over 8.7 -> 9.2 s (slow creep, ~0.6 %/ 0.1 s). Exit (9.217-9.233): left edge jumps 27.8 -> 93.3 % in 1 frame: this is a motion-blur cut, accelerating (ease-in expo) so fast the card is gone in 2 frames at 60 fps, with a rotateY perspective (right side taller). The star icon separates and drifts left as a lone white sparkle, then becomes a plain dot (9.5).

**Shot 7 (9.3-14.45) dots to pins to bars.** Five white dots on a horizontal line at y ~ 52 %. An arc swoosh (stroke gradient #AC58E7 -> #14E1C0, with comet taper) hops from dot 5 to 3 to 2 (10.0-10.8 s) as if a pointer is selecting. Dots then gain a blue halo + 3 px stem (pins); at 13.2-13.9 the stems grow into bars of staggered height (a rising bar chart / pitch ladder, 4 + 1 giant tall line to 100 %), final dot climbs and moves to centre by 14.4 with a big blue halo (#2463BC, #0A0B89). "Focus organizes motion" is at y 61 % Roboto light 1.7 % height, a blue-to-white left-to-right text reveal at 10.0-10.2.

**Transition 2 (14.467-14.62) radial white iris.** Glow dot at centre (halo ~5 % width). At 14.467 a circle already covers ~41 % of the frame (53k of 130k px above L 0.5), 62 % at 14.483, 70 % at 14.50, 77 % at .517, 82 % at .533, 86 % at .55, 90 % at .567, 93 % at .583, 95 % at .60, 96 % at .617: one-frame onset then an expo-out fill of ~8 frames. The circle edge carries a cyan-to-magenta chromatic fringe (#00FFFF bottom-left, #A020F0 top-right), the edge is soft. Mean luminance 0.05 -> 0.93 within ~0.12 s, no ramp before. Onset audio 14.40-14.47 is the biggest transient in the file (a downbeat hit + riser end).

**Shots 8-10 (14.5-22.0) black pill on white.** The pill is a fully rounded rect, about 40 % of frame width by 4 % of height when settled, black #000000 with a Roboto-light white label (1.8 % height) and a blue 4-point sparkle at left. A 1 px #35363C spline (cubic) hangs from the pill's bottom centre to a 2 % black dot. Pill exit: left edge goes 13.7, 11.5, 8.5, 4.8, 0 % (frames 17.20-17.40 every 3 frames = 0.05 s steps): steps of -2.2, -3.0, -3.7, -4.8: ease-in (power2-3), 0.35 s, with a small clockwise tilt (rotate ~ -4 deg) and scale blur. Pill entrance (left edge, every 3 frames): 89.3, 79.3, 71.1, 63.7, 57.8, 52.2, 47.8, 43.7, 40.0, 37.0, 34.4, 31.9, 30.0, 28.1 %: steps 10, 8.2, 7.4, 5.9, 5.6, 4.4, 4.1, 3.7, 3.0, 2.6, 2.5, 1.9, 1.9 = geometric decay (~0.88 per step) = expo/power4 ease-out, ~0.65 s, no overshoot. The spline end (dot) travels along its own curve at a different speed than the pill (the line's tail is dragged and curls as it arrives = follow-through / overlapping action). Colour burst: when the dot reaches the pill the pill fills from the bottom with a hard-edged radial blob (purple #AC58E7 at 16.9-17.3; blue at 18.5-19.0; cyan #00EAED at 20.5-21.0), peaks within ~4 frames, then decays back to black over ~0.35 s (and rim glow stays 0.2 s longer). Caption below.

**Transition 3 (21.9-22.35).** Cyan wash enters from the right edge at 22.0 as a gradient (opaque cyan at the edge, to transparent), covering ~35 % of frame by 22.2, then a HARD CUT to black at 22.35 (mean L 0.89 -> 0.0 in one frame). This down-flip is the second flood of the pair and the harshest visual event in the file.

**Shot 11 (22.4-24.9) dot draws outlined pill.** White 1.2 % dot slides in from the right at y ~ 30 %, draws a thin white stroke that arcs into a rounded-rect outline of ~85 % width, gradient glow along the top edge (blue #1C1CFF to green #1DCB9B) which then rests as a blue rim; text "Connected" fades in letter by letter inside (2.2 % height, white, Roboto-light-like). 24.6-25.2 pill and text slide left with horizontal motion blur and disappear.

**Shot 12 (25.3-29.5) blob text.** Three gaussian blobs (sigma ~ 2.5 % of width): magenta (#E01BFF-ish), deep blue (#2C38DA), cyan (#3796ED). They float and orbit; the text "Thought in motion" is drawn behind/over the blobs and its characters brighten as blobs pass (blob acts as a reveal light). Words go out in reverse (motion leaves, then Thought at 28.1-28.4). At 29.4 the blobs gather to the logo origin and a crisp white M mark emerges, blobs quickly fade to 10 % while shrinking (29.6-29.9): a metaball merge dissolve.

**Shot 13 (29.6-32.85).** Mark (a notched rounded square, white) 3 % wide at centre y 50 %, "youmotion.com" at 54 % opacity under it; no animation for 2.7 s, only the caption sweep continues.

Caption "Project File In Description" at y 87.5 %, ~1.1 % height, Poppins regular, white on black / black on white. A bold weight sweep (3-4 letters at a time) runs left to right every ~1.2 s: variable-font weight animation = built-in activity so the bottom is never dead.

## Camera and depth

No camera. Depth is faked in three ways: (1) parallax of two light discs in shot 1, (2) rotateY/perspective on the card in shot 6, (3) defocus: blobs in shot 12 are Gaussian-blurred (sigma 2-3 % of width) so they read as out-of-focus lights next to sharp type.

## Flash profile (measured, 160 px wide, per-frame linear luminance)

- Range of frame mean L: 0.000-0.964. World A mean L under 0.07; World B ~0.91-0.94; World C ~0.01.
- Floods (mean jump >= 0.1 and >= 25 % of pixels changed): 
  1. 14.467 s up: +0.38 in one frame (41 % of pixels), +0.58 within 3 frames, full by ~14.6 s.
  2. 22.350 s down: -0.77 in one frame, 100 % of pixels changed.
  3. Sub-flood: 1.65 s cyan wash, +0.13 / 3 frames, 59 % pixels.
- Opposing pair spacing: 7.88 s (14.47 up, 22.35 down). Max opposing transitions in any 1 s window: 0 (strict definition; the pair never lands inside one second). Frequency: 1 flood per ~11 s on average.
- Verdict: within WCAG 2.3.1 (3 flashes/s) trivially, but the 22.35 hard cut white to black is a one-frame 77 % luminance drop; for a brand use a 6-frame fade or a radial iris out instead.

## Sound design

Ambient synth pad plus soft four-on-the-floor pulse. Visual events lock to onsets: 0.49 first beat = disc bloom; 1.56-1.70 wash; 4.55 star morph; 6.59-6.64 pill peak (strong hit); 9.26 card exit whoosh; 9.78-9.85 dots line up; 14.40-14.47 impact + white iris (the biggest transient in the file); the loudest bars are 18.5-19.7 s (rms -15 to -10 dB) while the pills swap; 16.72 purple burst; 18.55 pill swap; 20.76-20.78 cyan burst; 21.85-22.0 wash; 23.03-23.10 outline draw; 28.42 blobs to mark; 30.70 last sting. No separate UI SFX: all hits are the music's own percussion. Silence: only 0-0.5 s and the final 0.4 s tail.

## Copy structure

Hook: "Let's begin". Tension: "With a system", "Finding form". Product moment (the component demo): "Form / Defines focus", "Focus organizes motion", "Build structure", "Create rhythm", "Shape meaning". Proof: "Connected". Payoff: "Thought in motion". CTA: youmotion.com mark + "Project File In Description" (persistent).

## Why this does not look AI-generated

1. Every element is vector or shader: pixel-sharp 1 px splines and exact circles; no texture mush, no melting edges.
2. One idea per second, one focal point; everything else is black. AI video fills the frame.
3. Easing is asymmetric and varied: hard in (ease-in expo for exits), long expo tail for arrivals, ~11 % overshoot only on the one "alive" object (pill).
4. Overlapping action: the spline tail lags and curls after the pill has stopped; the sparkle icon detaches from the card as it exits.
5. Colour discipline: just cobalt #0A1DE6, cyan #01DAFA/#00EAED, violet #AC58E7, black and white; the colour appears only at moments of contact (burst on connect).
6. Typography is a real light-weight grotesk, one size per role, sentence case, no tracking games, no gradient text; copy is 2-3 words.
7. Persistent bottom caption with a weight sweep: designed micro-detail humans add and AI never would.
8. Morphs are topologically meaningful (dot to pill to card to dot) so the eye can follow identity.
9. Glass edge: 1 px highlight on one corner only (light direction consistent), not a uniform glow outline.

## What would make it look AI

1. Random particles drifting behind everything for "atmosphere".
2. Gradient text, rainbow glows on every element, bloom on the text itself.
3. A different ease and random duration per element (jittery linear-ish 0.3 s everything).
4. Morph blobs between unrelated shapes (cross-fade melting) instead of identity-preserving morphs.
5. A white flash on every beat.
6. Text with warped glyphs that never resolve (the "With a system" distortion works only because it resolves to clean type in 0.5 s).

## Native vertical layout (where content sits vs platform UI)

Centre of mass y 45-56 % for all hero objects; secondary text at 25 % (shot 1) and 61 % (shot 7). Caption/watermark at 87.5 %. The ring bleeds to 99.6 % width, cards bleed off the right edge. Platform UI occupies roughly the top 8 % (status/title) and bottom 20-25 % (caption, account, buttons) and the right 12 % at y 50-80 % (like/comment rail). So only the caption sits in danger, and that is intentional (creator credit). Use x 8-88 % and y 12-72 % for a brand vertical heroes, and keep caption-like content out of the right rail.

## Archetypes

| name | t_in | t_out | recipe | default duration | easing | flash risk | HyperFrames plan | Tidewell fit |
|---|---|---|---|---|---|---|---|---|
| gradient opener | 0.1 | 6.4 | black stage, light-disc glow plates, hairline spline, 4-5 dots, 2-3 word label | 6 s | ease-in-out swell, expo out | low | HTML divs + CSS radial-gradient ellipses with filter: blur; SVG paths with stroke-dashoffset in one GSAP timeline | opener "Let's begin" becomes "A lead texts at 11:42 pm" |
| glow bloom (low-flash version) | 0.5 | 1.6 | radial gradient ellipse scales 0.2 -> 1 with opacity ramp over 12 frames, never above 0.15 mean L | 1.2 s | power3.out | low | CSS radial-gradient, mix-blend screen, GSAP scale/opacity | glow behind the incoming SMS bubble |
| dot -> pill -> status stack | 6.45 | 19.9 | dot scaleX grows to pill with back.out(2) ~11 % overshoot, label fades in at 70 %, next status slides from right expo.out 0.65 s, current exits left ease-in 0.35 s, fill burst at contact | 0.65 s per swap | back.out / expo.out in / power3.in out | low | one .pill component, GSAP x/xPercent, clip-path for fill burst, CSS gradient | status chain "Replied in 4 s, Showing booked, Application sent, Fee collected" with the sparkle swapped for the Tidewell mark |
| liquid glass slab | 7.0 | 9.25 | gradient card, 1 px top-left white stroke, perspective rotateY 8-12 deg, partially off-frame | 2.2 s | slow creep then ease-in exit | low | CSS 3D transform + backdrop-filter or linear-gradient; border via mask | slab carrying the DocuSign "Application sent" card |
| radial iris flood | 14.467 | 14.62 | circle clip-path from a glow dot, expo.out 8 frames, cyan/magenta fringe via 2 offset circles | 0.13 s | expo.out | HIGH (white full frame) | clip-path: circle() animated by GSAP, hold <= 8 s apart; for a brand use cream #F6EFE6 not #FFF and fade 0.3 s | scene change from dark SMS thread to light cockpit |
| spline tether line | 15.0 | 22.0 | 1 px cubic path with end dot; tail curls after target stops | 2 s | sine.inOut | none | SVG path + MotionPathPlugin or strokeDashoffset | line from the lead's message to the booking card |
| kinetic word blur-in / liquid text | 3.0 | 3.5 | displacement-map wave on text resolving to clean type | 0.5 s | power2.out | none | SVG feTurbulence + feDisplacementMap scale animated 40 -> 0 | headline resolve "Tidewell answers instantly" |
| metaball merge to logo lockup | 25.3 | 30.0 | 3 blurred colour blobs reveal text, gather, resolve to mark, wordmark fades | 4 s | power2.inOut | low | CSS circles with filter blur 60 px + mix-blend-mode; opacity swap to SVG mark | closing lockup |
| premium polish | all | all | 1 px lines, one weight of type, restrained palette | n/a | n/a | none | design tokens | whole piece |
| stroke trace outline pill | 22.4 | 24.9 | dot draws rounded-rect stroke, glow on top edge | 1.5 s | power2.inOut | none | SVG rect stroke-dashoffset | "Connected" badge when WhatsApp links |

## Frames
(frames not redistributed; see the original reel)