---
id_code: "CT.2"
milestone: Transport
order: 2
title: Offloading crane
summary: "A lightweight, cable-driven crane based on NASA's LSMS that lifts cargo off a lander deck and sets it on the ground. It can also dig, act as a forklift and position payloads around the base."
trl: 4
spec:
  - {k: "Heritage", v: "NASA Langley Lightweight Surface Manipulation System (LSMS)"}
  - {k: "Lift capacity", v: "1,000 kg in lunar gravity (LSMS-1000 class)"}
  - {k: "Reach", v: "~7.6 m (25 ft, NASA proto-flight design)"}
  - {k: "Mass", v: "~500 kg each (NASA proposal mass goal)"}
  - {k: "Peak load moment", v: "~12.3 kN·m at full reach and full load (arithmetic)"}
  - {k: "Leveling", v: "Self-leveling base, ±15°"}
  - {k: "Tools", v: "Hook/hoist, forklift tines, regolith bucket, quick-change wrist"}
  - {k: "Quantity", v: "2 (one lander-mounted, one on a mobile base)"}
  - {k: "Delivery class", v: "Medium lander (Blue Moon Mk1), ~1 t for both"}
subcomponents:
  - name: Base and self-leveling turret
    desc: "Holds the crane to a lander deck or rover and keeps it level on slopes or on a tilted lander."
    parts: ["Mounting frame to CT.1 pallet hard points", "Waist rotation bearing and drive", "Self-leveling legs or wedges (±15°)", "Launch locks", "Counterweight bay (filled with regolith on the surface)"]
    tech: "LSMS proposal: self-leveling base"
    trl: 4
  - name: Boom links
    desc: "Lightweight truss links carry loads mainly in tension and compression, not bending, which saves mass."
    parts: ["Shoulder link (~4 m)", "Elbow link (~4 m)", "Wrist link (~4 m)", "Spreader bars that guide the cables", "Hinges with passive structural cables"]
    tech: "LSMS truss-and-cable architecture"
    trl: 4
  - name: Cable actuators
    desc: "Motors on the base reel cables in and out to move each joint, so no heavy gearboxes sit out on the arm."
    parts: ["Cable spools and winch motors at the base", "Low-temperature gearboxes", "Pulleys and cable routing", "Cable tension and length sensors", "Brakes that hold on power loss"]
    tech: "LSMS cable actuation; JPL bulk-metallic-glass cold gearbox (option)"
    trl: 4
  - name: End effectors
    desc: "A quick-change wrist lets the crane switch tools without an astronaut."
    parts: ["Hook and hoist with spreader bar", "Forklift tines for CT.1 pallets", "Regolith bucket", "Quick-change tool interface", "Power connector at the tip for recharging a rover"]
    tech: "LSMS end-effector toolbox; Honeybee quick-change"
    trl: 4
  - name: Sensing and control
    desc: "Cameras and a pose estimator find the payload, and software plans cable motions so the load follows a safe path."
    parts: ["Pose estimator and cameras", "Joint angle encoders", "Load cell at the hoist", "Trajectory-tracking software", "Teleoperation link via the base network"]
    tech: "ULTOR pose estimator (LSMS field tests); NASA LSMS trajectory tracking"
    trl: 4
  - name: Power and thermal
    desc: "Runs from the lander or base grid during lifts and keeps its motors and electronics warm between jobs."
    parts: ["28 V DC power input (CT.1 interface)", "Small battery for safe-stow on power loss", "Survival heaters on motors and electronics", "Multi-layer insulation on the base box", "Dust seals on bearings"]
    tech: "Standard lander-hosted payload practice"
    trl: 5
risks:
  - {sev: Critical, title: "Only ground prototypes exist; no LSMS has flown", fix: "Fund the proto-flight unit and a full environment test campaign first. Keep simple backups (ramps and winches) for the first deliveries."}
  - {sev: High, title: "Cables, pulleys and bearings jam or wear in abrasive lunar dust and deep cold", fix: "Seal the bearings and spools at the base, test cables in dust and thermal-vacuum chambers, and design cables to be replaced robotically."}
  - {sev: High, title: "A tipped or sloped lander puts the crane far off level", fix: "Self-leveling base (±15°). If the lander leans more than that, the mobile crane offloads it from the ground."}
  - {sev: High, title: "A load swings or drops and damages the payload or the lander", fix: "Lift slowly with a load cell and pose camera. Brakes hold on power loss. Proof-load test before every first lift of a new payload type."}
  - {sev: Medium, title: "Starship decks are far higher than the crane can reach", fix: "Use the lander's own elevator to bring cargo to the ground, then let the crane move it from there."}
  - {sev: Medium, title: "Integration with each lander's structure and avionics is not yet designed", fix: "Mount the crane through the CT.1 pallet hard points and connector, so integration is the same as for any other payload."}
  - {sev: Medium, title: "A 1 t limit cannot lift a whole 3 t Blue Moon Mk1 payload in one piece", fix: "Split medium cargo into pieces of 1 t or less, or use the lander's own offloading system for single heavy items."}
sources:
  - {title: "NASA NTRS: LSMS technology overview (Jones, for Blue Origin)", url: "https://ntrs.nasa.gov/api/citations/20205006977/downloads/LSMS%20Technology%20Overview%20V5%20Blue%20Origin.pdf", date: "Aug 2020"}
  - {title: "NASA: Lightweight crane technology could find a home on the Moon", url: "https://www.nasa.gov/centers-and-facilities/langley/lightweight-crane-technology-could-find-a-home-on-the-moon/", date: "Feb 2021"}
  - {title: "NASA NTRS: Trajectory tracking for the LSMS family of cable-driven cranes", url: "https://ntrs.nasa.gov/api/citations/20240001448/downloads/rss_kin_trajectory_tracking_submission.pdf", date: "2024"}
  - {title: "Blue Moon (spacecraft), Wikipedia", url: "https://en.wikipedia.org/wiki/Blue_Moon_(spacecraft)", date: "accessed Nov 2026"}
  - {title: "NASA HLS IAC 2026 presentation", url: "https://ntrs.nasa.gov/api/citations/20260009199/downloads/HLS%20IAC%202026%20Presentation%20FINAL.pdf", date: "Oct 2026"}
  - {title: "NASA NSSDC: Moon fact sheet", url: "https://nssdc.gsfc.nasa.gov/planetary/factsheet/moonfact.html", date: "accessed Nov 2026"}
  - {title: "NASA NTRS: Vertical Solar Array Technology annual review (south pole thermal environment)", url: "https://ntrs.nasa.gov/api/citations/20230012849/downloads/GCD%20Annual%20Review%20VSAT%20September%202023%20Final.pdf", date: "Sep 2023"}
---

## What it does

Landers put cargo on a deck several metres above the ground. Something has to lift it down. This crane does that job. It also moves cargo around the landing zone, loads pallets onto carts and digs regolith. It is based on NASA Langley's **Lightweight Surface Manipulation System (LSMS)**, a family of cable-driven cranes that has been developed and field-tested on Earth.

## How it works

- **Why cables.** The LSMS uses truss links moved by cables. The structure works in tension and compression rather than bending, which gives a better mass and power ratio than a conventional robotic arm<sup class="r">[1](#s1)</sup>. All motors sit at the base<sup class="r">[3](#s3)</sup>.
- **Heritage.** A 1,000 kg-class LSMS prototype was field-tested at Moses Lake, Washington, in 2008. It demonstrated offloading, forklift mode, digging and a quick-change tool<sup class="r">[1](#s1)</sup>. The family runs from the LSMS-L35 (35 kg lift in lunar gravity, sized for CLPS landers) to the LSMS-1000 (1,000 kg, sized for Blue Moon)<sup class="r">[3](#s3)</sup>.
- **Proto-flight design.** NASA's proto-flight version reaches about 7.6 m (25 ft) and lifts about 1 t. It has a power connection at the tip that could recharge a rover. Its tools include a bucket, forklift tines and a welder<sup class="r">[2](#s2)</sup>. A mini version with about 1.8 m (6 ft) reach suits small landers<sup class="r">[2](#s2)</sup>.
- **NASA's proposed path.** A 3-year, $22M Phase I would build an engineering unit and a proto-flight unit. It targets a 500 kg mass goal, ±15° self-leveling, self-deployment and a 2-week mission. That would take components from TRL 3 to 5 and the system from TRL 4 to 6<sup class="r">[1](#s1)</sup>. The proposal drawing shows three links of about 4 m each<sup class="r">[1](#s1)</sup>.
- **Comparison.** The best planetary offload so far is InSight's 1.8 m arm, which moved a 29 kg seismometer once<sup class="r">[1](#s1)</sup>.
- **Our use.** Crane 1 is mounted on the deck of a Blue Moon Mk1 delivery. That lander is 8.05 m tall<sup class="r">[4](#s4)</sup>. Crane 1 lifts the other cargo down, then lifts Crane 2 down onto a mobile base. LSMS plans already show offloading from a mobility vehicle<sup class="r">[1](#s1)</sup>. For Starship, whose crew area is at the top of a 52 m vehicle with an elevator<sup class="r">[5](#s5)</sup>, the elevator brings cargo down and the mobile crane takes it from there.

## Sizing

Load at the hook (arithmetic, lunar gravity 1.62 m/s²<sup class="r">[6](#s6)</sup>):

| Quantity | Value | Working |
|---|---|---|
| Rated lift | 1,000 kg | LSMS-1000 class<sup class="r">[3](#s3)</sup> |
| Weight on the Moon | 1,620 N | 1,000 × 1.62 |
| Moment at 7.6 m reach | ~12.3 kN·m | 1,620 × 7.6 |
| Same weight on Earth | ~165 kg | 1,620 ÷ 9.81 |
| Payload-to-crane mass ratio | 2 : 1 | 1,000 ÷ 500 kg goal<sup class="r">[1](#s1)</sup> |
| Two cranes delivered | ~1,000 kg | 2 × 500 kg (transport budget) |

The fourth row matters for testing. On Earth, a 165 kg test mass loads the crane the way a full 1 t payload does on the Moon. The crane's own weight is six times higher on Earth, though, so ground tests need a gravity-offload rig.

## Testing and qualification

1. **Component tests.** Cycle cables, spools, brakes and gearboxes in thermal vacuum down to the south-pole design low of −180 °C used by NASA's VSAT project<sup class="r">[7](#s7)</sup>, with lunar dust simulant present.
2. **Engineering unit.** Build the full-size crane. Run lifts with a 165 kg test mass at full reach on a gravity-offload rig. Test self-leveling on a ±15° tilt table.
3. **Field test.** Offload a full-size lander deck mock-up and CT.1 pallets outdoors, as the 2008 Moses Lake tests did<sup class="r">[1](#s1)</sup>.
4. **Proto-flight unit.** Run vibration, acoustic and thermal-vacuum tests to the lander environment, then a fit check on the lander.
5. **On the Moon.** Deploy from stowage and lift a dummy mass, then the real cargo. Measure cable wear and dust after every lift.

## Open questions

- Astrobotic is to provide a cargo accommodation system for Blue Moon<sup class="r">[4](#s4)</sup>. Will it include an offloader? If so, could this crane be simplified?
- Which cable material keeps its strength and abrades least in lunar dust at −180 °C?
- Should the mobile crane ride on an LTV (M07), or on its own powered cart?
- How do we certify a crane for lifting near crew, and what proof-load factor should we use?
