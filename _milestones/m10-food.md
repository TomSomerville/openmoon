---
id_code: M10
order: 10
title: Growing food
phase: 3
window: "Years 8–14"
summary: Grow a growing share of the crew's food in buried, LED-lit greenhouses, starting with fresh vegetables and working toward most calories.
objective: "Produce at least 50% of the calories of the 6-person design crew on the Moon, in shielded greenhouse modules using hydroponics and LED lighting, with plant waste recycled into the life support loop."
trl_min: 5
depends_on: [M04, M06, M09]
spec:
  - {k: Approach, v: "Hydroponic / aeroponic crops under LEDs in buried modules"}
  - {k: Crops, v: "Leafy greens first; then potatoes, wheat, soy, peppers"}
  - {k: Target, v: "≥50% of calories for the 6-person design crew (DD-006); 9-person handover peaks eat stored food"}
  - {k: Food need, v: "12.8 MJ and 0.8 kg food solids per person per day"}
  - {k: "Canopy and power", v: "~196 m² growing area, ~46 kW (C10.1 ESTIMATE from BVAD and LED data)"}
cost: {low: 9.7, high: 43.6, note: "greenhouse modules, lighting power, and research"}
cost_items:
  - {item: "Greenhouse modules (build), 3 modules", low: 0.4, high: 1.1, basis: "ESTIMATE; was $0.5–1.5B for 4 modules for 8 crew, scaled × 3/4 for 6 crew (DD-006)"}
  - {item: "Delivery of greenhouse modules (~13–16 t, heavy cargo)", low: 2.6, high: 9.6, basis: "13–16 t (C10.1 ESTIMATE for 6 crew; was 17–21 t for 8) × $0.2–0.6M/kg"}
  - {item: "Extra ~60 kW for lighting: three more 20 kWe LR-1-class reactors feeding the PMC, each with 160 kWh of ride-through battery (DD-002, DD-003, DD-008)", low: 6.51, high: 32.43, basis: "C10.1 sizing (~46 kW for 6 crew, still more than two units give, so three are kept; power not resized); build 3 × $0.25–0.75B ESTIMATE + delivery 3 × 7.5–15 t × $0.2–0.6M/kg + batteries 3 × (~1 t × $0.4–1.0M/kg + $0.02–0.06B hardware)"}
  - {item: "Crop research and ground analog", low: 0.2, high: 0.5, basis: "ESTIMATE"}
exit_criteria:
  - "Fresh vegetables available to every crew member every week."
  - "At least 50% of the 6-person design crew's calories produced locally, averaged over a year (meals for the extra people at handovers come from stored food)."
  - "Inedible plant mass composted or processed and returned to the loop."
  - "No crop failure causes a food shortage (12 months of stored food on site)."
workstreams:
  - name: Greenhouse modules
    desc: Buried, shielded growing space.
    items: ["Pressurised modules under regolith", "LED lighting tuned per crop", "Separate atmosphere loop", "Each module on its own service connection and 120 V DC panel (DD-009)"]
  - name: Crops
    desc: Start easy, then scale to staples.
    items: ["Lettuce, kale, mustard greens (proven on ISS)", "Peppers (grown on ISS 2021)", "Potatoes, wheat, soy for calories"]
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
  - {name: "NASA Veggie", use: "Leafy greens", status: "ISS plant facilities (Veggie and APH) have grown lettuces, Chinese cabbage, mustard greens, kale", trl: 9, src: 1}
  - {name: "NASA Advanced Plant Habitat", use: "Controlled growth of fruiting crops", status: "Chile peppers bore fruit on ISS; harvests planned late Oct and early Nov 2021", trl: 9, src: 2}
  - {name: "Yuegong-1 (Lunar Palace 1) bioregenerative system", use: "Closed-loop life support with crops", status: "370 days, 8 crew in two groups of four (2017–18); 98.2% material closure on the ground", trl: 6, src: 8}
  - {name: "ESA MELiSSA", use: "Closed-loop ecosystem research", status: "Pilot plant at Universitat Autònoma de Barcelona since 2009", trl: 4, new: true, src: 4}
  - {name: "Interstellar Lab NUCLEUS", use: "Compact food production", status: "Won NASA Deep Space Food Challenge grand prize 2024", trl: 5, src: 5}
sources:
  - {title: "NASA: Science in space, plant science (Veggie)", url: "https://www.nasa.gov/missions/station/iss-research/science-in-space-week-of-july-10-2023-plant-science/", date: "Jul 2023"}
  - {title: "NASA: Houston, we have a pepper", url: "https://www.nasa.gov/centers-and-facilities/kennedy/houston-we-have-a-pepper/", date: "2021"}
  - {title: "Lunar Palace 1 (Lunar Palace 365 mission), Wikipedia", url: "https://en.wikipedia.org/wiki/Lunar_Palace_1", date: "accessed Nov 2026"}
  - {title: "MELiSSA, Wikipedia", url: "https://en.wikipedia.org/wiki/MELiSSA", date: "accessed Nov 2026"}
  - {title: "NASA: NASA awards $1.25 million to three teams at Deep Space Food finale", url: "https://www.nasa.gov/news-release/nasa-awards-1-25-million-to-three-teams-at-deep-space-food-finale", date: "Aug 2024"}
  - {title: "NASA: Scientists grow plants in lunar soil (Univ. of Florida, 2022)", url: "https://www.nasa.gov/?p=96327", date: "May 2022"}
  - {title: "NASA BVAD Rev2: food energy and mass per crew-day", url: "https://ntrs.nasa.gov/citations/20210024855", date: "Feb 2022"}
  - {title: "Fu et al.: Establishment of a closed artificial ecosystem to ensure human long-term survival on the Moon (bioRxiv preprint, Lunar Palace 365)", url: "https://www.biorxiv.org/content/10.1101/2021.01.12.426282v1", date: "Jan 2021"}
risks:
  - {sev: High, title: "Lighting needs a lot of power for staple crops", fix: "Phase crops by calories per kWh; expand power in step (M11); greens first"}
  - {sev: High, title: "Crop disease or system failure wipes out a harvest", fix: "Several isolated growing modules; 12-month food reserve; seed bank"}
  - {sev: Medium, title: "Raw lunar soil stunts plants (Apollo soil study)", fix: "Use hydroponics; research treated regolith separately"}
  - {sev: Medium, title: "Partial gravity effects on plants over many generations are unknown", fix: "Start with ISS-proven crops; monitor yields; keep Earth food supply until proven"}
---

## What's proven

- **Vegetables in orbit.** The ISS has grown lettuces, Chinese cabbage, mustard greens and kale in its Veggie and Advanced Plant Habitat units<sup class="r">[1](#s1)</sup>, and chile peppers in the Advanced Plant Habitat<sup class="r">[2](#s2)</sup>.
- **Closed loops on the ground.** China's Lunar Palace 1 kept crews alive for **370 days** in a closed system with crops, reaching **98.2% material closure**<sup class="r">[3](#s3)</sup><sup class="r">[8](#s8)</sup>.
- **Lunar soil.** Plants germinated in real Apollo soil, but grew stunted and stressed<sup class="r">[6](#s6)</sup>.

## How much food?

NASA's reference figures are **12.8 MJ** of food energy and **0.8 kg** of food solids per person per day<sup class="r">[7](#s7)</sup>.

{% include decision-note.html id="DD-006" extra="M10 was sized for 8 crew. It is now sized for the 6-person design crew: about 196 m² of canopy in 3 greenhouse modules instead of about 261 m² in 4. Handover peaks of 9 people, about 2 weeks every 3 months, raise the yearly average to 6.5 people; those meals come from stored food." %}

- **6 people:** 6 × 0.8 = 4.8 kg of food solids a day; half of it grown is 2.4 kg (this plan's arithmetic).
- **9 people at a handover:** 7.2 kg a day for about 2 weeks, from stored food and food carried on the crew lander.

## Step-by-step

1. **Fresh greens from Phase 2.** Fit a Veggie-class unit inside the habitat for morale and nutrition once the first crew is aboard (M09).
2. **Deliver and bury the greenhouse modules.**
3. **Scale to staples:** potatoes, wheat and soy, under LEDs.
4. **Close the nutrient loop** with plant waste and wastewater.
5. **Reach 50% of calories,** then keep going (M13).
