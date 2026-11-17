---
id_code: "C09.3"
milestone: M09
order: 3
title: Medical bay
summary: "A small clinic inside the buried habitat, with ultrasound, a pharmacy, basic surgery and telemedicine. Next to it is an exercise area to fight bone and muscle loss in 1/6 g. It is built to NASA's Level IV standard of care: treat what can be treated on site, and stabilise the rest for evacuation."
trl: 6
spec:
  - {k: "Level of care", v: "NASA Level IV (lunar >30 days): imaging, sustainable advanced life support, limited surgery, dental"}
  - {k: "Crew served", v: "4, growing to 8"}
  - {k: "Expected workload", v: "~300 medical events per 4 crew per 168-day stay (NASA IMPACT model)"}
  - {k: "Telemedicine delay", v: "5–12 s one-way"}
  - {k: "Exercise", v: "~2 h per person per day (ISS practice)"}
  - {k: "Bay volume", v: "~10 m³ clinic + ~15 m³ exercise area (ESTIMATE)"}
  - {k: "Medical mass", v: "~0.5 t at start + ~0.2 t resupply per year (ESTIMATE; NASA's sortie model used 50 kg)"}
  - {k: "Staffing", v: "At least one crew medical officer per rotation (plan design choice)"}
  - {k: "Evacuation", v: "Days, not hours: lander ascent plus ~5-day Earth return"}
subcomponents:
  - name: Diagnostics
    desc: "Portable tools that a trained crew member can use with guidance from doctors on Earth."
    parts: ["Two portable ultrasound units", "Vital signs monitor with ECG", "Point-of-care blood and urine analyser", "Eye and ear examination kit", "Dental examination kit"]
    tech: "ISS remote-guided ultrasound (ADUM)"
    trl: 8
  - name: Pharmacy
    desc: "A tracked stock of medicines, refreshed with every cargo landing so nothing is used past its date."
    parts: ["Formulary based on the ISS list", "Temperature-logged storage", "Barcode inventory tracking", "Retained samples for stability tests"]
    tech: "ISS formulary; NASA drug stability studies"
    trl: 7
  - name: Treatment and limited surgery
    desc: "Equipment to treat injuries, give advanced life support and do minor procedures, but not major operations."
    parts: ["Advanced life support kit (airway, defibrillator, IV fluids)", "Suction and oxygen", "Suture, wound and splint kits", "Dental repair kit", "Steriliser"]
    tech: "Orion medical kit; NASA Level IV capability list"
    trl: 6
  - name: Telemedicine
    desc: "Private video, voice and data links to flight surgeons, plus offline guides for when the link is slow or down."
    parts: ["Private audio and video channel", "Store-and-forward image upload", "Onboard medical procedure guides", "Medical records system"]
    tech: "ISS private medical conferences; NASA comm-delay studies"
    trl: 7
  - name: Exercise and monitoring
    desc: "Resistance and aerobic machines, plus regular tests to check that bone, muscle and fitness stay within NASA limits."
    parts: ["ARED-class resistance device", "Treadmill", "Cycle ergometer with VO₂ measurement", "Bone ultrasound checks", "Strength test station"]
    tech: "ISS ARED, treadmill and cycle"
    trl: 6
  - name: Evacuation kit
    desc: "Equipment and procedures to stabilise a patient and move them to the crew return vehicle."
    parts: ["Rigid stretcher that fits the airlock", "Portable monitor and oxygen", "Patient transfer procedures", "Return vehicle kept ready"]
    tech: "Orion medical system; ISS crew return planning"
    trl: 5
risks:
  - {sev: Critical, title: "Severe trauma or a surgical emergency is beyond Level IV care, and evacuation takes days", fix: "Train crew medical officers; stabilise with advanced life support; keep a return vehicle ready; flight surgeons on call."}
  - {sev: High, title: "Long-term effects of 1/6 g on bone and muscle are unknown; exercise may not be enough", fix: "Six-month rotations; test bone and fitness against NASA limits; stop extensions if trends are bad."}
  - {sev: High, title: "Many medicines expire within 3 years, and some degrade faster in space", fix: "Replace stock at every cargo landing; test retained samples; choose drugs with long shelf lives."}
  - {sev: High, title: "Lunar dust exposure is the most common predicted medical event", fix: "Dust control at the airlock (M08); eye wash and respiratory kits; track exposure."}
  - {sev: Medium, title: "Telemedicine is slowed by delay and lost during link outages", fix: "Onboard guides and decision support; store-and-forward images; crew trained to act alone."}
  - {sev: Medium, title: "A single broken ultrasound or analyser removes a key tool", fix: "Two ultrasound units; spare parts; printable fittings from the fab shop (C12.1)."}
  - {sev: Medium, title: "Medical privacy is hard in a small crew", fix: "Private comm channel; screened clinic area; clear rules on who sees records."}
sources:
  - {title: "Haas, NASA JSC: Artemis medical system overview (ASCEND 2023)", url: "https://ntrs.nasa.gov/api/citations/20230015294/downloads/ASCEND_Artemis_Med_System_Dvlpnt_Ovrvw_Final.pdf", date: "Oct 2023"}
  - {title: "Anderson et al., NASA HRP ExMC: Effect of mission duration on predicted medical risk for an extended lunar mission (AsMA 2024)", url: "https://ntrs.nasa.gov/api/citations/20240004460/downloads/Mission%20Duration%20AsMA%2024%20Anderson.pdf", date: "May 2024"}
  - {title: "JAXA: Remote-guided ultrasound on the ISS (ADUM)", url: "https://iss.jaxa.jp/en/iss/benefits/health/7ultrasound", date: "2009"}
  - {title: "Holden et al., NASA HRP: Communication delays in cislunar space, aims and methods", url: "https://ntrs.nasa.gov/api/citations/20260002621/downloads/Holden%20et%20al%202026%20-%20comm%20delay%20study%20methodsa.pdf", date: "2026"}
  - {title: "Diaz et al., npj Microgravity: Expiration analysis of the ISS formulary for exploration mission planning", url: "https://pmc.ncbi.nlm.nih.gov/articles/PMC11266549/", date: "Jul 2024"}
  - {title: "NASA HRP Human Research Roadmap: Risk of ineffective or toxic medications during long-duration exploration spaceflight", url: "https://humanresearchroadmap.nasa.gov/risks/risk.aspx?i=177", date: "accessed Nov 2026"}
  - {title: "NASA: Counteracting bone and muscle loss in microgravity", url: "https://www.nasa.gov/missions/station/iss-research/counteracting-bone-and-muscle-loss-in-microgravity/", date: "Dec 2023"}
  - {title: "NASA OCHMO-TB-031: Exercise overview (NASA-STD-3001 technical brief)", url: "https://www.nasa.gov/wp-content/uploads/2023/12/ochmo-tb-031-exercise-overview.pdf", date: "Oct 2023"}
  - {title: "Jones, NASA Ames: The problem of partial gravity on the Moon and Mars (ICES)", url: "https://ntrs.nasa.gov/citations/20205010170", date: "2021"}
---

## What it does

The medical bay keeps a crew of four to eight healthy for six-month stays. NASA's standard sets five levels of medical care. **Level IV** applies to lunar missions longer than 30 days. It covers everything in Level III, plus **medical imaging, sustainable advanced life support, limited surgery and dental care**<sup class="r">[1](#s1)</sup>. The bay is built to that level.

NASA's IMPACT model, from its Human Research Program, gives a sense of the workload. For four crew spending 168 days on the surface, it predicts about **299 medical events** per mission. Lunar dust exposure during EVA is the most common<sup class="r">[2](#s2)</sup>. Most events are minor, but they add up.

## How it works

**Diagnostics.** Ultrasound is the main imaging tool. On the ISS, crew made diagnostic-quality heart, blood-vessel and chest scans. A remote expert guided them by voice while watching the live video. The method worked with non-medical operators<sup class="r">[3](#s3)</sup>. NASA lists ultrasound among the planned lunar medical capabilities<sup class="r">[1](#s1)</sup>.

**Pharmacy.** In a 2024 analysis of the ISS formulary, shelf-life data could be found for 91 medicines. Of those, **54 (59%)** had an estimated shelf life of 36 months or less<sup class="r">[5](#s5)</sup>. NASA's Human Research Program tracks the risk that medicines become ineffective or toxic on long missions<sup class="r">[6](#s6)</sup>. With two cargo landings a year (M09), the stock is replaced well before it expires.

**Limited surgery.** Level IV means minor procedures, wound care and stabilisation. It does not mean major operations<sup class="r">[1](#s1)</sup>. Anything bigger is stabilised and evacuated.

**Telemedicine.** One-way delay at the Moon in the Artemis era is **5 to 12 seconds**<sup class="r">[4](#s4)</sup>. That is too slow for a doctor to steer an ultrasound probe second by second. So crew use onboard guides, send stored images for review, and talk with doctors at a slower pace.

**Exercise.** ISS crews exercise about **2 hours a day**. Without countermeasures, weight-bearing bones lose roughly **1% of their density per month**<sup class="r">[7](#s7)</sup>. NASA standards require hip and spine bone density to stay at or above **95%** of pre-flight values. They also require VO₂max of at least **36.5 ml/(min·kg)** for crew doing surface EVAs<sup class="r">[8](#s8)</sup>. A NASA analysis warns that gravity below 0.4 g seems too low to keep the body fully conditioned. It concludes that exercise is necessary but probably not sufficient<sup class="r">[9](#s9)</sup>.

**Evacuation.** In NASA's late-Artemis reference mission, the trip home is lander ascent, about 10 days at Gateway, then **5 days** in Orion<sup class="r">[2](#s2)</sup>. An emergency return might skip the wait at Gateway. Even so, the patient must be kept stable for days.

## Sizing (ESTIMATE)

| Item | Working |
|---|---|
| Medical mass at start | ~0.5 t: diagnostics, treatment kits, pharmacy, spares. This is about 10× the 50 kg allocation NASA used for one 4-crew mission model<sup class="r">[2](#s2)</sup>, because the bay is permanent and must have two of each key tool. |
| Resupply | ~0.2 t a year: medicines and consumables, split across two cargo landings |
| Exercise time | 8 crew × 2 h = 16 machine-hours a day. That needs at least two resistance and two aerobic stations. |

## Testing and qualification

1. Test the equipment list against NASA's IMPACT model for 4 and 8 crew on 6-month stays<sup class="r">[2](#s2)</sup>.
2. Run medical scenarios in a ground analog with a 5–12 s delay.
3. Check that each device works in the habitat's atmosphere, power supply and dust.
4. On the Moon, commission the bay during M08 sorties. Collect baseline bone and fitness data for every crew member.
5. Review the results after each rotation.

## Open questions

- How fast do bone and muscle change at 1/6 g with 2 hours of daily exercise?
- Which medicines degrade fastest in a lunar habitat's radiation and temperature?
- Should each rotation include a physician, or are trained crew medical officers enough?
- What is the fastest realistic medical evacuation from the south pole to a hospital on Earth?
