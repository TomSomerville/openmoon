---
id_code: "C09.2"
milestone: M08
order: 6
title: Solar particle event storm shelter
summary: "A small, heavily shielded room in the middle of the buried habitat, lined with water walls, big enough for all 9 people at a handover. Crew go there when a solar particle event is detected. It keeps their dose below NASA's 250 mSv per-event limit."
trl: 6
spec:
  - {k: "Design event", v: "Sum of the October 1989 solar particle events (NASA-STD-3001 design reference)"}
  - {k: "Dose limit", v: "<250 mSv effective per event (NASA-STD-3001)"}
  - {k: "Added shielding", v: "10 cm water fixed + 10 cm reconfigurable = 20 cm (millennial event)"}
  - {k: "Capacity", v: "9 people for up to 3 days, the handover peak (plan design choice, DD-006)"}
  - {k: "Interior", v: "~2 m × 3 m × 2 m, ~12 m³ (ESTIMATE; PROVISIONAL until the module design exists, DD-007), ~1.3 m³ per person at 9"}
  - {k: "Water in walls", v: "~2.6 t fixed + ~2.6 t reconfigurable (ESTIMATE)"}
  - {k: "Location", v: "Middle of the three side-by-side modules, under the 3 m roof cover (C09.1)"}
  - {k: "Ready", v: "Filled and checked before the first crew lands (M08, DD-005)"}
  - {k: "Time to enter", v: "<15 minutes from anywhere inside the habitat (plan design choice)"}
  - {k: "Warning sources", v: "NOAA SWPC and NASA SRAG forecasts; local HERA alarm; personal dosimeters"}
subcomponents:
  - name: Water-wall enclosure
    desc: "Fixed water tanks form the walls and ceiling of a small room. They double as the base's reserve water store."
    parts: ["Modular water bladders in rigid frames (10 cm)", "Level sensors on each bladder", "Fill and drain manifold to the water loop", "Hinged water-filled door panel"]
    tech: "NASA water-wall storm shelter studies (AES RadWorks)"
    trl: 5
  - name: Reconfigurable shielding
    desc: "Stowage, food and extra water bags are moved onto marked rails to add another 10 cm when a large event starts."
    parts: ["Rail-mounted bag holders", "Pre-packed water bags", "Shielding map showing where dense bags go", "Bag inventory tags"]
    tech: "Orion stowage-bag shelter (Artemis)"
    trl: 6
  - name: Air and power tie-in
    desc: "The shelter shares the habitat atmosphere through a bent, shielded duct and has its own backup lighting and sensors."
    parts: ["Ventilation duct with dog-leg", "CO₂ and O₂ sensors", "Battery-backed lights and fans", "Backup CO₂ absorbent canisters"]
    tech: "ISS life support practice"
    trl: 6
  - name: Warning chain
    desc: "Forecasts from Earth give advance notice. Local detectors give the final alarm without needing Earth."
    parts: ["NOAA SWPC forecasts and S-scale warnings", "NASA SRAG console support", "HERA-class area monitors with base alarm", "Crew Active Dosimeters with dose-rate alarm", "EVA recall procedure"]
    tech: "HERA and Crew Active Dosimeter (Artemis I); NOAA GOES proton monitoring"
    trl: 7
  - name: Shelter supplies
    desc: "Enough food, water, hygiene and medical items for a three-day stay are pre-packed inside."
    parts: ["Food and drinking water for 9 people × 3 days", "Waste bags and hygiene kit", "Medical kit", "Sleeping restraints and pads", "Comms and laptop terminal"]
    tech: "ISS and Orion crew provisions"
    trl: 9
risks:
  - {sev: Critical, title: "A large event hits crew on EVA far from the habitat", fix: "Limit EVA range so crew can reach shielding within 2 hours; pressurised rovers carry water shielding; recall on the first alarm."}
  - {sev: High, title: "Solar particle events cannot be predicted accurately", fix: "Rely on real-time dose rates and local alarms; keep the shelter minutes away from every work area."}
  - {sev: High, title: "Water drawn from the walls for life support leaves the shelter thin", fix: "Flight rule for a minimum fill; level alarms on every bladder; refill from M06 water."}
  - {sev: High, title: "A solar event during a handover puts 9 people in a room sized for few", fix: "Size air, CO₂ backup and supplies for 9; drill a 9-person entry at every handover; use reconfigurable stowage walls to extend the space."}
  - {sev: Medium, title: "Loss of the Earth link breaks the forecast part of the warning chain", fix: "Local HERA monitors raise the alarm on their own; crew act on local readings."}
  - {sev: Medium, title: "Several days in a cramped room strains crew and air quality", fix: "Size for 9 people; monitor CO₂; run regular drills; once fully buried, shelter stays should be short."}
  - {sev: Medium, title: "Frequent minor alerts disrupt work", fix: "Set action thresholds by dose rate; most events need only ALARA steps, not shelter."}
sources:
  - {title: "NASA OCHMO-TB-020: Design for ionizing radiation protection (NASA-STD-3001 technical brief)", url: "https://www.nasa.gov/wp-content/uploads/2023/03/radiation-protection-technical-brief-ochmo.pdf", date: "Dec 2022"}
  - {title: "Clowdsley, NASA LaRC: Protecting astronauts from space radiation on the lunar surface (LSIC talk)", url: "https://ntrs.nasa.gov/api/citations/20210009760/downloads/Clowdsley_Lunar_Radiation_Talk_v2.pdf", date: "Feb 2021"}
  - {title: "NOAA SWPC: Solar radiation storm", url: "https://www.spaceweather.gov/phenomena/solar-radiation-storm", date: "accessed Nov 2026"}
  - {title: "NASA Science: How NASA will protect astronauts from space radiation at the Moon", url: "https://science.nasa.gov/science-research/heliophysics/how-nasa-will-protect-astronauts-from-space-radiation-at-the-moon", date: "Aug 2019"}
  - {title: "NASA: Artemis I radiation measurements validate Orion safety for astronauts", url: "https://www.nasa.gov/humans-in-space/artemis-i-radiation-measurements-validate-orion-safety-for-astronauts/", date: "Oct 2024"}
  - {title: "NASA BVAD Rev2 (NASA/TP-2015-218570): crew consumables", url: "https://ntrs.nasa.gov/citations/20210024855", date: "Feb 2022"}
  - {title: "NASA NTRS 20230013896: Logistics rates beyond LEO (2.36 kg packaged food per crew-day)", url: "https://ntrs.nasa.gov/api/citations/20230013896/downloads/Logistics_BeyondLEO-ASCEND2023-Pres.pdf", date: "2023"}
---

## What it does

Solar particle events (SPEs) are bursts of low- to medium-energy protons. They are rare, but an unshielded crew could get acute radiation sickness<sup class="r">[1](#s1)</sup><sup class="r">[2](#s2)</sup>. NASA-STD-3001 says crews must be kept below **250 mSv** for the design event, which is the sum of the **October 1989** events<sup class="r">[1](#s1)</sup>. The storm shelter is where the crew go to meet that limit.

Because the habitat is under ≥2 m of regolith before anyone lands (C09.1, DD-005), the shelter is a backup. It matters most at the less-shielded entrance end, when crew are recalled from EVA, and at handovers, when 9 people are on base.

## How it works

**How thick.** NASA's guidance is to add **10 cm of water** to the crew quarters for a once-a-century event, and about **20 cm** for a once-a-millennium event. This can be done partly by moving water containers and stowage, and SPE timelines leave time to do it. About **95%** of SPEs need only "as low as reasonably achievable" (ALARA) steps, not a shelter<sup class="r">[1](#s1)</sup>.

**Water walls and stowage.** NASA studies show that food, water and supplies can be rearranged into a shelter, and that water walls can add to crew-quarters shielding<sup class="r">[2](#s2)</sup>. In one study of a four-person, ISS-derived habitat, the planned supplies were only enough to shield two crew quarters (with crew doubling up) or a central box half the size first proposed<sup class="r">[2](#s2)</sup>. That is why Open Moon builds the first 10 cm in as permanent tanks. Orion's plan uses stowage bags in the same way<sup class="r">[4](#s4)</sup>.

**Location.** The shelter is in the middle of the three side-by-side modules, under the deepest regolith (its exact place is set with the module design, DD-007). NASA describes a hub-and-spoke layout, with stores and equipment around a central core where the crew spend most of their time<sup class="r">[1](#s1)</sup>.

**Warning chain.**
1. NOAA's Space Weather Prediction Center watches proton flux with GOES satellites. It issues warnings when an S1 or larger storm is expected, and alerts when each level is reached<sup class="r">[3](#s3)</sup>.
2. NASA's Space Radiation Analysis Group at Johnson checks the SWPC forecast daily and alerts mission control<sup class="r">[4](#s4)</sup>.
3. On site, HERA monitors can warn crew to take shelter. Crew Active Dosimeters log each person's dose in real time<sup class="r">[5](#s5)</sup>.

Fast protons can arrive within **tens of minutes** of an eruption. A storm lasts **hours to days**<sup class="r">[3](#s3)</sup>. Long-range prediction is not accurate. But real-time dose-rate readings are enough to keep exposure well below the limits<sup class="r">[1](#s1)</sup>. For EVA, real-time alerts protect crew well if they can get to shielding **within 2 hours**<sup class="r">[1](#s1)</sup>.

## Sizing (ESTIMATE)

| Item | Working |
|---|---|
| Shielded faces | Walls + ceiling of a 2 × 3 × 2 m room = 26 m² (the floor faces the Moon) |
| Fixed water, 10 cm | 26 m² × 0.10 m ≈ 2.6 m³ ≈ **2.6 t** |
| Reconfigurable, +10 cm | another ≈ **2.6 t** of water bags and stowage |
| Drinking water, 9 people × 3 days | 9 × 3 × 3.217 kg<sup class="r">[6](#s6)</sup> ≈ **87 kg** |
| Food, 9 people × 3 days | 9 × 3 × 2.36 kg packaged<sup class="r">[7](#s7)</sup> ≈ **64 kg** |
| Room per person at 9 | 12 m³ ÷ 9 ≈ **1.3 m³** (provisional) |

The fixed 2.6 t is more than twice a 60-day drinking-water reserve for six people (6 × 60 × 3.217 kg ≈ 1.2 t). So the shelter walls can also serve as the base's water store.

## Testing and qualification

1. Model the shelter inside the buried habitat with OLTARIS, using the October 1989 design event<sup class="r">[2](#s2)</sup>.
2. Build a ground mock-up and time crews building the reconfigurable layer.
3. Test bladder leaks, the duct, and CO₂ build-up with 9 people for 72 hours.
4. On the Moon, fill the walls and compare HERA readings inside and outside during quiet-Sun conditions.
5. Run a shelter drill at every handover, with all 9 people, including an EVA recall.

## Open questions

- What dose do the entrance tunnel and airlock really get while the cover is being built?
- How far can EVAs and rovers go while keeping a 2-hour return to shielding?
- Can wastewater or brine fill the walls instead of clean water?
- What should the dose-rate thresholds be for the lunar surface?
