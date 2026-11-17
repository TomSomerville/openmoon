---
id_code: M04
order: 4
title: Surface power grid
phase: 1
window: "2028–2032"
summary: Build a hybrid power grid of tall solar towers on the sunlit ridges, a fission reactor for darkness, energy storage and high-voltage cables, sized to run the oxygen plant and the first habitat.
objective: "Deliver at least 100 kW of solar peak power and at least 40 kWe of continuous fission power, connected by a high-voltage DC grid, so the base never loses essential power, even during the longest polar darkness."
trl_min: 5
depends_on: [M00, M02, M03]
spec:
  - {k: "Solar", v: "2 × 10 kW VSAT + 2 × 50 kW VSAT-XL towers"}
  - {k: "Fission", v: "1 × 40 kWe-class reactor (ref. design ~10 t)"}
  - {k: "Storage", v: "Regenerative fuel cells, ~3 MWh"}
  - {k: "Grid", v: "±4 kVDC aluminium cables, 1–3 km"}
  - {k: "Load at end", v: "Oxygen pilot plant ~26 kW + habitat 20–50 kW"}
cost: {low: 8.6, high: 22.5, note: "about 85% of this is delivery cost; see the analysis below"}
cost_items:
  - {item: "2 × 10 kW vertical solar arrays (hardware)", low: 0.05, high: 0.15, basis: "ESTIMATE; NASA's three VSAT prototypes cost $19.4M in total [src 4]"}
  - {item: "Delivery of 10 kW arrays (~2 t, small landers)", low: 1.2, high: 2.4, basis: "2 t × $0.6–1.2M/kg (mass ESTIMATE)"}
  - {item: "2 × 50 kW VSAT-XL towers (hardware)", low: 0.1, high: 0.3, basis: "ESTIMATE"}
  - {item: "Delivery of VSAT-XL (~6 t, medium landers)", low: 2.4, high: 6.0, basis: "6 t × $0.4–1.0M/kg (mass ESTIMATE)"}
  - {item: "40 kWe fission unit (develop, build, qualify)", low: 1.0, high: 3.0, basis: "ESTIMATE; Congress gave $250M for Fission Surface Power in FY2026 alone [src 16]"}
  - {item: "Delivery of fission unit (~10 t, heavy lander)", low: 2.0, high: 6.0, basis: "NASA reference design ~10 t for 40 kWe [src 1] × $0.2–0.6M/kg"}
  - {item: "Regenerative fuel cell storage, ~3 MWh (hardware)", low: 0.05, high: 0.15, basis: "ESTIMATE"}
  - {item: "Delivery of storage (~3 t, medium lander)", low: 1.2, high: 3.0, basis: "3 MWh ÷ ~500 Wh/kg ≈ 6 t at cell level; ~3 t assumes partial reuse of ISRU tanks (ESTIMATE) × $0.4–1.0M/kg"}
  - {item: "Cables, converters, switchgear (hardware)", low: 0.05, high: 0.15, basis: "ESTIMATE"}
  - {item: "Delivery of grid hardware (~1 t: ~5 km of cable, converters, switchgear)", low: 0.4, high: 1.0, basis: "NASA estimates ~240 kg of cable for 3 km at 2,800 V [src 15]; rest ESTIMATE; × $0.4–1.0M/kg"}
  - {item: "Integration, testing, operations", low: 0.1, high: 0.3, basis: "ESTIMATE"}
exit_criteria:
  - "At least 100 kW solar peak power installed on at least two separate ridge points."
  - "Fission unit delivering at least 40 kWe continuously for six months."
  - "Essential loads (comms, heaters, life support standby) never lose power across the longest darkness period recorded at the site."
  - "Grid survives loss of any single power source without dropping essential loads."
  - "Cable-laying rover has laid at least 3 km of cable."
workstreams:
  - name: Solar towers
    desc: Tall, sun-tracking arrays that see over the terrain.
    items: ["10 kW VSAT, ~10 m mast", "50 kW VSAT-XL, 34 m tall", "Spread across 2–3 ridge points"]
  - name: Fission power
    desc: Continuous power regardless of sunlight.
    items: ["HALEU fuel, closed Brayton or Stirling", "Placed 1–3 km away, behind terrain", "Remote start after landing"]
  - name: Storage
    desc: Ride through solar gaps and peaks.
    items: ["Regenerative fuel cells (320–650 Wh/kg)", "Li-ion for fast peaks (~160 Wh/kg)", "Shares water and gas tanks with ISRU"]
  - name: Grid and cables
    desc: Move power between sources and users.
    items: ["±4 kVDC aluminium cable", "DC-DC converters at each user", "Separate habitat and ISRU microgrids"]
  - name: Cable laying
    desc: Robots lay and bury cable.
    items: ["LunaGrid-Lite-style rover reels out cable", "Shallow trench or regolith cover", "Fault location by time-domain reflectometry"]
  - name: Control
    desc: Automatic load management.
    items: ["Priority load shedding", "Remote operation from Earth", "Fault isolation"]
technologies:
  - {name: "Kilopower / KRUSTY fission test", use: "Heritage for the reactor", status: "28-hour nuclear system test 2018 at various power levels; Stirling converters worked", trl: 5, src: 5}
  - {name: "US Lunar Reactor-1 (SPARC)", use: "Reactor procurement path", status: "Draft solicitation Aug 2026: ≥20 kWe, ≥5 yr, HALEU, closed Brayton, <15 t. No award yet", trl: 5, src: 6}
  - {name: "Vertical Solar Array Technology (VSAT)", use: "10 kW-class solar towers", status: "Three NASA prototype contracts (2022); deploy to ~10 m", trl: 6, src: 4}
  - {name: "Astrobotic VSAT-XL", use: "50 kW towers", status: "NASA SBIR study award 2024; 34 m tall; Redwire ROSA arrays. Phase II follow-on Jun 2025–Jun 2027", trl: 5, new: true, src: 7}
  - {name: "Astrobotic LunaGrid-Lite", use: "Cable-laying rover and power transfer", status: "1 kW; ~500 m of cable in the 2025 design (1 km in earlier plans); passed CDR Aug 2025", trl: 6, src: 8}
  - {name: "Regenerative fuel cells", use: "Night and gap storage", status: "NASA Glenn breadboard ran 550+ hours of simulated lunar cycles (open-loop)", trl: 5, new: true, src: 9}
  - {name: "High-voltage DC lunar cable", use: "Power transmission", status: "NASA Glenn analysis: ±4 kVDC Al cable best for 3 km at 95%", trl: 5, src: 2}
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
risks:
  - {sev: Critical, title: "Darkness: even the best ridges have shadow periods; NASA cites up to ~100 h at the pole, and 354 h is the design night for the US reactor", fix: "Fission base load + solar on multiple ridge points + storage; never rely on one source"}
  - {sev: Critical, title: "The US lunar reactor's requirements keep changing (40 → 100 → 20 kWe) and no contract has been awarded", fix: "Design the grid for any 20–100 kWe unit; buy from whichever programme flies first; solar-only fallback with more storage"}
  - {sev: High, title: "Delivery cost dominates: ~85% of this milestone is shipping mass", fix: "Push heavy-cargo pricing down; make cables and later solar cells from regolith (Blue Alchemist, M12)"}
  - {sev: High, title: "Dust on arrays and radiators", fix: "Vertical arrays shed dust; keep 1 km+ from landing pads; landing pads in M05"}
  - {sev: High, title: "Reactor radiation near crew", fix: "1–3 km separation, terrain or berm shielding; US draft sets ≤5 rem/yr at 1 km"}
  - {sev: Medium, title: "Cable damage from rovers, thermal cycling and micrometeoroids", fix: "Bury or cover cables; redundant routes; fault-locating electronics"}
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

This milestone targets about 140 kW of total capacity: 100 kW of solar peak plus 40 kWe of fission. That's enough for the oxygen pilot plant (M06) and the first habitat (M08), with room to grow.

## Why not just solar, or just batteries?

- **Sunlight.** The best points on the ridge connecting Shackleton and de Gerlache craters are sunlit **92.27%** of the time at 2 m height and **95.65%** at 10 m<sup class="r">[11](#s11)</sup>. Shadow periods still happen, and NASA cites intermittent darkness of up to about 100 hours at the pole<sup class="r">[1](#s1)</sup>.
- **Storage maths** (this plan's arithmetic):
  - Keeping 30 kW of essential load alive for 100 hours takes 3 MWh.
  - Li-ion stores about 160 Wh/kg, so that's about **19 t** of batteries<sup class="r">[1](#s1)</sup>.
  - Regenerative fuel cells store 320–650 Wh/kg<sup class="r">[1](#s1)</sup>, which cuts it to about **5–9 t**.
  - Either way, that much storage is heavy to land.
- **Fission.** A 40 kWe reactor of about 10 t (NASA's reference design<sup class="r">[1](#s1)</sup>) gives continuous power for 10 years. For long darkness it's the lightest answer, and it lets solar handle peaks.

## The reactor: what's real today

- **KRUSTY (2018).** NASA and DOE ran a real fission reactor with Stirling converters for 28 hours straight, at various power levels<sup class="r">[5](#s5)</sup>.
- **NASA reference design.** 40 kWe, about 10 t, four pairs of Stirling engines, sodium heat pipes, 10-year life<sup class="r">[1](#s1)</sup>.
- **Moving target.** The US programme has changed requirements several times: 40 kWe in 2022<sup class="r">[1](#s1)</sup>, then at least 100 kWe with closed Brayton conversion in 2025<sup class="r">[12](#s12)</sup>. In 2026 it settled on "Lunar Reactor-1": at least 20 kWe, at least 5 years, HALEU fuel, under 15 t<sup class="r">[6](#s6)</sup><sup class="r">[14](#s14)</sup>. No contract has been awarded yet. Open Moon's grid is designed to accept any unit from 20 to 100 kWe.

## Solar towers

- **VSAT.** NASA funded three prototypes in 2022 for $19.4M in total; they deploy to about 10 m<sup class="r">[4](#s4)</sup>. Each is a 10 kW-class array<sup class="r">[20](#s20)</sup>.
- **VSAT-XL.** Astrobotic's design is 50 kW and 34 m tall, using Redwire roll-out arrays<sup class="r">[7](#s7)</sup>. NASA then gave it an SBIR Phase II contract running from June 2025 to June 2027<sup class="r">[17](#s17)</sup><sup class="r">[18](#s18)</sup>.
- **Why height matters.** Taller masts see over the horizon and catch more hours of sun<sup class="r">[11](#s11)</sup>.

## Cables

- **Voltage choice.** NASA Glenn found that about **±4 kVDC** aluminium cable gives the lightest 3 km link at 95% efficiency<sup class="r">[2](#s2)</sup>.
- **Why not beam power wirelessly?** Power beaming was 13–27% efficient and would need 30–60 t of extra generating capacity to make up the losses<sup class="r">[2](#s2)</sup>.
- **Cable mass.** NASA estimates the cable itself at only about 240 kg for 3 km at 2,800 V<sup class="r">[15](#s15)</sup>. Because the reactor is heavy (about 0.25 kg per watt), the line must be efficient: any power lost in the cable has to be made up with extra generating capacity<sup class="r">[2](#s2)</sup>.
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
5. **Fission unit on a heavy lander.** Rovers set it 1–3 km from the habitat zone behind terrain, then it starts remotely.
6. **Close the grid** so it survives losing any single source.
