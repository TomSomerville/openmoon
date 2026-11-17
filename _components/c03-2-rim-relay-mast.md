---
id_code: "C03.2"
milestone: M03
order: 2
title: Rim relay mast
summary: "A self-standing mast with a small radio station, set on the rim of a shadowed crater, so rovers and crews working on the crater floor stay connected to the base network."
trl: 5
spec:
  - {k: "Role", v: "Extend the base LTE / Wi-Fi network into a PSR worksite and backhaul it to the base"}
  - {k: "Mast height", v: "~10 m (NASA VSAT goal; 5 m threshold)"}
  - {k: "Radio", v: "LTE small cell + Wi-Fi mesh access point + point-to-point backhaul (design choice)"}
  - {k: "Line of sight", v: "~5.9 km to the horizon over flat ground from 10 m; ~8.5 km to a rover's 2 m antenna (arithmetic)"}
  - {k: "Load", v: "~100 W continuous (ESTIMATE)"}
  - {k: "Power", v: "Vertical solar panel + ~10 kWh battery, or cable from the base where within reach"}
  - {k: "Mass", v: "~205 kg solar version, ~120 kg cable version, incl. 30% margin (ESTIMATE)"}
  - {k: "Site", v: "Crater rim, slope up to 15° (VSAT goal)"}
  - {k: "Quantity", v: "3: one per PSR worksite (2) + 1 spare (design choice)"}
  - {k: "Delivery class", v: "Small or medium lander; placed by rover and crane (C02.2)"}
subcomponents:
  - name: Deployable mast
    desc: "A mast that packs short for launch and extends on the surface, carrying the antennas and solar panel high above the rim."
    parts: ["Helical metal-band or rolled composite mast", "Deployer drive and motor", "Top plate with antenna mounts", "Single-axis Sun-tracking gimbal for the panel", "Retraction for relocation"]
    tech: "NASA VSAT mast prototypes (Honeybee, Lockheed Martin, Astrobotic)"
    trl: 5
  - name: Radio package
    desc: "A small cellular cell and Wi-Fi access point point down into the crater, and a backhaul link points back to the base node (C03.1)."
    parts: ["LTE small cell with sector antenna aimed into the crater", "Wi-Fi mesh access point", "Point-to-point backhaul radio (or fibre in the cable version)", "Small router and data store", "Status beacon for rover navigation"]
    tech: "Nokia Bell Labs LSCS (IM-2); 802.11n lander WLAN"
    trl: 6
  - name: Power
    desc: "A vertical solar panel and battery keep the mast running through rim shadow periods, or a power cable from the base replaces most of the battery."
    parts: ["Vertical solar panel, ~1.5 m² (ESTIMATE)", "~10 kWh Li-ion battery (solar version)", "Power control and distribution", "Cable connector for grid power", "Electrodynamic dust shield on the panel (option)"]
    tech: "VSAT vertical solar arrays; LunaGrid-Lite cable power"
    trl: 5
  - name: Base, anchoring and leveling
    desc: "Wide legs, auto-leveling and regolith ballast hold the mast upright on a sloping rim."
    parts: ["Three or four adjustable legs", "Auto-leveling actuators", "Ballast trays filled with regolith by rover or crane", "Footpads sized for soft regolith", "Tilt sensor"]
    tech: "VSAT auto-leveling base; ballast is a design choice"
    trl: 4
  - name: Thermal and housing
    desc: "An insulated box keeps the radio electronics warm through shadow periods and sheds heat in sunlight."
    parts: ["Insulated electronics box", "Radiator facing away from the Sun", "Survival heaters", "Multi-layer insulation", "Dust seals"]
    tech: "Standard spacecraft practice"
    trl: 6
risks:
  - {sev: High, title: "The crater wall's shape blocks the line of sight to parts of the floor", fix: "Choose mast sites from LOLA terrain models before landing. Carry a rover-borne repeater for blind spots."}
  - {sev: High, title: "The mast buckles, unravels or tips over on a sloped, soft rim", fix: "Use auto-leveling legs and regolith ballast, and keep a low deployment height until the base is proven stable. Test buckling and unraveling, both of which are open VSAT risks."}
  - {sev: High, title: "Rim shadow periods drain the battery and the cold kills the radio, as happened to Nokia's device module on IM-2", fix: "Size the battery for ~100 h of darkness, insulate the box well, and use a power cable from the base where possible."}
  - {sev: Medium, title: "Frequencies for lunar surface cellular networks are not yet approved", fix: "Keep Wi-Fi mesh as a fallback and keep LTE equipment able to retune."}
  - {sev: Medium, title: "Dust from rovers and landers coats the solar panel and antennas", fix: "Keep masts far from roads and pads. Use a dust shield or brush, and the option of cable power."}
  - {sev: Medium, title: "A mast on a rim is a hazard to rovers and landers", fix: "Map every mast in the base hazard map and the landing keep-out zones. Fit a navigation beacon."}
  - {sev: Medium, title: "Moving or replacing a mast needs a rover and a crane", fix: "Use a retractable mast and the standard C02.1 lifting lugs so the C02.2 crane can move it."}
sources:
  - {title: "NASA NTRS: Vertical Solar Array Technology annual review", url: "https://ntrs.nasa.gov/api/citations/20230012849/downloads/GCD%20Annual%20Review%20VSAT%20September%202023%20Final.pdf", date: "Sep 2023"}
  - {title: "NASA: From Houston to the Moon, Johnson's thermal vacuum chamber tests lunar solar technology", url: "https://www.nasa.gov/centers-and-facilities/johnson/from-houston-to-the-moon-johnsons-thermal-vacuum-chamber-tests-lunar-solar-technology", date: "2024"}
  - {title: "NASA NSSDC: Moon fact sheet", url: "https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html", date: "accessed Nov 2026"}
  - {title: "Shackleton (crater), Wikipedia", url: "https://en.wikipedia.org/wiki/Shackleton_(crater)", date: "accessed Nov 2026"}
  - {title: "Gläser et al. 2014, Icarus: Illumination at the lunar south pole", url: "https://ui.adsabs.harvard.edu/abs/2014Icar..243...78G", date: "2014"}
  - {title: "Csank & Scott, NASA GRC: Power and Energy for the Lunar Surface", url: "https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf", date: "Apr 2022"}
  - {title: "Astrobotic: LunaGrid-Lite completes critical design review", url: "https://www.astrobotic.com/lunagrid-lite-completes-critical-design-review-flight-model-underway/", date: "Aug 2025"}
  - {title: "Nokia: Nokia and Intuitive Machines deliver first cellular network to the Moon", url: "https://www.nokia.com/newsroom/nokia-and-intuitive-machines-deliver-first-cellular-network-to-the-moon-achieve-some-key-mission-objectives/", date: "Mar 2025"}
  - {title: "NASA: LunaNet Interoperability Specification v5", url: "https://www.nasa.gov/wp-content/uploads/2025/02/lunanet-interoperability-specification-v5-baseline.pdf", date: "Jan 2025"}
  - {title: "Astrobotic Lunar Landers Payload User's Guide", url: "https://science.nasa.gov/wp-content/uploads/2023/11/astrobotic-lunar-landers-pug.pdf", date: "Aug 2021"}
  - {title: "NASA NTRS: VIPER Mission Overview (Andrews)", url: "https://ntrs.nasa.gov/api/citations/20205000864/downloads/2020-04-14%2C%20VIPER%20Mission%20Overview%20(Andrews).pdf", date: "Apr 2020"}
---

## What it does

Radio needs line of sight. A rover on the floor of a deep, permanently shadowed crater cannot see the base, Earth or most relay satellites. A rim relay mast stands on the crater rim, looks down into the worksite and passes data back to the base node (C03.1). It turns the PSR from a place of short, silent sorties into a connected worksite. M03 requires at least 10 Mbps to every robot, including at least one PSR worksite.

## How it works

- **Mast.** NASA's VSAT project developed masts for lunar solar arrays. Its goals were a 10 m height (5 m threshold), stable deployment on slopes of up to 15° (10° threshold), 10 deploy-and-retract cycles, and survival from −180 °C to +175 °C<sup class="r">[1](#s1)</sup>. Honeybee used a helical metal-band mast, Lockheed Martin a thin rolled composite mast, and Astrobotic a self-propelled cart with a gimbal<sup class="r">[1](#s1)</sup>. Prototypes were tested in thermal vacuum at NASA Johnson in 2024. Those tests required deployment on a curved surface and survival through 96 h of darkness<sup class="r">[2](#s2)</sup>. We use the same masts to carry antennas.
- **Radio.** Nokia's network-in-a-box ran its base station, radio and core on IM-2<sup class="r">[8](#s8)</sup>. The rim mast carries a smaller cell of the same kind, plus a Wi-Fi access point. Astrobotic landers already use 802.11n WLAN for deployed payloads<sup class="r">[10](#s10)</sup>. LunaNet expects surface users on Wi-Fi or 3GPP links, but the frequency bands for lunar cellular service are still under study<sup class="r">[9](#s9)</sup>.
- **Power.** Rim peaks at Shackleton are lit about 80–90% of the time<sup class="r">[4](#s4)</sup>. The best ridge point is lit 96% of the time at 10 m height<sup class="r">[5](#s5)</sup>. NASA cites intermittent darkness of up to about 100 h at the pole<sup class="r">[6](#s6)</sup>. Where the rim is close enough to the base, a power cable is simpler: Astrobotic's LunaGrid-Lite plans to send 1 kW over 500 m of light cable<sup class="r">[7](#s7)</sup>.
- **Anchoring.** NASA's VSAT work included auto-leveling bases<sup class="r">[1](#s1)</sup>. We add regolith ballast trays, filled by a rover or by the crane (C02.2), to resist tipping.
- **Why it matters for prospecting.** VIPER planned only about 6 h of work per PSR visit<sup class="r">[11](#s11)</sup>. With a live link, operators can steer the rover and drill in real time instead of planning blind.

## Sizing

**Line of sight (arithmetic).** On a smooth sphere, the distance to the horizon is d = √(2Rh), with R = 1,737.4 km<sup class="r">[3](#s3)</sup>:

- From a 10 m mast: √(2 × 1,737,400 × 10) ≈ 5,900 m.
- From a 2 m rover antenna: √(2 × 1,737,400 × 2) ≈ 2,640 m.
- So mast-to-rover range over flat ground is about 5.9 + 2.6 ≈ 8.5 km.

**Into a crater (Shackleton as the worst case).** Shackleton is 21 km across, 4.2 km deep, with a 6.6 km floor and walls of about 30°<sup class="r">[4](#s4)</sup>. From the rim to the floor's edge: horizontal (21 − 6.6) ÷ 2 = 7.2 km, drop 4.2 km, slant range √(7.2² + 4.2²) ≈ 8.3 km. To the floor centre: √(10.5² + 4.2²) ≈ 11.3 km. The sight line to the floor's edge drops at atan(4.2 ÷ 7.2) ≈ 30°, about the same as the wall. Any bulge in the wall therefore blocks the view, and mast sites must be checked against real terrain data. The PSRs chosen in M01 will mostly be smaller craters within cable distance of the base, which makes this easier.

**Power and mass (ESTIMATE).** Load: LTE cell 60 W + backhaul 20 W + computer and heaters 20 W = 100 W. Riding through 100 h of darkness needs 100 × 100 = 10 kWh, which is 10,000 ÷ 160 Wh/kg<sup class="r">[6](#s6)</sup> ≈ 63 kg of Li-ion.

| Item | Solar version (kg) | Cable version (kg) |
|---|---|---|
| Mast and deployer | 40 | 40 |
| Radios and router | 15 | 15 |
| Solar panel | 10 | 0 |
| Battery | 63 | 6 (1 kWh buffer) |
| Base, legs, ballast trays | 20 | 20 |
| Thermal and harness | 10 | 10 |
| **Subtotal** | **158** | **91** |
| **With 30% margin** | **~205** | **~120** (plus cable) |

## Testing and qualification

1. **Coverage model.** Use LOLA terrain to predict coverage from candidate rim sites into each M01 PSR. Publish the code.
2. **Mast tests.** Deploy, retract and redeploy 10 times on a 15° slope. Run thermal-vacuum tests to −180 °C, following the VSAT approach<sup class="r">[1](#s1)</sup>.
3. **Radio field test.** On an Earth crater rim, measure LTE and Wi-Fi throughput to a rover on the floor at 1–10 km.
4. **Dark survival test.** Run the full mast in a cold chamber through a 100 h dark period on battery.
5. **On the Moon.** Place the first mast on the rim of the first PSR worksite. Drive a rover into the crater and log throughput against position. Prove at least 10 Mbps across the worksite.

## Open questions

- Which rim sites give the best view into the PSRs that M01 selects? Can contributors run the LOLA viewshed analysis?
- Is LTE or Wi-Fi mesh the better choice for a single crater worksite?
- Is it cheaper to lay a power and fibre cable to the rim than to fly a 63 kg battery?
- Could the same mast also hold a vertical solar array for the M04 grid, sharing one deployment?
- How should rovers relay through each other when they are below the mast's line of sight?
