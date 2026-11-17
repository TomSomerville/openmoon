---
slug: regenerative-fuel-cells
title: "Regenerative fuel cells"
alternatives:
  - {name: "Lithium-ion batteries", compare: "Simple, efficient and already flown, but heavy for long nights: NASA puts packaged Li-ion at about 160 Wh/kg versus 320-650 Wh/kg for an RFC. Best for short gaps and fast power peaks, which is how Open Moon uses them alongside RFCs.", status: "Flight-proven; the ISS switched its main batteries to Li-ion between 2017 and 2021", url: "https://en.wikipedia.org/wiki/Electrical_system_of_the_International_Space_Station"}
  - {name: "Fission surface power", compare: "Makes power continuously through any length of night instead of storing it, so it removes most of the storage problem. It is heavier as a single unit, needs radiation keep-out distance, and is not yet built.", status: "In development; NASA asked industry in 2025 for a system of at least 100 kWe", url: "https://www.nasa.gov/centers-and-facilities/glenn/nasa-seeks-industry-feedback-on-fission-surface-power/"}
  - {name: "Regolith thermal energy storage", compare: "Stores daytime heat in a pile of local regolith and turns it back into electricity at night, so most of the mass is lunar soil. A 1992 NASA-sponsored design said its mass from Earth compared favourably with an RFC, but it was never built or tested.", status: "Paper concept only", url: "https://ntrs.nasa.gov/citations/19930018795"}
  - {name: "Unitized regenerative fuel cell", compare: "One stack works as both fuel cell and electrolyser, saving a stack. NASA found little mass saving for long lunar nights and slightly lower efficiency, and judged such PEM stacks not yet advanced enough for flight.", status: "Laboratory research", url: "https://ntrs.nasa.gov/citations/20210014627"}
links:
  - {title: "NASA NTRS 20260002730: Performance of a regenerative fuel cell system for the lunar surface", url: "https://ntrs.nasa.gov/citations/20260002730", kind: official, date: "Apr 2026"}
  - {title: "Csank & Scott, NASA GRC: Power and Energy for the Lunar Surface", url: "https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf", kind: official, date: "Apr 2022"}
  - {title: "NASA/TM-20210014627: Lunar equator regenerative fuel cell system efficiency analysis", url: "https://ntrs.nasa.gov/citations/20210014627", kind: official, date: "Aug 2022"}
  - {title: "NASA/TM-20210024659: Aerospace regenerative fuel cell fluidic component design challenges", url: "https://ntrs.nasa.gov/citations/20210024659", kind: official, date: "Jul 2022"}
  - {title: "NASA/TM-20205000357: Analysis of a 100-W regenerative fuel cell demonstration", url: "https://ntrs.nasa.gov/citations/20205000357", kind: official, date: "Aug 2020"}
  - {title: "Energy storage for lunar surface exploration (NASA AMPS study)", url: "https://ntrs.nasa.gov/citations/20190000472", kind: paper, date: "Sep 2018"}
  - {title: "Lunar regenerative fuel cell reliability testing for assured mission success", url: "https://ntrs.nasa.gov/citations/20090013280", kind: paper, date: "Feb 2009"}
  - {title: "Solar airplanes and regenerative fuel cells", url: "https://ntrs.nasa.gov/citations/20080003889", kind: paper, date: "Oct 2007"}
  - {title: "Hydrogen-oxygen PEM regenerative fuel cell development at NASA Glenn Research Center", url: "https://ntrs.nasa.gov/citations/20070010455", kind: paper, date: "2006"}
  - {title: "NASA Image Library: closed-loop regenerative fuel cell rig (GRC-2009-C-04808)", url: "https://images.nasa.gov/details/GRC-2009-C-04808", kind: official, date: "Dec 2005"}
  - {title: "Wikipedia: Regenerative fuel cell", url: "https://en.wikipedia.org/wiki/Regenerative_fuel_cell", kind: wiki, date: "2026"}
  - {title: "Regolith thermal energy storage for lunar nighttime power", url: "https://ntrs.nasa.gov/citations/19930018795", kind: paper, date: "Feb 1992"}
  - {title: "NASA: NASA seeks industry feedback on fission surface power", url: "https://www.nasa.gov/centers-and-facilities/glenn/nasa-seeks-industry-feedback-on-fission-surface-power/", kind: official, date: "Aug 2025"}
  - {title: "Wikipedia: Electrical system of the International Space Station", url: "https://en.wikipedia.org/wiki/Electrical_system_of_the_International_Space_Station", kind: wiki, date: "2026"}
---

## What it is

A regenerative fuel cell (RFC) is a rechargeable energy store built from water. During the day, an electrolyser uses spare solar power to split water into hydrogen and oxygen. At night, a fuel cell recombines the gases to make electricity, heat and water again ([Wikipedia](https://en.wikipedia.org/wiki/Regenerative_fuel_cell)). NASA's appeal is weight: it estimates 320 to 650 Wh/kg for a lunar RFC, against about 160 Wh/kg for packaged Li-ion batteries ([Csank & Scott, NASA](https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf)).

NASA Glenn Research Center started work on a closed-cycle hydrogen-oxygen RFC in 1998, at first to keep a solar aircraft flying through the night ([NASA](https://ntrs.nasa.gov/citations/20080003889)). By 2006 its rig had become the first fully closed RFC ever demonstrated, with round-trip efficiency of up to 52% ([NASA GRC](https://ntrs.nasa.gov/citations/20070010455); [photo](https://images.nasa.gov/details/GRC-2009-C-04808)). The Constellation programme then picked RFCs as the baseline night storage for its lunar outpost and crewed rovers ([NASA](https://ntrs.nasa.gov/citations/20090013280)). A 100 W lab demonstration in 2014 ran five cycles at 47.4% round-trip efficiency ([NASA](https://ntrs.nasa.gov/citations/20205000357)).

The latest step is a breadboard system built at Glenn. It ran autonomously for over 550 hours across simulated lunar day/night cycles ([NASA NTRS](https://ntrs.nasa.gov/citations/20260002730)). That test was open-loop: the gases it made were vented and bottled gas fed the fuel cell. Open Moon rates it TRL 5.

## Why Open Moon uses it

Open Moon's power milestone ([M04](/plan/m04-power/)) needs to keep about 30 kW of essential load alive through about 100 hours of darkness, which is about 3 MWh. NASA gives ~100 h as the south-pole night and 367 h at the equator ([Csank & Scott](https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf)). At 160 Wh/kg that is about 19 t of Li-ion. At 320-650 Wh/kg, RFCs cut it to roughly 5-9 t. RFC waste heat also helps hardware survive the cold ([Csank & Scott](https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf)).

RFCs also fit the base's chemistry. They run on the same water, hydrogen and oxygen as the water plant in M06, so the plan shares tanks between the two. Without RFCs the base would need far more battery mass, or would depend entirely on the fission unit through every shadow period.

## How it works

The NASA breadboard has seven parts: fuel cell stack, electrolyser stack, fluid conditioning, reactant storage, avionics, power management, and thermal control ([NASA NTRS](https://ntrs.nasa.gov/citations/20260002730)). Its proton exchange membrane (PEM) electrolyser compresses the gases itself, to balanced pressures of up to 12.4 MPa, so no separate compressor is needed. A CubeSat processor runs it as a state machine with fault monitoring.

Most of the size is tanks. For a 5 kW south-pole system, gas storage can be 93.5% of system volume ([NASA](https://ntrs.nasa.gov/citations/20190000472)). For long equatorial nights, storage is ~65% of system mass even at 0.1 kW ([NASA TM](https://ntrs.nasa.gov/citations/20210014627)).

| Key figure | Value | Source |
|---|---|---|
| Specific energy (lunar RFC, estimate) | 320-650 Wh/kg | [NASA GRC](https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf) |
| Theoretical max round-trip efficiency | ~80% | [NASA TM](https://ntrs.nasa.gov/citations/20210014627) |
| Demonstrated round-trip efficiency | 47.4% (100 W, 2014); up to 52% (2006) | [NASA](https://ntrs.nasa.gov/citations/20205000357), [NASA GRC](https://ntrs.nasa.gov/citations/20070010455) |
| Electrolyser output pressure | up to 12.4 MPa (1,800 psia) | [NASA NTRS](https://ntrs.nasa.gov/citations/20260002730) |
| Longest system test | 550+ h, open-loop | [NASA NTRS](https://ntrs.nasa.gov/citations/20260002730) |
| Crewed lunar system size range | 36 kWh to over 1 MWh | [NASA GRC](https://ntrs.nasa.gov/api/citations/20220005893/downloads/Power%20and%20Energy%20for%20the%20Lunar%20Surface.pdf) |

## Limitations and open issues

- **Never closed-loop in a lunar test.** The 550-hour run vented its gases and had five unplanned safe-mode stops: four from thermal control, one from water management ([NASA NTRS](https://ntrs.nasa.gov/citations/20260002730)).
- **Low efficiency.** About half the stored energy is lost per cycle, which means bigger solar arrays. An RFC at 50% efficiency needs an array of about 3 times its rated power ([NASA TM](https://ntrs.nasa.gov/citations/20210014627)).
- **Pressure trade-off.** Higher pressure shrinks tanks but hurts efficiency. Cryogenic storage drops round-trip efficiency below 15% ([NASA TM](https://ntrs.nasa.gov/citations/20210014627)).
- **Few flight-ready parts.** Valves, regulators and other fluid parts are mostly commercial items not built for space ([NASA TM](https://ntrs.nasa.gov/citations/20210024659)).
- **Long qualification.** NASA estimated that reliability testing alone for a crew-rated RFC would take 2 to 6 years ([NASA](https://ntrs.nasa.gov/citations/20090013280)).
- **No flight hardware and no published cost.** No RFC has flown to the Moon, and NASA has not published a price for a 3 MWh system. Open Moon's cost and mass figures for it are estimates.
