---
id_code: M04
order: 4
title: Surface power grid
phase: 1
window: "2028–2032"
summary: Build a hybrid power grid of tall solar towers on the sunlit ridges, a fission reactor for darkness, energy storage and high-voltage cables, sized to run the oxygen plant and the first habitat.
objective: "Deliver at least 100 kW of solar peak power and at least 20 kWe of continuous fission power from an LR-1-class reactor that charges the base battery through a battery management system (Reactor > BMS > Battery > Base; design change DD-002), connected by a 3 kV AC, 1 kHz grid (NASA's lunar grid baseline; design change DD-001), so the base never loses essential power, even during the longest polar darkness."
trl_min: 5
depends_on: [M00, M02, M03]
spec:
  - {k: "Solar", v: "2 × 10 kW VSAT + 2 × 50 kW VSAT-XL towers"}
  - {k: "Fission", v: "1 × LR-1-class reactor, 20 kWe (7.5–15 t); charges batteries only (DD-002)"}
  - {k: "Storage", v: "160 kWh fission battery with BMS + regenerative fuel cells, ~3 MWh"}
  - {k: "Grid", v: "3 kV AC, 3-phase, 1 kHz; 1–3 km links (NASA baseline, DD-001)"}
  - {k: "Load at end", v: "Oxygen pilot plant ~26 kW + habitat 20–50 kW"}
cost: {low: 8.9, high: 27.5, note: "about 85% of this is delivery cost; see the analysis below"}
cost_items:
  - {item: "2 × 10 kW vertical solar arrays (hardware)", low: 0.05, high: 0.15, basis: "ESTIMATE; NASA's three VSAT prototypes cost $19.4M in total [src 4]"}
  - {item: "Delivery of 10 kW arrays (~2 t, small landers)", low: 1.2, high: 2.4, basis: "2 t × $0.6–1.2M/kg (mass ESTIMATE)"}
  - {item: "2 × 50 kW VSAT-XL towers (hardware)", low: 0.1, high: 0.3, basis: "ESTIMATE"}
  - {item: "Delivery of VSAT-XL (~6 t, medium landers)", low: 2.4, high: 6.0, basis: "6 t × $0.4–1.0M/kg (mass ESTIMATE)"}
  - {item: "20 kWe LR-1-class fission unit (develop, build, qualify)", low: 1.0, high: 3.0, basis: "ESTIMATE; Congress gave $250M for Fission Surface Power in FY2026 alone [src 16]"}
  - {item: "Delivery of fission unit (7.5–15 t, heavy lander)", low: 1.5, high: 9.0, basis: "No LR-1 design yet: 7.5 t (NASA 2025 40 kWe Brayton reference [src 26]) to 15 t (LR-1 mass cap [src 25]) × $0.2–0.6M/kg"}
  - {item: "Fission charger, BMS and 160 kWh battery in two strings (hardware)", low: 0.02, high: 0.06, basis: "ESTIMATE; DD-002 sizing (8 h × 20 kWe)"}
  - {item: "Delivery of fission battery and charger (~1 t, medium lander)", low: 0.4, high: 1.0, basis: "160 kWh ÷ 160 Wh/kg [src 1] ≈ 1 t × $0.4–1.0M/kg"}
  - {item: "Regenerative fuel cell storage, ~3 MWh (hardware)", low: 0.05, high: 0.15, basis: "ESTIMATE"}
  - {item: "Delivery of storage (~3 t, medium lander)", low: 1.2, high: 3.0, basis: "3 MWh ÷ ~500 Wh/kg ≈ 6 t at cell level; ~3 t assumes partial reuse of ISRU tanks (ESTIMATE) × $0.4–1.0M/kg"}
  - {item: "Cables, converters, switchgear (hardware)", low: 0.05, high: 0.15, basis: "ESTIMATE"}
  - {item: "Delivery of grid hardware (~2 t: ~5 km of 3 kVac cable on spools, transformers, UMIC converters, switchgear)", low: 0.8, high: 2.0, basis: "NASA 2025 reference: 325 kg per 1 km main cable and spool [src 21]; UMIC target <0.55 kg/m [src 22]; rest ESTIMATE; × $0.4–1.0M/kg"}
  - {item: "Integration, testing, operations", low: 0.1, high: 0.3, basis: "ESTIMATE"}
exit_criteria:
  - "At least 100 kW solar peak power installed on at least two separate ridge points."
  - "Fission unit charging the base battery at at least 20 kWe continuously for six months, with all fission power reaching the base through the BMS and battery (DD-002)."
  - "A full battery hands surplus fission power to the reactor's parasitic load radiator with no fault or power dip on the base."
  - "Essential loads (comms, heaters, life support standby) never lose power across the longest darkness period recorded at the site."
  - "Grid survives loss of any single power source without dropping essential loads."
  - "Cable-laying rover has laid at least 3 km of cable."
workstreams:
  - name: Solar towers
    desc: Tall, sun-tracking arrays that see over the terrain.
    items: ["10 kW VSAT, ~10 m mast", "50 kW VSAT-XL, 34 m tall", "Spread across 2–3 ridge points"]
  - name: Fission power
    desc: Continuous power regardless of sunlight.
    items: ["LR-1-class 20 kWe unit (HALEU, closed Brayton, 3 kV AC); KRUSTY-class 1 kWe units for small remote loads", "Placed 1–3 km away, behind terrain", "Remote start after landing", "Charges batteries only: Reactor > BMS > Battery > Base (DD-002)"]
  - name: Storage
    desc: Ride through solar gaps and peaks.
    items: ["160 kWh fission battery per 20 kWe reactor, two strings, with charger and BMS", "Regenerative fuel cells (320–650 Wh/kg)", "Li-ion for fast peaks (~160 Wh/kg)", "Shares water and gas tanks with ISRU"]
  - name: Grid and cables
    desc: Move power between sources and users.
    items: ["3 kV AC, 3-phase, 1 kHz aluminium cable", "Transformers plus UMIC converters at each source and user", "Separate 120 V DC habitat and ISRU microgrids"]
  - name: Cable laying
    desc: Robots lay cable on the surface.
    items: ["LunaGrid-Lite-style rover reels out cable", "Cable left on the surface to shed heat (NASA advises against burial); ramps at rover crossings", "Fault location by time-domain reflectometry"]
  - name: Control
    desc: Automatic load management.
    items: ["Priority load shedding", "Remote operation from Earth", "Fault isolation"]
technologies:
  - {name: "Kilopower / KRUSTY (1–10 kWe Stirling reactor)", use: "Small reactor (plan value 1 kWe) charging batteries via a BMS", status: "KRUSTY ground test 2018: 28 h at full power, reactor rated TRL 5. No flight unit built", trl: 5, src: 5}
  - {name: "US Lunar Reactor-1 (20 kWe Brayton reactor)", use: "Main base reactor (plan value 20 kWe) charging batteries via a BMS", status: "Draft SPARC solicitation Aug 2026: ≥20 kWe at 3 kV AC, ≥5 yr, HALEU, closed Brayton, <15 t. No award yet", trl: 4, src: 25}
  - {name: "Vertical Solar Array Technology (VSAT)", use: "10 kW-class solar towers", status: "Three NASA prototype contracts (2022); deploy to ~10 m", trl: 6, src: 4}
  - {name: "Astrobotic VSAT-XL", use: "50 kW towers", status: "NASA SBIR study award 2024; 34 m tall; Redwire ROSA arrays. Phase II follow-on Jun 2025–Jun 2027", trl: 5, new: true, src: 7}
  - {name: "Astrobotic LunaGrid-Lite", use: "Cable-laying rover and power transfer", status: "1 kW; ~500 m of cable in the 2025 design (1 km in earlier plans); passed CDR Aug 2025", trl: 6, src: 8}
  - {name: "Regenerative fuel cells", use: "Night and gap storage", status: "NASA Glenn breadboard ran 550+ hours of simulated lunar cycles (open-loop)", trl: 5, new: true, src: 9}
  - {name: "Lunar AC power transmission (3 kVac, 1 kHz)", use: "Power transmission", status: "NASA lunar grid baseline since 2022; UMIC 1 kW module bench-tested (2023); AC cable tested in vacuum with regolith simulant (2025)", trl: 4, src: 23}
sources:
  - {title: "Csank & Scott, NASA GRC: Power and Energy for the Lunar Surface", url: "https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf", date: "Apr 2022"}
  - {title: "NASA NTRS 20220002315: Lunar power transmission for fission surface power", url: "https://ntrs.nasa.gov/api/citations/20220002315/downloads/Lunar_power_transmission_concepts_FINAL.pdf", date: "2022"}
  - {title: "SpaceNews: NASA and DOE to collaborate on lunar nuclear reactor development", url: "https://spacenews.com/nasa-and-doe-to-collaborate-on-lunar-nuclear-reactor-development/", date: "Jan 2026"}
  - {title: "NASA RELEASE 22-090: Vertical Solar Array Technology awards", url: "https://www.nasa.gov/?p=142765", date: "Aug 2022"}
  - {title: "Poston et al.: Results of the KRUSTY nuclear system test", url: "https://ntrs.nasa.gov/citations/20205009351", date: "2020"}
  - {title: "NewSpace Economy: What NASA's SPARC procurement reveals about Lunar Reactor-1 (secondary)", url: "https://newspaceeconomy.ca/2026/09/01/what-does-nasas-sparc-lunar-reactor-procurement-reveal-about-lunar-reactor-1/", date: "Sep 2026"}
  - {title: "Astrobotic: awarded lunar power study with VSAT-XL", url: "https://www.astrobotic.com/astrobotic-awarded-lunar-power-study-with-vsat-xl/", date: "Aug 2024"}
  - {title: "Astrobotic: LunaGrid-Lite completes critical design review", url: "https://www.astrobotic.com/lunagrid-lite-completes-critical-design-review-flight-model-underway/", date: "2025"}
  - {title: "NASA NTRS 20260002730: Regenerative fuel cell lunar cycle testing", url: "https://ntrs.nasa.gov/citations/20260002730", date: "Apr 2026"}
  - {title: "Colozza, NASA/CR: Small lunar base camp and ISRU power", url: "https://ntrs.nasa.gov/citations/20200001622", date: "Mar 2020"}
  - {title: "Gläser et al. 2014, Icarus: Illumination at the lunar south pole", url: "https://ui.adsabs.harvard.edu/abs/2014Icar..243...78G", date: "2014"}
  - {title: "NASA: NASA seeks industry feedback on fission surface power", url: "https://www.nasa.gov/centers-and-facilities/glenn/nasa-seeks-industry-feedback-on-fission-surface-power/", date: "Aug 2025"}
  - {title: "Blue Origin: Blue Alchemist powers our lunar future", url: "https://www.blueorigin.com/news/blue-alchemist-powers-our-lunar-future/", date: "Feb 2023"}
  - {title: "Scientific American: White House plan for lunar nuclear power (NSTM-3)", url: "https://www.scientificamerican.com/article/nasa-needs-nuclear-power-for-its-moon-base-heres-the-white-house-plan-to-get-it/", date: "Apr 2026"}
  - {title: "Oleson et al., NETS 2022: deployable 40 kWe fission surface power concept (NTRS 20220004670)", url: "https://ntrs.nasa.gov/citations/20220004670", date: "2022"}
  - {title: "SpacePolicyOnline: Great news for NASA in the House-Senate FY2026 appropriations report", url: "https://spacepolicyonline.com/news/great-news-for-nasa-in-the-house-senate-fy2026-appropriations-report/", date: "Jan 2026"}
  - {title: "Astrobotic: Astrobotic developing XL solar array tech for lunar power infrastructure (SBIR Phase II)", url: "https://www.astrobotic.com/astrobotic-developing-xl-solar-array-tech-for-lunar-power-infrastructure/", date: "Jul 2025"}
  - {title: "USAspending: NASA contract 80NSSC25C0032, Phase II SBIR VSAT-XL", url: "https://www.usaspending.gov/award/CONT_AWD_80NSSC25C0032_8000_-NONE-_-NONE-", date: "Jun 2025"}
  - {title: "NASA: 2023 NASA Tipping Point selections", url: "https://www.nasa.gov/general/2023-nasa-tipping-point-selections/", date: "Jul 2023"}
  - {title: "NASA GCD annual review: Vertical Solar Array Technology (VSAT) project", url: "https://ntrs.nasa.gov/citations/20230012849", date: "Sep 2023"}
  - {title: "Mason et al., NASA/DOE: Key Design Trades for a Near-term Lunar Fission Surface Power System (NETS 2025) — 3 kVac, 1 kHz link", url: "https://ntrs.nasa.gov/citations/20250000841", date: "2025"}
  - {title: "Thomas et al., NASA GRC: A Modular AC to DC Interface Converter (UMIC) to Enable Lunar Surface Power Transmission (AIAA ASCEND)", url: "https://ntrs.nasa.gov/citations/20230013309", date: "Sep 2023"}
  - {title: "Thomas, Granger, Csank & Gardner, NASA GRC: Establishing a Lunar Surface Power Grid (trade study selecting 3 kV AC)", url: "https://ntrs.nasa.gov/citations/20220011587", date: "Aug 2022"}
  - {title: "Klopp, Thomas & Csank, NASA GRC: An Experimental Study of Losses in High Voltage AC Lunar Power Cables (SciTech 2026)", url: "https://ntrs.nasa.gov/citations/20250011012", date: "Dec 2025"}
  - {title: "NASA Glenn: SPARC Industry Day presentation (Lunar Reactor-1 requirements)", url: "https://sam.gov/api/prod/opps/v3/opportunities/resources/files/6b927f8dc6c843749a45b2c0589bf0e7/download", date: "Sep 2026"}
  - {title: "INL/NASA: Fission Surface Power Technical Maturation Webinar (2025 reference design: masses, 8 h start-up)", url: "https://inl.gov/content/uploads/2024/11/FSP-Technical-Maturation-Webinar-Final-250924-1.pdf", date: "Sep 2025"}
risks:
  - {sev: Critical, title: "Darkness: even the best ridges have shadow periods; NASA cites up to ~100 h at the pole, and 354 h is the design night for the US reactor", fix: "Fission base load + solar on multiple ridge points + storage; never rely on one source"}
  - {sev: Critical, title: "The US lunar reactor's requirements keep changing (40 → 100 → 20 kWe) and no contract has been awarded", fix: "Plan on the LR-1 minimum of 20 kWe (DD-002); size the charger and BMS so a larger unit can be added; solar-only fallback with more storage"}
  - {sev: High, title: "All fission power passes through the charger, BMS and battery (DD-002), so a fault there cuts the base off from the reactor", fix: "At least two independent battery strings, each with its own charger and BMS; a full or failed string hands surplus to the reactor's parasitic load radiator"}
  - {sev: High, title: "Delivery cost dominates: ~85% of this milestone is shipping mass", fix: "Push heavy-cargo pricing down; make cables and later solar cells from regolith (Blue Alchemist, M12)"}
  - {sev: High, title: "Dust on arrays and radiators", fix: "Vertical arrays shed dust; keep 1 km+ from landing pads; landing pads in M05"}
  - {sev: High, title: "Reactor radiation near crew", fix: "1–3 km separation, terrain or berm shielding; US draft sets ≤5 rem/yr at 1 km"}
  - {sev: High, title: "The 3 kV AC grid hardware is early: NASA has bench-tested a single 1 kW UMIC module, and an AC grid with no spinning machines is harder to keep stable", fix: "Track NASA's UMIC development; test parallel UMICs and droop control in hardware before flight; keep links short (1–3 km), where NASA says 1 kHz suits"}
  - {sev: Medium, title: "Cable damage from rovers, thermal cycling and micrometeoroids", fix: "Surface routes away from traffic with protected crossings (NASA advises against burial because regolith traps heat [src 21]); redundant routes; fault-locating electronics"}
---

## How much power does a base need?

NASA studies give concrete numbers:

| Load | Power | Source |
|---|---|---|
| Oxygen plant making 1.63 kg/h of O₂ | 25.83 kW | Colozza (NASA)<sup class="r">[10](#s10)</sup> |
| Six-person base camp | 28.05 kW | Colozza<sup class="r">[10](#s10)</sup> |
| Habitat, 4 crew, 30+ days | 20–50 kW | Csank & Scott (NASA)<sup class="r">[1](#s1)</sup> |
| ISRU at scale | 60+ kW | Csank & Scott<sup class="r">[1](#s1)</sup> |
| Growth path | 1–5 → 10–20 → 80–100 kW | Csank & Scott<sup class="r">[1](#s1)</sup> |

This milestone targets about 120 kW of total capacity: 100 kW of solar peak plus 20 kWe of fission from one LR-1-class reactor (design change DD-002). That's enough for the oxygen pilot plant (M06) and the first habitat (M08), with room to grow.

## Why not just solar, or just batteries?

- **Sunlight.** The best points on the ridge connecting Shackleton and de Gerlache craters are sunlit **92.27%** of the time at 2 m height and **95.65%** at 10 m<sup class="r">[11](#s11)</sup>. Shadow periods still happen, and NASA cites intermittent darkness of up to about 100 hours at the pole<sup class="r">[1](#s1)</sup>.
- **Storage maths** (this plan's arithmetic):
  - Keeping 30 kW of essential load alive for 100 hours takes 3 MWh.
  - Li-ion stores about 160 Wh/kg, so that's about **19 t** of batteries<sup class="r">[1](#s1)</sup>.
  - Regenerative fuel cells store 320–650 Wh/kg<sup class="r">[1](#s1)</sup>, which cuts it to about **5–9 t**.
  - Either way, that much storage is heavy to land.
- **Fission.** NASA's 2022 reference design was a 40 kWe reactor of about 10 t<sup class="r">[1](#s1)</sup>. The reactor NASA is now buying, Lunar Reactor-1, gives at least 20 kWe for at least 5 years<sup class="r">[25](#s25)</sup>. That is 480 kWh a day into the base battery, through any darkness (this plan's arithmetic). For long darkness it's the lightest answer, and it lets solar handle peaks.

## The reactor: what's real today

- **KRUSTY (2018).** For under $20 million, NASA and DOE designed, built and ran a real fission reactor with Stirling converters for 28 hours straight, at various power levels<sup class="r">[5](#s5)</sup>.
- **NASA reference design.** 40 kWe, about 10 t, four pairs of Stirling engines, sodium heat pipes, 10-year life<sup class="r">[1](#s1)</sup>.
- **Moving target.** The US programme has changed requirements several times: 40 kWe in 2022<sup class="r">[1](#s1)</sup>, then at least 100 kWe with closed Brayton conversion in 2025<sup class="r">[12](#s12)</sup>. In 2026 it settled on "Lunar Reactor-1": at least 20 kWe, at least 5 years, HALEU fuel, under 15 t<sup class="r">[6](#s6)</sup><sup class="r">[14](#s14)</sup>. No contract has been awarded yet. Open Moon now plans on that 20 kWe minimum (see design change DD-002 below).

{% include decision-note.html id="DD-002" extra="Open Moon first planned one 40 kWe-class reactor feeding the grid directly. On 18 November 2026 it changed to KRUSTY-class (1 kWe) or LR-1-class (20 kWe) reactors that only charge batteries." %}

## Reactor > BMS > Battery > Base

![Diagram: the reactor feeds a charger and battery management system, which charges the battery; the base draws only from the battery; surplus power goes to the reactor's parasitic load radiator](/assets/tech/fission-to-battery-chain.svg)

- **The reactor only charges batteries.** The 3 kV AC line from the reactor ends at a charger at the base. The charger converts it to the battery's charging voltage, and a battery management system (BMS) watches every cell and controls charging. The base's loads draw fission power only from the battery bus.
- **Why it fits.** LR-1 must accept any load from 0 to 100% of its output and starts up into a parasitic load radiator<sup class="r">[25](#s25)</sup>. So when the battery is full and the BMS stops charging, the reactor dumps the surplus as heat. Stirling reactors already work this way: NASA's 40 kWe Stirling concept dumped unused power into a resistor bank or radiator<sup class="r">[15](#s15)</sup>.
- **Battery size (plan design).** 160 kWh per 20 kWe reactor, in two strings: 8 hours at full output, about the time NASA's reference reactor takes to start up<sup class="r">[26](#s26)</sup>. At 160 Wh/kg<sup class="r">[1](#s1)</sup> that is about 1 t.
- **KRUSTY-class units.** A 1 kWe Kilopower-type unit puts 24 kWh a day into storage. That suits a remote comms or science node, not the habitat. No flight unit is being built.

## Solar towers

- **VSAT.** NASA funded three prototypes in 2022 for $19.4M in total; they deploy to about 10 m<sup class="r">[4](#s4)</sup>. Each is a 10 kW-class array<sup class="r">[20](#s20)</sup>.
- **VSAT-XL.** Astrobotic's design is 50 kW and 34 m tall, using Redwire roll-out arrays<sup class="r">[7](#s7)</sup>. NASA then gave it an SBIR Phase II contract running from June 2025 to June 2027<sup class="r">[17](#s17)</sup><sup class="r">[18](#s18)</sup>.
- **Why height matters.** Taller masts see over the horizon and catch more hours of sun<sup class="r">[11](#s11)</sup>.

## Cables

{% include decision-note.html id="DD-001" extra="Open Moon first planned a ±4 kV DC grid, following a February 2022 NASA Glenn transmission review. In November 2026 it switched to NASA's 3 kV AC baseline." %}

- **Voltage and frequency.** In its 2022 grid trade study NASA compared 1.2–6 kV DC and 3-phase AC at 60 Hz to 1 kHz. It found **1 kHz the lightest AC option** and chose **3 kV AC as the mass-optimal feasible design**<sup class="r">[23](#s23)</sup>.
- **Why not DC?** NASA says DC would be lighter above 3–4 kV, but a DC grid is "practically limited to 1.2–1.5 kV, due to lack of high voltage rad-hard switches". AC voltage can be changed with transformers, and "these facts drove team to select AC"<sup class="r">[23](#s23)</sup>.
- **NASA's reactor uses it.** NASA's 2025 fission reference design sends power 1 km over a **3 kVac, 1 kHz** link, "selected to leverage the Universal Modular Interface Converter (UMIC)". It found no mass benefit above 3 kVac at 1 km, and dropping to 1 kVac added 570 kg<sup class="r">[21](#s21)</sup>.
- **Connecting equipment.** The UMIC links 120 V DC space equipment to the 3 kV AC grid. It is built from standard 1 kW modules, with targets of over 85% efficiency and under 0.55 kg/m<sup class="r">[22](#s22)</sup>.
- **Tested with lunar dirt.** NASA tested AC cables in vacuum with regolith simulant, coiled, buried and apart, and found no major losses. The frequency did not change the results<sup class="r">[24](#s24)</sup>.
- **Why not beam power wirelessly?** Power beaming was 13–27% efficient and would need 30–60 t of extra generating capacity to make up the losses<sup class="r">[2](#s2)</sup>.
- **Cable mass.** NASA's 2025 reactor reference lists **325 kg for a 1 km main cable and spool** on the 3 kVac link<sup class="r">[21](#s21)</sup>, heavier than the ~240 kg per 3 km NASA once estimated for a 2,800 V DC cable<sup class="r">[15](#s15)</sup>. Because the reactor is heavy (about 0.25 kg per watt), the line must still be efficient: any power lost in the cable has to be made up with extra generating capacity<sup class="r">[2](#s2)</sup>.
- **Laying the cable.** Astrobotic's LunaGrid-Lite is designed to transmit 1 kW; its 2025 design lays about 500 m of cable<sup class="r">[8](#s8)</sup>. NASA's 2023 award described 1 km<sup class="r">[19](#s19)</sup>.

## Where the money goes

About **85%** of this milestone's cost is **delivery**, not hardware. Two things change that:

1. **Cheaper heavy cargo landers (M02).**
2. **Making power hardware on the Moon.** Blue Origin's Blue Alchemist has made solar cells and wire from regolith simulant<sup class="r">[13](#s13)</sup>. Scaling that up is part of M12.

## Step-by-step

1. **First landing (small lander):** a 10 kW VSAT, a LunaGrid-Lite-class cable rover, and the LTE kit from M03.
2. **Second 10 kW VSAT** on a second ridge point, with a cable link between the two.
3. **Two 50 kW VSAT-XL towers** on medium landers.
4. **Regenerative fuel cell storage**, sharing tanks with the M06 water plant.
5. **Fission battery, charger and BMS** installed at the base end of the reactor cable, in two strings.
6. **Fission unit on a heavy lander.** Rovers set it 1–3 km from the habitat zone behind terrain, then it starts remotely into its parasitic load radiator and begins charging the battery.
7. **Close the grid** so it survives losing any single source.
