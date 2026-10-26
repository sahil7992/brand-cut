# Archetype contract

An archetype is a working HyperFrames sub-composition template that any brand and any format can use unchanged. Reference implementation: `status-stack/` (read it first).

## Files
```
archetypes/<name>/
  scene.html     the template (required)
  README.md      what it is, refs + timestamps, duration, easing, beats, flash risk, variables, format notes (required)
  preview.png    a real snapshot from the test harness, 16:9 frame + 9:16 frame side by side (required)
  assets/        optional files only this archetype needs (copied to assets/<scene-id>/ by add-scene.py)
```

## scene.html rules
1. Every id, class prefix, composition id and timeline key uses the token `__ID__` (add-scene.py replaces it with the scene id). Example: `id="__ID__-card"`, `.__ID__-pill`, `window.__timelines["__ID__"]`.
2. Standard sub-composition shape: everything inside `<template>`; root `<div id="root" data-composition-id="__ID__" data-width="1920" data-height="1080">` styled only by `#root { position:absolute; inset:0 }`; one `gsap.timeline({ paused: true })` registered last; `gsap.fromTo` for entrances; deterministic (no Math.random, Date, network; seeded PRNG if needed); no CDN libraries (vendor into `assets/`).
3. Brand-agnostic: never hardcode a brand colour, font, logo, name or product copy.
   - Colours: CSS `var(--bg) --bg2 --ink --ink-soft --muted --hair --accent --accent-lift --accent-deep --paper --on-paper --brand --brand-lit --brand-deep --ok --warn --info --glow-0 ... --glow-8 --glow-card` and app tokens `--app-*` for recreated product UI. `color-mix(in srgb, var(--x) 40%, transparent)` for alpha.
   - Fonts: `var(--font-display)` / `var(--font-ui)`, weights `var(--w-display)`, tracking `var(--track-display)` / `var(--track-ui)`.
   - JS: `window.BRAND` gives `name, tagline, endline, url, palette{...,glowRamp[]}, app, logo{tile,mark,wordmarkText,askRibbon,markColors}, partners{whatsapp,stripe,docusign,...}, ui{home,thread,ask,askOpen,showings,showingsMonth,captureSize}, phone{frame,rect}, faces{<id>: path}, photos{dir,hero}, cast{realtor,leads[],listing}, story{beats[],sampleThread[],sampleAsk{q,a},sampleFee}, format{id,w,h,safe{top,bottom,left,right}}`. Asset paths in BRAND are project-relative (`assets/...`) and resolve inside scene files.
   - Content defaults come from BRAND (for example the thread from `BRAND.story.sampleThread`); declare `data-composition-variables` on `<html>` only for what a film should override per instance (labels, times, which lead, toggles). Read them once with `window.__hyperframes.getVariables()`.
4. Format-native: read `W,H` from the root's `data-width/data-height` and `BRAND.format.safe`. Lay out for 16x9 (1920x1080), 9x16 (1080x1920), 1x1 (1080x1080) and 4x5 (1080x1350): keep every word and key UI inside the safe insets, scale hero elements up in vertical so they stay big, restack horizontal rows into columns where needed. Never crop a landscape layout. `html[data-format=...]` selectors do NOT match inside sub-composition templates (found while building): set `data-fmt="${BRAND.format.id}"` on your own content root in the script and branch CSS on `[data-fmt="9x16"] ...`, or branch in JS. Variable values in `data-variable-values` are single-quoted: add-scene.py escapes apostrophes; when editing by hand use a typographic apostrophe.
5. Design rules (binding): sentence case only, no `text-transform: uppercase`, no emojis, no italic serif, no purple AI gradients, no sparkles/orbs/particles/lens flares/neon outlines, no invented UI (recreate real UI from BRAND.ui captures and app tokens), no procedural phones or houses (use `BRAND.phone.frame` and photos), no drawn houses, no 3D tags. Big, detailed, physically lit elements: glass recipe, contact shadows, one light from top-left, motion blur on fast moves.
6. Flash-safe: no full-frame white or cream floods inside an archetype unless its README says "flood: yes" and the variable `flood` defaults to false. Never more than 3 luminance flashes in any 1 s. Light sweeps stay small (under a quarter of the frame) and soft.
7. Motion: entrances power3.out/expo.out 0.45-0.8 s; 3D settles power4.out 0.9-1.3 s; back.out(1.6) only for small pops and clicks; exits power2.in 0.25-0.4 s; a slow continuous drift on the whole scene; nothing pulses on beats.
8. SFX: list every on-screen action (tap, send, pop, snap, chime, whoosh) with its local time in README.md under "SFX cues", so the film's audio/events.json can place a designed sound on each.
9. Make it end clean: either a hand-off frame (described in README for the next scene to match) or a fade/blur out controlled by a `fadeOut` boolean variable.

## Test harness
```bash
SK=${MOTION_STUDIO:-.}
H=./work/arch-<name>
$SK/scripts/new-film.sh demo $H 16x9
python3 $SK/scripts/add-scene.py $H <name> a1 0 <dur>
cd $H && npx -y hyperframes@0.8.183 lint && npx -y hyperframes@0.8.183 snapshot --at <t1>,<t2> --no-end -o .hyperframes/s16
python3 $SK/scripts/set-format.py $H 9x16 && npx -y hyperframes@0.8.183 snapshot --at <t2> --no-end -o .hyperframes/s916
```
Also prove the re-theme once: `python3 -c` to set film.json brand to `demo`, re-run `scripts/brand-css.py $H`, snapshot one frame. Make `preview.png` from the 16:9 and 9:16 frames side by side (ffmpeg hstack at 640 px tall). Keep snapshot runs to 12 frames or fewer. Delete the harness dir when done except preview.png copied into the archetype.
