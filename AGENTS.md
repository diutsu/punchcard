# punchcard — Agent Instructions

> **One-liner:** `diutsu`'s shared agent setup as a multi-harness plugin marketplace (`https://github.com/diutsu/punchcard`): house rules, skills and agents for Claude Code, Antigravity and Codex.
> **Lifecycle stage:** `structured`

## Project map

- tasks:: kaneo (project `CLAUDE`)
- docs:: docs/
- investigations:: docs/investigations/
- prd:: docs/prd/
- design:: docs/design/
- scripts:: ops/scripts/
- changelog:: CHANGELOG.md
- worktrees:: ../punchcard.worktrees/
- verify:: the commands in section 2

## 1. Repository layout

| Path | What it is | When to edit |
|---|---|---|
| `.claude-plugin/marketplace.json` | Claude Code marketplace manifest | When adding, renaming or removing a plugin |
| `.agents/plugins/marketplace.json` | Codex marketplace manifest | When adding, renaming or removing a plugin |
| `.agents/plugins.json` | Antigravity workspace plugin discovery | When changing plugin roots or exclusions |
| `plugins/punchcard/` | Always-on base: output style (`output-styles/punchcard.md` synced to `rules/AGENTS.md`), session card + SessionStart hooks (`hooks/hooks.json` and `hooks.json`), task intake, question, briefing and skill-upkeep skills | When changing how the agent behaves in every session |
| `plugins/coding/` | The work loop (`do-work`), its execution `plan` and `intent-check`, its leaf skills per work type, investigation skills, and the `reviewer` and `suite-runner` agents | When changing how code is written, reviewed, investigated or operated |
| `plugins/techdocs/` | Writing style, doc templates, Diataxis layout, sourced research | When changing how docs are written or laid out |
| `plugins/project-management/` | Tasks in the tracker, what's next, prioritisation, backlog review, bug reports, and the product-direction session; names no tracker | When changing task handling |
| `plugins/wip/` | Draft skills from `skill-reviewer` and draft agents, awaiting promotion | Drafts only |
| `docs/` | This repository's own docs, committed, in the Diataxis layout | When the structure or a contract changes |

## 2. Verification gate commands

Run these before completing any task in this repository:

```bash
# 1. Cross-harness manifests parse cleanly, agree across harnesses, and rules/AGENTS.md is in sync
python3 plugins/punchcard/scripts/sync_rules.py --check

# 2. Claude Code marketplace and every plugin manifest are valid (when claude CLI is installed)
claude plugin validate .

# 3. Every skill has the required frontmatter and sections (no output = pass)
find plugins/{punchcard,coding,techdocs,project-management,wip}/skills -name SKILL.md -exec grep -L '^name:' {} +
find plugins/{punchcard,coding,techdocs,project-management,wip}/skills -name SKILL.md -exec grep -L '^tier:' {} +
find plugins/{punchcard,coding,techdocs,project-management,wip}/skills -name SKILL.md -exec grep -L '^trigger:' {} +
find plugins/{punchcard,coding,techdocs,project-management,wip}/skills -name SKILL.md -exec grep -L '^## Hard rules' {} +

# 4. No Claude-only path variable leaks in plugins (no output = pass)
grep -rn '\${CLAUDE_SKILL_DIR}' plugins/

# 5. No tracker is named outside its own plugin (no output = pass)
grep -rniE 'ctask|kaneo' plugins/punchcard/skills plugins/coding plugins/techdocs plugins/project-management/skills | grep -v 'grep -rn'

# 6. Every doc carries the frontmatter contract (no output = pass)
grep -rL '^type:' docs/explanation docs/reference docs/how-to docs/tutorials docs/investigations docs/prd docs/design 2>/dev/null
```

## 3. Authoring non-negotiables

- **Skill contract:** every `plugins/<plugin>/skills/<name>/SKILL.md` has YAML frontmatter (`name`, `tier: leaf | workflow | reference`, `description`, `trigger`), `## When NOT to use this skill`, `## Hard rules`, and `## Provenance and maintenance`. `skill-maintenance` holds the full contract.
- **No hardcoded locations or tools:** a skill names a project-map key or says "via `tracker`". Only a tracker's own plugin names it.
- **One fact, one home:** reference a sibling skill by name; never restate its mechanics. A file is never referenced across plugin folders.
- **Backtick angle-bracket placeholders:** any `<placeholder>` in prose outside code fences or YAML frontmatter is wrapped in backticks.
- **Drafts from `skill-reviewer` start in `wip`:** they land in `plugins/wip/` and move to another plugin only after promotion per `skill-maintenance`. A skill the user asks for goes into the plugin that owns its territory.
- **Third-party plugins are never vendored:** they are entries in `plugins/punchcard/skills/watchlist/references/watchlist.md`.
