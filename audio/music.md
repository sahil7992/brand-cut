# Music and mix

## Pick 3 options per film
Offer one of each and let the client choose by ear; do not pre-judge.
- **VO bed** (film has a voiceover): 96 to 125 BPM, sparse or airy, no lead melody in the speech band, a lift you can park on the end card. Library class "VO bed": piano-96-elevenP3, sparse-keynote-101-elevenE, glasspulse-101-elevenT1, glass-112-elevenF, techproduct-123-px383623, chillout-129-px12641.
- **Hype** (no VO, or a short teaser): 110 to 155 BPM, a build then a drop landed on the product reveal. Class "hype": glasspop-125-elevenA, circuit-110-px578473, product-117-px436870, housejuly-129-px605767, banger-136-px466403, tidalrush-155-px456799.
- Third option: the other class or a trending track (private cut). Match mood to the film: calm and premium for Ask or payments films, driving for the lead-to-showing story.
- Classes come from energy profile, not from listening. Audition each pick for 5 s before committing.

## Library
`${MOTION_LIBRARY:-./library}/music/` (read `LIBRARY.md`): `rf/` 12 royalty-free MP3 (source and licence per file in the table) with bar-aligned windows (start seconds for 15, 20 and 50 s cuts); `trending/` 8 WAV, private cuts only.

## Licences
- Pixabay Content License: free commercial use, no attribution, no standalone redistribution.
- ElevenLabs Music on Starter: commercial online use, not film, TV or radio, no resale or libraries. Re-verify before any paid release.
- Trending tracks: rights not cleared. Nothing is posted. For a real post, add the song in the app at post time (business accounts only get the commercial library).

## Cutting to the grid
`python3 scripts/beats.py <audio> <seconds>` prints tempo, beats, rms per 0.5 s and strong onsets (needs librosa). Cut scenes on bar lines (4 beats), land the product reveal on the drop or a downbeat, and never pulse visuals on every beat (no beat-pumping). Start the music at a library window offset so the first downbeat lands where scene 1 starts, then set `offset` in events.json. If the first hit sounds wrong, nudge by one beat.

## Trending-track route (private cuts only)
Use `trending/` files in a separate `*-private` cut. Name the file clearly, never upload it. The shippable cut uses an `rf/` track.

## events.json for `audio/mix.py`
```json
{"music": {"file": "${MOTION_LIBRARY:-./library}/music/rf/glasspop-125-elevenA.mp3", "offset": 7.66, "gain_db": -3.5, "fade_in": 0.3, "fade_out": 1.5},
 "vo": {"lines": "audio/vo/<take>/lines.json", "gain_db": 0},
 "sfx": [{"t": 1.23, "sound": "msg_pop_a", "gain_db": -4, "align": "onset"}],
 "duck": {"under_vo_db": -8, "under_sfx_db": -4, "attack": 0.15, "release": 0.4},
 "platform": "instagram", "duration": 49.0}
```
- `vo` can instead be `{"clips": [{"file": "audio/vo/x.wav", "at": 1.2}]}`; `lines.json` rows are `{file, at, dur}` as vo.py writes them.
- `sfx.sound` is a name from `audio/sfx/INDEX.md` (53 sounds). `align: onset` puts the first audible hit on `t`, `peak` the loudest moment; onset for taps and pops, peak for risers and booms.
- Run: `uvx --python 3.12 --with numpy python -I audio/mix.py <project>` writes `<project>/audio/mix.wav` (48 kHz stereo, exactly `duration` long, two-pass loudnorm to -14 LUFS, -1.0 dBTP) and prints the measured numbers. Music is ducked 8 dB under VO and 4 dB under each SFX.
- Rebuild the SFX index after adding files: `uvx --python 3.12 --with numpy python -I audio/build-sfx-index.py`.
