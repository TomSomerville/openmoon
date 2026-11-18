# Intuitive Machines Nova-C (IM-1 "Odysseus", Feb 2024)

## Summary
| Item | Value | Source |
|---|---|---|
| Max landing slope (design) | 10° ("It can land on slopes up to 10°"). Design spec, not demonstrated: IM-1 came down on 12° terrain and tipped over | [Bussey & Martin (Intuitive Machines), 55th LPSC 2024, abstract 1931](https://www.hou.usra.edu/meetings/lpsc2024/pdf/1931.pdf) |
| Max payload to lunar surface | Over 130 kg (design). IM-1 carried about 100 kg (demonstrated) | [LPSC 2024 abstract 1931](https://www.hou.usra.edu/meetings/lpsc2024/pdf/1931.pdf); [IM FY2024 Form 10-K](https://www.sec.gov/Archives/edgar/data/1844452/000184445225000023/lunr-20241231.htm) |
| Landing attempts | 1 for IM-1: 22 Feb 2024, 6:24 p.m. EST, near Malapert A. It landed but tipped over (IM-2 is covered separately) | [NASA LRO, 26 Feb 2024](https://www.nasa.gov/missions/lro/nasas-lro-images-intuitive-machines-odysseus-lander/) |
| Status (Nov 2026) | Inactive on the lunar surface. Powered down on 29 Feb 2024; on 23 Mar 2024 IM said it had "permanently faded" | [Space.com, 25 Mar 2024](https://www.space.com/intuitive-machines-im-1-moon-mission-ends) |

## Landing slope tolerance
- **Design spec: 10°.** Intuitive Machines staff wrote: "Nova-C uses one VR-900 bipropellant engine to deliver over 130 kg of payload to anywhere on the Moon. It can land on slopes up to 10° and uses a hazard detection and avoidance system to ensure a safe landing." ([Bussey & Martin, Intuitive Machines, LPSC 2024 #1931](https://www.hou.usra.edu/meetings/lpsc2024/pdf/1931.pdf)). The abstract does not say whether 10° is a certified value, what margins it includes, or what touchdown velocities it assumes.
- **Wikipedia agrees.** It says "The lander is designed to stay upright when landing on a slope of up to 10 degrees", citing the [New York Times, 4 Mar 2024](https://www.nytimes.com/2024/03/04/science/moon-landing-sideways-gravity.html) ([Wikipedia: Intuitive Machines Nova-C](https://en.wikipedia.org/wiki/Intuitive_Machines_Nova-C)). The NYT article is paywalled, so I did not check its text.
- **Not demonstrated.** On IM-1, the local terrain at the rest site was sloped 12°, which is above the 10° spec. The lander did not stay upright (see Landing record).
- **Not found:** a Nova-C payload user's guide or an official IM spec sheet giving the slope limit. The IM product pages could not be fetched: `intuitivemachines.com/build/nova-c-lunar-lander` and `/lunar-access-services` return a JavaScript app or a redirect loop, and the Wayback Machine connection was reset. The [NASA IM-1 press kit](https://www.nasa.gov/wp-content/uploads/2024/01/np-2023-12-016-jsc-clps-im-press-kit-web-508.pdf) does not give a slope tolerance.

## Payload capacity
| Figure | Type | Source |
|---|---|---|
| "over 130 kg of payload to anywhere on the Moon" | Design (IM authors, Jan–Mar 2024) | [LPSC 2024 #1931](https://www.hou.usra.edu/meetings/lpsc2024/pdf/1931.pdf) |
| "can hold a payload of over 130 kg" (article text) | Wiki | [Wikipedia](https://en.wikipedia.org/wiki/Intuitive_Machines_Nova-C) |
| 100 kg (infobox, citing IM's 2018 lander page via Wayback) | Wiki, older figure | [Wikipedia](https://en.wikipedia.org/wiki/Intuitive_Machines_Nova-C) |
| "approximately 100 kilograms of science experiment and technology demonstration payloads" carried on IM-1 | Demonstrated (IM SEC filing) | [IM Form 10-K for FY2024](https://www.sec.gov/Archives/edgar/data/1844452/000184445225000023/lunr-20241231.htm) |

- **Conflicting figures.** The current design figure is >130 kg. Wikipedia's own infobox still shows 100 kg, taken from a 2018 IM page, so the article contradicts itself. IM's 10-K gives about 100 kg as the mass actually flown on IM-1, not as a capacity.
- **Payload count.** The NASA press kit says IM-1 carried six NASA payloads. SpaceNews describes the NASA task order as six payloads worth $118 million after revisions ([NASA press kit](https://www.nasa.gov/wp-content/uploads/2024/01/np-2023-12-016-jsc-clps-im-press-kit-web-508.pdf); [SpaceNews](https://spacenews.com/intuitive-machines-lands-on-the-moon/)).

## Landing record
- **Date and site.** Odysseus landed on 22 Feb 2024 at 6:24 p.m. EST near Malapert A in the South Pole region. LRO measured the rest position as 80.13° S, 1.44° E, 2,579 m elevation, "within a degraded one-kilometer diameter crater where the local terrain is sloped at 12 degrees" ([NASA LRO](https://www.nasa.gov/missions/lro/nasas-lro-images-intuitive-machines-odysseus-lander/)).
- **Pre-landing anomaly.** The lander's laser rangefinders did not work. IM added an orbit (a 2-hour delay) and uploaded a patch so the lander could use NASA's Navigation Doppler Lidar (NDL) payload instead ([SpaceNews](https://spacenews.com/intuitive-machines-lands-on-the-moon/)). NASA says the CLPS contract had planned NDL only as a secondary velocity sensor, not a critical one ([NASA NTRS, FOP webinar, Aug 2024](https://ntrs.nasa.gov/api/citations/20240009717/downloads/FOP%20Webinar.pdf)).
- **Root cause of the rangefinder failure (as reported).** CEO Steve Altemus said a laser "safety enable switch" had not been disabled before launch, and mission control had no way to change it in flight ([SpaceQ, 24–26 Feb 2024](https://spaceq.ca/simple-error-could-have-resulted-in-intuitive-machines-mission-failure/); [New Atlas, 28 Feb 2024](https://newatlas.com/space/odysseus-broke-leg-landing)).
- **Touchdown.** Altemus said the planned touchdown was about 2 mph vertical and 0 mph horizontal. The data showed roughly 6 mph (10 km/h) vertical and 2 mph (3.2 km/h) horizontal. His working theory was that a landing leg caught on the terrain: "we might have fractured that landing gear and tipped over gently" ([Space.com, 24 Feb 2024](https://www.space.com/intuitive-machines-odysseus-moon-lander-tipped-over)). New Atlas, citing IM, reports that the lander came down short of the target on higher terrain than planned, skidded until a leg snapped, and came to rest on its helium tank at about 30° ([New Atlas](https://newatlas.com/space/odysseus-broke-leg-landing)). Flying Magazine says it "came to rest at an angle about 30 degrees above the surface" ([Flying, 28 Feb 2024](https://www.flyingmag.com/odysseus-lunar-landing-mission-nears-completion/)).
- **What the published cause says.** IM's explanation centres on touchdown velocity that was higher than planned and had a lateral component, which traces back to the disabled rangefinders. The leg then caught or fractured and the lander tipped. The 12° local slope, above the 10° design limit, is published by NASA. I found no official IM or NASA statement that weighs how much the slope contributed compared with velocity. I found no published post-flight reconstruction paper.
- **Outcome.** The mission was declared a soft landing. NASA received data from its active payloads. The lander powered down on 29 Feb 2024. IM listened for a wake-up from 20 Mar, and on 23 Mar 2024 said Odie "has permanently faded" ([Space.com](https://www.space.com/intuitive-machines-im-1-moon-mission-ends)).
- **Source discrepancy.** IM's FY2024 10-K says "Our IM-1 mission landed 9 degrees from the lunar South pole in March 2024". NASA's LRO page gives the landing date as 22 Feb 2024 ([10-K](https://www.sec.gov/Archives/edgar/data/1844452/000184445225000023/lunr-20241231.htm); [NASA LRO](https://www.nasa.gov/missions/lro/nasas-lro-images-intuitive-machines-odysseus-lander/)).

## Sources
1. Bussey, D.B.J. & Martin, T. (Intuitive Machines), "Intuitive Machines: Commercially enabling international lunar scientific exploration", 55th LPSC (2024), abstract 1931. https://www.hou.usra.edu/meetings/lpsc2024/pdf/1931.pdf
2. Intuitive Machines, Form 10-K for FY ended 31 Dec 2024 (SEC EDGAR). https://www.sec.gov/Archives/edgar/data/1844452/000184445225000023/lunr-20241231.htm
3. NASA, "NASA's LRO Images Intuitive Machine's Odysseus Lander", 26 Feb 2024. https://www.nasa.gov/missions/lro/nasas-lro-images-intuitive-machines-odysseus-lander/
4. NASA, CLPS Intuitive Machines IM-1 press kit (NP-2023-12-016-JSC), Jan 2024. https://www.nasa.gov/wp-content/uploads/2024/01/np-2023-12-016-jsc-clps-im-press-kit-web-508.pdf
5. NASA NTRS 20240009717, Flight Opportunities Community of Practice webinar (NDL), 7 Aug 2024. https://ntrs.nasa.gov/api/citations/20240009717/downloads/FOP%20Webinar.pdf
6. Wikipedia, "Intuitive Machines Nova-C". https://en.wikipedia.org/wiki/Intuitive_Machines_Nova-C
7. SpaceNews, "Intuitive Machines lands on the moon". https://spacenews.com/intuitive-machines-lands-on-the-moon/
8. Space.com, "Intuitive Machines' Odysseus lander tipped over on the moon during 'spicy' lunar landing", 24 Feb 2024. https://www.space.com/intuitive-machines-odysseus-moon-lander-tipped-over
9. Space.com, "Intuitive Machines' private Odysseus moon lander has 'permanently faded'...", 25 Mar 2024. https://www.space.com/intuitive-machines-im-1-moon-mission-ends
10. SpaceQ, "Simple error could have resulted in Intuitive Machines mission failure". https://spaceq.ca/simple-error-could-have-resulted-in-intuitive-machines-mission-failure/
11. New Atlas, "Odysseus broke leg on landing thanks to overlooked laser switch", 28 Feb 2024. https://newatlas.com/space/odysseus-broke-leg-landing
12. Flying Magazine, "'Odysseus' Lunar Landing Mission Nears Completion", 28 Feb 2024. https://www.flyingmag.com/odysseus-lunar-landing-mission-nears-completion/
13. New York Times, "Why It's So Challenging to Land Upright on the Moon", 4 Mar 2024 (paywalled, not checked; cited by Wikipedia for the 10° figure). https://www.nytimes.com/2024/03/04/science/moon-landing-sideways-gravity.html

Searched but not obtainable: Intuitive Machines' Nova-C product and IM-1 pages on intuitivemachines.com (JavaScript app, redirect loop); IM investor press releases (Akamai 403); NSSDCA entry (catalog error); a Nova-C payload user's guide (none found online).
