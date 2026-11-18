---
id_code: M00
order: 0
title: Site selection
phase: 0
content_first: true
window: "Before Year 0"
summary: The primary and backup base sites, chosen from lunar orbiter data before Year 0.
objective: "Choose a primary and a backup site near the lunar south pole that give the most sunlight, an access route to permanently shadowed ice, safe terrain for landing and building, and workable communications with Earth."
trl_min: 9
depends_on: []
spec:
  - {k: Team, v: "Engineering and science team"}
  - {k: Hardware, v: "None flown; uses existing orbital data"}
  - {k: Output, v: "Primary and backup sites (DD-015), open maps and analysis code"}
cost: {low: 0.045, high: 0.13, note: "people and computing only; no flight hardware"}
cost_items:
  - {item: "Core engineering team, 2 years", low: 0.04, high: 0.11, basis: "ESTIMATE: 60–150 full-time staff at ~$350k loaded cost per year"}
  - {item: "Computing, data processing, illumination modelling", low: 0.005, high: 0.02, basis: "ESTIMATE"}
exit_criteria:
  - "Primary and backup sites chosen, each with sunlit ground for solar towers and a shadowed crater that may hold ice (done, DD-015)."
  - "Every landing point on ground of 8° or less (done for both sites from LOLA slope; pads confirmed in M05)."
  - "Solar tower layout and its sunlight modelled over an 18.6-year cycle for each site (done, ESTIMATE)."
  - "Hydrogen and ice-candidate maps published, with prospecting targets handed to M01 (done)."
  - "Open checks handed on: boulder and fault-scarp hazard maps per pad (M05), Earth-visibility hours (M03)."
technologies:
  - {name: "Lunar Reconnaissance Orbiter (LRO)", use: "Terrain, imagery, temperature and radar data for site selection", status: "Operating; FY2026 budget request continues operations to support CLPS deliveries, landing-site characterisation and Artemis", trl: 9, src: 1}
  - {name: "ShadowCam on KPLO/Danuri", use: "Images inside permanently shadowed craters", status: "Operating in extended mission; expected to end in early 2028 when its battery runs out in a lunar eclipse", trl: 9, src: 2}
  - {name: "NASA Artemis south-pole candidate regions", use: "Starting shortlist of pre-screened regions", status: "9 regions published Oct 2024 (for Artemis III)", trl: 9, src: 3}
  - {name: "LRO LOLA slope and shadow maps (NASA GSFC)", use: "Slope classes and permanently shadowed region outlines for the focus area", status: "10 m/px south-pole products published 2023 (Barker et al.)", trl: 9, src: 10}
  - {name: "LRO LEND neutron detector", use: "Hydrogen in the top ~1 m", status: "South-polar averaged data 2009–2016 in NASA PDS; ~15 km cells", trl: 9, src: 13}
  - {name: "Chandrayaan-1 Moon Mineralogy Mapper (M3)", use: "Surface water-ice detections", status: "Ice spectra published 2018, clustered near Shackleton; one example in de Gerlache", trl: 9, src: 16}
sources:
  - {title: "NASA FY2026 Budget Technical Supplement (Lunar Reconnaissance Orbiter, PS-28/29)", url: "https://www.nasa.gov/wp-content/uploads/2025/05/fy-2026-budget-technical-supplement-002.pdf", date: "May 2025"}
  - {title: "Univ. of Hawaii SOEST: Scarce ice in Moon's darkest regions (ShadowCam)", url: "https://www.soest.hawaii.edu/soestwp/announce/news/scarce-ice-in-moons-darkest-regions/", date: "Mar 2026"}
  - {title: "NASA NTRS 20250011660: Artemis III Site Selection Update", url: "https://ntrs.nasa.gov/citations/20250011660", date: "Mar 2026"}
  - {title: "Peak of eternal light (Bussey et al. 2010; Speyerer & Robinson 2013 figures), Wikipedia", url: "https://en.wikipedia.org/wiki/Peak_of_eternal_light", date: "accessed Nov 2026"}
  - {title: "LROC: Islands in the Dark (Shackleton rim illumination)", url: "https://www.lroc.asu.edu/images/1105", date: ""}
  - {title: "NASA ACR22 white paper: Why the Lunar South Polar Region", url: "https://www.nasa.gov/wp-content/uploads/2023/10/acr22-wp-why-lunar-south-polar-region.pdf", date: "Oct 2023"}
  - {title: "NASA: Shrinking Moon causing moonquakes and faults near lunar south pole", url: "https://www.nasa.gov/solar-system/moon/shrinking-moon-causing-moonquakes-and-faults-near-lunar-south-pole/", date: "Jan 2024"}
  - {title: "NASA: NASA Provides Update on Artemis III Moon Landing Regions (map of nine regions, credit NASA/GSFC/ASU/JSC/AGDT)", url: "https://www.nasa.gov/news-release/nasa-provides-update-on-artemis-iii-moon-landing-regions/", date: "Oct 2024"}
  - {title: "NASA: NASA Identifies Candidate Regions for Landing Next Americans on Moon (original 13 regions)", url: "https://www.nasa.gov/news-release/nasa-identifies-candidate-regions-for-landing-next-americans-on-moon/", date: "Aug 2022"}
  - {title: "NASA GSFC PGDA: A New View of the Lunar South Pole from LOLA (LDSM slope and hillshade maps, 10 m/px; Barker et al. 2023, Planet. Sci. J. 4, 183, doi:10.3847/PSJ/acf3e1)", url: "https://pgda.gsfc.nasa.gov/products/90", date: "2023"}
  - {title: "LROC (NASA/GSFC/Arizona State University): Shackleton–de Gerlache Ridge maps, sheets 1–3", url: "https://lroc.im-ldi.com/data/support/popular_downloads/LROC_Shackleton_deGerlache_Ridge_maps.zip", date: "Mar 2024"}
  - {title: "NASA Science: Hydrogen at the Lunar Poles: How Much Water Is There? (summary of Sanin et al. 2017, Icarus 283)", url: "https://science.nasa.gov/wp-content/uploads/2023/05/NuggetHydrogenAtTheLunarPoles20170210.pdf", date: "Feb 2017"}
  - {title: "NASA PDS Geosciences Node: LRO LEND data (averaged south-polar products ALDS, 2009–2016)", url: "https://pds-geosciences.wustl.edu/missions/lro/lend.htm", date: "accessed Nov 2026"}
  - {title: "Feldman et al. 2000, Polar hydrogen deposits on the Moon (J. Geophys. Res.)", url: "https://earthref.org/ERR/61400/", date: "2000"}
  - {title: "NASA Ames Astrogram, Aug 2018: Ice confirmed at the Moon's poles (M3 surface-ice map, Li et al. 2018)", url: "https://www.nasa.gov/centers-and-facilities/ames/nasa-ames-astrogram-august-2018/", date: "Aug 2018"}
  - {title: "Li et al. 2018, Direct evidence of surface exposed water ice in the lunar polar regions (PNAS)", url: "https://europepmc.org/article/PMC/PMC6130389", date: "Aug 2018"}
  - {title: "Li et al. 2026, Searching for surficial water ice in lunar permanently shaded regions (PSRs) with ShadowCam (Science Advances)", url: "https://europepmc.org/article/PMC/PMC12998505", date: "Mar 2026"}
  - {title: "NASA NTRS: Vertical Solar Array Technology annual review (key performance parameters)", url: "https://ntrs.nasa.gov/api/citations/20230012849/downloads/GCD%20Annual%20Review%20VSAT%20September%202023%20Final.pdf", date: "Sep 2023"}
  - {title: "NASA GSFC PGDA: Lunar Polar Illumination (average solar illumination maps; Mazarico et al. 2011, Icarus 211)", url: "https://pgda.gsfc.nasa.gov/products/69", date: "accessed Nov 2026"}
  - {title: "LROC (NASA/GSFC/Arizona State University): NAC south polar maximum-pixel and sub-solar-longitude mosaics, 1 m/px, tile P878S2925, with PDS labels (NASA PDS)", url: "https://pds.mcp.nasa.gov/data/store/img/lunar_reconnaissance_orbiter/pds4/lroc/lro-l-lroc-5-rdr/LROLRC_2001/EXTRAS/BROWSE/NAC_POLE/NAC_POLE_SOUTH_CM_MAX/NAC_POLE_SOUTH_CM_MAX_P878S2925.xml", date: "accessed Nov 2026"}
  - {title: "JPL IPN Progress Report 42-176: Lunar pole illumination and communications maps (Bryant)", url: "https://ipnpr.jpl.nasa.gov/progress_report/42-176/176C.html", date: "Feb 2009"}
risks:
  - {sev: High, title: "Ice at both sites is unconfirmed: Shackleton's evidence is mixed and de Gerlache has only two candidate detections", fix: "M01 prospectors measure ice at both crater floors before the base is committed; switch to the backup if the primary fails"}
  - {sev: High, title: "A young fault scarp is mapped in de Gerlache Rim 2, next to the primary site", fix: "Map scarps from LROC NAC images; keep pads, the reactor and habitats clear of young faults (M05)"}
  - {sev: High, title: "ShadowCam's mission is expected to end in early 2028, cutting off new images inside shadowed craters", fix: "Archive all ShadowCam images of the de Gerlache and Shackleton floors; plan our own prospecting in M01"}
  - {sev: Medium, title: "Even at the best base site studied by JPL, Earth is in direct view only about half the time (source 21)", fix: "Treat relay satellites as mandatory (M03)"}
  - {sev: Medium, title: "No lander publishes a certified slope limit above 10°, and IM-1 tipped over on 12° ground", fix: "Land only on ground of 8° or less; confirm each pad with ~1 m LROC NAC hazard maps (M05)"}
---
## The chosen sites

![Both chosen base sites with their final solar tower layouts, over slope classes, ice candidates and hydrogen]({{ '/assets/sites/site-selection-overview.jpg' | relative_url }})

*Both base sites with their final power layouts. Slope in four classes, ice-candidate crater floors in blue, hydrogen in purple. Sunlit percentages are from NASA's illumination map. Click any image to see it full size.*

- **Primary:** de Gerlache north rim, 88.445°S, 63.44°W.
- **Backup:** Connecting ridge by Shackleton, 89.559°S, 163.66°W, 51.2 km away.

Both are chosen from orbital data and are to be confirmed on the ground by the M01 prospectors (DD-015).

## Criteria considered

<div class="tabs" id="m00tabs">
<input type="radio" name="m00tab" id="m00t1" checked><label for="m00t1">South pole</label>
<input type="radio" name="m00tab" id="m00t2"><label for="m00t2">Focus area</label>
<input type="radio" name="m00tab" id="m00t3"><label for="m00t3">Slope</label>
<input type="radio" name="m00tab" id="m00t4"><label for="m00t4">Sunlight</label>
<input type="radio" name="m00tab" id="m00t5"><label for="m00t5">Hydrogen</label>
<input type="radio" name="m00tab" id="m00t6"><label for="m00t6">Ice</label>
<input type="radio" name="m00tab" id="m00t7"><label for="m00t7">Power layout</label>
<div class="tabpanels" markdown="1">
<div class="tabpanel" id="m00p1" markdown="1">

### Why the south pole

Near the south pole some ridges are sunlit most of the time, while nearby craters stay permanently in shadow and cold enough to trap water ice<sup class="r">[6](#s6)</sup>. Near-constant solar power next to frozen water is what makes a self-sustaining base possible.

No point is sunlit all the time<sup class="r">[5](#s5)</sup>, but the best come close:

| Location | Sunlit | Source |
|---|---|---|
| de Gerlache ridge | ~85% | Bussey et al. 2010, via<sup class="r">[4](#s4)</sup> |
| Peaks near Shackleton | ~82% and ~86% | same |
| Two Shackleton-ridge points ~8 km apart, combined | ~94% | same |

So solar towers are spread over several high points, so that one is usually lit. Each tower is within 3 km of cable of the base as standard, or 10 km at most (DD-013, DD-014).

</div>
<div class="tabpanel" id="m00p2" markdown="1">

### Focus area: Shackleton – de Gerlache

NASA's nine candidate Artemis regions (October 2024) were the starting shortlist<sup class="r">[8](#s8)</sup>. The search then narrowed to about 180 × 130 km around the Shackleton–de Gerlache Ridge (DD-010), which holds:

- **de Gerlache Rim 2**, one of NASA's nine regions. The primary site is inside it.
- **The Connecting Ridge**, with the sunniest ground studied. It was on NASA's 2022 list of 13 regions but not the 2024 nine, and NASA has not said why<sup class="r">[9](#s9)</sup><sup class="r">[8](#s8)</sup>.
- **The shadowed floors of Shackleton and de Gerlache**, the ice candidates.

![NASA's nine candidate landing regions near the lunar south pole, with the Open Moon focus area outlined in red]({{ '/assets/sites/south-pole-candidate-regions.jpg' | relative_url }})
![LROC Shackleton–de Gerlache Ridge, sheet 1: multi-lighting mosaic]({{ '/assets/sites/lroc-ridge-sheet1-controlled-mosaic.jpg' | relative_url }})

*Left: NASA's nine regions (yellow), credit NASA/GSFC/ASU/JSC/AGDT<sup class="r">[8](#s8)</sup>, with Open Moon's focus area in red. Right: LROC's ridge map, credit NASA/GSFC/Arizona State University<sup class="r">[11](#s11)</sup>.*

</div>
<div class="tabpanel" id="m00p3" markdown="1">

### Slope and landing

Slope is from NASA Goddard's LOLA slope map at 10 m per pixel<sup class="r">[10](#s10)</sup>. Landers land only on ground of **8° or less**, NASA's tilt limit for crewed landers (DD-011). No lander publishes a certified limit above 10° ([Lander candidates]({{ '/landers/' | relative_url }})).

| Colour | Slope | Meaning |
|---|---|---|
| Green | ≤8° | Landable |
| Yellow | 8–15° | Above published lander limits; rovers and towers only |
| Orange | 15–20° | Above every lander limit |
| Red | ≥20° | Crater walls and scarps |

43% of the focus area is 8° or less. At the sites, 65% (primary) and 69% (backup) of the ground within 1 km is landable.

![Slope classes across the Open Moon focus area]({{ '/assets/sites/focus-slope-classes.jpg' | relative_url }})
![Slope classes across NASA's de Gerlache Rim 2 region]({{ '/assets/sites/de-gerlache-rim2-slope-classes.jpg' | relative_url }})

*Left: the focus area. Right: de Gerlache Rim 2 at 10 m per pixel. Boulders are too small to show at this scale, so pads still need ~1 m hazard maps (M05).*

</div>
<div class="tabpanel" id="m00p4" markdown="1">

### Sunlight and solar towers

NASA's VSAT solar towers are 10 kW each, on masts of 5 m (threshold) to 10 m (goal), and can stand on slopes up to 15° with a 10 m mast<sup class="r">[18](#s18)</sup>. Tower spots were picked from NASA Goddard's average sunlight map over a full 18.6-year cycle<sup class="r">[19](#s19)</sup>. Combined uptime comes from Open Moon's own shadow model (ESTIMATE).

| Best layout | Towers | At least one lit | Longest dark | Longest cable |
|---|---|---|---|---|
| Connecting ridge (backup) | 3 | 93.0% | 4.8 days | ~2 km |
| de Gerlache north rim (primary) | 2 | 84.1% | 6.2 days | 8.8 km |

![Solar tower spots in the focus area: orange at least 80% sunlit, yellow 70–80%]({{ '/assets/sites/focus-vsat-candidates.jpg' | relative_url }})
![Animation of sunlight and shadow over the focus area during one lunar day]({{ '/assets/sites/focus-sunlight-winter-2027.gif' | relative_url }})

*Left: tower spots sunlit at least 80% (orange) and 70–80% (yellow) at ground level, from NASA's map. Right: one lunar day of light and shadow in the darkest season (ESTIMATE).*

</div>
<div class="tabpanel" id="m00p5" markdown="1">

### Hydrogen

Orbiters map hydrogen in the top metre by counting escaping neutrons; hydrogen slows them, so fewer escape. A dip shows hydrogen, but not whether it is ice<sup class="r">[14](#s14)</sup>. NASA's LEND team found the enhancements "near and in areas of permanent shadow"<sup class="r">[12](#s12)</sup>. Open Moon mapped the neutron dip from NASA's LEND data<sup class="r">[13](#s13)</sup>. The strongest hydrogen in the focus area lies away from the craters: 19.9 km from the primary and 28.9 km from the backup.

![NASA LEND map of water-equivalent hydrogen around the lunar south pole]({{ '/assets/sites/nasa-lend-weh-south-pole.jpg' | relative_url }})
![Hydrogen from NASA LEND data around the south pole, with the Open Moon focus area outlined]({{ '/assets/sites/south-pole-lend-hydrogen.jpg' | relative_url }})

*Left: NASA's map, from Sanin et al. 2017<sup class="r">[12](#s12)</sup>. Right: Open Moon processing of the same data.*

</div>
<div class="tabpanel" id="m00p6" markdown="1">

### Ice candidates

None is confirmed. The ice candidates are the permanently shadowed floors of Shackleton (233 km²) and de Gerlache (242 km²)<sup class="r">[10](#s10)</sup>:

- **Shackleton:** a bright floor in LOLA data and nearby M3 ice spectra<sup class="r">[16](#s16)</sup>, but Kaguya and ShadowCam found no exposed ice.
- **de Gerlache:** one M3 ice spectrum and an unexplained bright spot seen by ShadowCam<sup class="r">[17](#s17)</sup>.

![NASA map of surface water ice detected by the Moon Mineralogy Mapper at the lunar poles]({{ '/assets/sites/nasa-m3-polar-ice-2018.jpg' | relative_url }})
![Ice candidates in the focus area: shadowed floors of Shackleton and de Gerlache, ShadowCam bright spot]({{ '/assets/sites/focus-ice-candidates.jpg' | relative_url }})

*Left: surface ice detected by NASA's Moon Mineralogy Mapper, south pole on the left<sup class="r">[15](#s15)</sup>. Right: ice candidates in the focus area.*

</div>
<div class="tabpanel" id="m00p7" markdown="1">

### Power layout at the primary site

The ice floor is 12.7 km from the primary base, beyond the 10 km cable limit, so the base and the mine run **separate grids** (DD-016). The figures below are from Open Moon's shadow model (ESTIMATE).

| Grid | Towers | At least one lit | Longest dark |
|---|---|---|---|
| Base | B1 (7.7 km) and B2 (8.8 km), plus B3 (0.8 km) | 84.1% (84.3% with B3) | 6.2 days |
| Ice mine | M1 and M2 on the rim, 2.3 km apart, with an 8.3 km feeder | 77.4% | 14.2 days |

- **B3** is for redundancy and faster battery charging, not extra hours of sun (DD-017).
- **The mine shuts down in the dark.** Its battery only keeps heaters, controls and comms alive.
- **Towers within 3 km of the base were rejected.** Up to five of them reach only 56.9%, because nearby high ground blocks the low Sun.

</div>
</div>
</div>
<script>
(function(){function open(){var h=location.hash.slice(1);if(!h)return;var el=document.getElementById(h);if(!el)return;var p=el.closest('.tabpanel');if(!p)return;var n=p.id.replace('m00p','');var r=document.getElementById('m00t'+n);if(r){r.checked=true;el.scrollIntoView();}}
window.addEventListener('hashchange',open);open();})();
</script>

## The two sites

| | **Primary: de Gerlache north rim** | **Backup: Connecting ridge** |
|---|---|---|
| Position | 88.445°S, 63.44°W | 89.559°S, 163.66°W |
| Slope at site; landable within 1 km | 5.0°; 65% | 5.8°; 69% |
| Solar towers (ESTIMATE) | 84.1% lit, longest dark 6.2 days | 93.0% lit, longest dark 4.8 days |
| Nearest ice-candidate floor | 12.7 km (de Gerlache) | 5.2 km (Shackleton) |
| Nearest high hydrogen | 19.9 km | 28.9 km |
| On NASA's 2024 list | Yes (de Gerlache Rim 2) | No (2022 list only) |

*Distances are straight lines.*

### Primary: de Gerlache north rim

**Pros**

- Inside NASA's de Gerlache Rim 2, a region NASA screened for landing safety, light and Earth visibility<sup class="r">[3](#s3)</sup>.
- Flat ground: 5.0° at the site, with a 1° spot for B3 0.8 km away.
- The most hydrogen of the two sites, and an ice target with two independent hints.

**Cons**

- Less sun: 84.1% with blackouts of up to 6.2 days, and the base towers need 7.7–8.8 km cables.
- The ice floor is 12.7 km away, so the mine needs its own grid and stops for up to about 14 days at a time.
- The cables to the mine cross a crater wall that is mostly steeper than 20°.
- A young fault scarp is mapped in Rim 2<sup class="r">[7](#s7)</sup>.

![Primary base site: slope classes, de Gerlache shadowed floor, hydrogen, base and ice-mine grids]({{ '/assets/sites/primary-base-site.jpg' | relative_url }})
![LROC NAC maximum-pixel mosaic of the primary base site, 4 by 4 km]({{ '/assets/sites/primary-base-nac-max-4km.jpg' | relative_url }})

*Left: the primary site and both of its grids. Right: the base at 1 m per pixel, from LROC's maximum-pixel mosaic, which shows each spot at its brightest so that most shadows are gone (credit NASA/GSFC/Arizona State University)<sup class="r">[20](#s20)</sup>.*

### Backup: Connecting ridge by Shackleton

**Pros**

- The best sun in the focus area: 93.0% with three towers, on short cables.
- Shackleton's ice floor is 5.2 km away, close enough for a mine on the base grid.
- Flat ground: 5.8° at the site.

**Cons**

- Not on NASA's 2024 list.
- Less hydrogen.
- Shackleton's ice evidence is mixed.
- China's Chang'e-7 targets the Shackleton area.
- No detailed layout yet.

## Status

Site selection is complete. Year 0 is the first landers: prospectors go to both sites to confirm ice (M01), and site preparation begins (M05).

*Open Moon is a plan for how we, as people, could build a self-sustaining Moon colony. It is hypothetical: a proposal, not a programme or organisation.*

Design decisions behind this page:

<ul class="ddlist">{% assign ids = "DD-010,DD-011,DD-012,DD-013,DD-014,DD-015,DD-016,DD-017,DD-018,DD-019" | split: "," %}{% for i in ids %}{% assign d = site.data.decisions | where: "id", i | first %}<li><a href="{{ '/decisions/' | relative_url }}#{{ i | downcase }}">{{ i }}</a> {{ d.title }}</li>{% endfor %}</ul>

Analysis code and data notes are in `analysis/` in the repository.
