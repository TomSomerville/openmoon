---
id_code: "C08.1"
milestone: M08
order: 1
title: Rigid surface habitat module
summary: "A ~15 t rigid pressurised module on wheels, in the Thales Alenia MPH class, that gives crews a shirt-sleeve home for 14–30 day sorties and can later be buried under regolith."
trl: 5
spec:
  - {k: "Class", v: "Thales Alenia Space MPH (preliminary design, ASI contract Jul 2025)"}
  - {k: "Size", v: "~3 m wide × ~6 m long"}
  - {k: "Mass", v: "~15 t at landing"}
  - {k: "Pressurised envelope", v: "~42 m³ outer (ESTIMATE, π × 1.5² × 6)"}
  - {k: "Crew", v: "2 in the MPH baseline; 4 in this plan (design choice, needs extra sleep stations)"}
  - {k: "Life", v: "≥10 years on the surface"}
  - {k: "Power draw", v: "20–50 kW for 4 crew (NASA GRC)"}
  - {k: "Delivery", v: "Heavy cargo lander, NET FY2033"}
  - {k: "Quantity", v: "1 in M08; 2 more of the same class in M09"}
subcomponents:
  - name: Pressure shell and primary structure
    desc: "The sealed aluminium-alloy cylinder that holds the cabin atmosphere and carries launch and landing loads."
    parts: ["Welded cylindrical barrel and end domes", "Internal ring frames and longerons", "Micrometeoroid and debris shield", "Multi-layer insulation blanket", "Lift and tie-down points for landing and burial"]
    tech: "Thales Alenia ISS modules (Harmony, Tranquility, Columbus structure), Cygnus pressure vessels"
    trl: 6
  - name: Mobility and levelling
    desc: "Wheels let the module be moved from the landing pad and placed precisely in the habitat zone."
    parts: ["Wheel and suspension units", "Tow interface for LTVs", "Levelling jacks", "Brakes and wheel locks"]
    tech: "MPH baseline includes wheels; LTV towing is this plan's design choice"
    trl: 4
  - name: Hatches, ports and windows
    desc: "Openings for crew, cargo, a dust lock and later module-to-module links."
    parts: ["Main hatch to dust lock / suitport bulkhead (C08.3)", "Second hatch for emergency exit", "Berthing port for M09 modules", "Two small windows with dust covers (design choice)", "Utility pass-throughs for power, data, fluids"]
    tech: "ISS hatch and berthing heritage"
    trl: 6
  - name: Interior outfitting
    desc: "Fold-down and rack-mounted fittings that turn the cabin into living and working space."
    parts: ["2 crew quarters plus 2 fold-down sleep stations", "Galley with food warmer and water dispenser", "Hygiene station and toilet", "Workstations and medical kit", "Exercise device and stowage racks"]
    tech: "ISS crew quarters, galley and waste-and-hygiene compartment heritage"
    trl: 6
  - name: Thermal control
    desc: "Keeps the cabin at room temperature while the sun sits low on the horizon and nearby ground stays very cold."
    parts: ["Internal water coolant loop", "External ammonia or similar loop", "Vertical radiators with dust covers", "Heaters for low-sun periods", "Thermal insulation and window shutters"]
    tech: "ISS active thermal control heritage"
    trl: 5
  - name: Power interface
    desc: "Connects the module to the M04 habitat microgrid and keeps essential loads alive if the grid drops."
    parts: ["DC-DC converter from the ±4 kVDC grid", "Internal power distribution units", "Essential-load battery", "Cable connector at the umbilical box"]
    tech: "M04 grid design; ISS power distribution heritage"
    trl: 5
risks:
  - {sev: Critical, title: "The MPH baseline is sized for 2 crew, but this plan flies 4", fix: "Add 2 fold-down sleep stations and size life support (C08.2) for 4; use the lander cabin as overflow quarters; negotiate a 4-crew outfitting option with ASI and Thales"}
  - {sev: High, title: "MPH is only in preliminary design; launch planned 2033 may slip", fix: "Keep sortie dates tied to the habitat delivery; track an inflatable or second rigid supplier as a backup"}
  - {sev: High, title: "Dust on radiators and windows degrades heat rejection (Apollo saw instruments run ~68 °F hot)", fix: "Vertical radiators, covers when crews are outside, and electrodynamic dust shields on critical surfaces (C08.3)"}
  - {sev: High, title: "Unshielded module gives little protection from radiation during sorties", fix: "Short stays; water and stowage wall storm shelter around the sleep area; burial in M09"}
  - {sev: Medium, title: "Wheels and suspension may fail while towing 15 t over rough ground", fix: "Prepared road from pad to habitat zone (M05); slow tow with two LTVs; jacks can level the module where it stops"}
  - {sev: Medium, title: "Pressure shell leak from micrometeoroid hit or seal wear", fix: "Shielded shell, leak checks during the 3-month uncrewed run, patch kit, and nitrogen make-up reserves"}
  - {sev: Medium, title: "Grid outage cuts heating and life support", fix: "Essential-load battery and load shedding; crew moves to the lander if outage exceeds battery time"}
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

## What it does

The habitat module is the crew's home on the surface. It holds a breathable atmosphere, carries the life support system (C08.2), connects to the dust lock (C08.3) and gives four people somewhere to sleep, eat, wash and work for 14–30 days.

Open Moon uses a module in the class of Thales Alenia Space's Multi-Purpose Habitation (MPH). Thales is designing it for the Italian Space Agency. It is about 3 m × 6 m, about 15 t, with a minimum 10-year life and a planned 2033 launch<sup class="r">[1](#s1)</sup>. Press reports say it has wheels for precise positioning and is planned for two astronauts on one 7–30 day mission per year<sup class="r">[2](#s2)</sup>. Thales has built many pressurised modules, including Harmony, Tranquility and the Columbus structure on the ISS, and the Cygnus pressure vessels<sup class="r">[3](#s3)</sup>.

## How it works

- **Pressure shell.** A rigid cylinder with ISS-style frames, shielding and insulation. It lands ready to use; nothing has to be inflated or assembled.
- **Mobility.** The module lands at pad 2 (M05). LTVs tow it on its own wheels to the habitat zone, where jacks level it. Towing by LTV is this plan's design choice.
- **Hatches and ports.** One hatch leads to the dust lock. A second hatch is the emergency exit. A berthing port is kept free for the M09 modules. Two small windows with covers are a design choice for crew morale and for watching EVAs.
- **Interior.** The MPH baseline is two crew<sup class="r">[2](#s2)</sup>. For four crew, this plan adds two fold-down sleep stations next to two fixed quarters, plus a galley, hygiene station, workstations and an exercise device.
- **Thermal control.** At the pole the sun stays low. Radiators are mounted vertically and kept clean. Apollo showed why: dust on radiator surfaces made one instrument run about 68 °F hotter than expected<sup class="r">[6](#s6)</sup>.
- **Power.** NASA's Glenn team estimates a habitat for four crew on 30+ day stays draws **20–50 kW**<sup class="r">[4](#s4)</sup>. The module plugs into the M04 habitat microgrid and has a battery for essential loads.

## Sizing

| Item | Value | Basis |
|---|---|---|
| Outer envelope | ~42 m³ | π × 1.5² × 6 (ESTIMATE; real habitable volume is smaller) |
| Volume per crew (4) | ~10 m³ outer | 42 ÷ 4 (ESTIMATE) |
| Landed mass | ~15 t | Thales<sup class="r">[1](#s1)</sup> |
| Mass split | shell 5 t, mobility 1.5 t, life support 2 t, thermal 1 t, power and avionics 1.5 t, outfitting 2 t, margin 2 t | ESTIMATE, sums to 15 t |
| Power | 20–50 kW | NASA GRC<sup class="r">[4](#s4)</sup> |

Ten cubic metres per person is tight. That is why stays are capped at 30 days in M08 and more modules come in M09.

## Testing and qualification

1. **Pressure tests on Earth.** Proof and leak tests of the shell, plus a burst test of a test article. As a benchmark, Sierra Space's LIFE inflatable held 77 psi before bursting, 27% above NASA's recommended level<sup class="r">[8](#s8)</sup>.
2. **Thermal vacuum test** of the complete module with radiators coated in lunar simulant.
3. **Tow test** on a regolith simulant course with LTV-class vehicles.
4. **Crew-in-the-loop fit checks** in a mock-up with four people for 14 days.
5. **On the Moon.** NASA expects habitats to arrive on cargo landers no earlier than FY2033<sup class="r">[5](#s5)</sup>. After landing and towing, the module runs uncrewed for at least 3 months with leak checks and life support running before the first crew.

## Open questions

- Will ASI and Thales offer a four-crew outfitting option, or must the plan design its own?
- How much radiation protection do the shell and stowage give? The surface dose measured by Chang'e-4 was about 1,369 µSv per day<sup class="r">[7](#s7)</sup>. NASA's OLTARIS tool could be run on the real geometry.
- Can the wheels and frames take the load of a regolith cover in M09, or does burial need a separate shell?
- What window size gives morale value without too much heat loss and dust risk?
