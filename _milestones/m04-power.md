---
id_code: M04
order: 4
title: Surface power grid
phase: 0
window: "Years 1–5"
summary: Build a hybrid power system of tall solar towers on the sunlit ridges, a fission reactor for darkness, energy storage and high-voltage cables, all routed through one power management controller (PMC) that sends power to the grid or to storage. Every habitat module and facility takes its power from the grid through its own service connection. Sized to run the oxygen plant and the first habitat.
objective: "Deliver solar peak power from NASA-class 10 kW VSAT towers, sized by the Phase 1 load budget (provisionally 100 kW; design change DD-004), and at least 20 kWe of continuous fission power from an LR-1-class reactor (design change DD-002), with every source feeding a power management controller (PMC) that routes power to the grid, to storage, or both (design changes DD-003 and DD-008), connected by a 3 kV AC, 1 kHz grid (NASA's lunar grid baseline; design change DD-001) that feeds every unit through its own service connection (design change DD-009), with every generation source within 3 km of cable run of the PMC as standard, or up to 10 km on an extended run (design change DD-014), and converting to 3 kV AC on the spot (design change DD-013), so the base never loses essential power, even during the longest polar darkness."
trl_min: 5
depends_on: [M00, M02, M03]
spec:
  - {k: "Solar", v: "N × 10 kW VSAT towers, N set by the Phase 1 load budget (provisional 10 = 100 kW) (DD-004)"}
  - {k: "Fission", v: "1 × LR-1-class reactor, 20 kWe (7.5–15 t) (DD-002)"}
  - {k: "PMC", v: "Power management controller: main switching units A/B with a cross-tie; all sources in, grid and storage out (DD-003, DD-008)"}
  - {k: "Storage", v: "~260 kWh Li-ion bank (160 kWh reactor ride-through + 100 kWh peaks), each string on a BCDU with its own BMS (DD-008) + regenerative fuel cells, ~3 MWh"}
  - {k: "Grid", v: "3 kV AC, 3-phase, 1 kHz (NASA baseline, DD-001); every source converts to it on the spot: UMIC-class low-voltage inverter + 1 kHz step-up transformer, LR-1 at its output (DD-013)"}
  - {k: "Max power run", v: "Standard ≤3 km of cable from a generation source to the PMC (DD-013); extended up to 10 km at ~10–15% loss, with receiving-end voltage regulation and a 1 kHz stability analysis per run; beyond 10 km rejected (DD-014)"}
  - {k: "Service connections", v: "One per unit (3 habitat modules + each facility): UMIC-class step-down to 120 V DC, meter, main breaker, DC panel (DD-009)"}
  - {k: "Load at end", v: "Oxygen pilot plant ~26 kW + habitat 20–50 kW"}
cost: {low: 9.8, high: 29.8, note: "about 85% of this is delivery cost; see the analysis below"}
cost_items:
  - {item: "2 × 10 kW vertical solar arrays (hardware)", low: 0.05, high: 0.15, basis: "ESTIMATE; NASA's three VSAT prototypes cost $19.4M in total [src 4]"}
  - {item: "Delivery of 10 kW arrays (~2 t, small landers)", low: 1.2, high: 2.4, basis: "2 t × $0.6–1.2M/kg (mass ESTIMATE)"}
  - {item: "8 more 10 kW VSATs, PROVISIONAL count until the Phase 1 load budget (hardware)", low: 0.2, high: 0.6, basis: "ESTIMATE; same per-tower basis as the first two (DD-004)"}
  - {item: "Delivery of 8 more VSATs (~8 t, medium landers)", low: 3.2, high: 8.0, basis: "8 × ~1 t (C04.2 ESTIMATE) × $0.4–1.0M/kg"}
  - {item: "20 kWe LR-1-class fission unit (develop, build, qualify)", low: 1.0, high: 3.0, basis: "ESTIMATE; Congress gave $250M for Fission Surface Power in FY2026 alone [src 16]"}
  - {item: "Delivery of fission unit (7.5–15 t, heavy lander)", low: 1.5, high: 9.0, basis: "No LR-1 design yet: 7.5 t (NASA 2025 40 kWe Brayton reference [src 26]) to 15 t (LR-1 mass cap [src 25]) × $0.2–0.6M/kg"}
  - {item: "PMC (main switching units A/B), BCDUs and 160 kWh reactor ride-through battery strings (hardware)", low: 0.02, high: 0.06, basis: "ESTIMATE; DD-002 and DD-003 sizing (8 h × 20 kWe)"}
  - {item: "Delivery of PMC and ride-through battery (~1 t, medium lander)", low: 0.4, high: 1.0, basis: "160 kWh ÷ 160 Wh/kg [src 1] ≈ 1 t × $0.4–1.0M/kg"}
  - {item: "Regenerative fuel cell storage, ~3 MWh (hardware)", low: 0.05, high: 0.15, basis: "ESTIMATE"}
  - {item: "Delivery of storage (~3 t, medium lander)", low: 1.2, high: 3.0, basis: "3 MWh ÷ ~500 Wh/kg ≈ 6 t at cell level; ~3 t assumes partial reuse of ISRU tanks (ESTIMATE) × $0.4–1.0M/kg"}
  - {item: "Cables, converters, switchgear, service connections (hardware)", low: 0.05, high: 0.15, basis: "ESTIMATE"}
  - {item: "Delivery of grid hardware (~2 t: ~5 km of 3 kVac cable on spools, transformers, UMIC-class service converters, switchgear)", low: 0.8, high: 2.0, basis: "NASA 2025 reference: 325 kg per 1 km main cable and spool [src 21]; UMIC target <0.55 kg/m [src 22]; rest ESTIMATE; × $0.4–1.0M/kg"}
  - {item: "Integration, testing, operations", low: 0.1, high: 0.3, basis: "ESTIMATE"}
exit_criteria:
  - "Solar peak power installed to the level set by the Phase 1 load budget (provisionally 100 kW of 10 kW VSATs), on at least two separate ridge points."
  - "Fission unit delivering at least 20 kWe continuously to the PMC for six months (DD-002)."
  - "All generated power reaches loads and storage through the PMC; it meets demand, charges storage with surplus, and feeds the grid from the battery when short, with no power dip on essential loads (DD-003)."
  - "With storage full, surplus solar is curtailed by each VSAT's array regulator and shunt on PMC command, and surplus reactor power goes to its parasitic load radiator, with no fault."
  - "Every habitat module and facility is powered through its own service connection, and opening any one main breaker leaves all the others powered (DD-009)."
  - "Essential loads (comms, heaters, life support standby) never lose power across the longest darkness period recorded at the site."
  - "Grid survives loss of any single power source without dropping essential loads."
  - "Every generation source sits within 3 km of cable run of the PMC (standard), or within 10 km on an approved extended run, and delivers 3 kV, 3-phase, 1 kHz AC from its own source-end converter (DD-013, DD-014)."
  - "Cable-laying rover has laid every source run (standard runs ≤3 km; extended runs ≤10 km, each with receiving-end voltage regulation and a passed 1 kHz stability analysis) and the distribution grid (DD-013, DD-014)."
workstreams:
  - name: Solar towers
    desc: Tall, sun-tracking arrays that see over the terrain.
    items: ["10 kW VSAT, ~10 m mast (the only tower type, DD-004)", "Number set by the Phase 1 load budget", "Spread across 2–3 ridge points, each within 3 km of cable run of the PMC (standard) or up to 10 km (extended) (DD-013, DD-014)", "At each tower: array regulator and shunt, UMIC-class inverter, 1 kHz step-up transformer to 3 kV AC (DD-013)"]
  - name: Fission power
    desc: Continuous power regardless of sunlight.
    items: ["LR-1-class 20 kWe unit (HALEU, closed Brayton, 3 kV AC); KRUSTY-class 1 kWe units for small remote loads", "Placed 1–3 km away, behind terrain, with a standard run of no more than 3 km of cable to the PMC (DD-013; extended runs up to 10 km allowed, DD-014)", "LR-1 interface: 3 kV, 3-phase, 1 kHz at the reactor output; vendor spec or frequency converter at the reactor (open, DD-013)", "KRUSTY-class units convert their DC bus to 3 kV AC at the unit (DD-013)", "Remote start after landing", "Feeds the PMC, which routes its power to the grid or storage (DD-003, DD-008)", "Excess power to its parasitic load radiator (PLR)"]
  - name: Storage
    desc: Ride through solar gaps and peaks.
    items: ["Li-ion battery bank behind the PMC: 160 kWh per 20 kWe reactor plus ~100 kWh for peaks, in several strings", "Each string on its own battery charge/discharge unit (BCDU), with its own BMS for cell management (DD-008)", "Regenerative fuel cells (320–650 Wh/kg), charged by PMC surplus", "Shares water and gas tanks with ISRU"]
  - name: Grid and cables
    desc: Move power between sources and users.
    items: ["3 kV AC, 3-phase, 1 kHz aluminium cable", "At each source: low-voltage UMIC-class inverter + 1 kHz step-up transformer; only low-voltage switches, no high-voltage DC (DD-013)", "Source runs: standard ≤3 km (DD-013); extended up to 10 km at ~10–15% loss (DD-014)", "One service connection per unit: UMIC-class step-down to 120 V DC, meter, main breaker, DC panel (DD-009)", "One base grid; no separate habitat or ISRU microgrids at the base (DD-009); remote sites such as the ice mine may run their own isolated grid (DD-016)"]
  - name: Cable laying
    desc: Robots lay cable on the surface.
    items: ["LunaGrid-Lite-style rover reels out cable", "Cable left on the surface to shed heat (NASA advises against burial); ramps at rover crossings", "Fault location by time-domain reflectometry"]
  - name: PMC and control
    desc: "Every source feeds the power management controller (PMC), which routes power to the grid, to storage, or both (DD-003, DD-008)."
    items: ["Two independent PMC main switching units (A/B) with a cross-tie", "Microgrid controller / energy management function (IEEE 2030.7 terms)", "Solar curtailment by each VSAT's array regulator and shunt; a disconnect contactor per tower", "Routing: demand first, then battery, then fuel-cell electrolyser; curtail or dump only when storage is full", "Priority load shedding", "Remote operation from Earth", "Fault isolation"]
technologies:
  - {name: "Kilopower / KRUSTY (1–10 kWe Stirling reactor)", use: "Small reactor (plan value 1 kWe) feeding the PMC", status: "KRUSTY ground test 2018: 28 h at full power, reactor rated TRL 5. No flight unit built", trl: 5, src: 5}
  - {name: "US Lunar Reactor-1 (20 kWe Brayton reactor)", use: "Main base reactor (plan value 20 kWe) feeding the PMC", status: "Draft SPARC solicitation Aug 2026: ≥20 kWe at 3 kV AC, ≥5 yr, HALEU, closed Brayton, <15 t. No award yet", trl: 4, src: 25}
  - {name: "Vertical Solar Array Technology (VSAT)", use: "10 kW-class solar towers feeding the PMC", status: "Three NASA prototype contracts (2022); deploy to ~10 m", trl: 6, src: 4}
  - {name: "Astrobotic LunaGrid-Lite", use: "Cable-laying rover and power transfer", status: "1 kW; ~500 m of cable in the 2025 design (1 km in earlier plans); passed CDR Aug 2025", trl: 6, src: 8}
  - {name: "Regenerative fuel cells", use: "Long-gap storage behind the PMC; recharges the battery", status: "NASA Glenn breadboard ran 550+ hours of simulated lunar cycles (open-loop)", trl: 5, new: true, src: 9}
  - {name: "Lunar AC power transmission (3 kVac, 1 kHz)", use: "Source lines into the PMC and the distribution grid to every service connection", status: "NASA lunar grid baseline since 2022; UMIC 1 kW module bench-tested (2023); AC cable tested in vacuum with regolith simulant (2025)", trl: 4, src: 23}
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
  - {title: "Button, NASA TM-104510: Development and testing of a source subsystem for the PMAD DC test bed (SSU, BCDU, DCSU; 160 V primary, 120 V secondary)", url: "https://ntrs.nasa.gov/api/citations/19910016888/downloads/19910016888.pdf", date: "Aug 1991"}
  - {title: "Wikipedia: Electrical system of the International Space Station", url: "https://en.wikipedia.org/wiki/Electrical_system_of_the_International_Space_Station", date: "2026"}
  - {title: "IEEE 2030.7: Standard for the Specification of Microgrid Controllers", url: "https://standards.ieee.org/ieee/2030.7/5941/", date: "2017"}
  - {title: "Wikipedia: Service drop", url: "https://en.wikipedia.org/wiki/Service_drop", date: "2026"}
  - {title: "Wikipedia: Distribution board", url: "https://en.wikipedia.org/wiki/Distribution_board", date: "2026"}
  - {title: "Austin et al., IEEE TNS: Inclusion of radiation environment variability for reliability estimates for SiC power MOSFETs (single-event burnout)", url: "https://ntrs.nasa.gov/api/citations/20205000795/downloads/2020-561-Austin-Final-Paper-TNS.pdf", date: "Jan 2020"}
  - {title: "Dugala, NASA Glenn: Stirling convertor controller development (presentation; ASC alternator voltage, current and frequency)", url: "https://ntrs.nasa.gov/api/citations/20180007412/downloads/20180007412.pdf", date: "Jul 2018"}
  - {title: "Dugala, NASA/TM-2018-219963: Stirling convertor controller development at NASA Glenn Research Center", url: "https://ntrs.nasa.gov/api/citations/20180008496/downloads/20180008496.pdf", date: "Nov 2018"}
  - {title: "Gibson et al.: NASA's Kilopower reactor development and the path to higher power missions (NTRS 20170002010)", url: "https://ntrs.nasa.gov/citations/20170002010", date: "Mar 2017"}
  - {title: "Wikipedia: Aluminium (resistivity and density)", url: "https://en.wikipedia.org/wiki/Aluminium", date: "2026"}
risks:
  - {sev: Critical, title: "Darkness: even the best ridges have shadow periods; NASA cites up to ~100 h at the pole, and 354 h is the design night for the US reactor", fix: "Fission base load + solar on multiple ridge points + storage; never rely on one source"}
  - {sev: Critical, title: "The US lunar reactor's requirements keep changing (40 → 100 → 20 kWe) and no contract has been awarded", fix: "Plan on the LR-1 minimum of 20 kWe (DD-002); size the PMC so a larger unit can be added; solar-only fallback with more storage"}
  - {sev: Critical, title: "Every watt passes through the PMC (DD-003, DD-008), so a PMC fault could cut every source off from every load", fix: "Two independent PMC main switching units (A/B), each able to carry the essential loads, with a cross-tie; battery in several strings; every source and grid output can be switched to either unit; ground-test failover before flight"}
  - {sev: High, title: "A fault inside one habitat module or facility could pull down the grid for everyone", fix: "Each unit has its own service connection with a main breaker and UMIC DC switch modules, so it can be isolated without affecting the others (DD-009)"}
  - {sev: High, title: "Delivery cost dominates: ~85% of this milestone is shipping mass", fix: "Push heavy-cargo pricing down; make cables and later solar cells from regolith (Blue Alchemist, M12)"}
  - {sev: High, title: "Dust on arrays and radiators", fix: "Vertical arrays shed dust; keep 1 km+ from landing pads; landing pads in M05"}
  - {sev: High, title: "Reactor radiation near crew", fix: "1–3 km separation, terrain or berm shielding; US draft sets ≤5 rem/yr at 1 km"}
  - {sev: High, title: "The 3 kV AC grid hardware is early: NASA has bench-tested a single 1 kW UMIC module, and an AC grid with no spinning machines is harder to keep stable", fix: "Track NASA's UMIC development; test parallel UMICs and droop control in hardware before flight; keep standard source runs to 3 km or less (DD-013), within NASA's Artemis design scale; run a 1 kHz charging and stability analysis before approving any extended run up to 10 km (DD-014)"}
  - {sev: High, title: "Power-run length constrains siting: the standard run is 3 km (DD-013); two Shackleton-ridge points about 8 km apart reach ~94% combined light, and NASA expects ISRU to need power over 3–5 km. Extended runs up to 10 km (DD-014) reach both, at ~10–15% loss and with stability not yet analysed", fix: "M00 picks a base point with every ridge point it uses within 10 km of cable run (at least one of the 8 km pair within 10 km, each run ≤10 km); use standard 3 km runs where possible; feed ISRU plants at 3–5 km by extended runs; add receiving-end voltage regulation and a 1 kHz stability analysis per extended run; PSR work beyond 10 km on the mobile power cart (PW.5) or a local source"}
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

This milestone targets about 120 kW of total capacity (provisional until the Phase 1 load budget): 100 kW of solar peak from 10 kW VSATs plus 20 kWe of fission from one LR-1-class reactor (design change DD-002). That's enough for the oxygen pilot plant (M06) and the first habitat (M08), with room to grow.

**Input to the Phase 1 load budget (crew change, DD-006).** The power design and sizing are not changed here. The base is now designed for 6 people, with up to 9 for about two weeks at each handover, in three standard 3-person habitat modules (DD-007). The figures above bracket that habitat load: NASA gives 28.05 kW for a six-person base camp<sup class="r">[10](#s10)</sup> and 20–50 kW for a four-crew habitat<sup class="r">[1](#s1)</sup>. Scaling the four-crew range linearly would give about 30–75 kW for 6 people and 45–113 kW for 9 (this plan's arithmetic, a crude upper bracket). The load budget must also cover the habitat's life support running for 9 at handovers, and the radiators and pumps that the buried modules need. Under the new phase structure (DD-005), everything built in Phase 1 must be powered before the first crew lands.

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
- **Moving target.** The US programme has changed requirements several times: 40 kWe in 2022<sup class="r">[1](#s1)</sup>, then at least 100 kWe with closed Brayton conversion in 2025<sup class="r">[12](#s12)</sup>. In 2026 it settled on "Lunar Reactor-1": at least 20 kWe, at least 5 years, HALEU fuel, under 15 t<sup class="r">[6](#s6)</sup><sup class="r">[14](#s14)</sup>. No contract has been awarded yet. Open Moon now plans on that 20 kWe minimum (see design changes DD-002, DD-003 and DD-008 below).

{% include decision-note.html id="DD-002" extra="Open Moon first planned one 40 kWe-class reactor feeding the grid directly. On 18 November 2026 it changed to KRUSTY-class (1 kWe) or LR-1-class (20 kWe) reactors. Its first rule, that reactors only charge a battery, was later widened by DD-003." %}

{% include decision-note.html id="DD-003" extra="DD-002 had the reactor charge only a battery. DD-003 widens that: every source now feeds one hub, which routes power to the grid, to storage, or both. DD-008 renamed that hub the power management controller (PMC)." %}

## How power flows: inputs, PMC, storage, outputs

{% include decision-note.html id="DD-008" extra="Until 18 November 2026 the plan called this hub the BMS. The routing rules did not change; only the names did." %}

![Diagram: fission reactors and solar towers feed the power management controller (PMC); the PMC sends power to the grid, to the batteries through their BCDUs, or to excess-power handling; the grid is fed by generation or by the battery, and the fuel cells recharge the battery; with storage full, solar is curtailed by each tower's shunt regulator and reactor surplus goes to its parasitic load radiator](/assets/tech/base-power-pmc-flow.svg)

- **Names (design change DD-008).** The whole system is the **EPS** (electrical power system): generation, storage, distribution and protection. Its routing and distribution part is **PMAD** (power management and distribution). Space Station Freedom used the same terms<sup class="r">[27](#s27)</sup>. The **power management controller (PMC)** is the part that decides where power goes. Ground grids call this a microgrid controller or energy management system (EMS)<sup class="r">[29](#s29)</sup>.
- **Inputs.** The reactor and the solar towers always send their power to the PMC. Nothing feeds a load directly.
- **The PMC decides.** Moment to moment it sends power to the grid to meet demand, to the batteries to charge, to excess-power handling, or some of each.
- **The grid has only two feeds:** generation passing through the PMC, or the battery. The regenerative fuel cells never feed the grid directly; when they discharge, they recharge the battery.
- **Default routing (plan design).**
  1. Meet grid demand, highest priority first (life support before everything else). NASA's lunar microgrid concept also has a controller that serves the highest-priority loads first<sup class="r">[1](#s1)</sup>.
  2. Charge the Li-ion battery with any surplus.
  3. With the battery full, run the fuel-cell electrolyser to fill long-term storage.
  4. With all storage full, curtail the solar towers and let the reactor dump its surplus to its parasitic load radiator (PLR). Each VSAT's array regulator shunts array strings to cut its output on PMC command, and a disconnect contactor can isolate the tower (plan design). The ISS does the same with its sequential shunt unit, which shunts array strings to hold its ~160 V DC bus<sup class="r">[27](#s27)</sup><sup class="r">[28](#s28)</sup>. LR-1 must accept any load from 0 to 100% of its output and starts up into that radiator<sup class="r">[25](#s25)</sup>. NASA's 40 kWe Stirling concept also dumped unused power into a resistor bank or radiator<sup class="r">[15](#s15)</sup>.
  5. When short: the battery feeds the grid; the fuel cells recharge the battery; as a last resort, shed loads by priority.
- **Outputs.** The grid: one 3 kV AC distribution network, like a national grid. Every habitat module and facility takes power from it through its own service connection (C04.4, design change DD-009).
- **Batteries.** Each Li-ion string connects to the PMC through its own battery charge/discharge unit (BCDU), as on the ISS<sup class="r">[28](#s28)</sup>. Each string has its own BMS, which now means only cell management: cell voltage, temperature, balancing and charge limits. It reports to the PMC (plan design).
- **Battery size (plan design).** About 260 kWh of Li-ion: 160 kWh per 20 kWe reactor, which is 8 hours at full output, about the time NASA's reference reactor takes to start up<sup class="r">[26](#s26)</sup>, plus about 100 kWh for fast peaks. At 160 Wh/kg<sup class="r">[1](#s1)</sup> that is about 1.6 t.
- **No single point of failure.** The PMC has two independent main switching units (A and B) with a cross-tie. Each can carry the essential loads, and every source and grid output can be switched to either unit.
- **KRUSTY-class units.** A 1 kWe Kilopower-type unit gives 24 kWh a day. That suits a remote comms or science node, not the habitat. No flight unit is being built.

## Service connections: every unit is a house on the grid

{% include decision-note.html id="DD-009" extra="The plan first followed NASA's 2022 layout of separate habitat and ISRU microgrids. It now has one grid and a service connection for each unit." %}

![Diagram: the 3 kV AC grid feeds three habitat modules and a water electrolysis plant, each through its own service connection: service drop, UMIC-class step-down and rectifier to 120 V DC, meter, main breaker, then a 120 V DC panel with branch circuits such as life support, lighting, galley, avionics and heaters; habitats have an optional unit inverter feeding a local AC subpanel; any one connection can be opened without affecting the others](/assets/tech/base-power-service-connection.svg)

- **The grid is the national grid.** The PMC feeds one 3 kV AC, 1 kHz distribution network (DD-001). There are no separate habitat or ISRU microgrids (plan design, DD-009).
- **Every unit is a house.** Each habitat module, and each facility, has its own service connection: a service drop from the grid, a UMIC-class converter that steps down and rectifies to 120 V DC, a meter, and a main breaker. This is the same pattern as a house on a terrestrial grid<sup class="r">[30](#s30)</sup> (plan design).
- **DC panel.** The main breaker feeds the unit's 120 V DC panel. Like a house's distribution board<sup class="r">[31](#s31)</sup>, it splits the feed into branch circuits, each with its own breaker. NASA's UMIC is built to connect 120 V DC equipment to the 3 kV AC grid<sup class="r">[22](#s22)</sup>. Space Station Freedom also converted its primary bus to 120 V DC for its users<sup class="r">[27](#s27)</sup>.
- **AC only where a unit needs it.** The grid does not supply AC to units. A unit that needs AC has its own inverter, fed from its DC panel, feeding a local AC subpanel. Each unit chooses its own inverter and AC voltage (plan design).
- **Who gets one.** Each of the 3 habitat modules (DD-007), and each facility: the regolith water-extraction plant, water electrolysis (H₂/O₂), the oxygen plant, life-support processing outside the habitats, comms nodes, rover chargers, greenhouses and the propellant depot.
- **Protection.** Any service connection can be opened without affecting the others. A fault in one unit trips its own main breaker, not the grid (plan design).

## Site layout

![Plan view, not to scale: 10 kW VSAT towers on two or three ridge points and an LR-1-class reactor 1–3 km away behind terrain, with its 36° shield shadow toward the crew, each send a 3 kV AC source line to the PMC near the habitat zone; the 3 kV AC distribution grid runs from the PMC to a service connection at each habitat module and facility; landing pads sit at least 1 km from the towers](/assets/tech/base-power-site-layout.svg)

- **3 km standard, 10 km extended.** The standard power run is 3 km of cable or less from a generation source to the PMC (plan design, DD-013). Extended runs of up to 10 km are allowed at about 10–15% loss (plan design, DD-014). That sets the size of the power site: the base, the ridge points and the reactor all fit inside a 10 km cable reach, and inside 3 km wherever possible.
- **Solar towers** stand on two or three ridge points, so that when one is in shadow another is usually lit (plan design; see M00). Each tower converts its own output to 3 kV AC and has its own source line to the PMC (DD-013). A ridge point beyond 3 km is fed by an extended run (DD-014).
- **The reactor** sits 1–3 km from the habitat zone, behind terrain, on a standard run of no more than 3 km of cable to the PMC (plan design, DD-002, DD-013). NASA's reference shield has a 36° included angle and keeps the dose below 5 rem/yr at 1 km<sup class="r">[26](#s26)</sup>, so the shield's shadow is pointed at the crew zone.
- **The PMC** sits near the habitat zone (plan design). Every source line ends there, already at 3 kV AC (DD-013). The distribution grid runs out from it to a service connection at each habitat module and facility (DD-009).
- **Landing pads** stay at least 1 km from the towers and radiators, to limit dust (plan design).
- **ISRU plants** sit within 3 km of cable run of the PMC where they can (DD-013). NASA expects ISRU to need power over 3–5 km<sup class="r">[1](#s1)</sup>, so a plant at that distance is fed by an extended run of up to 10 km (plan design, DD-014).
- **Cables** lie on the surface. NASA advises against burying them, because regolith traps heat<sup class="r">[21](#s21)</sup>.

## One-line diagram

![One-line diagram: each solar tower and the reactor send 3 kV AC over a source line to an input converter on PMC main switching unit A or B, joined by a cross-tie; Li-ion battery strings connect to each unit through BCDUs, each string with its own BMS; the fuel cells are charged from PMC surplus and discharge only into the battery, with no direct path to the grid; output converters feed the 3 kV AC distribution grid, which feeds a service connection with a 120 V DC panel at each of three habitat modules and each facility; the reactor's parasitic load radiator takes surplus and solar towers curtail on PMC command](/assets/tech/base-power-one-line.svg)

This is the plan's design, simplified to one line per 3-phase circuit. Each source converts to 3 kV AC on the spot (DD-013). Source lines are 3 km or shorter as standard, or up to 10 km as extended runs (DD-014). The source lines and the distribution grid run at 3 kV AC, NASA's lunar grid baseline<sup class="r">[23](#s23)</sup>. A UMIC-class converter in each service connection links that unit's 120 V DC panel to the 3 kV AC grid<sup class="r">[22](#s22)</sup>. The PMC buses, the converters inside it, the service connections and the battery and fuel-cell connections are plan design (DD-003, DD-008, DD-009).

## Solar towers

- **VSAT.** NASA funded three prototypes in 2022 for $19.4M in total; they deploy to about 10 m<sup class="r">[4](#s4)</sup>. Each is a 10 kW-class array<sup class="r">[20](#s20)</sup>.
- **Only 10 kW VSATs (DD-004).** The number of towers will come from the Phase 1 load budget. Until then the plan costs 10 towers (100 kW) as a provisional figure.
- **Not used: VSAT-XL.** Astrobotic's 50 kW, 34 m design<sup class="r">[7](#s7)</sup> is still a ground deployment prototype, under an SBIR Phase II contract to June 2027<sup class="r">[17](#s17)</sup><sup class="r">[18](#s18)</sup>. It is kept as an alternative only.

{% include decision-note.html id="DD-004" extra="M04 first planned two 10 kW VSATs and two 50 kW VSAT-XL towers." %}
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

## Isolated grids for remote sites (DD-016)

{% include decision-note.html id="DD-016" %}

The base runs one grid (DD-009). A remote site too far from the base for a power run can have its own isolated grid: its own generation, PMC and storage, with no tie to the base (plan design). The first case is the ice mine at the primary site, 12.7 km from the base: two 10 kW VSATs on the de Gerlache rim feed a mine PMC there, with a feeder down to the mine (M00). The base keeps its own VSATs. Each isolated grid needs its own storage and spares. The ice-mine grid stores only enough to keep its systems minimally alive while it is dark; mining stops until the VSATs are lit again (plan design). Its keep-alive load is not yet sized (open).

**Base VSATs at the primary site (DD-016, DD-017).** B1 (site 5, 8.2 km) and B2 (9.4 km) on extended runs (DD-020) give the base its hours of sunlight; B3, 2.0 km from the base on a standard run and clear of the flat patch (DD-021), adds redundancy and faster battery charging while the Sun is up (plan design; see M00).

{% include decision-note.html id="DD-017" %}

## Power runs: 3 km standard, up to 10 km extended, converted to 3 kV AC at the source

{% include decision-note.html id="DD-014" extra="DD-013 capped every run at 3 km. 3 km is now the standard, and extended runs of up to 10 km are allowed." %}

{% include decision-note.html id="DD-013" extra="Before this, links were '1–3 km' with no set maximum, and how each source reached 3 kV AC was only sketched." %}

![Diagram: three conversion chains, each built at the source. VSAT: native DC, array regulator and shunt, UMIC-class low-voltage inverter, 1 kHz step-up transformer, 3 kV AC. Kilopower: eight Stirling alternators at about 12 V AC and 100 Hz, one controller each rectifying to DC, a shared DC bus, a UMIC-class inverter, a 1 kHz transformer, 3 kV AC. LR-1: 3 kV AC at the reactor output, with the frequency matched to 1 kHz by the vendor or a converter. Every source then runs 3 km of cable or less to the PMC as standard, or up to 10 km as an extended run](/assets/tech/source-to-3kv-conversion.svg)

**The rule (plan design, DD-013 and DD-014).**
- **Standard run: 3 km or less.** Every generation source, whether a VSAT tower, the LR-1-class reactor or a KRUSTY-class unit, sits within **3 km of cable run** of the PMC where it can (DD-013).
- **Extended run: up to 10 km**, at about **10–15% transmission loss** (DD-014). Each extended run needs voltage regulation or transformer taps at the receiving end, and an analysis of 1 kHz cable charging and stability for that run before it is approved. A thicker cable can cut the loss. Runs beyond 10 km are rejected.
- Every source converts to **3 kV AC, 3-phase, 1 kHz** (DD-001) right where it stands. A low-voltage, UMIC-class inverter feeds a 1 kHz step-up transformer next to the source. NASA's UMIC is built from parallel 1 kW modules converting between 120 V DC and under 100 V AC, with transformers to 3 kV<sup class="r">[22](#s22)</sup>.
- Only low-voltage switches are used. The transformer does the step-up and has no switches. There are no high-voltage DC lines.

**Why.**
- **Switches.** NASA says a DC grid is "practically limited to 1.2-1.5 kV, due to lack of high voltage rad-hard switches"<sup class="r">[23](#s23)</sup>. Heavy ions can burn out high-voltage power MOSFETs: for 1200 V silicon carbide parts, even a 50% voltage derating "does not eliminate the risk"<sup class="r">[32](#s32)</sup>. NASA's 2025 reference notes that AC "allows use of existing flight-rated switches without stacking"<sup class="r">[26](#s26)</sup>.
- **Distance.** For 100 kW on 8 AWG cable at 1 kHz, NASA's study gives 3 kV as usable to about 600 m and 6 kV to 2.5 km, rising to 18 kV for 20 km. It adds that "long distances beyond Artemis may require dropping to lower frequency (TBD)"<sup class="r">[23](#s23)</sup>. NASA's Artemis working scale is 1–3 km links at "elevated voltage (2 kV+)"<sup class="r">[1](#s1)</sup>. So 1 kHz is kept, standard runs stay at 3 km or less, and any longer run, up to 10 km, must pass its own stability analysis (DD-014).
- **NASA does the same.** NASA's 2025 fission reference design converts its Stirling option to 350 V DC, then inverts it and steps it up with a transformer to 3 kVac<sup class="r">[26](#s26)</sup>.

**Each source (plan design, DD-013).**

| Source | Native output | Conversion at the source |
|---|---|---|
| VSAT tower | DC. The voltage is not published. For comparison, the ISS arrays hold a ~160 V DC bus<sup class="r">[27](#s27)</sup> | Array regulator and shunt (curtailment and disconnect, DD-008) → UMIC-class inverter → 1 kHz transformer → 3 kV AC |
| KRUSTY-class Kilopower | Each Stirling alternator makes single-phase AC: about 12 V RMS, 7–10 A, 102–103 Hz in its engine family, the Advanced Stirling Convertor<sup class="r">[33](#s33)</sup>. Each engine's controller rectifies to DC and holds a set voltage<sup class="r">[34](#s34)</sup>. Engines run in opposed pairs kept in step<sup class="r">[35](#s35)</sup>. The controllers feed one DC bus, at a voltage not published | DC bus → UMIC-class inverter → 1 kHz transformer → 3 kV AC. The 12 V never leaves the machine |
| LR-1-class reactor | 3 kV RMS AC is required<sup class="r">[25](#s25)</sup>. The requirements do not set the frequency; NASA's 2025 reference Brayton alternators gave 240 Vrms at 2 kHz<sup class="r">[26](#s26)</sup> | Plan interface: 3 kV, 3-phase, **1 kHz at the reactor output**. Specified to the vendor, or met with a frequency converter at the reactor end: **open** |

**Why 12 V cannot travel (this plan's arithmetic).** 1 kW at 12 V is about 83 A. For a 5% loss (50 W) on two 10 mm² aluminium conductors (26.5 nΩ·m<sup class="r">[36](#s36)</sup>), the cable can be only about 1.4 m long one-way. The same 1 kW at 3 kV, 3-phase is about 0.19 A.

**Sizing check: the worst case, 20 kW over 3 km (this plan's arithmetic).** Unity power factor; aluminium at 26.5 nΩ·m and 2,699 kg/m³<sup class="r">[36](#s36)</sup>.

| Quantity | Working | ≤3% loss | ≤5% loss |
|---|---|---|---|
| Current per phase | 20 kW ÷ (√3 × 3 kV) | 3.85 A | 3.85 A |
| Allowed loss | 3% or 5% × 20 kW | 600 W | 1,000 W |
| Resistance per conductor, 3 km | loss ÷ (3 × 3.85²) | 13.5 Ω (4.5 Ω/km) | 22.5 Ω (7.5 Ω/km) |
| Aluminium area | 26.5 nΩ·m ÷ (Ω per m) | ~5.9 mm² | ~3.5 mm² |
| Aluminium mass, 3 conductors × 3 km | area × 9 km × 2,699 kg/m³ | ~143 kg | ~86 kg |

- **At NASA's 8 AWG size** (8.37 mm², the size in NASA's grid study<sup class="r">[23](#s23)</sup>), the loss is about 2.1% (422 W) and the aluminium weighs about 203 kg (this plan's arithmetic).
- **Planning mass.** Insulation, jacket and spool make up most of a real cable. The plan uses NASA's 325 kg per 1 km main cable and spool<sup class="r">[21](#s21)</sup>: about 1 t for a 3 km run, and about 3.3 t for a 10 km extended run (this plan's arithmetic).

**Extended run: the same cable over 10 km (this plan's arithmetic, DD-014).** Same 20 kW, 3.85 A per phase and ~5.9 mm² conductor as above.

| Run on the same cable | Resistance per conductor | Resistive loss | Voltage drop |
|---|---|---|---|
| 3 km | ~13.5 Ω | ~0.6 kW (~3%) | ~3% |
| 10 km | ~45 Ω | ~2.0 kW (~10%) | ~10% |

- **On NASA's 8 AWG size** (8.37 mm²), the loss goes from about 2.1% at 3 km to about 7% at 10 km.
- **Up to ~15% is plan margin (ESTIMATE).** Two effects are not in the table. The current rises a little as the voltage sags: if the load holds 20 kW at the receiving end, the current rises to about 4.3 A and the loss to about 2.5 kW, about 11% of the power sent. And the 1 kHz reactive effects, cable charging current and inductance, are not quantified, because NASA has not published them for this cable. NASA warns that "long distances beyond Artemis may require dropping to lower frequency (TBD) to avoid stability, propagation issues"<sup class="r">[23](#s23)</sup>.
- **Thicker cable.** At constant loss, cable mass rises with the square of distance. Holding 3% at 10 km needs about 20 mm² per conductor, about 1.6 t of aluminium, against ~143 kg at 3 km.

**What it costs the plan (DD-013 and DD-014 trade-offs).**
- **Siting.** Two Shackleton-ridge points about 8 km apart reach ~94% combined light (M00). Both cannot be within 3 km of one PMC, but with extended runs both can be reached: at least one point must be within 10 km and each run must be 10 km or less (plan design, DD-014). M00 must still pick the base point.
- **ISRU.** NASA expects ISRU to need power over 3–5 km<sup class="r">[1](#s1)</sup>. Oxygen and water plants at that distance now run on grid power over extended runs (DD-014). Ice mining in shadowed craters beyond 10 km uses the mobile power cart (PBS PW.5) or a local source (open).
- **Loss.** An extended run loses about 10–15%, against ~3% on a standard run. For 20 kW over 10 km, the source must make about 2 kW more (this plan's arithmetic).
- **Mass.** Every source carries its own inverter and transformer. That mass sits in this milestone's converter and grid hardware items until the load budget sizes it; no cost line changes.

## Where the money goes

About **85%** of this milestone's cost is **delivery**, not hardware. Two things change that:

1. **Cheaper heavy cargo landers (M02).**
2. **Making power hardware on the Moon.** Blue Origin's Blue Alchemist has made solar cells and wire from regolith simulant<sup class="r">[13](#s13)</sup>. Scaling that up is part of M12.

## Step-by-step

![Seven panels showing the build-out: first 10 kW VSAT with PMC main switching unit A and a starter battery string; second VSAT; more 10 kW VSATs; regenerative fuel cells; PMC unit B with the ride-through battery and cross-tie; the LR-1-class reactor; and the closed grid that survives losing any single source](/assets/tech/base-power-build-out.svg)

1. **First landing (small lander):** a 10 kW VSAT with its own regulator, inverter and 1 kHz transformer (DD-013), PMC main switching unit A with a starter battery string, a LunaGrid-Lite-class cable rover, and the LTE kit from M03. From the first watt, power flows through the PMC, and each load gets its own service connection.
2. **Second 10 kW VSAT** on a second ridge point, within 3 km of cable run of the PMC, or up to 10 km on an extended run with receiving-end voltage regulation (DD-013, DD-014), with its own source line.
3. **More 10 kW VSATs** on medium landers, up to the number the Phase 1 load budget sets (provisionally 8 more, for 10 in total).
4. **Regenerative fuel cell storage**, sharing tanks with the M06 water plant, connected to the PMC.
5. **PMC main switching unit B and the reactor ride-through battery strings**, with the cross-tie to unit A.
6. **Fission unit on a heavy lander.** Rovers set it 1–3 km from the habitat zone behind terrain, on a standard run of no more than 3 km of cable from the PMC (DD-013; up to 10 km extended if needed, DD-014). It starts remotely into its parasitic load radiator and is then switched over to feed the PMC at 3 kV, 1 kHz.
7. **Close the grid** so it survives losing any single source.
