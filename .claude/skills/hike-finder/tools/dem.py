import math, sys, os, urllib.request, numpy as np
from PIL import Image
Z=14
W,E,Sb,N=-89.775,-89.655,43.395,43.445
def tile(lon,lat):
    n=2**Z; x=(lon+180)/360*n; lr=math.radians(lat)
    y=(1-math.log(math.tan(lr)+1/math.cos(lr))/math.pi)/2*n
    return x,y
x0,y0=tile(W,N); x1,y1=tile(E,Sb)
tx=range(int(x0),int(x1)+1); ty=range(int(y0),int(y1)+1)
out=sys.argv[1]
rows=[]
for y in ty:
    row=[]
    for x in tx:
        p=f"{out}/{Z}_{x}_{y}.png"
        if not os.path.exists(p):
            urllib.request.urlretrieve(f"https://s3.amazonaws.com/elevation-tiles-prod/terrarium/{Z}/{x}/{y}.png",p)
        a=np.asarray(Image.open(p).convert('RGB')).astype(np.float64)
        row.append(a[:,:,0]*256+a[:,:,1]+a[:,:,2]/256-32768)
    rows.append(np.hstack(row))
m=np.vstack(rows)
np.save(f"{out}/mosaic.npy",m)
print(m.shape, tx[0],ty[0], m.min()*3.28084, m.max()*3.28084)
open(f"{out}/meta.txt","w").write(f"{Z} {tx[0]} {ty[0]} {m.shape[0]} {m.shape[1]}")
