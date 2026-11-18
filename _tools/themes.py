"""Generate Open Moon colour-scheme previews.

Run from the repo root:  python3 _tools/themes.py
Writes assets/themes/<slug>.css (variable overrides on top of assets/site.css)
and _data/themes.yml (for the /themes/ gallery page).

Each scheme is defined by a neutral hue/saturation/lightness and two accents;
all other colours are derived so every scheme is internally consistent.
"""
import colorsys, pathlib, re, yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent

def hsl(h, s, l):
    r, g, b = colorsys.hls_to_rgb((h % 360) / 360, max(0, min(100, l)) / 100, max(0, min(100, s)) / 100)
    return "#%02x%02x%02x" % (round(r * 255), round(g * 255), round(b * 255))

# name, family, mode, neutral hue, neutral sat, background lightness, accent, accent 2
SCHEMES = [
    # cool light
    ("Daylight Cockpit", "Cool", "light", 205, 18, 95, "#0b7a8f", "#1e8a4c"),
    ("Arctic", "Cool", "light", 200, 30, 97, "#0369a1", "#0f766e"),
    ("Clean Lab", "Cool", "light", 210, 10, 99, "#0e7490", "#15803d"),
    ("Glacier", "Cool", "light", 190, 25, 94, "#0e7490", "#7c3aed"),
    ("Mist", "Cool", "light", 215, 14, 92, "#1d4ed8", "#0f766e"),
    ("Overcast", "Cool", "light", 220, 8, 90, "#2563eb", "#059669"),
    ("Steel Blue", "Cool", "light", 212, 22, 88, "#1e40af", "#0e7490"),
    ("Polar", "Cool", "light", 230, 20, 94, "#4338ca", "#0891b2"),
    ("Harbor", "Cool", "light", 198, 28, 90, "#075985", "#b45309"),
    ("Ice Station", "Cool", "light", 185, 30, 95, "#0f766e", "#2563eb"),
    ("Sky", "Cool", "light", 205, 60, 96, "#0369a1", "#db2777"),
    ("Moonlight", "Cool", "light", 220, 12, 96, "#2563eb", "#9333ea"),
    ("Blueprint Light", "Cool", "light", 215, 40, 96, "#1d4ed8", "#c2410c"),
    ("Agency Blue", "Cool", "light", 220, 30, 97, "#0b3d91", "#c62d1f"),
    # warm light
    ("Regolith", "Warm", "light", 40, 10, 92, "#9a3412", "#0f766e"),
    ("Lunar Dust", "Warm", "light", 35, 8, 89, "#7c2d12", "#1d4ed8"),
    ("Mission Paper", "Warm", "light", 45, 30, 96, "#b91c1c", "#1e3a8a"),
    ("Sandstone", "Warm", "light", 30, 25, 91, "#b45309", "#0f766e"),
    ("Basalt Light", "Warm", "light", 25, 6, 86, "#c2410c", "#0369a1"),
    ("Parchment", "Warm", "light", 42, 40, 93, "#92400e", "#166534"),
    ("Linen", "Warm", "light", 30, 20, 95, "#be123c", "#0f766e"),
    ("Ivory Ops", "Warm", "light", 50, 25, 97, "#a16207", "#0369a1"),
    ("Clay", "Warm", "light", 18, 22, 90, "#c2410c", "#15803d"),
    ("Desert Dawn", "Warm", "light", 28, 35, 94, "#c2410c", "#7c3aed"),
    ("Solar", "Warm", "light", 45, 60, 96, "#b45309", "#1d4ed8"),
    ("Copper Lab", "Warm", "light", 25, 15, 97, "#b45309", "#0e7490"),
    # green light
    ("Greenhouse", "Green", "light", 140, 18, 94, "#15803d", "#0e7490"),
    ("Sage", "Green", "light", 120, 10, 90, "#3f6212", "#1d4ed8"),
    ("Mint Ops", "Green", "light", 160, 25, 95, "#047857", "#7c3aed"),
    ("Moss", "Green", "light", 90, 12, 88, "#4d7c0f", "#b45309"),
    ("Seafoam", "Green", "light", 170, 25, 92, "#0f766e", "#be185d"),
    # purple / pink light
    ("Lavender", "Purple", "light", 260, 25, 95, "#6d28d9", "#0e7490"),
    ("Twilight Light", "Purple", "light", 250, 15, 90, "#5b21b6", "#b45309"),
    ("Orchid", "Purple", "light", 290, 20, 95, "#a21caf", "#0f766e"),
    ("Rose Quartz", "Purple", "light", 345, 30, 96, "#be123c", "#1d4ed8"),
    ("Mauve", "Purple", "light", 320, 10, 90, "#9d174d", "#0f766e"),
    # high-contrast light
    ("Swiss White", "Contrast", "light", 0, 0, 99, "#dc2626", "#111827"),
    ("Signal Orange", "Contrast", "light", 210, 8, 97, "#c2410c", "#0369a1"),
    ("Hazard", "Contrast", "light", 50, 40, 94, "#a16207", "#111827"),
    ("Concrete", "Contrast", "light", 0, 0, 88, "#a16207", "#1f2937"),
    # soft mid-tones (dark text replaced by light text, but far lighter than the current theme)
    ("Cockpit Soft", "Mid-tone", "mid", 205, 25, 18, "#38d4f0", "#7cf29a"),
    ("Graphite Soft", "Mid-tone", "mid", 215, 10, 22, "#38d4f0", "#7cf29a"),
    ("Dusk Slate", "Mid-tone", "mid", 220, 20, 26, "#7dd3fc", "#fbbf24"),
    ("Lunar Grey", "Mid-tone", "mid", 0, 0, 28, "#67e8f9", "#fcd34d"),
    ("Deep Sea Soft", "Mid-tone", "mid", 200, 30, 22, "#5eead4", "#fda4af"),
    ("Plum Dusk", "Mid-tone", "mid", 270, 18, 24, "#c4b5fd", "#fcd34d"),
    ("Olive Night", "Mid-tone", "mid", 80, 12, 22, "#bef264", "#67e8f9"),
    ("Charcoal Copper", "Mid-tone", "mid", 20, 8, 24, "#fdba74", "#67e8f9"),
    ("Storm", "Mid-tone", "mid", 210, 14, 32, "#93c5fd", "#fde68a"),
    ("Earthrise Dusk", "Mid-tone", "mid", 225, 30, 24, "#93c5fd", "#86efac"),
]

def derive(mode, h, s, L, a1, a2):
    if mode == "light":
        return {
            "bg": hsl(h, s, L), "sheet": hsl(h, s, min(L + 3, 99.6)), "panel": hsl(h, s, L - 2.5),
            "line": hsl(h, min(s * 1.2, 40), L - 13), "ink": hsl(h, min(s, 30), 13), "dim": hsl(h, min(s, 20), 40),
            "hi": a1, "hi2": a2, "warn": "#b45309", "bad": "#b91c1c", "btn": "#ffffff",
            "shadow": "0 1px 2px rgba(0,0,0,.06),0 12px 32px rgba(0,0,0,.08)",
        }
    return {
        "bg": hsl(h, s, L), "sheet": hsl(h, s, L + 4), "panel": hsl(h, s, L + 2),
        "line": hsl(h, s, L + 14), "ink": hsl(h, min(s, 15), 92), "dim": hsl(h, min(s, 12), 70),
        "hi": a1, "hi2": a2, "warn": "#fbbf24", "bad": "#f87171", "btn": hsl(h, s, 10),
        "shadow": "0 1px 2px rgba(0,0,0,.25),0 12px 32px rgba(0,0,0,.25)",
    }

def css(name, c):
    return (f"/* Open Moon colour scheme: {name}. Generated by _tools/themes.py */\n"
            f":root{{--bg:{c['bg']};--sheet:{c['sheet']};--panel:{c['panel']};--cobg:{c['panel']};--figbg:{c['panel']};"
            f"--ink:{c['ink']};--dim:{c['dim']};--line:{c['line']};--hi:{c['hi']};--hi2:{c['hi2']};--sk:{c['hi']};"
            f"--warn:{c['warn']};--bad:{c['bad']};--btn-ink:{c['btn']};--sheet-shadow:{c['shadow']}}}\n"
            f".fig{{background-image:none}}\n")

def main():
    out = ROOT / "assets" / "themes"
    out.mkdir(parents=True, exist_ok=True)
    data = []
    for name, fam, mode, h, s, L, a1, a2 in SCHEMES:
        slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
        c = derive(mode, h, s, L, a1, a2)
        (out / f"{slug}.css").write_text(css(name, c))
        data.append({"slug": slug, "name": name, "family": fam, "mode": mode,
                     "swatches": [c["bg"], c["panel"], c["line"], c["ink"], c["hi"], c["hi2"]]})
    yaml.safe_dump(data, open(ROOT / "_data" / "themes.yml", "w"), sort_keys=False)
    print(len(data), "schemes")

if __name__ == "__main__":
    main()
