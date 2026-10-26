# PATTERNS: motion archetype library (from 18 references)

Written by the lead on 2026-10-21 from `reference/studies/<id>.md` (17 reels studied frame by frame by six analysts, plus the ElevenLabs still) and the measured data in the measured study data. Every archetype names its sources with timestamps (seconds in the source file), a default duration and easing, a construction recipe, when to use it, its flash risk, and the HyperFrames plan. The skill templates live in `~/.claude/skills/brand-cut/archetypes/<dir>/` (the dir is given per entry).

Reference ids: Wise `DesrXMCIq-o` (xzecreative), Glow `DesrDGAoX_Q` (xzecreative), OpenAI `Dcn6EINyzaa` (anmoldoesmotion), Calendar `DcWXXbGKzMZ` (dija_motion), ElevenLabs still `DeaW0PvMe8j`, Brutalist `DeDaXyYoRTG` (cevox), Holo `Deq1nUPMqtr`, Change `DeKZK_ZNbUN` (jordans.archivess, + phone copy `DeOPXpGBXRq`), Coralarya `DeGb1XytuE1`, SDS `DYrpr7iztRy`, Blackbox `DdCmsxptRdM` (royrayfer), Matheus `DdUFf0FO7Cr`, Premium `DcYhz2ZN1vZ` (diegotomasfx), CodeRabbit `DdcEQPOstOH`, Figma/Higgsfield `DeM5Co3uEul` (saqibsouban), Gradient opener `DXzurbATRQT` (youmotion), Pulse `DeOxEFsItr5` (kendel4204), AirPods `DbsyEbSR5c1` (drae.visuals).

---

## 1. The laws (why none of these look AI-made)

Each law is backed by at least three references; the counterexample is what an AI-looking film does instead.

1. **Real, consistent content.** Every string is readable and true inside its world: named people with times, real amounts that repeat across shots (Pulse reuses $30,797.00, 19 customers, 212 leads; CodeRabbit shows real PR ids and diff stats; Wise uses locale-correct amounts and flags; Holo cards carry real headlines). AI tell: lorem bars, pseudo-text, numbers that change between shots.
2. **One world, one light.** A single continuous background plate or light field for the whole film (SDS silk light for 17 s, the Glow reel's one molten field that every glass object refracts, Premium's one dim room). Objects share that light: highlight top-left, contact shadow, refraction of the same field. AI tell: every scene a new random gradient; glass that refracts nothing.
3. **One accent, used physically.** One accent colour, spent on rim light, key words, the logo and moments of contact (CodeRabbit #FC5406, Figma lime highlighter boxes, Gradient opener "colour only at moments of contact", AirPods single orange). Everything else is functional colour. AI tell: neon glow on every card and word, purple-to-cyan gradients.
4. **Per-object easing, hand-set.** Measured curves differ by job: expo-out arrivals, power2.in exits, overshoot only on the one living object (Gradient opener 11% back.out on the pill only; Brutalist 3.7% spring on one word; Wise dot anticipation hold 0.2 s then sigmoid stretch). Pointers arrive fast and decelerate long with a rest before the press (Calendar: long decel, 5-frame rest, 3-4 frame press; CodeRabbit 0.15 s arrival + 0.5 s decel). AI tell: one ease-in-out 0.6 s on everything, uniform bounce, linear cursor.
5. **Shared-element continuity instead of cross-fades.** The same shape travels through the film: pill becomes window (CodeRabbit), chip becomes card becomes caret becomes light bar (Pulse), full stop becomes the next scene's dot (Brutalist), card cross-dissolves into the same sidebar card (Premium). AI tell: cross-fade between unrelated scenes.
6. **Match cuts and camera, not flashes.** Single-frame match-cut zooms to 1.9-3.3x (Calendar, Coralarya, Premium), whip pans with directional blur, push-through blur between beats (CodeRabbit), camera through a ring (OpenAI). AI tell: a white flash on every transition.
7. **Optics obey physics.** Motion blur only along the move and proportional to speed (Brutalist, AirPods), depth of field from real distance (AirPods 10-12 px macro defocus racking in 3 frames), a drum wheel whose opacity, scale and skew all derive from distance to one focus line (SDS). AI tell: uniform blur, rows that only fade.
8. **Restraint in count.** One idea per second, one focal point (Gradient opener), one moving element per beat (AirPods), four hierarchy levels and one CTA (ElevenLabs still). AI tell: everything moves at once.
9. **Human cadence.** Typing with irregular gaps (Holo 0.05-0.14 s), a blinking caret, newest letters tinted and cooling (Pulse, Coralarya), hand-drawn strokes with pressure (Change), animation on twos for drawn elements (Matheus). AI tell: metronomic typewriter, perfect vector circles for "hand-drawn".
10. **Designed silence and SFX per event.** Silence dips before the key click (Calendar 3.5-4.0 s; Glow 0.22 s digital silence before the tile pop; CodeRabbit 9.5-9.7 s), one SFX per visual event (AirPods lid 2.8, tips 6.5, swipe 8.4, cut 9.8). AI tell: wall-to-wall music, no foley.
11. **Off-black and off-white, grain.** #010101-#080509 blacks, cream whites, 6-8% grain, 8-bit banding left in the pool (Matheus, Glow). AI tell: pure #000/#FFF with diffusion-smooth gradients.
12. **Proof of making or of use.** A filmed monitor, a visible timeline, a real room (Blackbox, Premium) or real product UI in a real phone frame. AI tell: generated desks with melted posters, generated people.

**Banned in our films regardless of the references:** ALL CAPS and `text-transform: uppercase` (several refs use mono caps tags; we use sentence case), emojis, italic serif, purple AI gradients, sparkles, orbs, particles, lens flares, neon outlines (the refs' neon tube and light-writing are allowed only as a thin single-colour stroke under a quarter of the frame), fake UI, procedural phones or houses, drawn houses, 3D tags, beat-pumping.

## 2. Flash data from the references (why the rule is 1 flood per 8 s)

Measured by the analysts (mean relative luminance, opposing full-frame transitions):

| ref | max flashes/s | full-frame floods | note |
|---|---|---|---|
| Premium DcYhz2ZN1vZ | 0 | none | max frame step 0.033; the most premium piece is the least flashy |
| SDS DYrpr7iztRy | 0 | none | a black beat dims only 0.06 to 0.02 |
| Gradient opener DXzurbATRQT | 0 | 2 in 33 s | one radial iris (+0.38) |
| Pulse DeOxEFsItr5 | 0 | 3 in 52 s | one beat-aligned black-to-white cut, then 36 s of white |
| CodeRabbit DdcEQPOstOH | 1 | 1 in 69 s | one white pill at 1.45x; everything else dark-to-dark blur dissolves |
| AirPods DbsyEbSR5c1 | 1 | 2 | bloom opener + cut to black |
| Wise DesrXMCIq-o | 1 | several hard inversions | 1-3 frame dark/light inversions |
| Glow DesrDGAoX_Q | 1.1 | 6 blooms in 14.9 s | the look our v2 copied every bar |
| Matheus DdUFf0FO7Cr | 1 | 1 | one 0.93 cream slam |
| Coralarya, Holo, OpenAI, Figma, Blackbox | 2 | 1-14 | single-frame white word-swap hits (OpenAI), grey flicker frames (Figma) |
| Change DeKZK_ZNbUN | 2.3 | 19 hard steps | the saturated red/yellow wipe at 2.0 s is a red-flash risk |
| Brutalist DeDaXyYoRTG | 3 | several | rhythm montage at 3 transitions/s |
| Calendar DcWXXbGKzMZ | 4 | 1 burst | five transitions in 0.22 s at 1.6 s: over the WCAG limit |

The premium end (Premium, SDS, CodeRabbit, Pulse) floods once or never. Our flashcheck on our own v2 reel: 15 floods in 49 s and one WCAG breach (4/s at 39.5 s). House rule: at most one flood per 8 s and never more than 3 flashes in any 1 s; `qa/flashcheck.py` enforces both.

## 3. Timing vocabulary (measured)

- **Arrivals:** expo.out / power4.out, 0.45-0.8 s. CodeRabbit pill scale-down decrements 2.8, 7.5, 4.7, 3.4, 2.8, 2.2 % per frame (expo.out, no overshoot). Glow line pull-back 99% complete at 0.9 s.
- **Exits:** power2.in / power3.in 0.25-0.4 s, often with directional blur (Gradient opener slab exits in 2 frames).
- **Overshoot:** only on small living objects: back.out(1.4-1.6), 4-11% (Gradient opener pill 11%, Brutalist word 3.7%, Matheus blob 8%).
- **Anticipation:** 0.15-0.2 s dip or hold before a push (CodeRabbit 10% dip, Wise dot 0.2 s hold).
- **Pointer:** 0.15 s fast travel, 0.5 s decel, 5-frame rest, press scale 0.92 for 3-4 frames, ripple 0.2 s out + 0.2 s fade, SFX on the press frame.
- **Typing:** 9-17 characters/s with irregular gaps (0.05-0.14 s), caret blink 2 Hz, newest letters in accent cooling to ink over ~6 frames.
- **Word reveals:** blur 6-14 px to 0, opacity 0 to 1, y 4-6 px or scale 1.06 to 1, stagger 0.07-0.30 s; read words dim to 70%.
- **Counters:** geometric decay (x0.7 per 0.1 s), tabular figures, roll with jitter then lock to the round value.
- **Holds:** 0.3-0.5 s quiet holds before reveals; a scene is 3-6 s; one idea per second.
- **Camera:** continuous slow drift (scale 1.0 to 0.93-1.06 over a scene, sine.out or linear); match-cut zooms are a single-frame jump, never interpolated.
- **Cuts:** may land on beats (Figma edits within a frame of 136 BPM; Blackbox within 2 frames of 0.30 s beats). Nothing pulses on the beat.

## 4. Non-flash transition menu (use in this order)

1. **Shared-element morph** (pill to window, chip to card, dot to pill, card into sidebar). Flash: none.
2. **Match-cut zoom** (single-frame 1.9-3.3x jump onto the element the next scene starts with). Flash: none.
3. **Push-through blur** (scale 1.0 to 1.15 + blur 0 to 12 px out, next scene from 0.9 + blur in, dark to dark). Flash: none.
4. **Whip pan** (2-4 frames, horizontal blur, motion-matched). Flash: low.
5. **Mask or shape wipe** (clip-path circle from a dot, liquid edge, gradient peel). Keep the incoming luminance within 0.1 of the outgoing or ramp it over 6-8 frames. Flash: low.
6. **Camera through an object** (through a ring, a full stop, a phone tunnel). Flash: low.
7. **Glass wipe** (a tall glass slab slides across and the scene behind is replaced under the refraction). Flash: none.
8. **Light sweep** (a soft band under a quarter of the frame crossing an object). Flash: none if under 25% area.
9. **Glow bloom (low-flash)**: a pool or band that swells to at most 0.5 mean luminance and recedes over >= 0.6 s, at most once per 8 s. Flash: low when obeyed.
10. Full-frame flood: once per film section, >= 8 s apart, ramped over >= 8 frames, peak cream not white. Flash: high; flashcheck gate.

## 5. Archetypes

Format notes use the skill presets: 16x9 1920x1080 (safe 192/108), 9x16 1080x1920 (safe x 70-940, y 270-1240), 1x1 1080x1080 (hero in centre 810), 4x5 1080x1350 (centre 1012 x 1134).

### A01 Glow field (low-flash bloom) -> `glow-field`
- **Sources:** Glow DesrDGAoX_Q 0.0-14.9 (molten ramp, hourglass columns, pool, horizon band; blooms at 1.40, 3.50, 5.90, 8.00, 12.50); Gradient opener DXzurbATRQT 0.5-1.6 (radial ellipse 0.2 to 1 in 12 frames, mean L under 0.15); Premium DcYhz2ZN1vZ 3.3-5.5 (bloom attached to the active line only, 8-frame attack, 14-frame decay); Coralarya DeGb1XytuE1 9.7-12.6 (peach horizon arc under type).
- **Duration/easing:** full-film background; bloom swell power2.inOut 0.6-1.0 s, recede expo.out 0.8 s.
- **Recipe:** one WebGL fragment shader: scalar field (horizon band with tilt, radial pool, hourglass columns, corner lobes, roaming lobe, flood, rings) -> 9-stop brand ramp (`--glow-0..8`) with noise warp and triangular dither; uniforms from a monotone-Hermite keyframe table on one GSAP proxy tween. Low-flash mode: flood uniform capped so mean luminance stays <= 0.45, at most one flood per 8 s; scene changes ride pool/band moves instead.
- **Use:** behind type, glass and UI in hero films; the transition vehicle between scenes. Not behind dense reading UI.
- **Flash:** low (high if flooded every bar: v2 anti-example).
- **HF plan:** one full-length sub-composition on track 0 with the canvas; keyframes in a `KEYS` table in the file; ramp read from `window.BRAND.palette.glowRamp`; scenes above are transparent.
- **Example:** warm orange glow (or maroon) under "Any new leads?" and the Ask answer.

### A02 Liquid glass slab -> `glass-slab`
- **Sources:** Glow DesrDGAoX_Q 5.7-7.2 (swings in from above to rotateX 25-30 deg, power4.out settle, rotateY +-3 deg drift, refracts the glow); Calendar DcWXXbGKzMZ 1.9-4.1 (frosted card on a real photo, backdrop blur 24 px, 1 px specular rim 35% white, refraction rim, lower rows fade); Gradient opener DXzurbATRQT 7.0-9.2 (2-stop card, rotateY 8-12, bleeds off the edge, 2-frame blur exit).
- **Duration/easing:** 3-6 s; entry power4.out 1.0-1.3 s; drift sine.inOut.
- **Recipe:** CSS 3D (perspective 1600 px, preserve-3d); body `backdrop-filter: blur(22px) saturate(1.5) brightness(1.15)` + `linear-gradient(180deg, rgba(255,255,255,.20), rgba(255,255,255,.05))`; bevel as a masked gradient border (bright top-left .85 to .15); inner highlight `inset 0 1px 0 rgba(255,255,255,.6)`, inner shade, contact shadow `0 30px 80px rgba(0,0,0,.35)`; one sheen pass when it moves. Contents are real UI: question, streamed answer, lead rows.
- **Use:** the AI moment. The real question and the real answer must be legible for >= 2.5 s.
- **Flash:** none (fade glass out before any bloom peak; glass on cream reads as a white square).
- **HF plan:** sub-composition; answer streams word by word (0.06-0.09 s per word) from `BRAND.story.sampleAsk`; 9x16 stacks the slab full width inside safe x 70-940, taller.
- **Example:** Ask Tidewell panel: "Any new leads today?" -> the three-lead answer.

### A03 Glass tile + pointer click -> `glass-tile-click`
- **Sources:** Glow DesrDGAoX_Q 4.3-5.0 (tile pops between two words, back.out(1.6), words pushed apart with a motion-blur ghost, glass pointer from the right, press 0.9, ring ripple; inside a 0.22 s silence); CodeRabbit DdcEQPOstOH 3.7-5.5 (pixel pointer 0.15 s arrival, 0.5 s decel, press 0.92, orange ripple 0.2+0.2 s); Brutalist DeDaXyYoRTG 8.9-9.8 (toggle with ripple ring and 8 radial ticks); Figma DeM5Co3uEul 9.6-11.4 (menu + toggles on).
- **Duration/easing:** 1.8-3.7 s; tile back.out(1.6) 0.3 s; pointer power3.out travel + 5-frame rest + 3-4 frame press.
- **Recipe:** "With [tile] Tidewell" line; glass tile (96-150 px) with the brand tile art; Apple-style glass arrow pointer (46 px, glass edge, soft shadow) on a curved path; press scale 0.92; one ripple ring; SFX tap on the press frame.
- **Use:** introducing the product name or a button press (Approve and send).
- **Flash:** none (CodeRabbit's version at 1.45x white is med; enter at 1.0x).
- **HF plan:** flex line with gap tween; pointer inline SVG; `__ID__-ripple` div.
- **Example:** "With [Tidewell tile] Tidewell" and "Approve and send" on a clash card.

### A04 Kinetic word blur-in -> `word-blur-in`
- **Sources:** Glow DesrDGAoX_Q 0.1-1.1 (blur 14 px to 0, scale 1.06 to 1, stagger ~0.14 s, line starts 2.4x lower-left and pulls back to centre in one expo.out move, then shrinks to 0.94); CodeRabbit DdcEQPOstOH 0.0-3.6 (blur 8 px, 4-6 px baseline wave, stagger 0.15-0.30, read words dim to 70%, pivot word in accent); SDS DYrpr7iztRy 0.1-2.3 (karaoke playhead word tint); AirPods DbsyEbSR5c1 3.9-4.6; Pulse DeOxEFsItr5 8.4-9.0 (giant 22% word, per-letter blur 40 px).
- **Duration/easing:** 1.5-3.5 s per line; power3.out per word; line container expo.out.
- **Recipe:** split words into spans (no `<br>`), General Sans 500 84-120 px on 16x9 (5.5-7% of H), tracking `var(--track-display)`, sentence case, one accent word via colour (never gradient text on every word); slow continuous pull-back.
- **Use:** every on-screen line of copy. VO films: the line follows the VO word timing from `lines.json`.
- **Flash:** none.
- **HF plan:** variables `text`, `accent` (word index), `size`, `align`; vertical scales type to 96-132 px and wraps to 2-3 lines inside safe x.
- **Example:** "It's 9:41 pm." / "Every lead, answered." / "You just show up."

### A05 Tracking collapse -> `tracking-collapse`
- **Sources:** Wise DesrXMCIq-o 5.5-6.4 (words enter from the frame sides, gaps close in 0.3 s with ghost doubles, creeping shrink 0.5 s, then accelerating ease-in shrink to exit while a badge dot lifts out).
- **Duration/easing:** 1.2-1.8 s; expo.out close, power3.in exit.
- **Recipe:** per-word spans with x tweens (lint rejects tweening letter-spacing; move words/letters instead), 2 ghost copies at 35% and 15% opacity trailing 2 and 4 frames, optional badge dot handing off to the next scene.
- **Use:** a statement line that lands hard: "No missed leads." Hands off a dot to A07.
- **Flash:** none.
- **HF plan:** variables `text`, `dotOut` (bool); vertical stacks the words.

### A06 Real UI chip cluster -> marquee -> `chip-marquee`
- **Sources:** Wise DesrXMCIq-o 3.4-5.5 (5 chips fly in on curves with ghosting, amounts roll with jitter and lock, headline above, then 3 marquee rows overflow the frame); Pulse DeOxEFsItr5 38.3-40.7 (metric pills joined by connector chips, chain scrolls left as it grows); Holo Deq1nUPMqtr 3.1-4.9 (glass icons bobbing around a phone); CodeRabbit 29.5-35.5 (chips -> scored tags).
- **Duration/easing:** 3-4 s; arrivals expo.out 0.5 s on MotionPath curves, stagger 0.12-0.2; marquee linear.
- **Recipe:** chips are real message previews in app style: face (Commons portrait) + name + channel glyph (real WhatsApp/SMS) + the message text; cluster around a headline; then the cluster re-lays as 3 rows scrolling opposite directions under the headline.
- **Use:** "Every lead, answered": many leads at once.
- **Flash:** none (Wise's inversion cut replaced by a push-through).
- **HF plan:** chips from `BRAND.cast.leads` + a messages array variable; rows duplicated for seamless marquee; vertical uses 5 rows of narrower chips.
- **Example:** Jordan: "Is 14 Aspen Court still available?", Priya on WhatsApp: "Do you allow dogs?"... each chip gets an "Answered" tick.

### A07 Dot -> pill -> status stack -> `status-stack`
- **Sources:** Wise DesrXMCIq-o 11.1-15.0 (dot holds 0.2 s, sigmoid stretch 0.35 s with squash, text by mask, pills alternate dark/bright and offset left/right, camera scrolls up power3.out with a 2 px settle); CodeRabbit DdcEQPOstOH 43.3-63.0 (capsule stroke draws, text retypes inside the persisting outline, state label -> spinner -> check); Gradient opener DXzurbATRQT 6.5-19.9 (back.out 11% overshoot, colour fill burst at contact); Calendar 4.1-5.5; Premium 1.4-2.4.
- **Duration/easing:** 3-4 s for 5 pills; step 0.46 s; expo.out width, power3.out camera.
- **Recipe:** reference template built (see the skill). Glass dark pills alternate with bright paper pills; real partner glyphs; one sheen per pill; camera scroll keeps the stack centred.
- **Use:** recap of the flow; a loop for feeds.
- **Flash:** none.
- **HF plan:** variables `labels`, `icons`, `step`, `fadeOut`; vertical scales pills 1.3x.
- **Example:** New lead / Answered / Showing booked / Application signed / Fee paid.

### A08 Giant wordmark truck -> lockup -> `wordmark-lockup`
- **Sources:** Wise DesrXMCIq-o 0.0-1.6 (extruded 3D wordmark fills frame, camera trucks with 2-frame ghost, hard match cut to the small logo, quietest audio in the hold) and 18.6-20.8 (logo on dark then on light); OpenAI Dcn6EINyzaa 9.6-11.3 (letter-by-letter reveal with faint construction guide boxes); Premium DcYhz2ZN1vZ 12.0-13.1 (letters wipe from behind the mark, blurred leading edge); SDS 18.8-21.0 (shape wipe of arcs and bars); Pulse 47.2-49.1 (light bar sweeps, reveals wordmark, types tagline).
- **Duration/easing:** 3-6 s; truck near-linear with a start burst; lockup expo.out.
- **Recipe:** stacked text layers with translateZ (12-20 layers, darkening) for extrusion in mixed case "Tidewell"; truck x and yaw on one tween; match cut on colour to the lockup (Tidewell tile + wordmark); tagline types in. End-card variant: dark to cream by a slow wipe (not a cut) so it is not a flash.
- **Use:** open or close; logo sting.
- **Flash:** low (the Wise dark-to-light hard cut is replaced by a 0.5 s wipe).
- **HF plan:** variables `word`, `tagline`, `endTheme` (dark|paper); vertical trucks vertically or stacks the lockup.

### A09 Photoreal phone tunnel -> `phone-tunnel`
- **Sources:** Glow DesrDGAoX_Q 8.4-10.8 (four phone planes with real screens on the walls of a 3D box, fly in expo.out staggered, centre text swaps by blur cross, push in, walls part and the floor phone tilts up and sweeps off with heavy blur).
- **Duration/easing:** 3.7-5.6 s; expo.out in, power2.in out.
- **Recipe:** CSS 3D box; `BRAND.phone.frame` (photoreal, screen rect in json) with real captures (`BRAND.ui.*`); ghost-trail motion blur (4 copies at falling opacity).
- **Use:** "all in one app"; a high-energy middle beat.
- **Flash:** low.
- **HF plan:** variables `screens` (ui keys), `text`; vertical turns it into a tall tunnel (phones on left/right walls larger).

### A10 3D drum / list wheel -> `drum-wheel`
- **Sources:** SDS DYrpr7iztRy 7.9-12.6 (cylinder rows rotated ~-10 deg, focus row at exactly 50% height in white with a bullet, others ~45% pale and shrinking/skewing by distance, 0.1 s expo snaps on beats then an accelerando spin); Holo Deq1nUPMqtr 26.2-28.6 (masked list, active row black with gradient dot, 0.3-0.4 s steps with 4-frame ghost crossfade); SDS 7.0-8.0 (the full stop detaches and becomes the bullet).
- **Duration/easing:** 3-5 s; expo.out 0.1-0.35 s per step, power2.in for the final spin.
- **Recipe:** CSS 3D, perspective 1200 px; one `wheelPos` value drives every row's rotateX, translateZ, opacity, scale and skew as a function of distance from the focus line; depth fog.
- **Use:** "what it does" list.
- **Flash:** none.
- **HF plan:** variables `items` ("|" list), `lead` (static word before the wheel, e.g. "Tidewell"), `holds`.
- **Example:** "Tidewell [answers every lead | books the showing | sends the application | collects the fee]".

### A11 Card carousel -> `card-carousel`
- **Sources:** SDS DYrpr7iztRy 12.6-16.3 (ring of ~9 2:3 cards, centre ~20% W x 52% H, neighbours 0.75 scale rotateY 30-40, outer slivers darkened 40-60%, each card has its own animation, centre swaps ~0.5 s); Coralarya DeGb1XytuE1 5.9-6.9 (hard-cut montage; for us: 4-5 cards at 0.35 s with constant luminance).
- **Duration/easing:** 3-4 s; ring rotation power3.inOut per step.
- **Recipe:** CSS 3D ring, cards are real mini-UIs recreated in HTML (thread, calendar slot, DocuSign envelope, Stripe receipt, listing photo card), real home photos.
- **Use:** breadth of product surfaces.
- **Flash:** low (keep background constant).
- **HF plan:** variable `cards` (keys of built-in card kinds).

### A12 Chaos -> connected network lines -> `network-lines`
- **Sources:** OpenAI Dcn6EINyzaa 3.2-7.3 (blue origin dot with glow, 1 px wire drawn as a damped sine then forking into 8 Bezier curves staggered 2 frames, 1.2 px line icons with typed labels, close-up then pull-back, silent hold, endpoints become dots) and 0.5-3.2 (chaos hook: "too many signals / tabs / thoughts" with debris); Blackbox DdCmsxptRdM 7.4-10.0 (points converge into a mark); Pulse 16.6-19.0 (tilted node graph dolly, 12 deg to 3 deg); ElevenLabs still (orthogonal 1 px connectors with rounded elbows).
- **Duration/easing:** 4-6 s; stroke draw power2.out; camera expo.out; converge power3.in then a small back.out.
- **Recipe:** chaos: real message chips (missed calls, texts, WhatsApps, a calendar clash) drifting at 3 depths with blur by depth; then one line from the brand tile reaches each chip; chips snap to nodes; network pulls back into order. Glow only on the origin node.
- **Use:** "your day without vs with".
- **Flash:** none (OpenAI's white single frames removed).
- **HF plan:** SVG paths with `pathLength=1` dashoffset; chips HTML; variables `chaosLines` ("|" list) and `nodes`.

### A13 Composer typing over a photo + send -> `composer-send`
- **Sources:** Coralarya DeGb1XytuE1 0.9-3.8 (frosted composer with corner handles over a real photo, ~14 cps, newest word accent fading, rubber-band skew on wrap, cursor glides to send, 2x match-cut zoom, 3-stop press colour, cut back wide); OpenAI Dcn6EINyzaa 11.3-13.3 (prompt over a beach photo, whip-zoom to the send button, dolly drift); Holo 12.2-13.0 (irregular typing gaps 0.05-0.14 s); Premium 9.4-12.0 (mode popover, send glows, collapse into the logo); Figma 11.4-21.9.
- **Duration/easing:** 2.5-4 s; typing stepped with seeded irregular gaps; elastic.out(1,0.5) on wrap; match cut single frame.
- **Recipe:** real listing photo plate (slow push), iMessage/WhatsApp-style composer in the lead's phone language (not a chatbot box), typed lead message, send tap with SFX, the bubble flies up to become the first message of A23.
- **Use:** the lead's side of the story.
- **Flash:** none.
- **HF plan:** variables `text`, `photo`, `channel` (sms|whatsapp).

### A14 Radial card burst -> `card-burst`
- **Sources:** OpenAI Dcn6EINyzaa 13.3-14.4 (send tap, 14 cards fan round a hub with tilt jitter and shadows, concentric ripple rings, back.out ~6%); Holo Deq1nUPMqtr 4.9-7.2 (8 photo cards + chips fly from centre to polar positions, duotone to colour, drift, implode into a ring); Coralarya 8.4-9.7; Blackbox 10.1-11.8.
- **Duration/easing:** 1.5-2.5 s; expo.out 10 frames in, power2.in implode.
- **Recipe:** real home photos and app cards at polar positions computed with a seeded PRNG; duotone (brand ramp) to natural colour as they settle.
- **Use:** "every listing, every lead" abundance beat.
- **Flash:** low (keep the hub dark).
- **HF plan:** variables `count`, `photos` (dir), `chips`.

### A15 Code editor error -> fixed (application checklist) -> `checklist-fix`
- **Sources:** OpenAI Dcn6EINyzaa 15.5-21.0 (floating editor over a misty photo, typed code, red wash + red bar with X, "Fixing issue", 10-frame glyph scramble, corrected, green ticks); Blackbox 4.4-4.9 (speed-ramp stretch cut).
- **Duration/easing:** 3-5 s; expo/power4.out slide, no overshoot; red wash as a 6-frame ramp.
- **Recipe:** not code for a brand: a rental application checklist card (Application sent / Viewed / Signed; Fee requested / Paid). One row goes amber "Waiting on signature", then flips to green "Signed" with a tick draw; a small DocuSign status chip updates Sent -> Delivered -> Viewed -> Signed (the real statuses).
- **Use:** proof of follow-through.
- **Flash:** low (wash stays local, under 25% area).
- **HF plan:** variables `rows`, `fixRow`.

### A16 Hub with orbiting chips (Holo "gradient orb") -> `orbit-chips`
- **Sources:** Holo Deq1nUPMqtr 8.3-10.4 (giant gradient word wipe collapses into a domain-warped gradient orb with ~12 chips orbiting an ellipse with depth scale; active chip enlarges); Pulse 9.0-10.7 (orb + rings sting, rings rotate ~20 deg/s); Blackbox 5.1-7.4 (dot-matrix ring with orbiting dots).
- **Duration/easing:** 2-3 s; orbit linear with depth scale; active chip power3.out.
- **Recipe:** the hub is NOT a glowing AI orb (banned tell): it is the brand tile in glass (or the phone) lit by the glow field; chips (SMS, WhatsApp, Calendar, DocuSign, Stripe with real logos) orbit an ellipse, scale and blur by depth, the front one enlarges with its state.
- **Use:** "works where you already work", channels and tools.
- **Flash:** none.
- **HF plan:** variables `chips`, `speed`.

### A17 List with swapping UI cards + toggle on -> `list-swap-toggle`
- **Sources:** Holo Deq1nUPMqtr 15.3-23.6 (4-word list left, active black + gradient dot, glass card right with halo, slide-up swaps 0.25 out / 0.35 in, content scrolls inside, card collapses into a toggle that switches on); Premium DcYhz2ZN1vZ 6.0-7.9 (highlight bar slides 5 frames per row, spinner to check, header counts flip); CodeRabbit 18.0-22.0 (active row 1.06 with accent border, others 55%).
- **Duration/easing:** 5-8 s; expo.out card in, power2.in out, 8-frame dot glide.
- **Recipe:** left list "Texts / Showings / Applications / Fees"; right card swaps between real UI for each (thread, calendar slot, DocuSign envelope, Stripe receipt); end on a real-looking toggle "Tidewell replies" switching on (SFX click).
- **Use:** feature tour in one shot.
- **Flash:** low.
- **HF plan:** variables `items`, `toggleLabel`.

### A18 Object launch (Holo "3D mascot") -> `object-launch`
- **Sources:** Holo Deq1nUPMqtr 13.0-15.3 (pre-rendered white blob mascot with a jetpack launches from the send button, smoke arc, scale 12% to 85% in 0.4 s, breathing hold, directional blur exit); Premium DcYhz2ZN1vZ 0.1-1.4 (isometric cube rises expo.out, a cursor hits it, displaced ring + local wash).
- **Fit for a personal-assistant brand:** a mascot does not fit (the brand is a personal assistant; a cartoon reads as a toy and none exists in the brand). Use the launch grammar with a real object: the Tidewell app tile or the realtor's phone launching out of the send button, with a soft impact ring.
- **Duration/easing:** 1.5-2.3 s; expo.out scale, sine breathing hold, blur exit.
- **Flash:** low (local wash under 25%).
- **HF plan:** variables `object` (tile|phone), `ring` (bool).

### A19 Brutalist giant type + shapes -> `brutal-type`
- **Sources:** Brutalist DeDaXyYoRTG 1.5-3.0 (flat colour card grown from the dot in 3 frames, heavy lines clipped by a mask, last word slides in with horizontal blur and 3.7% spring, the full stop is a separate dot) and 2.8-3.1 (zoom through the full stop into the next scene) and 3.0-4.4 (shape morph chain with a Figma bbox); Blackbox 12.2-14.2.
- **Duration/easing:** 1.5-3 s; expo.out + 3.7% spring on one word.
- **Recipe:** huge mixed-case lines (18-26% of H) in the display face at weight 600-700 on a flat brand colour field; mask reveals per line; the period is a live dot that becomes the next scene's element (A07 dot).
- **Use:** hooks and punchlines on social cuts.
- **Flash:** med in the source (orange to cream in 3 frames); ours keeps the field change within 0.1 luminance or ramps 8 frames.
- **HF plan:** variables `lines`, `field` (accent|paper|brand), `dotHandoff`.

### A20 Icon ring + hand-drawn line -> `icon-ring`
- **Sources:** Change DeKZK_ZNbUN 6.6-8.3 (11 glossy pixel-art sprites with extruded shading and contact shadows on an ellipse, ease-out rotation, black ink brush strokes sweep and hit icons with orange bursts) and 0.9-2.0 (pen strokes with pressure variation, blurred ghost signature).
- **Fit:** the pixel-art toy look is off-brand; keep the grammar with real objects: real app/partner tiles (Tidewell, WhatsApp, Messages-style SMS bubble, Calendar, DocuSign, Stripe) in glass on an ellipse with contact shadows, and one hand-drawn pen stroke (variable width, two overlaid strokes) that circles the one that matters. Never drawn houses.
- **Duration/easing:** 1.8-3 s; power3.out rotation; pen stroke power2.out draw.
- **Flash:** low (no hard cuts around it).
- **HF plan:** variables `icons`, `circle` (index), `note` (handwritten label in the display face, not a script font).

### A21 Calendar date-pick micro-interaction -> `calendar-pick`
- **Sources:** Calendar DcWXXbGKzMZ 2.3-4.1 (range draws with discs staggered 0.07 s, cursor arrives, 1.93x match-cut zoom, decel arc to the date, 5-frame rest, 3-4 frame press -8% darker, pick-up squash into a blob, drag out with the camera panning, becomes a pill) and 2.9-4.1 (match-cut zoom + tracking pan); our v2 s07-calendar (real calendar, showing card drops in).
- **Duration/easing:** 3-4 s; expo.out no overshoot; press 0.92.
- **Recipe:** recreate the real Tidewell calendar (week view from `showings-dark.png`, app tokens), the lead's free slot glows, a tap (from the lead's side in the thread: "Saturday 11 AM") drops the showing card into the slot with a contact shadow and a "Confirmed" chip (free time auto-confirms).
- **Use:** "Showings, booked".
- **Flash:** none.
- **HF plan:** variables `day`, `time`, `lead`, `address`; 4x5 and 9x16 use the 3-day or day view, bigger.

### A22 Product hero (Blender look) -> `product-hero`
- **Sources:** AirPods DbsyEbSR5c1 2.4-3.8 (Blender soft key upper-left, fill from right, no floor, soft-touch materials with bevel rim lines, dolly 28.8% to 76% of frame in 1.1 s expo.inOut, parts move separately, exit ease-in) and 4.6-4.9 (rack-focus macro: 10-12 px defocus resolving in 3 frames) and 5.9-7.1 (exploded part lineup); Wise 15.0-17.7 (glossy card tilts and pulls back, un-tilts and pushes in 2.8x).
- **Duration/easing:** 2-4 s; expo.inOut dolly, ease-in exit.
- **Recipe:** no Blender here, so the "hero object" is the photoreal phone (`BRAND.phone.frame`) with a real capture, lit by a CSS key light (gradient sheen top-left, rim on the right edge), dolly + rotateY settle, rack-focus start; an exploded lineup of 4 real chips beside it (Lead, Slot, Application, Fee).
- **Flash:** none.
- **HF plan:** variables `screen`, `chips`, `rack` (bool).

### A23 Real message thread -> `chat-thread`
- **Sources:** our v2 s05-texts and the 2026-10-14 commercial (Jordan on SMS, real bubbles); CodeRabbit 5.5-7.4 (container transform pill -> window); Coralarya 2.0-2.7 (rubber-band grow as the reply wraps); Pulse 4.1-6.0 (typed question with caret and highlight chip).
- **Duration/easing:** 4-7 s; bubbles expo.out 0.45 s from the sender side with 4% scale settle; typing indicator 0.6-1.0 s before each Tidewell reply.
- **Recipe:** recreated Messages/WhatsApp thread inside the photoreal phone (or as a large flat thread on 16x9): lead bubble, typing dots, Tidewell's reply (the real reply text from `BRAND.story.sampleThread`, which follows the reply rules: intro "Hi! I'm Alex's assistant", no name opener, no emoji, no dashes, unsigned), a "Showing booked" system chip. Bubble pops get msg_pop SFX, the send gets a whoosh.
- **Use:** core product moment of every product film.
- **Flash:** none.
- **HF plan:** variables `channel`, `lead`, `thread` (index or "|" messages), `phone` (bool frame).

### A24 Container transform (pill to window) -> `container-morph`
- **Sources:** CodeRabbit DdcEQPOstOH 5.5-7.4 (one rect from pill size to window size while content cross-fades and the sidebar slides in; pointer exits with the pill; 12 px blur push-in at the end); Pulse 1.9-2.3 (chip loses its number, becomes a square, grows from 6% to 96% width); Pulse 6.0-6.5 (gradient peel reveals a real photo).
- **Duration/easing:** 0.5-0.9 s morph (expo.inOut) inside a 2-3 s scene.
- **Recipe:** an iOS-style notification banner ("Jordan Tate: Is 14 Aspen Court still available?") grows into the full thread view; the banner's text becomes the first bubble (shared element).
- **Flash:** none.
- **HF plan:** variables `from` (banner text), `to` (thread|card).

### A25 Notification stack over a real plate -> `notification-pile`
- **Sources:** Pulse DeOxEFsItr5 31.0-33.0 (background UI blurs 0 to 6 px, a gradient wash rises to 65% height, an iOS-style notification floats in with soft shadow) and 0.0-1.9 (count-up chip hook: "You just got 22 texts" with a chip counting 7, 16, 20, 21, 22); CodeRabbit 0.0-10.9 (problem type over clutter, then real UI pile-up); Premium (real room plate, constant 5% push).
- **Duration/easing:** 3-5 s; notifications power3.out 0.4 s, stagger accelerating (0.5, 0.35, 0.25, 0.18 s) to read as pressure; counter geometric decay.
- **Recipe:** real Pexels footage plate (dinner table / phone in hand, `BRAND.footage`), graded down 30%; iOS notifications stack (lead names, real-sounding messages, times 9:41 pm, 9:42 pm...), a count chip in the corner; then the stack freezes as Tidewell answers each (ticks).
- **Use:** the hook: the realtor's problem in one look.
- **Flash:** none.
- **HF plan:** variables `count`, `time`, `plate` (footage file), `messages`.

### A26 DocuSign signing -> `docusign-sign`
- **Sources:** our v2 s09-sign (envelope, signature drawn, Signed status); AirPods exploded lineup for the document layers; Wise 15.0-17.7 (glossy card pulls back and tilts); Change 0.9-2.0 (pressure pen stroke).
- **Duration/easing:** 3.5-4.5 s; document rises power4.out, signature path draw power2.out 0.8 s (variable width), status chip morph Sent -> Viewed -> Signed.
- **Recipe:** a realistic rental application page (form fields with the lead's name, address 14 Aspen Court, date) on paper-lit glass; the DocuSign yellow "Sign" tag; signature draws; the official DocuSign mark; status "Signed" with pen + chime SFX. Copy: "Rental application, signed." (never "lease").
- **Flash:** none.
- **HF plan:** variables `signer`, `address`, `date`.

### A27 Stripe fee paid -> `stripe-paid`
- **Sources:** our v2 s10-fee (receipt card, amount, Paid); Pulse 10.7-12.1 (dashboard zoom-out settle with counters); Holo 39.6-41.3 (digits roll with blur).
- **Duration/easing:** 3-4 s; receipt slides up power3.out; amount rolls 0.6 s with jitter then locks; "Paid" check stroke draws.
- **Recipe:** Stripe-style receipt (real Stripe mark): "Application fee $50.00, Marcus Lee, Paid", a card brand row, a timestamp; ka-ching / payment_chime SFX on Paid.
- **Flash:** none.
- **HF plan:** variables `label`, `amount`, `payer`.

### A28 Logo sting / end card -> `logo-sting`
- **Sources:** Glow DesrDGAoX_Q 12.8-14.9 (mark in a deep pool with banded rings, then a white card: we replace the hard cut with a wipe); Pulse 9.0-10.7 (orb + rings sting, wordmark types); SDS 16.4-18.8 (three dots orbit and settle into the mark); CodeRabbit 63.1-69.0 (mark hops onto a word, highlight follows the mark); Matheus 5.7-12.7 (living letter on twos); AirPods 9.8-11.1 (cut to black end card, sub hit, 1.3 s hold).
- **Duration/easing:** 4-6 s; Tidewell build = incoming bar slides 0.32 s, dot springs 0.16 s, reply bar draws 0.38 s (the brand's own animation from `the mark component`); wordmark expo.out; tagline types.
- **Recipe:** the mark builds the way the product works (message arrives, countersign, reply); a soft pool behind; endline in sentence case; url last.
- **Flash:** low.
- **HF plan:** variables `endline`, `url`, `theme`.

### A29 Branch connector tree -> `branch-tree`
- **Sources:** ElevenLabs still DeaW0PvMe8j (black parent pill branching with orthogonal 1 px rounded-elbow lines to four white partner pills stepped diagonally; grain gradient field; bottom 450 px left empty for platform UI).
- **Duration/easing:** 2-3 s; parent power3.out 0.5 s, each trunk draws 0.35 s power2.inOut, child pops back.out(1.4) 0.3 s, 0.12 s stagger.
- **Recipe:** parent = "Tidewell" pill with the tile; children = SMS, WhatsApp, Calendar, DocuSign, Stripe with real logos.
- **Flash:** none.
- **HF plan:** SVG paths with `pathLength=1`; variables `parent`, `children`.

### A30 Progress pill counter -> `counter-pill`
- **Sources:** Glow DesrDGAoX_Q 11.2-12.5 (glass capsule enters from the left with its left end off-frame, number counts 7 to 100 with expo decay, contour curves sweep, specular sweep at 100); Pulse 0.0-1.9 (count-up chip); Brutalist 9.8-10.5 (digit rolls).
- **Fit note:** a bare "Leads answered 100%" was called abstract; use with a concrete label and a concrete count ("22 texts tonight, 22 answered").
- **Duration/easing:** 2.5-3.5 s; value geometric decay; capsule power3.out.
- **Flash:** low (contour band brightens locally).
- **HF plan:** variables `label`, `from`, `to`, `suffix`.

### Structures and looks (guides, not single scenes; templates in `templates/structures/`)

- **S1 SaaS explainer structure.** CodeRabbit (69 s): hook with problem type over clutter 0-3.6, tension in real UI 3.7-10.9, reframe line 15.4-18, three product moments 22-54, promise 54-59.6, proof state change 59.6-63, logo CTA 63-69; one UI object per beat, 3-6 s each, push-through blur between beats. Pulse (52 s): dark hook number, tension question, logo sting, UI moments each with one typed sentence and one highlight chip, payoff notifications, end card. Holo (44.6 s): second-person hook 0-8, reveal 8-15, four-item demo 15-22, autopilot 22-30, volume 30-37, claim 37-40, number 40-41, typed URL CTA. OpenAI (31 s): chaos hook, connect, brand, product moment, proof, payoff, tagline, logo. **Tidewell hero = hook (9:41 pm pile-up) -> connect -> thread answer -> booking -> Ask -> signed -> paid -> recap -> "you just show up" -> lockup.**
- **S2 13 s native vertical.** Premium DcYhz2ZN1vZ: hook caption, product moment, proof statuses, interaction, brand lockup, seamless loop; constant 5% push; 70% of the viewer dark; one accent hue.
- **S3 Premium polish checklist.** Off-black/off-white + 6-8% static grain; one accent; one moving element per beat; 0.3-0.5 s quiet holds before reveals; per-event SFX with a silence dip before the key click; real microcopy; per-element easing; shared elements; a persistent caption layer; a black beat before the lockup (SDS) that dims, not flashes (Premium, SDS, AirPods, Holo, Matheus, Gradient opener).
- **S4 Dark cinematic AI (Blackbox, Figma 4.0-8.1).** Navy-black world, glowing white marks, real B&W plates with parallax streaks, glass UI cards; cuts within 2 frames of the beat. Keep the grammar, drop the flashes: luminance pulses become colour or motion pulses. Fits the night-time Tidewell hook ("9:41 pm").
- **S5 Figma/Higgsfield showcase (DeM5Co3uEul).** Hook line, triptych of three panels each with a mini-UI, hero card, recreated chat UI with a connector toggle, title card, composer with a docked thumbnail and a typed prompt, real result loading, typed bullets, logo. Highlighter boxes in the accent with ink text. Fits a "how it works in three steps" cut.
- **S6 Gradient opener (DXzurbATRQT, Holo 0.0-2.4).** Black stage, two volumetric light-disc plates, a 1 px spline with end dots, a 2-3 word label; or mask-drawn letters with a 3-colour gradient and a bright rim, a fluted blob of 5-6 offset columns. Colour only at moments of contact. Vertical-native: one focal point in the centre third.
- **S7 Matheus piece (DdUFf0FO7Cr).** Hand-made sting: stipple ring and 8-ray star, painted shard sprites, a hand-drawn zigzag, a cream flood (ours: ramp 8 frames, peak 0.6), then a living wordmark animated on twos (one letter boils inside a paper-cut square). Lesson: animate drawn elements on twos and quantise time (`floor(t*12)/12`) so they read hand-made.
- **S8 Proof plate (Premium, Blackbox).** A real room or desk plate with the film composited on the screen (CSS matrix3d corner pin, exposure low) and a constant linear push. Reads as authentic use.

## 6. Sound grammar (all references + our rules)
- One designed SFX per on-screen action: pop per bubble, whoosh per send, tap per press, snap per calendar drop, pen scribble + chime per signature, ka-ching per payment, soft hit per logo build.
- A silence dip (0.2-0.5 s) before the key click; the music ducks 3.5-6 dB under every SFX and under VO.
- VO films: a VO bed (sparse, warm, a bloom on the reveal, thinning on the quiet line, resolve on the logo). Music-only films: a hype track cut on bars; nothing visual pulses on the beat.
- End on a resolve or a tail, never a hard music stop under the logo.

## 7. Archetype -> film map (P4)
| film | lead reference grammar | archetypes |
|---|---|---|
| 1 Hero 16:9 4K + 2 hero 9:16 | S1 (CodeRabbit/Pulse/Holo) + Glow | notification-pile, network-lines, container-morph, chat-thread, calendar-pick, glass-slab, docusign-sign, stripe-paid, status-stack, word-blur-in, logo-sting, glow-field |
| 3 Teaser 15 s 9:16 | S2 Premium vertical + Pulse hook | counter-pill (count chip), chat-thread, logo-sting |
| 4 Every lead, answered 9:16 | Wise | chip-marquee, tracking-collapse, chat-thread, drum-wheel |
| 5 Ask Tidewell 16:9 + 1:1 | Glow | glow-field, glass-tile-click, glass-slab, word-blur-in |
| 6 Showings, booked 4:5 | Calendar (dija) + Holo list | composer-send, calendar-pick, list-swap-toggle |
| 7 Application signed, fee paid 9:16 | CodeRabbit shared pill + OpenAI fix | checklist-fix, docusign-sign, stripe-paid |
| 8 Without vs with 16:9 | OpenAI | network-lines (chaos), card-burst, branch-tree, orbit-chips |
| 9 Status loop 1:1 | Wise | status-stack (loop) |
| 10 Logo sting 16:9 + 9:16 | SDS/Pulse sting + Glow pool | logo-sting, word-blur-in |
