---
slug: iss-water-recovery-with-brine-processor
title: "ISS water recovery with Brine Processor"
alternatives:
  - {name: "ISS Water Recovery System without brine processing", compare: "The same Urine Processor and Water Processor, minus the Brine Processor. Simpler, with one less consumable bladder, but total recovery drops from about 98% to 93-94%, so more make-up water must be shipped or mined.", status: "Flight-proven on the ISS since 2008; the brine is stored and thrown away.", url: "https://www.nasa.gov/missions/station/iss-research/nasa-achieves-water-recovery-milestone-on-international-space-station/"}
  - {name: "NASA Brine Evaporation Bag (BEB)", compare: "A membrane bag that is dried with heat and vacuum, designed to work with a heat melt compactor. It cut brine mass by 96% in tests and needs no dedicated fan rack, but it has only been run as a breadboard.", status: "Laboratory breadboard; a reduced-gravity flight showed it works in microgravity. Not flown on the ISS.", url: "https://ntrs.nasa.gov/citations/20190001333"}
  - {name: "NASA Forward Osmosis Brine Drying (FOBD)", compare: "Pulls water out of brine into a salt solution through a membrane, so it needs little heat. Reached 95% brine recovery in tests, but needs a salt regeneration system that was not tested.", status: "Laboratory test of the forward osmosis bag only (2016).", url: "https://ntrs.nasa.gov/citations/20160000310"}
  - {name: "Honeywell/NASA Cascade Distillation System (CDS)", compare: "A multi-stage vacuum rotary distiller meant to replace the ISS urine distiller rather than the brine processor. NASA judged its controls simpler and more reliable, but a brine step would still be needed for 98%.", status: "Ground prototype; flight-like CDS 2.0 design reviewed in 2015. Not flown.", url: "https://ntrs.nasa.gov/citations/20150021780"}
  - {name: "Lunar polar ice as make-up water (open loop)", compare: "Instead of squeezing the last few percent from brine, mine water ice and accept higher losses. It avoids recycling hardware but needs mining, transport and purification, and the size of the deposits is not yet known.", status: "Surface ice confirmed in 2018 in permanently shadowed craters; no extraction yet.", url: "https://www.jpl.nasa.gov/news/ice-confirmed-at-the-moons-poles"}
links:
  - {title: "NASA: NASA achieves water recovery milestone on International Space Station", url: "https://www.nasa.gov/missions/station/iss-research/nasa-achieves-water-recovery-milestone-on-international-space-station/", kind: official, date: "Jun 2023"}
  - {title: "NASA NTRS: Status of ISS Water Management and Recovery (ICES-2024-317)", url: "https://ntrs.nasa.gov/citations/20240005472", kind: official, date: "Jul 2024"}
  - {title: "NASA NTRS: Status of ISS Water Management and Recovery (ICES 2026)", url: "https://ntrs.nasa.gov/citations/20260004140", kind: official, date: "Jul 2026"}
  - {title: "NASA NTRS: Brine Processor Assembly ground testing for ISS contingency planning and exploration reliability (ICES 2026-193)", url: "https://ntrs.nasa.gov/citations/20260005926", kind: official, date: "Jul 2026"}
  - {title: "NASA NTRS: Evaluation of brine processing technologies for spacecraft wastewater", url: "https://ntrs.nasa.gov/citations/20160001250", kind: paper, date: "Jan 2016"}
  - {title: "NASA NTRS: Continued development of the Brine Evaporation Bag", url: "https://ntrs.nasa.gov/citations/20190001333", kind: paper, date: "Mar 2019"}
  - {title: "NASA NTRS: Forward Osmosis Brine Drying", url: "https://ntrs.nasa.gov/citations/20160000310", kind: paper, date: "Jan 2016"}
  - {title: "NASA NTRS: Exploration-class Cascade Distillation System, flight-like prototype design status", url: "https://ntrs.nasa.gov/citations/20150021780", kind: paper, date: "Nov 2015"}
  - {title: "NASA NTRS: Lunar logistics drivers and needs", url: "https://ntrs.nasa.gov/api/citations/20230016304/downloads/Lunar%20Logistics%20Drivers%20and%20Needs.pdf", kind: official, date: "2023"}
  - {title: "NASA JPL: Ice confirmed at the Moon's poles", url: "https://www.jpl.nasa.gov/news/ice-confirmed-at-the-moons-poles", kind: official, date: "Aug 2018"}
  - {title: "Wikipedia: ISS ECLSS", url: "https://en.wikipedia.org/wiki/ISS_ECLSS", kind: wiki, date: "2026"}
  - {title: "Space.com: ISS hits 98% water recycling milestone", url: "https://www.space.com/astronaut-pee-iss-water-recycling-98-percent-milestone", kind: press, date: "Jun 2023"}
---

## What it is

The International Space Station recycles almost all of its water. Its Water Recovery System has two main racks: a Urine Processor Assembly (UPA) and a Water Processor Assembly (WPA). They were delivered to the station on 14 November 2008 and sit in the Node 3 module ([NASA NTRS, 2024](https://ntrs.nasa.gov/citations/20240005472)). The UPA distils urine, but it leaves behind a salty brine that still holds water. For years that brine was thrown away.

The Brine Processor Assembly (BPA) closes that gap. It was built by Paragon Space Development and has been installed on the station since March 2021 as a technology demonstration for exploration missions ([NASA NTRS, 2024](https://ntrs.nasa.gov/citations/20240005472)). Paragon's membrane design was one of four brine dryers NASA tested side by side before choosing a technology ([NASA NTRS, 2016](https://ntrs.nasa.gov/citations/20160001250)).

Before the BPA, total station water recovery was 93-94%. In June 2023 NASA reported that, with the BPA, it reached 98%, which is NASA's goal for long missions ([NASA](https://www.nasa.gov/missions/station/iss-research/nasa-achieves-water-recovery-milestone-on-international-space-station/); [Space.com](https://www.space.com/astronaut-pee-iss-water-recycling-98-percent-milestone)). The latest NASA status paper reports 81 dewatering cycles since first activation. In the most recent reporting period alone the BPA processed about 946 L of urine brine and returned an estimated 780 L of water ([NASA NTRS, 2026](https://ntrs.nasa.gov/citations/20260004140)).

## Why Open Moon uses it

Water is heavy. With open-loop life support, water and gases make up about half of all logistics mass for a lunar crew, and closing the water and oxygen loops can largely remove that need ([NASA NTRS, lunar logistics](https://ntrs.nasa.gov/api/citations/20230016304/downloads/Lunar%20Logistics%20Drivers%20and%20Needs.pdf)). Each crew member needs about a gallon of water a day for drinking, food and hygiene ([NASA](https://www.nasa.gov/missions/station/iss-research/nasa-achieves-water-recovery-milestone-on-international-space-station/)).

Open Moon installs this system before the first crew lands (**M08**) and relies on it in **M09, the crewed base**. The exit criteria for that milestone ask for at least 90% water recovery averaged over a year, and resupply mass per crew-day cut by at least 40%. ISS-class recycling gives the margin above 90%. The brine processor adds the last few percent and reduces brine that must be stored or thrown away ([NASA NTRS, 2026](https://ntrs.nasa.gov/citations/20260004140)). Without it, the base would still recycle most of its water, but more make-up water would have to come from Earth or from polar ice (M06).

## How it works

1. **Urine processing.** Urine is treated with an oxidiser and acid. The UPA then boils it at low pressure in a rotating centrifuge and recompresses the vapour to save energy ([NASA NTRS, 2024](https://ntrs.nasa.gov/citations/20240005472)).
2. **Brine processing.** The leftover brine fills a bladder made of a special membrane. Warm, dry air is blown over it, and water vapour passes through the membrane ([NASA](https://www.nasa.gov/missions/station/iss-research/nasa-achieves-water-recovery-milestone-on-international-space-station/)). NASA describes this as membrane distillation with heated forced convection ([NASA NTRS, 2026](https://ntrs.nasa.gov/citations/20260004140)).
3. **Humidity capture.** The moist air goes into the cabin. The station's normal dehumidifiers collect it along with crew breath and sweat ([NASA](https://www.nasa.gov/missions/station/iss-research/nasa-achieves-water-recovery-milestone-on-international-space-station/)).
4. **Water processing.** The WPA filters all collected water, breaks down trace contaminants in a catalytic reactor, checks purity with sensors, reprocesses bad water, and adds iodine to stop microbes ([NASA](https://www.nasa.gov/missions/station/iss-research/nasa-achieves-water-recovery-milestone-on-international-space-station/)).

| Specification | Value |
|---|---|
| UPA design load | 9 kg/day of urine and flush water (6 crew) ([NTRS](https://ntrs.nasa.gov/citations/20240005472)) |
| UPA recovery from US urine | 85% design; 87% now; 90% targeted ([NTRS](https://ntrs.nasa.gov/citations/20240005472)) |
| Brine produced on ISS | about 1.2 L/day ([NTRS](https://ntrs.nasa.gov/citations/20190001333)) |
| Total recovery without BPA | 93-94% ([NASA](https://www.nasa.gov/missions/station/iss-research/nasa-achieves-water-recovery-milestone-on-international-space-station/)) |
| Total recovery with BPA | 98% ([NASA](https://www.nasa.gov/missions/station/iss-research/nasa-achieves-water-recovery-milestone-on-international-space-station/)) |
| Ground test, new bladder | 22.5 L feed, 95.4% recovery, about 2.7 kg/day ([NTRS](https://ntrs.nasa.gov/citations/20260005926)) |
| BPA mass, power, volume | Not published in the sources we found |

## Limitations and open issues

- **Consumable bladders.** Crew must swap the BPA bladder and filters ([NASA](https://www.nasa.gov/missions/station/iss-research/nasa-achieves-water-recovery-milestone-on-international-space-station/)). In ground tests, reusing one bladder dropped recovery from 95.4% to 80.0% and the rate from 2.7 to 1.6 kg/day ([NTRS](https://ntrs.nasa.gov/citations/20260005926)).
- **Sensitive to pauses.** A two-week stop during a ground run caused "pore wetting" of the membrane and odour from the bladder ([NTRS](https://ntrs.nasa.gov/citations/20260005926)).
- **Hardware anomalies.** In 2024 and 2025 the BPA showed odd thermal behaviour linked to a heater inlet temperature switch. A 3D-printed exhaust part had sealing concerns and was replaced in 2025 ([NTRS](https://ntrs.nasa.gov/citations/20260004140)).
- **Urine processor limits.** The UPA's recovery was cut to 75% after urine quality problems in 2009, and Russian-segment urine is still processed at only 70% ([NTRS](https://ntrs.nasa.gov/citations/20240005472)).
- **Membrane sealing is hard.** In NASA's 2016 comparison, an earlier Paragon prototype leaked at bag seams because its Teflon and Nafion materials are difficult to seal ([NTRS](https://ntrs.nasa.gov/citations/20160001250)).
- **Not tested at lunar gravity.** The BPA has run in microgravity on the ISS and at 1 g on the ground at Marshall ([NTRS](https://ntrs.nasa.gov/citations/20260005926)). We found no published test at 1/6 g, or with lunar dust in the cabin.
- **Still a demonstration.** NASA calls the BPA a technology demonstration and a critical step before missions beyond the ISS ([NTRS](https://ntrs.nasa.gov/citations/20260004140)). Reliability data for years of use without resupply is still being gathered.
