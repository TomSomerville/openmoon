# Intuitive Machines Nova-C (IM-2 "Athena")

Researched 18 November 2026. IM-1 (Odysseus) is covered in a separate file; this file covers Nova-C design specifications and the IM-2 flight.

## Summary

| Item | Value | Source |
|---|---|---|
| Max landing slope (design) | Up to 10° (company design claim). No slope certification document published | [Bussey & Martin (Intuitive Machines), LPSC 2024 abstract 1931](https://www.hou.usra.edu/meetings/lpsc2024/pdf/1931.pdf) |
| Max payload to lunar surface | Over 130 kg (company figure); NASA NSSDCA gives "100 to 130 kg" | [LPSC 2024 abstract 1931](https://www.hou.usra.edu/meetings/lpsc2024/pdf/1931.pdf); [NSSDCA PRIME-1 entry](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=PRIME-1) |
| Landing attempts | 2 Nova-C landings: IM-1 (Feb 2024) and IM-2 (6 Mar 2025). Both landed and ended on their sides. IM-2 landed in a 20 m crater on Mons Mouton | [NSSDCA](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=PRIME-1); [LROC](https://lroc.im-ldi.com/images/1408); [NASA](https://www.nasa.gov/news-release/nasa-receives-some-data-before-intuitive-machines-ends-lunar-mission/) |
| Status (Nov 2026) | IM-2 mission ended 7 Mar 2025. No Nova-C has landed since. IM-3 is targeting a March–April 2027 launch (as of Q3 2026 results, 12 Nov 2026) | [NASA](https://www.nasa.gov/news-release/nasa-receives-some-data-before-intuitive-machines-ends-lunar-mission/); [Investing.com, Q3 2026 slides](https://in.investing.com/news/stock-market-news/intuitive-machines-q3-2026-slides-record-revenue-19b-backlog-93CH-5700167) |

## Landing slope tolerance

- **Design spec: 10°.** A 2024 Lunar and Planetary Science Conference abstract by Intuitive Machines staff (D. B. J. Bussey and T. Martin) says Nova-C "can land on slopes up to 10° and uses a hazard detection and avoidance system to ensure a safe landing." ([LPSC 2024 #1931](https://www.hou.usra.edu/meetings/lpsc2024/pdf/1931.pdf))
- Wikipedia agrees: "The lander is designed to stay upright when landing on a slope of up to 10 degrees." It cites the New York Times, 4 March 2024. ([Wikipedia: Intuitive Machines Nova-C](https://en.wikipedia.org/wiki/Intuitive_Machines_Nova-C); [NYT](https://www.nytimes.com/2024/03/04/science/moon-landing-sideways-gravity.html), paywalled and not read directly)
- **What I could not find.** I found no formal certification, payload user's guide or test report that gives the slope limit, and none that says which touchdown velocity or attitude conditions the 10° assumes.
  - The NASA IM-2 press kit has no slope figure. ([NASA IM-2 press kit, Feb 2025](https://www.nasa.gov/wp-content/uploads/2025/02/np-2025-02-005-jsc-clps-intuitive-machines-press-kit-508-2-25-25.pdf))
  - The intuitivemachines.com product pages (`/lunar-access-services`, `/build/nova-c-lunar-lander`, and a linked `_files/ugd/...pdf`) are now a JavaScript app that redirected endlessly when I fetched them, so I could not read them.
- **Demonstrated on IM-2: not tested.** IM-2 did not test the slope limit on its own terms. The lander came down with a failed altimeter, at 10–13 m/s, on the rim of a crater (see Landing record). No terrain-slope value for the IM-2 touchdown point has been published. I checked LROC, NASA, NSSDCA, Aerospace America, SpaceflightNow and SpacePolicyOnline.

## Payload capacity

| Figure | Type | Source |
|---|---|---|
| "over 130 kg of payload to anywhere on the Moon" | Company design claim (2024) | [LPSC 2024 #1931](https://www.hou.usra.edu/meetings/lpsc2024/pdf/1931.pdf) |
| "capable of carrying 100 to 130 kg of payload to the surface" | NASA catalogue (Athena entry) | [NSSDCA PRIME-1](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=PRIME-1) |
| 100 kg (infobox) vs. "over 130 kg" (body text) | Wiki, internally inconsistent; the 100 kg cites an older intuitivemachines.com page | [Wikipedia: Nova-C](https://en.wikipedia.org/wiki/Intuitive_Machines_Nova-C) |

**Payload actually flown on IM-2.** I found no published total for the IM-2 payload mass. The figures I did find:

- PRIME-1 (the NASA drill and mass spectrometer): "about 40 kg". ([NSSDCA](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=PRIME-1))
- Other payloads included the Micro-Nova "Grace" hopper, Lunar Outpost's MAPP rover, the Yaoki rover, the Nokia 4G/LTE system and a laser retroreflector array. ([NASA press kit](https://www.nasa.gov/wp-content/uploads/2025/02/np-2025-02-005-jsc-clps-intuitive-machines-press-kit-508-2-25-25.pdf); [NSSDCA](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=PRIME-1))

**Lander mass (Wikipedia, for context).**

- Nova-C generic: launch mass 1,908 kg and dry mass 675 kg. ([Wikipedia: Nova-C](https://en.wikipedia.org/wiki/Intuitive_Machines_Nova-C))
- IM-2 launch mass: 2,120 kg, citing Gunter's Space Page. ([Wikipedia: IM-2](https://en.wikipedia.org/wiki/IM-2))

**Nova-D (larger variant).** The figures conflict and none of them has been demonstrated:

- "payload capacity up to 2500 kg, depending on the launch vehicle" (Intuitive Machines, 2024). ([LPSC 2024 #1931](https://www.hou.usra.edu/meetings/lpsc2024/pdf/1931.pdf))
- Earlier reports said "more than 500 kg" using two VR-900 engines. ([Wikipedia: Nova-C](https://en.wikipedia.org/wiki/Intuitive_Machines_Nova-C), citing [NASASpaceflight, Aug 2021](https://www.nasaspaceflight.com/2021/08/intuitive-machines-im-3/))
- No Nova-D slope tolerance has been published.

## Landing record

**IM-2 / Athena (Nova-C)**

**Launch.** 27 February 2025 at 00:16 UT on a Falcon 9. ([NSSDCA](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=PRIME-1))

**Touchdown.** Sources give slightly different times:

| Time | Source |
|---|---|
| About 17:30 UT on 6 March 2025 | [NSSDCA](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=PRIME-1) |
| About 11:30 a.m. CST | [NASA, 7 Mar 2025](https://www.nasa.gov/news-release/nasa-receives-some-data-before-intuitive-machines-ends-lunar-mission/) |
| 17:28:50 UTC | [Wikipedia infobox](https://en.wikipedia.org/wiki/IM-2) |

**Site.**

- Mons Mouton plateau near the south pole, at 84.7906° S, 29.1957° E. ([NSSDCA](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=PRIME-1); [LROC, 10 Mar 2025](https://lroc.im-ldi.com/images/1408))
- The Lunar Reconnaissance Orbiter Camera (LROC) team says Athena "hit the surface faster than intended" and "ended up on its side within a 20-meter diameter crater." ([LROC](https://lroc.im-ldi.com/images/1408))

**Miss distance.** NASA's own release gives two figures:

- The text says "more than 1,300 feet (400 meters) from its intended landing site."
- The photo caption gives about 820 ft (about 250 m).

([NASA](https://www.nasa.gov/news-release/nasa-receives-some-data-before-intuitive-machines-ends-lunar-mission/))

**Outcome.**

- The lander rested on its side and could not generate enough power. ([NSSDCA](https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=PRIME-1))
- Intuitive Machines declared end of mission at 12:15 a.m. CST on 7 March 2025. ([NASA](https://www.nasa.gov/news-release/nasa-receives-some-data-before-intuitive-machines-ends-lunar-mission/))
- LROC says Athena sent back over 400 MB of data. ([LROC](https://lroc.im-ldi.com/images/1408))

**Published cause.** These are company statements: CEO Steve Altemus on the Q1 2025 earnings call (13 May 2025) and the IM-3 team to Aerospace America (July 2025). I found no NASA or independent failure report.

1. **Laser altimeter interference.** Altemus: "We saw signal noise and distortion that did not allow for accurate altitude readings." ([SpaceflightNow, 14 May 2025](https://spaceflightnow.com/2025/05/14/intuitive-machines-ceo-points-to-issues-that-prevented-upright-touchdown-during-im-2-moon-landing/); [SpacePolicyOnline, 13 May 2025](https://spacepolicyonline.com/news/im-2s-imperfect-landing-due-to-altimeter-interference-south-pole-lighting-conditions/))
   - The rangefinder showed optical noise even when the laser was not firing.
   - The team suspects a detector problem; this was still being evaluated.
   - Athena's software "judged the vehicle to be still some 400 meters above the surface."
   - The lander "hit the surface hard, traveling at 10 to 13 meters per second" near the edge of a crater.

   ([Aerospace America, 22 Jul 2025](https://aerospaceamerica.aiaa.org/how-intuitive-machines-is-planning-to-make-its-third-moon-landing-a-successful-one/))
2. **South-pole lighting.** "low-angle sunlight created long shadows and dim lighting conditions." ([SpaceflightNow](https://spaceflightnow.com/2025/05/14/intuitive-machines-ceo-points-to-issues-that-prevented-upright-touchdown-during-im-2-moon-landing/))
3. **Crater-recognition tuning.** The optical navigation relied on LRO imagery taken from 100 km, which "could not accurately account for how craters appear at lower altitudes with South Pole lighting conditions." ([SpaceflightNow](https://spaceflightnow.com/2025/05/14/intuitive-machines-ceo-points-to-issues-that-prevented-upright-touchdown-during-im-2-moon-landing/))

**Slope at the touchdown point:** not published (see Landing slope tolerance).

### Published changes for IM-3

- "dissimilar and redundant altimeters." Aerospace America describes these as redundant laser rangefinders from two vendors, flight-tested on a fixed-wing plane and a helicopter. ([SpaceflightNow](https://spaceflightnow.com/2025/05/14/intuitive-machines-ceo-points-to-issues-that-prevented-upright-touchdown-during-im-2-moon-landing/); [Aerospace America](https://aerospaceamerica.aiaa.org/how-intuitive-machines-is-planning-to-make-its-third-moon-landing-a-successful-one/))
- A sensor for surface-velocity measurement that does not depend on lighting. ([SpacePolicyOnline](https://spacepolicyonline.com/news/im-2s-imperfect-landing-due-to-altimeter-interference-south-pole-lighting-conditions/))
- An expanded onboard crater database, with IM-2 imagery fed into machine-learning crater tracking. ([SpacePolicyOnline](https://spacepolicyonline.com/news/im-2s-imperfect-landing-due-to-altimeter-interference-south-pole-lighting-conditions/))
- 12 lunar orbits before landing instead of 3, to allow more time for laser calibration. ([Aerospace America](https://aerospaceamerica.aiaa.org/how-intuitive-machines-is-planning-to-make-its-third-moon-landing-a-successful-one/))
- The team is "examining... ground contact conditions, vehicle stability and landing gear durability." No change to the legs, landing gear or the 10° slope tolerance has been published. The same propulsion and primary structure are kept, with "a few tweaks." ([Aerospace America](https://aerospaceamerica.aiaa.org/how-intuitive-machines-is-planning-to-make-its-third-moon-landing-a-successful-one/))
- **Target site:** Reiner Gamma. ([NASA press kit](https://www.nasa.gov/wp-content/uploads/2025/02/np-2025-02-005-jsc-clps-intuitive-machines-press-kit-508-2-25-25.pdf))
- **Launch:** targeting March–April 2027 after final end-to-end testing in Q1 2027. The lander's liquid oxygen–methane engine was fired on the integrated IM-3 lander in late October 2026. ([Investing.com, Nov 2026](https://in.investing.com/news/stock-market-news/intuitive-machines-q3-2026-slides-record-revenue-19b-backlog-93CH-5700167))
  - The company's Q3 2026 release (GlobeNewswire, 12 Nov 2026) says only that it remains "laser focused on IM-3." ([Finviz copy](https://finviz.com/news/421555/intuitive-machines-reports-third-quarter-2026-financial-results-reports-record-financials-across-the-board-revenue-profitability-positive-cash-flow-and-backlog))
  - The original on investors.intuitivemachines.com returned 403 to automated fetches.

## Sources

**Official (company and agency)**
- Bussey, D. B. J. & Martin, T. (Intuitive Machines), "Intuitive Machines: Commercially Enabling International Lunar Scientific Exploration," 55th LPSC (2024), abstract 1931: https://www.hou.usra.edu/meetings/lpsc2024/pdf/1931.pdf
- NASA NSSDCA, "Intuitive Machines 2 (PRIME 1)": https://nssdc.gsfc.nasa.gov/nmc/spacecraft/display.action?id=PRIME-1
- NASA, "NASA Receives Some Data Before Intuitive Machines Ends Lunar Mission" (7 Mar 2025): https://www.nasa.gov/news-release/nasa-receives-some-data-before-intuitive-machines-ends-lunar-mission/
- NASA, CLPS Intuitive Machines IM-2 press kit (Feb 2025): https://www.nasa.gov/wp-content/uploads/2025/02/np-2025-02-005-jsc-clps-intuitive-machines-press-kit-508-2-25-25.pdf
- LROC (Arizona State University), image post 1408, M. Robinson (10 Mar 2025): https://lroc.im-ldi.com/images/1408

**Wikis**
- Wikipedia, "Intuitive Machines Nova-C": https://en.wikipedia.org/wiki/Intuitive_Machines_Nova-C
- Wikipedia, "IM-2": https://en.wikipedia.org/wiki/IM-2

**Reputable press**
- Aerospace America (AIAA), K. Button, "How Intuitive Machines is planning to make its third moon landing a successful one" (22 Jul 2025): https://aerospaceamerica.aiaa.org/how-intuitive-machines-is-planning-to-make-its-third-moon-landing-a-successful-one/
- SpaceflightNow (14 May 2025): https://spaceflightnow.com/2025/05/14/intuitive-machines-ceo-points-to-issues-that-prevented-upright-touchdown-during-im-2-moon-landing/
- SpacePolicyOnline (13 May 2025): https://spacepolicyonline.com/news/im-2s-imperfect-landing-due-to-altimeter-interference-south-pole-lighting-conditions/
- Investing.com, Q3 2026 slides summary (Nov 2026): https://in.investing.com/news/stock-market-news/intuitive-machines-q3-2026-slides-record-revenue-19b-backlog-93CH-5700167
- Finviz copy of the GlobeNewswire Q3 2026 release (12 Nov 2026): https://finviz.com/news/421555/intuitive-machines-reports-third-quarter-2026-financial-results-reports-record-financials-across-the-board-revenue-profitability-positive-cash-flow-and-backlog

**Searched but not readable**
- intuitivemachines.com product pages and PDF (redirect loop).
- investors.intuitivemachines.com releases (HTTP 403).
- arstechnica.com IM-2 article (fetch blocked).
- NYT, 4 Mar 2024 (paywall).
