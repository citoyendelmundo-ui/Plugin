"""Master ranking: Driftless + Michigan + Indiana + rest of Illinois + Shawnee (stretch).

score = 0.85 * feature score (driftless_scoring weights, minus vetoes) + 0.15 * capacity
capacity (0-5) = quality hiking hours the place supports: 5 = two or more full days,
4 = one long day plus extra, 3 = fills one 5 h day, 2 = 3-4 h, 1 = ~2 h, 0.5 = under 1 h.
Long dull woods earn no capacity.
"""
import json, sys
from driftless_scoring import C as DRIFT, W, sc

WF, WC = .85, .15
def master(feat, cap): return round(WF*feat + WC*cap, 2)
def hours(mi, gain): return (mi/3 + gain/1000) * 1.25

# Driftless capacity (route as listed + rest of park)
DCAP = {"Wyalusing State Park":4,"Whitewater State Park (MN)":4,"Perrot State Park":4,
 "Backbone State Park (IA)":3,"Pikes Peak State Park (IA)":3.5,"Mines of Spain (Dubuque)":3,
 "Kickapoo Valley Reserve":4,"Effigy Mounds National Monument":3.5,"Wildcat Mountain State Park":3,
 "Governor Dodge State Park":4,"Mississippi Palisades State Park (IL)":3,"Decorah bluffs and springs":3,
 "Ferry Bluff State Natural Area":0.5,"Great River Bluffs State Park (MN)":2,"Rush Creek State Natural Area":2,
 "Maquoketa Caves State Park (IA)":1.5,"John A. Latsch State Park (MN)":1,"Hixon Forest + Grandad Bluff":3,
 "Yellow River State Forest (IA)":5,"Beaver Creek Valley State Park (MN)":2.5,
 "Pewit's Nest State Natural Area":0.5,"Apple River Canyon State Park (IL)":1.5,
 "Natural Bridge State Park":0.5,"Baxter's Hollow (Nature Conservancy)":2}

# name, route, region, base, drive_h, mi, gain, features, veto, capacity, stretch
NEW = [
("Sleeping Bear Dunes NL (MI)","Dunes Hiking Trail + Pyramid Point + Empire Bluff","MI","Empire / Glen Arbor",5.0,7.7,900,dict(V=5,T=4.5,P=4.5,R=1.5,W=5,O=4.5,H=2.5),0.1,5,False),
("Nordhouse Dunes Wilderness (MI)","Nurnberg trailhead → interior dunes → beach return","MI","Ludington / Manistee",4.25,9,500,dict(V=4,T=4,P=3.5,R=1,W=5,O=5,H=1),0,5,False),
("Ludington State Park (MI)","Skyline + Ridge + Island Lake + Lighthouse beach","MI","Ludington",4.0,10,400,dict(V=3.5,T=4,P=3.5,R=0.5,W=5,O=3.5,H=2),0.1,4,False),
("Manistee River Trail + NCT loop (MI)","West half of the 20-mi loop, suspension bridge, bluff camps","MI","Wellston / Mesick",4.75,10.5,1000,dict(V=3.5,T=3.5,P=3,R=1,W=4,O=4,H=1),0,5,False),
("Arcadia Dunes / Old Baldy (MI)","Old Baldy loop + Arcadia Marsh (pair with Nordhouse or Sleeping Bear)","MI","Frankfort / Arcadia",4.75,3.2,350,dict(V=4.5,T=3,P=4,R=1,W=4,O=4,H=1),0,2,False),
("Saugatuck Dunes State Park (MI)","South Trail + North Trail + beach","MI","Saugatuck",2.25,8,700,dict(V=3,T=3,P=3,R=0.5,W=4.5,O=4,H=0.5),0,3,False),
("Muskegon State Park (MI)","Lost Lake loops + Dune Ridge + Snowshoe trails + beach","MI","Muskegon",3.0,8,700,dict(V=3,T=3.5,P=3,R=0.5,W=4.5,O=3,H=1),0.1,3,False),
("P.J. Hoffmaster State Park (MI)","Dune Overlook stairs + Homestead + Walk-a-Mile + beach","MI","Grand Haven / Muskegon",2.75,7,500,dict(V=3.5,T=3,P=3.5,R=0.5,W=4.5,O=3,H=1),0.1,2.5,False),
("Warren Dunes State Park (MI)","Tower Hill + Great Warren Dune + beach loop","MI","Sawyer / Bridgman",1.67,6,700,dict(V=3.5,T=3,P=3.5,R=0.5,W=4.5,O=2.5,H=0.5),0.2,2,False),
("Yankee Springs Recreation Area (MI)","Hall Lake + Graves Hill + Devil's Soup Bowl + NCT","MI","Hastings / Middleville",2.75,9,600,dict(V=2.5,T=3,P=2.5,R=1,W=4,O=3,H=0.5),0.1,3,False),
("Indiana Dunes SP + NP (IN)","Trails 9 + 8 (3 Dune Challenge) + 10 + West Beach / Cowles Bog day","IN","Chesterton",1.17,11,900,dict(V=3.5,T=3,P=3.5,R=0.5,W=5,O=3,H=1),0.2,4,False),
("Turkey Run State Park (IN)","Trails 3 (ladders) + 2 + 5 + 9 + 10 via the suspension bridge","IN","Marshall / Crawfordsville",2.75,10,800,dict(V=2.5,T=5,P=5,R=5,W=4.5,O=2,H=2.5),0.3,3,False),
("Shades State Park (IN)","Six Ravine route + Devil's Punchbowl + Inspiration Point","IN","Waveland / Crawfordsville",2.75,7,800,dict(V=3,T=4.5,P=4.5,R=4.5,W=4,O=3,H=1),0.2,3,False),
("Brown County State Park (IN)","Trails 8 + 10 (fire tower) + 9/11 to Ogle Lake","IN","Nashville IN",4.0,10,1100,dict(V=3.5,T=3,P=3,R=1.5,W=2,O=3.5,H=2),0.2,4,False),
("Charles C. Deam Wilderness (IN)","Peninsula Trail to Lake Monroe shore + Grubb Ridge","IN","Bloomington",4.25,11,1000,dict(V=3,T=3,P=2.5,R=1,W=3.5,O=5,H=1),0.2,5,False),
("Knobstone Trail (IN)","Delaney Park → Elk Creek section (south half is the steep bit)","IN","Salem / Scottsburg",4.75,10,2000,dict(V=4,T=3,P=3,R=1.5,W=2,O=4.5,H=0.5),0.1,5,False),
("Clifty Falls State Park (IN)","Trails 2 (creekbed) + 3 + 4 + 5 + 8 past four falls","IN","Madison IN",5.0,9,900,dict(V=3,T=4.5,P=4.5,R=4.5,W=5,O=2.5,H=1.5),0.1,3,False),
("McCormick's Creek State Park (IN)","Trail 3 canyon + falls + Trails 5/7","IN","Spencer / Bloomington",3.75,5,400,dict(V=2,T=3.5,P=3.5,R=3.5,W=4,O=2,H=2),0.1,2,False),
("Pokagon State Park (IN)","8-mile connector loop over Hell's Point + Potawatomi preserve","IN","Angola",2.75,8,400,dict(V=2.5,T=3,P=2.5,R=0.5,W=4,O=3,H=2),0.1,3,False),
("Starved Rock + Matthiessen (IL)","East canyons (French→Ottawa/Kaskaskia) + Matthiessen Dells","IL","Utica / Oglesby",1.75,10,900,dict(V=3.5,T=4,P=4,R=4,W=4,O=2,H=2.5),0.4,4,False),
("Castle Rock SP + Lowden-Miller SF (IL)","Castle Rock bluff + Lowden-Miller river-bluff loops","IL","Oregon IL",2.0,10,600,dict(V=3,T=3,P=2.5,R=3,W=3.5,O=3,H=1),0.1,3,False),
("Kankakee River State Park (IL)","Rock Creek canyon + river bluff trail","IL","Bourbonnais",1.25,8,300,dict(V=2.5,T=3,P=3,R=2.5,W=4.5,O=2,H=1),0.2,3,False),
("White Pines Forest State Park (IL)","Pine stands + creek fords + CCC lodge","IL","Mount Morris",2.0,4,200,dict(V=1.5,T=2.5,P=2,R=1.5,W=2.5,O=2,H=2),0,1,False),
# Shawnee stretch class: beyond the approved 5 h envelope
("Garden of the Gods + Rim Rock (IL, Shawnee)","Observation Trail + Indian Point + River to River section; Rim Rock/Pounds Hollow second day","Shawnee","Harrisburg / Elizabethtown",5.75,10,1200,dict(V=5,T=4.5,P=4.5,R=5,W=2.5,O=4.5,H=2.5),0,5,True),
("Bell Smith Springs + Jackson Falls (IL, Shawnee)","Natural Bridge + Mill Branch + Sentry Bluff; Jackson Falls bluff line","Shawnee","Eddyville / Harrisburg",5.75,8,700,dict(V=3,T=4.5,P=4.5,R=5,W=5,O=4,H=1),0.1,4,True),
("Little Grand Canyon (IL, Shawnee)","Rim + canyon-floor loop","Shawnee","Murphysboro / Carbondale",5.75,3.6,350,dict(V=4,T=4.5,P=4,R=4.5,W=3.5,O=3.5,H=1),0,2,True),
("Giant City State Park (IL)","Red Cedar loop + Giant City Nature Trail + Stone Fort","Shawnee","Makanda / Carbondale",5.5,12,1000,dict(V=2.5,T=3.5,P=3,R=4.5,W=2.5,O=3,H=2.5),0.1,4,True),
("Ferne Clyffe State Park (IL)","Big Rocky Hollow + Round Bluff + Happy Hollow","Shawnee","Goreville",5.5,7,600,dict(V=2.5,T=4,P=4,R=4.5,W=3.5,O=3,H=1),0,3,True),
]

CAL = [("Devil's Lake bluffs, Oct 19 (rated 5)", 4.40, 5, 5.0),
       ("Indiana Dunes SP push, Sep 30 (rated 3.75)", sc(dict(V=3.5,T=3,P=3.5,R=0.5,W=5,O=3,H=1),0.2), 3, 3.75),
       ("Sauk Point → Parfrey's Glen, Oct 20 (rated 2.5)", 1.70, 2, 2.5)]

def tier(s): return 1 if s >= 4.0 else 2 if s >= 3.3 else 3

def main(out):
    for n, f, c, r in CAL:
        m = master(f, c); print(f"{n}: features {f:.2f} cap {c} -> {m:.2f}; predicted {0.9+0.92*m:.2f} vs {r}")
    rows = []
    for c in DRIFT:
        f = sc(c[7], c[8]); cap = DCAP[c[0]]
        rows.append(dict(name=c[0], route=c[1], region="Driftless", base=c[3], drive=c[4],
                         feat=f, cap=cap, score=master(f, cap), stretch=False))
    for n, rt, reg, base, d, mi, g, s, v, cap, st in NEW:
        f = sc(s, v)
        rows.append(dict(name=n, route=rt, region=reg, base=base, drive=d, mi=mi, gain=g,
                         hours=round(hours(mi, g), 2), feat=f, cap=cap, score=master(f, cap), stretch=st))
    for r in rows: r["tier"] = "S" if r["stretch"] else tier(r["score"])
    rows.sort(key=lambda r: (r["stretch"], -r["score"]))
    for i, r in enumerate(rows, 1):
        print(i, r["tier"], r["score"], r["feat"], r["cap"], r["region"], r["name"], r.get("hours", ""))
    json.dump(rows, open(out, "w"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "master.json")
