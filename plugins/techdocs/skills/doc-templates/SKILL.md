---
name: doc-templates
tier: leaf
description: >
  Starting skeletons for the doc types written often: vision, target
  architecture, discovery, technical design, PRD, research doc, ADR. Load when
  asked to write, start, restructure or convert one of these docs, or to decide
  which horizon a planning doc belongs to. Do NOT load for folder placement and
  frontmatter rules (see docs-management), for prose rules (see writing-style),
  or for execution plans (owned by project-management).
trigger: /doc-templates
---

# /doc-templates

Templates save tokens: copy the skeleton, fill it, delete the guidance. Read `${CLAUDE_SKILL_DIR}/references/model.md` first when the doc is a planning doc (vision, target architecture, discovery, design): it defines horizons, spans and the constraint tests.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Folder choice, frontmatter values | `docs-management` |
| Prose rules and LLM tells | `writing-style` |
| Critiquing a finished doc against the horizon model | `horizon-review` |
| Sourcing a research doc from external material | `external-research` |
| Execution plans, tasks, changelogs | `project-management`, `changelog` |

## Templates

All live in `${CLAUDE_SKILL_DIR}/references/templates/`. Destination keys resolve through `project-map`.

| Doc type | Horizon | Template | Destination |
|---|---|---|---|
| Vision | H6 | `vision.md` | `prd` key |
| Target architecture | H5 | `target-architecture.md` | `design` key |
| Discovery | H3 | `discovery.md` | `investigations` key |
| Technical design | H2 | `design-doc.md` | `design` key until built (see `docs-management`) |
| PRD | none | `prd.md` | `prd` key |
| Research doc | none | `research-doc.md` | `investigations` key |
| ADR | none | `adr.md` | `docs` key, `explanation/` |

The model has a Plan horizon (H4: initiatives, order, owners, dates). It has no template here, because quarter-level plans are owned by `project-management`.

## Choosing the horizon

Ask what the document decides and for how long that decision must hold:

- outcomes and bets for several years: vision
- components, data ownership and constraints for a domain: target architecture
- options for one question, a recommendation and no decision: discovery
- the mechanism for one piece of work: technical design

If a draft mixes horizons (a vision that names a broker, a discovery that "decides"), say so and propose a split. Do not move content silently.

## Filling a template

1. Copy the file to its destination under the right name (`kebab-case.md`) and keep the frontmatter block first. Set `created` and `updated` to today.
2. Replace each guidance line (quoted) with content, and delete the guidance once the section is filled.
3. Replace italic examples; never leave the online-shop examples in a real doc.
4. Fill upstream sections from the real docs above, with links. If they do not exist, say so in the table instead of inventing constraints.
5. Write the prose under `writing-style`, then run the template checklist and `horizon-review` for planning docs.
6. Finish with `editorial-review`.

## Hard rules

- Never leave template guidance, placeholder text or example content in a delivered doc.
- Never invent a constraint, source or number to fill a section; write "not known" and list it as an open question.
- Never mix horizons in one document.
- Never keep a template's section that has nothing to say after a real attempt; delete it.

## Provenance and maintenance

Updated: 2026-11-14. Source for the horizon templates and `model.md`: the Planning Horizons paper; the paper wins on disagreement.

Re-verification commands:
```bash
head -2 plugins/techdocs/skills/doc-templates/references/templates/*.md | grep -c '^type:'
sh plugins/techdocs/skills/writing-style/scripts/lint-prose.sh plugins/techdocs/skills/doc-templates/references/templates/*.md
```
