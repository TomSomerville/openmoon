# JAXA SLIM (Smart Lander for Investigating Moon)

## Summary
| Item | Value | Source |
|---|---|---|
| Max landing slope (design) | **No formal maximum (certified) slope tolerance found.** JAXA's design case: the target site is "sloped to approximately 15 degrees" / "relatively constant slope of 15 degrees or less", and the two-step landing method was adopted so SLIM could land safely on it. JAXA's own ISAS magazine gives a different figure for the target terrain: "average slope of 6 – 7 degrees". | [JAXA SLIM Media Kit (Aug 2023), pp. 18-19](https://global.jaxa.jp/countdown/slim/SLIM-mediakit-EN_2308.pdf); [ISAS Cosmos, "20 minutes of terror"](https://cosmos.isas.jaxa.jp/?p=7409) |
| Max payload to lunar surface | **Not published.** SLIM was a technology demonstrator, not a payload delivery lander. Payloads it actually carried: Multi-Band Camera (MBC, mass not published), LEV-1 (~2.1 kg), LEV-2/SORA-Q (238 g), NASA LRA (~21 g). Lander dry mass ~200 kg; launch mass ~715 kg. | [JAXA SLIM press briefing, 26 Dec 2024](https://www.isas.jaxa.jp/en/topics/files/SLIM-press-briefing-20241226.pdf) |
| Landing attempts | 1. Landed 20 Jan 2024 00:20 JST (19 Jan 15:20 UTC) near Shioli crater, 13.3°S 25.2°E. Soft landing, but it ended up "almost vertical" and upside down, with the main engine facing up. The cause was a main-engine nozzle that separated at ~50 m altitude. It was not a slope failure: the two-step landing was never carried out as designed. | [JAXA briefing, 25 Jan 2024](https://global.jaxa.jp/press/2024/01/file/jaxa_doc01_20240125_e.pdf) |
| Status (Nov 2026) | Mission ended. Last contact 28 Apr 2024. JAXA ended operations at 22:40 JST on 23 Aug 2024. NASA LRO continues to use the SLIM LRA as a laser-ranging target. | [JAXA press release, 26 Aug 2024](https://global.jaxa.jp/press/2024/08/20240826-1_e.html); [JAXA briefing, 26 Dec 2024](https://www.isas.jaxa.jp/en/topics/files/SLIM-press-briefing-20241226.pdf) |

## Landing slope tolerance

**Design spec: no explicit maximum slope tolerance (in degrees) is published in any official JAXA source I found.** What JAXA does publish:

- **The design-case site slope is about 15°.** The JAXA media kit says: "Because the landing site is located near a crater, the surrounding area is sloped to approximately 15 degrees. Therefore, the method of landing safely on such a slope becomes important." It also says the area has a "relatively constant slope of 15 degrees or less (13.3degS/25.2degE)". The kit presents the "two-step landing method" as the solution: the main landing gear touches down first, then the lander rotates forward to stabilise. The kit says this method "has shown excellent reliable landing results through simulation." This is the slope SLIM was designed to handle. JAXA does not call it a certified limit. ([Media Kit pp. 18-19](https://global.jaxa.jp/countdown/slim/SLIM-mediakit-EN_2308.pdf))
- **Conflicting figure (6-7°).** ISAS's own magazine says SLIM aimed to land "with a landing accuracy of within a 100m on terrain with an average slope of 6 – 7 degrees". The article gives no numeric tolerance for the two-step landing. ([ISAS Cosmos](https://cosmos.isas.jaxa.jp/?p=7409)) The two figures may describe different things (an upper bound for the area vs. an average). No source reconciles them, so both are recorded here.
- **Specified touchdown conditions.** JAXA gives the specified descent rate at touchdown as 1.8-2.8 m/s. It mentions specified ranges for lateral velocity and attitude but does not give their values. ([JAXA briefing 25 Jan 2024, p. 15](https://global.jaxa.jp/press/2024/01/file/jaxa_doc01_20240125_e.pdf))
- **Research studies (not design specs).** These papers simulated SLIM-based models on slopes of up to ±20° and gave no certified limit:
  - Morikawa et al., ISTS-2017-d-069/ISSFD-2017-069, "Evaluation of Landing Stability of Two-step Landing Method for Small Lunar-planetary Lander". It ran ADAMS simulations "refer[ring] to SLIM" at terrain slopes of 0, ±10 and ±20 deg, and concluded that the two-step method has higher landing stability than a conventional four-leg lander. ([ISSFD PDF](https://www.issfd.org/ISSFD_2017/paper/ISTS-2017-d-069__ISSFD-2017-069.pdf))
  - Nakata et al. (Kyushu Univ. / SLIM WG), ISAS Space Science Symposium poster P2-165. It ran overturn simulations at lunar-surface slopes of -20 to 20 deg. ([ISAS PDF](https://www.isas.jaxa.jp/j/researchers/symp/sss13/paper/P2-165.pdf))
  - Related JSASS paper on the two-step method: it says the method "can land on steep slope by tilting body attitude toward inclination direction of landing site". I saw only the abstract; it gives no degree limit. ([J-STAGE](https://www.jstage.jst.go.jp/article/astj/17/0/17_JSASS-D-17-00003/_article/-char/en))
- **Demonstrated: none.** The two-step landing was never carried out. A propulsion anomaly meant SLIM touched down "in an almost upright standing position" with lateral velocity and attitude outside the specified range (see Landing record). No measured slope of the actual touchdown point was published.

Searches run: JAXA/ISAS English and Japanese pages ("2段階着陸 傾斜 15度 斜面 許容"), the media kit, the Jan and Dec 2024 briefings, the 2016 JAXA project report, Wikipedia, NSSDCA (its entry has no description), and J-STAGE/ISSFD papers.

## Payload capacity

**Maximum payload mass to the lunar surface: not published.** SLIM's success criteria cover precision landing and a lightweight spacecraft. They do not cover payload delivery, and no JAXA document I found states a payload capacity. ([Media Kit p. 6](https://global.jaxa.jp/countdown/slim/SLIM-mediakit-EN_2308.pdf))

What JAXA publishes:
- **Spacecraft mass:**
  - As flown: ~200 kg dry and ~715 kg at launch ([Dec 2024 briefing p. 4](https://www.isas.jaxa.jp/en/topics/files/SLIM-press-briefing-20241226.pdf)).
  - The media kit gives 200 kg dry and 700-730 kg wet ([Media Kit p. 7](https://global.jaxa.jp/countdown/slim/SLIM-mediakit-EN_2308.pdf)).
  - The JAXA comparison table gives the landing mass excluding fuel as ~200 kg ([Dec 2024 briefing p. 7](https://www.isas.jaxa.jp/en/topics/files/SLIM-press-briefing-20241226.pdf)).
  - Conflicting earlier figure: the 2016 JAXA project report planned a launch mass of about 590 kg ([JAXA 2016 report](https://www.jaxa.jp/press/2016/07/files/20160714_slim_01_j.pdf)). Wikipedia cites this for its 590 kg launch / 120 kg dry figures ([Wikipedia](https://en.wikipedia.org/wiki/Smart_Lander_for_Investigating_Moon)).
- **Payloads actually carried (the PLD "payload mission system"):**
  - Multi-Band Camera (MBC): mass not published.
  - LEV-1: "Mass approx. 2.1kg" ([Dec 2024 briefing p. 8](https://www.isas.jaxa.jp/en/topics/files/SLIM-press-briefing-20241226.pdf)).
  - LEV-2 / SORA-Q: "Mass: 238g" ([same, p. 8](https://www.isas.jaxa.jp/en/topics/files/SLIM-press-briefing-20241226.pdf)). Wikipedia gives 250 g, citing JAXA ([Wikipedia](https://en.wikipedia.org/wiki/Smart_Lander_for_Investigating_Moon)).
  - NASA Laser Retroreflector Array (LRA): "approximately 21g" ([same, p. 9](https://www.isas.jaxa.jp/en/topics/files/SLIM-press-briefing-20241226.pdf)).
  - No total payload mass is published, because the MBC mass is missing.

## Landing record

**Attempt 1 (only attempt): 20 Jan 2024, 00:20 JST (19 Jan 15:20 UTC).** Site: near Shioli crater, Mare Nectaris.
- **Sources for the date and site:** the [JAXA press release of 20 Jan 2024](https://global.jaxa.jp/press/2024/01/20240120-1_e.html) and the [Media Kit p. 18](https://global.jaxa.jp/countdown/slim/SLIM-mediakit-EN_2308.pdf).
- **Target coordinates:** 13.3°S, 25.2°E.
- **Estimated landing point:**
  - Onboard estimate: 25.24889°E, -13.31549° ([Jan 2024 briefing](https://global.jaxa.jp/press/2024/01/file/jaxa_doc01_20240125_e.pdf)).
  - NASA LRO estimate: 13.3160°S, 25.2510°E ([Dec 2024 briefing p. 5](https://www.isas.jaxa.jp/en/topics/files/SLIM-press-briefing-20241226.pdf)).
- **Terrain slope at the site:** the target area slopes about 15° or less ([Media Kit](https://global.jaxa.jp/countdown/slim/SLIM-mediakit-EN_2308.pdf)) or averages 6-7° ([ISAS Cosmos](https://cosmos.isas.jaxa.jp/?p=7409)). No measured slope of the actual touchdown point was published. ISAS says only that "the landing site was also on sloped terrain" ([ISAS Cosmos](https://cosmos.isas.jaxa.jp/?p=8083)).
- **What happened** ([JAXA briefing 25 Jan 2024, pp. 14-17](https://global.jaxa.jp/press/2024/01/file/jaxa_doc01_20240125_e.pdf)):
  1. At about 00:19:18, at ~50 m altitude, total main-engine thrust suddenly fell to about 55%. The navigation camera images show what is likely the –X engine nozzle falling away.
  2. One engine could produce only about lunar-gravity thrust. SLIM descended at 2-3 m/s and gained horizontal velocity toward –X. It drifted about 55 m east (JAXA's Dec 2024 summary says about 60 m east).
  3. LEV-1 and LEV-2 separated at about 5 m altitude.
  4. SLIM touched down at about 00:19:52 "in an almost upright standing position". The descent rate was ~1.4 m/s, below the specified 1.8-2.8 m/s. However, "lateral velocity and attitude exceeded the specified range and produced a large attitude fluctuation after landing". As a result, SLIM settled "almost vertical … with the main engine facing upwards and the solar panels facing west". This means the planned two-step landing never took place.
- **Root cause (final):** SLIM used a blowdown propulsion system, and propellant supply pressure was low late in the mission. The 12 thrusters fired at the same moment as the main engine, which lowered supply pressure further, so the –X engine failed to ignite. Unburned propellant then built up and ignited about 1 s later. The resulting excessive ignition shock damaged and separated the nozzle. JAXA concluded the problem was not caused by the main engine itself. ([Dec 2024 briefing p. 12](https://www.isas.jaxa.jp/en/topics/files/SLIM-press-briefing-20241226.pdf))
- **Accuracy:** about 10 m or better, assessed from images taken at ~50 m altitude, before the anomaly-driven drift. JAXA's success criteria are met at "full" level.
  - Sources: [Dec 2024 briefing pp. 5, 11](https://www.isas.jaxa.jp/en/topics/files/SLIM-press-briefing-20241226.pdf) and the [JAXA 26 Aug 2024 release](https://global.jaxa.jp/press/2024/08/20240826-1_e.html).
- **Surface operations:**
  - With the solar panels facing west, SLIM was powered down after landing. It resumed operations on 28 Jan 2024 when the Sun angle changed.
  - The MBC observed 10 rocks and 2 regolith sites in 10 bands.
  - SLIM survived three lunar nights even though it was not designed to.
  - Last contact was 28 Apr 2024, and operations were terminated on 23 Aug 2024.
  - Sources: [Dec 2024 briefing pp. 8-10](https://www.isas.jaxa.jp/en/topics/files/SLIM-press-briefing-20241226.pdf) and the [JAXA 26 Aug 2024 release](https://global.jaxa.jp/press/2024/08/20240826-1_e.html).
- **What this tells us about the slope claim:** the tip-over was caused by the propulsion anomaly, which left lateral velocity and attitude out of range. It does not show whether the ~15° design slope was within or beyond SLIM's capability. The slope tolerance remains undemonstrated.

## Sources
- JAXA, *SLIM Media Kit* (Aug 2023): https://global.jaxa.jp/countdown/slim/SLIM-mediakit-EN_2308.pdf
- JAXA, SLIM press briefing materials, 25 Jan 2024: https://global.jaxa.jp/press/2024/01/file/jaxa_doc01_20240125_e.pdf
- JAXA press release, SLIM landing, 20 Jan 2024: https://global.jaxa.jp/press/2024/01/20240120-1_e.html
- JAXA press release, conclusion of SLIM lunar activities, 26 Aug 2024: https://global.jaxa.jp/press/2024/08/20240826-1_e.html
- JAXA/ISAS, SLIM press briefing (project summary and nozzle investigation), 26 Dec 2024: https://www.isas.jaxa.jp/en/topics/files/SLIM-press-briefing-20241226.pdf
- JAXA, SLIM project report (Japanese), 14 Jul 2016: https://www.jaxa.jp/press/2016/07/files/20160714_slim_01_j.pdf
- ISAS Cosmos, "20 minutes of terror: SLIM will attempt a pinpoint accurate landing": https://cosmos.isas.jaxa.jp/?p=7409
- ISAS Cosmos, "Landing on the Moon: Behind the scenes of the night when SLIM made history": https://cosmos.isas.jaxa.jp/?p=8083
- ISAS, SLIM mission page: https://www.isas.jaxa.jp/en/missions/spacecraft/past/slim.html
- Wikipedia, "Smart Lander for Investigating Moon": https://en.wikipedia.org/wiki/Smart_Lander_for_Investigating_Moon
- Morikawa et al., ISTS-2017-d-069 / ISSFD-2017-069: https://www.issfd.org/ISSFD_2017/paper/ISTS-2017-d-069__ISSFD-2017-069.pdf
- Nakata et al., ISAS Space Science Symposium P2-165: https://www.isas.jaxa.jp/j/researchers/symp/sss13/paper/P2-165.pdf
- JSASS, Aerospace Technology Japan vol. 17 (two-step landing): https://www.jstage.jst.go.jp/article/astj/17/0/17_JSASS-D-17-00003/_article/-char/en
