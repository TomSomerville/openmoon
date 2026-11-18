---
id_code: "C05.1"
milestone: M05
order: 1
title: Excavator robot (IPEx / RASSOR class)
summary: "A small, battery-powered robot that digs regolith with counter-rotating bucket drums, carries it, and dumps it where it is needed. Four of them grade pads and roads, pile berms and feed the oxygen plant."
trl: 5
spec:
  - {k: "Heritage", v: "NASA IPEx (TRL 5 design, 2024) and RASSOR"}
  - {k: "Quantity", v: "4 units (plan design choice)"}
  - {k: "Mass per unit", v: "~300 kg (ESTIMATE; IPEx itself is a 30 kg-class robot)"}
  - {k: "Load per dig cycle", v: "~150 kg (ESTIMATE; IPEx carries up to 30 kg)"}
  - {k: "Excavation rate", v: "200 kg/h per unit target (ESTIMATE; IPEx target is 42 kg/h)"}
  - {k: "Driving", v: "~30 cm/s, 7.5 cm rocks, 15° slopes (IPEx requirements)"}
  - {k: "Power", v: "Battery, recharged at a dock on the M04 grid; each charging dock has its own service connection and 120 V DC panel (plan design, DD-009)"}
  - {k: "Control", v: "Supervised autonomy; teleoperated from Earth when needed"}
  - {k: "Life", v: "5 years with yearly service (design goal; IPEx is sized for 11 days)"}
  - {k: "Delivery", v: "~2 t total with docks and spares, medium lander"}
subcomponents:
  - name: Bucket drums and arms
    desc: "Two pairs of hollow drums with staggered scoops dig in opposite directions, so the digging forces cancel and a light robot can still dig."
    parts: ["Bucket drums with internal baffles", "Drum actuator (harmonic drive + brushless motor)", "Arm actuators with power-off brake", "Replaceable scoop edges", "Load sensing from arm motor current"]
    tech: "IPEx regolith delivery subsystem; RASSOR 2"
    trl: 5
  - name: Chassis and mobility
    desc: "A simple four-wheel skid-steer chassis with no suspension, large rigid wheels and no steering motors."
    parts: ["Rigid aluminium grousered wheels", "Wheel actuators", "Chassis and electronics bay", "Grading blade and compaction roller (add-on tools)"]
    tech: "IPEx mobility subsystem; VIPER-derived wheels"
    trl: 5
  - name: Power and charging
    desc: "A battery pack runs the robot between charges at a dock fed by the base grid."
    parts: ["Li-ion battery pack (~50 V class bus)", "Wireless or contact charging dock", "Power distribution and motor drives", "Survival heaters"]
    tech: "IPEx lander charging concept"
    trl: 4
  - name: Autonomy and teleoperation
    desc: "Cameras give stereo depth and position; an auto-dig routine keeps the drums balanced; operators on Earth supervise."
    parts: ["Stereo camera pair for odometry and hazards", "Side camera and drum camera", "LED lighting", "Flight computer with auto-dig and path planning", "Radio link to base network (M03)"]
    tech: "IPEx cameras and auto-dig; NASA LTV delay tests"
    trl: 5
  - name: Dust and thermal protection
    desc: "Seals, covers and dust shields keep regolith out of joints and off lenses and radiators."
    parts: ["Felt and Nomex shaft seals", "Electrodynamic dust shields on camera covers", "Radiator with actuated cover", "Phase change material heat store", "Covers for idle periods"]
    tech: "IPEx camera and dust mitigation and thermal subsystems"
    trl: 4
  - name: Dumping and hauling
    desc: "Reversing drum rotation pours regolith out at a stockpile, hopper, berm or pad."
    parts: ["Reverse-rotation dumping", "Dump-site markers and maps", "ISRU hopper interface (M06)", "Arm lift to raise the chassis and climb obstacles"]
    tech: "IPEx bucket drum concept"
    trl: 5
risks:
  - {sev: Critical, title: "IPEx is designed for an 11-day mission, not years of work; no excavator has survived a lunar night", fix: "Design for night survival from the start (heaters, battery, park at dock); buy 4 units so the fleet survives losses."}
  - {sev: High, title: "Lunar excavation rates are unproven; the 42 kg/h figure is a design goal", fix: "Measure real rates in the first month; replan pads and berms; the sizing below shows berm work is the long pole."}
  - {sev: High, title: "Dust gets past seals; in tests dust filled the labyrinth part of a wheel seal", fix: "Double seals, covers when idle, sintered work areas; plan seal replacement during crew visits."}
  - {sev: High, title: "A wheel actuator bearing failed in accelerated life testing after about one mission's worth of turns", fix: "Upsize bearings and gearboxes for multi-year life; run life tests to at least 2x the planned revolutions."}
  - {sev: Medium, title: "Scaling IPEx from 30 kg to ~300 kg may change how drum forces balance and how the robot handles", fix: "Build and test a full-size prototype in a regolith bin and in reduced-gravity analogues before flight."}
  - {sev: Medium, title: "Teleoperation from Earth is slow with a several-second delay", fix: "Rely on onboard auto-dig and supervised autonomy; operators set goals, not individual moves."}
  - {sev: Medium, title: "Robots working near landing pads can be hit by ejecta", fix: "Park behind berms or at least 1 km away during landings; schedule digging around the landing timetable."}
sources:
  - {title: "NASA NTRS: IPEx TRL 5 design overview (ASCEND 2024)", url: "https://ntrs.nasa.gov/api/citations/20240008162/downloads/ASCEND24_IPEx%20TRL%205%20Design%20Overview.pdf", date: "2024"}
  - {title: "NASA KSC fact sheet: RASSOR (NTRS 20150022134)", url: "https://ntrs.nasa.gov/api/citations/20150022134/downloads/20150022134.pdf", date: "2015"}
  - {title: "NASA NTRS: ISRU Pilot Excavator design and scaling", url: "https://ntrs.nasa.gov/api/citations/20210025846/downloads/ASCE%20E%26S%202022-%20ISRU%20Pilot%20Excavator%20BD%20scaling.pdf", date: "2022"}
  - {title: "Connolly and Carrier, LPSC 2023: Updating lunar subsurface geotechnical properties", url: "https://ntrs.nasa.gov/api/citations/20220018853/downloads/LPSC%202023%20Abstract_Connolly_Carrier_v2.pdf", date: "2023"}
  - {title: "Gaier, NASA/TM-2005-213610: The effects of lunar dust on EVA systems during Apollo", url: "https://ntrs.nasa.gov/citations/20050160460", date: "2005"}
  - {title: "NASA NTRS 20240001217: LTV remote driving with time delay", url: "https://ntrs.nasa.gov/citations/20240001217", date: "2024"}
---

## What it does

The excavator digs, carries and dumps regolith. It grades the pad sites and roads, piles the ejecta berms and the reactor shield berm, and feeds regolith to the M06 oxygen plant. Open Moon plans four units, so the work continues if one fails.

## How it works

**Bucket drums.** NASA's IPEx uses bucket drums: hollow cylinders with scoops staggered around the outside. Regolith flows into the drum and is held by internal baffles. Two drum pairs dig in opposite directions, so the digging forces cancel. This lets a light robot dig without needing heavy weight for traction<sup class="r">[1](#s1)</sup><sup class="r">[3](#s3)</sup>. The forces from the drum arms are larger than the robot's own weight. So the arms can lift the chassis and climb obstacles taller than the wheels<sup class="r">[1](#s1)</sup>.

**Chassis.** IPEx has four wheels and skid-steers, with no suspension and no steering motors. It is designed to drive at 30 cm/s over 7.5 cm rocks and 15° slopes, and to cover up to 70 km in 11 days<sup class="r">[1](#s1)</sup>.

**Power.** IPEx runs on a battery and docks with a charger at its lander. Its actuators were tested at 47.6 to 58.8 V<sup class="r">[1](#s1)</sup>. Open Moon puts the docks on the M04 grid. Each dock is a rover charger with its own service connection and 120 V DC panel, like every other unit on the grid (plan design, design change DD-009).

**Autonomy.** IPEx needs at least four cameras: a stereo pair for odometry and hazards, a side camera that tracks the lander, and one between the drums. An "auto-dig" routine sets dig depth so the front and rear drums stay balanced<sup class="r">[1](#s1)</sup>. NASA tests showed operators can drive a rover with 4 to 8 s delays<sup class="r">[6](#s6)</sup>. So Earth operators set goals and the robot does the fine control.

**Dust.** Apollo found that dust abraded, clogged and fouled equipment<sup class="r">[5](#s5)</sup>. IPEx uses felt and Nomex shaft seals, electrodynamic dust shields on camera covers, and a radiator with an actuated cover and phase change material<sup class="r">[1](#s1)</sup>.

**Dumping.** To dump, the drums spin backwards and pour the regolith out<sup class="r">[1](#s1)</sup>.

## Sizing

IPEx is a 30 kg-class robot. It carries up to 30 kg per dig cycle and targets 10,000 kg at 42 kg/h<sup class="r">[1](#s1)</sup>. The RASSOR concept moves 35 loads of 20 kg every 24 hours, or 700 kg a day<sup class="r">[2](#s2)</sup>. Open Moon's biggest job is the berm around pad 2.

| Item | Value | Basis |
|---|---|---|
| Berm length | 377 m | ESTIMATE: ring at 60 m radius, 2π × 60 |
| Berm cross-section | 6 m² | ESTIMATE: 2 m high, 6 m base, triangle |
| Berm volume | 2,262 m³ | 377 × 6 |
| Bulk density | 1.5 t/m³ | ESTIMATE: between 1.30 at the surface and 1.92 below 1 m<sup class="r">[4](#s4)</sup> |
| Berm mass | ~3,400 t | 2,262 × 1.5 |
| Time with 4 IPEx units (168 kg/h) | ~20,200 h, ~2.3 years nonstop | 3,400,000 ÷ 168 |
| Time with 4 Open Moon units (800 kg/h) | ~4,250 h, ~6 months nonstop | 3,400,000 ÷ 800 |

So the design target of 200 kg/h per unit (ESTIMATE, about 5× IPEx) is needed. That is why the unit is scaled up to about 300 kg (ESTIMATE). Four units plus docks and spares fit the ~2 t delivery in M05.

## Testing and qualification

1. **Component life tests.** Run wheel, drum and arm actuators in thermal vacuum with dust, to at least 2× planned life. IPEx already ran this kind of test<sup class="r">[1](#s1)</sup>.
2. **Full-size prototype** in a regolith simulant bin. Measure dig rate, power and wheel slip.
3. **Reduced-gravity checks** of drum flow (IPEx planned drum experiments on a New Shepard flight<sup class="r">[1](#s1)</sup>).
4. **Day-in-the-life test** in a thermal vacuum chamber, including a simulated lunar night.
5. **On the Moon:** first unit grades a small area near its lander. Measure real rates for a month, then replan.

## Open questions

- Can a bucket-drum robot survive many lunar nights, or should it shelter in a heated garage?
- Does drum performance scale from 30 kg to 300 kg as expected?
- What is the best add-on tool for compaction: roller, vibratory plate or drum tamping?
- How fast do seals wear in real regolith, and can crews swap them in suits?
