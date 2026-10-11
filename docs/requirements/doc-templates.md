---
type: requirement
state: done
created: 2026-10-11
updated: 2026-10-11
cross-file-references: [docs/architecture.md, docs/requirements/_index.md, skills/docs-management/SKILL.md, skills/operator-instructions/SKILL.md, skills/migrate-project-docs/SKILL.md]
---
# Requirements — `doc-templates`
Contract for the project documentation starter files under `doc-templates/`.

## Responsibilities & boundaries

- Provides a copy-ready `CLAUDE.md` and `docs/` tree that implements the v2 documentation contract out of the box.
- Serves as the structural target for `skills/migrate-project-docs/SKILL.md`.

## Behavioral invariants

- **Root visibility:** Only `tasks.md`, `done.md`, `next-session-prompt.md`, `operator-instructions.md`, `architecture.md`, `usage.md`, and `progress-log.md` sit at `doc-templates/docs/`.
- **Subfolder isolation:** Module requirements, domain logic, investigations, and ephemeral plans live under `requirements/`, `logic/`, `investigations/`, and `plans/` respectively.
- **Strict ceilings:** `next-session-prompt.md` stays $\le 40$ lines; `plans/_template.md` enforces $\le 150$ lines and phase roll-forward; `operator-instructions.md` contains only `## Run queue` and `## Decision gates`.
- **Frontmatter validity:** Every `.md` file under `doc-templates/docs/` includes valid 5-field YAML frontmatter (`type`, `state`, `created`, `updated`, `cross-file-references`).
