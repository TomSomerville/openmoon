---
id_code: M02
order: 2
title: Site preparation
phase: 0
window: "Years 0–5"
summary: Robots clear rocks, grade the ground flat, and fuse regolith into hard surfaces for landing pads and roads, with berms to catch rocket blast, so the site is ready before anything the base depends on lands.
objective: "Prepare the ground at the base site at the same time as prospecting (M01). Clear small rocks by pushing them aside or picking them up and hauling them away, grade and compact level areas with blades, build at least two hardened landing pads and the roads between them and the base, and pile berms that stop rocket exhaust spraying dust and rock across the site."
trl_min: 4
depends_on: [M00]
spec:
  - {k: Rock clearing, v: "Push small rocks aside with a blade; pick up and haul larger ones; rake and sieve where rocks are dense"}
  - {k: Grading, v: "Blade-graded and compacted pad sites, roads and work areas"}
  - {k: Pads, v: "2 hardened pads with fused-regolith surfaces (small and medium landers first, then heavy)"}
  - {k: Roads, v: "~5 km graded and compacted, fused on busy sections (plan design)"}
  - {k: Berms, v: "Ejecta berms around each pad"}
  - {k: Fleet, v: "4 excavators with blades and drums (C02.1) + 2 regolith fusing robots (C02.3)"}
  - {k: Runs alongside, v: "M01 Site prospecting (same years); uses its ground and small-rock data"}
cost: {low: 2.88, high: 7.3, note: "robot fleet plus delivery; pad and road material is local regolith"}
cost_items:
  - {item: "Excavator robots ×4 with blades (IPEx / RASSOR class)", low: 0.1, high: 0.3, basis: "ESTIMATE"}
  - {item: "Delivery of excavators (~1.2 t, medium landers)", low: 0.48, high: 1.2, basis: "4 × ~300 kg scaled-up units (C02.1 ESTIMATE; RASSOR 2.0 is 65 kg dry, IPEx 30 kg-class [src 2]) × $0.4–1.0M/kg"}
  - {item: "Regolith fusing robots ×2", low: 0.2, high: 0.5, basis: "ESTIMATE; ICON's NASA R&D contract alone is $57.2M [src 4]"}
  - {item: "Delivery of fusing robots (~3 t)", low: 1.2, high: 3.0, basis: "3 t × $0.4–1.0M/kg (ESTIMATE)"}
  - {item: "Binder / additives shipped from Earth (~2 t)", low: 0.8, high: 2.0, basis: "2 t × $0.4–1.0M/kg (ESTIMATE); only if fusing alone is not enough"}
  - {item: "Engineering and operations", low: 0.1, high: 0.3, basis: "ESTIMATE"}
exit_criteria:
  - "Pad sites, roads and work areas cleared of rocks larger than the plan's limit and graded to within ±1° (NASA LuSTR target as cited for CraterGrader)."
  - "At least two hardened pads survive repeated landings with no measurable damage to equipment beyond 500 m."
  - "Graded roads connect every planned site; rovers drive them autonomously."
  - "Ejecta berms around each pad, built to the measured spray angles."
  - "Ejecta measured during a landing on a hardened pad confirms the model used for the keep-out zones."
workstreams:
  - name: Rock clearing
    desc: Get rocks off the pad sites and roads.
    items: ["Blade pushes small rocks to the edge of the work area", "Scoop or grapple picks up larger rocks and hauls them to a spoil pile", "Rake and sieve where small rocks are dense", "Use M01 small-rock survey to plan routes"]
  - name: Grading
    desc: Make the ground flat and firm.
    items: ["Blade grading to ±1°", "Compaction by repeated driving or a roller", "Stockpiles of spare regolith for berms"]
  - name: Fused surfaces
    desc: Turn the top layer of regolith into a hard, dust-free surface.
    items: ["Laser melting (NASA's landing-pad choice, ICON)", "Microwave sintering (NASA MSFC concept; favoured in one cost study)", "Concentrated sunlight (ESA PAVER)", "Interlocking tiles rather than one large slab"]
  - name: Landing pads and roads
    desc: Use the fused surfaces where they matter most.
    items: ["Pad: fused inner zone, compacted outer apron", "Roads: graded everywhere, fused on busy sections", "Marker beacons for navigation"]
  - name: Berms
    desc: Walls of piled regolith that catch low-angle rocket spray.
    items: ["Ejecta berms around each pad", "Height and standoff from NASA KSC's 2026 design as a starting point", "Fused crest to test later"]
technologies:
  - {name: "NASA ISRU Pilot Excavator (IPEx)", use: "Excavation, grading and berm building", status: "TRL 5 design (2024); target 42 kg/h, 10 t over an 11-day mission; no flight date", trl: 5, src: 1}
  - {name: "RASSOR 2.0", use: "Light excavation and berm building", status: "Under 100 kg; built a test berm in Earth conditions", trl: 5, src: 3}
  - {name: "NASA LANCE bulldozer blade", use: "Rock clearing, levelling and berms", status: "Field-tested on the Chariot rover at Moses Lake in 2008, in Earth gravity", trl: 5, src: 15}
  - {name: "ICON Project Olympus (laser melting)", use: "Fused pads, roads and blast shields", status: "$57.2M NASA SBIR Phase III (2022); chosen in NASA's 2022–23 landing-pad material down-select", trl: 4, src: 11}
  - {name: "ESA PAVER (laser standing in for concentrated sunlight)", use: "Paved roads and pads from interlocking tiles", status: "ESA project Jun 2021 – Dec 2022; tiles made in air in the lab", trl: 4, src: 8}
  - {name: "NASA MSFC microwave sintering (MMPACT MSCC)", use: "Fused pads and roads by microwave", status: "Bench and vacuum-chamber tests; not in the 2022–23 landing-pad down-select", trl: 4, src: 10}
  - {name: "Sintered basalt pavers / regolith-polymer pads", use: "Landing pads", status: "Hot-fire tested on the ground by NASA KSC", trl: 4, src: 5}
sources:
  - {title: "NASA NTRS: IPEx TRL 5 design overview (ASCEND 2024)", url: "https://ntrs.nasa.gov/api/citations/20240008162/downloads/ASCEND24_IPEx%20TRL%205%20Design%20Overview.pdf", date: "2024"}
  - {title: "NASA NTRS: ISRU Pilot Excavator design and scaling", url: "https://ntrs.nasa.gov/api/citations/20210025846/downloads/ASCE%20E%26S%202022-%20ISRU%20Pilot%20Excavator%20BD%20scaling.pdf", date: "2022"}
  - {title: "NASA NTRS 20150022134: RASSOR 2.0", url: "https://ntrs.nasa.gov/api/citations/20150022134/downloads/20150022134.pdf", date: "2015"}
  - {title: "ICON: ICON to develop lunar surface construction system with $57.2M NASA award", url: "https://www.iconbuild.com/newsroom/icon-to-develop-lunar-surface-construction-system-with-57-2-million-nasa-award", date: "Nov 2022"}
  - {title: "NASA: NASA tests landing pad materials for future lunar missions", url: "https://www.nasa.gov/centers-and-facilities/kennedy/nasa-tests-landing-pad-materials-for-future-lunar-missions", date: "Oct 2021"}
  - {title: "Metzger et al., NASA NTRS 20120000029: Further analysis on the mystery of the Surveyor III dust deposits", url: "https://ntrs.nasa.gov/api/citations/20120000029/downloads/20120000029.pdf", date: "2012"}
  - {title: "Gaier, NASA/TM-2005-213610: The effects of lunar dust on EVA systems during Apollo", url: "https://ntrs.nasa.gov/citations/20050160460", date: "2005"}
  - {title: "ESA: How to make roads on the Moon (PAVER)", url: "https://www.esa.int/Enabling_Support/Space_Engineering_Technology/How_to_make_roads_on_the_Moon", date: "Oct 2023"}
  - {title: "Ginés-Palomares et al.: Laser melting manufacturing of large elements of lunar regolith simulant for paving on the Moon (Scientific Reports 13)", url: "https://www.nature.com/articles/s41598-023-42008-1.pdf", date: "Oct 2023"}
  - {title: "Effinger, NASA MSFC: Microwave Structure Construction Capability (NTRS 20205010871)", url: "https://ntrs.nasa.gov/api/citations/20205010871/downloads/Moon%20Village-MSCC%202020-12-09.pptx.pdf", date: "Dec 2020"}
  - {title: "NASA NTRS: MMPACT Jamboree poster 2023", url: "https://ntrs.nasa.gov/api/citations/20230008890/downloads/MMPACT%20Jamboree%20Poster%202023%20-%20final.pdf", date: "2023"}
  - {title: "Metzger & Autry: The cost of lunar landing pads with a trade study of construction methods (arXiv 2205.00378)", url: "https://arxiv.org/pdf/2205.00378", date: "May 2022"}
  - {title: "Metzger et al., NASA KSC: ISRU implications for lunar and martian plume effects (arXiv 2104.06248)", url: "https://arxiv.org/pdf/2104.06248", date: "Apr 2021"}
  - {title: "Gelino, NASA KSC: Lunar Innovation Park site plan and bulk regolith feature design (NTRS 20260002816)", url: "https://ntrs.nasa.gov/api/citations/20260002816/downloads/329%20-%20Site%20Plan%20and%20Bulk%20Presentation.pdf", date: "Apr 2026"}
  - {title: "Mueller et al.: Lightweight bulldozer attachment for construction and excavation on the lunar surface (LANCE, NTRS 20130012987)", url: "https://ntrs.nasa.gov/api/citations/20130012987/downloads/20130012987.pdf", date: "2009"}
  - {title: "Just et al.: Effect of inlet geometry on excavation forces for small-scale continuous excavators (Acta Geotechnica 19)", url: "https://link.springer.com/content/pdf/10.1007/s11440-023-01914-4.pdf", date: "2024"}
  - {title: "Boazman et al.: Mapping potential hazards and identifying sampling points within lunar south polar region areas of interest (PSJ)", url: "https://iopscience.iop.org/article/10.3847/PSJ/ad8fb0", date: "2024"}
  - {title: "Boazman et al.: The distribution and accessibility of geologic targets near the lunar south pole and candidate Artemis landing sites (PSJ 3:275)", url: "https://iopscience.iop.org/article/10.3847/PSJ/aca590", date: "Dec 2022"}
  - {title: "Lee et al.: CraterGrader, autonomous robotic terrain manipulation for lunar site preparation (arXiv 2311.01697)", url: "https://ar5iv.labs.arxiv.org/html/2311.01697", date: "2023"}
  - {title: "NASA STRG: ASPECT, autonomous site preparation, excavation, compaction and testing", url: "https://www.nasa.gov/directorates/stmd/space-tech-research-grants/aspect-autonomous-site-preparation-excavation-compaction-and-testing", date: "Apr 2022"}
  - {title: "Brandić Lipińska et al.: PAVER roadmap (IAC 2022)", url: "https://liquifer.com/wp-content/uploads/2022/12/PAVER_IAC22_0109_FINAL.pdf", date: "2022"}
risks:
  - {sev: Critical, title: "Rocket exhaust blasts dust and rock across the site; Apollo 12 landed 155 m from Surveyor III and the probe's surface was pitted by soil particles", fix: "Hardened pads before heavy landers; berms; keep towers and future habitats well away from pads"}
  - {sev: High, title: "No fused-in-place surface has been tested under a real lander engine; the PAVER team warns glass could shatter into sharp fragments under a plume", fix: "Test small pads with small landers first; use interlocking tiles; keep a regolith-polymer pad as fallback; scale up step by step"}
  - {sev: High, title: "Fusing may be much slower than planned: the only measured lab figure (PAVER) is about 15 times the energy per kg that C02.3 assumes (ESTIMATE)", fix: "Measure fusing energy in vacuum early; size the robots and pad schedule on measured rates; fuse only the pad's inner zone and busy road sections"}
  - {sev: High, title: "Fusing needs tens of kilowatts, and Phase 0 has no power milestone yet", fix: "Open: decide whether the fusing robots carry their own power, use concentrated sunlight (ESA PAVER's approach), or wait for a power supply"}
  - {sev: High, title: "Light robots have little traction in lunar gravity, so blades cannot push hard (the ~700 kg Apollo rover's usable traction was calculated at only 239 N)", fix: "Grade in thin passes; prefer drums and scoops for digging; test vibrating blades, which cut forces by up to 50% in tests"}
  - {sev: Medium, title: "Small rocks at the site are not mapped: orbital images show nothing under about 1–4 m", fix: "Use the M01 prospectors' small-rock survey before planning routes; carry rock-picking tools as well as blades"}
  - {sev: Medium, title: "Reheating a cooled fused track cracked it, and multi-layer builds cracked, in PAVER lab tests", fix: "Prefer single-pass fusing and separate tiles; test thermal cycling before relying on layers"}
  - {sev: Medium, title: "Dust damages seals and mechanisms; on Apollo 12 all the environmental and gas sample seals failed", fix: "Dust-tolerant designs, covers, and fused surfaces around work sites"}
---

## Why the site is prepared first

When a lander touches down on bare regolith, its exhaust throws dust and rocks outward at high speed. In 1969 Apollo 12 landed 155 m from the Surveyor III probe<sup class="r">[6](#s6)</sup>. Surveyor's surface was pitted by soil particles that struck at 300 m/s to 2 km/s<sup class="r">[13](#s13)</sup>. In Apollo landing videos, dust blew out only 1–3° above horizontal, at about 1 km/s<sup class="r">[13](#s13)</sup>. Larger engines on heavier landers will throw more material further. So a base needs hard pads and berms before its big landers arrive.

## How it is done

### 1. Clear the rocks

Orbital images show the big boulders. On the de Gerlache rim area GR1, about 1.5 km², researchers mapped 48 boulders and found rim slopes under 6°<sup class="r">[17](#s17)</sup>. But rocks smaller than about 1–4 m cannot be seen from orbit<sup class="r">[18](#s18)</sup>, so the small rocks a blade will meet are not counted. The M01 prospectors survey them first.

- **Push them.** NASA's LANCE blade on the Chariot rover was built for "area clearing of rocks, leveling, dozing, grading, and berm construction"<sup class="r">[15](#s15)</sup>. Small rocks are pushed to the edge of the work area.
- **Pick them up and haul them away.** Larger rocks are lifted by scoop or grapple and carried to a spoil pile (plan design). NASA's ASPECT project pairs a Lunar Outpost rover with a "rock and regolith grader" and lists boulder moving among its tasks<sup class="r">[20](#s20)</sup>.
- **Rake and sieve** where small rocks are dense. ESA's PAVER team says a site must be raked and graded "to remove larger rocks" before paving<sup class="r">[21](#s21)</sup>.

### 2. Grade it flat with a blade

On Earth, LANCE cleared a 25 × 25 m area in about 2.5 hours and built a 1.3 m berm in about 4 hours<sup class="r">[15](#s15)</sup>. On the Moon, light machines have little weight to push with. The ~700 kg Apollo rover's usable traction there was calculated at only 239 N<sup class="r">[16](#s16)</sup>. Vibrating the cutting edge cut forces by up to 50% in tests<sup class="r">[16](#s16)</sup>. So the excavators grade in thin passes and do the heavy digging with drums (plan design). A small Carnegie Mellon grading robot reached 0.11° final grade, against NASA targets of ±1°, in quartz sand on Earth<sup class="r">[19](#s19)</sup>.

### 3. Fuse the surface

Heat turns the top layer of regolith into a hard, glassy or sintered surface that rocket exhaust cannot blow away. Three methods are being developed:

| Method | Who | What has been shown | Source |
|---|---|---|---|
| **Laser melting** | ICON with NASA (Project Olympus) | Chosen in NASA's 2022–23 landing-pad material down-select; the only one of three materials to pass the full test suite | <sup class="r">[11](#s11)</sup> |
| **Concentrated sunlight** | ESA PAVER (BAM lead, Jun 2021 – Dec 2022) | A 12 kW laser stood in for sunlight that a Fresnel lens a couple of metres across would focus. It made interlocking glassy tiles about 22–25 cm across, one ~2 cm layer deep, averaging 94 MPa (56–216 MPa), in air | <sup class="r">[8](#s8)</sup><sup class="r">[9](#s9)</sup> |
| **Microwave sintering** | NASA Marshall (MMPACT) | Goal of "a 2mT microwave paver vehicle" for pads and roads; bench and vacuum-chamber tests. A cost study found microwaves "currently the most favorable method" for a pad's hot inner zone, needing a modelled 21.73 kWh/m² | <sup class="r">[10](#s10)</sup><sup class="r">[12](#s12)</sup> |

**The microwave rover idea is NASA's, not ESA's.** ESA's paving project, PAVER, uses light. One of its two strategies is a mobile setup, carried by a rover or a lander arm, that melts tiles in place<sup class="r">[21](#s21)</sup>. NASA Marshall's microwave team proposed the paver vehicle<sup class="r">[10](#s10)</sup>. Open Moon keeps the method open (plan design): the fusing robot (C02.3) is laser-baseline, with microwave and concentrated sunlight as alternatives.

### 4. Build pads, roads and berms

- **Landing pads (C02.2).** A fused inner zone where the plume is hottest and a compacted outer apron. NASA KSC splits pads this way, with blast barriers around them<sup class="r">[14](#s14)</sup>. NASA has hot-fire tested sintered basalt pavers and regolith-polymer pads on the ground<sup class="r">[5](#s5)</sup>.
- **Roads.** Graded and compacted everywhere, fused on the busiest sections (plan design). PAVER aims at transport routes that are less dusty, but warns its rough glassy surface could hurt wheel grip, which is untested<sup class="r">[9](#s9)</sup>.
- **Berms.** Because rocket spray is low, a berm may block most of it<sup class="r">[13](#s13)</sup>. NASA KSC's 2026 design uses a 2.5 m berm with a 1 m crest and an 8 m standoff from the lander, sized for landers of about 625 kg<sup class="r">[14](#s14)</sup>. Open Moon's heavier landers may need more. The same paper says a scour hole would throw larger debris over berms, so a full solution needs a hard surface too<sup class="r">[13](#s13)</sup>.

## Step-by-step

1. **Plan routes** from the M00 maps and the M01 small-rock and ground-strength data. Pads go on natural ground of 8° or less (DD-011), so grading only removes local bumps.
2. **Land the excavators** on a small lander, on the pad site itself.
3. **Clear rocks and grade** the first pad area and the first roads.
4. **Fuse pad 1 in stages**, then test it with a small lander. Measure ejecta with cameras and witness plates.
5. **Scale up:** a larger pad 2 for medium and heavy landers, plus berms.
6. **Finish roads and stockpiles.** Spare regolith is piled for later berms and shielding.

## Dust is a design requirement

NASA's review of Apollo found that lunar dust abraded, clogged and coated equipment and caused seal failures. On Apollo 12, all the environmental and gas sample seals failed because of dust<sup class="r">[7](#s7)</sup>. Every site-preparation machine has to:

- tolerate dust
- be covered when idle
- work on fused ground wherever possible
