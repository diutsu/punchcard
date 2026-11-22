---
type: reference
state: done
created: 2026-10-11
updated: 2026-11-22
cross-file-references: [plugins/techdocs/skills/doc-templates/SKILL.md, plugins/techdocs/skills/docs-management/SKILL.md, plugins/punchcard/skills/project-doctor/SKILL.md, plugins/project-management/skills/product-direction/SKILL.md]
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
| Proof-of-concept brief | none | `poc.md` | `investigations` key |
| ADR | none | `adr.md` | `docs` key, `explanation/` |

## Project starter (`punchcard`)

In `plugins/punchcard/skills/project-doctor/templates/`, used by `project-doctor`.

| Path | Purpose |
|---|---|
| `AGENTS.md` | Starter project instructions and Project map block |

## Session read-back (`project-management`)

In `plugins/project-management/skills/product-direction/templates/`, used by `product-direction`.

| Path | Purpose |
|---|---|
| `read-back.md` | The closing summary shown in the conversation: what changed, conflicts settled, when each change is built. Never saved as a file |
