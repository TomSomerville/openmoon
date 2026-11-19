---
id_code: M02
order: 2
title: Site preparation
phase: 0
content_first: true
window: "Years 0–5"
summary: Robots clear rocks, grade the ground flat, and fuse regolith into hard surfaces for landing pads and roads, with berms to catch rocket blast.
trl_min: 4
depends_on: [M00]
spec:
  - {k: Fleet, v: "4 excavators with blades and drums (C02.1), 2 regolith fusing robots (C02.3)"}
  - {k: Output, v: "2 hardened landing pads (C02.2), ~5 km of graded roads, ejecta berms"}
  - {k: Runs alongside, v: "M01 Site prospecting; uses its small-rock and ground data"}
technologies:
  - {name: "NASA ISRU Pilot Excavator (IPEx)", use: "Digging, grading and berm building", status: "TRL 5 design (2024); no flight date", trl: 5, src: 1}
  - {name: "RASSOR 2.0 (NASA KSC)", use: "Light digging and berms", status: "Built a test berm in Earth conditions", trl: 5, src: 2}
  - {name: "NASA LANCE bulldozer blade", use: "Clearing rocks, levelling, berms", status: "Field-tested on the Chariot rover, Moses Lake, 2008", trl: 5, src: 9}
  - {name: "ICON Project Olympus (laser melting)", use: "Fused pads, roads and blast shields", status: "Chosen in NASA's 2022–23 landing-pad material down-select", trl: 4, src: 14}
  - {name: "ESA PAVER (laser standing in for concentrated sunlight)", use: "Interlocking glassy paving tiles", status: "ESA project 2021–22; lab tiles made in air", trl: 4, src: 11}
  - {name: "NASA MSFC microwave sintering (MMPACT)", use: "Fused pads and roads by microwave", status: "Bench and vacuum-chamber tests; not in the 2022–23 down-select", trl: 4, src: 13}
sources:
  - {title: "NASA NTRS: IPEx TRL 5 design overview (ASCEND 2024)", url: "https://ntrs.nasa.gov/api/citations/20240008162/downloads/ASCEND24_IPEx%20TRL%205%20Design%20Overview.pdf", date: "2024"}
  - {title: "Gelino, NASA KSC: Lunar Innovation Park site plan and bulk regolith feature design (NTRS 20260002816)", url: "https://ntrs.nasa.gov/api/citations/20260002816/downloads/329%20-%20Site%20Plan%20and%20Bulk%20Presentation.pdf", date: "Apr 2026"}
  - {title: "Metzger et al., NASA NTRS 20120000029: Further analysis on the mystery of the Surveyor III dust deposits", url: "https://ntrs.nasa.gov/api/citations/20120000029/downloads/20120000029.pdf", date: "2012"}
  - {title: "Metzger et al., NASA KSC: ISRU implications for lunar and martian plume effects (arXiv 2104.06248)", url: "https://arxiv.org/pdf/2104.06248", date: "Apr 2021"}
  - {title: "Boazman et al.: Mapping potential hazards and identifying sampling points within lunar south polar region areas of interest (PSJ)", url: "https://iopscience.iop.org/article/10.3847/PSJ/ad8fb0", date: "2024"}
  - {title: "Boazman et al.: The distribution and accessibility of geologic targets near the lunar south pole and candidate Artemis landing sites (PSJ 3:275)", url: "https://iopscience.iop.org/article/10.3847/PSJ/aca590", date: "Dec 2022"}
  - {title: "NASA STRG: ASPECT, autonomous site preparation, excavation, compaction and testing", url: "https://www.nasa.gov/directorates/stmd/space-tech-research-grants/aspect-autonomous-site-preparation-excavation-compaction-and-testing", date: "Apr 2022"}
  - {title: "Brandić Lipińska et al.: PAVER roadmap (IAC 2022)", url: "https://liquifer.com/wp-content/uploads/2022/12/PAVER_IAC22_0109_FINAL.pdf", date: "2022"}
  - {title: "Mueller et al.: Lightweight bulldozer attachment for construction and excavation on the lunar surface (LANCE, NTRS 20130012987)", url: "https://ntrs.nasa.gov/api/citations/20130012987/downloads/20130012987.pdf", date: "2009"}
  - {title: "Just et al.: Effect of inlet geometry on excavation forces for small-scale continuous excavators (Acta Geotechnica 19)", url: "https://link.springer.com/content/pdf/10.1007/s11440-023-01914-4.pdf", date: "2024"}
  - {title: "ESA: How to make roads on the Moon (PAVER)", url: "https://www.esa.int/Enabling_Support/Space_Engineering_Technology/How_to_make_roads_on_the_Moon", date: "Oct 2023"}
  - {title: "Ginés-Palomares et al.: Laser melting manufacturing of large elements of lunar regolith simulant for paving on the Moon (Scientific Reports 13:15593, CC BY 4.0)", url: "https://www.nature.com/articles/s41598-023-42008-1", date: "Oct 2023"}
  - {title: "Effinger, NASA MSFC: Microwave Structure Construction Capability (NTRS 20205010871)", url: "https://ntrs.nasa.gov/api/citations/20205010871/downloads/Moon%20Village-MSCC%202020-12-09.pptx.pdf", date: "Dec 2020"}
  - {title: "NASA NTRS: MMPACT Jamboree poster 2023", url: "https://ntrs.nasa.gov/api/citations/20230008890/downloads/MMPACT%20Jamboree%20Poster%202023%20-%20final.pdf", date: "2023"}
  - {title: "Metzger & Autry: The cost of lunar landing pads with a trade study of construction methods (arXiv 2205.00378)", url: "https://arxiv.org/pdf/2205.00378", date: "May 2022"}
  - {title: "NASA: NASA tests landing pad materials for future lunar missions", url: "https://www.nasa.gov/centers-and-facilities/kennedy/nasa-tests-landing-pad-materials-for-future-lunar-missions", date: "Oct 2021"}
  - {title: "Lee et al.: CraterGrader, autonomous robotic terrain manipulation for lunar site preparation (arXiv 2311.01697)", url: "https://ar5iv.labs.arxiv.org/html/2311.01697", date: "2023"}
  - {title: "Gaier, NASA/TM-2005-213610: The effects of lunar dust on EVA systems during Apollo", url: "https://ntrs.nasa.gov/citations/20050160460", date: "2005"}
risks:
  - {sev: Critical, title: "Rocket exhaust sandblasts the site before pads exist", fix: "Fuse the first pad and pile its berm before heavier landers come"}
  - {sev: High, title: "No fused surface has been tested under a real lander engine; glass may shatter into sharp fragments", fix: "Test small pads with small landers first; use separate interlocking tiles"}
  - {sev: High, title: "Fusing may be far slower than planned: the only measured lab figure is about 15× the energy per kg C02.3 assumes (ESTIMATE)", fix: "Measure fusing energy in vacuum early; fuse only the pad centre and busy road sections"}
  - {sev: High, title: "Fusing needs tens of kilowatts and Phase 0 has no power supply yet", fix: "Open: robots with their own power, concentrated sunlight (PAVER's approach), or wait for power"}
  - {sev: Medium, title: "Light robots have little traction in lunar gravity, so blades cannot push hard", fix: "Grade in thin passes; dig with drums; test vibrating blades"}
---
## The plan

![IPEx excavator digging in the regolith bin at NASA Kennedy]({{ '/assets/milestones/ipex-regolith-bin.jpg' | relative_url }})

*NASA's ISRU Pilot Excavator digging in the Swamp Works regolith bin at Kennedy, July 2022. Photo: NASA/Frank Michaux, [KSC-20220728-PH-FMX01_0070](https://images.nasa.gov/details/KSC-20220728-PH-FMX01_0070).*

While the prospectors (M01) measure the water, robots get the ground ready:

1. **Clear rocks.** Push small ones aside with a blade; pick up and haul larger ones away.
2. **Grade.** Blade the ground flat and compact it.
3. **Fuse.** Melt the top layer of regolith into a hard, glassy surface.
4. **Build.** Two hardened landing pads (C02.2), about 5 km of roads, and berms around the pads.

The fleet is four excavators with blades and drums (C02.1) and two fusing robots (C02.3).

## What we looked at

<div class="tabs" id="m02tabs">
<input type="radio" name="m02tab" id="m02t1" checked><label for="m02t1">Why prepare</label>
<input type="radio" name="m02tab" id="m02t2"><label for="m02t2">Clearing rocks</label>
<input type="radio" name="m02tab" id="m02t3"><label for="m02t3">Grading</label>
<input type="radio" name="m02tab" id="m02t4"><label for="m02t4">Fusing regolith</label>
<input type="radio" name="m02tab" id="m02t5"><label for="m02t5">Pads, roads, berms</label>
<input type="radio" name="m02tab" id="m02t6"><label for="m02t6">Open questions</label>
<div class="tabpanels" markdown="1">
<div class="tabpanel" id="m02p1" markdown="1">
<div class="tp-text" markdown="1">

### Why the site is prepared first

A lander's exhaust throws dust and rock sideways. Apollo 12 landed 155 m from the Surveyor III probe<sup class="r">[3](#s3)</sup>. Surveyor's surface was pitted by soil particles that hit at 300 m/s to 2 km/s<sup class="r">[4](#s4)</sup>.

In Apollo landing videos the dust blew out only 1–3° above horizontal, at about 1 km/s<sup class="r">[4](#s4)</sup>. Bigger landers throw more, further. So hard pads and berms come before the big cargo.

Dust also wrecks equipment: on Apollo 12 every environmental and gas sample seal failed because of dust<sup class="r">[18](#s18)</sup>.

</div>
<div class="tp-media" markdown="1">

![Surveyor III with the Apollo 12 lunar module behind it]({{ '/assets/milestones/surveyor3-apollo12.jpg' | relative_url }})

Surveyor III, with the Apollo 12 lunar module on the horizon, November 1969. NASA, [AS12-48-7133](https://images.nasa.gov/details/AS12-48-7133).
{: .tp-cap}

</div>
</div>
<div class="tabpanel" id="m02p2" markdown="1">
<div class="tp-text" markdown="1">

### Clearing rocks

On the de Gerlache rim area GR1 (about 1.5 km²), researchers mapped 48 boulders and found slopes under 6°<sup class="r">[5](#s5)</sup>. But rocks smaller than about 1–4 m can't be seen from orbit<sup class="r">[6](#s6)</sup>, so the M01 prospectors count them first.

| Way | Example |
|---|---|
| **Push** with a blade | NASA's LANCE blade on the Chariot rover was built for "area clearing of rocks, leveling, dozing, grading, and berm construction"<sup class="r">[9](#s9)</sup> |
| **Pick up and haul** | NASA's ASPECT project pairs a rover with a "rock and regolith grader" and lists boulder moving<sup class="r">[7](#s7)</sup> |
| **Rake and sieve** | ESA's PAVER team says a site is raked and graded "to remove larger rocks" before paving<sup class="r">[8](#s8)</sup> |

</div>
<div class="tp-media" markdown="1">

![RASSOR 2.0 in the regolith bin at NASA Kennedy]({{ '/assets/milestones/rassor-regolith-bin.jpg' | relative_url }})

RASSOR 2.0 in a regolith bin at Kennedy, September 2016. NASA/Dimitri Gerondidakis, [KSC-20160929-PH_DNG01_0039](https://images.nasa.gov/details/KSC-20160929-PH_DNG01_0039).
{: .tp-cap}

</div>
</div>
<div class="tabpanel" id="m02p3" markdown="1">
<div class="tp-text" markdown="1">

### Grading with a blade

On Earth, LANCE cleared a 25 × 25 m area in about 2.5 hours and built a 1.3 m berm in about 4 hours<sup class="r">[9](#s9)</sup>.

On the Moon, light machines have little weight to push with. The ~700 kg Apollo rover's usable traction there was calculated at only 239 N<sup class="r">[10](#s10)</sup>. Vibrating the cutting edge cut forces by up to 50% in tests<sup class="r">[10](#s10)</sup>.

So the excavators grade in thin passes and dig with drums (plan design). A small Carnegie Mellon robot graded sand to 0.11°, against NASA's ±1° target<sup class="r">[17](#s17)</sup>.

</div>
<div class="tp-media" markdown="1">

![IPEx excavator in the regolith bin]({{ '/assets/milestones/ipex-regolith-bin.jpg' | relative_url }})

IPEx uses counter-rotating bucket drums, which need little traction. NASA/Frank Michaux, [KSC-20220728-PH-FMX01_0070](https://images.nasa.gov/details/KSC-20220728-PH-FMX01_0070).
{: .tp-cap}

</div>
</div>
<div class="tabpanel" id="m02p4" markdown="1">
<div class="tp-text" markdown="1">

### Fusing regolith into glass

Heat melts or sinters the top layer into a hard surface that exhaust can't blow away.

**The "ESA microwave rover" is two projects.** ESA's paving project, **PAVER** (2021–22), uses light: a 12 kW laser standing in for sunlight that a Fresnel lens a couple of metres across would focus<sup class="r">[11](#s11)</sup>. One of its two plans is a mobile setup on a rover or lander arm that melts tiles in place<sup class="r">[8](#s8)</sup>. The **microwave** paver vehicle is NASA's: Marshall's team set a goal of "a 2mT microwave paver vehicle" for pads and roads<sup class="r">[13](#s13)</sup>.

| Method | Result |
|---|---|
| Laser (ICON, NASA) | Only one of three materials to pass NASA's 2022–23 landing-pad tests<sup class="r">[14](#s14)</sup> |
| Sunlight (ESA PAVER) | Interlocking glassy tiles ~22–25 cm across, one ~2 cm layer, 94 MPa average (56–216 MPa), made in air. Reheated tracks cracked<sup class="r">[12](#s12)</sup>. ESA estimates 115 days for a 100 m², 2 cm pad<sup class="r">[11](#s11)</sup> |
| Microwave (NASA MSFC) | Bench and vacuum tests<sup class="r">[13](#s13)</sup>. A cost study calls it "currently the most favorable method" for a pad's hot centre, needing a modelled 21.73 kWh/m²<sup class="r">[15](#s15)</sup> |

We keep laser as the baseline, with sunlight and microwave as alternatives (plan design).

</div>
<div class="tp-media" markdown="1">

![PAVER interlocking paving tiles melted from lunar regolith simulant]({{ '/assets/milestones/paver-interlocking-tiles.jpg' | relative_url }})
![PAVER laser melting setup]({{ '/assets/milestones/paver-laser-setup.jpg' | relative_url }})

Top: PAVER's interlocking tiles (200 mm scale bar). Bottom: the laser setup. Cropped from Fig. 3 of Ginés-Palomares et al. 2023, *Scientific Reports*, [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)<sup class="r">[12](#s12)</sup>.
{: .tp-cap}

</div>
</div>
<div class="tabpanel" id="m02p5" markdown="1">
<div class="tp-text" markdown="1">

### Pads, roads and berms

| Use | What the sources say |
|---|---|
| **Landing pads** (C02.2) | A fused centre where the plume is hottest, a compacted outer apron and blast barriers, as in NASA Kennedy's layout<sup class="r">[2](#s2)</sup>. NASA has hot-fire tested sintered basalt pavers on the ground<sup class="r">[16](#s16)</sup> |
| **Roads** | Graded everywhere, fused on busy sections (plan design). PAVER warns its rough glass could hurt wheel grip, which is untested<sup class="r">[12](#s12)</sup> |
| **Berms** | Spray is low, so a berm can block most of it<sup class="r">[4](#s4)</sup>. NASA Kennedy's 2026 design: 2.5 m high, 1 m crest, 8 m from the lander, sized for ~625 kg landers<sup class="r">[2](#s2)</sup> |

A scour hole under a lander would throw bigger debris over berms, so berms work best with a hard pad<sup class="r">[4](#s4)</sup>.

</div>
<div class="tp-media" markdown="1">

![PAVER interlocking tiles]({{ '/assets/milestones/paver-interlocking-tiles.jpg' | relative_url }})

Tiles rather than one big slab, because reheated slabs crack. Ginés-Palomares et al. 2023, CC BY 4.0<sup class="r">[12](#s12)</sup>.
{: .tp-cap}

</div>
</div>
<div class="tabpanel" id="m02p6" markdown="1">
<div class="tp-text" markdown="1">

### Open questions

- **Power for fusing.** The fusing robots need tens of kilowatts, and Phase 0 has no power supply yet. Options: robots with their own power, concentrated sunlight (PAVER's approach), or wait for a power supply.
- **Fusing rate.** The fusing robot (C02.3) assumes ~72 kg/h from 30 kW. PAVER's lab melt needed about 23 MJ/kg, which would give about 5 kg/h (this plan's arithmetic from<sup class="r">[12](#s12)</sup>).
- **Laser, sunlight or microwave.** NASA chose laser for its pad material<sup class="r">[14](#s14)</sup>; a cost study prefers microwave<sup class="r">[15](#s15)</sup>; ESA uses sunlight<sup class="r">[11](#s11)</sup>.
- **Berm size** for landers far heavier than the ~625 kg NASA Kennedy designed for<sup class="r">[2](#s2)</sup>.

</div>
<div class="tp-media" markdown="1">

![Surveyor III and Apollo 12]({{ '/assets/milestones/surveyor3-apollo12.jpg' | relative_url }})

What pads and berms are for. NASA, [AS12-48-7133](https://images.nasa.gov/details/AS12-48-7133).
{: .tp-cap}

</div>
</div>
</div>
</div>

## Order of work

1. Plan routes from the M00 maps and the M01 rock and ground data. Pads go on natural ground of 8° or less (DD-011).
2. Land the excavators on the pad site.
3. Clear rocks and grade the first pad area and roads.
4. Fuse pad 1, pile its berm, and test it with a small lander.
5. Build pad 2 for heavier landers, then finish the roads.
