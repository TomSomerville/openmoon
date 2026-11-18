---
id_code: "C08.1"
milestone: M08
order: 1
title: Standard 3-person habitat module
summary: "One standard pressurised module design that houses 3 people. The base lands three of them side by side and connects them, for 9 beds. The detailed design is to be defined later; the Thales Alenia MPH is the reference hardware, and its ~15 t is used only as a provisional placeholder."
trl: 5
spec:
  - {k: "Design", v: "One standard module that houses 3 people (DD-007); detailed design to be defined later (open)"}
  - {k: "Quantity", v: "3, landed side by side and connected, all in M08 before the first crew (DD-005)"}
  - {k: "Beds", v: "3 per module; 9 in all: 6 resident + 3 flexible for handovers (DD-006)"}
  - {k: "Connections", v: "Hatches or tunnels between modules: needed, not yet designed"}
  - {k: "Reference hardware", v: "Thales Alenia Space MPH (~3 m × 6 m, ASI contract Jul 2025), heritage only"}
  - {k: "Mass", v: "~15 t per module, PROVISIONAL placeholder from the MPH class"}
  - {k: "Life", v: "≥10 years on the surface (MPH reference)"}
  - {k: "Power draw", v: "20–50 kW for a 4-crew habitat (NASA GRC); base load for 6–9 people to be set in the load budget"}
  - {k: "Delivery", v: "Heavy cargo lander, NET FY2033"}
subcomponents:
  - name: Pressure shell and primary structure
    desc: "The sealed aluminium-alloy cylinder that holds the cabin atmosphere and carries launch and landing loads."
    parts: ["Welded cylindrical barrel and end domes", "Internal ring frames and longerons", "Micrometeoroid and debris shield", "Multi-layer insulation blanket", "Lift and tie-down points for landing and burial"]
    tech: "Thales Alenia ISS modules (Harmony, Tranquility, Columbus structure), Cygnus pressure vessels"
    trl: 6
  - name: Mobility and levelling
    desc: "Reference feature from the MPH: wheels let a module be moved from the landing pad and placed precisely beside its neighbours. Whether the standard module keeps them is open."
    parts: ["Wheel and suspension units", "Tow interface for LTVs", "Levelling jacks", "Brakes and wheel locks"]
    tech: "MPH baseline includes wheels; LTV towing is this plan's design choice"
    trl: 4
  - name: Hatches, ports and windows
    desc: "Openings for crew, cargo, a dust lock and the links to neighbouring modules (connection design to be defined later)."
    parts: ["Main hatch to dust lock / suitport bulkhead (C08.3)", "Second hatch for emergency exit", "Connecting hatch or tunnel to the neighbouring modules (not yet designed)", "Two small windows with dust covers (design choice)", "Utility pass-throughs for power, data, fluids"]
    tech: "ISS hatch and berthing heritage"
    trl: 6
  - name: Interior outfitting
    desc: "Fold-down and rack-mounted fittings that turn the cabin into living and working space."
    parts: ["3 beds (design to be defined later)", "Galley with food warmer and water dispenser", "Hygiene station and toilet", "Workstations and medical kit", "Exercise device and stowage racks"]
    tech: "ISS crew quarters, galley and waste-and-hygiene compartment heritage"
    trl: 6
  - name: Thermal control
    desc: "Keeps the cabin at room temperature while the sun sits low on the horizon and nearby ground stays very cold."
    parts: ["Internal water coolant loop", "External ammonia or similar loop", "Vertical radiators with dust covers", "Heaters for low-sun periods", "Thermal insulation and window shutters"]
    tech: "ISS active thermal control heritage"
    trl: 5
  - name: Power interface
    desc: "Connects the module to the M04 habitat microgrid, which the BMS supplies (DD-003), and keeps essential loads alive if the grid drops."
    parts: ["UMIC converter from the 3 kV AC grid to the 120 V DC habitat bus", "Internal power distribution units", "Essential-load battery", "Cable connector at the umbilical box"]
    tech: "M04 grid design; ISS power distribution heritage"
    trl: 5
risks:
  - {sev: Critical, title: "No standard 3-person module exists; its design is to be defined later (DD-007)", fix: "Use the MPH class only as reference and its ~15 t only as a placeholder; freeze the design before Phase 1 deliveries; track an inflatable as a backup"}
  - {sev: High, title: "Module-to-module connections are new interfaces and leak paths", fix: "Design hatches or tunnels with the module; each module can be sealed off on its own; leak-check every connection in the uncrewed run"}
  - {sev: High, title: "At handover peaks all 9 beds are full, so a module out of service leaves no spare bed", fix: "Shorten or delay the handover if a module is closed; storm shelter can serve as an emergency sleep area (C09.2)"}
  - {sev: High, title: "Dust on radiators and windows degrades heat rejection (Apollo saw instruments run ~68 °F hot)", fix: "Vertical radiators, covers when crews are outside, and electrodynamic dust shields on critical surfaces (C08.3)"}
  - {sev: High, title: "An unshielded module gives little protection from radiation", fix: "No crew until the modules are buried under ≥2 m of regolith (C09.1, DD-005)"}
  - {sev: Medium, title: "Wheels and suspension may fail while towing 15 t over rough ground", fix: "Prepared road from pad to habitat zone (M05); slow tow with two LTVs; jacks can level the module where it stops; side-by-side placement needs precise positioning"}
  - {sev: Medium, title: "Pressure shell leak from micrometeoroid hit or seal wear", fix: "Shielded shell, leak checks during the 3-month uncrewed run, patch kit, and nitrogen make-up reserves; neighbouring modules can be sealed off"}
  - {sev: Medium, title: "Grid outage cuts heating and life support", fix: "Essential-load battery and load shedding; crew moves to an unaffected module or the lander if the outage exceeds battery time"}
sources:
  - {title: "Thales Alenia Space: contract with ASI to develop lunar Multi-Purpose Habitation module", url: "https://www.thalesgroup.com/en/worldwide/space/press_release/thales-alenia-space-signs-contract-italian-space-agency-asi-develop", date: "Jul 2025"}
  - {title: "European Spaceflight: ASI awards new lunar habitat contract to Thales Alenia Space", url: "https://europeanspaceflight.com/asi-awards-new-lunar-habitat-contract-to-thales-alenia-space/", date: "Jul 2025"}
  - {title: "Wikipedia: Thales Alenia Space", url: "https://en.wikipedia.org/wiki/Thales_Alenia_Space", date: "2026"}
  - {title: "Csank & Scott, NASA GRC: Power and Energy for the Lunar Surface", url: "https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf", date: "Apr 2022"}
  - {title: "NASA HLS IAC 2026 presentation (cargo landers, habitat delivery NET FY2033)", url: "https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf", date: "Oct 2026"}
  - {title: "Gaier, NASA/TM-2005-213610: Effects of lunar dust on EVA systems during Apollo", url: "https://ntrs.nasa.gov/citations/20050160460", date: "2005"}
  - {title: "Zhang et al., Science Advances: radiation dose on the lunar surface (Chang'e-4)", url: "https://doi.org/10.1126/sciadv.aaz1334", date: "Sep 2020"}
  - {title: "TechCrunch: Sierra Space's inflatable habitat blows up as planned", url: "https://techcrunch.com/2024/01/22/successful-failure-sierra-spaces-inflatable-habitat-blows-up-as-planned", date: "Jan 2024"}
---

{% include decision-note.html id="DD-007" extra="This page used to describe one ~15 t MPH-class module for 4 crew on 14–30-day sorties. It now describes one standard 3-person module design, landed three times and connected. Specific figures from the MPH are reference values and placeholders only." %}

## What it does

The habitat module is the crew's home on the surface. Each module houses **3 people**. The base lands **three** of them next to each other and connects them, for **9 beds**: 6 for the resident crew and 3 flexible beds for handovers (this plan's arithmetic, DD-006, DD-007). The modules hold a breathable atmosphere, carry the life support system (C08.2), connect to the dust lock (C08.3) and give people somewhere to sleep, eat, wash and work for a 6.5-month tour.

**The detailed design is to be defined later (open).** This page does not set the module's size, layout or mass. It lists what the module must do and the reference hardware it can learn from.

## Reference hardware: Thales Alenia MPH

Thales Alenia Space is designing the Multi-Purpose Habitation (MPH) module for the Italian Space Agency. It is about 3 m × 6 m, about 15 t, with a minimum 10-year life and a planned 2033 launch<sup class="r">[1](#s1)</sup>. Press reports say it has wheels for precise positioning and is planned for two astronauts on one 7–30 day mission per year<sup class="r">[2](#s2)</sup>. Thales has built many pressurised modules, including Harmony, Tranquility and the Columbus structure on the ISS, and the Cygnus pressure vessels<sup class="r">[3](#s3)</sup>.

Open Moon uses the MPH as **heritage only**. Its ~15 t is used as a **provisional placeholder** for each standard module in the delivery costs (M08).

## What the module must do

- **House 3 people** for 6.5-month tours. Across three modules that gives 6 resident beds, plus 3 flexible beds that are full only at handover peaks (DD-006).
- **Connect to its neighbours.** Hatches or tunnels between the three modules are a needed element. They are not yet designed.
- **Be buried.** The modules sit under a support arch and regolith (C09.1). The regolith must never press on the module skin.
- **Shed heat through pumped loops** to surface radiators, because the regolith cover is a near-perfect insulator (C09.1). At the pole the sun stays low, so radiators are mounted vertically and kept clean. Apollo showed why: dust on radiator surfaces made one instrument run about 68 °F hotter than expected<sup class="r">[6](#s6)</sup>.
- **Take power from the grid.** NASA's Glenn team estimates a habitat for four crew on 30+ day stays draws **20–50 kW**<sup class="r">[4](#s4)</sup>. Each module plugs into the M04 habitat microgrid and has a battery for essential loads.

## Input to the load budget

Power sizing is not changed here. As an input to the Phase 1 load budget (DD-004): if habitat load grew in proportion to crew size from NASA's 20–50 kW for four<sup class="r">[4](#s4)</sup>, 6 people would need about 30–75 kW and 9 people about 45–113 kW (this plan's arithmetic, a crude linear scaling). The real figure must come from the module design.

## Placeholder figures (PROVISIONAL)

| Item | Value | Basis |
|---|---|---|
| Mass per module | ~15 t | MPH reference<sup class="r">[1](#s1)</sup>; placeholder until the design exists |
| Mass for 3 modules | ~45 t | 3 × 15 t (this plan's arithmetic) |
| Beds | 3 per module, 9 in all | DD-006, DD-007 |
| Power | 20–50 kW for a 4-crew habitat | NASA GRC<sup class="r">[4](#s4)</sup> |

## Testing and qualification

1. **Pressure tests on Earth.** Proof and leak tests of the shell, plus a burst test of a test article. As a benchmark, Sierra Space's LIFE inflatable held 77 psi before bursting, 27% above NASA's recommended level<sup class="r">[8](#s8)</sup>.
2. **Connection test.** Join three modules on the ground and leak-test every hatch or tunnel.
3. **Thermal vacuum test** of a complete module with radiators coated in lunar simulant.
4. **Crew-in-the-loop fit checks** in a mock-up of three connected modules, with 6 people for weeks and 9 people for 2 weeks.
5. **On the Moon.** NASA expects habitats to arrive on cargo landers no earlier than FY2033<sup class="r">[5](#s5)</sup>. After landing, placing, connecting and burying, the modules run uncrewed for at least 3 months before the first crew (M08).

## Open questions

- What is the module's size, mass and layout? (To be defined later.)
- How are the three modules joined: direct hatches, short tunnels or a shared node?
- How much radiation protection do the shell and stowage give? The surface dose measured by Chang'e-4 was about 1,369 µSv per day<sup class="r">[7](#s7)</sup>. NASA's OLTARIS tool could be run on the real geometry.
- Can the module and its connections take the shape change of a regolith arch over three modules side by side?
