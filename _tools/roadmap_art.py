"""Draw the evolving Open Moon base, one SVG per roadmap stage.

Run from the repo root:  python3 _tools/roadmap_art.py
Reads _data/roadmap.yml and writes assets/roadmap/year-NN.svg.
Every element appears at a stage and stays for all later stages; elements that
are new at a stage get an amber label so the viewer sees what changed.
"""
import pathlib, yaml, math, random

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "roadmap"
W, H = 1600, 600
CY, AM, INK, DIM = "#38d4f0", "#ffb020", "#d6e2ec", "#7890a3"

def ground_y(x):
    """Height of the foreground plain at x (gentle undulation)."""
    return 470 + 8 * math.sin(x / 140) + 5 * math.sin(x / 47)

# ---------- element painters (each returns svg text) ----------
def tower(x, h, w=16):
    gy = ground_y(x) - 112  # towers stand on the ridge
    return (f'<line x1="{x}" y1="{gy}" x2="{x}" y2="{gy-h}" stroke="{CY}" stroke-width="2"/>'
            f'<rect x="{x-w/2}" y="{gy-h}" width="{w}" height="{h*0.62}" fill="rgba(56,212,240,.18)" stroke="{CY}" stroke-width="1.5"/>'
            + "".join(f'<line x1="{x-w/2}" y1="{gy-h+i*h*0.62/6}" x2="{x+w/2}" y2="{gy-h+i*h*0.62/6}" stroke="{CY}" stroke-width=".6" opacity=".6"/>' for i in range(1, 6))
            + f'<path d="M{x-10} {gy} L{x+10} {gy} L{x+6} {gy-8} L{x-6} {gy-8}Z" fill="#0a1015" stroke="{CY}" stroke-width="1.5"/>')

def small_lander(x, y, s=1.0):
    return (f'<g transform="translate({x},{y}) scale({s})"><path d="M-14 -26 h28 v14 h-28z" fill="#0a1015" stroke="{CY}" stroke-width="1.5"/>'
            f'<path d="M-14 -12 L-24 0 M14 -12 L24 0 M-6 -12 L-10 0 M6 -12 L10 0" stroke="{CY}" stroke-width="1.5"/>'
            f'<rect x="-10" y="-34" width="20" height="8" fill="rgba(56,212,240,.25)" stroke="{CY}" stroke-width="1"/></g>')

def rover(x, y, s=1.0, mast=False):
    m = f'<line x1="6" y1="-12" x2="6" y2="-24" stroke="{CY}" stroke-width="1.5"/><rect x="2" y="-28" width="8" height="4" fill="{CY}"/>' if mast else ""
    return (f'<g transform="translate({x},{y}) scale({s})"><rect x="-14" y="-12" width="28" height="8" rx="2" fill="#0a1015" stroke="{CY}" stroke-width="1.5"/>'
            f'<circle cx="-9" cy="-2" r="4" fill="#0a1015" stroke="{CY}" stroke-width="1.5"/><circle cx="9" cy="-2" r="4" fill="#0a1015" stroke="{CY}" stroke-width="1.5"/>{m}</g>')

def excavator(x, y):
    return rover(x, y, 1.1) + f'<circle cx="{x+20}" cy="{y-4}" r="6" fill="none" stroke="{CY}" stroke-width="1.5"/><circle cx="{x-20}" cy="{y-4}" r="6" fill="none" stroke="{CY}" stroke-width="1.5"/>'

def pad(x, y, rx, hard=True):
    fill = "rgba(56,212,240,.10)" if hard else "rgba(56,212,240,.04)"
    s = f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{rx*0.16}" fill="{fill}" stroke="{CY}" stroke-width="1.5"/>'
    if hard:
        s += f'<ellipse cx="{x}" cy="{y}" rx="{rx*0.6}" ry="{rx*0.1}" fill="none" stroke="{CY}" stroke-width="1" opacity=".6"/>'
        s += f'<path d="M{x+rx+6} {y+2} Q{x+rx+24} {y-18} {x+rx+42} {y+2}Z" fill="rgba(56,212,240,.08)" stroke="{CY}" stroke-width="1.2"/>'
    return s

def reactor(x):
    y = ground_y(x)
    return (f'<path d="M{x-60} {y} Q{x-30} {y-40} {x} {y-34} T{x+60} {y}Z" fill="#0c141b" stroke="{CY}" stroke-width="1.2"/>'
            f'<rect x="{x-8}" y="{y-92}" width="16" height="42" fill="#0a1015" stroke="{CY}" stroke-width="1.5"/>'
            f'<path d="M{x-8} {y-86} L{x-44} {y-100} L{x-44} {y-62} L{x-8} {y-58}Z M{x+8} {y-86} L{x+44} {y-100} L{x+44} {y-62} L{x+8} {y-58}Z" fill="rgba(255,176,32,.12)" stroke="{AM}" stroke-width="1.3"/>')

def comms_mast(x, h=90):
    y = ground_y(x)
    return (f'<line x1="{x}" y1="{y}" x2="{x}" y2="{y-h}" stroke="{CY}" stroke-width="2"/>'
            f'<path d="M{x-14} {y-h+6} Q{x} {y-h-14} {x+14} {y-h+6}" fill="none" stroke="{CY}" stroke-width="2"/>'
            f'<line x1="{x}" y1="{y-h}" x2="{x+8} " y2="{y-h-12}" stroke="{CY}" stroke-width="1.5"/>')

def relay_sat(x, y):
    return (f'<rect x="{x-6}" y="{y-6}" width="12" height="12" fill="#0a1015" stroke="{CY}" stroke-width="1.5"/>'
            f'<rect x="{x-34}" y="{y-4}" width="24" height="8" fill="rgba(56,212,240,.25)" stroke="{CY}" stroke-width="1"/>'
            f'<rect x="{x+10}" y="{y-4}" width="24" height="8" fill="rgba(56,212,240,.25)" stroke="{CY}" stroke-width="1"/>')

def habitat(x, y, buried=False):
    if buried:
        return (f'<path d="M{x-62} {y} Q{x} {y-62} {x+62} {y}Z" fill="#101a22" stroke="{CY}" stroke-width="1.5"/>'
                f'<rect x="{x-8}" y="{y-14}" width="16" height="14" fill="{AM}" opacity=".85"/>')
    return (f'<rect x="{x-44}" y="{y-34}" width="88" height="26" rx="12" fill="#0a1015" stroke="{CY}" stroke-width="1.8"/>'
            f'<circle cx="{x-26}" cy="{y-4}" r="6" fill="#0a1015" stroke="{CY}" stroke-width="1.5"/><circle cx="{x+26}" cy="{y-4}" r="6" fill="#0a1015" stroke="{CY}" stroke-width="1.5"/>'
            f'<rect x="{x-6}" y="{y-28}" width="12" height="8" fill="{AM}" opacity=".7"/>')

def plant(x, y):
    return (f'<rect x="{x-30}" y="{y-30}" width="40" height="30" fill="#0a1015" stroke="{CY}" stroke-width="1.5"/>'
            f'<rect x="{x+14}" y="{y-40}" width="14" height="40" rx="7" fill="rgba(56,212,240,.12)" stroke="{CY}" stroke-width="1.5"/>'
            f'<line x1="{x-22}" y1="{y-30}" x2="{x-22}" y2="{y-44}" stroke="{CY}" stroke-width="1.5"/><circle cx="{x-22}" cy="{y-46}" r="2" fill="{AM}"/>')

def tanks(x, y, n=3):
    return "".join(f'<rect x="{x+i*22}" y="{y-34}" width="16" height="34" rx="8" fill="rgba(56,212,240,.12)" stroke="{CY}" stroke-width="1.5"/>' for i in range(n))

def crew_lander(x, y):
    return (f'<path d="M{x-12} {y-10} L{x-12} {y-150} Q{x} {y-176} {x+12} {y-150} L{x+12} {y-10}Z" fill="#0a1015" stroke="{CY}" stroke-width="1.8"/>'
            f'<rect x="{x-8}" y="{y-128}" width="16" height="8" fill="{AM}" opacity=".7"/>'
            f'<path d="M{x-12} {y-10} L{x-22} {y} M{x+12} {y-10} L{x+22} {y}" stroke="{CY}" stroke-width="1.8"/>')

def person(x, y):
    return (f'<circle cx="{x}" cy="{y-17}" r="3.2" fill="none" stroke="{INK}" stroke-width="1.3"/>'
            f'<path d="M{x} {y-13} L{x} {y-5} M{x-4} {y-10} L{x+4} {y-10} M{x} {y-5} L{x-3} {y} M{x} {y-5} L{x+3} {y}" stroke="{INK}" stroke-width="1.3"/>')

def greenhouse(x, y):
    return (f'<path d="M{x-48} {y} Q{x} {y-44} {x+48} {y}Z" fill="#101a22" stroke="{CY}" stroke-width="1.5"/>'
            f'<path d="M{x-26} {y-12} L{x+26} {y-12}" stroke="#7cf29a" stroke-width="3" opacity=".8"/>')

def factory(x, y):
    return (f'<rect x="{x-46}" y="{y-40}" width="70" height="40" fill="#0a1015" stroke="{CY}" stroke-width="1.5"/>'
            f'<path d="M{x-46} {y-40} L{x-30} {y-54} L{x-14} {y-40} L{x+2} {y-54} L{x+18} {y-40}" fill="none" stroke="{CY}" stroke-width="1.5"/>'
            f'<rect x="{x+26}" y="{y-58}" width="8" height="58" fill="#0a1015" stroke="{CY}" stroke-width="1.5"/>'
            f'<rect x="{x-38}" y="{y-26}" width="20" height="8" fill="{AM}" opacity=".7"/>')

def dome(x, y, r):
    return (f'<path d="M{x-r} {y} A{r} {r*0.8} 0 0 1 {x+r} {y}Z" fill="#101a22" stroke="{CY}" stroke-width="1.5"/>'
            f'<path d="M{x-r*0.6} {y} A{r*0.6} {r*0.5} 0 0 1 {x+r*0.6} {y}" fill="none" stroke="{CY}" stroke-width=".8" opacity=".5"/>'
            f'<circle cx="{x}" cy="{y-r*0.35}" r="2.5" fill="{AM}"/>')

def label(x, y, text, tx, ty):
    return (f'<line x1="{x}" y1="{y}" x2="{tx}" y2="{ty+4}" stroke="{AM}" stroke-width="1" opacity=".9"/>'
            f'<text x="{tx}" y="{ty}" fill="{AM}" font-family="Share Tech Mono, monospace" font-size="15" text-anchor="middle">{text}</text>')

# ---------- scene elements: (first stage index, painter, label or None, label anchor) ----------
def elements():
    E = []
    add = lambda st, svg, lab=None: E.append((st, svg, lab))
    g = ground_y
    # stage indices refer to positions in roadmap.yml (0..13)
    add(2, small_lander(1210, g(1210)) + small_lander(1330, g(1330)), ("PROSPECTOR LANDERS", 1270, g(1270)-40, 1270, 200))
    add(2, rover(1395, 545, 0.9, True) + rover(1450, 560, 0.9, True), ("PROSPECTORS IN CRATER", 1420, 535, 1420, 250))
    add(2, rover(980, g(980), 1.2) + rover(1050, g(1050), 1.2), ("LUNAR TERRAIN VEHICLES", 1015, g(1015)-14, 1015, 300))
    add(3, tower(330, 70), ("FIRST 10 kW SOLAR TOWER", 330, g(330)-180, 330, 120))
    add(3, comms_mast(770, 90), ("COMMS MAST + LTE", 770, g(770)-90, 770, 250))
    add(3, excavator(880, g(880)) + excavator(940, g(940)), ("EXCAVATORS", 910, g(910)-14, 910, 340))
    add(4, tower(410, 70) + tower(520, 150, 22) + tower(610, 150, 22), ("120 kW OF SOLAR TOWERS", 560, g(560)-260, 470, 70))
    add(4, relay_sat(1180, 70) + relay_sat(1460, 110), ("RELAY SATELLITES", 1320, 90, 1320, 48))
    add(4, pad(1010, 560, 120), ("HARDENED PAD", 1010, 560, 1010, 450))
    add(4, comms_mast(1180, 70), None)
    add(5, reactor(110) + f'<path d="M150 {g(150)} C300 {g(300)+14} 500 {g(500)+14} 700 {g(700)+6}" fill="none" stroke="{AM}" stroke-width="1.6" stroke-dasharray="6 4"/>', ("40 kWe FISSION REACTOR", 110, g(110)-100, 160, 160))
    add(5, pad(1250, 585, 100) + tanks(560, g(560)+10, 2), ("PAD 2 + STORAGE", 1250, 585, 1250, 470))
    add(6, plant(1120, g(1120)) + tanks(1150, g(1150), 3), ("OXYGEN + WATER PLANTS", 1135, g(1135)-40, 1135, 160))
    add(6, excavator(1505, 575), ("ICE MINING", 1505, 565, 1540, 300))
    add(6, habitat(650, g(650)), ("FIRST HABITAT", 650, g(650)-34, 650, 220))
    add(7, crew_lander(1010, 550), ("CREW LANDER", 1010, 400, 900, 120))
    add(7, person(620, g(620)) + person(690, g(690)), ("FIRST CREW", 655, g(655)-20, 620, 300))
    add(8, habitat(470, g(470)+4, True) + habitat(560, g(560)+6, True), ("BURIED HABITATS", 515, g(515)-50, 560, 230))
    add(8, person(520, g(520)+8) + person(590, g(590)+8), None)
    add(9, greenhouse(240, g(240)+4) + greenhouse(320, g(320)+6), ("GREENHOUSES", 280, g(280)-30, 250, 190))
    add(10, greenhouse(160, g(160)+8) + greenhouse(400, g(400)+10), ("STAPLE CROPS", 280, g(280)-10, 330, 170))
    add(11, tanks(1300, g(1300), 5) + reactor(1530) , ("PROPELLANT DEPOT + MORE POWER", 1350, g(1350)-34, 1330, 250))
    add(11, tower(700, 150, 22) + tower(790, 150, 22), None)
    add(12, factory(860, g(860)), ("FABRICATION SHOP", 850, g(850)-50, 880, 250))
    add(12, dome(760, g(760)+10, 34), ("PRINTED REGOLITH SHELTER", 760, g(760)-20, 700, 300))
    add(13, dome(140, g(140)+12, 40) + dome(360, g(360)+14, 46) + dome(450, g(450)+16, 30) + dome(1380, g(1380)+12, 38) + dome(1460, g(1460)+12, 30), ("COLONY: 50–100 PEOPLE", 360, g(360)-30, 620, 200))
    add(13, "".join(person(x, g(x)+12) for x in (300, 330, 420, 700, 730, 1080, 1110)), None)
    return E

def scene(stage_idx, title):
    rnd = random.Random(7)
    stars = "".join(f'<circle cx="{rnd.randint(0,W)}" cy="{rnd.randint(0,300)}" r="{rnd.choice([0.6,0.8,1.1])}" fill="#d6e2ec" opacity="{rnd.choice([.3,.5,.8])}"/>' for _ in range(140))
    ridge = "M0 380 L80 360 L180 372 L280 340 L380 352 L470 330 L560 344 L660 326 L760 356 L860 362 L960 350 L1060 372 L1140 366 L1180 380 L1600 386 L1600 600 L0 600Z"
    plain = "M0 " + " L".join(f"{x} {ground_y(x):.1f}" for x in range(0, W + 1, 20)) + f" L{W} {H} L0 {H}Z"
    crater = (f'<path d="M1150 {ground_y(1150):.1f} Q1230 {ground_y(1230)+6:.1f} 1290 520 Q1400 596 1530 570 Q1580 556 1600 540 L1600 600 L1150 600Z" fill="#05090d" stroke="#1e4e5c" stroke-width="1.5"/>'
              f'<path d="M1150 {ground_y(1150):.1f} Q1230 {ground_y(1230)+6:.1f} 1290 520" fill="none" stroke="{CY}" stroke-width="1.5" opacity=".7"/>')
    rnd2 = random.Random(11)
    texture = "".join(f'<ellipse cx="{x}" cy="{y}" rx="{rnd2.choice([2,3,4,6])}" ry="{rnd2.choice([1,1.5,2])}" fill="none" stroke="#1e4e5c" stroke-width="1"/>'
                      for x, y in ((rnd2.randint(0, 1140), rnd2.randint(490, 595)) for _ in range(70)))
    base = (f'<rect width="{W}" height="{H}" fill="#05080c"/>{stars}'
            f'<circle cx="190" cy="250" r="34" fill="#16324f" stroke="#6fb6ff" stroke-width="1.5"/><path d="M160 244 Q190 232 220 248" stroke="#9ee0ff" stroke-width="1.2" fill="none" opacity=".7"/>'
            f'<path d="{ridge}" fill="#0b141c" stroke="{CY}" stroke-width="1.2" opacity=".9"/>'
            f'<path d="{plain}" fill="#0e1922" stroke="{CY}" stroke-width="1.5"/>{texture}{crater}'
            f'<text x="1490" y="590" fill="{DIM}" font-family="Share Tech Mono, monospace" font-size="13" text-anchor="middle">PERMANENTLY SHADOWED CRATER</text>')
    body, labels = "", ""
    for st, svg, lab in elements():
        if st <= stage_idx:
            body += svg
            if st == stage_idx and lab:
                labels += label(lab[1], lab[2], lab[0], lab[3], lab[4])
    foot = (f'<text x="24" y="{H-16}" fill="{AM}" font-family="Share Tech Mono, monospace" font-size="14">CONCEPT ILLUSTRATION · OPEN MOON</text>'
            f'<text x="24" y="34" fill="{INK}" font-family="Share Tech Mono, monospace" font-size="18">{title}</text>')
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Concept illustration of the Open Moon base: {title}">'
            f'<title>Open Moon base concept: {title}</title>{base}{body}{labels}{foot}</svg>')

def main():
    OUT.mkdir(parents=True, exist_ok=True)
    stages = yaml.safe_load(open(ROOT / "_data" / "roadmap.yml"))
    for i, s in enumerate(stages):
        t = f"YEAR {s['year']} ({s['cal']}) · {' '.join(s['label']).upper()}"
        (OUT / f"year-{s['year']:02d}.svg").write_text(scene(i, t))
    print(len(stages), "images written")

if __name__ == "__main__":
    main()
