import numpy as np, sys
from scipy.signal import fftconvolve
f=np.fromfile(sys.argv[1],dtype=np.float32); r=np.fromfile(sys.argv[2],dtype=np.float32)
c=fftconvolve(f,r[::-1],mode='valid')
e=np.sqrt(fftconvolve(f**2,np.ones(len(r)),mode='valid'))+1e-9
n=c/(e*np.linalg.norm(r))
i=int(np.argmax(n)); print('offset_s=%.3f score=%.3f'%(i/8000,n[i]))
top=np.argsort(n)[::-1]
seen=[]
for j in top:
    if all(abs(j-s)>8000*3 for s in seen): seen.append(j)
    if len(seen)==4: break
print([('%.2f'%(s/8000),'%.3f'%n[s]) for s in seen])
