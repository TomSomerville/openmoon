---
id_code: M10
order: 10
title: Growing food
phase: 4
window: "2035–2041"
summary: Grow a growing share of the crew's food in buried, LED-lit greenhouses, starting with fresh vegetables and working toward most calories.
objective: "Produce at least 50% of crew calories on the Moon for a crew of eight, in shielded greenhouse modules using hydroponics and LED lighting, with plant waste recycled into the life support loop."
trl_min: 5
depends_on: [M04, M06, M09]
spec:
  - {k: Approach, v: "Hydroponic / aeroponic crops under LEDs in buried modules"}
  - {k: Crops, v: "Leafy greens first; then potatoes, wheat, soy, peppers"}
  - {k: Target, v: "≥50% of calories for 8 crew"}
  - {k: Food need, v: "12.8 MJ and 0.8 kg food solids per person per day"}
  - {k: "Canopy and power", v: "~261 m² growing area, ~61 kW (C10.1 ESTIMATE from BVAD and LED data)"}
cost: {low: 6.35, high: 21.35, note: "greenhouse modules, lighting power, and research"}
cost_items:
  - {item: "Greenhouse modules (build)", low: 0.5, high: 1.5, basis: "ESTIMATE"}
  - {item: "Delivery of greenhouse modules (~17–21 t, heavy cargo)", low: 3.4, high: 12.6, basis: "17–21 t (C10.1 ESTIMATE) × $0.2–0.6M/kg"}
  - {item: "Extra ~60 kW for lighting: one more fission unit (build + ~10 t delivery)", low: 2.25, high: 6.75, basis: "C10.1 sizing (~61 kW); build $0.25–0.75B ESTIMATE + 10 t × $0.2–0.6M/kg"}
  - {item: "Crop research and ground analog", low: 0.2, high: 0.5, basis: "ESTIMATE"}
exit_criteria:
  - "Fresh vegetables available to every crew member every week."
  - "At least 50% of crew calories produced locally, averaged over a year."
  - "Inedible plant mass composted or processed and returned to the loop."
  - "No crop failure causes a food shortage (12 months of stored food on site)."
workstreams:
  - name: Greenhouse modules
    desc: Buried, shielded growing space.
    items: ["Pressurised modules under regolith", "LED lighting tuned per crop", "Separate atmosphere loop"]
  - name: Crops
    desc: Start easy, then scale to staples.
    items: ["Lettuce, kale, mizuna (proven on ISS)", "Peppers (grown on ISS 2021)", "Potatoes, wheat, soy for calories"]
  - name: Growing medium
    desc: Hydroponics first; treated regolith later.
    items: ["Hydroponic and aeroponic racks", "Regolith only after treatment (plants were stunted in raw Apollo soil)"]
  - name: Waste and nutrient loop
    desc: Recycle everything.
    items: ["Composting or bioreactor for plant waste", "Nutrient recovery from wastewater", "CO₂ from crew feeds plants"]
  - name: Food safety and variety
    desc: Keep people fed and healthy.
    items: ["12-month stored-food reserve", "Microbial monitoring", "Menu variety for morale"]
technologies:
  - {name: "NASA Veggie", use: "Leafy greens", status: "Grown lettuces, cabbage, mizuna, kale on ISS", trl: 9, src: 1}
  - {name: "NASA Advanced Plant Habitat", use: "Controlled growth of fruiting crops", status: "Grew chile peppers on ISS, first harvest Oct 2021", trl: 9, src: 2}
  - {name: "Yuegong-1 (Lunar Palace 1) bioregenerative system", use: "Closed-loop life support with crops", status: "370 days with 8 crew in rotation (2017–18); 98.2% material closure on the ground", trl: 6, src: 3}
  - {name: "ESA MELiSSA", use: "Closed-loop ecosystem research", status: "Pilot plant operating; compartments tested individually", trl: 4, new: true, src: 4}
  - {name: "Interstellar Lab NUCLEUS", use: "Compact food production", status: "Won NASA Deep Space Food Challenge grand prize 2024", trl: 5, src: 5}
sources:
  - {title: "NASA: Science in space, plant science (Veggie)", url: "https://www.nasa.gov/missions/station/iss-research/science-in-space-week-of-july-10-2023-plant-science/", date: "Jul 2023"}
  - {title: "NASA: Houston, we have a pepper", url: "https://www.nasa.gov/centers-and-facilities/kennedy/houston-we-have-a-pepper/", date: "2021"}
  - {title: "Lunar Palace 1 (Lunar Palace 365 mission), Wikipedia", url: "https://en.wikipedia.org/wiki/Lunar_Palace_1", date: "accessed Nov 2026"}
  - {title: "MELiSSA, Wikipedia", url: "https://en.wikipedia.org/wiki/MELiSSA", date: "accessed Nov 2026"}
  - {title: "NASA: NASA awards $1.25 million to three teams at Deep Space Food finale", url: "https://www.nasa.gov/news-release/nasa-awards-1-25-million-to-three-teams-at-deep-space-food-finale", date: "Aug 2024"}
  - {title: "NASA: Scientists grow plants in lunar soil (Univ. of Florida, 2022)", url: "https://www.nasa.gov/?p=96327", date: "May 2022"}
  - {title: "NASA BVAD Rev2: food energy and mass per crew-day", url: "https://ntrs.nasa.gov/citations/20210024855", date: "Feb 2022"}
risks:
  - {sev: High, title: "Lighting needs a lot of power for staple crops", fix: "Phase crops by calories per kWh; expand power in step (M11); greens first"}
  - {sev: High, title: "Crop disease or system failure wipes out a harvest", fix: "Several isolated growing modules; 12-month food reserve; seed bank"}
  - {sev: Medium, title: "Raw lunar soil stunts plants (Apollo soil study)", fix: "Use hydroponics; research treated regolith separately"}
  - {sev: Medium, title: "Partial gravity effects on plants over many generations are unknown", fix: "Start with ISS-proven crops; monitor yields; keep Earth food supply until proven"}
---

## What's proven

- **Vegetables in orbit.** The ISS has grown lettuces, Chinese cabbage, mizuna and kale in Veggie<sup class="r">[1](#s1)</sup>, and chile peppers in the Advanced Plant Habitat<sup class="r">[2](#s2)</sup>.
- **Closed loops on the ground.** China's Lunar Palace 1 kept crews alive for **370 days** in a closed system with crops, reaching **98.2% material closure**<sup class="r">[3](#s3)</sup>.
- **Lunar soil.** Plants germinated in real Apollo soil, but grew stunted and stressed<sup class="r">[6](#s6)</sup>.

## How much food?

NASA's reference figures are **12.8 MJ** of food energy and **0.8 kg** of food solids per person per day<sup class="r">[7](#s7)</sup>.

## Step-by-step

1. **Fresh greens in Phase 3.** Fit a Veggie-class unit inside the M09 habitat for morale and nutrition.
2. **Deliver and bury the greenhouse modules.**
3. **Scale to staples:** potatoes, wheat and soy, under LEDs.
4. **Close the nutrient loop** with plant waste and wastewater.
5. **Reach 50% of calories,** then keep going (M13).
