import json
W=dict(V=.25,T=.20,R=.15,W=.15,O=.10,P=.10,H=.05)
# name, route, region, base, drive_h, mi, gain_ft, scores V T P R W O H, veto, readiness, flags
C=[
("Wyalusing State Park","Sentinel Ridge + Bluff Trail + Treasure Cave + Sand Cave loop","WI core","Prairie du Chien",3.9,"6–7","~800",dict(V=5,T=4.5,P=4.5,R=4.5,W=3.5,O=3.5,H=5),0,"After a check: steep stairs and the Treasure Cave ladder","Treasure Cave was closed for bats Oct 2024–Apr 2026; reopening not confirmed"),
("Whitewater State Park (MN)","Chimney Rock + Inspiration Point + Coyote Point + river","MN core","Winona / Rochester",5.0,"5–6","~900",dict(V=4.5,T=4.5,P=4.5,R=4.5,W=4,O=3.5,H=2),0,"After a check: steep limestone stairs","At the 5 h limit; one listing shows some trails closed"),
("Perrot State Park","Brady's Bluff + Perrot Ridge + Riverview figure-eight","WI core","Trempealeau / La Crosse",4.6,"5–6","~1,000",dict(V=5,T=4,P=4.5,R=3.5,W=4,O=4,H=3),0,"After a check: 12% grades and stairs up Brady's Bluff",""),
("Backbone State Park (IA)","Backbone Trail over the dolomite fin + river and lake trails","IA core","Dubuque / Strawberry Point",4.2,"4–6","~600",dict(V=3,T=4,P=4,R=5,W=4,O=2.5,H=3),0,"After a check: narrow rocky ridge with ~90 ft drops",""),
("Pikes Peak State Park (IA)","Bridal Veil Falls + bluff trail toward Point Ann","IA core","McGregor / Prairie du Chien",3.9,"4–8","~500",dict(V=4.5,T=3.5,P=3.5,R=3.5,W=3.5,O=3,H=2.5),0,"Yes","Point Ann is ~4 mi each way; turn around early for a shorter day"),
("Mines of Spain (Dubuque)","Horseshoe Bluff + Catfish Creek + Julien Dubuque Monument","IA core","Dubuque",3.3,"~5","~600",dict(V=4,T=4,P=3.5,R=3.5,W=3.5,O=3,H=4),0.1,"Yes; monument trail slick after rain",""),
("Kickapoo Valley Reserve","Hanson Rock / West Ridge overlook + Weister Creek","WI core","Viroqua / La Farge",3.8,"~7","~700",dict(V=4,T=4,P=3,R=4,W=4,O=3.5,H=1.5),0.3,"After a check: creek crossings, poorly marked","Trails close after rain; bring a map"),
("Effigy Mounds National Monument","Fire Point + Twin Views + Hanging Rock (North Unit)","IA core","McGregor / Prairie du Chien",3.9,"~7","600–880",dict(V=4.5,T=3,P=3.5,R=2.5,W=3,O=3,H=5),0,"After a check: last 200 ft to Hanging Rock narrow, rocky, very steep",""),
("Wildcat Mountain State Park","Old Settler's Trail + Hemlock Nature Trail","WI core","Viroqua / Ontario",3.8,"~4","~750",dict(V=4,T=4,P=3.5,R=3.5,W=3.5,O=3,H=1),0,"Yes",""),
("Governor Dodge State Park","Lost Canyon + Stephens Falls + Pine Cliff","WI core","Spring Green / Dodgeville",3.0,"~6","~500",dict(V=3,T=4,P=4,R=4.5,W=4,O=3,H=1.5),0.2,"Yes","Lakes are man-made; Lost Canyon is shared with horses (mud)"),
("Mississippi Palisades State Park (IL)","Sentinel + Twin Sisters + Indian Head (south trails)","IL core","Savanna / Galena",2.8,"~4","~500",dict(V=4,T=3.5,P=3.5,R=4,W=2.5,O=3,H=1),0.2,"Route-specific: south trails run very close to the bluff edge; hazardous wet",""),
("Decorah bluffs and springs","Dunning's Spring + Ice Cave + Palisades Park + Pulpit Rock","IA core","Decorah",4.5,"~5","~500",dict(V=3,T=4,P=4,R=4,W=4.5,O=2,H=1.5),0.2,"Yes","Town-edge parks; Ice Cave needs a flashlight"),
("Ferry Bluff State Natural Area","Bluff-top climb over the Wisconsin River","Baraboo edge","Sauk City / Baraboo",3.0,"~1","~300",dict(V=5,T=2,P=4,R=3,W=4,O=4,H=1),0,"Yes","Closed to all entry in winter for eagles (DNR pages say Nov 15 or Dec 1 – Mar 31). Too short alone; pair it"),
("Great River Bluffs State Park (MN)","King's Bluff + overlook trails","MN core","Winona",5.0,"~4","~300",dict(V=5,T=3,P=3,R=2.5,W=2.5,O=4.5,H=1),0,"Yes","At the 5 h limit; Queen's Bluff closed without a permit"),
("Rush Creek State Natural Area","Old lane to the goat-prairie bluff tops","WI core","Prairie du Chien / Ferryville",4.0,"3–4","~450",dict(V=5,T=3,P=3,R=3,W=2.5,O=5,H=1),0.2,"After a check: unmarked, waist-high brush, steady climb",""),
("Maquoketa Caves State Park (IA)","Caves loop + Natural Bridge + Dancehall Cave","IA core","Dubuque / Maquoketa",3.0,"3–4","~400",dict(V=1.5,T=4,P=5,R=5,W=3,O=1,H=2),0.2,"Yes; caves need a headlamp","Caves close Nov 15 – Apr 1 for bats; one trail section closed"),
("John A. Latsch State Park (MN)","Stairway trail to the bluff top","MN core","Winona",4.8,"~1","~450",dict(V=5,T=2,P=4,R=3.5,W=2.5,O=4,H=1),0,"After a check: long steep stairway","Short; pair it with Perrot or Great River Bluffs"),
("Hixon Forest + Grandad Bluff","George's Point + Hixon View + Grandad Bluff loop","WI core","La Crosse",4.3,"~4","~700",dict(V=4,T=3,P=3,R=3,W=2,O=3,H=1),0.3,"Yes","City noise and crowds at Grandad Bluff"),
("Yellow River State Forest (IA)","Paint Creek loop with Fire Tower / Cedar Point overlooks","IA core","McGregor / Decorah",4.0,"8–13","~1,200",dict(V=3.5,T=3.5,P=2.5,R=2.5,W=3.5,O=3.5,H=1),0,"After a check: long day; stream crossings","Best as a distance-building day"),
("Beaver Creek Valley State Park (MN)","Spring-fed creek valley loops","MN core","Decorah / Caledonia",4.6,"~5","~400",dict(V=2.5,T=3.5,P=3.5,R=3,W=5,O=2.5,H=1),0,"Yes","Not checked in detail this run"),
("Pewit's Nest State Natural Area","Sandstone gorge walk","Baraboo edge","Baraboo",3.2,"~1","~100",dict(V=1,T=2,P=4,R=4.5,W=4,O=1,H=0.5),0,"Yes","Short; an add-on to a Devil's Lake day. Not checked this run"),
("Apple River Canyon State Park (IL)","Canyon trails","IL core","Galena",2.7,"~3","~250",dict(V=2,T=3,P=3,R=3.5,W=4,O=2,H=1),0,"Yes","Not confirmed this run"),
("Natural Bridge State Park","Sandstone arch + rock shelter","Baraboo edge","Baraboo",3.3,"~1","~150",dict(V=1,T=2,P=3,R=4.5,W=0.5,O=1,H=3),0,"Yes","Short; an add-on. Not checked this run"),
("Baxter's Hollow (Nature Conservancy)","Creek gorge in the Baraboo Hills","Baraboo edge","Baraboo",3.1,"3–4","~300",dict(V=1.5,T=3,P=3,R=3.5,W=4,O=3,H=0.5),0,"After a check: rough creekside footing","Not checked this run"),
]
CAL=[("Devil's Lake bluffs (your rating 5)",dict(V=4.5,T=5,P=5,R=4.5,W=4,O=3.5,H=3),0),("Sauk Point → Parfrey's Glen (your rating 2.5)",dict(V=1,T=2,P=1,R=3.5,W=1.5,O=1.5,H=1),0)]
def sc(s,v): return round(sum(W[k]*s[k] for k in W)-v,2)
for n,s,v in CAL: print(n,sc(s,v))
rows=[]
for c in C:
    s=sc(c[7],c[8]); t=1 if s>=4.0 else 2 if s>=3.3 else 3
    rows.append(dict(name=c[0],route=c[1],region=c[2],base=c[3],drive=c[4],mi=c[5],gain=c[6],s=c[7],veto=c[8],score=s,tier=t,ready=c[9],flags=c[10]))
rows.sort(key=lambda r:-r['score'])
for i,r in enumerate(rows,1): print(i,r['tier'],r['score'],r['name'],r['drive'])
json.dump(rows,open('/tmp/claude-0/-home-user-Plugin/f96f31c2-624c-53ad-a7e9-b2235cc8484d/scratchpad/driftless.json','w'))
