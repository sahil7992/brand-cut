import numpy as np, subprocess, sys, glob, os
for f in sorted(glob.glob(os.path.join(sys.argv[1],'*.wav'))):
    x=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',f,'-ac','1','-f','f32le','-'],capture_output=True).stdout,dtype=np.float32)
    w=480; e=np.sqrt(np.convolve(x**2,np.ones(w)/w,'same'))
    on=np.argmax(e>0.1*e.max())/48000
    print(f"{os.path.basename(f):16s} onset={on:.3f} peak={np.argmax(e)/48000:.3f} dur={len(x)/48000:.2f}")
