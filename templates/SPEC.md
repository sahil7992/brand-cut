# __NAME__: build spec (contract)

Brand: `__BRAND__` (see `film.json`, themed by `scripts/brand-css.py`). Formats: __FORMATS__. 60 fps.

## 1. The product in one breath
<!-- Copy from brand.json "story". Every scene must answer "what does the product do for me here?" -->

## 2. Script of product moments
| # | product moment (concrete, real UI) | on-screen words (sentence case) | VO line | proof on screen |
|---|---|---|---|---|

Rules: every scene is a concrete product moment with real app UI; wherever the AI appears, a real AI answer is on screen; no abstract slogans; claims only from brand.json truths.may_claim.

## 3. Storyboard / timeline (absolute seconds)
| scene id | archetype | in | out | transition out (non-flash first) | SFX events (time: sound) | music / VO note |
|---|---|---|---|---|---|---|

Flash budget: at most one full-frame flood per 8 s and never more than 3 flashes in any 1 s (qa/flashcheck.py must pass). Prefer match cuts, masks, wipes, glass wipes, push/whip moves, morphs, camera moves through objects, sub-threshold light sweeps.

## 4. Music (3 options, one picked)
| option | file | licence | BPM | window (in-out) | why |
|---|---|---|---|---|---|
Pick: A. Alternates go in REPORT.md. VO films use a VO bed (sparse, warm, a bloom on the reveal); music-only films may use a hype track. Cuts may land on beats; nothing pulses on beats.

## 5. Voice
Voice id, model, speed, stability. Script lives in `audio/vo/script.txt`. One full-script generation; `audio/vo.py` guards the character budget.

## 6. Design tokens
From the brand block in index.html: `var(--bg) --ink --accent --accent-lift --accent-deep --paper --on-paper --brand --glow-0..8 --font-display --font-ui --w-display --track-display --safe-top/bottom/left/right`, and `window.BRAND` (cast, story, logo, partners, ui captures, faces, format). Never hardcode brand colours or fonts in scenes.

## 7. Motion rules (non-negotiable)
1. Everything drifts slowly (continuous camera pull-back or drift, sine.out/power1.out). Nothing sits dead still, nothing floats aimlessly.
2. Entrances power3.out/expo.out 0.45-0.8 s; 3D settles power4.out 0.9-1.3 s; back.out(1.6) only for small pops and clicks; exits power2.in 0.25-0.4 s. Never linear except counters fed through an ease.
3. Physical realism: motion blur on fast moves, real perspective 1400-2000 px, one consistent light (top-left), soft contact shadows.
4. No beat-pumping. Arrivals and cuts may land on beats.
5. No AI-slop tells: no sparkles, orbs, particles, lens flares, neon outlines, fake UI, procedural phones or houses, drawn houses, 3D tags, emojis, ALL CAPS or text-transform uppercase, italic serif, purple gradients.
6. Every on-screen UI action has a designed SFX (listed in section 3 and in audio/events.json).
7. Vertical and square formats are native layouts inside the safe insets (html[data-format] CSS or window.BRAND.format in JS), never crops.

## 8. Engineering contract
- Scenes are sub-compositions in `compositions/<scene-id>.html`: everything inside `<template>`; root `<div id="root" data-composition-id="<scene-id>" data-width=".." data-height="..">` styled by `#root { position:absolute; inset:0 }`; one `gsap.timeline({paused:true})` registered at `window.__timelines["<scene-id>"]`; `gsap.fromTo` for entrances; deterministic only (no Math.random, Date, network; seeded PRNG if needed). Prefix every element id with the scene id.
- Start scenes from an archetype: `python3 <skill-dir>/scripts/add-scene.py <project> <archetype> <scene-id> <start> <dur> [--vars JSON]`.
- Own only your files (your scenes and `assets/<scene-id>/`). Never edit index.html, SPEC.md, other scenes or shared assets; report needed changes instead.
- Verify by looking: `npx hyperframes snapshot --composition=<scene-id> --frames=8 -o .hyperframes/snap-<scene-id>`; at most 12 frames per run. `npx hyperframes lint` shows no errors in your files.
- Report (under 250 words): what you built, times verified, what falls short and why, asset sources.
