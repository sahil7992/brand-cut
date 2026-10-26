#!/usr/bin/env python3
"""Kokoro-82M helper, run in an isolated env by vo.py:
uvx --python 3.12 --with "kokoro>=0.9.4" --with soundfile --with pip python -I tts_kokoro.py <lines.json> <out_dir> <voice> <speed>
lines.json = ["text", ...]; writes <out_dir>/raw01.wav ... at 24 kHz, one synthesis call per line.
"""
import json, sys
import numpy as np
import soundfile as sf
from kokoro import KPipeline

lines, out, voice, speed = json.load(open(sys.argv[1])), sys.argv[2], sys.argv[3], float(sys.argv[4])
pipe = KPipeline(lang_code=voice[0] if voice[:1] in "abefhijpz" else "a", repo_id="hexgrad/Kokoro-82M")
for i, text in enumerate(lines, 1):
    chunks = [np.asarray(a) for _, _, a in pipe(text, voice=voice, speed=speed) if a is not None]
    if not chunks:
        sys.exit(f"kokoro produced no audio for line {i}: {text}")
    sf.write(f"{out}/raw{i:02d}.wav", np.concatenate(chunks), 24000)
