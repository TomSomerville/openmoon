---
id_code: "C05.2"
milestone: M05
order: 2
title: Hardened landing pad
summary: "A prepared, fused-regolith surface with a compacted apron and an ejecta berm, so landers can touch down and lift off without blasting dust and rocks across the base."
trl: 4
spec:
  - {k: "Quantity", v: "2 pads (plan design choice)"}
  - {k: "Pad 1", v: "30 m sintered core, small and medium landers (design choice)"}
  - {k: "Pad 2", v: "50 m sintered core plus compacted apron to 100 m, heavy landers (design choice)"}
  - {k: "Surface thickness", v: "50 mm fused regolith (design choice; NASA study range 25–50 mm)"}
  - {k: "Surface mass", v: "~95 t (pad 1) and ~265 t (pad 2), all local regolith (ESTIMATE)"}
  - {k: "Berm", v: "~2 m high ring around each pad (ESTIMATE)"}
  - {k: "Landing aids", v: "Beacons, lights and reflective markers on the pad edge"}
  - {k: "Inspection", v: "Stereo cameras and witness plates at every landing"}
  - {k: "Material from Earth", v: "Polymer grout for repairs only, under 2 t"}
subcomponents:
  - name: Sub-grade preparation
    desc: "Excavators clear rocks, level the site and compact the loose top layer so the fused surface sits on a firm base."
    parts: ["Rock clearing and survey", "Grading to a level surface", "Compaction passes", "Drainage-free cross-slope check by lidar"]
    tech: "IPEx-class excavators (C05.1); PISCES robotic site grading"
    trl: 4
  - name: Fused surface (sintered or pavers)
    desc: "The core is fused regolith, either laid in place by the C05.3 robot or as interlocking pavers with grouted joints."
    parts: ["In-place laser or microwave fused layers", "Interlocking sintered pavers", "Regolith-polymer grout for joints", "Compacted outer apron"]
    tech: "NASA/Masten hot-fire tests of sintered pavers; ICON laser VMX"
    trl: 4
  - name: Edge and ejecta berm
    desc: "A ring of piled regolith stops low-angle spray that leaves the pad."
    parts: ["Piled regolith berm", "Sintered or bagged berm crest", "Gaps for road access, offset so there is no line of sight to the base"]
    tech: "NASA KSC pad concepts (blast barriers)"
    trl: 3
  - name: Landing markers and lighting
    desc: "Passive and active markers help the lander's navigation system find the pad centre in low sun or darkness."
    parts: ["Radio beacon at pad centre", "LED edge lights on the grid", "High-contrast reflective markers", "Pad survey map shared with lander providers"]
    tech: "Plan design choice; no lunar pad aids have flown"
    trl: 3
  - name: Inspection and repair
    desc: "Cameras and witness plates measure what each landing does; robots fix damage between landings."
    parts: ["Stereo cameras on the berm (SCALPSS-type)", "Witness plates at 100 m, 500 m and 1 km", "Post-landing lidar scan of the surface", "Repair kit: pavers and polymer grout"]
    tech: "SCALPSS (flew on Blue Ghost Mission 1)"
    trl: 5
risks:
  - {sev: Critical, title: "No fused pad has been tested under a full-size lander engine, on Earth or the Moon", fix: "Build pad 1 first and use it only for small landers; measure; scale up step by step before any heavy lander."}
  - {sev: Critical, title: "Heavy landers land with a large error; NASA's Artemis pad requirement was 200 m across", fix: "Work with lander providers to cut the ellipse to about 100 m with beacons and terrain-relative navigation; keep pad 2's apron to 100 m."}
  - {sev: High, title: "Hot-fire tests eroded pavers under the most extreme thermal conditions", fix: "Thicker centre zone; replaceable centre pavers; inspect and repair after every landing."}
  - {sev: High, title: "Lunar regolith compacts less than simulants, so the base may settle and crack the surface", fix: "Use M01 geotechnical data; test compaction on site before sintering; leave expansion joints."}
  - {sev: High, title: "Polymer binder must be shipped from Earth; a 50 m polymer pad needs about 35 t", fix: "Use local fused regolith for the pad; keep polymer for grout and repairs only."}
  - {sev: Medium, title: "Thermal cycling may crack a large fused slab", fix: "Build in pavers or panels with grouted joints rather than one slab."}
  - {sev: Medium, title: "Landing aids on the pad edge can be damaged by the plume", fix: "Mount lights low behind the berm crest; make beacons cheap and replaceable."}
sources:
  - {title: "Gelino et al., NASA KSC: In-situ lunar launch and landing pad construction with regolith-thermoset polymer composites", url: "https://ntrs.nasa.gov/api/citations/20220000334/downloads/In%20situ%20Lunar%20Launch%20and%20Landing%20Pad%20Construction%20with%20Regolith%20and%20Thermoset%20Polymers%20ASCE%20Earth%20and%20Space%202022%20Paper%20SUBMITTED.pdf", date: "2022"}
  - {title: "NASA: NASA tests landing pad materials for future lunar missions", url: "https://www.nasa.gov/centers-and-facilities/kennedy/nasa-tests-landing-pad-materials-for-future-lunar-missions", date: "Oct 2021"}
  - {title: "Gelino et al., NASA KSC: Lunar landing and launch pad construction, concepts and criteria", url: "https://ntrs.nasa.gov/api/citations/20205008550/downloads/Landing%20Launch%20Pads%20Concepts%20v3%20Poster.pdf", date: "2020"}
  - {title: "NASA NTRS 20120000029: Further analysis on the mystery of the Surveyor III dust deposits", url: "https://ntrs.nasa.gov/api/citations/20120000029/downloads/20120000029.pdf", date: "2012"}
  - {title: "NASA: NASA begins Moon mission plume-surface interaction tests", url: "https://www.nasa.gov/missions/artemis/nasa-begins-moon-mission-plume-surface-interaction-tests/", date: "Aug 2026"}
  - {title: "NASA NTRS 20250010922: SCALPSS 1.1 post-landing terrain measurements", url: "https://ntrs.nasa.gov/citations/20250010922", date: "2026"}
  - {title: "PISCES: PISCES completes lunar landing pad bullseye", url: "https://pacificspacecenter.com/2016/01/05/pisces-completes-lunar-landing-pad-bullseye/", date: "Jan 2016"}
  - {title: "Effinger, NASA MSFC: Microwave sintering lunar landing pads and horizontal infrastructure (MMPACT)", url: "https://ntrs.nasa.gov/api/citations/20205010871/downloads/Moon%20Village-MSCC%202020-12-09.pptx.pdf", date: "Dec 2020"}
  - {title: "ICON: Project Olympus, LSIC slides", url: "https://lsic.jhuapl.edu/uploadedDocs/focus-files/2291-ICON%20Olympus%20LSIC%20Slides%2031JAN2024.pdf", date: "Jan 2024"}
  - {title: "Connolly and Carrier, LPSC 2023: Updating lunar subsurface geotechnical properties", url: "https://ntrs.nasa.gov/api/citations/20220018853/downloads/LPSC%202023%20Abstract_Connolly_Carrier_v2.pdf", date: "2023"}
---

## What it does

A rocket plume on bare regolith erodes the surface and throws particles out at high speed. These particles obscure sensors, crater the ground under the lander, and hit nearby equipment<sup class="r">[3](#s3)</sup>. In 1969 Apollo 12 landed 155 m from Surveyor III. A NASA analysis found that small dust particles could reach Surveyor at up to 130 m/s<sup class="r">[4](#s4)</sup>. A pad gives a known, firm surface that makes little ejecta. A barrier around it catches what does escape<sup class="r">[3](#s3)</sup>.

## How it works

NASA KSC splits a pad into a central zone for normal landings, an outer perimeter for off-target landings and dust control, and blast barriers<sup class="r">[3](#s3)</sup>. Open Moon follows that layout.

**Sub-grade.** Lunar regolith is loose at the top. Its bulk density is about 1.30 g/cm³ at the surface, rising to 1.92 g/cm³ below 1 m<sup class="r">[10](#s10)</sup>. It also compacts less than simulants on Earth<sup class="r">[8](#s8)</sup>. So C05.1 excavators clear rocks, level the site and compact it before any fusing. In 2015 the PISCES team in Hawaii, working with NASA Swamp Works, used a rover to grade a site and lay 100 basalt pavers<sup class="r">[7](#s7)</sup>.

**Fused surface.** NASA and Masten hot-fire tested sintered basalt pavers, carbon fibre blankets and regolith-polymer pavers<sup class="r">[2](#s2)</sup>. They used a 444 N methane-oxygen engine. Erosion was heavy under the most extreme thermal case, but every test article stopped regolith ejecta<sup class="r">[1](#s1)</sup>. One test had nine sintered pavers with polymer grout in the joints<sup class="r">[1](#s1)</sup>. ICON's laser-fused regolith reached about 50,000 psi compressive strength. Its density is 2.7 g/cm³<sup class="r">[9](#s9)</sup>. Open Moon fuses the core with the C05.3 robot. It lays pavers where joints are needed.

**Berm.** A ring of piled regolith around each pad blocks low-angle spray. Road gaps are offset, so no straight path leads from the pad centre to the base.

**Markers and lighting.** Pad size depends on how accurately landers land. Landing aids and terrain-relative navigation shrink the landing ellipse and the pad<sup class="r">[1](#s1)</sup>. Open Moon puts a radio beacon at the centre and lights and reflectors on the edge. This is a design choice; no pad aids have flown.

**Inspection.** NASA's SCALPSS stereo cameras imaged a real landing on Blue Ghost Mission 1 in 2025<sup class="r">[6](#s6)</sup>. NASA is now using them in vacuum-chamber plume tests to measure craters, the ejecta sheet angle and particle speeds<sup class="r">[5](#s5)</sup>. Open Moon puts the same kind of cameras on each berm.

## Sizing

| Item | Pad 1 | Pad 2 | Basis |
|---|---|---|---|
| Fused core diameter | 30 m | 50 m | Design choice |
| Core area | 707 m² | 1,963 m² | π × r² |
| Thickness | 50 mm | 50 mm | Design choice, within NASA's 25–50 mm study range<sup class="r">[1](#s1)</sup> |
| Fused volume | 35 m³ | 98 m³ | area × 0.05 |
| Fused mass | ~95 t | ~265 t | × 2.7 t/m³<sup class="r">[9](#s9)</sup> |
| Polymer for same pad | — | ~35 t | NASA table, 50 m at 50 mm<sup class="r">[1](#s1)</sup> |

NASA's Artemis pad requirement was 200 m across. NASA's landing experts were working to cut it to 100 m<sup class="r">[1](#s1)</sup>. Pad 2's compacted apron reaches 100 m for that reason. A polymer-only pad would need far more than the ~2 t of binder in the M05 budget. So polymer is kept for grout and repairs.

## Testing and qualification

1. **Coupon hot-fire tests** of fused samples and grouted pavers, as in the NASA/Masten campaigns<sup class="r">[1](#s1)</sup>.
2. **Vacuum plume tests** on a fused test bin at NASA Langley-type facilities<sup class="r">[5](#s5)</sup>.
3. **Full-size paver section** on Earth, built by the same robots, then thermal-cycled.
4. **Pad 1 on the Moon:** a small lander lands on it. Cameras and witness plates measure ejecta. Lidar scans for damage.
5. **Pad 2** is cleared for heavy landers only after pad 1 data match the models.

## Open questions

- What plume pressure and temperature will heavy landers put on the pad, and at what height?
- Is a continuous fused slab or a paver field better under thermal cycling?
- Which landing aids will lander providers actually use?
- How far must the berm sit from the pad edge to catch most spray?
