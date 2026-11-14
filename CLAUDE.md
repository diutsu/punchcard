# punchcard — Agent Instructions

> **One-liner:** `diutsu`'s shared Claude setup as a plugin marketplace (`https://github.com/diutsu/punchcard`): house rules, skills and agents that would otherwise live in a personal `~/.claude`.
> **Lifecycle stage:** `structured`

## Project map

- tasks:: ctask
- docs:: docs/
- investigations:: docs/investigations/
- prd:: docs/prd/
- design:: docs/design/
- scripts:: ops/scripts/
- changelog:: CHANGELOG.md
- worktrees:: ../punchcard.worktrees/
- operator-queue:: ops/local/operator-queue.md
- handoff:: ops/local/handoff.md
- verify:: the commands in section 2

## 1. Repository layout

| Path | What it is | When to edit |
|---|---|---|
| `.claude-plugin/marketplace.json` | The marketplace manifest | When adding, renaming or removing a plugin |
| `plugins/claude/` | Always-on base: output style, session card, question, briefing, operator-queue and skill-upkeep skills, watchlist | When changing how Claude behaves in every session |
| `plugins/coding/` | The work loop (`do-work`), its leaf skills per work type, investigation skills, and the `reviewer` and `suite-runner` agents | When changing how code is written, reviewed, investigated or operated |
| `plugins/techdocs/` | Writing style, doc templates, Diataxis layout, sourced research | When changing how docs are written or laid out |
| `plugins/project-management/` | Backlog, prioritisation, triage, plans; the only place that names the task tool | When changing task handling or adding a task-tool adapter |
| `plugins/wip/` | Draft skills from `skill-reviewer`, awaiting promotion | Drafts only |
| `plugins/local-project-manager/` | Temporary: holds only `migrate-project-docs` | Do not edit; it is removed when the remaining migrations finish |
| `docs/` | This repository's own docs, committed, in the Diataxis layout | When the structure or a contract changes |

## 2. Verification gate commands

Run these before completing any task in this repository:

```bash
# 1. The marketplace and every plugin manifest are valid
claude plugin validate .

# 2. Every skill has the required frontmatter and sections (no output = pass)
grep -L '^name:' plugins/{claude,coding,techdocs,project-management,wip}/skills/*/SKILL.md
grep -L '^tier:' plugins/{claude,coding,techdocs,project-management,wip}/skills/*/SKILL.md
grep -L '^trigger:' plugins/{claude,coding,techdocs,project-management,wip}/skills/*/SKILL.md
grep -L '^## Hard rules' plugins/{claude,coding,techdocs,project-management,wip}/skills/*/SKILL.md

# 3. The task tool is named only inside project-management (no output = pass)
grep -rln 'ctask' plugins/claude/skills plugins/coding plugins/techdocs | grep -v -e project-map -e skill-maintenance -e project-doctor

# 4. Every doc carries the frontmatter contract (no output = pass)
grep -rL '^type:' docs/explanation docs/reference docs/how-to docs/tutorials docs/investigations docs/prd docs/design 2>/dev/null

# 5. The task registry is valid (local file; skip on a checkout without one)
ctask --file ops/local/tasks.md --done-file ops/local/done.md validate
```

## 3. Authoring non-negotiables

- **Skill contract:** every `plugins/<plugin>/skills/<name>/SKILL.md` has YAML frontmatter (`name`, `tier: leaf | workflow | reference`, `description`, `trigger`), `## When NOT to use this skill`, `## Hard rules`, and `## Provenance and maintenance`. `skill-maintenance` holds the full contract.
- **No hardcoded locations or tools:** a skill names a project-map key or says "via `backlog`". Only `project-management` names the task tool.
- **One fact, one home:** reference a sibling skill by name; never restate its mechanics. A file is never referenced across plugin folders.
- **Backtick angle-bracket placeholders:** any `<placeholder>` in prose outside code fences or YAML frontmatter is wrapped in backticks.
- **New skills start in `wip`:** drafts from `skill-reviewer` land in `plugins/wip/` and move to another plugin only after review.
- **Third-party plugins are never vendored:** they are entries in `plugins/claude/skills/watchlist/references/watchlist.md`.
