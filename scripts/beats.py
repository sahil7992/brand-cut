import numpy as np, librosa, sys
y,sr=librosa.load(sys.argv[1],sr=22050,mono=True,duration=float(sys.argv[2]))
tempo,beats=librosa.beat.beat_track(y=y,sr=sr)
bt=librosa.frames_to_time(beats,sr=sr)
print('tempo',np.round(tempo,1)); print('beats',np.round(bt,2).tolist())
rms=librosa.feature.rms(y=y,hop_length=11025)[0]
print('rms/0.5s dB',np.round(20*np.log10(rms+1e-6),0).astype(int).tolist())
on=librosa.onset.onset_detect(y=y,sr=sr,units='time',backtrack=False)
st=librosa.onset.onset_strength(y=y,sr=sr); ot=librosa.times_like(st,sr=sr)
strong=[round(float(t),2) for t,s in zip(ot,st) if s>np.percentile(st,97)]
print('strong onsets',strong)
