"""Lake Michigan geometry: an approximate shoreline polygon and fetch ray-casting.

The shoreline is hand-digitised from town/headland coordinates (~5-10 km error).
That is adequate for fetch, which matters on a 50-500 km scale. Green Bay is
excluded (closed off along the Door Peninsula -> Garden Peninsula island chain)
and the Straits of Mackinac are closed, since neither adds meaningful fetch to
the open-lake beaches.
"""
import math

# (lat, lon), walking the shore counter-clockwise from Chicago.
LAKE = [
    (41.880, -87.610),  # Chicago Loop
    (41.790, -87.575),  # 57th St
    (41.730, -87.530),  # South Chicago
    (41.680, -87.490),  # Whiting
    (41.615, -87.330),  # Gary
    (41.630, -87.200),  # Ogden Dunes
    (41.670, -87.030),  # Indiana Dunes
    (41.725, -86.900),  # Michigan City
    (41.800, -86.750),  # New Buffalo
    (41.950, -86.620),  # Bridgman
    (42.110, -86.490),  # St. Joseph
    (42.400, -86.285),  # South Haven
    (42.660, -86.215),  # Saugatuck
    (42.770, -86.212),  # Holland
    (43.060, -86.250),  # Grand Haven
    (43.230, -86.345),  # Muskegon
    (43.400, -86.430),  # Whitehall
    (43.650, -86.540),  # Little Sable Point
    (43.780, -86.440),  # Pentwater
    (43.950, -86.450),  # Ludington
    (44.060, -86.510),  # Big Sable Point
    (44.250, -86.340),  # Manistee
    (44.490, -86.240),  # Arcadia
    (44.630, -86.250),  # Frankfort
    (44.690, -86.260),  # Point Betsie
    (44.810, -86.070),  # Empire
    (44.900, -86.040),  # Sleeping Bear Point
    (44.970, -85.930),  # Pyramid Point
    (45.020, -85.760),  # Leland
    (45.210, -85.620),  # Leelanau tip
    (45.000, -85.650),  # Suttons Bay
    (44.770, -85.620),  # Traverse City
    (44.950, -85.400),  # Elk Rapids
    (45.250, -85.300),  # Norwood
    (45.320, -85.260),  # Charlevoix
    (45.380, -84.950),  # Petoskey
    (45.430, -84.990),  # Harbor Springs
    (45.580, -85.120),  # Good Hart
    (45.650, -85.040),  # Cross Village
    (45.750, -84.980),  # Waugoshance Point
    (45.780, -84.730),  # Mackinaw City
    (45.870, -84.730),  # St. Ignace (straits closed)
    (45.950, -85.000),
    (46.050, -85.170),  # Epoufette
    (46.090, -85.450),  # Naubinway
    (45.920, -85.910),  # Seul Choix Point
    (45.950, -86.250),  # Manistique
    (45.900, -86.500),  # Garden Peninsula, east side
    (45.600, -86.620),  # Point Detour (Green Bay closed)
    (45.290, -86.980),  # Door Peninsula tip
    (45.060, -87.120),  # Baileys Harbor
    (44.920, -87.180),  # Whitefish Dunes
    (44.790, -87.310),  # Sturgeon Bay canal
    (44.610, -87.430),  # Algoma
    (44.460, -87.500),  # Kewaunee
    (44.210, -87.510),  # Rawley Point
    (44.090, -87.650),  # Manitowoc
    (43.920, -87.740),  # Cleveland WI
    (43.750, -87.700),  # Sheboygan
    (43.620, -87.730),  # Oostburg
    (43.390, -87.865),  # Port Washington
    (43.200, -87.890),  # Mequon
    (43.040, -87.885),  # Milwaukee
    (42.910, -87.840),  # South Milwaukee
    (42.730, -87.780),  # Racine
    (42.580, -87.810),  # Kenosha
    (42.360, -87.820),  # Waukegan
    (42.250, -87.810),  # Lake Forest
    (42.140, -87.750),  # Glencoe
    (42.050, -87.670),  # Evanston
    (41.960, -87.630),  # Montrose
]

ISLANDS = [
    [(45.55, -85.62), (45.79, -85.62), (45.79, -85.48), (45.55, -85.48)],  # Beaver
    [(45.07, -86.07), (45.17, -86.07), (45.17, -85.95), (45.07, -85.95)],  # N. Manitou
    [(44.99, -86.16), (45.05, -86.16), (45.05, -86.08), (44.99, -86.08)],  # S. Manitou
]

_LAT0 = 43.8
_KX = 111.32 * math.cos(math.radians(_LAT0))
_KY = 110.57


def to_xy(lat, lon):
    """Equirectangular projection to km, good to ~1% across the lake."""
    return lon * _KX, lat * _KY


def to_latlon(x, y):
    return y / _KY, x / _KX


def _rings():
    rings = [LAKE] + ISLANDS
    return [[to_xy(*p) for p in r] for r in rings]


_RINGS = _rings()


def _point_in_ring(x, y, ring):
    inside = False
    n = len(ring)
    for i in range(n):
        x1, y1 = ring[i]
        x2, y2 = ring[(i + 1) % n]
        if (y1 > y) != (y2 > y):
            xi = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
            if x < xi:
                inside = not inside
    return inside


def in_lake(lat, lon):
    x, y = to_xy(lat, lon)
    if not _point_in_ring(x, y, _RINGS[0]):
        return False
    return not any(_point_in_ring(x, y, r) for r in _RINGS[1:])


def offset(lat, lon, bearing_deg, km):
    x, y = to_xy(lat, lon)
    b = math.radians(bearing_deg)
    return to_latlon(x + km * math.sin(b), y + km * math.cos(b))


def ray_fetch_km(lat, lon, bearing_deg):
    """Distance (km) from a point on the water to the nearest shore along a bearing."""
    px, py = to_xy(lat, lon)
    b = math.radians(bearing_deg)
    dx, dy = math.sin(b), math.cos(b)
    best = math.inf
    for ring in _RINGS:
        n = len(ring)
        for i in range(n):
            x1, y1 = ring[i]
            x2, y2 = ring[(i + 1) % n]
            ex, ey = x2 - x1, y2 - y1
            den = dx * ey - dy * ex
            if abs(den) < 1e-12:
                continue
            # Solve P + t*d = A + s*e
            t = ((x1 - px) * ey - (y1 - py) * ex) / den
            s = ((x1 - px) * dy - (y1 - py) * dx) / den
            if t > 1e-9 and 0.0 <= s <= 1.0:
                best = min(best, t)
    return 0.0 if best is math.inf else best


def effective_fetch_km(lat, lon, wind_from_deg, half_width=15, step=3):
    """Mean of radial fetches within +/-half_width of the wind direction (CEM practice)."""
    vals = [ray_fetch_km(lat, lon, wind_from_deg + a)
            for a in range(-half_width, half_width + 1, step)]
    return sum(vals) / len(vals)


def fetch_table(lat, lon, step=5):
    """Effective fetch for every `step` degrees, keyed by integer bearing."""
    return {d: effective_fetch_km(lat, lon, d) for d in range(0, 360, step)}


def lookup_fetch(table, direction_deg):
    """Linear interpolation in a fetch table keyed by evenly spaced bearings."""
    keys = sorted(table)
    step = keys[1] - keys[0]
    d = direction_deg % 360
    lo = int(d // step) * step % 360
    hi = (lo + step) % 360
    w = (d - (d // step) * step) / step
    return table[lo] * (1 - w) + table[hi] * w


def angdiff(a, b):
    """Smallest absolute difference between two bearings, 0..180."""
    d = abs(a - b) % 360
    return 360 - d if d > 180 else d
