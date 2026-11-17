---
id_code: "C08.4"
milestone: M08
order: 4
title: EVA system
summary: "AxEMU-class spacesuits with their life support backpacks, the equipment to service and recharge them in the habitat, EVA tools, and the rules that keep moonwalkers within reach of safety and within their radiation budget."
trl: 6
spec:
  - {k: "Suit", v: "Axiom AxEMU class, rear entry (CDR closed Nov 2026)"}
  - {k: "EVA duration", v: "Up to 8 h (6 ± 2 h) per NASA xEVA requirement"}
  - {k: "Suit pressure", v: "4.3 psid nominal; 0.4–8.2 psid range"}
  - {k: "Cold shadow exposure", v: "At least 2 h in permanently shadowed regions"}
  - {k: "Walk-back range", v: "~2 km walking; ~10 km by LTV (~5 h walk back)"}
  - {k: "Suits on site", v: "4 + 2 spares (design choice)"}
  - {k: "Consumables per 6 h EVA", v: "~0.5 kg O₂, ~2 kg cooling water lost (ESTIMATE from BVAD)"}
  - {k: "Radiation per 6 h EVA", v: "~0.34 mSv (ESTIMATE from Chang'e-4 surface dose)"}
subcomponents:
  - name: Pressure garment
    desc: "The suit body that holds pressure, protects from cold, heat and dust, and lets the crew walk, kneel and use their hands."
    parts: ["Hard upper torso with rear-entry hatch", "Helmet with visors and lights", "Arm, leg and hip bearings", "Gloves sized per crew member", "Boots and outer thermal and dust layer"]
    tech: "Axiom AxEMU, evolved from NASA xEMU"
    trl: 6
  - name: Portable life support system (PLSS)
    desc: "The backpack that supplies oxygen, removes CO₂, and cools the crew member."
    parts: ["Primary and secondary oxygen tanks and regulators", "Rapid Cycle Amine swing bed for CO₂ and humidity", "Suit Water Membrane Evaporator for cooling", "Fan, battery and sensors", "Radio and caution-and-warning display"]
    tech: "NASA xPLSS, vacuum chamber tested 2025–2026"
    trl: 6
  - name: Servicing and recharge
    desc: "Habitat equipment that refills, recharges and checks the suits between EVAs."
    parts: ["Servicing and cooling umbilical at each suitport", "Oxygen recharge at high pressure", "Feedwater refill and water quality check", "Battery charger", "Suit leak check and data download"]
    tech: "xEMU Exploration Servicing, Performance and Checkout Equipment (xSPCE) concept"
    trl: 5
  - name: EVA tools
    desc: "Hand tools and carriers for maintenance, installation and science."
    parts: ["Powered drill and torque tools with lunar-rated bearings", "Sample bags, scoops, tongs and core tubes", "Tool carrier and tethers", "Spare connectors and cable repair kit", "Cameras and lights"]
    tech: "Apollo and ISS EVA tool heritage"
    trl: 6
  - name: EVA safety system
    desc: "Rules, sensors and planning tools that stop an EVA from going beyond what can be survived."
    parts: ["Personal radiation dosimeters with alarm", "Walk-back planner tied to suit consumables", "Navigation and tracking beacons", "Space-weather alert link to Earth", "Buddy rescue tether and stretcher"]
    tech: "NASA xEVA operations concept; this plan's dose budget"
    trl: 5
risks:
  - {sev: Critical, title: "Suit schedule may slip; NASA's Inspector General said demonstrations could slip to 2031 if testing follows historical averages", fix: "Keep sortie dates flexible; plan sortie 1 with few EVAs; track suit qualification milestones each quarter"}
  - {sev: Critical, title: "Suit or PLSS failure far from the habitat", fix: "Two-person EVAs only; walk-back limits set by remaining consumables; buddy oxygen and cooling hose; LTV carries a spare PLSS battery"}
  - {sev: High, title: "Single suit provider; Collins left the programme in 2024", fix: "Hold spare suits and parts on site; standard suit-to-habitat interfaces so another supplier could plug in later"}
  - {sev: High, title: "Solar particle event during an EVA; the suit gives little shielding", fix: "Space-weather watch from Earth; stay within time-to-shelter limits; abort and return on any warning"}
  - {sev: High, title: "Dust abrades bearings and visors; Apollo 12 suits wore more in 8 h on the Moon than training suits in 100 h", fix: "Replaceable outer layers and bearing seals; inspect after every EVA; suitports keep suits outside the cabin (C08.3)"}
  - {sev: Medium, title: "Decompression sickness with an 8.2 psia cabin and 4.3 psi suit", fix: "Follow NASA prebreathe protocols from exploration atmosphere tests; hyperbaric treatment plan; medical monitoring"}
  - {sev: Medium, title: "Cold exposure in shadow beyond the 2-hour design point", fix: "Plan routes in sunlight; time limits in shadows; heated tools and gloves"}
sources:
  - {title: "Axiom Space: completes NASA's critical design review for next-generation spacesuit", url: "https://www.axiomspace.com/release/axiom-space-completes-nasas-critical-design-review-for-next-generation-spacesuit", date: "Nov 2026"}
  - {title: "Axiom Space: testing of next-gen spacesuit underway", url: "https://www.axiomspace.com/news/axemu-spacesuit-testing", date: "Jan 2024"}
  - {title: "NASA OIG: Spacesuit development delays could impact Artemis timeline and ISS operations", url: "https://oig.nasa.gov/news/spacesuit-development-delays-could-impact-artemis-timeline-and-iss-operations/", date: "Apr 2026"}
  - {title: "Coan, NASA NTRS 20210000827: Exploration EVA integrated HITL testing and analogs", url: "https://ntrs.nasa.gov/api/citations/20210000827/downloads/Exporation%20EVA%20Testing%20and%20Analogs%2020210000827.pdf", date: "Jan 2021"}
  - {title: "NASA BVAD Rev2 (NASA/TP-2015-218570): Life Support Baseline Values and Assumptions", url: "https://ntrs.nasa.gov/citations/20210024855", date: "Feb 2022"}
  - {title: "NASA NTRS 20260002907: xEMU 11-foot vacuum chamber upgrades test results", url: "https://ntrs.nasa.gov/citations/20260002907", date: "2026"}
  - {title: "Zhang et al., Science Advances: radiation dose on the lunar surface (Chang'e-4)", url: "https://doi.org/10.1126/sciadv.aaz1334", date: "Sep 2020"}
  - {title: "NASA OCHMO: Radiation protection technical brief (600 mSv career limit)", url: "https://www.nasa.gov/wp-content/uploads/2023/03/radiation-protection-technical-brief-ochmo.pdf", date: "2023"}
  - {title: "Gaier, NASA/TM-2005-213610: Effects of lunar dust on EVA systems during Apollo", url: "https://ntrs.nasa.gov/citations/20050160460", date: "2005"}
  - {title: "NASA NTRS 20220015741: Medical lessons learned from the Exploration Atmospheres study (8.2 psia, 34% O₂)", url: "https://ntrs.nasa.gov/citations/20220015741", date: "2022"}
---

## What it does

The EVA system lets crews work outside: fix power and ISRU hardware, install M09 equipment and collect samples. It covers the suits, the habitat equipment that services them, the tools, and the safety rules.

## How it works

- **Suits.** Axiom closed the critical design review of its AxEMU suit on 13 November 2026. Assembly of the suit and its backpack should finish by early 2027, followed by thermal vacuum, vibration and life-cycle tests<sup class="r">[1](#s1)</sup>. Axiom says the suit builds on NASA's xEMU, handles the full range of south-pole temperatures, and can stay in permanently shadowed regions for at least two hours<sup class="r">[2](#s2)</sup>.
- **What NASA asks of the suit.** Rear entry; 0.4–8.2 psid with 4.3 psid nominal; EVAs of up to 8 hours (6 ± 2); walking on slopes up to 20°<sup class="r">[4](#s4)</sup>.
- **Backpack (PLSS).** NASA's reference backpack uses a Rapid Cycle Amine swing bed to remove CO₂ and a Suit Water Membrane Evaporator for cooling. Both were tested in a vacuum chamber, along with consumables recharge and vehicle-supplied cooling and power<sup class="r">[6](#s6)</sup>.
- **Servicing.** At each suitport (C08.3) an umbilical tops up oxygen, water and battery between EVAs and downloads suit data.
- **Schedule risk.** NASA's Inspector General warned in April 2026 that if testing follows historical averages, suit demonstrations would not happen until 2031. The contracts are worth up to $3.1B, and Axiom is now the only provider<sup class="r">[3](#s3)</sup>.

## Walk-back limits

NASA planning gives these ranges<sup class="r">[4](#s4)</sup>:

| Mode | Range from habitat | Limit |
|---|---|---|
| Walking | ~2 km | Suit consumables, ~2 km/h pace |
| Unpressurised rover (LTV) | ~10 km | ~5 h walk back if the rover fails |
| One pressurised rover | ~12 km | Walk back of under 8 h on a fully recharged suit |

**This plan's rule (design choice):** at every point of an EVA, the time to walk home at 2 km/h, plus a 1-hour reserve, must be less than the suit time left. M08 sorties stay within LTV range.

## Sizing (ESTIMATE)

Per crew member, from BVAD EVA rates<sup class="r">[5](#s5)</sup>:

- Oxygen used: 0.086 kg/h × 6 h = **0.52 kg**
- Cooling water lost at the poles: 0.3375 kg/h × 6 h = **2.0 kg**
- With suitports, NASA estimates O₂ losses of 0.1 kg/h plus 0.54 kg per EVA = **1.14 kg** per 6 h EVA

Per 30-day sortie, if crews make 3 two-person EVAs a week (design choice): about 13 EVAs, 26 crew-EVAs. That needs ~52 kg of cooling water and ~30 kg of suitport O₂ losses.

**Radiation budget.** Chang'e-4 measured about 1,369 µSv per day on the surface<sup class="r">[7](#s7)</sup>, or ~57 µSv/h. A 6-hour EVA gives ~0.34 mSv. About 6–7 EVAs each adds ~2.2 mSv per person. Even 30 days fully unshielded would be ~41 mSv, against NASA's 600 mSv career limit<sup class="r">[8](#s8)</sup>. The bigger danger is a solar particle event during an EVA, which is why the space-weather abort rule matters.

## Testing and qualification

1. **Suit qualification** by Axiom and NASA: thermal vacuum, vibration, life-cycle, and tests at NASA's Neutral Buoyancy Laboratory<sup class="r">[1](#s1)</sup><sup class="r">[2](#s2)</sup>.
2. **Suitport fit tests** with the flight suit and the habitat's suitports.
3. **Dust endurance.** Apollo 12 suits wore more in 8 hours on the Moon than training suits in 100 hours<sup class="r">[9](#s9)</sup>. Run bearing and visor tests with simulant for the full number of EVAs planned.
4. **Prebreathe validation** at 8.2 psia, 34% O₂. NASA's chamber trials saw several cases of decompression sickness<sup class="r">[10](#s10)</sup>.
5. **On the Moon.** Sortie 1 starts with short EVAs near the habitat, then extends range once the walk-back rule has been checked against real consumable use.

## Open questions

- Will the AxEMU suit interface match this habitat's suitports, or does it need an adapter?
- How long do suits last on the surface between depot-level maintenance on Earth?
- What prebreathe will NASA finally approve for an 8.2 psia, 34% O₂ cabin?
- How much warning of a solar particle event can crews count on?
