---
title: Lander candidates
eyebrow: Which landers can reach our site
summary: How steep a slope each lunar lander can land on and how much it can carry to the surface, compared with the terrain in the Open Moon focus area. Every figure links to its source; nothing here is estimated.
section: tech
doc_id: OM-310
permalink: /landers/
---

## Landing slope and payload

Researched November 2026, one lander at a time. The full notes and every source are in the [lander research files]({{ site.repo }}/tree/main/research/landers).

<div class="tablewrap" markdown="1">

| Lander | Max landing slope (published) | Max payload to surface | Landing record | Status (Nov 2026) |
|---|---|---|---|---|
| JAXA SLIM | No certified limit. Target site "approximately 15°"<sup class="r">[1](#s1)</sup>; JAXA's magazine says 6–7° average<sup class="r">[2](#s2)</sup> | Not published (technology demo; ~2.3 kg of rovers flown)<sup class="r">[3](#s3)</sup> | Landed 20 Jan 2024, ended upside down after an engine nozzle came off at ~50 m<sup class="r">[4](#s4)</sup> | Ended Aug 2024 |
| ispace Hakuto-R M1 | Not published | 30 kg (design)<sup class="r">[5](#s5)</sup> | Crashed 25 Apr 2023 (altitude software error)<sup class="r">[6](#s6)</sup> | Destroyed |
| Astrobotic Peregrine | No lander limit. Site rule ≤10°<sup class="r">[7](#s7)</sup> | 90 kg mid-latitude, 100 kg polar<sup class="r">[7](#s7)</sup> | Propulsion leak; never landed, re-entered Earth 18 Jan 2024<sup class="r">[8](#s8)</sup> | Retired |
| Intuitive Machines IM-1 (Nova-C) | **10°** design<sup class="r">[9](#s9)</sup> | >130 kg design; ~100 kg flown<sup class="r">[9](#s9)</sup> | Landed 22 Feb 2024 on **12°** terrain and too fast; a leg broke and it tipped<sup class="r">[10](#s10)</sup> | Inactive |
| Firefly Blue Ghost M1 | No lander limit. Site rule ≤10°; actual site under ~5°<sup class="r">[11](#s11)</sup> | Up to 240 kg (Firefly)<sup class="r">[12](#s12)</sup>; ~94 kg flown | **Success**, 2 Mar 2025, upright<sup class="r">[13](#s13)</sup> | Mission complete |
| Intuitive Machines IM-2 (Nova-C) | **10°** design<sup class="r">[9](#s9)</sup> | >130 kg (IM); 100–130 kg (NASA)<sup class="r">[14](#s14)</sup> | Landed 6 Mar 2025 in a 20 m crater, on its side<sup class="r">[15](#s15)</sup> | Ended; IM-3 targets Mar–Apr 2027 |
| ispace Resilience | Not published | 30 kg (design)<sup class="r">[16](#s16)</sup> | Crashed 5 Jun 2025 (laser range finder fault)<sup class="r">[17](#s17)</sup> | Destroyed; successor ULTRA 2028 |
| Astrobotic Griffin | No formal limit. "Can easily tolerate a 10-degree slope"<sup class="r">[18](#s18)</sup> | **625 kg** design<sup class="r">[19](#s19)</sup>; Griffin-1 carries 455 kg<sup class="r">[20](#s20)</sup> | Not flown | Launch Jan 2027 to Nobile crater<sup class="r">[18](#s18)</sup> |
| Blue Origin Blue Moon Mk1 / Mk2 | Not published. NASA crew rules: site <10°, tilt ≤8°<sup class="r">[21](#s21),[22](#s22)</sup> | Mk1 **3 t**<sup class="r">[23](#s23)</sup>; Mk2 cargo ~15 t (NASA)<sup class="r">[24](#s24)</sup> to 30 t (Blue Origin) | Not flown | Mk1 NET Q1 2027; Mk2 2028–29 |
| SpaceX Starship HLS | Not published. NASA crew rules: site <10° over 100 m, tilt ≤8°<sup class="r">[21](#s21),[22](#s22)</sup> | Cargo **15 t** (NASA interface spec)<sup class="r">[25](#s25)</sup>; SpaceX claims 100 t | No lunar attempt | Uncrewed landing ~Q1 2028<sup class="r">[24](#s24)</sup> |

</div>

## What the table tells us

- **No lander publishes a certified slope above 10°.** The only design figures are Nova-C's 10° and Griffin's "easily tolerate 10°". Landing-site rules from Astrobotic, Firefly's science team and NASA's crewed landers are all 10° or less.
- **The one landing on steeper ground failed.** IM-1 came down on 12° terrain (also too fast) and tipped over.
- **Crewed landers have a stricter rule:** NASA requires them to end up tilted no more than 8° from vertical.
- **Only one commercial lander has landed fully successfully:** Firefly's Blue Ghost, on flat mare ground under about 5°.
- **For a scout rover, Griffin is the nearest option** (625 kg, aimed at the south pole) but it has not flown.

## Slope classes used on Open Moon maps

| Colour | Slope | Meaning |
|---|---|---|
| Green | ≤8° | Within NASA's crewed-lander tilt limit |
| Yellow | 8–15° | Up to and just past published robotic lander limits (10°) |
| Orange | 15–20° | Above every published lander limit |
| Red | ≥20° | Crater walls and steep scarps |

## The focus area against these limits

| Area | ≤8° | 8–15° | 15–20° | ≥20° | Resolution |
|---|---|---|---|---|---|
| Focus area (~180 × 130 km around the pole) | 43% | 35% | 14% | 8% | 40 m/px |
| NASA's de Gerlache Rim 2 (box as drawn, ~20 × 20 km) | 22% | 42% | 25% | 12% | 10 m/px |

*Computed by Open Moon from NASA Goddard's LOLA slope map (Barker et al. 2023)<sup class="r">[26](#s26)</sup>. Slopes at 10–40 m per pixel do not show boulders or small craters; final landing pads need ~1 m imagery. See [M00 site selection]({{ '/plan/m00-site-selection/' | relative_url }}) for how the maps were made.*

![Slope classes across the Open Moon focus area: green ≤8°, yellow 8–15°, orange 15–20°, red ≥20°]({{ '/assets/sites/focus-slope-classes.jpg' | relative_url }})

![Slope classes across NASA's de Gerlache Rim 2 candidate region at 10 m per pixel]({{ '/assets/sites/de-gerlache-rim2-slope-classes.jpg' | relative_url }})

## Sources

<ol>
<li id="s1"><a href="https://global.jaxa.jp/countdown/slim/SLIM-mediakit-EN_2308.pdf">JAXA: SLIM media kit</a> (Aug 2023)</li>
<li id="s2"><a href="https://cosmos.isas.jaxa.jp/?p=7409">JAXA ISAS: "20 minutes of terror"</a></li>
<li id="s3"><a href="https://www.isas.jaxa.jp/en/topics/files/SLIM-press-briefing-20241226.pdf">JAXA: SLIM press briefing</a> (Dec 2024)</li>
<li id="s4"><a href="https://global.jaxa.jp/press/2024/01/file/jaxa_doc01_20240125_e.pdf">JAXA: SLIM landing briefing</a> (Jan 2024)</li>
<li id="s5"><a href="https://www.ispace-inc.com/2020/07/30/commercial-lunar-exploration-program-hakuto-r-reveals-final-design-and-plan-for-mission-1-lunar-lander/">ispace: HAKUTO-R Mission 1 final design</a> (Jul 2020)</li>
<li id="s6"><a href="https://www.ispace-inc.com/2023/05/26/ispace-announces-results-of-the-hakuto-r-mission-1-lunar-landing/">ispace: Mission 1 landing results</a> (May 2023)</li>
<li id="s7"><a href="https://www.astrobotic.com/wp-content/uploads/2022/01/PUGLanders_011222.pdf">Astrobotic: Lunar Landers Payload User's Guide v5.0</a> (2021)</li>
<li id="s8"><a href="https://astrobotic.com/wp-content/uploads/2024/08/PM1_Post-Mission-Report_2024-1.pdf">Astrobotic: Peregrine Mission One post-mission report</a> (Aug 2024)</li>
<li id="s9"><a href="https://www.hou.usra.edu/meetings/lpsc2024/pdf/1931.pdf">Bussey &amp; Martin (Intuitive Machines), LPSC 2024 abstract 1931</a></li>
<li id="s10"><a href="https://www.nasa.gov/missions/lro/nasas-lro-images-intuitive-machines-odysseus-lander/">NASA: LRO images Odysseus lander</a> (Feb 2024)</li>
<li id="s11"><a href="https://www.hou.usra.edu/meetings/lpsc2022/pdf/1390.pdf">Nagihara et al., LPSC 2022 abstract 1390</a></li>
<li id="s12"><a href="https://fireflyspace.com/blue-ghost/">Firefly: Blue Ghost lunar lander</a></li>
<li id="s13"><a href="https://fireflyspace.com/news/firefly-aerospace-becomes-first-commercial-company-to-successfully-land-on-the-moon/">Firefly: first commercial company to successfully land on the Moon</a> (Mar 2025)</li>
<li id="s14"><a href="https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=PRIME-1">NASA NSSDCA: IM-2 / PRIME-1</a></li>
<li id="s15"><a href="https://www.nasa.gov/news-release/nasa-receives-some-data-before-intuitive-machines-ends-lunar-mission/">NASA: data received before IM-2 ended</a> (Mar 2025)</li>
<li id="s16"><a href="https://ispace-inc.com/spacecraft">ispace: spacecraft</a></li>
<li id="s17"><a href="https://www.ispace-inc.com/2025/06/24/ispace-releases-technical-cause-analysis-for-hakuto-r-mission-2/">ispace: Mission 2 technical cause analysis</a> (Jun 2025)</li>
<li id="s18"><a href="https://voyagertechnologies.com/insights/how-voyager-chose-griffins-lunar-landing-site/">Voyager Technologies: how Griffin's landing site was chosen</a> (Oct 2026)</li>
<li id="s19"><a href="https://www.astrobotic.com/lunar-delivery/landers/griffin-lander/">Astrobotic: Griffin lander</a></li>
<li id="s20"><a href="https://www.nasa.gov/missions/moon-base/nasa-jpl-testing-readies-voyager-technologies-lander-for-moon-mission/">NASA: JPL testing readies Griffin</a> (Oct 2026)</li>
<li id="s21"><a href="https://ntrs.nasa.gov/api/citations/20240009596/downloads/ArtemisHLSUpdate_2024.pdf">NASA NTRS: Artemis HLS update 2024</a></li>
<li id="s22"><a href="https://oig.nasa.gov/wp-content/uploads/2026/03/final-report-ig-26-004-nasas-management-of-the-human-landing-system-contracts.pdf">NASA OIG IG-26-004: management of the HLS contracts</a> (Mar 2026)</li>
<li id="s23"><a href="https://en.wikipedia.org/wiki/Blue_Moon_(spacecraft)">Blue Moon (spacecraft), Wikipedia</a> (accessed Nov 2026)</li>
<li id="s24"><a href="https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf">NASA NTRS: HLS IAC 2026 presentation</a></li>
<li id="s25"><a href="https://ntrs.nasa.gov/api/citations/20260007769/downloads/HLS-IRD-010_HDL%20System%20to%20Cargo_Revision_C.pdf">NASA NTRS: HLS-IRD-010 Rev C, lander-to-cargo interface</a> (Apr 2026)</li>
<li id="s26"><a href="https://pgda.gsfc.nasa.gov/products/90">NASA GSFC PGDA: A New View of the Lunar South Pole from LOLA</a> (Barker et al. 2023)</li>
</ol>
