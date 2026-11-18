# Working rules for Open Moon

## Sources and claims
- Cite every claim with a link. Prefer official documentation, then wikis, then repositories or press. No AI-generated sources.
- State only what a source says. Mark this plan's own arithmetic or choices as "ESTIMATE", "plan design" or "this plan's arithmetic".

## Photos
- Any photo can be used, from any source, as long as it is properly cited: credit the photographer or organisation and link the page it came from.
- Prefer real hardware photos. When no hardware exists, say so plainly and show the closest real hardware, clearly captioned.

## Design decisions
- When a plan design decision is made, record it in `_data/decisions.yml` as the next `DD-00N`, with was / now / why, a dated source timeline and trade-offs.
- Then go through the ENTIRE plan and update everything it affects: milestones (`_milestones/`), components (`_components/`), technology cards (`_tech/`, `_data/tech.yml`), roadmap (`_data/roadmap.yml`, then run `python3 _tools/roadmap_art.py`), costs (milestone `cost` totals must equal the sum of `cost_items`), PBS (`_data/pbs.yml`) and any summaries that quote the old figures.
- Add `{% include decision-note.html id="DD-00N" extra="..." %}` where the change is most visible.
- Build the site (`jekyll build`) and check the affected pages before committing.

## Publishing
- GitHub Pages publishes the site from `main`. The owner wants every change live as soon as it is made.
- After every commit, push it to `main` (fast-forward) as well as to the working branch, so the site updates straight away. No pull request step.
