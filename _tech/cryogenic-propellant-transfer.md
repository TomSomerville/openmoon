---
slug: cryogenic-propellant-transfer
title: "Cryogenic propellant transfer"
alternatives:
  - {name: "Blue Origin LH2/LOX transporter with zero boil-off storage", compare: "Moves liquid hydrogen and oxygen instead of methane and oxygen, and relies on cryocoolers to stop boil-off over long stays in orbit. Hydrogen gives more performance but is far harder to keep cold, so it raises the bar for storage technology.", status: "In development for Artemis V; NASA OIG expected Blue Origin's uncrewed demo, which shows its cryogenic transfer, in February 2029", url: "https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf"}
  - {name: "Storable (hypergolic) propellant refuelling", compare: "Room-temperature propellants do not boil off, so transfer between docked vehicles is routine. They cannot be made from lunar oxygen and give lower performance than cryogenic propellants.", status: "Flight proven; China's Tianzhou 1 refuelled the Tiangong-2 lab three times in 2017", url: "https://en.wikipedia.org/wiki/Tianzhou_1"}
  - {name: "Satellite-servicing fluid transfer (Orbital Express style)", compare: "Small robotic transfer of storable hydrazine between purpose-built satellites. Proves docking couplers and pumps but at tiny scale and without the boil-off and two-phase flow problems of cryogens.", status: "Demonstrated by the US military Orbital Express mission in 2007", url: "https://en.wikipedia.org/wiki/Orbital_Express"}
  - {name: "Single-launch, no-refuelling lander (Apollo style)", compare: "Launch the lander fully fuelled on one large rocket and refuel nothing in space. Simple and proven, but it limits payload, and the Apollo Lunar Module used hypergolic propellants that the Moon cannot supply.", status: "Flight proven in the Apollo programme; no current heavy lander uses this approach for large cargo", url: "https://en.wikipedia.org/wiki/Apollo_Lunar_Module"}
links:
  - {title: "NASA HLS IAC 2026 presentation (large-scale propellant transfer test on HLS schedule)", url: "https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf", kind: official, date: "Oct 2026"}
  - {title: "NASA OIG IG-26-004: NASA's management of the Human Landing System contracts", url: "https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf", kind: official, date: "Mar 2026"}
  - {title: "NASA: Cryogenic Fluid Management (CFM) portfolio", url: "https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/cryogenic-fluid-management-cfm/", kind: official, date: "accessed Nov 2026"}
  - {title: "NASA: Cryogenic Fluid Management fact sheet", url: "https://www.nasa.gov/wp-content/uploads/2024/01/cryogenicfluidmanagement-factsheet.pdf", kind: official, date: "Jan 2024"}
  - {title: "NASA: NASA, industry prepare cryogenic fuel technology demo (LOXSAT)", url: "https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/cryogenic-fluid-management-cfm/nasa-industry-prepare-cryogenic-fuel-technology-demo/", kind: official, date: "May 2026"}
  - {title: "NASA: Liquid Oxygen Flight Demonstration (LOXSAT) project page", url: "https://www.nasa.gov/space-travel-technology/liquid-oxygen-flight-demonstration/", kind: official, date: "Nov 2026"}
  - {title: "NASA: NASA tests new device for future in-space refueling missions (cryocoupler)", url: "https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/cryogenic-fluid-management-cfm/nasa-tests-new-refuel-device-for-future-in-space-refueling-missions/", kind: official, date: "Jun 2026"}
  - {title: "NASA: Ice to Fuel, NASA tests technology for refueling landers (CryoFILL)", url: "https://www.nasa.gov/general/nasa-tests-lander-refueling-tech/", kind: official, date: "Mar 2026"}
  - {title: "Hansen et al., Cryogenic Fluid Management Technologies Enabling for the Artemis Program and Beyond (AIAA ASCEND)", url: "https://ntrs.nasa.gov/citations/20205008297", kind: paper, date: "Nov 2020"}
  - {title: "Starship HLS, Wikipedia", url: "https://en.wikipedia.org/wiki/Starship_HLS", kind: wiki, date: "accessed Nov 2026"}
  - {title: "Starship flight 15, Wikipedia", url: "https://en.wikipedia.org/wiki/Starship_flight_15", kind: wiki, date: "Nov 2026"}
  - {title: "Orbital propellant depot, Wikipedia", url: "https://en.wikipedia.org/wiki/Orbital_propellant_depot", kind: wiki, date: "accessed Nov 2026"}
  - {title: "Robotic Refueling Mission, Wikipedia", url: "https://en.wikipedia.org/wiki/Robotic_Refueling_Mission", kind: wiki, date: "accessed Nov 2026"}
  - {title: "List of Electron launches (LOXSAT launch date), Wikipedia", url: "https://en.wikipedia.org/wiki/List_of_Electron_launches", kind: wiki, date: "accessed Nov 2026"}
---

## What it is

Cryogenic propellant transfer means moving super-cold liquid propellants, such as liquid oxygen, liquid methane or liquid hydrogen, from one tank or vehicle to another away from a launch pad. It is one part of what NASA calls [cryogenic fluid management](https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/cryogenic-fluid-management-cfm/): the technologies that store, transfer and measure ultra-cold fluids. Liquid oxygen must be kept at about [minus 300 °F](https://www.nasa.gov/space-travel-technology/liquid-oxygen-flight-demonstration/) or it boils into vapour.

NASA has worked on this [since the 1960s](https://ntrs.nasa.gov/citations/20205008297), but many planned flight experiments were cancelled. In 2020 NASA engineers wrote that the state of the art for storing cryogens in space was [fourteen hours](https://ntrs.nasa.gov/citations/20205008297). Storable hydrazine has been moved between satellites, as on [Orbital Express in 2007](https://en.wikipedia.org/wiki/Orbital_propellant_depot). Cryogens have not. NASA's [Robotic Refueling Mission 3](https://en.wikipedia.org/wiki/Robotic_Refueling_Mission) stored methane on the ISS for four months, but its cryocooler failed and no transfer took place. On [Starship Flight 3](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf) in March 2024, SpaceX moved propellant between two tanks inside one vehicle.

Today, both Artemis landers depend on it. SpaceX's Starship lander uses liquid oxygen and methane, and Blue Origin's Blue Moon uses liquid oxygen and hydrogen ([NASA OIG](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf)). A large-scale, ship-to-ship transfer test was planned for March 2025 and then slipped to March 2026. In October 2026 NASA still listed it as an upcoming milestone, shown around [Q1 2027](https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf). Starship reached orbit on [Flight 15 in November 2026](https://en.wikipedia.org/wiki/Starship_flight_15), but it had still not shown refuelling in orbit.

## Why Open Moon uses it

Open Moon uses this technology for **refuelling landers**. It matters at two points in the plan:

- **Heavy cargo (M02).** The heavy landers that carry habitats and reactors are refuelled in Earth orbit before they go to the Moon. Starship needs a depot filled by [more than 10 tanker flights](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf). Blue Moon needs a transporter and refuelers.
- **Propellant and industrial ISRU (M11).** The M11 depot stores and moves cryogens at the landing pads, so landers can fill up with oxygen made on the Moon. M11's exit criteria include refuelling at least one lander with lunar oxygen. NASA's [CryoFILL project](https://www.nasa.gov/general/nasa-tests-lander-refueling-tech/) is working towards the same goal: liquefy oxygen on the surface and fuel landers where they land.

Without it, every heavy item would need its own fully fuelled launch. That would cut the mass per landing, and lunar oxygen would have nowhere to go. The plan's fallback is to split heavy items into medium-lander pieces.

## How it works

A transfer needs several parts working together ([NASA fact sheet](https://www.nasa.gov/wp-content/uploads/2024/01/cryogenicfluidmanagement-factsheet.pdf)):

- **Storage.** Multilayer insulation slows heat leak. Cryocoolers remove the rest, like a refrigerator, giving near "zero boil-off".
- **Liquid acquisition.** In microgravity liquid floats and clings to walls. A [LOXSAT page](https://www.nasa.gov/space-travel-technology/liquid-oxygen-flight-demonstration/) explains that this makes it hard to pull liquid, not gas, from a tank. Small thrusts can settle it, or devices inside the tank can trap it.
- **Couplers and lines.** Docked vehicles connect through automated couplers. NASA and L3Harris tested a [cryocoupler](https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/cryogenic-fluid-management-cfm/nasa-tests-new-refuel-device-for-future-in-space-refueling-missions/) with liquid nitrogen at minus 321 °F. It must reconnect many times and tolerate misalignment.
- **Pressure control and gauging.** Tanks must be kept at the right pressure without venting, and the amount of liquid must be measured while it floats.

| Item | Value | Source |
|---|---|---|
| Starship propellants | Liquid oxygen + liquid methane | [NASA OIG](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf) |
| Blue Moon propellants | Liquid oxygen + liquid hydrogen | [NASA OIG](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf) |
| Starship tanker flights per mission | More than 10 (NASA OIG); 4 to 14 (Wikipedia) | [OIG](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf), [Wikipedia](https://en.wikipedia.org/wiki/Starship_HLS) |
| Planned tanker cadence | One every 6 days; aggregation starts more than 200 days before crew launch | [NASA OIG](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf) |
| LOXSAT demo | 11 CFM technologies over 9 months | [NASA](https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/cryogenic-fluid-management-cfm/nasa-industry-prepare-cryogenic-fuel-technology-demo/) |
| Flow rates, transfer losses | Not published | |

Before a lunar mission, SpaceX must fly a long-duration test of [storage and boil-off](https://en.wikipedia.org/wiki/Starship_HLS), then a ship-to-ship transfer. NASA's small LOXSAT demo with Eta Space will test oxygen transfer, storage and pressure control. NASA gave its launch as [no earlier than 17 July 2026](https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/cryogenic-fluid-management-cfm/nasa-industry-prepare-cryogenic-fuel-technology-demo/); Wikipedia later listed it for [November 2026](https://en.wikipedia.org/wiki/List_of_Electron_launches).

## Limitations and open issues

- **Never done between vehicles.** NASA's OIG says the methods are [entirely new](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf) and NASA tracks immature cryogenic technology as a top risk. A NASA manager called it [one of the toughest engineering challenges in spaceflight](https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/cryogenic-fluid-management-cfm/nasa-tests-new-refuel-device-for-future-in-space-refueling-missions/).
- **Repeated slips.** The Starship test has slipped from March 2025 to [around Q1 2027](https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf). Blue Origin's transfer demo is expected in [February 2029](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf).
- **Launch cadence.** SpaceX had not yet shown the [12- to 24-day pad turnover](https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf) that tanker flights need.
- **Boil-off.** Cryocoolers can fail, as on [RRM3](https://en.wikipedia.org/wiki/Robotic_Refueling_Mission), and venting in microgravity wastes propellant ([NASA fact sheet](https://www.nasa.gov/wp-content/uploads/2024/01/cryogenicfluidmanagement-factsheet.pdf)).
- **Surface transfer is a different problem.** Lunar gravity helps settle liquid, but lunar dust, day-night temperature swings and couplers at the pads are untested. NASA's [cryocoupler](https://www.nasa.gov/directorates/stmd/tech-demo-missions-program/cryogenic-fluid-management-cfm/nasa-tests-new-refuel-device-for-future-in-space-refueling-missions/) work is still at basic-function testing.
- **No published performance data.** Flow rates, chilldown losses and total transfer efficiency for the Starship and Blue Moon systems are not public.
