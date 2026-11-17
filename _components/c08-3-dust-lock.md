---
id_code: "C08.3"
milestone: M08
order: 3
title: Dust lock and suitports
summary: "A small vestibule with two suitports, cleaning tools, electrodynamic dust shields and filters that lets crews go outside and come back without bringing lunar dust into the cabin."
trl: 5
spec:
  - {k: "Layout", v: "2 suitports on the rear bulkhead of a 2-person dust lock (design choice)"}
  - {k: "Dust lock volume", v: "4.25 m³ empty, 3.7 m³ free gas (NASA 2-person airlock value)"}
  - {k: "Pre-EVA time target", v: "Under 30 minutes via suitport (NASA)"}
  - {k: "Suitport test pressure", v: "8.3 psi across the suit (NASA JSC chamber test)"}
  - {k: "Gas lost per full airlock cycle", v: "~0.25 kg at 8.2 psia (ESTIMATE)"}
  - {k: "EDS cleaning", v: "96–99% dust removal in vacuum lab tests; worked on the Moon Mar 2025"}
  - {k: "Cabin dust limit", v: "<0.3 mg/m³ of particles under 10 µm (NASA-STD-3001)"}
  - {k: "Mass", v: "~1.5 t including suitports and fittings (ESTIMATE)"}
subcomponents:
  - name: Suitport bulkhead
    desc: "Rear-entry suits dock to the outside of the bulkhead, so the dusty suit never enters the pressurised volume."
    parts: ["Suitport interface plate and capture mechanism", "Inner hatch and outer suit-hatch seals", "Pressure equalisation valves", "Life support and power umbilical", "Suit stowage cover for dust"]
    tech: "NASA JSC Marman clamp and pneumatic flipper suitports, tested with the Z-1 suit"
    trl: 5
  - name: Dust lock chamber
    desc: "A two-person airlock that also serves as a backup way in and out and a place to clean tools and samples."
    parts: ["Outer hatch to the surface", "Inner hatch to the habitat", "Depress and repress pump", "Sample and tool pass-through box", "Lighting and cameras"]
    tech: "ISS Quest airlock heritage; BVAD airlock values"
    trl: 6
  - name: Mechanical cleaning
    desc: "Removes the coarse dust before a suit docks or a person enters."
    parts: ["Soft and stiff brushes at the entrance", "Boot scraper and grate", "Vacuum brush with filtered exhaust", "Wipes for hands and eye rinse kit"]
    tech: "Apollo practice (brushes, vacuum brush), improved"
    trl: 6
  - name: Electrodynamic dust shields (EDS)
    desc: "Embedded electrodes that use a moving electric field to lift dust off windows, radiators, camera lenses and seal faces."
    parts: ["Transparent electrode film for windows and cameras", "Electrode panels on radiators near the hatch", "High-voltage, low-power drive electronics", "Controller tied to EVA schedule"]
    tech: "NASA KSC EDS, flown on Firefly Blue Ghost Mission 1"
    trl: 6
  - name: Filtration and monitoring
    desc: "Catches fine dust that gets past the lock and checks it stays below the NASA limit."
    parts: ["High-efficiency particulate filters on dust lock and cabin air", "Pre-filters that are easy to change", "Airborne particle monitor", "Filter spares"]
    tech: "ISS bacteria and particulate filter heritage"
    trl: 6
  - name: Seals and exterior apron
    desc: "Dust-tolerant seals at every hatch and a hard, clean surface outside so less dust is kicked up near the door."
    parts: ["Double seals with a dust lip", "Seal covers when hatches are open", "Sintered regolith apron around the dust lock (M05)", "Seal inspection and cleaning kit"]
    tech: "Design choice; sintered pavers from M05"
    trl: 4
risks:
  - {sev: Critical, title: "Dust ruins seals; on Apollo 12 a suit leak rose to 0.25 psi/min against a 0.30 psi/min limit after two EVAs", fix: "Double seals with dust lips, seal covers, inspection after every EVA, and EDS on seal faces"}
  - {sev: High, title: "Suitport doffing was harder than expected in tests on Earth", fix: "Human-in-the-loop tests in 1/6 g simulation; handholds and assist devices; keep the dust lock as a backup way in"}
  - {sev: High, title: "Suitport needs a matching suit interface; the AxEMU and the habitat may not fit", fix: "Fix the interface standard with the suit provider early (C08.4); test with flight suits before launch"}
  - {sev: High, title: "Brushes worked in ground tests but poorly on the Moon", fix: "Treat brushes as first stage only; rely on suitports to keep suits outside; qualify cleaning with real-like simulant in vacuum"}
  - {sev: Medium, title: "EDS has only a short Moon demonstration on small samples", fix: "Fly EDS on non-critical surfaces first; measure performance over the 3-month uncrewed run"}
  - {sev: Medium, title: "Each full airlock cycle loses gas that must be shipped or made", fix: "Use suitports for routine EVAs; use the dust lock for emergencies and cargo; recover more gas with longer pump-down"}
  - {sev: Medium, title: "Dust harms eyes and lungs; Apollo crews needed saline eye rinses", fix: "Particle monitor alarm, eye rinse and masks at the dust lock, and limits on cabin dust from NASA-STD-3001"}
sources:
  - {title: "Gaier, NASA/TM-2005-213610: Effects of lunar dust on EVA systems during Apollo", url: "https://ntrs.nasa.gov/citations/20050160460", date: "2005"}
  - {title: "NASA NTRS 20130013652: Suitport feasibility, pressurised donning tests with Marman clamp and pneumatic flipper suitports", url: "https://ntrs.nasa.gov/citations/20130013652", date: "2013"}
  - {title: "NASA BVAD Rev2 (NASA/TP-2015-218570): Life Support Baseline Values and Assumptions", url: "https://ntrs.nasa.gov/citations/20210024855", date: "Feb 2022"}
  - {title: "NASA NTRS 20150016082: History and flight development of the Electrodynamic Dust Shield", url: "https://ntrs.nasa.gov/citations/20150016082", date: "Aug 2015"}
  - {title: "NASA: dust shield successfully repels lunar regolith on Moon", url: "https://www.nasa.gov/image-article/nasas-dust-shield-successfully-repels-lunar-regolith-on-moon/", date: "Mar 2025"}
  - {title: "NASA NTRS 20250005380: CLPS EDS payload thermal design and analysis", url: "https://ntrs.nasa.gov/citations/20250005380", date: "2025"}
  - {title: "NASA OCHMO-TB-011: Lunar dust technical brief (NASA-STD-3001)", url: "https://www.nasa.gov/wp-content/uploads/2023/03/lunar-dust-technical-brief-ochmo.pdf", date: "Nov 2022"}
  - {title: "NASA NTRS 20200000920: Current state of the Electrodynamic Dust Shield for mitigation", url: "https://ntrs.nasa.gov/citations/20200000920", date: "Feb 2020"}
---

## What it does

Lunar dust was the biggest housekeeping problem on Apollo. A NASA review sorted its effects into nine groups, from clogged mechanisms and abrasion to seal failures and lung irritation. Simple measures did not stop the serious ones, and ground tests kept underestimating the problem<sup class="r">[1](#s1)</sup>. The dust lock is the habitat's line of defence. Its job is to meet NASA's cabin limit: dust particles under 10 µm kept below **0.3 mg/m³** on average<sup class="r">[7](#s7)</sup>.

## How it works

- **Suitports first.** A suitport is a bulkhead opening that captures and seals a rear-entry suit while the suit stays outside. NASA says it can cut pre-EVA time from hours to under 30 minutes, save airlock gas and keep dirt out of the cabin. NASA JSC tested human donning and doffing of the Z-1 suit at an 8.3 psi difference in a vacuum chamber, and found doffing harder than expected<sup class="r">[2](#s2)</sup>.
- **Dust lock as backup.** NASA's reference two-person airlock is 4.25 m³ empty with 3.7 m³ of free gas. About 10% of that gas is lost each cycle, or 5% with a slower pump-down<sup class="r">[3](#s3)</sup>. Flight rules normally ask for two ways out<sup class="r">[3](#s3)</sup>, so the dust lock is the second exit and the way to bring in samples and tools.
- **Brushes and vacuum.** Apollo crews used a nylon brush. It removed coarse grains but not the fine dust. Cabins were cleaned with a vacuum brush<sup class="r">[1](#s1)</sup>. Here brushes are only the first stage.
- **Electrodynamic dust shields.** Electrodes in a surface carry a travelling electric field that moves dust off. In vacuum lab tests, coated thermal radiators returned to 96–99% of their clean reflectance<sup class="r">[4](#s4)</sup>. On Firefly's Blue Ghost Mission 1 in March 2025, the shield removed regolith from glass and radiator samples on the Moon<sup class="r">[5](#s5)</sup>. KSC can now make large shields roll-to-roll<sup class="r">[8](#s8)</sup>.
- **Seals.** On Apollo 12, Pete Conrad's suit leak rose from 0.15 to 0.25 psi/min over two EVAs, against a 0.30 psi/min limit. All sample container seals failed because of dust<sup class="r">[1](#s1)</sup>. Every hatch here has double seals, covers and an inspection step.

## Sizing

Gas lost per full dust lock cycle at 8.2 psia, 34% O₂ (ESTIMATE):

- Gas in 3.7 m³: n = PV/RT = (56,540 Pa × 3.7) ÷ (8.314 × 295) ≈ 85 mol
- Mass at 29.4 g/mol ≈ **2.5 kg**; at 10% loss ≈ **0.25 kg per cycle**
- BVAD nominal is 5 cycles per week<sup class="r">[3](#s3)</sup>. A 30-day sortie is about 21 cycles, or **~5.4 kg** of gas.

With suitports, NASA estimates oxygen loss of 0.1 kg per crew-hour plus 0.54 kg per crew per EVA, mostly the nitrogen purge before EVA<sup class="r">[3](#s3)</sup>. The main gain from suitports is dust and time, not gas.

## Testing and qualification

1. **Suitport tests** in a vacuum chamber with the flight suit (C08.4), including emergency doffing.
2. **Dust tests** with high-fidelity simulant in vacuum: brush, EDS and seal cycling for at least the number of EVAs in four sorties.
3. **EDS life test** on habitat-sized panels and window films.
4. **On the Moon, uncrewed.** Run the dust lock pumps, EDS and seals through many cycles during the 3-month habitat checkout. A NASA thermal study found dust from landing degraded the EDS payload's optical surfaces<sup class="r">[6](#s6)</sup>, so expect to clean after every landing nearby.
5. **Each sortie.** Log particle counts in the cabin and compare with the 0.3 mg/m³ limit.

## Open questions

- Can suitports be cleaned and inspected from inside, or does that need an EVA?
- How long do EDS electrodes last under daily abrasion near a hatch?
- What is the best simulant for qualifying seals? Apollo-era ground tests were too kind<sup class="r">[1](#s1)</sup>.
- How much does a sintered apron cut the dust carried to the door?
