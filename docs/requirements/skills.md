---
type: requirement
state: done
created: 2026-10-11
updated: 2026-10-11
cross-file-references: [docs/architecture.md, docs/requirements/_index.md, plugins/local-project-manager/skills/docs-management/SKILL.md]
---
# Requirements — `skills`
Contract for distributable agent skills stored under `plugins/local-project-manager/skills/<name>/SKILL.md` and installed via `npx skills add https://github.com/diutsu/punchcard`.

## Responsibilities & boundaries

- Owns every reusable skill directory under `plugins/local-project-manager/skills/<name>/`.
- Must be directly discoverable by `npx skills` from the GitHub repository root.
- Contains zero hardcoded paths to consumer projects; project-specific facts live in each consumer repo's own `CLAUDE.md` and `docs/`.

## Behavioral invariants

- **Required sections:** Every `plugins/local-project-manager/skills/<name>/SKILL.md` contains YAML frontmatter (`name`, `tier`, `description`, `trigger`), `## When NOT to use this skill`, the core runbook, `## Hard rules`, and `## Provenance and maintenance`.
- **One fact, one home:** `workflow`-tier skills compose `leaf`-tier skills by name and never restate leaf mechanics.
- **CommonMark-safe placeholders:** Bare `<placeholder>` tokens in prose are always wrapped in backticks (`` `<placeholder>` ``).
  > **Guardrail:** Unquoted `<tag>` tokens match CommonMark §6.8 raw HTML and render invisible in Obsidian and Markdown viewers.
