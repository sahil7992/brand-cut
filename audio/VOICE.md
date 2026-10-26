# Voiceover providers

`audio/vo.py say <project>` writes `audio/vo/<take>/L01.wav...` (48 kHz mono) and `lines.json` with every provider, so `mix.py`, `qa/vo_diff.py` and storyboard timing do not care which one ran.

## How `--provider auto` (default) picks
1. `ELEVENLABS_API_KEY` set: **elevenlabs** (best quality, budget guard + ledger apply).
2. else `uvx` present: **kokoro** (local, open source, no setup, no key).
3. else **system** (macOS `say`, or `espeak-ng` on Linux).

It prints the choice and why. If Kokoro fails (for example espeak-ng missing) it reports the error and falls through to system. Nothing is installed for you.

## Commands
```
python3 audio/vo.py say <project> --take v1                         # auto
python3 audio/vo.py say <project> --provider kokoro --voice am_michael --speed 1.05
python3 audio/vo.py say <project> --provider system [--voice Samantha]
python3 audio/vo.py voices          # Kokoro list without a key, account voices with one
python3 audio/vo.py sfx "soft message pop" out.wav   # no key: copies the closest bundled SFX
python3 audio/vo.py music ...       # key only; otherwise drop a track in $MOTION_LIBRARY/music (audio/music.md)
```
Script format is unchanged: `audio/vo/script.txt`, one line per VO line, optional `@12.5 ` start prefix (mix.py needs it on every line).

## Kokoro
Kokoro-82M runs through `uvx --python 3.12 --with kokoro --with soundfile` in a throwaway env (`audio/tts_kokoro.py`), one synthesis call per line, so no alignment is needed. First run downloads about 330 MB of weights plus Python deps (a few GB of cache in total, mostly torch). `--voice` takes any Kokoro id; anything else falls back to `af_heart`.

| Voice | Character |
|---|---|
| `af_heart` | American female, warm (default) |
| `af_bella`, `af_nicole`, `af_sarah` | American female |
| `am_michael` | American male, steady |
| `am_adam`, `am_fenrir` | American male |
| `bf_emma`, `bm_george` | British |

`--speed` maps directly (Kokoro 1.0 is normal; the 1.1 default suits product films). ElevenLabs-only flags (`--model --stability --similarity --style --seed`) are ignored by the local providers. Local takes have no filler or pause cleanup (not needed: lines are synthesized separately and edge silence is trimmed).

## Licences
- Kokoro-82M: Apache-2.0 (model and code), output usable commercially.
- ElevenLabs output: per your plan terms (commercial use depends on the tier).
- macOS `say` voices: personal use; do not ship them in commercial work.
- espeak-ng: GPL-3.0 as a tool; output is fine, but it sounds robotic.
