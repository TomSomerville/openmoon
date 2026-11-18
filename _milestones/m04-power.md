---
id_code: M04
order: 4
title: Surface power grid
phase: 1
window: "2028–2032"
summary: Build a hybrid power system of tall solar towers on the sunlit ridges, a fission reactor for darkness, energy storage and high-voltage cables, all routed through one BMS that sends power to the grid or to storage, sized to run the oxygen plant and the first habitat.
objective: "Deliver solar peak power from NASA-class 10 kW VSAT towers, sized by the Phase 1 load budget (provisionally 100 kW; design change DD-004), and at least 20 kWe of continuous fission power from an LR-1-class reactor (design change DD-002), with every source feeding a BMS that routes power to the grid, to storage, or both (design change DD-003), connected by a 3 kV AC, 1 kHz grid (NASA's lunar grid baseline; design change DD-001), so the base never loses essential power, even during the longest polar darkness."
trl_min: 5
depends_on: [M00, M02, M03]
spec:
  - {k: "Solar", v: "N × 10 kW VSAT towers, N set by the Phase 1 load budget (provisional 10 = 100 kW) (DD-004)"}
  - {k: "Fission", v: "1 × LR-1-class reactor, 20 kWe (7.5–15 t) (DD-002)"}
  - {k: "BMS", v: "Central power routing hub, two halves (A/B); all sources in, grid and storage out (DD-003)"}
  - {k: "Storage", v: "~260 kWh Li-ion bank (160 kWh reactor ride-through + 100 kWh peaks) + regenerative fuel cells, ~3 MWh"}
  - {k: "Grid", v: "3 kV AC, 3-phase, 1 kHz; 1–3 km links (NASA baseline, DD-001)"}
  - {k: "Load at end", v: "Oxygen pilot plant ~26 kW + habitat 20–50 kW"}
cost: {low: 9.8, high: 29.8, note: "about 85% of this is delivery cost; see the analysis below"}
cost_items:
  - {item: "2 × 10 kW vertical solar arrays (hardware)", low: 0.05, high: 0.15, basis: "ESTIMATE; NASA's three VSAT prototypes cost $19.4M in total [src 4]"}
  - {item: "Delivery of 10 kW arrays (~2 t, small landers)", low: 1.2, high: 2.4, basis: "2 t × $0.6–1.2M/kg (mass ESTIMATE)"}
  - {item: "8 more 10 kW VSATs, PROVISIONAL count until the Phase 1 load budget (hardware)", low: 0.2, high: 0.6, basis: "ESTIMATE; same per-tower basis as the first two (DD-004)"}
  - {item: "Delivery of 8 more VSATs (~8 t, medium landers)", low: 3.2, high: 8.0, basis: "8 × ~1 t (C04.2 ESTIMATE) × $0.4–1.0M/kg"}
  - {item: "20 kWe LR-1-class fission unit (develop, build, qualify)", low: 1.0, high: 3.0, basis: "ESTIMATE; Congress gave $250M for Fission Surface Power in FY2026 alone [src 16]"}
  - {item: "Delivery of fission unit (7.5–15 t, heavy lander)", low: 1.5, high: 9.0, basis: "No LR-1 design yet: 7.5 t (NASA 2025 40 kWe Brayton reference [src 26]) to 15 t (LR-1 mass cap [src 25]) × $0.2–0.6M/kg"}
  - {item: "BMS hub (two halves) and 160 kWh reactor ride-through battery strings (hardware)", low: 0.02, high: 0.06, basis: "ESTIMATE; DD-002 and DD-003 sizing (8 h × 20 kWe)"}
  - {item: "Delivery of BMS hub and ride-through battery (~1 t, medium lander)", low: 0.4, high: 1.0, basis: "160 kWh ÷ 160 Wh/kg [src 1] ≈ 1 t × $0.4–1.0M/kg"}
  - {item: "Regenerative fuel cell storage, ~3 MWh (hardware)", low: 0.05, high: 0.15, basis: "ESTIMATE"}
  - {item: "Delivery of storage (~3 t, medium lander)", low: 1.2, high: 3.0, basis: "3 MWh ÷ ~500 Wh/kg ≈ 6 t at cell level; ~3 t assumes partial reuse of ISRU tanks (ESTIMATE) × $0.4–1.0M/kg"}
  - {item: "Cables, converters, switchgear (hardware)", low: 0.05, high: 0.15, basis: "ESTIMATE"}
  - {item: "Delivery of grid hardware (~2 t: ~5 km of 3 kVac cable on spools, transformers, UMIC converters, switchgear)", low: 0.8, high: 2.0, basis: "NASA 2025 reference: 325 kg per 1 km main cable and spool [src 21]; UMIC target <0.55 kg/m [src 22]; rest ESTIMATE; × $0.4–1.0M/kg"}
  - {item: "Integration, testing, operations", low: 0.1, high: 0.3, basis: "ESTIMATE"}
exit_criteria:
  - "Solar peak power installed to the level set by the Phase 1 load budget (provisionally 100 kW of 10 kW VSATs), on at least two separate ridge points."
  - "Fission unit delivering at least 20 kWe continuously to the BMS for six months (DD-002)."
  - "All generated power reaches loads and storage through the BMS; it meets demand, charges storage with surplus, and feeds the grid from the battery when short, with no power dip on essential loads (DD-003)."
  - "With storage full, surplus solar is curtailed and surplus reactor power goes to its parasitic load radiator, with no fault."
  - "Essential loads (comms, heaters, life support standby) never lose power across the longest darkness period recorded at the site."
  - "Grid survives loss of any single power source without dropping essential loads."
  - "Cable-laying rover has laid at least 3 km of cable."
workstreams:
  - name: Solar towers
    desc: Tall, sun-tracking arrays that see over the terrain.
    items: ["10 kW VSAT, ~10 m mast (the only tower type, DD-004)", "Number set by the Phase 1 load budget", "Spread across 2–3 ridge points"]
  - name: Fission power
    desc: Continuous power regardless of sunlight.
    items: ["LR-1-class 20 kWe unit (HALEU, closed Brayton, 3 kV AC); KRUSTY-class 1 kWe units for small remote loads", "Placed 1–3 km away, behind terrain", "Remote start after landing", "Feeds the BMS, which routes its power to the grid or storage (DD-003)"]
  - name: Storage
    desc: Ride through solar gaps and peaks.
    items: ["Li-ion battery bank behind the BMS: 160 kWh per 20 kWe reactor plus ~100 kWh for peaks, in several strings", "Regenerative fuel cells (320–650 Wh/kg), charged by BMS surplus", "Shares water and gas tanks with ISRU"]
  - name: Grid and cables
    desc: Move power between sources and users.
    items: ["3 kV AC, 3-phase, 1 kHz aluminium cable", "Transformers plus UMIC converters at each source and user", "Separate 120 V DC habitat and ISRU microgrids"]
  - name: Cable laying
    desc: Robots lay cable on the surface.
    items: ["LunaGrid-Lite-style rover reels out cable", "Cable left on the surface to shed heat (NASA advises against burial); ramps at rover crossings", "Fault location by time-domain reflectometry"]
  - name: BMS and control
    desc: "Every source feeds the BMS, which routes power to the grid, to storage, or both (DD-003)."
    items: ["Two independent BMS halves (A/B) with a cross-tie", "Routing: demand first, then battery, then fuel-cell electrolyser; curtail or dump only when storage is full", "Priority load shedding", "Remote operation from Earth", "Fault isolation"]
technologies:
  - {name: "Kilopower / KRUSTY (1–10 kWe Stirling reactor)", use: "Small reactor (plan value 1 kWe) feeding the BMS", status: "KRUSTY ground test 2018: 28 h at full power, reactor rated TRL 5. No flight unit built", trl: 5, src: 5}
  - {name: "US Lunar Reactor-1 (20 kWe Brayton reactor)", use: "Main base reactor (plan value 20 kWe) feeding the BMS", status: "Draft SPARC solicitation Aug 2026: ≥20 kWe at 3 kV AC, ≥5 yr, HALEU, closed Brayton, <15 t. No award yet", trl: 4, src: 25}
  - {name: "Vertical Solar Array Technology (VSAT)", use: "10 kW-class solar towers feeding the BMS", status: "Three NASA prototype contracts (2022); deploy to ~10 m", trl: 6, src: 4}
  - {name: "Astrobotic LunaGrid-Lite", use: "Cable-laying rover and power transfer", status: "1 kW; ~500 m of cable in the 2025 design (1 km in earlier plans); passed CDR Aug 2025", trl: 6, src: 8}
  - {name: "Regenerative fuel cells", use: "Long-gap storage behind the BMS; recharges the battery", status: "NASA Glenn breadboard ran 550+ hours of simulated lunar cycles (open-loop)", trl: 5, new: true, src: 9}
  - {name: "Lunar AC power transmission (3 kVac, 1 kHz)", use: "Source lines into the BMS hub and feeders to the microgrids", status: "NASA lunar grid baseline since 2022; UMIC 1 kW module bench-tested (2023); AC cable tested in vacuum with regolith simulant (2025)", trl: 4, src: 23}
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
  - {sev: Critical, title: "The US lunar reactor's requirements keep changing (40 → 100 → 20 kWe) and no contract has been awarded", fix: "Plan on the LR-1 minimum of 20 kWe (DD-002); size the BMS so a larger unit can be added; solar-only fallback with more storage"}
  - {sev: Critical, title: "Every watt passes through the BMS (DD-003), so a BMS fault could cut every source off from every load", fix: "Two independent BMS halves (A/B), each able to carry the essential loads, with a cross-tie; battery in several strings; every source and feeder can be switched to either half; ground-test failover before flight"}
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

This milestone targets about 120 kW of total capacity (provisional until the Phase 1 load budget): 100 kW of solar peak from 10 kW VSATs plus 20 kWe of fission from one LR-1-class reactor (design change DD-002). That's enough for the oxygen pilot plant (M06) and the first habitat (M08), with room to grow.

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
- **Moving target.** The US programme has changed requirements several times: 40 kWe in 2022<sup class="r">[1](#s1)</sup>, then at least 100 kWe with closed Brayton conversion in 2025<sup class="r">[12](#s12)</sup>. In 2026 it settled on "Lunar Reactor-1": at least 20 kWe, at least 5 years, HALEU fuel, under 15 t<sup class="r">[6](#s6)</sup><sup class="r">[14](#s14)</sup>. No contract has been awarded yet. Open Moon now plans on that 20 kWe minimum (see design changes DD-002 and DD-003 below).

{% include decision-note.html id="DD-002" extra="Open Moon first planned one 40 kWe-class reactor feeding the grid directly. On 18 November 2026 it changed to KRUSTY-class (1 kWe) or LR-1-class (20 kWe) reactors. Its first rule, that reactors only charge a battery, was later widened by DD-003." %}

{% include decision-note.html id="DD-003" extra="DD-002 had the reactor charge only a battery. DD-003 widens that: every source now feeds one BMS, which routes power to the grid, to storage, or both." %}

## How power flows: inputs, BMS, storage, outputs

![Diagram: fission reactors and solar towers feed the BMS; the grid is fed by generation or by the battery, and the fuel cells recharge the battery; surplus with storage full is curtailed or dumped to the reactor's parasitic load radiator](/assets/tech/base-power-bms-flow.svg)

- **Inputs.** The reactor and the solar towers always send their power to the BMS. Nothing feeds a load directly.
- **The BMS decides.** In this plan BMS means the base's central power management and routing system, including battery cell management. Moment to moment it sends power to the grid to meet demand, into storage, or some of each.
- **The grid has only two feeds:** generation passing through the BMS, or the battery. The regenerative fuel cells never feed the grid directly; when they discharge, they recharge the battery.
- **Default routing (plan design).**
  1. Meet grid demand, highest priority first (life support before everything else). NASA's lunar microgrid concept also has a controller that serves the highest-priority loads first<sup class="r">[1](#s1)</sup>.
  2. Charge the Li-ion battery with any surplus.
  3. With the battery full, run the fuel-cell electrolyser to fill long-term storage.
  4. With all storage full, curtail the solar towers and let the reactor dump its surplus to its parasitic load radiator. LR-1 must accept any load from 0 to 100% of its output and starts up into that radiator<sup class="r">[25](#s25)</sup>. NASA's 40 kWe Stirling concept also dumped unused power into a resistor bank or radiator<sup class="r">[15](#s15)</sup>.
  5. When short: the battery feeds the grid; the fuel cells recharge the battery; as a last resort, shed loads by priority.
- **Outputs.** The grid: the 3 kV AC trunk and the 120 V DC habitat and ISRU microgrids (C04.4).
- **Battery size (plan design).** About 260 kWh of Li-ion: 160 kWh per 20 kWe reactor, which is 8 hours at full output, about the time NASA's reference reactor takes to start up<sup class="r">[26](#s26)</sup>, plus about 100 kWh for fast peaks. At 160 Wh/kg<sup class="r">[1](#s1)</sup> that is about 1.6 t.
- **No single point of failure.** The BMS is split into two independent halves (A and B) with a cross-tie. Each can carry the essential loads, and every source and feeder can be switched to either half.
- **KRUSTY-class units.** A 1 kWe Kilopower-type unit gives 24 kWh a day. That suits a remote comms or science node, not the habitat. No flight unit is being built.

## Site layout

![Plan view, not to scale: 10 kW VSAT towers on two or three ridge points and an LR-1-class reactor 1–3 km away behind terrain, with its 36° shield shadow toward the crew, each send a 3 kV AC source line to the BMS hub near the habitat zone; feeders run from the BMS to the habitat and ISRU 120 V DC microgrids; landing pads sit at least 1 km from the towers](/assets/tech/base-power-site-layout.svg)

- **Solar towers** stand on two or three ridge points, so that when one is in shadow another is usually lit (plan design; see M00). Each tower has its own source line to the BMS hub.
- **The reactor** sits 1–3 km from the habitat zone, behind terrain (plan design, DD-002). NASA's reference shield has a 36° included angle and keeps the dose below 5 rem/yr at 1 km<sup class="r">[26](#s26)</sup>, so the shield's shadow is pointed at the crew zone.
- **The BMS hub** sits near the habitat zone (plan design). Every source line ends there. Feeders go out from it to the habitat and ISRU microgrids.
- **Landing pads** stay at least 1 km from the towers and radiators, to limit dust (plan design).
- **Cables** lie on the surface. NASA advises against burying them, because regolith traps heat<sup class="r">[21](#s21)</sup>.

## One-line diagram

![One-line diagram: each solar tower and the reactor send 3 kV AC over a source line to an input converter on BMS half A or half B, joined by a cross-tie; Li-ion battery strings hang off each half; the fuel cells are charged from BMS surplus and discharge only into the battery, with no direct path to the grid; output converters send 3 kV AC feeders to transformers and UMICs at the 120 V DC habitat and ISRU microgrids; the reactor's parasitic load radiator takes surplus and solar towers curtail on BMS command](/assets/tech/base-power-one-line.svg)

This is the plan's design, simplified to one line per 3-phase circuit. The source lines and feeders run at 3 kV AC, NASA's lunar grid baseline<sup class="r">[23](#s23)</sup>. UMIC converters link the 120 V DC microgrids to the 3 kV AC feeders<sup class="r">[22](#s22)</sup>. The BMS buses, the converters inside the hub and the battery and fuel-cell connections are plan design (DD-003).

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

## Where the money goes

About **85%** of this milestone's cost is **delivery**, not hardware. Two things change that:

1. **Cheaper heavy cargo landers (M02).**
2. **Making power hardware on the Moon.** Blue Origin's Blue Alchemist has made solar cells and wire from regolith simulant<sup class="r">[13](#s13)</sup>. Scaling that up is part of M12.

## Step-by-step

![Seven panels showing the build-out: first 10 kW VSAT with BMS half A and a starter battery string; second VSAT; more 10 kW VSATs; regenerative fuel cells; BMS half B with the ride-through battery and cross-tie; the LR-1-class reactor; and the closed grid that survives losing any single source](/assets/tech/base-power-build-out.svg)

1. **First landing (small lander):** a 10 kW VSAT, BMS half A with a starter battery string, a LunaGrid-Lite-class cable rover, and the LTE kit from M03. From the first watt, power flows through the BMS.
2. **Second 10 kW VSAT** on a second ridge point, with a cable link between the two.
3. **More 10 kW VSATs** on medium landers, up to the number the Phase 1 load budget sets (provisionally 8 more, for 10 in total).
4. **Regenerative fuel cell storage**, sharing tanks with the M06 water plant, connected to the BMS.
5. **BMS half B and the reactor ride-through battery strings**, with the cross-tie to half A.
6. **Fission unit on a heavy lander.** Rovers set it 1–3 km from the habitat zone behind terrain, then it starts remotely into its parasitic load radiator and is switched over to feed the BMS.
7. **Close the grid** so it survives losing any single source.
