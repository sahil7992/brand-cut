# DeGb1XytuE1: whocoralarya_ (Coral Arya), "I make things move" intro

- Creator: Coral Arya (@whocoralarya_), caption "Ideas are static. Motion brings them to life."
- URL: https://www.instagram.com/reel/DeGb1XytuE1/
- Duration 12.600 s (756 frames), 60 fps, 1080x608 (16:9)
- Source: native After Effects render, no phone filming, no crop.
- Song: no metadata (track null). Librosa tempo 112.3 BPM, beat grid 0.53, 1.07, 1.63, 2.16 ... (0.534 s). Audio ends in silence at ~12.0 s (RMS -76 and -84 dB) while the final frame holds to 12.6 s.

## Summary

A designer's self-intro told as a product-like chat moment. A dotted orange orb opens on black and expands into a sunset hills photo that grades to a blue-sky day while the frame drops into a quiet scene: a frosted-white composer types "Hi, I'm Koral Arya, a Motion Designer with over 6 years of experience bringing ideas to life." (current words orange), the box skews and grows as text wraps, a cursor arrives at the send button in a 2x zoom and presses it (button cycles dark -> yellow -> pink). A hard cut to cream hands over to kinetic type on a cream background ("I turn ideas", "into visuals", "And visuals into", "Motion") with slash, chevron and asterisk glyphs flying, a thin layout grid and a peach horizon glow, and a 10 Hz slideshow of nine work cards ("Fund your D with sats", "Zero excitement.", "Zero hassle.", "GLASS" and others). The cards reassemble as a floating 3D stack that zooms in, then shrinks away and cuts to a black finale with a peach horizon: "Let's Make / Things / Move". The arc is identity -> promise -> proof (portfolio) -> invitation.

## Shot list

| # | in | out | on screen | construction | camera | transition out | cut on beat? |
|---|----|-----|-----------|--------------|--------|----------------|--------------|
| 1 | 0.00 | 0.60 | black, dotted orange orb growing | circular mask with noisy edge over a sunset hills photo, a radial halftone-dot field warped like a lens bulge | none | orb scales to full bleed, 0.3 s (ease-in-out expo) | n/a (orb starts 0.07) |
| 2 | 0.60 | 0.95 | sunset hills photo grades to blue-sky day | colour grade crossfade orange/pink -> neutral, cloud drift | slow push in | continuous | no |
| 3 | 0.95 | 2.95 | white composer types intro, orange current words, 4 corner handles | recreated chat UI over a photo; corner handles black squares fade/blur away | slow drift (clouds enlarge 6%/s) | match-cut zoom, 1 frame at 2.95 | 2.95 is 0.23 s after beat 2.72, no |
| 4 | 2.95 | 3.77 | zoom on send button + cursor + press | 2x zoom of the composer corner, hollow cursor arrow becomes filled | static + cursor | hard cut back to wide at 3.767 | yes (-0.01 s vs beat 3.78) |
| 5 | 3.77 | 4.27 | wide composer with cursor on send | same as shot 3 | none | hard cut | 4.267, 0.07 s before beat 4.34 (onset 4.23/4.34) |
| 6 | 4.27 | 5.9 | cream: "I turn ideas", "into visuals", glyph confetti | live type (typewriter then word swaps), slash/chevron/asterisk particles | none, text scale-out at end | scale down exit then grid reveal | 5.71 onset |
| 7 | 5.9 | 6.9 | grid + peach glow, 9 work cards at 10 Hz | cards centred on a 3x3 grid, hard cut each 0.1 s | none | hard cut to "And" at 6.85 | cards 6.25 ... 6.85 each 0.1 s |
| 8 | 6.9 | 8.4 | "And visuals into" -> "Motion" | kinetic type, orange words, scale-out | none | scale-down exit 8.3 | onsets 6.94, 7.62, 7.89 |
| 9 | 8.4 | 9.65 | white + peach glow + grid: 3D card stack zooms in then collapses | cards as planes in 3D with random rotation, zoom push | camera push 2x then pull to nothing | hard cut to black at 9.65 | 9.65 is 0.17 s before beat 9.82 |
| 10 | 9.65 | 12.6 | black with peach horizon: "Let's / Let's Make / Things / Move" | live type white on black, glow arc tilting | slow tilt of the glow | end | hits at 10.5, 10.63, 10.89 |

## Per shot detail

### Shot 1: dotted orange orb (0.00-0.60)
- Black #000001 (48% of the pixels at 0.3), orb colour #f8964f (13%) with shadows #b46631.
- Orb is not a sphere render: it is a circular mask with a noisy, slightly lumpy edge (radius jitter around 10%) filled with a sunset version of the hills photo (pink #e29565, orange #ef8d44, cream clouds). A feather of about 8% of the diameter.
- Around it, a field of tiny white dots (halftone, 2-3 px, spacing about 2.2% of frame width) is warped radially like a lens bulge: dots near the orb are displaced outward and elongated into short dashes, those far away stay round. This is the "dotted orb" and reads as 3D because of the displacement field, not a real sphere.
- Growth (diameter in 360 px tile frames at 30 fps): 2, 12, 22, 38, 42, 55, 80, 120, 160, 190, 220, 330, then full bleed at 0.47 s. That is slow-start, fast-finish: ease-in expo/ease-in-out (power4) for 0.45 s. No overshoot.
- Dots fade out as the orb crosses 150% of frame height (0.5 s), leaving the photo.
- Sound: orb starts after a ~0.3 s silence (onset at 0.33-0.35 in the cut detector); no audible hit.

### Shot 2: sunset -> day grade (0.60-0.95)
- Same photo, grade swaps: pink/orange #ef8d44 / #e29565 sky and gold hills -> blue sky #5fadf5, green hills #9f953e, #545e33, clouds #e4ecf6. A 0.35 s dissolve of two grades of the same plate (LUT animation), accompanied by a 6% zoom and background blur easing out (the foreground flowers go from sharp to bokeh, i.e. rack focus).
- Meanwhile a tiny black rectangle (the future composer) fades in at the horizon (x 50%, y 45%) at 0.9 s, 4 px wide, then stretches to the composer width (0.95-1.05 s, ease-out).

### Shot 3: composer + typing (0.95-2.95)
- Composer: white (#fdfdfd, 20% of pixels at 3.4) rounded rectangle, corner radius ~8% of height, soft 1 px shadow, 4 black 6 px corner handles like an AE/Figma selection box (they blur and vanish around 1.9 s). Send button: dark #1c1612 square 6% of box width, radius 25%, white up-arrow icon.
- The thin white layout grid is faintly visible over the photo for 1.0-1.8 s (1 px, 8% opacity) and fades out: a nod to design tooling.
- Typing: "Hi, I'm Koral Arya, a Motion Designer" at ~14 chars/s with a visible caret; the newest word is #e48a1e orange and decays to dark #1d1d1d over ~0.5 s (colour trail). Tracks "Hi," -> "Hi, I'm" -> "Hi, I'm Koral" -> "Koral Arya," -> "a Motion Designer". Then the line wraps ("with over 6 years of experience bringing ideas to life.") at 2.4-2.75 s.
- At 2.0-2.6 the box does a perspective/skew deformation: the right end of the box drops and the send button becomes a trapezoid (skew about 6 deg, scale on the right edge 0.9) as it grows from 1 line to 3 lines; settles with a damped wobble (about 1.5 oscillations, about 4% overshoot) by 2.7. It is a rubber-band layout transition, not a plain height tween. Height grows 40 -> 70 tile px with ease-out expo.
- Cursor: tiny arrow appears at x 82% y 58% at 2.75 s and glides toward the send button.
- Sound: onset 2.16 (expansion starts ~2.1). Onsets at 3.25 and 3.39.

### Shot 4: zoom + press (2.95-3.77)
- At 2.95 hard match-cut to a ~2.2x zoom (send button 14 -> 26 px in a 360 px tile). Text "of experience bringing" is now cropped at the top. Background photo is blurred (bokeh grass, pink flower) and slowly drifts.
- Cursor path (tile px, 30 fps, x): 258, 247, 238, 225, 213, 205, 196, 190, 184, 180: decelerating (steps 11, 9, 13, 12, 8, 9, 6, 6, 4), final approach angled (hollow outline arrow while moving, solid black arrow at contact).
- 3.5-3.6 press: cursor sits on the button, the button darkens from #1c1612 to olive #4a3d1a, then yellow #e8b83a (3.62), then dusty pink #b87c78 (3.68). The colour cycle is a 3-stop ping on a pressed state while the cursor stays. Press is three frames at 30 fps. No scale squash on the button, just colour.
- 3.77 hard cut back to the wide shot (beat 3.78): the cursor is on the button, the button is dark purple #1c1450 (press state on release).

### Shot 5: composer wide (3.77-4.27)
Held for 0.5 s with cursor on send and a tiny slow zoom; gives the viewer time to see the full composer before the cut to cream.

### Shot 6: cream kinetic type (4.27-5.9)
- Hard cut to #ebe1d0 which brightens to #fdf2db over 0.15 s (hence a 0.495 up-flood of luminance, mean 0.4 -> 0.89 with 0.88 changed fraction).
- "I turn ideas" appears typewriter-style: "I" at 4.30 (a lone 14 px orange tick), "I tu", "I turn", "I turn ide", "I turn ideas" at 4.6; the active word "ideas" orange #d98a1c shifting to a gradient brown #7a4a10, other words black #1d1208. Font: geometric sans, Poppins-like, regular weight, size ~9% of frame height, tracking 0, sentence case.
- 4.8-5.2 glyph confetti: orange asterisks (*), black and orange slashes (/), chevrons (< >) drift in from the edges and rotate, 8-14 particles, each 3% of height. They spin 30-90 deg and drift 5% of frame height over 0.5 s (ease-out). Same glyph set as the dija "Wake Up" shot, a recurring AE "type playground" technique.
- 5.0-5.5 "into visuals": "into" black then "visuals" with an orange gradient; typed in the same way. After a ~0.4 s hold the phrase shrinks to ~25% scale (ease-in) and a layout grid appears: this is how "I turn ideas" -> "into visuals" -> card burst chain.
- Onset at 5.71.

### Shot 7: cards slideshow (5.9-6.9)
- On cream #fdf2db with a thin 1 px grey grid (3 columns, 3 rows, 4 intersecting lines) and a soft peach glow #f1c37e rising at the bottom (a horizon curve 12% height).
- Nine cards appear centred, 16:9, ~55% of frame width, each ~0.1 s: (1) dark code/UI screenshot, (2) a 2x3 grid of dark UI cards, (3) "Fund your [3D icon] with sats" dark #12111a card with a violet gradient corner, (4) yellow #e8c80f card with a row of gift-card art (Amazon etc.), (5) orange #e5601a card with a woman holding a pink gift: "Zero excitement.", (6) blue-sky card with a phone in hand: "Zero hassle.", (7) runner on a salt flat (real photo), (8) pink card with five cartoon avatars, (9) navy "GLASS" with a blue 3D flower.
- Each cut is a hard cut at 10 Hz; no transition. Cards are real portfolio work (full projects), which is the proof. Cadence: 6.0, 6.07, 6.17, 6.27, 6.37, 6.47, 6.6, 6.7, 6.8 (about 0.1 s each).
- Flash note: each cut changes 15-25% of pixels; the sequence includes dark (0.12) <-> light (0.7) jumps at 6.45 (+0.115), 6.75 (-0.195) and 6.85 (+0.384). That is 3 alternating transitions in 0.4 s (peak ~5/s rate), brief.

### Shot 8: "And visuals into" -> "Motion" (6.9-8.4)
- "And visuals into" enters at 6.9 as one line, "visuals" orange, scale from 1.4x down to 1.0x with a slight blur-in, then holds 0.6 s, then scales down to 25% and exits at 7.5.
- "Motion" enters at 7.55 larger (12% of height, orange #f0a030, 30% opacity) and fades to black-brown with the letters "ti" orange; ease-out 0.3 s. Holds, scales down to small at 8.3 and the frame goes white as the cards zoom in at 8.4.
- Onsets 6.94, 7.62, 7.76, 7.89 (type hits).

### Shot 9: 3D card stack (8.4-9.65)
- White #fdfdfd bg with a 1 px grey 3x3 grid and a peach glow #fde0c7 in the upper right. About 12 portfolio cards (Born in India yellow, GFF 2025 black, "Fund your D with sats", "India" with a monument, etc.) as planes with slight 3D rotation (rotateX/Y ~10-20 deg) and random offsets, compressed into a tight stack that opens by scale: 0.08 -> 0.5 -> 1.2 of frame width during 8.4-9.2 (ease-out expo), cards also drift apart in z. After 9.2 the whole stack scales away to nothing by 9.6 (ease-in) and cuts to black at 9.65.
- Card thumbnails mix many palettes; the white bg and peach glow unify them.
- Onset 8.15 at the opening of the stack.

### Shot 10: finale (9.65-12.6)
- Black #000001; peach horizon #f4d0b1 / #ba866e with a purple falloff #361d2c (a radial gradient ellipse at the bottom, 40% of frame height, rotating a few degrees: at 10.0 the high side is on the right, at 11.0 centred, then rising on the right again by 12.0).
- White text, Poppins-like regular, ~7% of frame height. "Let's" at 9.7 (small, 30% scale, grows to 100% over 0.25 s), "Let's Make" at 9.95-10.75, "Things" 10.85-11.4 (fade-in from #151515 over 0.2 s, 0.15 s hold overlap), a dash morph into "Move" at 11.45 (hairline "-" grows into the word), "Move" held 11.5-12.6. Tracking constant, no italics, no caps.
- Onsets 10.5, 10.63, 10.89 (word hits), then silence from 12.0.

## Palette
- Orange accent #d98a1c / #e48a1e / #f8964f; brown ink #7a4a10 / #1d1208
- Cream bg #fdf2db (95% of pixel area in text shots), peach glow #f1c37e, #fde0c7, #f4d0b1, shadow purple #361d2c
- Photo: sky #5fadf5, hills #9f953e, #545e33; white UI #fdfdfd
- Black #000001; cards: yellow #e8c80f, orange #e5601a, violet #7c4dff

## Typography
Geometric humanist sans (Poppins Regular/Medium), sentence case, 7-12% of frame height for display, 1.4% for composer text; tracking 0 to -1%; two-colour words (orange accent + near-black); glyph confetti set / < > * in the same orange and black.

## Flash profile (coral, 60 fps, 160 px luminance)
- Floods: 4.267 (+0.495, frac 0.88), 6.450 (+0.115, 0.27), 6.750 (-0.195, 0.35), 6.850 (+0.384, 0.66), 9.650 (-0.835, 0.99).
- Max opposing transitions in any 1 s window: 2 (6.45 up, 6.75 down, 6.85 up). The full-frame floods are one-way: dark composer -> cream (4.27) and cream -> black (9.65), 5.4 s apart, so there is no flash pair. Mean L ranges 0.0 - 0.97.
- Mean L per 0.5 s: 0.0, 0.28, 0.33, 0.37, 0.37, 0.4, 0.41, 0.38, 0.41, 0.89, 0.88, 0.89, 0.84, 0.72, 0.89, 0.89, 0.89, 0.9, 0.8, 0.8, 0.12 ...
- Largest threat for our rule: the 10 Hz card slideshow (shot 7), but it alternates over 0.4 s and changes only a centred 55% box.

## Copy structure
- Hook: the dotted orb opening (no words, 0-0.95 s).
- Tension: "Ideas are static" (caption only; on screen it is the typed intro and the pause on send).
- Product moment: typing an intro into a composer, pressing send.
- Proof: "I turn ideas into visuals / And visuals into Motion" over nine portfolio cards ("Zero excitement.", "Zero hassle.", "GLASS").
- CTA: "Let's Make Things Move".
Exact text: "Hi, I'm Koral Arya, a Motion Designer with over 6 years of experience bringing ideas to life."; "I turn ideas"; "into visuals"; "And visuals into"; "Motion"; "Let's"; "Let's Make"; "Things"; "Move".

## Why this does not look AI-generated
1. Real photograph, layered grades: a single plate used for sunset and day, with rack focus on foreground flowers and slow cloud drift.
2. The composer is a believable product object: caret, newest-word colour trail, wrapped lines, a send button with a press state.
3. The skew/rubber-band deformation on text wrap is a hand-animated touch that no template gives you.
4. The cursor decelerates and presses; the zoom is a clean match cut at 2x, not a drifting scale.
5. The dotted orb is warped by a displacement field with a noisy mask edge: imperfect shape, not a perfect sphere.
6. Type rhythm: letters appear at human speed, the colour moves word by word, glyph confetti exits in 0.5 s.
7. Portfolio cards are real, varied work (photo, 3D, illustration, UI) shown at 10 Hz; the variety is the proof.
8. Controlled palette: cream, orange, near-black; the black finale reuses the orange as a horizon glow, not a rainbow.

## What would make it look AI
1. A smooth CSS-style scale-in of the orb as a perfect radial gradient with no halftone field and no mask noise.
2. A typewriter with identical letter timing and a uniform caret and no colour trail.
3. Card stack cards with the same layout and AI-looking gibberish text.
4. A bright gradient glow bloom that flashes at every cut and a bouncy spring on every text element.
5. A photo that is a stock-looking AI landscape with melting detail; the real plate here is sharp and photographic.

## Archetypes

| name | t_in | t_out | recipe | default duration | easing | flash risk | HyperFrames build | Tidewell fit |
|------|------|-------|--------|------------------|--------|------------|-------------------|------------|
| dotted orb mask reveal | 0.0 | 0.6 | noisy-edge circle mask over a photo, radial halftone dot field displaced by a bulge | 0.5 s | ease-in-out expo | low | canvas 2D dots or CSS radial-gradient mask + SVG feTurbulence displacement | opener: orb opens on a house photo |
| photo grade swap (sunset to day) | 0.6 | 0.95 | two LUT-graded versions of one plate crossfaded with rack focus | 0.4 s | power2 inout | low | two stacked img with CSS filter hue/sat/brightness animated | house photo morning to evening |
| composer typing over a photo + send | 0.95 | 3.77 | white composer, typed text with colour trail, wrap skew, cursor press | 2.5 s | typing 14 cps, ease-out | none | HTML div, GSAP text char timeline, caret, skewX on wrap | a buyer's text typed into an SMS composer over the listing, Tidewell replying |
| rubber-band layout skew | 2.0 | 2.7 | box grows with skewX 6 deg and damped wobble ~4% overshoot | 0.7 s | back.out(1.2) damped | none | gsap to scaleY/height + skewX with elastic.out(1, 0.5) | the reply bubble growing as Tidewell answers |
| match-cut zoom + cursor press | 2.95 | 3.77 | 2x single-frame zoom, cursor decel, 3-stop press colour | 0.8 s | expo out | none | stage scale step + cursor motion path | zoom on "Book showing" button |
| cream kinetic type | 4.27 | 5.9 | typewriter + orange accent word + glyph confetti | 1.6 s | ease-out | low at the cut (0.495 up flood) | HTML spans + GSAP SplitText-like manual char split | headline "Every lead gets an answer in seconds" |
| 10 Hz card slideshow | 5.9 | 6.9 | nine centred cards, hard cuts 0.1 s | 1.0 s | none | med (dark/light alternation) | stacked absolute divs toggled with GSAP set() on a timeline | rapid set of Tidewell surfaces: Inbox, Calendar, Listings, DocuSign, Stripe |
| 3D card stack zoom | 8.4 | 9.65 | planes in 3D with random rotation, zoom push then collapse | 1.2 s | expo out then ease-in | low | CSS 3D perspective div stack, GSAP z/scale | an assembled "everything Tidewell does" stack |
| black horizon finale | 9.65 | 12.6 | white text on black, peach horizon glow, slow tilt | 3.0 s | ease-out | low | radial-gradient + rotate tween | CTA lockup "Tidewell. Book more showings." |

## Frames
(frames not redistributed; see the original reel)