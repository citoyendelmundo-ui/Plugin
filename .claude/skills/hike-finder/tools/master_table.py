import json, sys
rows=json.load(open(sys.argv[1])); drift={r[1].split(':')[0].strip():r for r in json.load(open(sys.argv[2]))}
X={
"Sleeping Bear Dunes NL (MI)":("~7.7 mi · ~900 ft","~5h (sand adds ~15%)","Yes; 2+ days with Alligator Hill, Bay View, Lasso Loop","[NPS](https://www.nps.gov/slbe/)"),
"Nordhouse Dunes Wilderness (MI)":("~9 mi · ~500 ft","~5h on sand","Yes; extended loop ~14 mi; add Ludington SP for day 2","[USFS](https://www.fs.usda.gov/r09/huron-manistee/recreation/nordhouse-dunes-wilderness-area-0)"),
"Ludington State Park (MI)":("~10 mi · ~400 ft","~5h on sand","Yes (21 mi of marked trail)","[MI DNR](https://www.michigan.gov/ludington)"),
"Manistee River Trail + NCT loop (MI)":("~10.5 mi · ~1,000 ft","5h40","Yes; full 20-mi loop = 2 days","[USFS](https://www.fs.usda.gov/r09/huron-manistee/recreation/trails/manistee-river-trail)"),
"Arcadia Dunes / Old Baldy (MI)":("~3.2 mi · ~350 ft","1h45","No: pair with Nordhouse or Sleeping Bear","[Grand Traverse Regional Land Conservancy](https://www.gtrlc.org/) (preserve page not confirmed)"),
"Saugatuck Dunes State Park (MI)":("~8 mi · ~700 ft","4h15","Close: all four trails (~12–13 mi) ≈ 6h","[MI DNR](https://www.michigan.gov/recsearch/parks/saugatuck)"),
"Muskegon State Park (MI)":("~8 mi · ~700 ft","4h15","Close: ~12 mi of trail","[MI DNR](https://www.michigan.gov/muskegon) (URL not confirmed)"),
"P.J. Hoffmaster State Park (MI)":("~7 mi · ~500 ft","3h30","No (~10 mi in park): pair with Muskegon","[MI DNR](https://www.michigan.gov/hoffmaster)"),
"Warren Dunes State Park (MI)":("~6 mi · ~700 ft","3h25","No (~6 mi in park)","[MI DNR](https://www.michigan.gov/warrendunes)"),
"Yankee Springs Recreation Area (MI)":("~9 mi · ~600 ft","4h30","Close (16+ mi, few loops)","[MI DNR](https://www.michigan.gov/YankeeSprings)"),
"Indiana Dunes SP + NP (IN)":("~11 mi · ~900 ft","5h45","Yes (50+ mi across both parks)","[IN DNR](https://www.in.gov/dnr/state-parks/parks-lakes/indiana-dunes-state-park/) · [NPS](https://www.nps.gov/indu/)"),
"Turkey Run State Park (IN)":("~10 mi · ~800 ft","5h10 (ladders, creekbed: slow)","Yes (~14 mi); Shades next door for day 2","[IN DNR](https://www.in.gov/dnr/state-parks/parks-lakes/turkey-run-state-park/index)"),
"Shades State Park (IN)":("~7 mi · ~800 ft","3h55","Close: pair with Turkey Run","[IN DNR](https://www.in.gov/dnr/state-parks/parks-lakes/shades-state-park/)"),
"Brown County State Park (IN)":("~10 mi · ~1,100 ft","5h30","Yes","[IN DNR](https://www.in.gov/dnr/state-parks/parks-lakes/brown-county-state-park/index)"),
"Charles C. Deam Wilderness (IN)":("~11 mi · ~1,000 ft","5h50","Yes (36 mi of trail)","[USFS](https://www.fs.usda.gov/r09/hoosier/recreation/charles-c-deam-wilderness)"),
"Knobstone Trail (IN)":("~10 mi · ~2,000 ft","6h40","Yes (48–58 mi; a Deam Lake segment closed)","Indiana DNR (Knobstone page URL not confirmed)"),
"Clifty Falls State Park (IN)":("~9 mi · ~900 ft","4h55 (creekbed: slow)","Yes","[IN DNR](https://www.in.gov/dnr/state-parks/parks-lakes/clifty-falls-state-park/)"),
"McCormick's Creek State Park (IN)":("~5 mi · ~400 ft","2h35","No: pair with Brown County","[IN DNR](https://www.in.gov/dnr/state-parks/parks-lakes/mccormicks-creek-state-park/)"),
"Pokagon State Park (IN)":("~8 mi · ~400 ft","3h50","Close","[IN DNR](https://www.in.gov/dnr/state-parks/parks-lakes/pokagon-state-parktrine-state-recreation-area/)"),
"Starved Rock + Matthiessen (IL)":("~10 mi · ~900 ft","5h20","Yes (13+ mi + 5 mi); LaSalle/Tonti closed","[IL DNR Starved Rock](https://dnr.illinois.gov/parks/park.starvedrock) · [Matthiessen](https://dnr.illinois.gov/parks/activity/park.matthiessen.html)"),
"Castle Rock SP + Lowden-Miller SF (IL)":("~10 mi · ~600 ft","4h55","Yes (6–7 mi + ~22 mi)","[IL DNR Lowden-Miller](https://dnr.illinois.gov/parks/activity/park.lowdenmiller.html) (Castle Rock page not confirmed)"),
"Kankakee River State Park (IL)":("~8 mi · ~300 ft","3h45","Close","IL DNR (URL not confirmed)"),
"White Pines Forest State Park (IL)":("~4 mi · ~200 ft","1h55","No: an add-on to Castle Rock","IL DNR (URL not confirmed)"),
"Garden of the Gods + Rim Rock (IL, Shawnee)":("~10 mi · ~1,200 ft","5h40","Yes; Rim Rock + Pounds Hollow + High Knob fill day 2","[USFS Garden of the Gods](https://fs.usda.gov/r09/shawnee/recreation/garden-gods-recreation-area) · [Rim Rock](https://www.fs.usda.gov/r09/shawnee/recreation/trails/rim-rock-national-recreation-trail)"),
"Bell Smith Springs + Jackson Falls (IL, Shawnee)":("~8 mi · ~700 ft","4h15","Close; Jackson Falls bluff line adds ~1h","[USFS Bell Smith](https://fs.usda.gov/r09/shawnee/recreation/bell-smith-springs-recreation-area) · [Jackson Falls](https://www.fs.usda.gov/r09/shawnee/recreation/jackson-falls)"),
"Little Grand Canyon (IL, Shawnee)":("~3.6 mi · ~350 ft","1h55","No: pair with Giant City","[USFS Shawnee](https://www.fs.usda.gov/r09/shawnee/maps-guides/recreation-opportunity-guides)"),
"Ferne Clyffe State Park (IL)":("~7 mi · ~600 ft","3h40","Close: pair with Giant City","IL DNR (URL not confirmed)"),
"Giant City State Park (IL)":("~12 mi · ~1,000 ft","6h15","Yes (Red Cedar loop; closed in shotgun deer season)","[IL DNR Red Cedar trail PDF](https://dnr.illinois.gov/content/dam/soi/en/web/dnr/parks/documents/giantcityredcedartrail.pdf)"),
}
REG={"Driftless":"Driftless","MI":"Michigan","IN":"Indiana","IL":"Illinois","Shawnee":"Shawnee (stretch)"}
def dstr(h):
    hh=int(h); m=round((h-hh)*60/15)*15
    if m==60: hh+=1;m=0
    return f"{hh}h{m:02d}" if m else f"{hh}h"
out=["| # | Hike | Region | Tier | Score (features · capacity) | Drive | Distance · climb | Hiking time | 5-hour day? | Base town | Official site |","| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |"]
for i,r in enumerate(rows,1):
    if r['region']=='Driftless':
        d=drift[r['name']]; hike=d[1]; drive,dist,time,five,base,link=d[4],d[5],d[6],d[7],d[8],d[9]
    else:
        dist,time,five,link=X[r['name']]; hike=f"{r['name']}: {r['route']}"; drive=dstr(r['drive']); base=r['base']
    t={"S":"Stretch"}.get(r['tier'],str(r['tier']))
    out.append(f"| {i} | {hike} | {REG[r['region']]} | {t} | **{r['score']:.2f}** ({r['feat']:.2f} · {r['cap']:g}) | {drive} | {dist} | {time} | {five} | {base} | {link} |")
open(sys.argv[3],'w').write('\n'.join(out)+'\n')
print(len(out))
