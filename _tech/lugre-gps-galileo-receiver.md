---
slug: lugre-gps-galileo-receiver
title: "LuGRE GPS/Galileo receiver"
alternatives:
  - {name: "NASA LCRNS lunar relay navigation (Intuitive Machines)", compare: "Commercial relay satellites in lunar orbit that will broadcast their own navigation signals, so geometry and signal strength at the Moon are far better than Earth GNSS seen from 384,000 km. The catch is that the satellites must be built and launched first, and the service is paid for per mission.", status: "Contract to Intuitive Machines Sep 2024 (max $4.82 billion, to 2034); first relay not yet flown", url: "https://www.nasa.gov/goddard/esc/lcrns"}
  - {name: "ESA Moonlight (LCNS)", compare: "A European constellation of lunar satellites for communications and navigation, following LunaNet standards and focused on the south pole. It would give much better geometry than Earth GNSS, but it is a whole new infrastructure that is years from full service.", status: "In development; ESA targets initial operations by end of 2028 and full operations by 2030", url: "https://www.esa.int/Applications/Connectivity_and_Secure_Communications/ESA_s_Moonlight_programme_Pioneering_the_path_for_lunar_exploration"}
  - {name: "NaviMoon receiver (SpacePNT / EECL, on Lunar Pathfinder)", compare: "Another weak-signal GPS/Galileo receiver built for lunar orbit. It does the same job as LuGRE, and in ground tests it beat its 100 m accuracy target with a 42 m 3D position RMSE, but it has not yet operated at the Moon.", status: "Proto-flight model qualified and delivered for Lunar Pathfinder; in-orbit trials pending", url: "https://navisp.esa.int/news/article/navimoon-earth-moon-gnss-spaceborne-receiver-for-in-orbit-demonstration"}
  - {name: "Ground radio tracking (NASA Deep Space Network)", compare: "Large antennas in California, Spain and Australia measure range and Doppler to the spacecraft. It is proven and accurate, but it needs scarce ground antenna time and human operators, and the position is computed on Earth rather than on board.", status: "Operational for decades", url: "https://www.nasa.gov/communicating-with-missions/dsn/"}
links:
  - {title: "NASA: NASA successfully acquires GPS signals on Moon", url: "https://www.nasa.gov/centers-and-facilities/goddard/nasa-successfully-acquires-gps-signals-on-moon/", kind: official, date: "Mar 2025"}
  - {title: "NASA: NASA and Italian Space Agency test future lunar navigation technology", url: "https://www.nasa.gov/missions/artemis/nasa-and-italian-space-agency-test-future-lunar-navigation-technology/", kind: official, date: "Jan 2025"}
  - {title: "NASA: NASA Moon mission set to break record in navigation signal test", url: "https://www.nasa.gov/centers-and-facilities/goddard/nasa-moon-mission-set-to-break-record-in-navigation-signal-test/", kind: official, date: "Jun 2022"}
  - {title: "NASA Artemis blog: Blue Ghost prepares for landing, NASA instrument breaks record", url: "https://blogs.nasa.gov/artemis/2025/02/21/blue-ghost-prepares-for-landing-nasa-instrument-breaks-record/", kind: official, date: "Feb 2025"}
  - {title: "Parker, Dovis et al.: GNSS Reception at the Moon: First Results of the Lunar GNSS Receiver Experiment (LuGRE), NAVIGATION 73(1)", url: "https://navi.ion.org/content/73/1/navi.756", kind: paper, date: "Mar 2026"}
  - {title: "Politecnico di Torino open-access copy of the LuGRE first-results paper (PDF)", url: "https://iris.polito.it/retrieve/1383355f-0c92-43cd-b505-a11b56b5d792/navi.756.full.pdf", kind: paper, date: "2026"}
  - {title: "NASA NTRS: Flight experiences and results of the Lunar GNSS Receiver Experiment (LuGRE)", url: "https://ntrs.nasa.gov/citations/20260002034", kind: official, date: "Mar 2026"}
  - {title: "First multi-constellation observations of navigation satellite signals in the lunar domain by post-processing L1/L5 IQ snapshots (arXiv)", url: "https://arxiv.org/abs/2601.06081", kind: paper, date: "Dec 2025"}
  - {title: "LuGRE public mission data set (Zenodo)", url: "https://doi.org/10.5281/zenodo.16411686", kind: data, date: "2025"}
  - {title: "Wikipedia: Lunar GNSS Receiver Experiment", url: "https://en.wikipedia.org/wiki/Lunar_GNSS_Receiver_Experiment", kind: wiki, date: "2026"}
  - {title: "Wikipedia: Blue Ghost Mission 1", url: "https://en.wikipedia.org/wiki/Blue_Ghost_Mission_1", kind: wiki, date: "2026"}
  - {title: "NASA: The Lunar Relay (LCRNS project)", url: "https://www.nasa.gov/goddard/esc/lcrns", kind: official, date: "2026"}
  - {title: "NASA: NASA selects lunar relay contractor for Near Space Network services", url: "https://www.nasa.gov/news-release/nasa-selects-lunar-relay-contractor-for-near-space-network-services", kind: official, date: "Sep 2024"}
  - {title: "ESA: Moonlight programme, pioneering the path for lunar exploration", url: "https://www.esa.int/Applications/Connectivity_and_Secure_Communications/ESA_s_Moonlight_programme_Pioneering_the_path_for_lunar_exploration", kind: official, date: "Oct 2024"}
  - {title: "ESA NAVISP: NaviMoon, Earth-Moon GNSS spaceborne receiver for in-orbit demonstration", url: "https://navisp.esa.int/news/article/navimoon-earth-moon-gnss-spaceborne-receiver-for-in-orbit-demonstration", kind: official, date: "Oct 2024"}
---

## What it is

The Lunar GNSS Receiver Experiment (LuGRE) is a satellite-navigation receiver built to pick up GPS and Galileo signals at the Moon. It is a joint project of NASA Goddard, the Italian Space Agency (ASI), the Italian company Qascom and Politecnico di Torino, funded by NASA's SCaN program ([NASA](https://www.nasa.gov/centers-and-facilities/goddard/nasa-successfully-acquires-gps-signals-on-moon/)). Qascom built the weak-signal receiver with ASI funding ([NASA](https://www.nasa.gov/centers-and-facilities/goddard/nasa-moon-mission-set-to-break-record-in-navigation-signal-test/)). It flew on Firefly's Blue Ghost Mission 1 under NASA's CLPS program and landed in the Mare Crisium basin ([NASA](https://www.nasa.gov/centers-and-facilities/goddard/nasa-moon-mission-set-to-break-record-in-navigation-signal-test/), [Wikipedia](https://en.wikipedia.org/wiki/Blue_Ghost_Mission_1)).

It builds on nearly 30 years of high-altitude GNSS work. Before LuGRE, NASA's MMS mission held the record, with a GPS fix 116,300 miles (about 187,000 km) from Earth in 2019 ([NASA](https://www.nasa.gov/missions/artemis/nasa-and-italian-space-agency-test-future-lunar-navigation-technology/)). Blue Ghost launched on 15 January 2025, landed on 2 March and LuGRE finished its mission on 16 March 2025 ([Parker et al.](https://navi.ion.org/content/73/1/navi.756)).

LuGRE set several records. On 19 January it computed a fix about 329,982 km from Earth. On 3 March at 06:51 UTC it made the first GNSS navigation fix on the lunar surface. On 16 March it made a fix 398,350 km from Earth, and it tracked one Galileo satellite 433,220 km away ([paper PDF](https://iris.polito.it/retrieve/1383355f-0c92-43cd-b505-a11b56b5d792/navi.756.full.pdf)). It ran for more than 111 hours in total, over 95 of them on the surface, and met all its top-level science requirements ([paper PDF](https://iris.polito.it/retrieve/1383355f-0c92-43cd-b505-a11b56b5d792/navi.756.full.pdf)). Its data are public on [Zenodo](https://doi.org/10.5281/zenodo.16411686).

## Why Open Moon uses it

Milestone M03 (communications and navigation) needs every robot to know where it is. Open Moon's plan uses a weak-signal GPS/Galileo receiver of LuGRE heritage, combined with relay-based positioning and visual landmarks, so rovers can drive mapped roads.

The value is autonomy. Normally spacecraft are tracked from ground stations by human operators. GNSS signals can be picked up and used on board, even at the Moon ([NASA](https://www.nasa.gov/centers-and-facilities/goddard/nasa-successfully-acquires-gps-signals-on-moon/)). The GPS and Galileo satellites already exist, so the base gets a navigation source without building or paying for new infrastructure.

Without it, the base would depend on ground tracking through the [Deep Space Network](https://www.nasa.gov/communicating-with-missions/dsn/) and on lunar relay services such as [NASA's LCRNS](https://www.nasa.gov/goddard/esc/lcrns) and [ESA's Moonlight](https://www.esa.int/Applications/Connectivity_and_Secure_Communications/ESA_s_Moonlight_programme_Pioneering_the_path_for_lunar_exploration), which are not yet in service. GNSS is also a useful cross-check on those services.

## How it works

GPS and Galileo satellites point their antennas at Earth. Far from Earth, a receiver only catches the weak edges of the main beams that spill past the planet, plus even weaker side lobes ([Wikipedia](https://en.wikipedia.org/wiki/Lunar_GNSS_Receiver_Experiment)). LuGRE makes up for this with a high-gain antenna pointed at Earth, a low-noise amplifier and a receiver that can lock onto very faint signals.

The payload has three parts mounted separately on the lander, with a total mass of 4.64 kg ([NTRS](https://ntrs.nasa.gov/citations/20260002034)):

| Item | Value |
|---|---|
| Signals | GPS L1 C/A and L5; Galileo E1 and E5a |
| Antenna (Haigh Farr) | 15.35 dB, 12° beam at L1/E1; 14.56 dB, 16° beam at L5/E5a |
| Low-noise amplifier | 40 dB gain, ~1 dB noise figure |
| Receiver (Qascom QN400-Space) | 1.24 kg, under 14 W, two cold-redundant units |
| Acquisition / tracking threshold | 23 dB-Hz / 20 dB-Hz |
| Operating temperature | −35 °C to 50 °C |
| Clock | Temperature-compensated crystal (VCTCXO) |

Sources: [NTRS](https://ntrs.nasa.gov/citations/20260002034), [paper PDF](https://iris.polito.it/retrieve/1383355f-0c92-43cd-b505-a11b56b5d792/navi.756.full.pdf).

The receiver has two modes. In real-time mode it outputs pseudorange, Doppler and carrier-phase measurements and computes position, velocity and time by weighted least squares, with a Kalman filter option. In snapshot mode it records raw I/Q samples for processing on the ground ([paper PDF](https://iris.polito.it/retrieve/1383355f-0c92-43cd-b505-a11b56b5d792/navi.756.full.pdf)). The ground sends it broadcast ephemeris to help it acquire signals.

Measurement quality was comparable to typical receivers on Earth. L5/E5a signals were stronger and could be tracked for longer than L1/E1 ([NTRS](https://ntrs.nasa.gov/citations/20260002034)). Ground processing of the snapshots also found BeiDou and other regional and augmentation signals. Adding those constellations raised the share of time with at least four satellites in view from 11% to 46% in simulations ([arXiv](https://arxiv.org/abs/2601.06081)).

## Limitations and open issues

- **Poor accuracy from a single fix.** All the satellites sit in a tiny patch of sky, so geometry is bad. On the surface, steady-state errors were about 0.1-1 km, and range errors reached 1-100 km during bad-geometry periods ([paper PDF](https://iris.polito.it/retrieve/1383355f-0c92-43cd-b505-a11b56b5d792/navi.756.full.pdf)). The authors say operational use needs a Kalman filter and a high-stability clock or extra measurements.
- **Weaker signals than predicted.** Measured signal strength was 7-12 dB below the team's simulation. The cause is still under investigation, but it looks specific to this flight system rather than the lunar environment ([NTRS](https://ntrs.nasa.gov/citations/20260002034)).
- **Short test.** LuGRE ran for about two weeks on one near-side lander ([NASA](https://www.nasa.gov/centers-and-facilities/goddard/nasa-successfully-acquires-gps-signals-on-moon/)), with only about 3 hours of operation after sunset ([paper PDF](https://iris.polito.it/retrieve/1383355f-0c92-43cd-b505-a11b56b5d792/navi.756.full.pdf)). Lunar night survival and long-term radiation exposure were not tested.
- **Needs Earth in view.** The antenna must see Earth. Far-side sites and deep south-pole craters with no Earth view cannot use it; this is a general geometry limit, not a measured LuGRE result.
- **Not a product yet.** LuGRE was a one-off demonstration. No price or production model for a lunar version has been published.
- **Depends on outside systems.** GPS and Galileo are run for Earth users. Their side-lobe signals, which the Moon relies on, are not guaranteed by the operators; Open Moon could not find a published commitment.
