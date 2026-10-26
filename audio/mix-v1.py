# Music + designed SFX, music ducked under the SFX bus. Usage: python mix.py <project_dir>
import numpy as np, subprocess, sys, os
P=sys.argv[1]; SR=48000; DUR=49.0
def load(f):
    b=subprocess.run(['ffmpeg','-v','error','-i',f,'-ar',str(SR),'-ac','2','-f','f32le','-'],capture_output=True,check=True).stdout
    return np.frombuffer(b,dtype=np.float32).reshape(-1,2).copy()
music=load(os.path.join(P,'assets/addiction-cut.wav'))[:int(DUR*SR)]*10**(-3.5/20)
N=len(music); sfx=np.zeros((N,2),np.float32)
# (absolute time of the visual event, file, which point of the sound lands on it, gain dB)
EVENTS=[
 (6.34,'pop_soft','onset',-8),(7.59,'tap','onset',-3),
 (8.70,'whoosh_push','peak',-9),
 (9.65,'tap','onset',-6),(9.91,'pop_soft','onset',-11),(11.21,'pop_soft','onset',-12),(11.46,'pop_soft','onset',-12),
 (13.92,'fly_in','peak',-11),(14.06,'fly_in','peak',-12),(14.25,'pop_soft','onset',-12),(14.55,'pop_soft','onset',-13),(14.85,'pop_soft','onset',-13),(15.15,'pop_soft','onset',-13),
 (15.70,'whoosh_push','peak',-12),
 (17.55,'fly_in','peak',-11),(17.63,'fly_in','peak',-12),(17.71,'fly_in','peak',-12),(17.79,'fly_in','peak',-13),
 (20.45,'flypast','peak',-5),
 (22.15,'pop_clean','onset',-8),(22.30,'done_chime','onset',0),
 (27.05,'whoosh_push','peak',-12),(27.78,'pen','onset',-10),(28.88,'pop_clean','onset',-8),
 (31.90,'tap','onset',-4),(32.12,'kaching','peak',-8),
 (34.22,'pop_soft','onset',-10),(34.92,'pop_soft','onset',-10),(35.38,'pop_soft','onset',-10),(35.84,'pop_soft','onset',-10),(36.31,'pop_soft','onset',-10),
 (40.40,'whoosh_push','peak',-10),
 (43.50,'logo_hit','onset',-5),
]
def mark(x,mode):
    m=x.mean(1); e=np.sqrt(np.convolve(m**2,np.ones(480)/480,'same'))
    return int(np.argmax(e>0.1*e.max())) if mode=='onset' else int(np.argmax(e))
for t,name,mode,db in EVENTS:
    x=load(os.path.join(P,'audio/sfx',name+'.wav'))
    if name=='pen': x=x[:int(1.0*SR)]*np.linspace(1,0,int(1.0*SR))[:,None]**0.5
    s=int(t*SR)-mark(x,mode); a=max(0,s); x=x[a-s:]; e=min(N,a+len(x))
    sfx[a:e]+=x[:e-a]*10**(db/20)
# sidechain duck: up to ~3.5 dB under the SFX bus, 5 ms attack, 220 ms release
env=np.abs(sfx).max(1); g=np.empty(N,np.float32); v=0.0
aa=np.exp(-1/(0.005*SR)); rr=np.exp(-1/(0.22*SR))
for i in range(N):
    c=env[i]; v = aa*v+(1-aa)*c if c>v else rr*v+(1-rr)*c; g[i]=v
duck=10**(-3.5*np.clip(g/0.15,0,1)/20)
out=music*duck[:,None]+sfx
peak=np.abs(out).max(); print('pre-limit peak dBFS %.2f'%(20*np.log10(peak)))
tmp=os.path.join(P,'audio/mix_raw.f32'); out.astype(np.float32).tofile(tmp)
subprocess.run(['ffmpeg','-v','error','-y','-f','f32le','-ar',str(SR),'-ac','2','-i',tmp,'-af','alimiter=limit=0.891:attack=3:release=60:level=disabled','-c:a','pcm_s16le',os.path.join(P,'audio/mix.wav')],check=True)
os.remove(tmp)
