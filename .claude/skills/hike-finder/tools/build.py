import math,sys,json,io,base64,numpy as np,matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from PIL import Image
sys.path.insert(0,sys.argv[2]); from trails import SEG,POI
d=sys.argv[1]; out=sys.argv[3]
Z,tx0,ty0,H,W=map(int,open(f"{d}/meta.txt").read().split())
M=np.load(f"{d}/mosaic.npy")*3.28084; n=2**Z
def ll2px(lon,lat):
    x=(lon+180)/360*n; lr=math.radians(lat); y=(1-math.log(math.tan(lr)+1/math.cos(lr))/math.pi)/2*n
    return (x-tx0)*256,(y-ty0)*256
def px2ll(px,py):
    x=tx0+px/256; y=ty0+py/256
    return x/n*360-180, math.degrees(math.atan(math.sinh(math.pi*(1-2*y/n))))
def el(lat,lon):
    x,y=ll2px(lon,lat); j,i=x-0.5,y-0.5; i0,j0=int(i),int(j); fi,fj=i-i0,j-j0
    a=M[i0,j0]*(1-fj)+M[i0,j0+1]*fj; b=M[i0+1,j0]*(1-fj)+M[i0+1,j0+1]*fj
    return a*(1-fi)+b*fi
LAKE=962.3
# snap Tumbled Rocks to west shoreline (25 m inland)
def westshore(lat):
    x,y=ll2px(-89.745,lat); i=int(y)
    j=int(x)
    while M[i,j]>LAKE and j<W-1: j+=1
    lon,_=px2ll(j,y); return lon-25/(111320*math.cos(math.radians(lat)))
tr=[(43.4118,-89.7382)]
for lat in np.arange(43.4128,43.4254,0.0012): tr.append((round(lat,5),round(westshore(lat),5)))
tr.append((43.4268,-89.7349)); tr.append((43.4282,-89.7338)); SEG['tumbled_rocks']['pts']=tr
# map extent
Wl,El,Sl,Nl=-89.7455,-89.6765,43.4030,43.4315
lat0=(Sl+Nl)/2; kx=111320*math.cos(math.radians(lat0)); ky=110950
MW=(El-Wl)*kx; MH=(Nl-Sl)*ky
VBW=1000; sc=VBW/MW; VBH=MH*sc
def proj(lat,lon): return ((lon-Wl)*kx*sc, (Nl-lat)*ky*sc)
x0,y0=ll2px(Wl,Nl); x1,y1=ll2px(El,Sl); sub=M[int(y0):int(y1),int(x0):int(x1)]
# hillshade
cell=( (El-Wl)*kx/sub.shape[1]*3.28084, (Nl-Sl)*ky/sub.shape[0]*3.28084 )
gy,gx=np.gradient(sub, cell[1], cell[0])
slope=np.arctan(np.hypot(gx,gy)*1.6); aspect=np.arctan2(-gx,gy)
az,alt=math.radians(315),math.radians(45)
hs=np.clip(np.sin(alt)*np.cos(slope)+np.cos(alt)*np.sin(slope)*np.cos(az-aspect),0,1)
shade=(1-hs)  # darkness
img=Image.fromarray((np.clip(shade*1.25,0,1)*255).astype(np.uint8),'L').resize((1100,int(1100*VBH/VBW)),Image.LANCZOS)
rgba=Image.new('RGBA',img.size,(0,0,0,0)); rgba.putalpha(img)
buf=io.BytesIO(); rgba.save(buf,'PNG',optimize=True); hill=base64.b64encode(buf.getvalue()).decode()
# contours
xs=np.linspace(0,VBW,sub.shape[1]); ys=np.linspace(0,VBH,sub.shape[0])
fig=plt.figure(); levels=np.arange(820,1600,20)
cs=plt.contour(xs,ys,sub,levels=levels)
contours=[]
for lv,segs in zip(cs.levels,cs.allsegs):
    for sgm in segs:
        if len(sgm)<6: continue
        pts=sgm[::2] if len(sgm)>40 else sgm
        dpath="M"+" L".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)
        contours.append({"z":int(lv),"d":dpath,"idx":int(lv)%100==0})
# lake polygon
flat=(np.abs(sub-961.9)<0.35)
from collections import deque
cx_,cy_=ll2px(-89.731,43.42); si,sj=int(cy_-int(y0)),int(cx_-int(x0))
mask=np.zeros_like(sub); q=deque([(si,sj)]); mask[si,sj]=1
while q:
    i,j=q.popleft()
    for a,c in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
        if 0<=a<sub.shape[0] and 0<=c<sub.shape[1] and flat[a,c] and not mask[a,c]:
            mask[a,c]=1; q.append((a,c))
lakec=proj(43.4195,-89.7312)
cl=plt.contour(xs,ys,mask,levels=[0.5])
lake=[]
for sgm in cl.allsegs[0]:
    if len(sgm)<20: continue
    cx=np.mean(sgm[:,0]); cy=np.mean(sgm[:,1])
    lake.append("M"+" L".join(f"{p[0]:.1f},{p[1]:.1f}" for p in sgm[::2])+" Z")
plt.close('all')
# trails
def hav(a,b):
    R=6371000; p1,p2=math.radians(a[0]),math.radians(b[0]); dl=math.radians(b[1]-a[1]); dp=p2-p1
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2; return 2*R*math.asin(math.sqrt(h))
def densify(pts,step=8):
    o=[pts[0]]
    for a,b in zip(pts,pts[1:]):
        L=hav(a,b); k=max(1,int(L/step))
        for t in range(1,k+1): o.append((a[0]+(b[0]-a[0])*t/k, a[1]+(b[1]-a[1])*t/k))
    return o
trails={}
for k,s in SEG.items():
    p=s['pts']; trails[k]={"name":s['name'],"conf":s['conf'],"d":"M"+" L".join("%.1f,%.1f"%proj(*q) for q in p),
        "mi":round(sum(hav(a,b) for a,b in zip(p,p[1:]))/1609.34,2)}
# routes: list of (segment, reverse)
F,R=False,True
WEST=[("west_bluff",F),("south_shore_w",F),("south_shore_e",F)]
GROT=[("grottos",F),("grottos",R)]
BACKW=[("south_shore_e",R),("south_shore_w",R),("tumbled_rocks",F)]
EAST=[("north_shore",F),("east_bluff",F),("east_bluff_woods",F)]
UPX=[("uplands",F),("uplands",R)]
IAT=[("north_shore",F),("east_bluff_woods",R),("uplands",F),("roznos_climb",F),("roznos_meadow",F),
     ("roznos_meadow",R),("roznos_climb",R),("uplands",R),("east_bluff",R)]
ROUTES={
 "o1d1":dict(opt=1,day="Mon Oct 19",title="Both bluffs, figure-eight + Grottos",seq=WEST+GROT+BACKW+EAST,
   push="Steep rock-stair climbing with poles (~2× the 3 Dune Challenge)",
   notes=["Start at the North Shore. West Bluff in the morning light.","Grottos out-and-back from the South Shore: flat, cool, quiet.","Back north on Tumbled Rocks, then up the East Bluff stone steps.","Aim to reach the East Bluff overlook and Devil's Doorway ~5–5:45 pm for golden hour.","Gentle way down: East Bluff Woods Trail (no stone steps). Sunset ~6:05 pm."]),
 "o1d2":dict(opt=1,day="Tue Oct 20",title="Ice Age Trail uplands to Roznos Meadow and back",seq=IAT,
   push="Hours on rolling terrain; one 475 ft climb out of Roznos Meadow",
   notes=["Gated on the morning check.","Up the gentle East Bluff Woods grade, then east on the Uplands (Ice Age Trail).","Down the stream switchbacks to Roznos Meadow and the Hwy 113 lot, then back up.","Finish along the East Bluff top past Devil's Doorway. Skip the north-end stone steps by returning on East Bluff Woods instead."]),
 "o2d1":dict(opt=2,day="Mon Oct 19",title="Figure-eight + Grottos + Uplands extension",seq=WEST+GROT+BACKW+[("north_shore",F),("east_bluff",F)]+UPX+[("east_bluff_woods",F)],
   push="Climbing volume, stairs, and day one of back-to-back",
   notes=["Option 1's Monday, plus an out-and-back east along the Uplands from the East Bluff Woods junction.","Go only if the West Bluff with poles stays at 2/10 or less and clears fast."]),
 "o2d2":dict(opt=2,day="Tue Oct 20",title="Figure-eight reversed + Grottos",seq=[("east_bluff_woods",R),("east_bluff",R),("north_shore",R),("tumbled_rocks",R),("south_shore_w",F),("south_shore_e",F)]+GROT+[("south_shore_e",R),("south_shore_w",R),("west_bluff",R)],
   push="Second day of ~1,000 ft of stairs",
   notes=["Gentle start up East Bluff Woods, then down the East Bluff stone steps.","Tumbled Rocks to the South Shore, Grottos out-and-back.","Finish climbing the West Bluff from its south end, down its north end."]),
 "o3d1":dict(opt=3,day="Mon Oct 19",title="East Bluff loop + lakeshore + Grottos + Steinke Basin",seq=EAST+[("north_shore",R),("tumbled_rocks",R),("south_shore_w",F),("south_shore_e",F),("grottos",F),("steinke",F),("grottos",R),("south_shore_e",R),("south_shore_w",R),("tumbled_rocks",F)],
   push="Hours only; one bluff climb",
   notes=["One East Bluff climb (about the 3 Dune Challenge's climbing), down the gentle East Bluff Woods.","Long flat miles: Tumbled Rocks, Grottos, and the Steinke Basin loop (old glacial lake bed).","Steinke Basin replaces the Roznos Meadow flat section from the earlier plan: it's flat too, and connects directly to the Grottos."]),
 "o3d2":dict(opt=3,day="Tue Oct 20",title="Ice Age Trail uplands to Roznos Meadow and back",seq=IAT,
   push="Hours on rolling terrain",
   notes=["Same as Option 1's Tuesday.","Skip the north-end stone steps by returning on East Bluff Woods."]),
}
def route_pts(seq):
    pts=[]
    for k,r in seq:
        p=SEG[k]['pts'][::-1] if r else SEG[k]['pts']
        if pts:
            g=hav(pts[-1],p[0]); assert g<40, (k,r,g)
            p=p[1:]
        pts+=p
    return pts
out_routes={}
for rid,r in ROUTES.items():
    p=densify(route_pts(r['seq']),10)
    dist=[0.0]
    for a,b in zip(p,p[1:]): dist.append(dist[-1]+hav(a,b))
    z=np.array([el(*q) for q in p]); zs=np.convolve(np.pad(z,4,mode='edge'),np.ones(9)/9,'valid')
    gain=loss=0; ref=zs[0]
    for v in zs[1:]:
        if v-ref>=6: gain+=v-ref; ref=v
        elif ref-v>=6: loss+=ref-v; ref=v
    mi=dist[-1]/1609.34
    hrs=mi/3.0+gain/1000.0
    step=max(1,len(p)//400)
    prof=[[round(dist[i]/1609.34,3),round(float(zs[i]),0)] for i in range(0,len(p),step)]
    xy=[["%.1f"%proj(*p[i])[0],"%.1f"%proj(*p[i])[1]] for i in range(0,len(p),step)]
    conf=[ ]  # approximate share
    approx=sum(SEG[k]['mi'] if False else 0 for k,_ in r['seq'])
    am=0;tm=0
    for k,_ in r['seq']:
        L=sum(hav(a,b) for a,b in zip(SEG[k]['pts'],SEG[k]['pts'][1:]))/1609.34; tm+=L
        if SEG[k]['conf']=='approx': am+=L
    out_routes[rid]=dict(opt=r['opt'],day=r['day'],title=r['title'],push=r['push'],notes=r['notes'],
        d="M"+" L".join("%.1f,%.1f"%proj(*q) for q in route_pts(r['seq'])),
        mi=round(mi,1),gain=int(round(gain/10)*10),loss=int(round(loss/10)*10),hrs=round(hrs*1.25,1),hrs_move=round(hrs,1),
        zmin=int(zs.min()),zmax=int(zs.max()),approx_pct=int(round(100*am/tm)),prof=prof,xy=xy,
        segs=sorted(set(SEG[k]['name'] for k,_ in r['seq'])))
pois=[{"name":nm,"type":t,"x":round(proj(la,lo)[0],1),"y":round(proj(la,lo)[1],1),"z":int(el(la,lo))} for nm,la,lo,t in POI]
# scale bar & north; grid of 0.5 mi
data=dict(lakec=[round(lakec[0],1),round(lakec[1],1)],vbw=VBW,vbh=round(VBH,1),m_per_unit=round(1/sc,3),hill=hill,contours=contours,lake=lake,trails=trails,routes=out_routes,pois=pois,
          extent=[Wl,El,Sl,Nl])
json.dump(data,open(out,'w'))
for k,v in out_routes.items(): print(k,v['mi'],'mi',v['gain'],'ft',v['hrs_move'],'h moving',v['hrs'],'h total', 'approx',v['approx_pct'],'%')
for k,v in trails.items(): print(' ',v['name'],v['mi'])
print('contours',len(contours),'lake',len(lake),'hill KB',len(hill)//1024)
