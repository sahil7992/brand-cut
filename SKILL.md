---
name: brand-cut
description: Plug-and-play motion design studio for product films in HyperFrames. Give it a company name, a URL or a codebase and it researches the product, builds a brand kit (logo, fonts, colours, real UI), scripts real product moments, and builds the film from 30 archetype scene templates studied from 18 premium reference reels. Includes an ElevenLabs voiceover pipeline with a budget guard, an SFX mix, native format presets (16:9 1080/4K, 9:16, 1:1, 4:5), and QA gates including a WCAG flash check. Use for product launch films, social cuts, explainers, logo stings, reel recreations ("make this kind of motion for X"), or "make a video for <company>".
license: MIT
compatibility: Any agent that reads Agent Skills (Claude Code, Codex, OpenCode, ...) with shell access. Needs Node 18+, Python 3.10+, ffmpeg and uv. Web access for company research. ELEVENLABS_API_KEY optional (falls back to open-source Kokoro TTS).
metadata:
  author: sahil7992
  version: "0.1.0"
---

# brand-cut

`company / URL / repo -> research -> brand kit -> script of product moments -> storyboard -> (VO) -> archetype build -> (mix) -> QA -> render matrix -> deliver`

Read `LEARNINGS.md` before your first film. It is the list of everything that got a film rejected or a render failed.

## 0. Rules (binding)
- **Every scene is a concrete product moment** with real UI. When AI appears, a real AI answer is on screen. No abstract slogans.
- **Truth over marketing.** Build from the codebase, docs and real app screens; the website is for tone only. Every on-screen claim traces to a source (`qa/claims.py`).
- **Exact logo**, colours taken from source, never approximated.
- **Not AI-looking.** No ALL CAPS / `text-transform: uppercase`, emojis, italic display serifs, purple AI gradients, sparkles, orbs, particles, lens flares, neon outlines, fake UI, procedural phones or houses.
- **Flash-safe.** At most one full-frame flood per ~8 s, never more than 3 flashes in any 1 s. `qa/flashcheck.py` passes on the final file.
- **Sound.** A designed SFX on every on-screen UI action; music ducks under SFX and VO; no beat-pumping.
- **Formats** are native layouts inside the safe zones, never crops. 60 fps; 1080 is rendered at 4K and downscaled.
- **Never** post, upload or publish anything, or buy credits, without the user saying so.

## 1. Layout
```
SKILL.md, LEARNINGS.md  this file, the traps
research/RESEARCH.md    stage 0: company name / URL / codebase -> brand kit + truths + real UI captures
brand.schema.json       brand kit schema
brands/demo/            "Tidewell", a fictional brand; copy it for a new brand
archetypes/             CONTRACT.md + 30 scene templates (scene.html + README.md)
formats/                presets.json (sizes, safe insets, render presets, loudness) + safe-*.png overlays
shared/                 hf.js (runtime: format, pick, seeded rng), phone.js (photoreal phone), type.js, uikit/ (chat, notification,
                        calendar, receipt components)
audio/                  vo.py (ElevenLabs + budget guard), mix.py, music.md, sfx/ (INDEX.md, INDEX.json, files)
qa/                     flashcheck.py, framecheck.py, safezone.py, claims.py, vo_diff.py, contact.py, run-all.sh
scripts/                new-film.sh, add-scene.py, set-format.py, set-brand.py, brand-css.py, render-matrix.sh,
                        save-ref.sh, index-refs.py, shazam.py, xcorr.py, beats.py, peaks.py
templates/              SPEC.md (film contract), index.html, project/, structures/
reference/              PATTERNS.md (archetype library + laws), RESEARCH-digest.md, studies/ (18 reel breakdowns + INDEX.md)
examples/               finished sample films with their brand kit, SPEC and stills
```
Requirements: Node 18+ (`npx hyperframes`), Python 3.10+, ffmpeg, [uv](https://docs.astral.sh/uv/) (`uvx` runs the QA and audio scripts in throwaway envs). Optional: `ELEVENLABS_API_KEY` for voiceover (without it, `audio/vo.py` falls back to open-source Kokoro TTS; see `audio/VOICE.md`), a music folder (`$MOTION_LIBRARY/music`).

Works in any agent with a shell. Where this file says "subagents", run the steps sequentially if your agent has none; "web fetch" means whatever fetch/browse tool your agent has, or `curl`.

## 2. Pipeline
0. **Research** (`research/RESEARCH.md`). Codebase mode when you have the repo (most accurate), website mode otherwise, both when you can. Output: `brands/<id>/brand.json`, `truths` with sources, real UI captures in `brands/<id>/assets/ui/`, and 5-8 product moments.
1. **Brief.** Audience, formats, length, VO or music-only or silent, the one thing the viewer must understand.
2. **Brand kit.** Copy `brands/demo/`, fill palettes (9-stop glowRamp), fonts with files, logo, UI captures, story, truths, voice. Validate against `brand.schema.json`.
3. **Scaffold.** `scripts/new-film.sh <brand> <dir> <format> [format...] [--palette id]` -> index.html with the brand block (fonts, CSS vars, `window.BRAND`), film.json, SPEC.md, audio stubs. Re-theme any time: `scripts/set-brand.py <dir> <brand> [palette]`. Switch format: `scripts/set-format.py <dir> <fmt>`.
4. **Script.** SPEC.md section 2: one row per product moment (real UI, on-screen words, VO line, proof, hard size targets). Reading limits: <= 3 words/s, <= 42 characters per line, 2 lines max.
5. **VO first (VO films).** `audio/vo/script.txt`, one line per VO line, then `python3 audio/vo.py say <dir> --voice <id> --take <name>`. It makes one request with timestamps, splits by alignment, cuts fillers and caps pauses. `lines.json` gives durations. Check with `qa/vo_diff.py <dir> <take>`. The budget guard refuses any call over the job cap.
6. **Storyboard** on the VO and the bar grid (`scripts/beats.py <wav> <dur>`). SPEC.md section 3: archetype, in/out, transition (non-flash first, PATTERNS section 4), SFX events.
7. **Music.** Three options cut to bar-aligned windows (bloom on the reveal, resolve on the logo); render the pick. See `audio/music.md`.
8. **Build from archetypes.** `python3 scripts/add-scene.py <dir> <archetype> <scene-id> <start> <dur> [--vars JSON]`, then customise. With subagents: one builder per scene group, each owning only its files, then an independent critic on snapshots, then fixes.
9. **Mix.** `audio/events.json` (music, VO lines, SFX with times from `audio/sfx/INDEX.md`, ducking) -> `python3 audio/mix.py <dir>` -> `audio/mix.wav` at -14 LUFS / -1 dBTP.
10. **QA.** `npx hyperframes check` with 0 errors, a draft render, then `qa/run-all.sh <dir> <video> <fmt>` (framecheck, flashcheck, safezone, claims, loudness, fps). Review `qa/contact.py <video> 10 <prefix>` sheets against section 0.
11. **Render matrix.** `scripts/render-matrix.sh <dir> [--4k 16x9]`: per format, 4K capture downscaled to 1080, audio muxed, QA gates run. Check free disk first.
12. **Deliver.** A folder with the videos, an `index.html` gallery and a short REPORT.md (what, credits used, music and voice alternates, what fell short). Open it for the user.

## 3. Formats (formats/presets.json)
| id | canvas | safe insets (t/b/l/r) | for |
|---|---|---|---|
| 16x9 | 1920x1080 | 108/108/192/192 | YouTube, LinkedIn, X, site |
| 9x16 | 1080x1920 | 270/680/70/140 | Reels, TikTok, Shorts |
| 1x1 | 1080x1080 | 86/86/135/135 | IG/LinkedIn feed |
| 4x5 | 1080x1350 | 108/108/86/86 | IG/FB feed |
| banner | 1920x600 | 60/60/96/96 | README / site header strip (silent loop) |

Scenes read `window.BRAND.format` and branch layout per format (`[data-fmt="9x16"]`). The short side is always 1080 px, so px sizes carry across; scale heroes up in vertical.

## 4. Archetypes (details in reference/PATTERNS.md)
glow-field (A01, full-film WebGL light) | glass-slab (A02, AI panel with a real streamed answer) | glass-tile-click (A03) | word-blur-in (A04) | tracking-collapse (A05) | chip-marquee (A06) | status-stack (A07, reference implementation) | wordmark-lockup (A08) | phone-tunnel (A09) | drum-wheel (A10) | card-carousel (A11) | network-lines (A12) | composer-send (A13) | card-burst (A14) | checklist-fix (A15) | orbit-chips (A16) | list-swap-toggle (A17) | object-launch (A18) | brutal-type (A19) | icon-ring (A20) | calendar-pick (A21) | product-hero (A22) | chat-thread (A23) | container-morph (A24) | notification-pile (A25) | docusign-sign (A26) | stripe-paid (A27) | logo-sting (A28) | branch-tree (A29) | counter-pill (A30) | logo-wheel (A31, looping "works with" carousel).

Film structures S1-S8 (SaaS explainer, 13 s vertical, premium polish checklist, dark cinematic, Figma showcase, gradient opener, hand-made sting, proof plate) are in PATTERNS.md section 5. Contract: `archetypes/CONTRACT.md` (brand-agnostic CSS vars, `window.BRAND`, per-instance variables, format-native, flash-safe, SFX cues in the README).

## 5. Studying a new reference reel
- `scripts/save-ref.sh <url>` downloads a reel with yt-dlp and makes a 2 fps overview + song ID; `scripts/index-refs.py` indexes it.
- Build 10 fps strips per 2 s and native-fps runs at key moments; track one element per frame to name the easing; beat grid with `scripts/beats.py`; palette hexes; per-frame luminance for the flash profile.
- Write `reference/studies/<id>.md`: shot list, construction per element, camera, easing numbers, transitions, type, palette, depth, sound, copy structure, why it is not AI, what would make it AI, archetypes. The 18 studies there are the worked examples.

## 6. Proven looks
- **Glow (A01):** one WebGL shader; scalar field -> 9-stop ramp, noise warp, dither; uniforms from a monotone-Hermite keyframe table driven by a GSAP proxy tween.
- **Glass:** `backdrop-filter: blur(22px) saturate(1.5) brightness(1.15)`, gradient bevel via mask-composite, inner highlight and shade, contact shadow, one sheen on motion.
- **Type:** a grotesk at 500, per-word blur-in 14 -> 0 px, scale 1.06 -> 1, power3.out, line re-centres, continuous pull-back.
- **Real UI:** recreate the product's components in HTML/CSS from its source or captures (`shared/uikit/` is a starting point); `HF.phone` maps a screen into the photoreal phone.
