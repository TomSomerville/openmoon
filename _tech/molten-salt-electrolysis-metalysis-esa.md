---
slug: molten-salt-electrolysis-metalysis-esa
title: "Molten salt electrolysis (Metalysis/ESA)"
alternatives:
  - {name: "Molten regolith electrolysis (NASA + Lunar Resources)", compare: "Melts the regolith itself at higher temperature and passes current through the melt, so no salt bath is needed. It makes oxygen plus molten iron and silicon, but needs hotter, more corrosion-resistant hardware.", status: "TRL 4: in 2024 a 25 kg simulant batch was processed in vacuum at about 0.07 kg O2 per hour for 9 hours", url: "https://ntrs.nasa.gov/citations/20260006167"}
  - {name: "Carbothermal reduction (Sierra Space + NASA)", compare: "Heats regolith with methane so carbon pulls oxygen out as carbon monoxide and dioxide, then recovers the oxygen in a second step. Further along in testing, but it does not leave a useful metal product and must recycle carbon.", status: "Flight-like reactor ran automated in NASA's dirty thermal-vacuum chamber in 2024; key hardware matured to TRL 6", url: "https://ntrs.nasa.gov/citations/20250004151"}
  - {name: "Blue Origin Blue Alchemist", compare: "A molten regolith electrolysis system aimed at oxygen plus iron, silicon and aluminium, with silicon used for solar cells. Commercially funded, but few test numbers are public.", status: "Passed critical design review in Sep 2025; autonomous demo in a simulated lunar environment planned for 2026", url: "https://www.blueorigin.com/news/blue-alchemist-hits-major-milestone-toward-permanent-sustainable-lunar-infrastructure"}
  - {name: "ROXY (Airbus)", compare: "Another European process that turns regolith into oxygen and metals for additive manufacturing. Airbus has released very few technical details, so it is hard to compare directly.", status: "Oxygen extracted from simulant in laboratory tests at Fraunhofer IFAM in 2020; funded by ESA", url: "https://www.airbus.com/en/newsroom/press-releases/2020-10-roxy-turns-moon-dust-into-oxygen"}
links:
  - {title: "ESA: ESA opens oxygen plant, making air out of moondust", url: "https://www.esa.int/Enabling_Support/Space_Engineering_Technology/ESA_opens_oxygen_plant_making_air_out_of_moondust", kind: official, date: "Jan 2020"}
  - {title: "ESA: British technology to turn Moon dust into oxygen", url: "https://www.esa.int/Space_in_Member_States/United_Kingdom/British_technology_to_turn_Moon_dust_into_oxygen", kind: official, date: "Nov 2020"}
  - {title: "ESA: Oxygen and metal powder extracted from moonrocks", url: "https://www.esa.int/Space_in_Member_States/United_Kingdom/Oxygen_and_metal_powder_extracted_from_moonrocks", kind: official, date: "Aug 2021"}
  - {title: "Thales Alenia Space: Study contract to develop a payload to extract oxygen on the Moon", url: "https://www.thalesaleniaspace.com/en/press-releases/thales-alenia-space-wins-study-contract-develop-payload-extract-oxygen-moon", kind: official, date: "Feb 2022"}
  - {title: "Danish Technological Institute: Researchers turn lunar soil into Moon-made electronics", url: "https://www.dti.dk/services/researchers-turn-lunar-soil-into-moon-made-electronics/47664", kind: official, date: "Jan 2026"}
  - {title: "Lomax et al.: Proving the viability of an electrochemical process for the simultaneous extraction of oxygen and production of metal alloys from lunar regolith (Planetary and Space Science 180)", url: "https://eprints.gla.ac.uk/196778", kind: paper, date: "Sep 2019"}
  - {title: "Meurisse et al.: Lower temperature electrochemical reduction of lunar regolith simulants in molten salts (Planetary and Space Science 211)", url: "https://doi.org/10.1016/j.pss.2021.105408", kind: paper, date: "Feb 2022"}
  - {title: "Lomax et al.: Identifying an efficient endpoint for oxygen extraction from lunar regolith simulant pellets using molten salt electrolysis (Acta Astronautica 234)", url: "https://eprints.gla.ac.uk/355741", kind: paper, date: "Apr 2025"}
  - {title: "Chen, Fray and Farthing: Direct electrochemical reduction of titanium dioxide to titanium in molten calcium chloride (Nature 407)", url: "https://doi.org/10.1038/35030069", kind: paper, date: "Sep 2000"}
  - {title: "Wikipedia: FFC Cambridge process", url: "https://en.wikipedia.org/wiki/FFC_Cambridge_process", kind: wiki, date: ""}
  - {title: "NASA NTRS: Molten regolith electrolysis ground demonstration (ICES 2026)", url: "https://ntrs.nasa.gov/citations/20260006167", kind: official, date: "2026"}
  - {title: "NASA NTRS 20250004151: Carbothermal oxygen production reactor testing", url: "https://ntrs.nasa.gov/citations/20250004151", kind: official, date: "2025"}
  - {title: "Airbus: ROXY turns Moon dust into oxygen", url: "https://www.airbus.com/en/newsroom/press-releases/2020-10-roxy-turns-moon-dust-into-oxygen", kind: official, date: "Oct 2020"}
---

## What it is

Molten salt electrolysis pulls oxygen out of lunar rock without melting the rock. Regolith sits in a metal basket inside molten calcium chloride salt. An electric current strips the oxygen from the minerals and carries it to an anode. What stays in the basket is a powder of [mixed metal alloys](https://www.esa.int/Enabling_Support/Space_Engineering_Technology/ESA_opens_oxygen_plant_making_air_out_of_moondust).

The method comes from the FFC Cambridge process, first published by [Chen, Fray and Farthing in 2000](https://doi.org/10.1038/35030069) as a way to turn titanium oxide into titanium metal. The UK company Metalysis, near Sheffield, acquired the [intellectual property](https://en.wikipedia.org/wiki/FFC_Cambridge_process) and uses it to make metals and alloys on Earth. For Metalysis, oxygen is just an unwanted by-product. A University of Glasgow team, working with ESA and Metalysis, tested the process on lunar regolith simulant and extracted [96% of the total oxygen](https://eprints.gla.ac.uk/196778), leaving a mixed metal alloy.

In January 2020 ESA opened a prototype oxygen plant at its [ESTEC technical centre](https://www.esa.int/Enabling_Support/Space_Engineering_Technology/ESA_opens_oxygen_plant_making_air_out_of_moondust) in the Netherlands. Metalysis's own pilot reactors later produced [multiple-kilogram batches of metal powder](https://www.esa.int/Space_in_Member_States/United_Kingdom/Oxygen_and_metal_powder_extracted_from_moonrocks) from simulant. In 2022 ESA gave Thales Alenia Space a [one million euro study contract](https://www.thalesaleniaspace.com/en/press-releases/thales-alenia-space-wins-study-contract-develop-payload-extract-oxygen-moon), with Metalysis, AVS, the Open University and Redwire Space Europe, to design a demonstration payload for a future ESA lunar mission. No flight date has been announced. Open Moon rates the process at TRL 4.

## Why Open Moon uses it

Lunar regolith is [40–45% oxygen by weight](https://www.esa.int/Enabling_Support/Space_Engineering_Technology/ESA_opens_oxygen_plant_making_air_out_of_moondust), but it is locked in minerals and glass. Oxygen is needed for breathing and, above all, as [rocket propellant](https://www.esa.int/Space_in_Member_States/United_Kingdom/British_technology_to_turn_Moon_dust_into_oxygen).

In **M06 (ISRU pilot)** the main oxygen plants are molten regolith electrolysis and carbothermal reduction. Molten salt electrolysis is the European back-up path. It runs cooler than melting rock and keeps the regolith solid.

Its real value is in **M12 (Manufacturing)**. Every kilogram of oxygen it makes leaves metal behind. ESA and Metalysis see that powder as feedstock for [3D printing, casting and building habitats](https://www.esa.int/Space_in_Member_States/United_Kingdom/Oxygen_and_metal_powder_extracted_from_moonrocks). A 2026 ESA-funded project is even testing the conductive residue as [printable electronic ink](https://www.dti.dk/services/researchers-turn-lunar-soil-into-moon-made-electronics/47664). Without this process, the base would rely on iron and silicon from molten regolith electrolysis, and would ship more metal from Earth.

## How it works

1. Regolith, loose or [pressed into pellets](https://eprints.gla.ac.uk/355741), is loaded into a metal basket that acts as the [cathode](https://en.wikipedia.org/wiki/FFC_Cambridge_process).
2. The basket goes into molten calcium chloride at about [950 °C](https://www.esa.int/Enabling_Support/Space_Engineering_Technology/ESA_opens_oxygen_plant_making_air_out_of_moondust). The regolith stays solid.
3. A current removes oxygen from the oxides. Oxygen ions travel through the salt to the anode.
4. With an inert tin oxide anode, oxygen gas is released. With a carbon anode, the oxygen reacts with the carbon instead and comes off as [carbon oxides](https://doi.org/10.1016/j.pss.2021.105408).
5. What is left in the basket is a [mixed metal alloy powder](https://eprints.gla.ac.uk/196778).

| Parameter | Value |
|---|---|
| Electrolyte | Molten calcium chloride ([ESA](https://www.esa.int/Enabling_Support/Space_Engineering_Technology/ESA_opens_oxygen_plant_making_air_out_of_moondust)) |
| Operating temperature | 950 °C baseline; 660 °C tested with eutectic salts ([Meurisse et al.](https://doi.org/10.1016/j.pss.2021.105408)) |
| Oxygen extracted (lab) | 96% of total ([Lomax et al. 2019](https://eprints.gla.ac.uk/196778)); over 40% at 660 °C ([Meurisse et al.](https://doi.org/10.1016/j.pss.2021.105408)) |
| Best operating point | About 60% extraction for fastest output, 70–80% for best power efficiency ([Lomax et al. 2025](https://eprints.gla.ac.uk/355741)) |
| Research reactor size | About the size of a washing machine ([ESA](https://www.esa.int/Space_in_Member_States/United_Kingdom/British_technology_to_turn_Moon_dust_into_oxygen)) |
| Energy per kg of oxygen | Not published |
| Plant mass and throughput | Not published |

## Limitations and open issues

- **Oxygen lost to the hardware.** In the 2019 test only about a third of the extracted oxygen reached the off-gas; the rest [corroded the reactor vessel](https://eprints.gla.ac.uk/196778).
- **Anode problems.** Carbon anodes react with the oxygen they should release, and calcium cycles between the electrodes, which [slows the reduction](https://doi.org/10.1016/j.pss.2021.105408).
- **Salt balance.** Around 90% extraction may be needed to keep the electrolyte self-sustaining, at the cost of [lower efficiency and throughput](https://eprints.gla.ac.uk/355741).
- **Uneven reduction.** Reduction does not happen evenly through a bulk sample, and highland simulant behaves differently from [mare simulant](https://eprints.gla.ac.uk/355741).
- **Mixed metals.** The process leaves a "tangle" of metals whose mix [varies by lunar region](https://www.esa.int/Enabling_Support/Space_Engineering_Technology/ESA_opens_oxygen_plant_making_air_out_of_moondust). Sorting them into useful alloys is unproven.
- **Mass and scale.** The salt and reactor must be shrunk to [fly to the Moon](https://www.esa.int/Space_in_Member_States/United_Kingdom/British_technology_to_turn_Moon_dust_into_oxygen). The 2022 [payload study](https://www.thalesaleniaspace.com/en/press-releases/thales-alenia-space-wins-study-contract-develop-payload-extract-oxygen-moon) names no flight date.
- **No energy figure.** No published kWh per kg of oxygen exists for a lunar-scale plant.
- **Not yet run on the Moon.** The results above all come from Earth laboratories using [simulants](https://eprints.gla.ac.uk/355741).
