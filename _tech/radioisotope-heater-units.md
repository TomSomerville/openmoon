---
slug: radioisotope-heater-units
title: "Radioisotope heater units"
alternatives:
  - {name: "Electric heaters on batteries", compare: "Uses stored solar power instead of a radioactive source, so there is no nuclear launch approval. But heaters can take up to half of an electronics system's power, and the batteries themselves need warming below about 0 C, so a long night needs a much bigger battery.", status: "Standard on every spacecraft; the usual choice for short missions that do not try to survive the night", url: "https://technology.nasa.gov/patent/MFS-TOPS-134"}
  - {name: "Passive thermal switches (NASA wax-actuated PCB switch)", compare: "Does not make heat. It cuts the heat path from the electronics to the cold enclosure when temperatures fall, so the electronics keep their own heat. It needs no power and could cost under $100 per unit, but it only slows cooling and cannot keep a box warm through a full night alone.", status: "Patented NASA design offered for licensing; flight use not stated", url: "https://technology.nasa.gov/patent/MFS-TOPS-134"}
  - {name: "Americium-241 heater units (ESA programme)", compare: "Same idea, but fuelled with americium-241, which Europe can source itself. Am-241 has about five times the half-life of Pu-238 but lower power per gram, so units are heavier for the same heat.", status: "In development under ESA funding since 2009; prototypes tested in the lab; not yet flown", url: "https://doi.org/10.1007/s11214-019-0623-9"}
  - {name: "Polonium-210 heat source", compare: "Used by the Soviet Lunokhod rovers. Po-210 gives more heat per gram, but its half-life is only about 138 days, so it suits only short missions.", status: "Flown on Lunokhod 1 (1970); not produced for current missions", url: "https://en.wikipedia.org/wiki/Lunokhod_1"}
  - {name: "Fission surface power (electric heating)", compare: "A 40 kWe-class reactor could power electric heaters for a whole base with no night limit. It is far too large for a small prospecting rover, and it must be set up at least about 1 km from users.", status: "Concept design stage with NASA and DOE; not yet built", url: "https://ntrs.nasa.gov/api/citations/20220004670/downloads/40%20kW%20Deployable%20FSP%20Paper_FINAL.pdf"}
links:
  - {title: "NASA RPS: Thermal systems, Radioisotope Heater Units (missions and RHU counts)", url: "https://science.nasa.gov/planetary-science/programs/radioisotope-power-systems/thermal-radioisotope-heater-units/", kind: official, date: "Aug 2026"}
  - {title: "NASA: Radioisotope Heater Units fact sheet", url: "https://science.nasa.gov/resource/radioisotope-heater-units-fact-sheet/", kind: official, date: "Apr 2016"}
  - {title: "DOE Facts: Radioisotope Heater Units (design and safety)", url: "https://assets.science.nasa.gov/content/dam/science/psd/solar/2023/09/r/rhu.pdf", kind: official, date: "Dec 1998"}
  - {title: "NASA Discovery AO: Lightweight Radioisotope Heater Unit (LWRHU) information summary", url: "https://discovery.larc.nasa.gov/PDF_FILES/6RHU_Description.pdf", kind: official, date: "Sep 2009"}
  - {title: "NASA Science: Cassini's radioisotope thermoelectric generators (82 RHUs, one watt each)", url: "https://science.nasa.gov/mission/cassini/radioisotope-thermoelectric-generator", kind: official, date: "accessed Nov 2026"}
  - {title: "NASA RPS: About Plutonium-238", url: "https://science.nasa.gov/planetary-science/programs/radioisotope-power-systems/about-plutonium-238/", kind: official, date: "accessed Nov 2026"}
  - {title: "NASA Technology Transfer: Passive PCB-Mounted Thermal Switch (MFS-TOPS-134)", url: "https://technology.nasa.gov/patent/MFS-TOPS-134", kind: official, date: "accessed Nov 2026"}
  - {title: "Ambrosi et al., European RTGs and RHUs for Space Science and Exploration, Space Science Reviews", url: "https://doi.org/10.1007/s11214-019-0623-9", kind: paper, date: "Dec 2019"}
  - {title: "Oleson et al., A Deployable 40 kWe Lunar Fission Surface Power Concept (NASA NTRS)", url: "https://ntrs.nasa.gov/api/citations/20220004670/downloads/40%20kW%20Deployable%20FSP%20Paper_FINAL.pdf", kind: paper, date: "2022"}
  - {title: "Radioisotope heater unit, Wikipedia", url: "https://en.wikipedia.org/wiki/Radioisotope_heater_unit", kind: wiki, date: "accessed Nov 2026"}
  - {title: "Lunokhod 1, Wikipedia", url: "https://en.wikipedia.org/wiki/Lunokhod_1", kind: wiki, date: "accessed Nov 2026"}
  - {title: "Yutu (rover), Wikipedia", url: "https://en.wikipedia.org/wiki/Yutu_(rover)", kind: wiki, date: "accessed Nov 2026"}
  - {title: "Chang'e 4, Wikipedia", url: "https://en.wikipedia.org/wiki/Chang%27e_4", kind: wiki, date: "accessed Nov 2026"}
  - {title: "Chandrayaan-3, Wikipedia", url: "https://en.wikipedia.org/wiki/Chandrayaan-3", kind: wiki, date: "accessed Nov 2026"}
---

## What it is

A radioisotope heater unit (RHU) is a small, sealed heat source. It holds one pellet of plutonium dioxide, mostly plutonium-238, about the size of a pencil eraser. The natural decay of the pellet gives off about one watt of heat, with no moving parts and no electronics ([NASA](https://science.nasa.gov/planetary-science/programs/radioisotope-power-systems/thermal-radioisotope-heater-units/)). The whole unit is about the size of a C-cell battery. The US Department of Energy (DOE) builds them, with Oak Ridge, Idaho and Los Alamos national laboratories, and NASA buys them for its missions ([NASA Discovery](https://discovery.larc.nasa.gov/PDF_FILES/6RHU_Description.pdf)).

RHUs have a long flight record. Apollo 11's seismic experiment package on the Moon carried 2. Galileo carried 103 on the orbiter and 17 on its probe. Cassini carried 82, and its Huygens probe 35. Sojourner, Spirit and Opportunity on Mars also used them ([NASA](https://science.nasa.gov/planetary-science/programs/radioisotope-power-systems/thermal-radioisotope-heater-units/), [NASA Cassini](https://science.nasa.gov/mission/cassini/radioisotope-thermoelectric-generator)). Other nations use them on the Moon too. The Soviet Lunokhod 1 rover used a polonium-210 heater and worked for eleven lunar days ([Wikipedia](https://en.wikipedia.org/wiki/Lunokhod_1)). China's Yutu and Yutu-2 rovers and their landers used them ([Wikipedia](https://en.wikipedia.org/wiki/Yutu_(rover)), [Wikipedia](https://en.wikipedia.org/wiki/Chang%27e_4)). India flew two units on the Chandrayaan-3 propulsion module ([Wikipedia](https://en.wikipedia.org/wiki/Chandrayaan-3)).

## Why Open Moon uses it

RHUs belong to milestone M01, robotic prospecting, in Phase 0. The two prospector rovers park in sunlight to recharge, then drive into permanently shadowed regions (PSRs) to drill for ice. RHUs keep their electronics alive in the dark and through the lunar night.

The Moon's night lasts about 14 Earth days, with lows near -173 C ([NASA](https://technology.nasa.gov/patent/MFS-TOPS-134)). Without RHUs, the rovers would need electric heaters. Heaters can use up to half of an electronics system's power, and common batteries stop working near 0 C, so they need heat too ([NASA](https://technology.nasa.gov/patent/MFS-TOPS-134)). That means bigger batteries and shorter trips into the shadow. RHUs give steady heat whatever the sunlight, and leave the batteries for driving, drilling and instruments ([NASA Discovery](https://discovery.larc.nasa.gov/PDF_FILES/6RHU_Description.pdf)).

## How it works

The fuel is a ceramic form of plutonium dioxide. It tends to break into large pieces rather than fine dust if damaged ([DOE](https://assets.science.nasa.gov/content/dam/science/psd/solar/2023/09/r/rhu.pdf)). The pellet sits in a platinum-rhodium metal clad. Around that are graphite insulators and a graphite aeroshell that protect it from impact, fire and re-entry. Each pellet has its own shell, so one accident is less likely to breach several units. The heat flows straight into the part it is bolted to. Designers place many units near the parts that must stay warm.

| Specification | Value | Source |
|---|---|---|
| Heat output | About 1 W thermal (0.88-0.94 W for inventory units in 2009) | [NASA Discovery](https://discovery.larc.nasa.gov/PDF_FILES/6RHU_Description.pdf) |
| Size | 3.2 cm long, 2.6 cm diameter | [DOE](https://assets.science.nasa.gov/content/dam/science/psd/solar/2023/09/r/rhu.pdf) |
| Mass | About 40 g per unit; fuel pellet about 2.7 g | [DOE](https://assets.science.nasa.gov/content/dam/science/psd/solar/2023/09/r/rhu.pdf) |
| Fuel | Plutonium dioxide, mostly Pu-238 | [NASA](https://science.nasa.gov/resource/radioisotope-heater-units-fact-sheet/) |
| Half-life of Pu-238 | About 88 years | [NASA](https://science.nasa.gov/planetary-science/programs/radioisotope-power-systems/about-plutonium-238/) |
| Heat per gram of Pu-238 | 0.57 W | [Wikipedia](https://en.wikipedia.org/wiki/Radioisotope_heater_unit) |
| Hardware price (2009 guidance) | About $3,000 per unit, excluding launch approval costs | [NASA Discovery](https://discovery.larc.nasa.gov/PDF_FILES/6RHU_Description.pdf) |

## Limitations and open issues

- **Small output.** One unit gives about one watt. A rover box may need many units, and the heat cannot be switched off. Integration at the launch site has to handle high temperatures and radiation safety for workers ([NASA Discovery](https://discovery.larc.nasa.gov/PDF_FILES/6RHU_Description.pdf)).
- **Slow, costly approval.** Any US mission with RHUs needs environmental review under NEPA, nuclear launch safety approval and launch-site emergency planning. These are multi-year processes. DOE wants the launch vehicle data book at least three years before launch ([NASA Discovery](https://discovery.larc.nasa.gov/PDF_FILES/6RHU_Description.pdf)). This drives the M01 schedule.
- **Fuel supply.** US production of Pu-238 stopped in the late 1980s and only restarted with funding from 2011 ([NASA](https://science.nasa.gov/planetary-science/programs/radioisotope-power-systems/about-plutonium-238/)). The 2009 Discovery offer covered only units already in inventory ([NASA Discovery](https://discovery.larc.nasa.gov/PDF_FILES/6RHU_Description.pdf)). We found no published current price, stock level or process for a non-NASA mission to obtain units.
- **Output fades.** Older units in DOE's 2009 inventory had already dropped below 1 W ([NASA Discovery](https://discovery.larc.nasa.gov/PDF_FILES/6RHU_Description.pdf)).
- **Instrument interference.** NASA picked Pu-238 partly for its relatively low neutron and gamma emissions ([NASA](https://science.nasa.gov/planetary-science/programs/radioisotope-power-systems/about-plutonium-238/)). The prospector carries a neutron spectrometer, and we found no published data on RHU background in lunar neutron instruments. This needs testing.
- **European option not ready.** Americium-241 units have been in development since 2009 but have not flown ([Ambrosi et al.](https://doi.org/10.1007/s11214-019-0623-9)).
