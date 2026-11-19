---
id_code: M01
order: 1
title: Site prospecting
phase: 0
content_first: true
window: "Years 0–2"
summary: Two robot rovers land at the chosen site, scoop and drill icy soil in the shadowed craters, bake it, and measure how much water actually comes out.
trl_min: 4
depends_on: [M00]
spec:
  - {k: Rovers, v: "2 prospector rovers (C01.1), on 2 different landers"}
  - {k: Tools, v: "Neutron spectrometer, scoop arm with rasp, 1 m drill, sealed bake chamber, mass spectrometer"}
  - {k: Output, v: "Measured water by depth in at least two shadowed craters; small rocks and ground strength for M02"}
  - {k: Runs alongside, v: "M02 Site preparation"}
technologies:
  - {name: "Resource Prospector drill-to-oven system (NASA)", use: "Heritage for the bake chamber fed straight from the drill", status: "Rover cancelled 2018; its 12 cc oven passed vibration and thermal-vacuum tests", trl: 5, src: 15}
  - {name: "TRIDENT drill (Honeybee Robotics)", use: "Breaking ice-cemented ground into cuttings, to 1 m", status: "Flew on IM-2 (2025) but the lander tipped, so it never drilled; on VIPER for 2027", trl: 7, src: 6}
  - {name: "MSolo mass spectrometer (NASA KSC / INFICON)", use: "Identifying the gases from the bake chamber", status: "Flew on IM-2; saw mostly Earth air and lander venting", trl: 7, src: 8}
  - {name: "Phoenix scoop and rasp (NASA, Mars)", use: "Heritage for the scoop arm", status: "Flew 2008; dug icy Martian soil", trl: 9, src: 2}
  - {name: "VIPER neutron spectrometer (NASA)", use: "Mapping hydrogen in the top metre while driving", status: "Built; VIPER due 2027", trl: 6, src: 9}
sources:
  - {title: "Boynton et al.: Evidence for calcium carbonate at the Mars Phoenix landing site (TEGA results, Science 325)", url: "https://planetary.chem.tufts.edu/Boynton%20etal%20Science%202009v325p61.pdf", date: "Jul 2009"}
  - {title: "Bonitz et al.: NASA Mars 2007 Phoenix Lander Robotic Arm and Icy Soil Acquisition Device (JGR 113)", url: "https://www-robotics.jpl.nasa.gov/media/documents/2007JE003030.pdf", date: "Jun 2008"}
  - {title: "Leshin et al.: Volatile, isotope and organic analysis of Martian fines with the Mars Curiosity rover (Science)", url: "https://mars.nasa.gov/files/msl/Science-2013-Leshin-.pdf", date: "Sep 2013"}
  - {title: "JPL (archived): MSL Science Corner, sampling system", url: "https://webarchive.library.unt.edu/web/20130214054221/http://msl-scicorner.jpl.nasa.gov/samplingsystem", date: "2013"}
  - {title: "AAAS: LCROSS impact ejects minerals and frozen water (Colaprete et al. 2010)", url: "https://www.aaas.org/news/science-lcross-impact-ejects-minerals-and-frozen-water-crater-moon", date: "Oct 2010"}
  - {title: "Zacny et al.: TRIDENT ice mining drill for lunar volatile prospecting for PRIME-1 and VIPER (PSJ)", url: "https://iopscience.iop.org/article/10.3847/PSJ/ae0b51", date: "Dec 2025"}
  - {title: "NASA: Lunar drill technology passes tests on the Moon (PRIME-1)", url: "https://www.nasa.gov/missions/artemis/clps/nasas-lunar-drill-technology-passes-tests-on-the-moon/", date: "May 2025"}
  - {title: "NASA NTRS: MSolo PRIME-1 overview and results", url: "https://ntrs.nasa.gov/api/citations/20260003150/downloads/MSolo%20PRIME-1%20overview%20and%20results%20-%20LSSW.pdf", date: "Apr 2026"}
  - {title: "NASA: NASA provides progress update on Moon base rovers (VIPER)", url: "https://www.nasa.gov/missions/moon-base/nasa-provides-progress-update-on-moon-base-rovers/", date: "Oct 2026"}
  - {title: "Chang'e 7, Wikipedia", url: "https://en.wikipedia.org/wiki/Chang'e_7", date: "accessed Nov 2026"}
  - {title: "JAXA: Lunar Polar Exploration Mission (LUPEX)", url: "https://www.exploration.jaxa.jp/e/program/lunarpolar/", date: "accessed Nov 2026"}
  - {title: "Trautner et al.: PROSPECT, a sample acquisition and analysis package for lunar science and exploration (Frontiers)", url: "https://www.frontiersin.org/journals/space-technologies/articles/10.3389/frspt.2024.1331828/full", date: "Apr 2024"}
  - {title: "Sefton-Nash et al.: ExoMars Rosalind Franklin mission status (EPSC 2026)", url: "https://meetingorganizer.copernicus.org/EPSC2026/EPSC2026-411.html", date: "2026"}
  - {title: "NASA NTRS: Colaprete et al., Resource Prospector instrumentation for lunar volatiles prospecting, sample acquisition and processing", url: "https://ntrs.nasa.gov/api/citations/20160005014/downloads/20160005014.pdf", date: "Apr 2016"}
  - {title: "NASA NTRS: Paz, Environmental testing of the OVEN system for lunar water extraction and prospecting", url: "https://ntrs.nasa.gov/citations/20210013522", date: "2021"}
  - {title: "NASA NTRS: Kleinhenz et al., Volatiles loss from water bearing regolith simulant at lunar environments", url: "https://ntrs.nasa.gov/api/citations/20180004331/downloads/20180004331.pdf", date: "Apr 2018"}
  - {title: "Spaceflight Now: NASA cancels lunar rover, shifts focus to commercial Moon landers", url: "https://spaceflightnow.com/2018/05/01/nasa-cancels-lunar-rover-shifts-focus-to-commercial-moon-landers/", date: "May 2018"}
  - {title: "DLR: Water from Moon rock for future astronaut missions (LUWEX)", url: "https://www.dlr.de/en/latest/news/2024/water-from-moon-rock-for-future-astronaut-missions", date: "Oct 2024"}
  - {title: "Ethridge & Kaukler, NASA MSFC: Microwave extraction of water from lunar regolith simulant (NTRS 20070018802)", url: "https://ntrs.nasa.gov/api/citations/20070018802/downloads/20070018802.pdf", date: "2007"}
  - {title: "NASA NTRS: Lunar Auger Dryer ISRU (LADI)", url: "https://ntrs.nasa.gov/citations/20230013485", date: "2023"}
  - {title: "Mantovani et al., NASA KSC: Swamp Works regolith excavation (ice-regolith strength, citing Gertsch et al. 2006)", url: "https://ntrs.nasa.gov/api/citations/20140017852/downloads/20140017852.pdf", date: "2014"}
  - {title: "Hayne et al.: Global regolith thermophysical properties of the Moon from Diviner (JGR Planets)", url: "https://arxiv.org/pdf/1711.00977", date: "2017"}
  - {title: "Murphy & Koop: Review of the vapour pressures of ice and supercooled water (QJRMS 131)", url: "https://zenodo.org/records/1236243/files/article.pdf", date: "2005"}
  - {title: "Lunar Sourcebook, Chapter 9: Physical properties of the lunar surface (Carrier, Olhoeft & Mendell)", url: "https://www.lpi.usra.edu/publications/books/lunar_sourcebook/pdf/Chapter09.pdf", date: "1991"}
  - {title: "NASA: Technology Readiness Levels", url: "https://www.nasa.gov/directorates/somd/space-communications-navigation-program/technology-readiness-levels/", date: ""}
  - {title: "Univ. of Hawaii SOEST: Scarce ice in Moon's darkest regions (ShadowCam)", url: "https://www.soest.hawaii.edu/soestwp/announce/news/scarce-ice-in-moons-darkest-regions/", date: "Mar 2026"}
  - {title: "Boazman et al.: The distribution and accessibility of geologic targets near the lunar south pole and candidate Artemis landing sites (PSJ 3:275)", url: "https://iopscience.iop.org/article/10.3847/PSJ/aca590", date: "Dec 2022"}
  - {title: "CAS: Chang'e-5 lander detects water on the Moon's surface in situ", url: "https://english.cas.cn/head/202201/t20220108_295734.shtml", date: "Jan 2022"}
  - {title: "NASA JSC Lunar Sample Compendium: Apollo 17 deep drill core 70001–70009", url: "https://curator.jsc.nasa.gov/lunar/lsc/a17drill.pdf", date: ""}
  - {title: "Biemann et al.: The search for organic substances and inorganic volatile compounds in the surface of Mars (Viking GCMS, NTRS)", url: "https://ntrs.nasa.gov/citations/19780027538", date: "Sep 1977"}
  - {title: "USGS Astrogeology: Lunar M3 Water Map PDS4 Archive (Li et al. 2023, Nature Astronomy; doi:10.17189/gmce-w279)", url: "https://astrogeology.usgs.gov/search/map/lunar_m3_water_map_pds4_archive", date: "Dec 2022"}
  - {title: "NASA GSFC PGDA: A New View of the Lunar South Pole from LOLA (slope and hillshade, Barker et al. 2023)", url: "https://pgda.gsfc.nasa.gov/products/90", date: "2023"}
risks:
  - {sev: Critical, title: "The lander tips over and the rover never drives off (as on IM-1 and IM-2)", fix: "Fly the two rovers on two different lander providers"}
  - {sev: High, title: "Water escapes before a sample is sealed: about 30% from 4.5 wt% soil and about 80% from 0.8 wt% soil in NASA vacuum tests", fix: "Brush drill bites straight into the chamber and seal at once; calibrate the losses on icy simulant before flight"}
  - {sev: High, title: "The bake chamber is about 20 times bigger than any tested lunar oven", fix: "Build a full-size chamber first and test it cold, in vacuum, with icy simulant"}
  - {sev: High, title: "Ice is patchy, so a few samples may miss it or overstate it", fix: "Sample a grid of points in each crater, guided by the neutron spectrometer"}
  - {sev: Medium, title: "Icy soil sticks in the scoop or the chamber inlet, as on Phoenix", fix: "Vibrate the scoop and screen; keep the scoop cold so ice does not melt and refreeze"}
---
## The prospector rover

![Phoenix's rasp under its scoop, on the engineering model]({{ '/assets/milestones/phoenix-rasp.jpg' | relative_url }})

*The powered rasp under the scoop of Phoenix's robotic arm, on the engineering model at the University of Arizona. Phoenix used it to chip icy Martian soil. Photo: NASA/JPL/University of Arizona, [PIA10961](https://images.nasa.gov/details/PIA10961).*

Two rovers (C01.1) land on two different landers and drive into the permanently shadowed craters near the base. At each stop the rover:

1. **Finds** the hydrogen with a neutron spectrometer while it drives.
2. **Scoops** loose soil and small debris. A rasp chips hard icy ground at the surface.
3. **Drills** the hard, ice-cemented ground into cuttings, 10 cm at a time, down to 1 m. Each bite is brushed straight into the bake chamber.
4. **Bakes** each batch in a sealed chamber at 150, 350 and 450 °C, and measures the water that comes out.

So the rover does not just detect water. It measures how much heated soil gives up, which is what the ice mine will do later at full size (DD-025).

## What we looked at

<div class="tabs" id="m01tabs">
<input type="radio" name="m01tab" id="m01t1" checked><label for="m01t1">Past missions</label>
<input type="radio" name="m01tab" id="m01t2"><label for="m01t2">Getting water out</label>
<input type="radio" name="m01tab" id="m01t3"><label for="m01t3">Drilling</label>
<input type="radio" name="m01tab" id="m01t4"><label for="m01t4">Closest rovers</label>
<input type="radio" name="m01tab" id="m01t5"><label for="m01t5">Our rover</label>
<input type="radio" name="m01tab" id="m01t6"><label for="m01t6">Readiness</label>
<div class="tabpanels" markdown="1">
<div class="tabpanel" id="m01p1" markdown="1">
<div class="tp-text" markdown="1">

### Missions that sampled water ice

**No mission has yet measured ice in place inside a lunar shadowed crater.**

| Mission | What it did | Result |
|---|---|---|
| Viking (Mars, 1976) | Heated soil to 500 °C | Water and CO₂ released<sup class="r">[30](#s30)</sup> |
| Apollo 17 (Moon, 1972) | Drilled a 3 m core | Returned to Earth; extraction "was very difficult"<sup class="r">[29](#s29)</sup> |
| Phoenix (Mars, 2008) | Scooped and rasped icy soil into 8 small ovens | Ice-cemented soil could not be delivered; a drier layer held ~2% ice<sup class="r">[1](#s1)</sup> |
| LCROSS (Moon, 2009) | Crashed into Cabeus crater | 5.6 ± 2.9 wt% water in the debris<sup class="r">[5](#s5)</sup> |
| Curiosity (Mars, 2012–) | Scooped soil into its SAM ovens | 1.5–3 wt% water<sup class="r">[3](#s3)</sup> |
| Chang'e-5 (Moon, 2020) | Spectrometer on the lander | Under 120 ppm in the soil<sup class="r">[28](#s28)</sup> |
| PRIME-1 on IM-2 (Moon, 2025) | TRIDENT drill and MSolo | Lander tipped; the drill "did not penetrate the ground"<sup class="r">[6](#s6)</sup> |

**Coming up:** VIPER (2027, on Blue Moon Mark 1)<sup class="r">[9](#s9)</sup>, ESA's PROSPECT on IM-4 (2027)<sup class="r">[12](#s12)</sup>, Chang'e-7 (listed for 2027)<sup class="r">[10](#s10)</sup>, LUPEX (no earlier than 2028)<sup class="r">[11](#s11)</sup>. We use whatever arrives but don't wait for it.

</div>
<div class="tp-media" markdown="1">

![Phoenix TEGA oven doors open, ready for a sample]({{ '/assets/milestones/phoenix-tega-oven.jpg' | relative_url }})
![Curiosity's first drilled sample in its scoop]({{ '/assets/milestones/curiosity-drill-sample-in-scoop.jpg' | relative_url }})

Top: Phoenix's first TEGA oven ready for a sample, NASA/JPL-Caltech/University of Arizona/Max Planck Institute, [PIA10769](https://images.nasa.gov/details/PIA10769). Bottom: Curiosity's first drilled sample in its scoop, NASA/JPL-Caltech/MSSS, [PIA16729](https://images.nasa.gov/details/PIA16729).
{: .tp-cap}

</div>
</div>
<div class="tabpanel" id="m01p2" markdown="1">
<div class="tp-text" markdown="1">

### Getting the water out

**wt%** (weight percent) is the share of a sample's mass that is water. 1 kg of soil at 1 wt% holds 10 g of water. LCROSS found 5.6 wt% at Cabeus<sup class="r">[5](#s5)</sup>, and many places will hold far less, so heating must collect grams of water from kilograms of soil.

Two kinds of hardware exist:

| Kind | Example | What it does | Status |
|---|---|---|---|
| Analytical oven | Resource Prospector OVEN | 12 cc from the drill, weighed, sealed, heated to 150/350/450 °C<sup class="r">[14](#s14)</sup> | Tested; never flew |
| Analytical oven | ESA ProSPA (PROSPECT) | Up to 25 single-use ovens to 950 °C<sup class="r">[12](#s12)</sup> | Flies on IM-4, 2027 |
| Bulk extraction | LUWEX (DLR-led) | Stirred crucible; ~65% of the water out at ~110 K in vacuum<sup class="r">[18](#s18)</sup> | Lab, TRL 4–5 |
| Bulk extraction | NASA LADI | Heated screw conveyor<sup class="r">[20](#s20)</sup> | Lab, TRL 4 |
| Bulk extraction | NASA MSFC microwave | ≥ 85% of the water out of 0.5–2% icy simulant in 5 min<sup class="r">[19](#s19)</sup> | Lab demo |

Our bake chamber sits between the two: bigger than an analytical oven, so it collects grams of water, but far smaller than a mining plant.

</div>
<div class="tp-media" markdown="1">

![Resource Prospector test rover in a regolith bin]({{ '/assets/tech/resource-prospector-nasa.jpg' | relative_url }})

A lightweight test version of NASA's Resource Prospector at Kennedy, June 2017. It carries no drill or oven; no flight rover was built. NASA/Kim Shiflett, [KSC-20170628-PH_KLS01_0073](https://images.nasa.gov/details/KSC-20170628-PH_KLS01_0073).
{: .tp-cap}

</div>
</div>
<div class="tabpanel" id="m01p3" markdown="1">
<div class="tp-text" markdown="1">

### Drilling into the shadowed ground

| Drill | Depth | Status |
|---|---|---|
| TRIDENT (Honeybee) | 1 m, in 10 cm bites; 26.5 kg | Flew on PRIME-1, did not drill; on VIPER<sup class="r">[6](#s6)</sup> |
| ProSEED (ESA) | 1 m; 31.8 kg package | IM-4, 2027<sup class="r">[12](#s12)</sup> |
| LUPEX auger | ~1.5 m | No earlier than 2028<sup class="r">[11](#s11)</sup> |
| ExoMars drill (Mars) | 2 m | Launch late 2028<sup class="r">[13](#s13)</sup> |
| Apollo drill (crew) | 3 m | Flew 1971–72<sup class="r">[29](#s29)</sup> |

**We use 1 m.** It is the deepest that has flight-ready robotic hardware. No robotic lunar drill found in this research reaches 3 m.

**Ice makes the ground hard.** Soil with about 10.6% ice behaves like "strong limestone or sandstone"<sup class="r">[21](#s21)</sup>, so the drill's job is to break it into cuttings. No drill has been tested at true shadowed-crater cold (about 25–40 K); TRIDENT's coldest test was below −100 °C<sup class="r">[6](#s6)</sup>.

</div>
<div class="tp-media" markdown="1">

![VIPER mobility platform in testing at NASA Glenn]({{ '/assets/tech/viper-rover-nasa.jpg' | relative_url }})

VIPER, which carries the TRIDENT drill, in mobility testing at NASA Glenn, October 2019. NASA/GRC/Bridget Caswell, [GRC-2019-C-09947](https://images.nasa.gov/details/GRC-2019-C-09947).
{: .tp-cap}

</div>
</div>
<div class="tabpanel" id="m01p4" markdown="1">
<div class="tp-text" markdown="1">

### The closest rovers

No flown rover does all this on the Moon. Two come close, and our design combines them:

- **Resource Prospector (Moon) is the closest design.** A polar rover whose 1 m drill brushed samples "directly into a cup/oven"<sup class="r">[14](#s14)</sup>. Its oven survived vibration tests and worked in thermal vacuum from −50 to 75 °C<sup class="r">[15](#s15)</sup>. NASA cancelled it in 2018<sup class="r">[17](#s17)</sup>.
- **Curiosity (Mars) is the closest that has flown.** A scoop and a drill both feed one handling device that sieves and portions the sample<sup class="r">[4](#s4)</sup> for ovens inside the rover. But its samples are milligrams of warm, dry soil.

Phoenix adds the lesson: its scoop and rasp dug icy soil, but icy samples stuck in the scoop<sup class="r">[2](#s2)</sup>.

</div>
<div class="tp-media" markdown="1">

![Curiosity's first drilled sample in its scoop]({{ '/assets/milestones/curiosity-drill-sample-in-scoop.jpg' | relative_url }})

Curiosity's drill passes its powder to the scoop, then to the ovens. NASA/JPL-Caltech/MSSS, [PIA16729](https://images.nasa.gov/details/PIA16729).
{: .tp-cap}

</div>
</div>
<div class="tabpanel" id="m01p5" markdown="1">
<div class="tp-text" markdown="1">

### Our rover

| Part | What it does |
|---|---|
| Scoop arm | Bladed scoop and rasp (Phoenix layout<sup class="r">[2](#s2)</sup>); ~10 mm screen keeps stones out |
| Drill | Breaks icy ground into cuttings; each 10 cm bite brushed into the chamber |
| Bake chamber | ~250 cm³, about 0.4 kg of soil; sealed, heated in steps to 450 °C, then dumped and reused |
| Gas readout | Known-volume gauge, mass spectrometer, and a cold trap that freezes out the water |

**Per batch** (this plan's arithmetic):

- **Soil:** soil in the top 30 cm is about 1.53–1.63 g/cm³<sup class="r">[24](#s24)</sup>, so ~0.4 kg fills the chamber.
- **Water:** 2 g at 0.5 wt%, 20 g at 5 wt%.
- **Energy:** ~150 Wh, from regolith heat capacity<sup class="r">[22](#s22)</sup> and the heat needed to turn ice to vapour<sup class="r">[23](#s23)</sup>, doubled for heat leaks. Two batches per trip into the shadow still leave a 4 kWh battery nearly 2× margin.

**Water lost before sealing.** In NASA vacuum tests, sealing took about 5 minutes, and samples lost ~30% of their water from 4.5 wt% soil and ~80% from 0.8 wt% soil<sup class="r">[16](#s16)</sup>. So each bite is sealed at once and the losses are calibrated on the ground.

</div>
<div class="tp-media" markdown="1">

![Phoenix rasp on the scoop]({{ '/assets/milestones/phoenix-rasp.jpg' | relative_url }})

The scoop arm copies Phoenix's blades and rasp. NASA/JPL/University of Arizona, [PIA10961](https://images.nasa.gov/details/PIA10961).
{: .tp-cap}

</div>
</div>
<div class="tabpanel" id="m01p6" markdown="1">
<div class="tp-text" markdown="1">

### Readiness

NASA's TRL 6 means a fully working prototype; TRL 7 means shown working in space<sup class="r">[25](#s25)</sup>. A system is only as ready as its least mature critical part.

| Part | TRL |
|---|---|
| Drill, mass spectrometer | 6–7 (flown, never drilled the Moon) |
| Rover, neutron spectrometer | 6 (VIPER designs) |
| Scoop arm | 6 (flew on Mars; untested at lunar cold) |
| **Bake chamber** | **4** (only a 12 cc version tested) |

**The rover is TRL 4.** Building and testing a full-size chamber cold, in vacuum, with icy simulant would bring it to about TRL 5–6. That is the first test.

</div>
<div class="tp-media" markdown="1">

![Phoenix TEGA oven]({{ '/assets/milestones/phoenix-tega-oven.jpg' | relative_url }})

Phoenix's TEGA oven: the flown ancestor of a sample oven. NASA/JPL-Caltech/University of Arizona/Max Planck Institute, [PIA10769](https://images.nasa.gov/details/PIA10769).
{: .tp-cap}

</div>
</div>
</div>
</div>

## Surface water around the base

![Moon Mineralogy Mapper surface water within 10 km of the base, over slope, with the base and solar towers]({{ '/assets/milestones/m3-water-base-10km.jpg' | relative_url }})

*Surface water (OH plus H₂O, top ~1 mm) from the Moon Mineralogy Mapper water maps of Li et al. 2023<sup class="r">[31](#s31)</sup>, over NASA's LOLA slope map<sup class="r">[32](#s32)</sup>. Open Moon processing: the six maps are averaged per pixel and smoothed to ~300 m for display.*

Within 10 km of the base (this plan's processing of the archive data):

| Measure | Value |
|---|---|
| Median | **~260 ppm** (0.026 wt%) |
| Mean | ~580 ppm |
| Middle 80% of the area | ~105–1,415 ppm |
| Area with a value | 89% |

**Read these with care.** The archive warns users to "use this dataset with caution for other purposes", and the mapping uncertainty is 20%<sup class="r">[31](#s31)</sup>. Almost half the pixels near the base hold exactly 20 ppm, a value the archive does not explain. They are left out above; if they are real low readings, the median falls to ~34 ppm. These maps also cannot tell OH from H₂O<sup class="r">[31](#s31)</sup>. So the surface number is a range, roughly 30–300 ppm, and it is the M01 rovers that will measure it.

## Where to prospect

From the [M00 maps]({{ '/plan/m00-site-selection/' | relative_url }}):

- **de Gerlache floor**, next to the primary base, including ShadowCam's unexplained bright spot at 88.5352°S, 97.4007°W.
- **Shackleton floor**, next to the backup base.
- **Unmeasured cold traps** along the ridge, such as Spudis.

ShadowCam found little widespread surface ice, only small patches<sup class="r">[26](#s26)</sup>. So each crater gets a grid of sampling points, not one hole.

## Ground truth for site preparation

Orbital images can't show rocks smaller than about 1–4 m<sup class="r">[27](#s27)</sup>. The prospectors image the planned pad and road routes and log ground strength from the drill and scoop, and hand both to M02, which runs at the same time.

## Go / no-go

If the measured water is there, the base goes ahead at de Gerlache. If not, the plan switches to the backup site by Shackleton. All data is published openly.
