"""Build the Blueprint-layout theme variants into templates/.

Run from the repo root:  python3 _templates_src/build.py
Every page shares body.html (markup) and base.css (layout). Each theme only
adds fonts, colour variables and its own CSS, so layout changes happen once.
"""
import pathlib

SRC = pathlib.Path(__file__).parent
ROOT = SRC.parent
BODY = (SRC / "body.html").read_text()
BASE = (SRC / "base.css").read_text()

PUNK_STRIP = """<div class="strip"><span class="live">● LIVE</span><span>SECTOR <b>D-4</b></span><span>DEPTH <b>−18 m</b></span><span>HAB P <b data-k="p">101.3</b> kPa</span><span>O₂ <b data-k="o2">20.9</b>%</span><span>CO₂ <b data-k="co2">612</b> ppm</span><span>DOSE <b data-k="dose">0.42</b> µSv/h</span><span>BASE TIME <b data-clock>--:--:--</b></span></div>"""
PUNK_JS = """<script>
(function(){var r={p:[101.3,.2,1],o2:[20.9,.15,1],co2:[612,25,0],dose:[.42,.05,2]};
function t(){document.querySelectorAll('[data-k]').forEach(function(e){var v=r[e.dataset.k];e.textContent=(v[0]+(Math.random()-.5)*2*v[1]).toFixed(v[2])});
var d=new Date();document.querySelectorAll('[data-clock]').forEach(function(e){e.textContent=d.toISOString().slice(11,19)})}
t();setInterval(t,1500)})();
</script>"""
PUNK_BASE = """
.strip{display:flex;flex-wrap:wrap;gap:4px 22px;padding:8px 20px;font:12px var(--fm);letter-spacing:.08em;color:var(--dim);border-bottom:1px solid var(--line)}
.strip b{color:var(--ink);font-weight:500}
.strip .live{color:var(--hi);animation:blink 1.6s steps(2) infinite}
@keyframes blink{50%{opacity:.25}}
"""

THEMES = [
# ---------------- Iterations on the Blueprint layout ----------------
dict(group="iter", slug="01-graphite", name="Graphite",
 desc="Dark product-spec sheet. Charcoal panels, orange accent, crisp sans.",
 fonts="Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500",
 logo="OPEN<span>MOON</span>", eyebrow="Component spec",
 css="""
:root{--bg:#111214;--sheet:#17181b;--ink:#eceef1;--dim:#8d929b;--line:#2a2c31;--hi:#ff7a1a;--hi2:#ffb070;--warn:#ffb070;--bad:#ff5a4f;
--sk:#c9cdd4;--skfill:#202226;--hatch:#3a3d44;--fh:Inter,sans-serif;--fb:Inter,sans-serif;--fm:"JetBrains Mono",monospace;--r:14px;--logo-ls:.02em;--h1-ls:-.02em;
--figbg:#1c1e22;--figp:14px;--cob:0px solid;--cogap:10px;--cobg:#1c1e22;--cor:10px;--bfill:#ff7a1a;--btxt:#111;--trlr:3px}
.sheet{box-shadow:0 30px 80px rgba(0,0,0,.45)}
.callouts{border-top:0}
"""),
dict(group="iter", slug="02-datasheet", name="Datasheet",
 desc="Light engineering datasheet. Warm paper, black ink, one signal red.",
 fonts="IBM+Plex+Sans:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500;600",
 logo="Open Moon<span>.</span>", eyebrow="Datasheet 1.2.1",
 css="""
:root{--bg:#ecebe6;--sheet:#fbfaf6;--ink:#141414;--dim:#66645e;--line:#cfccc3;--hi:#d7261e;--hi2:#d7261e;--warn:#c56a00;--bad:#d7261e;
--sk:#141414;--skfill:#fff;--hatch:#b9b5aa;--fh:"IBM Plex Sans",sans-serif;--fb:"IBM Plex Sans",sans-serif;--fm:"IBM Plex Mono",monospace;--bw:1px;--logo-ls:0;--h1-w:600;--h1-ls:-.01em}
.sheet{box-shadow:0 2px 0 #d8d5cc,0 20px 50px rgba(0,0,0,.08)}
header.bar{border-bottom:3px solid var(--ink)}
.side h2{color:var(--ink);border-bottom:2px solid var(--ink);padding-bottom:4px}
.titleblock{border-top:3px solid var(--ink)}
"""),
dict(group="iter", slug="03-regolith", name="Regolith",
 desc="Soft lunar greys with a sand accent. Solid filled schematic, rounded cards.",
 fonts="Manrope:wght@400;500;600;700;800&family=DM+Mono:wght@400;500",
 logo="open<span>moon</span>", eyebrow="Phase 1 · Power",
 css="""
:root{--bg:#d9d7d2;--sheet:#e9e7e2;--ink:#2a2926;--dim:#6e6b64;--line:#cbc8c0;--hi:#a8743a;--hi2:#a8743a;--warn:#b0782f;--bad:#a2412f;
--sk:#55534d;--skfill:#cfccc4;--hatch:#b4b0a6;--fh:Manrope,sans-serif;--fb:Manrope,sans-serif;--fm:"DM Mono",monospace;--r:18px;--logo-w:800;--logo-ls:-.02em;--h1-w:800;--h1-ls:-.03em;
--figbg:#dedbd4;--figp:12px;--cob:0px solid;--cogap:10px;--cobg:#dedbd4;--cor:14px;--bfill:#a8743a;--btxt:#fff;--trlr:6px;--riskbg:#e1ded7}
.sheet{border:0;box-shadow:0 20px 60px rgba(60,50,40,.18)}
.schem .p-rad{fill:#bfbbb2}.schem .p-core{fill:#a8a49b}.schem .p-out{fill:#c9b79c}
.callouts{border-top:0}.risk{border-left-width:4px}
"""),
dict(group="iter", slug="04-archive", name="Archive Report",
 desc="1960s technical report. Typewriter type, cream stock, rubber-stamp red.",
 fonts="Courier+Prime:wght@400;700&family=Libre+Baskerville:wght@400;700",
 logo="OPEN MOON <span>/</span> TECHNICAL REPORT", eyebrow="Technical memorandum OM-1.2.1",
 css="""
:root{--bg:#cfc6b2;--sheet:#f3ecd9;--ink:#2b2620;--dim:#6d6352;--line:#a99e86;--hi:#b3261e;--hi2:#2b2620;--warn:#8a5a00;--bad:#b3261e;
--sk:#2b2620;--skfill:none;--hatch:#8f8570;--fh:"Libre Baskerville",serif;--fb:"Courier Prime",monospace;--fm:"Courier Prime",monospace;--logo-ls:.04em;--h1-w:700;--h1-tt:uppercase;--h1-s:30px;--stamprot:-6deg}
.logo{font-size:18px}
.sheet{box-shadow:4px 6px 0 rgba(0,0,0,.12);background-image:repeating-linear-gradient(0deg,transparent 0 27px,rgba(80,60,30,.05) 27px 28px)}
.stamp{font-size:14px;border-width:3px;opacity:.85}
.schem .s{stroke-width:1.2}
"""),
dict(group="iter", slug="05-swiss", name="Swiss",
 desc="International-style grid. Heavy grotesk, big numerals, black and red on white.",
 fonts="Inter+Tight:wght@500;700;800;900&family=Inter:wght@400;500&family=JetBrains+Mono:wght@400",
 logo="Open<br>Moon", eyebrow="1.2.1",
 css="""
:root{--bg:#fff;--sheet:#fff;--ink:#000;--dim:#555;--line:#000;--hi:#e30613;--hi2:#e30613;--warn:#000;--bad:#e30613;
--sk:#000;--skfill:#fff;--hatch:#000;--fh:"Inter Tight",sans-serif;--fb:Inter,sans-serif;--fm:"JetBrains Mono",monospace;--bw:2px;--logo-w:900;--logo-ls:-.03em;--h1-w:900;--h1-s:56px;--h1-ls:-.04em;--cob:2px solid}
.logo{font-size:28px;line-height:.9}
.eyebrow{font:900 64px/1 var(--fh);color:var(--hi);letter-spacing:-.04em}
.draw h1{line-height:.95}
.co b{border-radius:0;background:#000;color:#fff;border-color:#000}
.schem .b circle{fill:#e30613;stroke:#e30613}.schem .bt text{fill:#fff}
.side h2{color:#000;font:800 18px var(--fh);letter-spacing:-.01em;text-transform:none}
@media (max-width:520px){.draw h1{font-size:38px}.eyebrow{font-size:44px}}
"""),
dict(group="iter", slug="06-glass-cockpit", name="Glass Cockpit",
 desc="Avionics display. Slate panels, cyan readouts, amber cautions.",
 fonts="Rajdhani:wght@500;600;700&family=Share+Tech+Mono",
 logo="OPEN<span>MOON</span>", eyebrow="PWR · FSP UNIT 1",
 css="""
:root{--bg:#0b1117;--sheet:#101820;--ink:#d6e2ec;--dim:#7890a3;--line:#22313f;--hi:#38d4f0;--hi2:#7cf29a;--warn:#ffb020;--bad:#ff4d4d;
--sk:#38d4f0;--skfill:rgba(56,212,240,.06);--hatch:#1e4e5c;--fin:#38d4f0;--fh:Rajdhani,sans-serif;--fb:Rajdhani,sans-serif;--fm:"Share Tech Mono",monospace;--r:8px;--h1-w:700;--h1-tt:uppercase;--h1-ls:.04em;
--figbg:#0a1015;--figb:1px;--figp:10px;--cob:0px solid;--cogap:8px;--cobg:#0d151c;--cor:6px}
body{font-size:15px}
.sheet{box-shadow:0 0 0 1px #000,0 0 40px rgba(56,212,240,.08) inset}
.callouts{border-top:0}
.fig{background-image:linear-gradient(rgba(56,212,240,.05) 1px,transparent 1px),linear-gradient(90deg,rgba(56,212,240,.05) 1px,transparent 1px);background-size:24px 24px}
"""),
dict(group="iter", slug="07-earthrise", name="Earthrise",
 desc="Deep-space gradient, frosted glass panels, Earth-blue highlights.",
 fonts="Sora:wght@400;500;600;700&family=IBM+Plex+Mono:wght@400;500",
 logo="Open Moon", eyebrow="Phase 1 · Power system",
 css="""
:root{--bg:#05070d;--ink:#eef2fa;--dim:#9aa6bd;--line:rgba(255,255,255,.12);--hi:#6fb6ff;--hi2:#9ee0ff;--warn:#ffcf70;--bad:#ff7d7d;
--sk:#dfe8f7;--skfill:rgba(255,255,255,.04);--hatch:rgba(255,255,255,.18);--fh:Sora,sans-serif;--fb:Sora,sans-serif;--fm:"IBM Plex Mono",monospace;--r:22px;--logo-ls:0;--h1-w:600;--h1-ls:-.02em;
--sheet:rgba(255,255,255,.04);--figbg:rgba(255,255,255,.03);--figp:12px;--cob:0px solid;--cogap:10px;--cobg:rgba(255,255,255,.05);--cor:14px;--bfill:#6fb6ff;--btxt:#05070d;--trlr:5px}
body{background:radial-gradient(900px 500px at 85% -10%,#1f4f8f 0,transparent 60%),radial-gradient(700px 400px at 0% 110%,#2b1c4f 0,transparent 60%),#05070d;min-height:100vh}
.sheet{backdrop-filter:blur(14px);box-shadow:0 40px 100px rgba(0,0,0,.5)}
.callouts{border-top:0}
.logo::before{content:"";display:inline-block;width:18px;height:18px;border-radius:50%;margin-right:10px;vertical-align:-2px;background:radial-gradient(circle at 35% 35%,#bfe0ff,#2f6fd0 60%,#0d2a5a)}
"""),
dict(group="iter", slug="08-brutalist", name="Brutalist",
 desc="Concrete grey, thick black rules, hazard-yellow highlights.",
 fonts="Archivo+Black&family=Space+Mono:wght@400;700",
 logo="OPEN_MOON", eyebrow="[COMPONENT 1.2.1]",
 css="""
:root{--bg:#c9c9c4;--sheet:#e4e4df;--ink:#000;--dim:#3d3d3a;--line:#000;--hi:#000;--hi2:#000;--warn:#000;--bad:#000;
--sk:#000;--skfill:#ffd400;--hatch:#000;--fh:"Archivo Black",sans-serif;--fb:"Space Mono",monospace;--fm:"Space Mono",monospace;--bw:4px;--h1-w:400;--h1-tt:uppercase;--h1-s:44px;--h1-ls:-.01em;--cob:3px solid;--bfill:#ffd400;--btxt:#000}
.sheet{box-shadow:12px 12px 0 #000}
.logo{background:#ffd400;padding:2px 10px;border:3px solid #000}
nav a.on{background:#ffd400;border:0;padding:0 6px}
.schem .p-rad,.schem .p-out{fill:#fff}
.co b{background:#ffd400;border:2px solid #000;border-radius:0}
.side h2{background:#000;color:#ffd400;padding:4px 8px;display:inline-block}
.risk{border:3px solid #000;border-left-width:10px;background:#fff}
.trl i.f{background:#ffd400;border-color:#000}
.titleblock{background:repeating-linear-gradient(-45deg,#ffd400 0 14px,#000 14px 28px)}
.titleblock div{background:#e4e4df;margin:6px 0}
@media (max-width:520px){.draw h1{font-size:30px}.sheet{box-shadow:6px 6px 0 #000}}
"""),
dict(group="iter", slug="09-field-manual", name="Field Manual",
 desc="Expedition field manual. Olive and khaki, stencil headings, plain instructions.",
 fonts="Big+Shoulders+Stencil+Display:wght@700;800&family=Courier+Prime:wght@400;700&family=Barlow:wght@400;500;600",
 logo="OPEN MOON <span>FM 1-2</span>", eyebrow="Chapter 2 · Power",
 css="""
:root{--bg:#3d4230;--sheet:#e6dfc8;--ink:#23261b;--dim:#5e604c;--line:#a8a284;--hi:#5a6b2a;--hi2:#8a3b12;--warn:#8a5a00;--bad:#8a1f12;
--sk:#23261b;--skfill:#d8d0b4;--hatch:#9d9677;--fh:"Big Shoulders Stencil Display",sans-serif;--fb:Barlow,sans-serif;--fm:"Courier Prime",monospace;--bw:2px;--logo-ls:.06em;--h1-w:800;--h1-tt:uppercase;--h1-s:46px;--h1-ls:.02em;--stamprot:-4deg}
.logo{font-size:28px}
header.bar{background:#5a6b2a;color:#efe9d2}.logo{color:#efe9d2}.logo span{color:#e6c55a}
header.bar nav a{color:#d6d0b3}header.bar nav a.on{color:#fff;border-color:#e6c55a}
.co h3{font-size:19px;text-transform:uppercase;letter-spacing:.05em}
.side h2{color:var(--ink);font:800 20px var(--fh);letter-spacing:.06em}
.stamp{color:#8a1f12;border-color:#8a1f12}
"""),
dict(group="iter", slug="10-studio", name="Studio",
 desc="Bright modern docs. Pastel colour-coded parts that match the callouts.",
 fonts="Plus+Jakarta+Sans:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500",
 logo="open<span>moon</span>", eyebrow="Phase 1 → Power → 1.2.1",
 css="""
:root{--bg:#f4f5fb;--sheet:#fff;--ink:#16182b;--dim:#646a86;--line:#e4e6f0;--hi:#5b5bf0;--hi2:#f0884a;--warn:#e08a1e;--bad:#e5484d;
--sk:#2b2e4a;--skfill:#fff;--hatch:#c9cce0;--fh:"Plus Jakarta Sans",sans-serif;--fb:"Plus Jakarta Sans",sans-serif;--fm:"JetBrains Mono",monospace;--r:16px;--logo-w:800;--logo-ls:-.02em;--h1-w:800;--h1-ls:-.03em;
--figbg:#f7f8fd;--figp:12px;--cob:0px solid;--cogap:10px;--cor:12px;--trlr:4px;--bfill:#5b5bf0;--btxt:#fff}
.sheet{border:0;box-shadow:0 1px 2px rgba(20,20,60,.06),0 20px 50px rgba(20,20,60,.08)}
.callouts{border-top:0}
.schem .p-core{fill:#ffe1d1}.schem .p-conv{fill:#d9f2e4}.schem .p-rad{fill:#e0e3ff}.schem .p-shield{fill:#fff1c7}.schem .p-out{fill:#eef0f6}
.co:nth-child(1){background:#fff3ec}.co:nth-child(2){background:#eefaf3}.co:nth-child(3){background:#f0f1ff}.co:nth-child(4){background:#fff8e0}.co:nth-child(5){background:#f3f4f8}
.co b{background:#fff;border-color:var(--ink);color:var(--ink)}
"""),

# ---------------- Moonpunk: a real underground base ----------------
dict(group="punk", slug="p1-shaft-terminal", name="Shaft 7 Terminal",
 desc="Amber CRT terminal in a maintenance shaft. Scanlines, glow, live hab telemetry.",
 fonts="VT323",
 logo="OPEN_MOON://SHAFT-7", eyebrow="> cat /plan/phase1/power/1.2.1",
 strip=PUNK_STRIP, after=PUNK_JS,
 css=PUNK_BASE+"""
:root{--bg:#0a0700;--ink:#ffb000;--dim:#a87400;--line:#5a3e00;--hi:#ffd27a;--hi2:#ffd27a;--warn:#ffd27a;--bad:#ff5a2a;
--sk:#ffb000;--skfill:none;--hatch:#5a3e00;--fh:VT323,monospace;--fb:VT323,monospace;--fm:VT323,monospace;--logo-ls:.04em;--h1-w:400;--h1-tt:uppercase;--h1-s:44px}
body{font-size:19px;text-shadow:0 0 6px rgba(255,176,0,.55);min-height:100vh}
body::after{content:"";position:fixed;inset:0;pointer-events:none;background:repeating-linear-gradient(0deg,rgba(0,0,0,.28) 0 2px,transparent 2px 4px),radial-gradient(ellipse at center,transparent 55%,rgba(0,0,0,.65));z-index:9}
.strip{font-size:17px}
.draw h1::after{content:"█";animation:blink 1s steps(2) infinite;margin-left:6px}
.note,.co ul,.spec,.risk,.srcs,.titleblock{font-size:17px}
.side h2,.eyebrow,nav a,.risk .t,.titleblock small,.trl-l{font-size:16px}
.schem text{font-size:16px}
.schem *{filter:drop-shadow(0 0 2px rgba(255,176,0,.6))}
.co b{border-radius:0}
"""),
dict(group="punk", slug="p2-neon-lava-tube", name="Neon Lava Tube",
 desc="A colony carved into a lava tube. Magenta and cyan neon on wet black rock.",
 fonts="Chakra+Petch:wght@500;600;700&family=Share+Tech+Mono",
 logo="OPEN<span>MOON</span>", eyebrow="Marius Hills tube · Level −3",
 strip=PUNK_STRIP, after=PUNK_JS,
 css=PUNK_BASE+"""
:root{--bg:#07050c;--ink:#f2e9ff;--dim:#9b8fb5;--line:#2c2140;--hi:#ff2bd6;--hi2:#22f0ff;--warn:#ffcc33;--bad:#ff2b5e;
--sk:#22f0ff;--skfill:rgba(34,240,255,.05);--hatch:#3a2a55;--fin:#22f0ff;--fh:"Chakra Petch",sans-serif;--fb:"Chakra Petch",sans-serif;--fm:"Share Tech Mono",monospace;--h1-w:700;--h1-tt:uppercase;--h1-s:40px;--h1-ls:.04em;
--sheet:rgba(14,9,24,.85);--figbg:rgba(0,0,0,.35);--figp:10px;--cob:1px solid;--bfill:#07050c}
body{min-height:100vh;background:radial-gradient(600px 300px at 15% 0,rgba(255,43,214,.18),transparent 70%),radial-gradient(700px 400px at 100% 100%,rgba(34,240,255,.12),transparent 70%),repeating-linear-gradient(100deg,#07050c 0 40px,#0a0711 40px 41px),#07050c}
.sheet{box-shadow:0 0 0 1px #ff2bd6,0 0 30px rgba(255,43,214,.35),inset 0 0 60px rgba(34,240,255,.05)}
.logo,.draw h1{text-shadow:0 0 8px #ff2bd6,0 0 24px rgba(255,43,214,.6)}
.logo span{color:#22f0ff;text-shadow:0 0 8px #22f0ff}
.draw h1{animation:flick 6s infinite}
@keyframes flick{0%,96%,100%{opacity:1}97%{opacity:.4}98%{opacity:1}99%{opacity:.6}}
.schem .s,.schem .c{filter:drop-shadow(0 0 3px currentColor)}
.schem .s{color:#22f0ff}.schem .c{color:#ff2bd6;stroke:#ff2bd6}
.side h2{text-shadow:0 0 8px #ff2bd6}
.trl i.f{box-shadow:0 0 8px #ff2bd6}
"""),
dict(group="punk", slug="p3-hab-ops", name="Hab Ops Console",
 desc="Industrial control panel. Brushed steel, rivets, hazard stripes, green phosphor.",
 fonts="Oxanium:wght@500;600;700;800&family=Share+Tech+Mono",
 logo="HAB OPS <span>//</span> OPEN MOON", eyebrow="Power bus A · Reactor bay",
 strip=PUNK_STRIP, after=PUNK_JS,
 css=PUNK_BASE+"""
:root{--bg:#1a1c1d;--sheet:#25282a;--ink:#d9e0e2;--dim:#8a9497;--line:#3c4144;--hi:#39ff7a;--hi2:#ffd000;--warn:#ffd000;--bad:#ff3b30;
--sk:#39ff7a;--skfill:rgba(57,255,122,.04);--hatch:#1f5a33;--fin:#39ff7a;--fh:Oxanium,sans-serif;--fb:Oxanium,sans-serif;--fm:"Share Tech Mono",monospace;--bw:2px;--r:6px;--h1-w:800;--h1-tt:uppercase;--h1-ls:.03em;
--figbg:#06110a;--figb:2px;--figp:10px;--cob:0px solid;--cogap:8px;--cobg:#1e2123;--cor:4px}
body{background:repeating-linear-gradient(90deg,#1a1c1d 0 3px,#1c1e1f 3px 6px)}
.sheet{background:linear-gradient(180deg,#2c2f31,#222527);box-shadow:inset 0 1px 0 rgba(255,255,255,.08),0 20px 50px rgba(0,0,0,.6);position:relative}
.sheet::before{content:"";display:block;height:12px;background:repeating-linear-gradient(-45deg,#ffd000 0 12px,#111 12px 24px)}
.fig{box-shadow:inset 0 0 30px rgba(57,255,122,.12);border-color:#0d0f10}
.schem .s,.schem text{filter:drop-shadow(0 0 2px rgba(57,255,122,.7))}
.schem text{fill:#39ff7a}
.co{border:1px solid #3c4144;box-shadow:inset 0 1px 0 rgba(255,255,255,.05)}
.co::before,.co::after{content:"";float:right;width:6px;height:6px;border-radius:50%;background:#555;box-shadow:inset 0 1px 1px #000;margin-left:4px}
.side section{background:linear-gradient(180deg,rgba(255,255,255,.02),transparent)}
.risk.crit{animation:alarm 1.2s infinite}
@keyframes alarm{50%{background:rgba(255,59,48,.15)}}
.callouts{border-top:0}
"""),
dict(group="punk", slug="p4-consortium", name="Consortium Intranet",
 desc="A corporate moonbase intranet. Sleek black and red, clearance badges, a quota ticker.",
 fonts="Michroma&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500",
 logo="MARE <span>INDUSTRIAL</span>", eyebrow="Clearance L3 · Asset register",
 strip=PUNK_STRIP.replace('<span class="live">● LIVE</span>','<span class="live">● LIVE</span><span>EMPLOYEE <b>#40-1187</b></span><span>CLEARANCE <b>L3</b></span>'), after=PUNK_JS,
 css=PUNK_BASE+"""
:root{--bg:#0b0b0d;--sheet:#111114;--ink:#f1f1f3;--dim:#8b8b95;--line:#26262c;--hi:#ff1f3d;--hi2:#ff1f3d;--warn:#ff9f1a;--bad:#ff1f3d;
--sk:#e8e8ec;--skfill:#16161a;--hatch:#2e2e35;--fh:Michroma,sans-serif;--fb:Inter,sans-serif;--fm:"JetBrains Mono",monospace;--logo-ls:.18em;--h1-w:400;--h1-tt:uppercase;--h1-s:28px;--h1-ls:.08em;
--cob:1px solid;--bfill:#ff1f3d;--btxt:#fff}
.logo{font-size:16px}
.strip{background:#ff1f3d;color:#2a0006;border:0}.strip b{color:#fff}.strip .live{color:#fff}
.sheet{border-color:#26262c;box-shadow:0 0 0 1px #000}
header.bar::after{content:"OXYGEN ALLOCATION ON SCHEDULE · SHIFT 3 BEGINS 18:00 · REPORT DUST BREACHES TO SECTOR SUPERVISOR · ";flex-basis:100%;white-space:nowrap;overflow:hidden;font:11px var(--fm);color:var(--dim);letter-spacing:.1em;animation:tick 30s linear infinite}
@keyframes tick{from{text-indent:100%}to{text-indent:-220%}}
.draw h1{line-height:1.3}
.co b{border-radius:2px;background:#ff1f3d;color:#fff}
.stamp{background:#ff1f3d;color:#fff;border-color:#ff1f3d}
"""),
dict(group="punk", slug="p5-maintenance-tablet", name="Maintenance Tablet",
 desc="A scuffed, rugged field tablet a tech carries down the tunnels. Grime, tape, big touch targets.",
 fonts="Barlow+Condensed:wght@500;600;700;800&family=Fira+Code:wght@400;500",
 logo="TECH-PAD <span>v4.2</span>", eyebrow="Work order WO-2291 · Reactor bay",
 strip=PUNK_STRIP, after=PUNK_JS,
 css=PUNK_BASE+"""
:root{--bg:#141310;--sheet:#1f1d18;--ink:#ece6d6;--dim:#9a917c;--line:#3a362c;--hi:#f5c400;--hi2:#f5c400;--warn:#f5c400;--bad:#ff5b3a;
--sk:#ece6d6;--skfill:#25221c;--hatch:#4a4436;--fh:"Barlow Condensed",sans-serif;--fb:"Barlow Condensed",sans-serif;--fm:"Fira Code",monospace;--r:4px;--h1-w:800;--h1-tt:uppercase;--h1-s:44px;
--cob:0px solid;--cogap:8px;--cobg:#28251e;--cor:6px;--bfill:#f5c400;--btxt:#141310}
body{font-size:16px;background:radial-gradient(circle at 20% 30%,rgba(255,255,255,.03),transparent 30%),#141310}
.sheet{border:14px solid #2b2924;border-radius:28px;box-shadow:0 0 0 2px #000,0 30px 80px rgba(0,0,0,.7);position:relative;
background-image:radial-gradient(circle at 70% 20%,rgba(255,255,255,.04),transparent 40%),radial-gradient(circle at 10% 90%,rgba(120,100,60,.12),transparent 35%)}
.sheet::after{content:"DO NOT REMOVE FROM SECTOR D";position:absolute;top:8px;right:40px;z-index:2;background:#d8cfb2;color:#3a3020;font:700 11px var(--fm);padding:3px 14px;transform:rotate(3deg);box-shadow:0 1px 2px rgba(0,0,0,.5)}
.strip{background:#000;font-size:12px}
nav a{font:700 15px var(--fh);padding:6px 10px;border:1px solid var(--line);border-radius:6px}
nav a.on{background:#f5c400;color:#141310;border-color:#f5c400}
.co{min-height:110px}.co h3{font-size:19px;text-transform:uppercase}
.callouts{border-top:0}
.side h2{font:800 18px var(--fh);letter-spacing:.06em}
.risk{border-radius:6px;font-size:15px}
.stamp{color:#ff5b3a;border-color:#ff5b3a}
@media (max-width:520px){.sheet{border-width:8px;border-radius:18px}}
"""),
]

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Open Moon · {name}</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family={fonts}&display=swap" rel="stylesheet">
<style>
{base}
{css}
</style>
</head>
<body>
{body}
</body>
</html>
"""

def build():
    for t in THEMES:
        body = (BODY.replace("{{STRIP}}", t.get("strip", ""))
                    .replace("{{AFTER}}", t.get("after", ""))
                    .replace("{{LOGO}}", t["logo"])
                    .replace("{{EYEBROW}}", t["eyebrow"]))
        out = ROOT / "templates" / ("blueprint-v2" if t["group"] == "iter" else "moonpunk") / t["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(PAGE.format(name=t["name"], fonts=t["fonts"], base=BASE, css=t["css"].strip(), body=body))
    return THEMES

if __name__ == "__main__":
    for t in build():
        print(t["group"], t["slug"])
