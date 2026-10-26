import numpy as np, subprocess, sys
f=sys.argv[1]; W,H=192,108
raw=subprocess.run(['ffmpeg','-v','error','-i',f,'-vf',f'scale={W}:{H}','-f','rawvideo','-pix_fmt','gray','-'],capture_output=True).stdout
fr=np.frombuffer(raw,np.uint8).reshape(-1,H,W).astype(np.float32)
fps=float(sys.argv[2]) if len(sys.argv)>2 else 30
mean=fr.mean((1,2)); d=np.abs(np.diff(fr,axis=0)).mean((1,2))
print('frames',len(fr))
print('darkest frames (t,mean):',[(round(i/fps,2),round(float(mean[i]),1)) for i in np.argsort(mean)[:5]])
med=np.median(d); top=np.argsort(d)[::-1][:14]
print('biggest frame-to-frame jumps (t, diff, median=%.2f):'%med, sorted([(round((i+1)/fps,2),round(float(d[i]),1)) for i in top]))
