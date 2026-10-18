import math,sys,json,io,base64,numpy as np,matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from PIL import Image
from collections import deque
sys.path.insert(0,sys.argv[1]); from trails import SEG,POI,SEG2,POI2,FERRY
S=sys.argv[2]; OUT=sys.argv[3]
def hav(a,b):
    R=6371000; p1,p2=math.radians(a[0]),math.radians(b[0]); dl=math.radians(b[1]-a[1]); dp=p2-p1
    h=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2; return 2*R*math.asin(math.sqrt(h))
def densify(pts,step=10):
    o=[pts[0]]
    for a,b in zip(pts,pts[1:]):
        L=hav(a,b); k=max(1,int(L/step))
        for t in range(1,k+1): o.append((a[0]+(b[0]-a[0])*t/k, a[1]+(b[1]-a[1])*t/k))
    return o
class DEM:
    def __init__(s,d):
        s.Z,s.tx0,s.ty0,s.H,s.W=map(int,open(f"{d}/meta.txt").read().split()); s.M=np.load(f"{d}/mosaic.npy")*3.28084; s.n=2**s.Z
    def px(s,lon,lat):
        x=(lon+180)/360*s.n; lr=math.radians(lat); y=(1-math.log(math.tan(lr)+1/math.cos(lr))/math.pi)/2*s.n
        return (x-s.tx0)*256,(y-s.ty0)*256
    def ll(s,px,py):
        x=s.tx0+px/256; y=s.ty0+py/256; return x/s.n*360-180, math.degrees(math.atan(math.sinh(math.pi*(1-2*y/s.n))))
    def el(s,lat,lon):
        x,y=s.px(lon,lat); j,i=x-0.5,y-0.5; i0,j0=int(i),int(j); fi,fj=i-i0,j-j0; M=s.M
        a=M[i0,j0]*(1-fj)+M[i0,j0+1]*fj; b=M[i0+1,j0]*(1-fj)+M[i0+1,j0+1]*fj; return a*(1-fi)+b*fi
DL=DEM(f"{S}/dem"); DE=DEM(f"{S}/dem14b"); DR=DEM(f"{S}/dem13")
# snap Tumbled Rocks (as before)
LAKE=962.3
def westshore(lat):
    x,y=DL.px(-89.745,lat); i=int(y); j=int(x)
    while DL.M[i,j]>LAKE and j<DL.W-1: j+=1
    lon,_=DL.ll(j,y); return lon-25/(111320*math.cos(math.radians(lat)))
tr=[(43.4118,-89.7382)]+[(round(lat,5),round(westshore(lat),5)) for lat in np.arange(43.4128,43.4254,0.0012)]+[(43.4268,-89.7349),(43.4282,-89.7338)]
SEG['tumbled_rocks']['pts']=tr
ALLSEG=dict(SEG); ALLSEG.update(SEG2)
MPU=5.58  # metres per SVG unit, shared by all detail maps
def make_map(dem,ext,mpu,cint,idx_every,water=None,hill_w=1100,segs=(),pois=()):
    Wl,El,Sl,Nl=ext; lat0=(Sl+Nl)/2; kx=111320*math.cos(math.radians(lat0)); ky=110950
    vbw=(El-Wl)*kx/mpu; vbh=(Nl-Sl)*ky/mpu
    proj=lambda lat,lon: ((lon-Wl)*kx/mpu,(Nl-lat)*ky/mpu)
    x0,y0=dem.px(Wl,Nl); x1,y1=dem.px(El,Sl); sub=dem.M[int(y0):int(y1),int(x0):int(x1)]
    cw=(El-Wl)*kx/sub.shape[1]*3.28084; ch=(Nl-Sl)*ky/sub.shape[0]*3.28084
    gy,gx=np.gradient(sub,ch,cw); slope=np.arctan(np.hypot(gx,gy)*1.6); aspect=np.arctan2(-gx,gy)
    az,alt=math.radians(315),math.radians(45)
    hs=np.clip(np.sin(alt)*np.cos(slope)+np.cos(alt)*np.sin(slope)*np.cos(az-aspect),0,1)
    w=min(hill_w,max(300,int(sub.shape[1]*1.6)))
    img=Image.fromarray((np.clip((1-hs)*1.25,0,1)*255).astype(np.uint8),'L').resize((w,max(2,int(w*vbh/vbw))),Image.LANCZOS)
    rgba=Image.new('RGBA',img.size,(0,0,0,0)); rgba.putalpha(img); b=io.BytesIO(); rgba.save(b,'PNG',optimize=True)
    xs=np.linspace(0,vbw,sub.shape[1]); ys=np.linspace(0,vbh,sub.shape[0])
    lo=math.floor(sub.min()/cint)*cint; hi=math.ceil(sub.max()/cint)*cint
    cs=plt.contour(xs,ys,sub,levels=np.arange(lo,hi+cint,cint)); contours=[]
    for lv,segs_ in zip(cs.levels,cs.allsegs):
        for sg in segs_:
            if len(sg)<6: continue
            pts=sg[::2] if len(sg)>40 else sg
            contours.append({"z":int(lv),"d":"M"+" L".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts),"idx":int(lv)%idx_every==0})
    waters=[]
    for (lv,seeds) in (water or []):
        flat=(np.abs(sub-lv)<0.35); mask=np.zeros_like(sub)
        for (la,lo_) in seeds:
            px_,py_=dem.px(lo_,la); si,sj=int(py_-int(y0)),int(px_-int(x0))
            if not(0<=si<sub.shape[0] and 0<=sj<sub.shape[1]) or not flat[si,sj]: continue
            q=deque([(si,sj)]); mask[si,sj]=1
            while q:
                i,j=q.popleft()
                for a,c in ((i+1,j),(i-1,j),(i,j+1),(i,j-1)):
                    if 0<=a<sub.shape[0] and 0<=c<sub.shape[1] and flat[a,c] and not mask[a,c]: mask[a,c]=1; q.append((a,c))
        mp=np.pad(mask,1)
        cl=plt.contour(np.linspace(-vbw/(sub.shape[1]-1),vbw+vbw/(sub.shape[1]-1),sub.shape[1]+2),np.linspace(-vbh/(sub.shape[0]-1),vbh+vbh/(sub.shape[0]-1),sub.shape[0]+2),mp,levels=[0.5])
        for sg in cl.allsegs[0]:
            if len(sg)<12: continue
            waters.append("M"+" L".join(f"{p[0]:.1f},{p[1]:.1f}" for p in sg[::2])+" Z")
    plt.close('all')
    tr={k:{"name":ALLSEG[k]['name'],"conf":ALLSEG[k]['conf'],"d":"M"+" L".join("%.1f,%.1f"%proj(*q) for q in ALLSEG[k]['pts'])} for k in segs}
    ps=[{"name":q[0],"type":q[3],"x":round(proj(q[1],q[2])[0],1),"y":round(proj(q[1],q[2])[1],1),"z":int(dem.el(q[1],q[2])),"side":(q[4] if len(q)>4 else "")} for q in pois]
    return dict(vbw=round(vbw,1),vbh=round(vbh,1),mpu=mpu,hill=base64.b64encode(b.getvalue()).decode(),contours=contours,water=waters,trails=tr,pois=ps),proj
maps={}; projs={}
LAKESEGS=[k for k in SEG]
maps['lake'],projs['lake']=make_map(DL,(-89.7455,-89.6765,43.4030,43.4315),MPU,20,100,water=[(961.9,[(43.42,-89.731)])],segs=LAKESEGS,pois=POI)
maps['parf'],projs['parf']=make_map(DE,(-89.6460,-89.6300,43.4075,43.4215),MPU,20,100,segs=['parfreys'],pois=POI2['parf'])
maps['gib'],projs['gib']=make_map(DE,(-89.6070,-89.5880,43.3400,43.3500),MPU,20,100,segs=['gibraltar'],pois=POI2['gib'])
REG=(-89.765,-89.565,43.335,43.437)
reg_pois=[("Devil's Lake",43.4195,-89.7312,"poi"),("1 · Roznos Meadow",43.4084,-89.6790,"trailhead","l"),("2 · Parfrey's Glen",43.4128,-89.6372,"trailhead"),
          ("Merrimac Ferry",43.3692,-89.6220,"poi"),("3 · Gibraltar Rock",43.3478,-89.5936,"trailhead")]
maps['region'],projs['region']=make_map(DR,REG,22.0,40,200,water=[(773.9,[(43.37,-89.66),(43.36,-89.60),(43.385,-89.60)]),(961.9,[(43.42,-89.731)])],hill_w=1100,segs=[],pois=reg_pois)
pr=projs['region']
maps['region']['drives']=[
  {"d":"M%.1f,%.1f L%.1f,%.1f"%(*pr(43.4084,-89.6790),*pr(43.4092,-89.6360)),"label":"~10 min drive"},
  {"d":"M%.1f,%.1f L%.1f,%.1f L%.1f,%.1f"%(*pr(43.4092,-89.6360),*pr(43.3712,-89.6262),*pr(43.3672,-89.6178)),"label":"~15 min + ferry"},
  {"d":"M%.1f,%.1f L%.1f,%.1f"%(*pr(43.3672,-89.6178),*pr(43.3478,-89.5936)),"label":"~10 min"}]
maps['region']['ferry']="M%.1f,%.1f L%.1f,%.1f"%(*pr(*FERRY[0]),*pr(*FERRY[1]))
# detail-map frames on the region map
for k in ('parf','gib'):
    pass
F,R=False,True
WEST=[("west_bluff",F),("south_shore_w",F),("south_shore_e",F)]
GROT=[("grottos",F),("grottos",R)]
BACKW=[("south_shore_e",R),("south_shore_w",R),("tumbled_rocks",F)]
EAST=[("north_shore",F),("east_bluff",F),("east_bluff_woods",F)]
def route_pts(seq):
    pts=[]
    for k,r in seq:
        p=ALLSEG[k]['pts'][::-1] if r else ALLSEG[k]['pts']
        if pts:
            g=hav(pts[-1],p[0]); assert g<40,(k,r,g); p=p[1:]
        pts+=p
    return pts
def part(mapid,dem,seq):
    pts=route_pts(seq); p=densify(pts,10); dist=[0.0]
    for a,b in zip(p,p[1:]): dist.append(dist[-1]+hav(a,b))
    z=np.array([dem.el(*q) for q in p]); zs=np.convolve(np.pad(z,4,mode='edge'),np.ones(9)/9,'valid')
    gain=loss=0; ref=zs[0]
    for v in zs[1:]:
        if v-ref>=6: gain+=v-ref; ref=v
        elif ref-v>=6: loss+=ref-v; ref=v
    step=max(1,len(p)//300); proj=projs[mapid]
    am=sum(hav(a,b) for k,_ in seq if ALLSEG[k]['conf']=='approx' for a,b in zip(ALLSEG[k]['pts'],ALLSEG[k]['pts'][1:]))
    tm=sum(hav(a,b) for k,_ in seq for a,b in zip(ALLSEG[k]['pts'],ALLSEG[k]['pts'][1:]))
    return dict(map=mapid,d="M"+" L".join("%.1f,%.1f"%proj(*q) for q in pts),mi=dist[-1]/1609.34,gain=gain,
        prof=[[round(dist[i]/1609.34,3),round(float(zs[i]))] for i in range(0,len(p),step)],
        xy=[[round(proj(*p[i])[0],1),round(proj(*p[i])[1],1)] for i in range(0,len(p),step)],
        zmin=float(zs.min()),zmax=float(zs.max()),approx_m=am,total_m=tm)
def route(key,title,day,parts,push,notes,drive_h=0.0,start=10.0):
    mi=sum(p['mi'] for p in parts); gain=sum(p['gain'] for p in parts); mv=mi/3.0+gain/1000.0
    return dict(key=key,title=title,day=day,parts=parts,push=push,notes=notes,mi=round(mi,1),gain=int(round(gain/10)*10),
        hrs_move=round(mv,2),hrs=round(mv*1.25,2),drive_h=drive_h,start=start,zmin=int(min(p['zmin'] for p in parts)),zmax=int(max(p['zmax'] for p in parts)),
        approx_pct=int(round(100*sum(p['approx_m'] for p in parts)/sum(p['total_m'] for p in parts))))
R_={}
R_['std']=route('std',"Both bluffs, figure-eight + Grottos","Mon Oct 19",[part('lake',DL,WEST+GROT+BACKW+EAST)],
  "Steep rock-stair climbing with poles, about twice the 3 Dune Challenge",
  ["Start at the North Shore. West Bluff first, in morning light.","Grottos out-and-back from the South Shore: flat, cool, quiet.","Back north on Tumbled Rocks, then up the East Bluff stone steps.","Reach the East Bluff overlook and Devil's Doorway around 5–5:45 pm for golden hour.","Down the gentle East Bluff Woods Trail, no stone steps. Sunset is about 6:05 pm.","Shorter day: skip the Grottos (saves ~1.5 mi)."])
R_['big']=route('big',"Figure-eight + Grottos + Steinke Basin","Mon Oct 19",[part('lake',DL,WEST+[("grottos",F),("steinke",F),("grottos",R)]+BACKW+EAST)],
  "Climbing plus mileage: the most total work on the lake",
  ["The standard day, plus the Steinke Basin loop through an old glacial lake bed off the end of the Grottos.","The added loop is flat and grassy; often muddy after rain.","Decide at the Grottos: add Steinke only if the West Bluff with poles stayed at 2/10 or less."])
R_['gen']=route('gen',"East Bluff loop + lakeshore + Grottos + Steinke Basin","Mon Oct 19",[part('lake',DL,EAST+[("north_shore",R),("tumbled_rocks",R),("south_shore_w",F),("south_shore_e",F),("grottos",F),("steinke",F),("grottos",R),("south_shore_e",R),("south_shore_w",R),("tumbled_rocks",F)])],
  "Hours on foot; only one bluff climb",
  ["One East Bluff climb (about the 3 Dune Challenge's climbing), down the gentle East Bluff Woods Trail.","Long flat miles: Tumbled Rocks, the Grottos, and the Steinke Basin loop.","Pick this if your hip check or the weather says go easy on stairs."])
tue_parts=[part('lake',DL,[("roznos_meadow",R),("roznos_climb",R),("uplands_east",F)]),part('parf',DE,[("parfreys",F),("parfreys",R)]),part('gib',DE,[("gibraltar",F)])]
R_['tue']=route('tue',"Beyond the bluffs: Roznos Meadow, Parfrey's Glen, Gibraltar Rock","Tue Oct 20",tue_parts,
  "Distance spread over three landscapes; fewer stone stairs than Monday",
  ["Morning check first. 1 · Roznos Meadow + Uplands loop from the Hwy 113 lot: prairie and sand dunes, then stream switchbacks up the bluff.",
   "2 · Parfrey's Glen, 10 min east: sandstone gorge and stream. The last stretch is in the streambed on rough stone; turn around there if tired or wet.",
   "3 · Merrimac Ferry across Lake Wisconsin (free, runs 24/7), then Gibraltar Rock: a short climb to a 200-ft cliff over Lake Wisconsin.",
   "Gibraltar is on the way home: the drive to Chicago starts from there."],drive_h=0.75,start=8.5)
for k,v in R_.items(): v['parts_mi']=[round(p['mi'],2) for p in v['parts']]; v['parts_gain']=[int(p['gain']) for p in v['parts']]
json.dump(dict(maps=maps,routes=R_,overlap=0),open(OUT,'w'))
for k,v in R_.items(): print(k,v['mi'],'mi',v['gain'],'ft',round(v['hrs_move'],1),'h move',round(v['hrs'],1),'h total',v['parts_mi'],v['parts_gain'],'approx',v['approx_pct'])
for k,m in maps.items(): print(k,m['vbw'],m['vbh'],len(m['contours']),'water',len(m['water']),len(m['hill'])//1024,'KB')
