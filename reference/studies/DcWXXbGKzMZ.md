# DcWXXbGKzMZ: dija_motion, "Wake Up" SaaS micro-interaction reel

- Creator: Khadija | Motion Designer (@dija_motion); caption "I know I'm the best editor", inspo credited to @ali.motionnnn
- URL: https://www.instagram.com/reel/DcWXXbGKzMZ/
- Duration 10.017 s (601 frames), 60 fps, 1904x1078 (16:9)
- Source: native screen-render (After Effects export, no phone filming). No crop. Cursor, glass and UI are all composited, not recorded.
- Song: no track metadata in info.json (track/artist null). Librosa tempo 99.4 BPM, beats 0.67, 1.23, 1.81, 2.41 ... (0.6 s grid). Sound is a mixed bed with designed hits, see Sound.
- Study scope: the calendar date-pick micro-interaction in detail (cursor easing, press states, reminder chip).

## Summary

A 10-second light-mode motion-designer sizzle in six beats. A kinetic "Wake Up" type lock-up with a blue arrow resolves on neutral grey; a hard cut to black with a lime horizon glow reveals a frosted-glass Calendar widget over a real alpine photo (the photo starts hue-inverted and grades to natural as the glow retreats); a match-cut zoom (about 1.9x) goes into the widget where a cursor arrives, picks 12 inside a highlighted 9-16 range, and drags that date out of the card as a blue pill; a grey panel wipes in from the right and the pill morphs into a white "Sat 22 | Wake up at 8 am" reminder chip; a motion-blur whip lands a held dachshund photo; a "sorry bro, the edit is still being edited" meme card; and a plain "Bye :)". The arc is claim -> tool moment -> payoff -> joke -> sign-off. The only real product moment is shots 3-4.

## Shot list

| # | in | out | on screen | construction | camera | transition out | cut on beat? |
|---|----|-----|-----------|--------------|--------|----------------|--------------|
| 1 | 0.00 | 1.63 | "Wake Up" + blue arrow, glyph confetti (0 * ( 1) | live type, 2 words slide together, blue flash on "Wake", arrow slides in from left | static, flat | hard cut to black, 1 frame (1.633), then 0.22 s flicker | 1.633 is 0.18 s before beat 1.81, no |
| 2 | 1.63 | 2.88 | black + lime half-disc glow, then alpine photo with glass Calendar widget | glow = large blurred ellipse rising from bottom (#b6c20d), photo hue-inverted then graded to natural, glass slab fades up | static, subtle photo drift | match-cut zoom, 1 frame at 2.867 | 2.867 is 0.15 s early of 3.02 (anticipation) |
| 3 | 2.88 | 4.12 | zoomed calendar, range 9-16, cursor picks 12 and drags it out as a pill | CSS-like UI: blue discs #1a5fd0 joined by a line, SF numerals on blurred glass | tracking pan following the cursor, scale constant at ~1.93x | grey panel wipe from right, 0.40 s | press at 3.57-3.63 sits on beat 3.62 (onset 3.62) |
| 4 | 4.12 | 5.48 | flat grey #e1e1e1, pill morphs to white chip "Sat 22 / Wake up at 8 am" | rounded rect fill fades #7ba0e0 -> #e9e9e9 while icon, label, red divider and red text stagger in | none, cursor outline arrow below chip | motion-blur whip into photo, ~0.1 s | 5.50 vs beat 5.53, yes |
| 5 | 5.48 | 8.00 | dachshund photo on grey, slow shrink | real photo, directional blur 3 frames then resolves while scaling from ~1.35x to 1.0x | slow push-out | hard cut | 8.00 vs beat 8.08 and onset 8.08, yes |
| 6 | 8.00 | 9.30 | meme card "sorry bro / the edit is still being edited / keep scrolling" | flat PNG on grey, slight scale drift | static | hard cut at 9.28 | 9.28 = beat 9.28 (extrapolated from 0.6 s grid) |
| 7 | 9.30 | 10.02 | "Bye :)" | live type, #191819 on #e1e1e1 | static | end | n/a |

## Per shot detail

### Shot 1: "Wake Up" kinetic type (0.00-1.63)
- Background #f0f0f0 at t=0.2, settles to #eeeeee (dominant 97% of pixels), then #e0e0e0 in tile frames after the first 0.5 s (the whole reel drifts from #f0f0f0 to #e1e1e1; the colour is not constant).
- Two words "Wake" and "Up" start about 33% of frame width apart (x 115 and 229 of a 360 px tile, so 32% and 64% of width) and converge over ~0.45 s with ease-out (spacing 114, 105, 56, 0 px at 0.0, 0.07, 0.13, 0.2 s in 15 fps tiles, decelerating, no overshoot).
- During the slide, tiny glyphs ("0", "*", "(", "1") spawn and drift 20-60 px, 1-4 frames each, like a text scramble: this is the "not AI" tell, it is controlled clutter that is fully resolved by 1.0 s.
- "Wake" flashes blue #1f5fd9 for ~3 frames while the arrow "->" (blue, thin stroke 2 px at 360 px tile, ~6% of height) slides in from left x 5% to centre-left with ease-out, turns black on landing.
- Final lock-up "->Wake Up": tight tracking (about -3% to -4%), grotesque (Inter Display / Neue Montreal feel), regular weight, size about 5% of frame height, colour #191819. Held static from ~1.0 to 1.63. The first 1.0 s is the entire kinetic payload.
- Sound: loud hit at 0.5-1.0 s (RMS -8 dB), onsets 0.07 and 0.26 (initial pop), then bed drops to -33 dB.

### Shot 2: glow + photo reveal + glass widget (1.63-2.88)
- Frame-by-frame (60 fps, key_1.6s.jpg): 1.633 grey -> near-black #101010 (mean L 0.84 -> 0.0). 1.683 black. 1.70 a grey frame with a lime half-disc rising (mean L +0.595). 1.733 black again with lime. 1.80 grey again with lime and a ghost of "->Wake Up" at 20% opacity. 1.85 black with lime. Then 1.9: photo appears hue-inverted (maroon sky #3a1308, purple/violet trees) with an indigo #4a35d8 band at the bottom, then beige #e3cfae band, then natural photo (sky #caefff, trees green) with a navy #07244c bottom band that fades out by 2.2.
- This is a deliberate 5-transition flicker in 0.22 s (floods -0.841, +0.595, -0.396, +0.297, -0.242). It is the strobing that the client rejected. Our low-flash version: one 8-frame crossfade, no grey/black alternation.
- The "glow" is a stack of 3 coloured bands (lime #b6c20d, then indigo, then beige #e3cfae) acting as a soft-edged matte that rises from the bottom and carries the photo's grade from inverted to natural: a dye-colour wipe, not a light bloom. Bands travel upward ~100% frame height in ~0.35 s.
- Glass widget (a "liquid glass" slab): rounded square corner radius about 8% of its width, edge highlight ring 1-2 px white at ~35% opacity, background blur heavy (visible gaussian about 20-30 px at 1080p), inner top-left specular, slight darkening gradient to the bottom, thick refraction rim on the left and bottom. "Calendar" title 18 px-equiv white, "22 aug 2026" small right-aligned, 8 columns of numerals 1-8 (bold white), the numerals lower in the grid fade (opacity gradient 100% to ~30%), as if the card is falling into depth.
- Sound: near-silent bed, -33 to -36 dB from 1.0 to 3.0. The visual flicker has no audible hit (onsets only at 0.07/0.26 and 3.62), so the flicker is silent: a miss. Add a low sub hit if reused.

### Shot 3: the date-pick micro-interaction (2.88-4.12), the key study

All numbers below are tracked from key_2.75s.jpg, key_3.5s.jpg, key_4.1s.jpg (30 fps tiles) and dija.py panel-edge tracking.

1. 2.30-2.85 (wide): the range 9-16 draws itself: a thin blue line (2 px) grows from 9 to 16 left to right while each numeral gets a blue disc #1a5fd0 (the numeral turns white). Discs appear in sequence about 0.07 s apart (9 at 2.30, 16 at 2.8). This is a stagger with ease-out, no overshoot.
2. 2.82: a small white arrow cursor enters bottom right of the widget (x 96% y 80% of the wide frame).
3. 2.867: match-cut to a zoomed view (about 1.93x: digit pitch 127 px -> 245 px in a 360 px tile). The cut is on a single frame, not a camera move, which avoids any in-between blur. Camera then pans slowly (about 1.5% of width per 0.1 s) following the cursor.
4. 2.9-3.3 cursor path (tile px, 30 fps): x 310, 272, 245, 220, 210, 200, 190, 185, 180, 175 and y 200, 189, 172, 154, 144, 136, 128, 120, 113, 110. Step sizes in x: 38, 27, 25, 10, 10, 10, 5, 5, 5. That is a curve with a fast start and a long tail (about power3/expo out, arrival in ~0.4 s, no overshoot, approach is a slight arc, not a straight line). The cursor is the filled white macOS arrow with a thin dark outline and a soft drop shadow.
5. 3.3-3.55: cursor rests on 12, 4-6 frames of near-zero motion (1-2 px jitter). This beat of stillness before the press is what makes it read as intent.
6. 3.57-3.63 press (beat 3.62, onset 3.62): the 12 disc scales down about 8% and its numeral dims (the disc darkens to #3b73d0, press state), cursor stays. Press duration about 3-4 frames at 60 fps.
7. 3.63-3.83 pick-up: neighbours 13 and 14 slide left to overlap 12 (13 at 3.70 overlaps 12; 14 at 3.80), the line between 9-11 remains, the 12 disc morphs from circle to a fatter rounded blob (squash and stretch: width +20%, height -10%) and detaches from the line. Disc colour fades from #1a5fd0 toward a lighter periwinkle #7ba0e0 (about 55% opacity) as it is "lifted".
8. 3.83-4.12 drag out: cursor stays glued at the blob's centre-bottom; the blob moves right across 13-16, over the card edge, onto the bare photo; the camera pans left with it (blob x stays 39-50% of frame while the card scrolls away), speed rising then falling. Blob becomes a rounded pill about 90x30 tile px at 4.0 (aspect 3:1, radius = half-height). Pill centre drifts only 0.52 -> 0.48 of width over 0.3 s because the camera follows. Note the glass widget slides off to the left edge and is gone by 4.1.
9. 4.12-4.53 grey panel wipe from the right (measured left edge px of a 952 px frame): 827, 668, 560, 570, 330, 256, 196, 144, 106, 72, 42, 18, 0 at 1/30 s steps from 4.133. Progress = 0.13, 0.30, 0.41, 0.40, 0.65, 0.73, 0.79, 0.85, 0.89, 0.92, 0.96, 0.98, 1.0. That is a strong ease-out (power4/expo out), duration 0.40 s, hard vertical edge, no overshoot. The pill is held in place relative to the camera while the world is replaced.
10. 4.53-4.75 the pill colour fades #7ba0e0 -> #a9b9d1 -> #dde1e4 -> #e9e9e9 (white chip) while its width grows ~15% and height ~10% (pill squares off to a rounded rect, radius about 28% of height).
11. 4.75-5.2 chip content builds, staggered: red "Wake up / at 8 am" text appears first at the right (small, #d0103a), then "22", then "Sat" and a chat-bubble icon typed in from left, each fading up with ~2 px y-offset blur (about 0.07 s offsets). Final chip: left icon (speech bubble with 4 lines, charcoal #2b2b2b outline), "Sat 22" in SF Pro Medium about 4.4% of frame height #191819, a dashed red vertical divider #d0103a, then "Wake up" (red, medium) over "at 8 am" (smaller red). A soft red glow shadow (blur ~30 px, #d0103a at ~15%) sits behind the chip's right edge: the only coloured shadow in the film and it is what separates it from a flat template chip.
12. Cursor: during shot 4 the cursor turns from solid arrow to a white-filled outline arrow (hollow, 2 px black stroke) and drifts down 0.5% of height per 0.1 s as if releasing, then fades by ~5.2.

Easing family used: everything is ease-out (power3-power4 / expo out), no overshoot, no springs, no linear. Cursor arrives with a long decel; panel wipes are expo-out; object morphs are a quick ease-in-out.

### Shot 4: reminder chip (4.12-5.48)
Described in steps 9-12 above. Background #e1e1e1 dominant (89% of pixels). Held from ~5.0 to 5.45 (0.45 s) so the content is legible.

### Shot 5: whip to dog (5.48-8.00)
- 5.45 chip + cursor fade to 40% over a beige #e8d7c0 horizontal streak (motion blur smear of the next image), 5.48-5.50 one frame of orange/yellow/pink horizontal streaks (directional blur about 250 px, the next shot's photo smeared), mean L drops 0.187 (grey 0.74 -> 0.55). 5.52 onward the dog photo appears at ~1.35x and a strong directional blur, resolves over ~0.5 s (blur 80 -> 0 px, scale 1.35 -> 1.0, ease-out expo), then slow continuous shrink (width 138 -> 122 tile px between 6.0 and 8.0, i.e. 0.94x/s ... about 12% over 2 s, ease-in-out).
- Photo: an iPhone-quality dachshund snapshot with a pink collar, no frame, shown as a portrait rectangle on grey with slight 1 px light edge. Real photograph, imperfect framing, that is the humour.
- Sound: loud hit at 5.53 (-13 dB RMS in 5.5-6.5 window), decays to -34 dB by 7.5.

### Shot 6: meme (8.00-9.30)
- White (#fdffff) square meme card with a Comic-like black headline "sorry bro", subline "the edit is still being edited", a 3D yellow bean character in a hard hat pushing a wheelbarrow, caption "keep scrolling". Cut at 8.0 with a small flood (+0.127 mean L). Card scales from 0.93x to 1.0x in 0.25 s (spring-free ease-out) then drifts up to 1.04x until 9.2 then shrinks to 0.9x for the last 3 frames (anticipation out), cut at 9.28.
- Sound: onset 8.08 (beat), bed -33 to -38 dB, silent at 9.0-9.5 (-58 dB) before the sting.

### Shot 7: "Bye :)" (9.30-10.02)
Plain text in the same grotesque, ~5.5% of frame height, #191819 on #e1e1e1. Sting at 9.5 (-15 dB), fade to -24.

## Typography
- Family guess: SF Pro / Inter-class neo-grotesque; sizes: lock-up ~5% of frame height, calendar numerals ~3.2% (bold), chip title 4.4% medium, chip subtitle 2.4%.
- Tracking -3% on display, 0 on UI. Case: sentence case always ("Wake Up" is title case, "Bye :)" sentence case). No caps. No italics. No emoji (text smiley instead).
- Colours: text #191819; arrow and calendar blue #1a5fd0 / #1f5fd9; red #d0103a.

## Palette
- Neutral base: #f0f0f0 -> #eeeeee -> #e1e1e1 (grey drifts darker as the film progresses).
- Lime glow #b6c20d (dominant 24% at 1.75), with #626806 and #131501 in its falloff.
- Photo: alpine, greens #6b7550, #516758, #728561, shadows #31444b, sky #caefff.
- Pill/chip: #7ba0e0 -> #a9b9d1 -> #e9e9e9.
- Accent red #d0103a, shadow tint of the same at 15%.

## Flash profile (dija_motion, 60 fps, 160 px luminance)
- Floods (mean jump >= 0.1 and changed fraction >= 0.25): 1.633 (-0.841, frac 1.00), 1.700 (+0.595, 1.00), 1.733 (-0.396, 0.59), 1.800 (+0.297, 0.84), 1.850 (-0.242, 0.94), 5.500 (-0.187, 0.69), 5.517 (-0.106, 0.57). The 8.0 s meme cut (+0.127 mean L) changes under 25% of pixels, so it is not a flood.
- Max opposing transitions in any 1 s window: 4 (five alternating floods inside 0.22 s at 1.63-1.85, i.e. about 2 full flash pairs in 0.22 s, plus nothing else near it). The measured peak rate of alternation is about 22 transitions/s for 0.22 s, far above our cap of 3 flashes/s even though it is brief. the client's rule would reject it: replace with a single crossfade.
- Everything else: smooth. The meanL list per 0.5 s shows a gentle 0.84 -> 0.72 -> 0.55 -> 0.61 ramp, i.e. no flashes.

## Copy structure
- Hook: "-> Wake Up" (instruction, doubles as the label of the product; 0-1.6 s).
- Tension: none; the black cut is the "wake up".
- Product moment: Calendar widget, "22 aug 2026", range 9-16, picking 12, dragged into a reminder chip.
- Proof: the chip "Sat 22 | Wake up at 8 am" (the result of the gesture, legible for 0.5 s).
- Joke/relief: dachshund photo, then "sorry bro / the edit is still being edited / keep scrolling".
- CTA: "Bye :)" (no CTA; sign-off).

## Why this does not look AI-generated
1. The UI is fully designed and consistent: 8-column numerals, a range line with discs at exact pitch, press and pick states, not a decorative mock.
2. Real photography under real glass: an alpine photo behind a genuinely blurred slab with refraction rim and depth fade of the lower rows.
3. The cursor behaves like a human hand: long deceleration, 5 frames of rest, a small arc, a 3-4 frame press, then a drag with the camera chasing it.
4. Match-cut zoom on a single frame (no mushy interpolated zoom) with a camera that then tracks the subject.
5. Hard, asymmetric easing (expo-out wipes, no overshoot), with different durations per element (0.4 s panel, 0.07 s stagger, 0.5 s whip).
6. Controlled imperfection: glyph confetti in the opening, a coloured red glow behind a white chip, a grey that drifts from #f0f0f0 to #e1e1e1.
7. Humour and a real human photo break the polish and show a person's taste.
8. Restraint: three colours (grey, blue, red) plus a one-second lime moment; type is one family.

## What would make it look AI
1. A spring/overshoot on every element and uniform 0.3 s easings.
2. A cursor teleporting to a target, or gliding linearly with no rest and no press state.
3. A generic gradient blob glow with bloom across the whole frame instead of a directional dye-colour matte.
4. A calendar of invented dates with nonsense numerals and uneven pitch, or lorem-style chip text.
5. Photoreal clip generated with melting detail instead of a real photograph with proper sharpness.
6. Everything shown at 1.0x with no zoom/tracking, and no silence or cuts on beat.

## Archetypes

| name | t_in | t_out | recipe | default duration | easing | flash risk | HyperFrames build | Tidewell fit |
|------|------|-------|--------|------------------|--------|------------|-------------------|------------|
| kinetic word converge + glyph scramble | 0.0 | 1.6 | two words slide together from 32%/64% x, arrow in from left, 6 stray glyphs live 1-4 frames, blue flash on one word | 1.0 s | expo out | none | HTML spans + one paused GSAP timeline, glyphs as absolutely positioned spans with opacity steps | the headline "Texts in. Showings booked." |
| glow bloom (low-flash version) | 1.63 | 2.2 | dye-colour band matte rising from bottom, photo grade inverted -> natural | 0.5 s | power3 out | high as shot (5 transitions); low if one soft crossfade | CSS mask-image linear-gradient + hue-rotate/invert filter animated, or WebGL canvas | opener over a house photo to reveal the Tidewell inbox |
| liquid glass slab | 1.9 | 4.1 | frosted card on a real photo, backdrop-filter blur 24 px, 1 px specular rim, bottom depth fade | 2.2 s | power3 out | none | HTML div with backdrop-filter, an inset box-shadow rim and a mask gradient on the lower rows | the Showings calendar over a listing photo |
| calendar date-pick micro-interaction | 2.3 | 4.12 | range draws with staggered discs, cursor decel arc and rest, press state, pick-up squash, drag out as pill | 1.8 s | expo out, no overshoot | none | HTML grid + SVG cursor, GSAP motion path with custom ease, scale pulse 0.92 on press | a buyer picks Saturday 22 at 10:30, Tidewell books it |
| glass tile + pointer click | 3.57 | 3.63 | disc shrinks 8% and darkens, 3-4 frames | 0.07 s | ease in out | none | scale + filter brightness tween | Approve button on a pending showing |
| match-cut zoom + tracking pan | 2.867 | 4.1 | single-frame jump to ~1.93x then pan follows subject | 1.2 s | step then expo out | none | wrap UI in a stage div, set scale on the cut, animate translate | zoom to a lead's reply bubble |
| wipe to flat field + pill -> chip morph | 4.12 | 5.2 | grey panel expo wipe, pill colour/size morph, chip content staggered | 1.1 s | power4 out | low | absolutely positioned panel with clip-path/translateX, chip built from flex children with opacity stagger | pill becomes "Showing confirmed Sat 22, 10:30" chip |
| whip transition with directional blur | 5.45 | 5.8 | streak frame (blur 250 px horizontal) then target photo resolves from 1.35x, blur 80 -> 0 | 0.35 s | expo out | med (single dark dip -0.19) | CSS filter blur on a horizontal-only SVG feGaussianBlur stdDeviation="x 0" animated | between rooms or a listing photo cut |
| meme / humour beat | 8.0 | 9.3 | flat card with a 3D character on grey, scale 0.93 -> 1.0 | 1.3 s | power2 out | none | image asset in a div | a light beat only if the brand wants it (probably skip) |
| calendar chip with coloured glow shadow | 4.75 | 5.45 | white chip with divider and red text, soft red shadow | 0.7 s | power3 out | none | HTML flex + box-shadow 0 0 30px color | the confirmed-showing chip with a green glow |


## Frames
(frames not redistributed; see the original reel)