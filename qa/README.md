# QA gates

`qa/run-all.sh <project> <video> <format>` runs every gate and writes `<project>/qa/QA-<format>.md`
(PASS / WARN / FAIL per gate; exit 2 on any FAIL). `scripts/render-matrix.sh` calls it after each render.

| gate | tool | pass rule |
|---|---|---|
| composition check | `npx hyperframes@0.8.183 check` (in the project) | exit 0: lint, runtime, layout, motion and contrast clean. Any error = FAIL |
| frame jumps | `framecheck.py <video> <fps>` | WARN when the largest frame-to-frame mean difference is over 60 (hard cut or flood: confirm it is intended) |
| flash safety | `flashcheck.py <video>` | exit 0 PASS. WARN at exactly 3 flashes in 1 s over the area threshold; FAIL above 3 per second or two floods less than 8 s apart. Thresholds are fixed (WCAG 2.2 SC 2.3.1) |
| safe zones | `safezone.py <video> <format> [--frames 8] [--out png]` | 9x16, 4x5, 1x1 only. WARN when an unsafe band has text-like detail (over 3 % strong Sobel edges) in any sampled frame; writes a contact sheet with the overlay for the eye check. Overlays: `formats/safe-*.png` |
| copy claims | `claims.py <project>` | FAIL on banned words, never-claim keywords (lease, brief sent, reminders), ALL CAPS of 3+ letters (except SMS PM AM ID PDF), emoji, uppercase CSS, italic serif / Instrument Serif, VO dashes or ellipses |
| loudness | ffmpeg ebur128 on the video | -14 LUFS +-1 (WARN beyond +-0.5), true peak at or below -1.0 dBTP (FAIL above -0.9) |
| fps | ffprobe | exactly 60 |
| size | ffprobe vs `formats/presets.json` | 1x or 2x (4K) of the preset size |

Separate tools: `vo_diff.py <project> <take>` (whisper vs script; exit 1 on missing or extra words, fillers,
pauses over 0.35 s; brand word misheard is a note), `contact.py <video> <fps> <outprefix>` (6x5 sheets for review),
`test_flashcheck.py` (15 calibration cases).

Interpreters: `uvx --python 3.12 --with numpy --with pillow python -I <script>` (claims.py needs only python3).
