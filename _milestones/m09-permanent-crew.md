---
id_code: M09
order: 9
title: "Crewed base: first landing and continuous rotation"
phase: 2
window: "2035–2040"
summary: The first crew lands at a finished base and stays. Crews of three arrive every three months and each stays about six and a half months, so the base holds six people, and nine for two weeks at each handover.
objective: "Keep the base crewed without a gap for four years from the first landing, with crews of 3 arriving every 3 months, tours of about 6.5 months and 2-week handovers (6 people in steady state, 9 at handover peaks), radiation doses within career limits, life support recycling at least 90% of water and making oxygen locally, and resupply mass per person cut by at least 40% compared with open-loop operations."
trl_min: 5
depends_on: [M04, M06, M08]
spec:
  - {k: Crew, v: "6 resident; up to 9 for ~2 weeks at each handover (DD-006)"}
  - {k: "Crew size", v: "3 per landing"}
  - {k: Rotation, v: "New crew every 3 months; ~6.5-month tours; 2-week handover overlap"}
  - {k: "Crew landings", v: "4 arrivals and 4 departures a year (this plan's arithmetic)"}
  - {k: Habitats, v: "3 standard 3-person modules, connected and buried before the first landing, each with its own service connection and 120 V DC panel (M08, DD-007, DD-009)"}
  - {k: "Life support", v: "≥90% water recovery; local O₂"}
  - {k: Duration, v: "4 years of continuous presence"}
cost: {low: 33.7, high: 111.5, note: "16 crew rotations and resupply over 4 years dominate"}
cost_items:
  - {item: "16 crewed missions over 4 years (4 a year, crews of 3)", low: 24.0, high: 65.6, basis: "16 × $1.5–4.1B per crewed mission. High: $4.1B per SLS/Orion launch (OIG) [src 17]; low assumes commercial crew transport at ~$1.5B per mission (ESTIMATE). Was 8 rotations, $12.0–32.8B (DD-006)"}
  - {item: "Resupply, ~46–73 t over 4 years", low: 9.1, high: 43.8, basis: "~9,130 crew-days (this plan's arithmetic: 3 people for the first 3 months, then 6, plus 9 for 2 weeks every 3 months) × 5–8 kg per crew-day (ESTIMATE after loop closure) × $0.2–0.6M/kg. Was 4 crew × 1,461 days, $5.8–28.2B"}
  - {item: "Medical and radiation monitoring", low: 0.2, high: 0.5, basis: "ESTIMATE"}
  - {item: "Surface and ground operations, 4 years", low: 0.4, high: 1.6, basis: "ESTIMATE"}
exit_criteria:
  - "Four years of continuous crew presence with no gap, starting with the first landing."
  - "Every crew arrives and leaves on the 3-month cadence, with a 2-week handover, or the plan records why not."
  - "Every crew member's measured dose stays within the career limit with margin for a full career."
  - "Water recovery at least 90% averaged over a year; all breathing oxygen made on the Moon."
  - "Resupply mass per crew-day at least 40% below the open-loop baseline."
  - "No crew member needs emergency evacuation for a condition that could have been treated on site."
workstreams:
  - name: Crew rotation
    desc: ISS-style staggered crews (DD-006).
    items: ["Crews of 3, a new crew every 3 months", "~6.5-month tours", "2-week handover between outgoing and incoming crews", "Each crew's lander kept ready as its way home"]
  - name: Living in the base
    desc: Use the base built in Phase 1 (M08).
    items: ["9 beds in 3 modules: 6 resident, 3 for handovers", "Storm shelter for 9 (C09.2)", "Medical bay (C09.3)"]
  - name: Local consumables
    desc: Use M06 output instead of shipping.
    items: ["Breathing oxygen from regolith", "Water from PSR ice", "Nitrogen still shipped (leak make-up)"]
  - name: Crew health
    desc: Keep people healthy for 6.5 months at 1/6 g.
    items: ["Exercise equipment", "Bone and muscle monitoring (no long-duration human data at 1/6 g)", "Telemedicine at 5–12 s delay", "Psychological support"]
  - name: Radiation
    desc: Measure, shield, warn.
    items: ["Personal dosimeters", "Solar flare warning from space weather services", "Dose budgeting per tour and for outdoor work"]
  - name: Logistics
    desc: A steady supply chain.
    items: ["Two cargo landings per year", "Food and spares also carried on crew landings", "Standard cargo containers reused as storage", "Spares inventory managed on site"]
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
  - {title: "ESA: International Space Station doubles crew to six (three join three; rotation of three of the six due in October)", url: "https://www.esa.int/Science_Exploration/Human_and_Robotic_Exploration/OasISS_Mission/International_Space_Station_doubles_crew_to_six2", date: "May 2009"}
  - {title: "NASA: What you need to know about NASA's SpaceX Crew-11 mission (short handover period with Crew-10)", url: "https://www.nasa.gov/missions/station/commercial-crew/what-you-need-to-know-about-nasas-spacex-crew-11-mission/", date: "Jul 2025"}
  - {title: "NASA: International Space Station facts and figures (crew of seven; more aboard during a handover)", url: "https://www.nasa.gov/international-space-station/space-station-facts-and-figures/", date: "2026"}
  - {title: "NASA OIG IG-22-003: NASA's management of the Artemis missions ($4.1B per launch)", url: "https://www.oversight.gov/sites/default/files/oig-reports/NASA/Final-Report-IG-22-003-NASAs-Management-Artemis-Missions.pdf", date: "Nov 2021"}
  - {title: "NASA: NASA Unveils Initiatives to Achieve America's National Space Policy (crewed landing every six months after Artemis V)", url: "https://www.nasa.gov/news-release/nasa-unveils-initiatives-to-achieve-americas-national-space-policy/", date: "Mar 2026"}
risks:
  - {sev: Critical, title: "Radiation: unshielded surface dose is ~0.5 Sv/yr, against a 600 mSv career limit", fix: "Habitats buried under ≥2 m before the first landing (M08); limit outdoor hours; storm shelter; cap each person's number of tours"}
  - {sev: Critical, title: "Four crewed landings and four departures a year is twice NASA's planned rate of one crewed landing every six months after Artemis V", fix: "Book two crew transport providers; allow a tour to stretch by up to one cycle (3 months) if a landing slips; never leave the base with fewer than 3"}
  - {sev: Critical, title: "Long stays at 1/6 g have never been measured in people; NASA analysis suggests less deconditioning than in zero g, but bone and muscle effects are unquantified", fix: "6.5-month tours; exercise; measure everyone; don't extend tours until data supports it"}
  - {sev: High, title: "Each crew's lander must wait on the surface about 6.5 months, and up to three may be parked at once; no crewed lander has a published stay that long", fix: "Make lander surface life a transport requirement (M02); power and shade the parked landers, each from its own service connection on the grid (plan design, DD-009); keep a rescue option"}
  - {sev: High, title: "9 people for 2 weeks uses every bed and pushes life support to its peak", fix: "Size life support and the storm shelter for 9 (C08.2, C09.2); shorten the handover if a module is out of service"}
  - {sev: High, title: "Life support failure far from Earth", fix: "Two independent oxygen sources (electrolysis + regolith O₂ stock); 60+ days of reserves; spares on site"}
  - {sev: High, title: "Resupply landing failure", fix: "Hold 6 months of food and spares on site; two cargo providers; extra food on every crew landing"}
  - {sev: High, title: "Buried habitats cannot shed heat: regolith is a near-perfect insulator (~0.003–0.013 W/m·K), so the cover passes well under 1% of the habitat load", fix: "Pumped loops to surface radiators sized for full load (installed in M08), with two independent loops (see C09.1)"}
  - {sev: Medium, title: "Psychological strain from isolation", fix: "Crew selection and training from analogs (CHAPEA, HERA); private quarters; regular contact with Earth; crews overlap so no one arrives to an empty base"}
---

{% include decision-note.html id="DD-006" extra="Before, M09 kept 4 people in six-month rotations, growing to 8. Now crews of 3 land every 3 months and stay about 6.5 months: 6 people in steady state and 9 for about two weeks at each handover." %}

{% include decision-note.html id="DD-005" extra="This milestone used to follow a phase of short crewed sorties. Now the first crew lands at a finished, buried base and stays, and that landing starts Phase 2." %}

## How the rotation works

The plan copies the International Space Station's staggered rotation. When the ISS first went to six people in 2009, three new crew members joined the three already aboard for six months, and "a rotation of three of the six crewmembers" was due a few months later<sup class="r">[14](#s14)</sup>. NASA crews still hold a short handover with the crew they replace<sup class="r">[15](#s15)</sup>, and NASA says that sometimes more people are aboard the station during a crew handover<sup class="r">[16](#s16)</sup>.

The Open Moon sequence (plan design, DD-006):

1. **Crew 1 lands.** 3 people on base.
2. **Crew 2 lands 3 months later.** 6 people.
3. **Crew 3 lands 3 months after that.** 9 people for 2 weeks while crew 1 hands over.
4. **Crew 1 leaves** 2 weeks after crew 3 arrives. Back to 6.
5. **And so on.** Every 3 months one crew lands; 2 weeks later the oldest crew leaves.

![Crew rotation timeline over 18 months: crews 1 to 6 shown as bars, each of 3 people, each starting 3 months after the last and lasting about 6.5 months, so each overlaps the next-but-one crew by 2 weeks. A headcount strip along the bottom reads 3 for the first 3 months, then 6, rising to 9 for 2 weeks at each handover at months 6, 9, 12 and 15.](/assets/tech/crew-rotation-timeline.svg)

**This plan's arithmetic.**

- **Tour length.** Two 3-month gaps plus a 2-week handover: 3 + 3 + 0.5 = **6.5 months**, about 198 days.
- **Landings.** 12 months ÷ 3 months = **4 crew arrivals a year**, and in steady state **4 departures a year**. Over 4 years that is 16 crewed missions.
- **Headcount.** 3 people for the first 3 months, then **6**, and **9** for about 2 weeks every 3 months. The steady-state average is 6 + 3 × 0.5 ÷ 3 = **6.5 people**.
- **Crew-days.** Over 4 years, about **9,130 crew-days**, against 5,844 in the old 4-person plan.
- **The ISS comparison.** ISS handovers last days<sup class="r">[15](#s15)</sup>; this plan's 2 weeks is longer, to pass on hands-on surface work at 1/6 g.

## The radiation problem, in numbers

- **Surface dose.** China's Chang'e-4 measured about **1,369 µSv per day** on the lunar surface<sup class="r">[5](#s5)</sup>. That's about **0.5 Sv per year** unshielded.
- **The limit.** NASA's career limit is **600 mSv**<sup class="r">[7](#s7)</sup>. One year living on the surface unprotected would use almost an entire career's allowance.
- **Shielding is mandatory.** There is **no single NASA design value** for how much regolith is enough. NASA lists dose behind thick shielding as an open data gap<sup class="r">[12](#s12)</sup>.
- **The working number.**
  - One model using NASA's OLTARIS tool found dose actually rises in the first metre of regolith because of secondary particles<sup class="r">[6](#s6)</sup>.
  - It gives about **150 mSv per 180 days at 2 m** and about **100 mSv at 3 m**, before any time spent outdoors.
  - **Per 6.5-month tour** (198 days, this plan's arithmetic): about **165 mSv at 2 m** and **110 mSv at 3 m**, or about **271 mSv** unshielded.
  - Within 600 mSv, one person could fly about **3.6 tours at 2 m** or **5.5 tours at 3 m**, before EVA dose (this plan's arithmetic).
  - Open Moon therefore sets **2 m as the minimum and 3 m as the target** over the sleeping quarters (see C09.1), finished before the first crew lands (M08), and will verify both with OLTARIS on the actual habitat geometry.

## What a person uses each day

From NASA's Baseline Values and Assumptions Document<sup class="r">[8](#s8)</sup>, with this plan's multiplication for 6 and 9 people:

| Item | Per person per day | 6 people | 9 people |
|---|---|---|---|
| Oxygen consumed | 0.895 kg | 5.37 kg | 8.06 kg |
| CO₂ produced | 1.085 kg | 6.51 kg | 9.77 kg |
| Drinking water | 3.217 kg | 19.3 kg | 29.0 kg |
| Food solids (without packaging) | 0.800 kg | 4.8 kg | 7.2 kg |
| Food as shipped, packaged | 2.36 kg<sup class="r">[10](#s10)</sup> | 14.2 kg | 21.2 kg |

NASA's logistics analysis found that:

- with open-loop life support, water and gases are about **half** of all logistics mass
- closing the oxygen and water loops could largely remove the oxygen and water needs, which make up almost **40%** of the total
- packaging and carriers add another **75–150%** on top<sup class="r">[9](#s9)</sup>

That's why this milestone pairs ISS-class recycling with oxygen and water made in M06.

## Life support: what's proven

- **Water.** The ISS reached **98% water recovery** in 2023 with its brine processor<sup class="r">[1](#s1)</sup>.
- **Oxygen.** Its oxygen generator makes about 5.4 kg of O₂ a day, enough for four people<sup class="r">[2](#s2)</sup>. Six people need 5.37 kg a day and nine need 8.06 kg (BVAD<sup class="r">[8](#s8)</sup>), so the base carries more than one generator (C08.2).
- **The gap.** Today's Sabatier reactor vents methane, which caps oxygen recovery from CO₂ at about **50%**<sup class="r">[4](#s4)</sup>. On the Moon that's acceptable, because extra oxygen comes from rock (M06).

## Why crew transport dominates the cost

- **Upper bound.** NASA's Inspector General put each SLS/Orion launch at about **$4.1B**<sup class="r">[17](#s17)</sup>. That figure doesn't include the lander.
- **Lower bound.** This plan assumes commercial crew transport eventually costs about $1.5B per mission, but that is an **estimate, not a published price**.
- **Cadence.** NASA plans a crewed landing every six months after Artemis V<sup class="r">[18](#s18)</sup>. This plan needs one every three months, so it doubles both NASA's planned rate and this plan's old cost line: 16 missions, **$24.0–65.6B**, against 8 missions and $12.0–32.8B before.
- **Total.** $26.9–88.6B before (with modules and burial, now moved to M08), **$33.7–111.5B** now.

## Step-by-step

1. **Confirm the base is ready.** M08 exit criteria met: modules connected and buried, life support and storm shelter checked for 9.
2. **Crew 1 lands** (3 people) and commissions the base with Earth support.
3. **Crew 2 lands** 3 months later. The base reaches its design crew of 6.
4. **First handover.** Crew 3 lands at month 6; crew 1 hands over for 2 weeks and leaves.
5. **Keep the cadence.** A crew lands every 3 months; two cargo landings a year bring the rest.
6. **Measure everything:** dose per tour, bone density, resupply mass per day. Publish the results.
