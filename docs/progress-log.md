---
type: log
state: done
created: 2026-10-11
updated: 2026-11-11
cross-file-references: []
---
# Progress Log — punchcard
Curated highlights only — significance bar and template in the `progress-log` skill (`development`, `operation`, `major-product-decision`, `new-feature`, max 250 chars per line, newest first).

- `2026-11-11 12:00` **[major-product-decision]** Renamed Frank to punchcard and turned it into a Claude Code plugin marketplace; skills now live in the `local-project-manager` plugin under `plugins/` (`npx skills` still discovers all 19).
- `2026-10-26 12:00` **[development]** Moved `doc-templates/` into `skills/migrate-project-docs/templates/` so the starter skeleton installs with the skill; repointed all skills and meta-docs at the new path.
- `2026-10-11 21:15` **[new-feature]** Ported 19 general-purpose v2 skills into `skills/`, split `code-task` into `code-task` + `code-discipline` + `write-docs`, and wired `handle-comments` to `operator-instructions.md` decision gates (`SKL-01`).
- `2026-10-11 20:50` **[new-feature]** Scaffolded Frank repository with v2 subfolder doc-templates/, core v2 documentation/workflow skills in skills/, and dogfooded meta-docs in docs/.

