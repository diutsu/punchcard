---
type: reference
state: done
created: 2026-10-11
updated: 2026-11-27
cross-file-references: [plugins/punchcard/skills/skill-maintenance/SKILL.md, .claude-plugin/marketplace.json, .agents/plugins/marketplace.json, plugins/punchcard/skills/project-map/SKILL.md]
---

# Skill authoring contract

The structure every `plugins/<plugin>/skills/<name>/SKILL.md` must follow. The full guidance is in the `skill-maintenance` skill.

## Frontmatter

| Field | Rule |
|---|---|
| `name` | Equal to the folder name |
| `tier` | `leaf`, `workflow` or `reference` |
| `description` | 300 characters or fewer: the triggers and the Do NOT load pointers, never a method summary |
| `trigger` | `/<name>` |

## Sections

In order: a `## When NOT to use this skill` table naming the sibling that owns adjacent work, an imperative body, `## Hard rules` as flat imperatives, and `## Provenance and maintenance` with a date, any external source, no history, and runnable check commands.

## Tiers

| Tier | Role |
|---|---|
| `leaf` | Runs one intent and loads no sibling to orchestrate |
| `workflow` | Composes leaves and agents by name and never restates their mechanics |
| `reference` | Consulted during work, never stepped through |

## Placement and size

- Aim for 60 to 110 lines. Move long lists and templates to `references/` or `templates/` inside the skill folder and link to them with relative paths (`./references/...`, `./templates/...`).
- Never reference a file across plugin folders.
- Name map keys and capabilities, never paths or tools. Locations resolve through `project-map`.

## Prose

- Wrap every `<placeholder>` in prose, outside code fences and frontmatter, in backticks. CommonMark reads a bare one as raw HTML, and it renders invisible.
- Follow `writing-style`.

## Registration

Each plugin ships `plugin.json`, `.claude-plugin/plugin.json` and `.codex-plugin/plugin.json`, and appears in `.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json`. Skills in `plugins/*/skills/` are found by `npx skills add`.

## Verification

```bash
python3 plugins/punchcard/scripts/sync_rules.py --check
grep -L '^name:' plugins/*/skills/*/SKILL.md
grep -L '^tier:' plugins/*/skills/*/SKILL.md
grep -L '^## Hard rules' plugins/*/skills/*/SKILL.md
grep -rn '\${CLAUDE_SKILL_DIR}' plugins/
```

Each command prints nothing when every skill complies.
