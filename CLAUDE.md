# punchcard — Agent Instructions

> **One-liner:** Central repository (`https://github.com/diutsu/punchcard`) for `diutsu`'s AI agent skills (`plugins/local-project-manager/skills/`) and project documentation templates (`plugins/local-project-manager/skills/migrate-project-docs/templates/`), installable via `npx skills`.
> **Lifecycle stage:** `structured`

## 1. Repository Layout & Ownership Boundaries

This repository has three distinct top-level directories — **never confuse `plugins/local-project-manager/skills/migrate-project-docs/templates/docs/` with `docs/`**:

| Directory | What it is | When to edit |
|---|---|---|
| `plugins/local-project-manager/skills/<name>/SKILL.md` | Distributable agent skills installed via `npx skills add https://github.com/diutsu/punchcard` | When authoring, updating, or auditing reusable agent skills |
| `plugins/local-project-manager/skills/migrate-project-docs/templates/` | Starter skeleton (`CLAUDE.md` + `docs/`) copied into *other* side projects | When changing the template contract that downstream projects inherit |
| `docs/` | Meta-documentation for **this** repository (`punchcard` itself) | When tracking `punchcard`'s own architecture, tasks (`tasks.md`), or session state |

**Exception:** projects that adopt the v2 framework keep `docs/` local-only (gitignored, own repo). This repository tracks its own `docs/` on purpose, as a readable example of the contract.

## 2. Verification Gate Commands

Run these checks before completing any task in this repository:

```bash
# 1. Validate punchcard's own task registry
ctask validate

# 2. Verify every skill has required frontmatter (name, tier, description, trigger)
grep -L '^name:' plugins/local-project-manager/skills/*/SKILL.md
grep -L '^tier:' plugins/local-project-manager/skills/*/SKILL.md

# 3. Verify all docs in both docs/ and plugins/local-project-manager/skills/migrate-project-docs/templates/docs/ satisfy the v2 frontmatter contract
grep -rL '^type:' docs/ plugins/local-project-manager/skills/migrate-project-docs/templates/docs/
```

## 3. Authoring Non-Negotiables

- **Skill authoring contract:** Every `plugins/local-project-manager/skills/<name>/SKILL.md` must include YAML frontmatter (`name`, `tier: leaf | workflow | reference`, `description`, `trigger`), `## When NOT to use this skill`, `## Hard rules`, and `## Provenance and maintenance`.
- **Backtick angle-bracket placeholders:** Any `<placeholder>` in prose outside code fences or YAML frontmatter must be wrapped in backticks (`` `<placeholder>` ``) so CommonMark/Obsidian never eats it as raw HTML.
- **Sync `plugins/local-project-manager/skills/` and `plugins/local-project-manager/skills/migrate-project-docs/templates/`:** Any change to the v2 documentation contract in `plugins/local-project-manager/skills/docs-management/SKILL.md` or `plugins/local-project-manager/skills/operator-instructions/SKILL.md` must be reflected in `plugins/local-project-manager/skills/migrate-project-docs/templates/` in the same commit.
