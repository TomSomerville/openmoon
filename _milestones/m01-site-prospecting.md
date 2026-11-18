---
id_code: M01
order: 1
title: Site prospecting
phase: 0
window: "Years 0–2"
summary: Robot rovers land at the chosen site and measure, on the ground, how much water the icy soil really gives up, how deep it goes, and what the ground is like to build on.
objective: "Confirm the site's water resource before anything the base depends on is landed. Scoop and drill icy soil to 1 m at several points in at least two permanently shadowed regions (PSRs) near the base, bake each sample and measure the water it releases, and map the ground's strength and small rocks for site preparation (M02). This runs at the same time as site preparation."
trl_min: 4
depends_on: [M00]
spec:
  - {k: Missions, v: "2 prospector rovers on 2 different landers, plus data from partner missions"}
  - {k: Rover, v: "C01.1: neutron spectrometer, scoop arm with rasp, 1 m drill, sealed bake chamber, mass spectrometer, cameras"}
  - {k: Samples, v: "Scooped surface soil, and drill cuttings baked 10 cm at a time down to 1 m"}
  - {k: Runs alongside, v: "M02 Site preparation (same years)"}
cost: {low: 0.5, high: 1.2, note: "two rovers and two deliveries; delivery priced from a published NASA task order"}
cost_items:
  - {item: "Prospector rover ×2 (design, build, test)", low: 0.2, high: 0.5, basis: "ESTIMATE. Smaller than LTV-class rovers, whose task orders are $219–220M each [benchmark]"}
  - {item: "Delivery to the south pole ×2", low: 0.25, high: 0.5, basis: "VIPER delivery task order up to $190M each (CS-7) [src 3]; range covers price growth"}
  - {item: "Operations, science team, data release", low: 0.05, high: 0.2, basis: "ESTIMATE"}
exit_criteria:
  - "Water released by baking measured in at least two PSRs, to at least 1 m depth, at several points in each, with the sampling losses calibrated on the ground."
  - "A water map with enough detail to site the ice mine, published openly."
  - "Ground strength, density and small-rock counts measured at the planned pad, road and habitat locations, and handed to M02."
  - "A go / no-go decision on the site. If the water is not there, switch to the backup site from M00."
workstreams:
  - name: Use partner data first
    desc: Fold in results from missions already planned.
    items: ["NASA VIPER (due 2027)", "China's Chang'e-7 near Shackleton (2027)", "ESA PROSPECT on IM-4 (2027)", "Lessons from PRIME-1 on IM-2"]
  - name: Prospector rover
    desc: A small rover that drives into PSRs, scoops and drills icy soil, and bakes it to measure the water.
    items: ["Neutron spectrometer to find hydrogen while driving", "1 m drill that breaks ice-cemented ground into cuttings (TRIDENT heritage)", "Scoop arm with rasp (Phoenix heritage)", "Sealed bake chamber to 450 °C (Resource Prospector heritage)", "Mass spectrometer (MSolo heritage)"]
  - name: Ground truth for site preparation
    desc: Measure what the builders in M02 need to know.
    items: ["Ground strength from drilling and the scoop", "Density and grain size", "Counts of rocks too small to see from orbit, along pad and road routes"]
  - name: Lander selection
    desc: Pick delivery services with the best landing record.
    items: ["Demonstrated upright landings", "Terrain-relative navigation", "Landing ellipse clear of the site's hazards"]
technologies:
  - {name: "Resource Prospector OVEN (NASA)", use: "Heritage for the sealed bake chamber fed by the drill", status: "Rover cancelled 2018; OVEN passed vibration and thermal-vacuum tests (−50 to 75 °C)", trl: 5, src: 4}
  - {name: "TRIDENT drill (Honeybee Robotics)", use: "Drilling ice-cemented ground to 1 m", status: "Flew on IM-2 (2025). Powered up and extended to its full range; lander ended on its side, so it never drilled", trl: 7, src: 1}
  - {name: "MSolo mass spectrometer", use: "Identifying the gases released in the bake chamber", status: "Flew on IM-2; worked, but gases detected were from the lander or Earth", trl: 7, src: 2}
  - {name: "Phoenix Robotic Arm scoop and rasp (NASA, Mars)", use: "Heritage for the scoop arm", status: "Flew in 2008; dug icy Martian soil", trl: 9, src: 5}
  - {name: "VIPER rover (NASA)", use: "Partner ice-prospecting data", status: "Built and in final testing; due to fly in 2027 on Blue Moon Mark 1", trl: 8, src: 6}
  - {name: "Commercial lunar landers (CLPS)", use: "Delivering the prospectors", status: "Mixed record: Peregrine never attempted a landing (2024); IM-1 and IM-2 tipped; Blue Ghost M1 fully successful (2025)", trl: 7, src: 7}
  - {name: "Radioisotope heater units", use: "Keeping electronics warm in PSRs and at night", status: "Flight-proven (Cassini carried 82), about 1 W each", trl: 9, src: 8}
sources:
  - {title: "NASA: Lunar drill technology passes tests on the Moon (PRIME-1)", url: "https://www.nasa.gov/missions/artemis/clps/nasas-lunar-drill-technology-passes-tests-on-the-moon/", date: "May 2025"}
  - {title: "NASA NTRS: MSolo PRIME-1 overview and results", url: "https://ntrs.nasa.gov/api/citations/20260003150/downloads/MSolo%20PRIME-1%20overview%20and%20results%20-%20LSSW.pdf", date: "2026"}
  - {title: "NASA: NASA selects Blue Origin to deliver VIPER rover to Moon's south pole", url: "https://www.nasa.gov/news-release/nasa-selects-blue-origin-to-deliver-viper-rover-to-moons-south-pole/", date: "Sep 2025"}
  - {title: "NASA NTRS: Paz, Environmental testing of the OVEN system for lunar water extraction and prospecting", url: "https://ntrs.nasa.gov/citations/20210013522", date: "2021"}
  - {title: "Bonitz et al.: NASA Mars 2007 Phoenix Lander Robotic Arm and Icy Soil Acquisition Device (JGR 113)", url: "https://www-robotics.jpl.nasa.gov/media/documents/2007JE003030.pdf", date: "Jun 2008"}
  - {title: "NASA: NASA provides progress update on Moon base rovers", url: "https://www.nasa.gov/missions/moon-base/nasa-provides-progress-update-on-moon-base-rovers/", date: "Oct 2026"}
  - {title: "Commercial Lunar Payload Services, Wikipedia", url: "https://en.wikipedia.org/wiki/Commercial_Lunar_Payload_Services", date: "accessed Nov 2026"}
  - {title: "NASA Science: Cassini's radioisotope thermoelectric generators (82 RHUs, one watt each)", url: "https://science.nasa.gov/mission/cassini/radioisotope-thermoelectric-generator", date: ""}
  - {title: "NASA Science: LCROSS mission", url: "https://science.nasa.gov/mission/lcross/", date: ""}
  - {title: "NASA M2M-30044 Lunar Surface Data Book (LCROSS water ~5% by mass)", url: "https://ntrs.nasa.gov/api/citations/20250002845/downloads/M2M-30044%20Lunar%20Surface%20Data%20Book%20Baseline_Final.pdf", date: "2025"}
  - {title: "JPL: Ice confirmed at the Moon's poles (M3)", url: "https://www.jpl.nasa.gov/news/ice-confirmed-at-the-moons-poles/", date: "Aug 2018"}
  - {title: "Univ. of Hawaii SOEST: Scarce ice in Moon's darkest regions (ShadowCam)", url: "https://www.soest.hawaii.edu/soestwp/announce/news/scarce-ice-in-moons-darkest-regions/", date: "Mar 2026"}
  - {title: "UCLA Diviner: lunar temperatures", url: "https://www.diviner.ucla.edu/science", date: ""}
  - {title: "NASA NTRS: Kleinhenz et al., Volatiles loss from water bearing regolith simulant at lunar environments", url: "https://ntrs.nasa.gov/api/citations/20180004331/downloads/20180004331.pdf", date: "Apr 2018"}
  - {title: "Chang'e 7, Wikipedia", url: "https://en.wikipedia.org/wiki/Chang'e_7", date: "accessed Nov 2026"}
  - {title: "ESA: European drill and mini lab secure ride to the Moon", url: "https://esa.int/Science_Exploration/Human_and_Robotic_Exploration/European_drill_and_mini_lab_secure_ride_to_the_Moon", date: "Aug 2024"}
  - {title: "Boazman et al.: The distribution and accessibility of geologic targets near the lunar south pole and candidate Artemis landing sites (PSJ 3:275)", url: "https://iopscience.iop.org/article/10.3847/PSJ/aca590", date: "Dec 2022"}
risks:
  - {sev: Critical, title: "Lander tips over or crashes (IM-1 and IM-2 landed on their sides; ispace M2 crashed)", fix: "Fly the two prospectors on two different landers; pick services with a demonstrated upright landing; require terrain-relative navigation"}
  - {sev: High, title: "Ice is patchy: ShadowCam found no widespread surface ice above ~20–30%, only small patches", fix: "Sample many points across several PSRs rather than one deep hole; rank sites by measured, not modelled, water"}
  - {sev: High, title: "Samples lose water before they are sealed in: about 30% from 4.5 wt% soil and about 80% from 0.8 wt% soil in NASA vacuum tests", fix: "Brush drill bites straight into the chamber and seal at once; calibrate losses on icy simulant before flight"}
  - {sev: High, title: "The bake chamber is about 20 times larger than any tested lunar oven (TRL 4)", fix: "Build and test a full-size chamber in thermal vacuum with icy simulant early, before the rover design is frozen"}
  - {sev: High, title: "Extreme cold in PSRs (about 25–40 K) drains batteries and can freeze mechanisms", fix: "Short sorties into the shadow from a sunlit parking spot; radioisotope heaters; insulated warm electronics box"}
  - {sev: Medium, title: "No line of sight to Earth or a relay from inside a crater", fix: "Store data on board and send it when back in view"}
  - {sev: Medium, title: "Lander exhaust contaminates the gas readings (as MSolo saw on IM-2)", fix: "Drive away from the lander before sampling; bake a dry batch in sunlight first as a baseline"}
---

## What we already know about the ice

- **LCROSS (2009)** hit the shadowed crater Cabeus<sup class="r">[9](#s9)</sup>. NASA's 2025 data book says later analyses put the water found "on the order of five percent" by mass<sup class="r">[10](#s10)</sup>.
- **Chandrayaan-1's M3 instrument** confirmed surface water ice in polar cold traps in 2018<sup class="r">[11](#s11)</sup>.
- **ShadowCam (2026)** found **little widespread surface ice**. It found only a few 20–50 m patches consistent with more than 10% ice, often near young craters<sup class="r">[12](#s12)</sup>.
- Temperatures inside shadowed craters can fall to about 25 K<sup class="r">[13](#s13)</sup>.

So ice exists, but its amount and depth at any one spot are unknown, and no mission has yet measured ice in place in a lunar PSR. That is why this milestone exists. The ice mine and water plant are sized on numbers that only ground sampling can confirm.

## How the prospector measures water

The prospector rover (C01.1) does more than detect water. It heats icy soil and measures the water that actually comes out, which is what the ice mine will later do at full size (design change DD-025).

1. **Find it.** A neutron spectrometer maps hydrogen in the top metre while the rover drives.
2. **Scoop it.** Where hydrogen is high, a bladed scoop picks up loose soil and small debris. A powered rasp chips hard icy ground at the surface, as on NASA's Phoenix lander<sup class="r">[5](#s5)</sup>.
3. **Drill it.** A 1 m drill breaks the hard, ice-cemented ground into cuttings and lifts them 10 cm at a time. Each bite is brushed straight into the bake chamber, as on NASA's Resource Prospector design.
4. **Bake it.** The sealed chamber weighs each batch and heats it to 150, 350 and 450 °C. The gas is measured, identified by the mass spectrometer and frozen in a cold trap. Resource Prospector's 12 cc oven passed vibration and thermal-vacuum tests<sup class="r">[4](#s4)</sup>; Open Moon's chamber is about 20 times larger (plan design).

Water escapes between the ground and the sealed lid. In NASA vacuum tests, samples lost about 30% of their water from 4.5 wt% soil and about 80% from 0.8 wt% soil<sup class="r">[14](#s14)</sup>. Those losses are calibrated on the ground before flight so the readings can be corrected.

## Lessons already paid for

- **PRIME-1 on IM-2 (2025).** The TRIDENT drill and MSolo spectrometer both worked on the Moon, but the lander ended up on its side, the mission lasted about half a day, and the gases MSolo detected came from the lander or Earth<sup class="r">[1](#s1)</sup><sup class="r">[2](#s2)</sup>. **Lesson:** don't depend on one lander.
- **Phoenix (Mars, 2008).** It dug icy soil with a scoop and rasp, but icy samples were hard to deliver into its ovens<sup class="r">[5](#s5)</sup>. **Lesson:** design the sample path for sticky, icy material.

## Where to prospect

The [M00 maps]({{ '/plan/m00-site-selection/' | relative_url }}) give three kinds of target in the Shackleton–de Gerlache focus area (plan design):

- **Ice candidates:** the permanently shadowed floors of Shackleton and de Gerlache, reached from landable ground on their rims. de Gerlache also holds ShadowCam's unexplained bright spot at 88.5352°S, 97.4007°W.
- **Hydrogen:** the high-hydrogen zone in NASA's LEND data, around 88°S, 0–60°E.
- **Unmeasured cold traps:** Spudis and the small shadowed craters along the ridge, which have no published ice data.

Each prospector lands on ground of 8° or less (DD-011).

## Ground truth for site preparation

Orbital images cannot show rocks smaller than about 1–4 m<sup class="r">[17](#s17)</sup>, and small-rock counts for the site are not published. Site preparation (M02) needs them to plan rock clearing and grading. So the prospectors also image the planned pad and road routes, and log ground strength from the drill and scoop. M01 and M02 run at the same time (plan design): prospecting data feed site preparation as they arrive.

## Step-by-step

1. **Collect partner results.** VIPER is built and due to fly in 2027<sup class="r">[6](#s6)</sup>. Chang'e-7, which targets the Shackleton area, is listed for 2027<sup class="r">[15](#s15)</sup>. ESA's PROSPECT drill and lab have a ride on IM-4<sup class="r">[16](#s16)</sup>. Use whatever arrives, but don't wait on it.
2. **Build two prospector rovers** (C01.1). Build and test the full-size bake chamber first, because it is the least mature part.
3. **Buy two deliveries on different landers.** Pricing reference: NASA's VIPER delivery task order is worth up to $190M<sup class="r">[3](#s3)</sup>.
4. **Explore from a sunlit parking spot.** Each rover recharges in sunlight, then makes short trips into the PSR. Radioisotope heaters (about 1 W each<sup class="r">[8](#s8)</sup>) keep electronics alive.
5. **Sample a grid.** Several points per PSR: a scooped surface batch, then drill bites to 1 m, each baked for its water.
6. **Survey the build sites** for M02: small rocks, ground strength and density along pad and road routes.
7. **Make the go / no-go decision** and publish all data openly.
