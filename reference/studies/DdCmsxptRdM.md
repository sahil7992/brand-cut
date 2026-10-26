# DdCmsxptRdM - Roy Rayfer, "@googlegemini lets work already" (BLACKBOX.AI piece, phone filming an After Effects monitor)

- Creator: royrayfer (Roy Rayfer). Caption: "@googlegemini Let's work already"
- URL: https://www.instagram.com/reel/DdCmsxptRdM/
- Duration 16.83 s, 30 fps, 1080x1920 vertical
- Source type: SELFIE (0-0.57 s) then a PHONE FILMING A MONITOR (0.57-16.83 s). Tripod-locked, straight-on, no shake. The monitor shows an After Effects project previewing the comp; the laptop below shows the AE timeline (many layers).
- Crop to analyse the picture: monitor screen = `crop=1080:668:0:430` (screen spans the full frame width, y 430-1098 of 1920; measured from row-mean luminance edges: wall 184 -> bezel at y 428-444, bottom bezel at y 1098). Letterboxed comps (the 2.7:1 B&W part 12.2-14.2 and the robot shot) sit at about `crop=942:350:70:620`; full-bleed comps (code editor, UI panels, ring) fill the AE viewer, roughly `crop=1080:560:0:470`.
- Song: "Bliss" by Klsr. Librosa says 198.8 BPM with beats every 0.30 s (0.72, 1.04, 1.35, 1.63 ... 14.93 ...); musically this is ~99 BPM with cuts on eighth notes (0.30 s). rms is -48 / -45 dB for the first second (selfie, almost silent), the drop is at 1.0 s (-10 dB).
- Scratch: /tmp/study-DdCmsxptRdM, /tmp/study-scripts (cuts.py, flash.py, track.py)

## Summary

A creator's "I edited this all night" brag film. Beat 0 (0-0.57 s): selfie, hand on head, white overlay "Edited all night for this..." (human hook, near-silent). Then the camera pulls back to a monitor playing the actual comp so the viewer sees the real After Effects UI (and the real timeline on the laptop beneath). The comp itself is a ~16 s dark cinematic AI sizzle: a hexagon mark whoosh, two flash-pulses of X-ray / skull / satin, two robot arms with pens drawing on white (1.2-2.5 s), a whip into a blue lotus whose petals dissolve into code and a black ASCII tree, a globe, a coffee-cup swirl, a dial and the Creation-of-Adam hands, dark data-UI panels with product claims, a glitch stretch into a code editor, a white column-wipe flash (4.87-5.07 s), then a dot-matrix eclipse ring with tiny labels (5.07-7.4 s), a constellation of glowing points (7.4-8.5 s) that converges into a glowing hexagon (8.6-10 s), a collage of photos (booth, speaker, "All Agents. End-to-end Encrypted." card) that assembles and mosaics into a flock of doves (10-12 s), a high-contrast black-and-white montage under the subtitle "where the future gets built" (eyelid, horse, arms, planet, hand, car, hand with phone, lightning, 12.2-14.2 s), and a dark end card with the BLACKBOX.AI mark and wordmark held for 2.4 s.

## Shot list (times from per-frame cut detection and 10 fps sheets; 30 fps so +-1 frame = 0.03 s)

| # | in | out | on screen | construction | camera | transition out | on beat? |
|---|----|-----|-----------|--------------|--------|----------------|----------|
| 0 | 0.00 | 0.57 | selfie, hand on head, "Edited all night for this..." | real phone selfie + IG-style text overlay (white, soft shadow) at y 60 % | handheld selfie, slight drift | hard cut | pre-roll, silent |
| 1 | 0.57 | 0.77 | dark, hexagon mark | AE comp: white hex glyph with glow, dark navy | locked | speed-ramp stretch | -0.15 to beat 0.72 |
| 2 | 0.77 | 1.23 | hex whoosh streak, spine X-ray, skull CT, satin | stretch blur streak + 3 stock images at 2-3 frames each | locked | hard cuts | 0.77 (beat 0.72), 1.0 (beat 1.04) |
| 3 | 1.23 | 2.50 | two robot arms drawing, white studio | photoreal 3D/stock render, soft long shadow, 2 pens | slow push | smear whip | 1.35 beat after cut |
| 4 | 2.50 | 3.50 | lotus to code, ASCII tree, globe, coffee swirl, dial, hands | 6 stock/3D images, 2-6 frames each, code-text particle mask | locked | hard cut | 2.51, 2.81, 3.11 all on beat |
| 5 | 3.50 | 4.40 | dark UI panels: "Every agent harness. One platform." etc. | recreated product UI in AE, panels slide and stack | slow drift | glitch stretch | 3.5 (between beats) |
| 6 | 4.40 | 4.87 | code editor | screen capture of a code editor, dark theme | locked | column wipe to white | 4.44 |
| 7 | 4.87 | 5.07 | white flash, dotted ring pattern | white wipe from left over 3 frames, 5 frames at full white | locked | hard cut to dark | 5.04 |
| 8 | 5.07 | 7.40 | dot-matrix eclipse ring + labels | halftone/dot grid, glowing white ring with orbiting dots, red layer-bounds boxes | locked | fade | 5.04, 5.32 |
| 9 | 7.40 | 8.55 | constellation of 10 glowing points | points with soft glow, tiny labels | locked | converge | 8.43 onset |
| 10 | 8.55 | 10.05 | glowing hexagon, labels "one" / "place" | hex outline pulse | locked | photos fly in | 9.94 |
| 11 | 10.05 | 11.8 | photo collage assembles and shrinks to a cluster, label "this" | 8-10 photo planes in 2D, ease into a cluster, pixel mosaic at end | locked | mosaic to doves | 10.3, 10.91 onset |
| 12 | 11.8 | 12.2 | doves | B&W doves over dot-grid | locked | blur cut | 11.73 |
| 13 | 12.2 | 14.2 | B&W montage with "where the future gets built" | 8 inverted-contrast stock shots, red AE bounding boxes, speed-ramp zoom | locked | cut to dark | 12.63, 12.9, 13.13, 13.7, 14.13 |
| 14 | 14.2 | 16.83 | BLACKBOX.AI mark + wordmark | white hex icon + wordmark ~7 % of frame width, centre | locked | end | logo at 14.2-14.4; outro kicks every 0.3 s |

## Per shot detail

**Shot 0 hook (0-0.57).** Real selfie: phone close to the face, right hand on head, soft warm window light, face under-lit, not retouched. Overlay text "Edited all night for this..." (about 3.4 % of frame height, white, a rounded proportional sans like Instagram's Modern/Classic caption font, soft drop shadow, centred at about 61 % of frame height, sentence case with trailing ellipsis). No music (rms -48 dB), so the first spoken-like beat is the silence. Purpose: a human admission before any spectacle.

**Pull to the monitor (0.57).** Hard cut; picture is a monitor with real moiré: horizontal banding and exposure pumping from the phone shutter against the monitor refresh. The AE UI (menus, panels, a project tab) is visible above and below the comp. The laptop under the monitor shows an AE timeline with 40+ layers: the viewer is shown the proof of labour. The frame layout: wall (beige, top 22 %), monitor 22-57 %, laptop 57-95 %: the monitor is only 35 % of the vertical frame, so the comp is small; comps are 2.7:1 or full-bleed and the creator accepted that.

**Shot 1-2 (0.57-1.23) hex + montage.** Hex mark at 0.60 (white outline hex with inner notch, soft bloom), then a horizontal speed-ramp stretch (the hex smeared 8x wide, 0.7-0.8 s) which is the first flash: mean luminance 0.02 -> 0.19 -> 0.43 -> 0.05 over frames 0.77, 0.80, 0.83. A second pulse follows at 0.93 -> 0.97 -> 1.0 (0.13, 0.34, 0.08). Between them the montage cuts every 2-3 frames (spine X-ray 0.9-1.0, skull CT 1.0-1.1, white satin 1.1-1.2). The brightness ramps 0.14 -> 0.35 during 1.03-1.2 as the X-ray images get lighter.

**Shot 3 robot arms (1.23-2.5).** Two glossy chrome-and-black pen arms on a seamless white sweep, pens touching the surface, long soft shadows falling left (single key light from the right, clean contact shadow), shallow depth of field; looks like a 3D render with physically plausible reflections or a high-end product-film stock. Small text "passion" top-left and a tiny label bottom right. Slow push-in (estimated from the sheets, not measured). Ends in a diagonal motion smear at 2.4-2.5 (whip pan with directional blur).

**Shot 4 montage (2.5-3.5).** 2.57 lotus in cool blue (#7F9FD8) on a pale blue sky bg with a code-character dissolve covering the petals from the bottom; 2.7 the code mask becomes the silhouette of a black ASCII/hex-digit tree (the characters are the foliage: the text's density draws the tree) on the lotus background; 2.8 a bright globe (cyan atmosphere, L jumps +0.2) on a pale cyan bg; 3.0 an orange coffee-cup swirl on cream; 3.1 a black circle with a white ring UI glyph; 3.2 an aerial dial/watch face overlay (gold ticks), 3.3-3.5 Creation-of-Adam hands overlaid on the dial. Each image is 2-6 frames (0.07-0.2 s) and the cuts land on beats 2.51, 2.81, 3.11. Mean luminance 0.40 -> 0.21 (2.57) -> 0.09 (2.73) -> 0.38 (2.8) -> 0.07 (3.1) -> 0.27 (3.23-3.43) -> 0.02 at 3.5: strobing dark/light alternation at 0.3 s intervals.

**Shot 5 UI panels (3.5-4.4).** Dark UI (bg #07090F) with a large Inter-like headline "Every agent harness. One platform." (top-left), a green terminal panel with red/green diff lines, a grey code panel, a card "Dispatch from anywhere, anytime, autonomously." (top-right), a bold card "Same model. 3X faster, 3X cheaper." (lower middle), and a bottom statement "All models. All agents. End-to-end encrypted." Panels appear by staggered slide (2-3 frames apart) and overlap with 20 % opacity glass; stylised as real product UI (recreated), with glare from the monitor on the right.

**Shot 6-7 code to white flash (4.4-5.07).** At 4.4 the UI stretches horizontally (a speed-ramp stretch) into a code editor (IDE with file tree left, syntax colours #6C9EF8, #C792EA, #A5E075 on #0B0E14). At 4.87 a white column wipe sweeps in from the left over 3 frames (L 0.03 -> 0.17 -> 0.30 -> 0.52), holds at 0.52 for 5 frames (4.93-5.03; the editor is now white with dark text, then a dotted-ring pattern on white with vertical guide lines), and at 5.07 hard cuts to dark (0.52 -> 0.08): a 0.13 s flood followed by a one-frame drop.

**Shot 8 eclipse ring (5.07-7.4).** A dot-matrix (halftone) cloud in a diagonal swoosh from the top-left to the centre with a glowing white ring (about a third of the screen height, estimated) lit like an eclipse corona: the ring is formed by a few hundred small white dots with bloom (bright-pixel count ~3.9-4.2k at 360 px width), brightest at the left rim; a few larger dots orbit the ring, and small drifting white points ("stars") scatter. Labels: "singularity" (top-left of the ring), another small label bottom-right (reads like "negentropic"), plus red AE layer-bounds rectangles around the labels. Ring size stays constant (bright-pixel count 4150 -> 3860, within 7 %) while the halftone cloud and orbit dots animate: a rotation / breathing loop, not a scale. It fades out over 0.27 s (7.30-7.57; bright-pixel count 10552 -> 8915 -> 7478 -> 6420 -> 5954 -> 5444 -> 4758 -> 3091 -> 1911, roughly linear ramp).

**Shot 9-10 constellation to hex (7.4-10.05).** ~10 soft-glow points (#F5E3C0 warm white, 1.2 % of screen width) drift on slow different vectors (parallax), a few twinkle (cross flares). From 8.43 (strong onset) they accelerate toward the centre: bbox width 66.9 % (8.43), 66.1, 65.3 (8.57), 63.6 (8.63), 60.6 (8.67), 56.7 (8.70), 56.4 (8.73): an ease-in over ~0.3 s, then a hexagon outline (#FFFFFF, 3 px, bloom) forms at 8.7 and pulses (scale 1 -> 1.15 -> 1) until 10.0. Two tiny text labels flank it ("one" top-left, "place" right).

**Shot 11 photo collage (10.05-11.8).** A portrait photo (two men at a conference booth) pops in top-left at 10.1, then 6-8 more photo planes and a card "All Agents. End-to-end Encrypted." (Inter bold, white on #121212 with an orange bullet) enter from the edges and compress into a cluster at screen centre (2.4 s total, ease-out). Photo planes are un-rounded rectangles with no shadow (flat editorial), with micro labels "this". At 11.6 the cluster dithers to a black-and-white mosaic, then becomes the doves.

**Shot 12-13 B&W montage (11.8-14.2).** Doves (white birds on black with red AE box tracking on 3 birds) 11.8-12.2; then an eyelid close-up (12.2-12.4, L rises 0.08 -> 0.30), a jumping horse silhouette (12.5), Creation-of-Adam arms (12.7-12.9), a planet horizon (13.0), a hand and car-hood (13.1-13.6, L 0.25), a radial zoom-burst (13.5) and a hand holding a phone (13.7), a lightning crack on white (13.9-14.1, L 0.3), and a planet horizon with floating sparks (14.1-14.2). The images are inverted-contrast high-key B&W with crushed blacks; the subtitle "where the future gets built" (white on dark / black on white with auto-contrast, ~1.6 % of frame height, centred at 55 % of the comp height) stays pinned while the images change, fixed in place. Cuts on beats 12.63, 12.9, 13.13, 13.7, 14.13.

**Shot 14 end card (14.2-16.83).** Dark navy (#0B1220) bg with a very faint vignette, white hex mark + "BLACKBOX.AI" in a wide-tracked geometric sans, all-caps (brand wordmark), mark+word about 20 % of comp width at y 50 %. No animation: a static hold of 2.4 s while the audio outro continues (onsets every 0.3 s: 14.81, 14.93, 15.16, 15.46, 15.77, 16.02) and the tail fades (-32 dB at the end).

## Camera and depth

The phone camera is the "camera": static, straight on, sharp. Depth comes from the physical room: monitor above, laptop below, wall behind; AE UI chrome frames the comp (3 levels of rectangles). Natural exposure hunting causes ~5-10 % luminance pulsing on bright frames.

## Palette (sampled from the comps)

Navy #07090F / #0B1220; white #FFFFFF; warm star #F5E3C0; lotus blue #7F9FD8 on sky #A9C2E8; globe cyan #4FB6D6; orange swirl #E3753A on cream #F2E3C4; code colours #6C9EF8, #C792EA, #A5E075; B&W montage pure black and #F4F4F2; red AE boxes #E4474A.

## Flash profile (measured on crop=1080:668:0:430, per frame, linear luminance)

- Mean L 0.009 to 0.52.
- Floods (mean jump >= 0.1, >= 25 % of pixels changed, up and back down):
  1. 0.77-0.83: 0.02 -> 0.43 -> 0.05 (3 frames, 0.07 s pulse).
  2. 0.93-1.00: 0.02 -> 0.34 -> 0.08 (3 frames).
  3. 2.77-3.10: 0.09 -> 0.38 (2.8) ... 0.07 (3.1): 0.3 s bright then a dark drop.
  4. 4.87-5.07: 0.03 -> 0.52 plateau 5 frames (0.13 s) -> 0.08: the biggest full-frame flood, 0.2 s total.
  5. 12.2-12.6 (0.05 -> 0.30 -> 0.05), 13.1-13.7 (0.09 -> 0.25 -> 0.11), 13.9-14.1 (0.17 -> 0.32 -> 0.08): B&W white-frame sections.
- Max opposing transitions per second: 4 in the 0.77-1.0 window (two pulses within 0.25 s) = 2 flashes per second; any other window <= 1.5. So the strobe peak is 2/s and 3/s is never reached, but the first second is a rapid on-off and violates the "one flood per 8 s" rule many times (5 floods in 14 s, with 3 within the first 5 s).
- Verdict: this is the strobe style the client rejected. Use as a reference for energy only; replace luminance pulses with colour or motion pulses.

## Sound design

Intro silent (rms -48 dB under the selfie). The drop at 1.0 s (rms -10 dB) lines up with the second flash pulse (0.97). Hits land on cuts: 0.72 (first transient, hex stretch at 0.77), 2.81 (globe flash), 3.27, 3.74 (UI panel entrances), 5.29 (just after the white flash cut at 5.07, ring starts), 8.43 (constellation convergence), 10.91 (photos cluster), 11.73-11.82 (doves), 12.61 (B&W montage start), 14.81 onwards (logo outro). The song runs through; there are no UI SFX or whooshes distinct from the music. Quietest window: 3.5-5 s and 6-8 s sections sit near -20 to -35 dB while the ring and constellation play (music breathes, then 8.43 re-energises).

## Copy structure

Hook: "Edited all night for this..." (the creator's own face). Tension: montage of image/text-only attitude. Product moment: the data-UI panels ("Every agent harness. One platform." "Dispatch from anywhere, anytime, autonomously." "Same model. 3X faster, 3X cheaper." "All models. All agents. End-to-end encrypted."). Proof: the visible AE project + timeline and the real making of the piece. Promise: "where the future gets built". CTA: BLACKBOX.AI mark, caption "@googlegemini Let's work already".

## Why this does not look AI-generated

1. It is filmed as a screen: moiré, exposure pulsing, real AE UI and a real timeline of 40 layers on the laptop. Proof of authorship and process.
2. Human hook: a tired face, hand on head, line "Edited all night for this..." before any effects.
3. The code-tree silhouette is built from the text itself (density of characters draws the tree): it is a designed idea that a generator would render as mush.
4. Shot lengths cut to the 0.30 s music grid (each cut within 2 frames of a beat): lots of rhythm, tiny images, not long AI clips.
5. Layer-bound boxes (red AE boxes) are visible in the B&W montage: the creator tracked objects; boxes are not removed.
6. Typography stays tiny and precise: micro-labels at 1 % height ("singularity", "this", "one", "place"), subtitle pinned while images change, not floating random captions.
7. B&W section uses inverted contrast with crushed black and high-key white: a consistent grade across 8 stock shots.
8. The hexagon is the same logo shape across the piece (opening whoosh, constellation, hex pulse, end card): visual motif repeated 4 times.

## What would make it look AI

1. Replacing the stock/3D shots with generated video clips: the robot arms and horse silhouette would melt and morph.
2. Over-smooth, ultra-sharp, noise-free render of the same screen (no moiré, no exposure drift).
3. A voice-over or captions describing the piece ("In a world where...").
4. Motion without a beat: longer 1 s dreamy transitions between the images.
5. Random sparkle particles and lens flares on every shot; the original keeps dots to the ring and constellation only.

## Archetypes

| name | t_in | t_out | recipe | default duration | easing | flash risk | HyperFrames plan | Tidewell fit |
|---|---|---|---|---|---|---|---|---|
| dark cinematic AI | 0.57 | 16.8 | navy bg, glowing white marks, dot-matrix cloud, images in 2-6 frame cuts on the beat | 8-16 s | hard cuts + ease-in converge | HIGH as made, LOW if luminance pulses are replaced by colour pulses | scenes as sub-compositions, a beat array drives cut times; GSAP timeline | night-time film "11:42 pm" |
| screen-recorded making-of proof | 0.0 | 16.8 | selfie hook then real tool UI behind the work | 1-3 s hook | none | none | video clip of the hook + framed comp inside a monitor mock | the founder (the client) hook: "I built this over a weekend" before the film, then the real cockpit |
| chaos -> connected network lines (stars converge) | 7.4 | 10.0 | 10 glow points on parallax drifts, ease-in converge, resolve to hexagon mark, pulse | 2.5 s | power3.in then back.out small | low | canvas or 10 absolutely positioned divs with radial-gradient glow | leads (SMS, WhatsApp dots) converge to the Tidewell mark |
| code particle silhouette | 2.6 | 2.9 | mask a character grid with an image alpha (tree), foliage = text density | 0.3-1 s | steps | low | canvas 2d or SVG text with mask-image | "text becomes a house" for the listing reveal |
| dot-matrix eclipse ring | 5.07 | 7.4 | halftone grid cloud plus a bright ring of dots with orbiters, tiny labels | 2.3 s | sine loop, 0.27 s linear fade out | low | canvas with dot grid + ring points; labels as 10 px text | "Tidewell is always on" ring around the phone icon |
| photo collage cluster | 10.05 | 11.8 | 8 photo planes ease into a centred cluster, then pixel mosaic | 1.8 s | expo.out | low | stacked divs animated with GSAP, mosaic via CSS mask/blocks | real listing photos assemble into the showing card |
| B&W stock montage + pinned subtitle | 12.2 | 14.2 | 8 inverted B&W shots 0.2-0.5 s each, subtitle pinned | 2 s | hard cuts | MED/HIGH (white frames) | video clips, subtitle in a persistent layer | listing photos in B&W then colour on the approval |
| data UI panels with product claims | 3.5 | 4.4 | 4-5 panels staggered, headline + terminal + claim cards | 0.9 s | power3.out stagger 2-3 frames | none | HTML panels | cockpit panels "Every lead answered. Every showing booked." |
| glitch stretch to editor | 4.4 | 4.87 | horizontal speed-ramp stretch cutting to a code view | 0.4 s | expo in | low | CSS scaleX + filter blur then swap | "SMS arrives" to "reply drafted" |
| white column wipe flood | 4.87 | 5.07 | column wipe from left to full white 5 frames, hard cut out | 0.2 s | linear | HIGH | avoid for a brand; use a soft ink wipe | not used |
| logo end card | 14.2 | 16.8 | static mark + wordmark 2.4 s on dark navy | 2.4 s | none | none | HTML | Tidewell end card (wordmark mixed case, no all caps) |

## Frames
(frames not redistributed; see the original reel)