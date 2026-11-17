---
slug: nasa-advanced-plant-habitat
title: "NASA Advanced Plant Habitat"
alternatives:
  - {name: "NASA Veggie (Vegetable Production System)", compare: "A simpler, lower-resource ISS garden with a red, blue and green LED light cap and a flexible enclosure. It is cheaper in crew time and power but has no closed chamber control of CO2, humidity or temperature, so it suits leafy greens better than long fruiting crops.", status: "On the ISS since April 2014 and listed by NASA as active.", url: "https://science.nasa.gov/mission/veggie"}
  - {name: "NASA Ohalo III crop production testbed", compare: "NASA's next-generation ISS crop system, designed from Veggie and APH lessons, with reusable root zones for both substrate and soilless hydroponic growing. It aims at food production rather than plant physiology research, but is not yet flight-proven.", status: "Being built for testing on the ISS (NASA, March 2026).", url: "https://ntrs.nasa.gov/citations/20260002161"}
  - {name: "DLR EDEN ISS greenhouse", compare: "A container-sized hydroponic greenhouse tested in Antarctica. It grows far more food than APH (268 kg from 12.5 m2 in 9.5 months) but has only been tested in Earth gravity and took about two-thirds of the operator's working time.", status: "Ground analogue; a Falcon 9 deployable concept has been proposed.", url: "https://eden-iss.net/index.php/2019/08/26/vegetable-cultivation-in-the-antarctic-for-the-moon-and-mars/"}
  - {name: "Yuegong-1 (Lunar Palace 1)", compare: "A Chinese closed bioregenerative ground facility with 58 m2 of plant growing area that fed crews for up to 370 days. It shows food production at base scale, but only on Earth and with no flight hardware.", status: "Ground demonstrator; 105-day and 370-day crewed tests completed.", url: "https://en.wikipedia.org/wiki/Yuegong-1"}
links:
  - {title: "NASA Facts: Advanced Plant Habitat (FS-2017-02-132-KSC)", url: "https://www.nasa.gov/sites/default/files/atoms/files/advanced-plant-habitat.pdf", kind: official, date: "Feb 2017"}
  - {title: "Massa, Wheeler, Morrow and Levine: Growth Chambers on the International Space Station for Large Plants (8th Int. Symposium on Light in Horticulture)", url: "https://ntrs.nasa.gov/citations/20160006561", kind: paper, date: "May 2016"}
  - {title: "Validation of the Advanced Plant Habitat Facility on ISS (NTRS)", url: "https://ntrs.nasa.gov/citations/20180006722", kind: official, date: "Jul 2018"}
  - {title: "Dufour, Levine and Onate: Hardware Validation Test of the Advanced Plant Habitat (ASGSR 2018, NTRS)", url: "https://ntrs.nasa.gov/citations/20180008565", kind: paper, date: "Nov 2018"}
  - {title: "Development of Advanced Plant Habitat Flight Unit (KSC intern report, NTRS)", url: "https://ntrs.nasa.gov/citations/20140002643", kind: official, date: "Jul 2013"}
  - {title: "NASA: Astronauts Harvest Radish Crop on International Space Station (PH-02)", url: "https://www.nasa.gov/missions/station/astronauts-harvest-radish-crop-on-international-space-station/", kind: official, date: "Dec 2020"}
  - {title: "NASA Facts: Plant Habitat-04 (FS-2021-06-445-KSC)", url: "https://www.nasa.gov/sites/default/files/atoms/files/plant_habitat-04.pdf", kind: official, date: "Jun 2021"}
  - {title: "NASA Kennedy: Houston, We Have a Pepper", url: "https://www.nasa.gov/centers-and-facilities/kennedy/houston-we-have-a-pepper/", kind: official, date: "Oct 2021"}
  - {title: "NASA: Astronauts Have First Taste of Peppers Grown in Space", url: "https://www.nasa.gov/image-article/astronauts-have-first-taste-of-peppers-grown-space/", kind: official, date: "Nov 2021"}
  - {title: "NASA Image and Video Library: chile peppers in the Advanced Plant Habitat (iss065e434051)", url: "https://images.nasa.gov/details/iss065e434051", kind: official, date: "Sep 2021"}
  - {title: "Poulet et al.: Large-Scale Crop Production for the Moon and Mars: Current Gaps and Future Perspectives (Frontiers in Astronomy and Space Sciences)", url: "https://www.frontiersin.org/articles/10.3389/fspas.2021.733944/full", kind: paper, date: "Feb 2022"}
  - {title: "Massa and Smith: Space Crop Production Research Informing Exploration (NTRS)", url: "https://ntrs.nasa.gov/citations/20260002161", kind: official, date: "Mar 2026"}
---

## What it is

The Advanced Plant Habitat (APH) is a fully automated plant growth chamber on the International Space Station. It was [developed by NASA and ORBITEC of Madison, Wisconsin](https://www.nasa.gov/sites/default/files/atoms/files/advanced-plant-habitat.pdf); ORBITEC later became part of [Sierra Nevada Corp.](https://ntrs.nasa.gov/citations/20180006722). Kennedy Space Center manages the hardware and runs experiments from the ground, so the crew mostly installs the science, adds water and does maintenance. NASA calls it [the largest of three plant growth chambers](https://www.nasa.gov/sites/default/files/atoms/files/plant_habitat-04.pdf) on the station, about the size of a large microwave oven.

The hardware was [carried to the ISS on SpaceX CRS-11 and Orbital ATK OA-7, assembled in the Kibo module on 27 Oct 2017, and activated on 19 Jan 2018](https://ntrs.nasa.gov/citations/20180006722). Its first test grew Arabidopsis and dwarf wheat, harvested after about 30 days. Later runs grew [20 radishes, harvested by Kate Rubins on 30 Nov 2020](https://www.nasa.gov/missions/station/astronauts-harvest-radish-crop-on-international-space-station/), and NuMex 'Española Improved' chile peppers. The peppers were [planted on 12 July 2021](https://www.nasa.gov/image-article/astronauts-have-first-taste-of-peppers-grown-space/), and the crew ate the first seven on 29 Oct 2021. This was the first time astronauts ate peppers grown in space.

## Why Open Moon uses it

Open Moon's milestone M10 (Growing food, Phase 4) needs fruiting crops, not only leafy greens. APH is the flight-proven example of growing a fruiting crop through a full cycle in a closed, sensor-rich chamber. The pepper run [lasted 120 days with harvests on days 100 and 120](https://www.nasa.gov/sites/default/files/atoms/files/plant_habitat-04.pdf). Peppers were picked because they are [a good source of Vitamin C](https://www.nasa.gov/centers-and-facilities/kennedy/houston-we-have-a-pepper/), a nutrient that breaks down in long-stored packaged food.

APH is a research chamber, not a farm. Open Moon uses it as the source of proven methods: light recipes, closed-chamber environment control, ground-controlled operation and pollination without insects. These would carry over into larger lunar greenhouse racks. Without that heritage, the plan would rely only on ground analogues for fruiting crops.

## How it works

Plants grow in a removable **Science Carrier**, a [0.2 m2 instrumented root module](https://ntrs.nasa.gov/citations/20180008565). It is packed with growing media, seeded on Earth and launched dry. An experiment starts when the crew installs it and wets it. For the peppers, the media was [arcillite, a baked clay, with controlled-release fertilizer](https://www.nasa.gov/sites/default/files/atoms/files/plant_habitat-04.pdf). An LED Growth Light Assembly sits above the plants. The chamber controls temperature, humidity, CO2, airflow and watering, and scrubs ethylene. A computer called PHARMER sends [real-time telemetry and photos to Kennedy and takes remote commands](https://www.nasa.gov/sites/default/files/atoms/files/advanced-plant-habitat.pdf). More than 180 sensors track conditions down to the roots and leaves. In microgravity, Kennedy staff [ran the fans at variable rates to pollinate pepper flowers](https://www.nasa.gov/centers-and-facilities/kennedy/houston-we-have-a-pepper/), and the crew hand-pollinated some.

Key specifications, from [Massa et al. 2016](https://ntrs.nasa.gov/citations/20160006561) unless noted:

| Parameter | Value |
|---|---|
| Shoot zone area | 0.19 m2 |
| Chamber height | 50 cm (max shoot height 45 cm) |
| Total light | 0-1000 µmol m-2 s-1, in steps of 50 |
| LED channels | Red 630 nm (0-600), blue 450 nm (0-400), green 525 nm (0-100), white 4100 K (0-600), far red 730 nm (0-50) |
| Temperature | 18-30 °C (±1 °C) |
| Relative humidity | 50-90% (±5%) |
| CO2 | 400-5000 ppm |
| Ethylene | Scrubbed to below 25 ppb |
| Air flow | 0.3-1.5 m/s |
| Experiment length | Up to 135 days; [at least one year of operation without maintenance](https://www.nasa.gov/sites/default/files/atoms/files/advanced-plant-habitat.pdf) |
| Sensors | [More than 180](https://www.nasa.gov/sites/default/files/atoms/files/advanced-plant-habitat.pdf) |

NASA has not published a power draw or mass for the APH unit in the sources here.

## Limitations and open issues

- **Tiny scale.** About 0.2 m2 of growing area yields a few peppers or radishes per run. It shows that crops can grow but provides no meaningful food supply. Poulet et al. note that [larger platforms will bring new engineering challenges](https://www.frontiersin.org/articles/10.3389/fspas.2021.733944/full).
- **Lower fruit set.** Pepper plants formed [fewer fruit than on the ground](https://www.nasa.gov/centers-and-facilities/kennedy/houston-we-have-a-pepper/), for reasons not fully understood. Pollination at scale is unsolved.
- **Water delivery.** APH uses substrate-based capillary watering. In microgravity, [roots can suffer from hypoxia without proper water and nutrient delivery](https://www.frontiersin.org/articles/10.3389/fspas.2021.733944/full), and substrates add up-mass and waste. Lunar gravity (1/6 g) has not been tested.
- **Crew and ground effort.** Operation relies on a ground team at Kennedy. Future systems [need to be less crew-time intensive](https://www.frontiersin.org/articles/10.3389/fspas.2021.733944/full).
- **Research hardware, not production hardware.** NASA describes APH as a [plant physiology research chamber](https://ntrs.nasa.gov/citations/20260002161). Its successor for food production, Ohalo III, is still being built.
- **Power per kg of food.** The energy cost of LED lighting per kg of produce from APH has not been published.
