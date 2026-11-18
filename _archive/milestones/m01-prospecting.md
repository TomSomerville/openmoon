---
id_code: M01
order: 1
title: Robotic prospecting and ground truth
phase: 0
window: "Years 0–2"
summary: Land robots at the chosen site to confirm, on the ground, how much ice is there, how deep, and what the soil is really like.
objective: "Confirm the site's ice resource and terrain before committing billions to infrastructure. Measure ice concentration and depth in at least two permanently shadowed regions (PSRs) within cable distance of the base, test the regolith's mechanical properties, and record the local radiation and dust environment."
trl_min: 6
depends_on: [M00]
spec:
  - {k: Missions, v: "2 prospecting landings, plus data from partner missions"}
  - {k: Payload, v: "Prospecting rover: neutron spectrometer, scoop arm, 1 m drill, sealed bake chamber, mass spectrometer, cameras"}
  - {k: Delivery, v: "Commercial lander service (CLPS-class)"}
cost: {low: 0.5, high: 1.2, note: "two missions; delivery priced from published task orders"}
cost_items:
  - {item: "Prospecting rover ×2 (design, build, test)", low: 0.2, high: 0.5, basis: "ESTIMATE. Smaller than LTV-class rovers, whose task orders are $219–220M each [benchmark]"}
  - {item: "Delivery to the south pole ×2", low: 0.25, high: 0.5, basis: "VIPER delivery task order up to $190M each (CS-7); range covers price growth"}
  - {item: "Operations, science team, data release", low: 0.05, high: 0.2, basis: "ESTIMATE"}
exit_criteria:
  - "Ice concentration measured by drilling and baking samples (not only by orbit) in at least two PSRs, to at least 1 m depth, at several points in each."
  - "Ice map with enough resolution to site an extraction plant, published openly."
  - "Regolith bearing strength, density and grain size measured at the planned pad and habitat locations."
  - "Surface radiation dose and dust levitation measured over at least one full lunar day and night."
  - "A go / no-go decision on the site. If the ice is not there, switch to the backup site from M00."
workstreams:
  - name: Use partner data first
    desc: Fold in results from missions already planned.
    items: ["NASA VIPER (if delivered)", "China's Chang'e-7 near Shackleton", "ISRO/JAXA LUPEX", "Lessons from PRIME-1 on IM-2"]
  - name: Prospector rover
    desc: A small rover that drives into PSRs, scoops and drills icy soil, and bakes it to measure the water released.
    items: ["Neutron spectrometer for hydrogen", "1 m drill (TRIDENT heritage) that brushes cuttings into the bake chamber", "Scoop arm with rasp (Phoenix heritage)", "Sealed bake chamber to 450 °C (Resource Prospector OVEN heritage)", "Mass spectrometer (MSolo heritage)", "Survives 25–40 K cold for hours"]
  - name: Lander selection
    desc: Pick the delivery service with the best landing record.
    items: ["Demonstrated soft landings", "Terrain-relative navigation", "Landing ellipse inside site hazards map"]
  - name: Geotechnics
    desc: Measure what the builders in M05 need to know.
    items: ["Bearing strength (penetrometer)", "Density and cohesion", "Grain-size sampling"]
  - name: Environment monitoring
    desc: Measure what the crew will live with.
    items: ["Radiation dosimeter", "Dust levitation sensor", "Thermal and seismic logging"]
technologies:
  - {name: "TRIDENT drill (Honeybee Robotics)", use: "Drilling up to 1 m to sample ice", status: "Flew on IM-2 (2025). Powered up and extended to its full range; lander ended on its side and the mission ended early", trl: 7, src: 1}
  - {name: "MSolo mass spectrometer", use: "Identifying volatiles released from drilled soil", status: "Flew on IM-2; worked, but gases detected were from the lander or Earth", trl: 7, src: 2}
  - {name: "Resource Prospector OVEN (NASA)", use: "Heritage for the sealed bake chamber fed by the drill", status: "Rover cancelled 2018; OVEN passed vibration and thermal-vacuum tests", trl: 5, src: 17}
  - {name: "VIPER rover (NASA)", use: "Partner ice-prospecting data", status: "Revived Sep 2025 via CLPS task order up to $190M; delivery option tied to Blue Moon MK1's first flight", trl: 8, src: 3}
  - {name: "Commercial lunar landers (CLPS)", use: "Delivering the prospector", status: "Mixed record: Peregrine never attempted a landing (2024); IM-1 and IM-2 tipped; Blue Ghost M1 fully successful (2025)", trl: 7, src: 16}
  - {name: "Radioisotope heater units", use: "Keeping electronics warm in PSRs and at night", status: "Flight-proven (Cassini carried 82), about 1 W each", trl: 9, src: 15}
sources:
  - {title: "NASA: Lunar drill technology passes tests on the Moon (PRIME-1)", url: "https://www.nasa.gov/missions/artemis/clps/nasas-lunar-drill-technology-passes-tests-on-the-moon/", date: "May 2025"}
  - {title: "NASA NTRS: MSolo PRIME-1 overview and results", url: "https://ntrs.nasa.gov/api/citations/20260003150/downloads/MSolo%20PRIME-1%20overview%20and%20results%20-%20LSSW.pdf", date: "2026"}
  - {title: "NASA: NASA selects Blue Origin to deliver VIPER rover to Moon's south pole", url: "https://www.nasa.gov/news-release/nasa-selects-blue-origin-to-deliver-viper-rover-to-moons-south-pole/", date: "Sep 2025"}
  - {title: "Firefly: Blue Ghost completes 14 days of surface operations", url: "https://fireflyspace.com/news/firefly-aerospace-successfully-completes-14-days-of-surface-operations-on-the-moon", date: "Mar 2025"}
  - {title: "NASA: Radioisotope Heater Units fact sheet", url: "https://science.nasa.gov/resource/radioisotope-heater-units-fact-sheet/", date: ""}
  - {title: "NASA Science: LCROSS mission", url: "https://science.nasa.gov/mission/lcross/", date: ""}
  - {title: "NASA M2M-30044 Lunar Surface Data Book (LCROSS water ~5% by mass)", url: "https://ntrs.nasa.gov/api/citations/20250002845/downloads/M2M-30044%20Lunar%20Surface%20Data%20Book%20Baseline_Final.pdf", date: "2025"}
  - {title: "JPL: Ice confirmed at the Moon's poles (M3)", url: "https://www.jpl.nasa.gov/news/ice-confirmed-at-the-moons-poles/", date: "Aug 2018"}
  - {title: "Univ. of Hawaii SOEST: Scarce ice in Moon's darkest regions (ShadowCam)", url: "https://www.soest.hawaii.edu/soestwp/announce/news/scarce-ice-in-moons-darkest-regions/", date: "Mar 2026"}
  - {title: "UCLA Diviner: lunar temperatures", url: "https://www.diviner.ucla.edu/science", date: ""}
  - {title: "JPL: NASA's Lunar Trailblazer mission ends", url: "https://www.jpl.nasa.gov/news/nasas-lunar-trailblazer-moon-mission-ends/", date: "2025"}
  - {title: "Space.com: ispace lander crashed due to laser errors", url: "https://www.space.com/space-exploration/launches-spacecraft/private-japanese-moon-lander-crashed-due-to-laser-errors-ispace-says", date: "Jun 2025"}
  - {title: "Zhang et al., Science Advances: radiation dose on the lunar surface (Chang'e-4 LND)", url: "https://doi.org/10.1126/sciadv.aaz1334", date: "Sep 2020"}
  - {title: "Chang'e 7, Wikipedia", url: "https://en.wikipedia.org/wiki/Chang'e_7", date: "accessed Nov 2026"}
  - {title: "NASA Science: Cassini's radioisotope thermoelectric generators (82 RHUs, one watt each)", url: "https://science.nasa.gov/mission/cassini/radioisotope-thermoelectric-generator", date: ""}
  - {title: "Commercial Lunar Payload Services, Wikipedia", url: "https://en.wikipedia.org/wiki/Commercial_Lunar_Payload_Services", date: "accessed Nov 2026"}
  - {title: "NASA NTRS: Paz, Environmental testing of the OVEN system for lunar water extraction and prospecting", url: "https://ntrs.nasa.gov/citations/20210013522", date: "2021"}
risks:
  - {sev: Critical, title: "Lander tips over or crashes (IM-1 and IM-2 landed on their sides; ispace M2 crashed)", fix: "Fly two prospectors on two different landers; pick services with a demonstrated upright landing; require terrain-relative navigation"}
  - {sev: High, title: "Ice is patchy: ShadowCam found no widespread surface ice above ~20–30%, only small patches", fix: "Drill many points across several PSRs rather than one deep hole; rank by measured, not modelled, ice"}
  - {sev: High, title: "Extreme cold in PSRs (about 25–40 K) kills batteries and electronics", fix: "Short sorties into the shadow from a sunlit base point; radioisotope heaters; insulated warm electronics box"}
  - {sev: Medium, title: "No line of sight to Earth or relay from inside a crater", fix: "Store-and-forward data; a relay rover or relay mast on the crater rim"}
  - {sev: Medium, title: "Contaminating our own samples with lander exhaust (as MSolo saw on IM-2)", fix: "Drive away from the lander before sampling; measure lander exhaust signature as a baseline"}
---

## What we already know about the ice

- **LCROSS (2009)** hit the shadowed crater Cabeus<sup class="r">[6](#s6)</sup>. NASA's 2025 data book says later analyses put the water found "on the order of five percent" by mass<sup class="r">[7](#s7)</sup>.
- **Chandrayaan-1's M3 instrument** confirmed surface water ice in polar cold traps in 2018<sup class="r">[8](#s8)</sup>.
- **ShadowCam (2026)** found **little widespread surface ice**. It found only a few 20–50 m patches consistent with more than 10% ice, often near young craters<sup class="r">[9](#s9)</sup>.
- Temperatures inside shadowed craters can fall to about 25 K<sup class="r">[10](#s10)</sup>.

So ice exists, but its amount and depth at any one spot are unknown. That is why this milestone exists. The water plant in M06 and the propellant plant in M11 are sized on numbers that only drilling can confirm.

## Lessons already paid for

- **PRIME-1 on IM-2 (2025).** The TRIDENT drill and MSolo spectrometer both worked on the Moon, but the lander ended up on its side, the mission lasted about half a day, and the gases MSolo detected came from the lander or Earth<sup class="r">[1](#s1)</sup><sup class="r">[2](#s2)</sup>. **Lesson:** don't depend on one lander.
- **Lunar Trailblazer** was lost the day after launch in February 2025<sup class="r">[11](#s11)</sup>. **Lesson:** orbital ice mapping can't be counted on either.
- **Blue Ghost M1** operated for 14 days and into the lunar night<sup class="r">[4](#s4)</sup>. **Lesson:** reliable commercial landers now exist.

## Where to prospect

The [M00 maps]({{ '/plan/m00-site-selection/' | relative_url }}) give three kinds of target in the Shackleton–de Gerlache focus area (plan design):

- **Ice candidates:** the permanently shadowed floors of Shackleton and de Gerlache, reached from landable ground on their rims. de Gerlache also holds ShadowCam's unexplained bright spot at 88.5352°S, 97.4007°W.
- **Hydrogen:** the high-hydrogen zone in NASA's LEND data, around 88°S, 0–60°E.
- **Unmeasured cold traps:** Spudis and the small shadowed craters along the ridge, which have no published ice data.

Each prospector lands on ground of 8° or less (DD-011).

## Step-by-step

1. **Collect partner results.** NASA will decide whether to deliver VIPER after Blue Moon MK1's first flight<sup class="r">[3](#s3)</sup>. Chang'e-7, which targets the Shackleton area, slipped to 2027<sup class="r">[14](#s14)</sup>. Use whatever arrives, but don't wait on it.
2. **Build two small prospector rovers** with flight-proven instruments: TRIDENT-class drill, MSolo-class mass spectrometer, neutron spectrometer and stereo cameras.
3. **Buy two deliveries on different landers.** Pricing reference: NASA's VIPER delivery task order is worth up to $190M<sup class="r">[3](#s3)</sup>.
4. **Explore from a sunlit base point.** Each rover parks in sunlight to recharge, then makes short trips into the PSR. Radioisotope heaters (about 1 W each<sup class="r">[5](#s5)</sup>) keep electronics alive.
5. **Drill a grid of holes.** Several points per PSR, down to 1 m.
6. **Measure the environment.** Chang'e-4 measured about 1,369 µSv per day on the far side<sup class="r">[13](#s13)</sup>. We need the polar equivalent, along with dust and seismic data, before crews arrive.
7. **Make the go / no-go decision** and publish all data openly.
