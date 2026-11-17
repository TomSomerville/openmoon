# Open Moon

An open-source plan for a self-sustaining Moon colony, using technology that exists
today or is in active testing.

Hosted on GitHub Pages at https://openmoon.beached.lol

## Structure of the plan

Phase → System → Component → Sub-component. Every level records:

- what it is and what it does
- the real hardware it is based on, and that hardware's Technology Readiness Level (TRL)
- the problems it will face, and how each one is solved
- sources for every claim

## Design templates

Five candidate designs are in `templates/`, viewable at https://openmoon.beached.lol/templates/.
The sample content in them shows the layout only and has not been checked against sources yet.

Round 2 templates (`templates/blueprint-v2/` and `templates/moonpunk/`) are generated:
edit `_templates_src/` (shared `body.html`, `base.css`, and per-theme CSS in `build.py`), then run
`python3 _templates_src/build.py`.
