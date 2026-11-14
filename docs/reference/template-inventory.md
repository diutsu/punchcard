---
type: reference
state: done
created: 2026-10-11
updated: 2026-11-13
cross-file-references: [plugins/techdocs/skills/doc-templates/SKILL.md, plugins/techdocs/skills/docs-management/SKILL.md, plugins/local-project-manager/skills/migrate-project-docs/SKILL.md]
---

# Template inventory

Every doc and project template the marketplace ships, and where it lives.

## Doc skeletons (`techdocs`)

In `plugins/techdocs/skills/doc-templates/references/templates/`. Destination keys resolve through `project-map`; `references/model.md` defines the horizons.

| Doc type | Horizon | File | Destination |
|---|---|---|---|
| Vision | H6 | `vision.md` | `prd` key |
| Target architecture | H5 | `target-architecture.md` | `design` key |
| Discovery | H3 | `discovery.md` | `investigations` key |
| Technical design | H2 | `design-doc.md` | `design` key until built |
| PRD | none | `prd.md` | `prd` key |
| Research doc | none | `research-doc.md` | `investigations` key |
| ADR | none | `adr.md` | `docs` key, `explanation/` |

## Starter tree (`local-project-manager`, temporary)

In `plugins/local-project-manager/skills/migrate-project-docs/templates/`, used by `migrate-project-docs`.

| Path | Purpose |
|---|---|
| `CLAUDE.md` | Starter project instructions |
| `docs/tasks.md`, `docs/done.md` | Task registry and done log |
| `docs/next-session-prompt.md` | Live snapshot, at most 40 lines |
| `docs/operator-instructions.md` | Run queue and decision gates only |
| `docs/architecture.md`, `docs/usage.md`, `docs/progress-log.md` | Root docs |
| `docs/requirements/`, `docs/logic/` | Index and template per folder |
| `docs/investigations/_template.md` | Investigation skeleton |
| `docs/plans/_template.md` | Plan skeleton, at most 150 lines with phase roll-forward |


## Contract

Every `.md` under the starter `docs/` carries the five-field frontmatter from `docs-management`.

```bash
grep -rL '^type:' plugins/local-project-manager/skills/migrate-project-docs/templates/docs/
```
