---
id_code: M09
order: 9
title: Permanent crew presence
phase: 3
window: "2034–2038"
summary: Move from visits to a crew that never leaves, with habitats buried under regolith for radiation protection, life support that recycles most air and water, and steady six-month rotations.
objective: "Keep at least four people on the surface continuously for four years with six-month rotations, radiation doses within career limits, life support recycling at least 90% of water and making oxygen locally, and resupply mass per person cut by at least 40% compared with open-loop operations."
trl_min: 5
depends_on: [M04, M06, M08]
spec:
  - {k: Crew, v: "4 continuous, growing to 8"}
  - {k: Rotation, v: "6 months"}
  - {k: Habitats, v: "3 modules, buried under 2–3 m of regolith (4,300–6,800 t, C09.1)"}
  - {k: "Life support", v: "≥90% water recovery; local O₂"}
  - {k: Duration, v: "4 years of continuous presence"}
cost: {low: 26.9, high: 88.6, note: "crew rotation and resupply over 4 years dominate"}
cost_items:
  - {item: "2 more habitat modules (build)", low: 2.0, high: 6.0, basis: "ESTIMATE; same class as M08"}
  - {item: "Delivery of 2 modules (~30 t, heavy cargo)", low: 6.0, high: 18.0, basis: "30 t × $0.2–0.6M/kg (ESTIMATE)"}
  - {item: "Extra excavators for burial", low: 0.2, high: 0.5, basis: "ESTIMATE; reuses M05 fleet"}
  - {item: "Life support closure upgrades", low: 0.3, high: 1.0, basis: "ESTIMATE"}
  - {item: "8 crew rotations over 4 years", low: 12.0, high: 32.8, basis: "8 × $1.5–4.1B per crewed mission (see M08)"}
  - {item: "Resupply, ~29–47 t over 4 years", low: 5.8, high: 28.2, basis: "4 crew × 1,461 days × 5–8 kg per crew-day (ESTIMATE after loop closure) × $0.2–0.6M/kg"}
  - {item: "Medical and radiation monitoring", low: 0.2, high: 0.5, basis: "ESTIMATE"}
  - {item: "Surface and ground operations, 4 years", low: 0.4, high: 1.6, basis: "ESTIMATE"}
exit_criteria:
  - "Four years of continuous crew presence with no gap."
  - "Every crew member's measured dose stays within the career limit with margin for a full career."
  - "Water recovery at least 90% averaged over a year; all breathing oxygen made on the Moon."
  - "Resupply mass per crew-day at least 40% below the open-loop baseline."
  - "No crew member needs emergency evacuation for a condition that could have been treated on site."
workstreams:
  - name: Shielded habitats
    desc: Bury the modules under regolith.
    items: ["2 more modules linked to the M08 habitat", "2 m minimum, 3 m target regolith cover (bags or sintered shell)", "Storm shelter inside for solar particle events"]
  - name: Life support closure
    desc: Recycle air and water like the ISS, then go further.
    items: ["Water recovery with brine processing", "Oxygen generation by electrolysis", "CO₂ removal (4-bed molecular sieve)", "Sabatier to recover water from CO₂"]
  - name: Local consumables
    desc: Use M06 output instead of shipping.
    items: ["Breathing oxygen from regolith", "Water from PSR ice", "Nitrogen still shipped (leak make-up)"]
  - name: Crew health
    desc: Keep people healthy for six months at 1/6 g.
    items: ["Exercise equipment", "Bone and muscle monitoring (no long-duration human data at 1/6 g)", "Telemedicine at 5–12 s delay", "Psychological support"]
  - name: Radiation
    desc: Measure, shield, warn.
    items: ["Personal dosimeters", "Solar flare warning from space weather services", "Dose budgeting for outdoor work"]
  - name: Logistics
    desc: A steady supply chain.
    items: ["Two cargo landings per year", "Standard cargo containers reused as storage", "Spares inventory managed on site"]
technologies:
  - {name: "ISS water recovery with Brine Processor", use: "Water recycling", status: "98% recovery demonstrated (2023)", trl: 9, src: 1}
  - {name: "ISS Oxygen Generation Assembly", use: "Oxygen from water", status: "Flight-proven; ~5.4 kg O₂/day for 4 crew", trl: 9, src: 2}
  - {name: "Four-bed CO₂ scrubber (4BCO2)", use: "CO₂ removal", status: "ISS flight demonstration for 4 crew-equivalents", trl: 7, src: 3}
  - {name: "Sabatier reactor", use: "Water from CO₂", status: "Flown on ISS; limits O₂ recovery to ~50% because methane is vented", trl: 8, src: 4}
  - {name: "Regolith radiation shielding", use: "Protect crew in habitats", status: "No single NASA design value; models suggest ≥2 m", trl: 4, new: true, src: 6}
sources:
  - {title: "Space.com: ISS hits 98% water recycling milestone", url: "https://www.space.com/astronaut-pee-iss-water-recycling-98-percent-milestone", date: "Jun 2023"}
  - {title: "NASA NTRS 20190030425: ISS Oxygen Generation Assembly", url: "https://ntrs.nasa.gov/api/citations/20190030425/downloads/20190030425.pdf", date: "2019"}
  - {title: "NASA NTRS ICES-2020-178: Four-Bed CO₂ Scrubber", url: "https://ntrs.nasa.gov/api/citations/20205003542/downloads/ICES-2020-178.docx", date: "2020"}
  - {title: "NASA NTRS 20190030371: Sabatier and oxygen recovery", url: "https://ntrs.nasa.gov/api/citations/20190030371/downloads/20190030371.pdf", date: "2019"}
  - {title: "Zhang et al., Science Advances: radiation dose on the lunar surface (Chang'e-4)", url: "https://doi.org/10.1126/sciadv.aaz1334", date: "Sep 2020"}
  - {title: "IAC-24 abstract: regolith shielding depth (OLTARIS)", url: "https://iafastro.directory/iac/paper/id/82864/abstract-pdf/IAC-24,D3,IP,1,x82864.brief.pdf", date: "2024"}
  - {title: "NASA OCHMO: Radiation protection technical brief (600 mSv career limit)", url: "https://www.nasa.gov/wp-content/uploads/2023/03/radiation-protection-technical-brief-ochmo.pdf", date: "2023"}
  - {title: "NASA BVAD Rev2 (NASA/TP-2015-218570): crew consumables", url: "https://ntrs.nasa.gov/citations/20210024855", date: "Feb 2022"}
  - {title: "NASA NTRS 20230016304: Lunar logistics drivers and needs", url: "https://ntrs.nasa.gov/api/citations/20230016304/downloads/Lunar%20Logistics%20Drivers%20and%20Needs.pdf", date: "2023"}
  - {title: "NASA NTRS 20230013896: Logistics rates beyond LEO (2.36 kg packaged food per crew-day)", url: "https://ntrs.nasa.gov/api/citations/20230013896/downloads/Logistics_BeyondLEO-ASCEND2023-Pres.pdf", date: "2023"}
  - {title: "NASA NTRS 20205010170: partial gravity and bone", url: "https://ntrs.nasa.gov/citations/20205010170", date: "2020"}
  - {title: "NASA NTRS: NASEM 2025 presentation (radiation data gaps)", url: "https://ntrs.nasa.gov/api/citations/20250006713/downloads/nasem_presentation%20v07012025%20vf.pdf", date: "2025"}
  - {title: "NASA NTRS: Holden et al. 2026, communication delay (5–12 s)", url: "https://ntrs.nasa.gov/api/citations/20260002621/downloads/Holden%20et%20al%202026%20-%20comm%20delay%20study%20methodsa.pdf", date: "2026"}
risks:
  - {sev: Critical, title: "Radiation: unshielded surface dose is ~0.5 Sv/yr, against a 600 mSv career limit", fix: "Bury habitats under ≥2 m regolith; limit outdoor hours; storm shelter; run NASA OLTARIS on the real design before crewing"}
  - {sev: Critical, title: "Long stays at 1/6 g have never been measured in people; NASA analysis suggests less deconditioning than in zero g, but bone and muscle effects are unquantified", fix: "Six-month rotations; exercise; measure everyone; don't extend stays until data supports it"}
  - {sev: High, title: "Life support failure far from Earth", fix: "Two independent oxygen sources (electrolysis + regolith O₂ stock); 60+ days of reserves; spares on site"}
  - {sev: High, title: "Resupply landing failure", fix: "Hold 6 months of food and spares on site; two cargo providers"}
  - {sev: Medium, title: "Psychological strain from isolation", fix: "Crew selection and training from analogs (CHAPEA, HERA); private quarters; regular contact with Earth"}
---

## The radiation problem, in numbers

- **Surface dose.** China's Chang'e-4 measured about **1,369 µSv per day** on the lunar surface<sup class="r">[5](#s5)</sup>. That's about **0.5 Sv per year** unshielded.
- **The limit.** NASA's career limit is **600 mSv**<sup class="r">[7](#s7)</sup>. One year living on the surface unprotected would use almost an entire career's allowance.
- **Shielding is mandatory.** There is **no single NASA design value** for how much regolith is enough. NASA lists dose behind thick shielding as an open data gap<sup class="r">[12](#s12)</sup>.
- **The working number.**
  - One model using NASA's OLTARIS tool found dose actually rises in the first metre of regolith because of secondary particles<sup class="r">[6](#s6)</sup>.
  - It gives about **150 mSv per 180 days at 2 m** and about **100 mSv at 3 m**, before any time spent outdoors.
  - At 2 m, four six-month rotations would use up a 600 mSv career.
  - Open Moon therefore sets **2 m as the minimum and 3 m as the target** (see C09.1), and will verify both with OLTARIS on the actual habitat geometry.

## What a person uses each day

From NASA's Baseline Values and Assumptions Document<sup class="r">[8](#s8)</sup>:

| Item | Per person per day |
|---|---|
| Oxygen consumed | 0.895 kg |
| CO₂ produced | 1.085 kg |
| Drinking water | 3.217 kg |
| Food solids (without packaging) | 0.800 kg |
| Food as shipped, packaged | 2.36 kg<sup class="r">[10](#s10)</sup> |

NASA's logistics analysis found that:

- with open-loop life support, water and gases are about **half** of all logistics mass
- closing the oxygen and water loops could largely remove the oxygen and water needs, which make up almost **40%** of the total
- packaging and carriers add another **75–150%** on top<sup class="r">[9](#s9)</sup>

That's why this milestone pairs ISS-class recycling with oxygen and water made in M06.

## Life support: what's proven

- **Water.** The ISS reached **98% water recovery** in 2023 with its brine processor<sup class="r">[1](#s1)</sup>.
- **Oxygen.** Its oxygen generator makes about 5.4 kg of O₂ a day, enough for four people<sup class="r">[2](#s2)</sup>.
- **The gap.** Today's Sabatier reactor vents methane, which caps oxygen recovery from CO₂ at about **50%**<sup class="r">[4](#s4)</sup>. On the Moon that's acceptable, because extra oxygen comes from rock (M06).

## Step-by-step

1. **Deliver two more modules** and link them to the M08 habitat.
2. **Bury them.** Excavators from M05 cover the modules with ≥2 m of regolith, held in bags or a sintered shell.
3. **Upgrade life support** to the full ISS-class closed loop, fed by M06 oxygen and water.
4. **Start continuous presence.** Four crew, six-month rotations, two cargo landings a year.
5. **Measure everything:** dose, bone density, resupply mass per day. Publish the results.
6. **Grow to eight crew** once the data supports it.
