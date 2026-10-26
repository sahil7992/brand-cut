# Learnings

Everything below was learned the hard way while making product films with this skill: drafts that got rejected, renders that failed QA, and traps that cost hours. Read it before your first film.

## Story

- **Motion is the product, the script must say what the product does.** One film had great motion and a script made of abstract slogans ("Leads answered 100%"), and it was rejected: "the video is great but the script is shit." Every scene is a concrete product moment: real UI on screen and one line that answers "what does this do for me here?". When AI appears, show a real AI answer, not an empty panel.
- **Marketing copy is not the product.** A film written from a company's website made a vendor add-on the hero feature and invented a UI that doesn't exist. It was rejected outright. Build from the codebase, the docs and real app screens. Use the website only for positioning and tone. See `research/RESEARCH.md`.
- **The logo is exact, always.** Take the colours from the source (the logo component, the SVG, the CSS variables), never by eye. Sample the pixels on the final frame.
- **Each film gets its own world.** "The motion graphics are great" was praise for one film, not a house style. In a slate, write an art-direction table first: one row per film with its own palette, ground (flat / paper / dark grid / gradient / glow), type treatment and signature set piece. Show one frame per film side by side before full renders.
- **Open on a designed set piece**, not stock footage of people. Real footage works as a supporting plate only.

## Looking human-made, not AI-made

- Banned: ALL CAPS and `text-transform: uppercase`, emojis, italic display serifs, purple AI gradients, sparkles, orbs, particles, lens flares, neon outlines, fake UI, procedural phones or houses, drawn houses, floating 3D tags.
- Use big, detailed, physically lit elements: real UI, real photos, real footage, licence-safe faces (Wikimedia Commons PD/CC0, never generated).
- Scenes must not look "very white" or like a slideshow. Use colour and commercial grammar, not just the app palette.

## Flash safety (WCAG 2.3.1)

- At most one full-frame flood about every 8 s, and never more than 3 flashes in any 1 s. `qa/flashcheck.py` must pass on every render.
- **Moving UI text trips the flash gate**, mostly in vertical. A pile that slides every 0.5 s, a fast zoom across a chat thread, a big white window rising fast, or a 0 -> 99.99 counter all flip enough pixels. Fix it with motion blur proportional to speed (8-14 px at the peak), shorter travel, a fade, or counting from 85 % of the target.
- **At 120 fps** any camera push across dense tables or icon grids flips pixels. Blur-cut straight to the close framing, then only drift.
- Find the cause with a per-pixel transition heatmap over the failing 1 s window, not by guessing. The reported time is the end of the window.
- **Draft and final renders differ near the threshold.** A draft that passes at the edge can warn at `--quality high`. Always flashcheck the final file.
- Never run two fixers on one film in parallel. Each verifies a state the other is changing.

## Sharpness and size

- **"1080 feels very blurry."** Render at 4K and downscale (lanczos, CRF 15). Never deliver a native 1080 capture. `scripts/render-matrix.sh` does this by default.
- No `will-change` on text. Push from 0.9 to 1.0, not from 1.0 to 1.3. Keep rasters at or below native size at 4K.
- **Put hard size targets in every SPEC row**: hero element at 50-85 % of frame height, story text >= 30-36 px, headlines >= 100-120 px, wordmark >= 180 px. Without numbers, builders and critics both left elements small on lots of black.
- Story text >= 26 px at 1080p in 16:9, >= 30 px in vertical and square. Push the camera into phone threads when the bubbles are small.
- If people say the frame rate drops when they share, render at 120 fps (4K, then downscaled).

## Formats

- **Vertical is not landscape shrunk.** First drafts put content in the top half and left the rest black. In 9:16 the story lives in x 70-940, y 270-1240. Centre the group there, scale it up and keep a light source under it.
- Native layouts per format inside the safe zones (`formats/safe-*.png`), never crops. Ship a native 9:16 cut with every film.

## Sound

- **A designed SFX on every on-screen UI action**: pop per notification, send/receive, booking chime, approve tap, pen + chime on signed, ka-ching on paid. Quiet ticks at -20 dB under music are inaudible. Sidechain-duck the music under SFX and VO.
- **No beat-pumping.** Camera pushes, logo pulses or glow throbs on every beat read as "tub tub tub". Cuts may land on beats; nothing scales, glows or flashes on them.
- **Give music options, don't pick blind.** Three per film, each cut to a bar-aligned window so the bloom lands on the reveal and the resolve on the logo.
- **VO films need a VO bed, not a hype track**: sparse, warm piano/plucks/pulse, phrases in the VO gaps, a bloom (not a drop) on the reveal.
- **Snappy VO**: ElevenLabs stock voice, speed ~1.1, higher stability, no audio tags, no ellipses or dashes, one full-script generation for momentum. Cut fillers with whisper and cap pauses (0.22 s sentence, 0.14 s comma).
- HyperFrames renders land 0.7-1.9 LU under the mastered mix. Mux `audio/mix.wav` onto the picture (render-matrix does this). Master to -14 LUFS / -1 dBTP.

## Building with agents

- One builder per scene group, each owning only its files, with the archetype README and the PATTERNS section as its brief. Then an independent critic looks at snapshots against the rules, then a fix pass.
- Cap concurrency to your RAM (about 8 agents on a 16 GB Mac). One render at a time when the machine lags.
- Fast turnaround: split rework across parallel agents per scene, and do renders and mixes yourself with a prepared script. Don't run a sequential "finisher" agent for mechanical steps.

## HyperFrames and tooling traps

- 4K60 needs `HF_CAPTURE_PARALLEL_STREAM=true --workers 4`, or it disk-captures ~24 GB per 49 s and aborts. Check free disk first.
- `npx hyperframes snapshot --at t1,t2 --no-end -o <dir>` is your eye. Adjacent tiles in a contact sheet can visually merge text, so check single frames (`ffmpeg -ss t -frames:v 1`) before "fixing" a clip.
- Tracking collapse: move spans, don't tween `letter-spacing` (lint rejects it). No `<br>` in body text.
- Glass on a cream bloom reads as a white square. Fade glass objects before any bloom peak.
- zsh: `set -- $var` doesn't split (use `${=var}`); `"$WH:flags"` loses `:fl` (write `"${WH}:flags"`); an unmatched glob aborts a `&&` chain.
- ElevenLabs: the account's usage counter lags minutes behind. `audio/vo.py` keeps a local ledger and refuses any call over the job cap.
