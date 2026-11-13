---
name: skill-maintenance
tier: leaf
description: >
  How the punchcard skill library is organised and kept free of drift: where a
  rule belongs, the skill anatomy contract, split, merge and retire heuristics,
  and promotion from `wip`. Load when authoring or editing a SKILL.md, auditing
  skills for overlap or stale paths, deciding whether a rule belongs in the
  session card, a skill or a project CLAUDE.md, or promoting a draft. Do NOT
  load to run a task governed by another skill.
trigger: /skill-maintenance
---

# /skill-maintenance

Every skill earns its context budget. One fact lives in one home, siblings refer to each other by name, and project-specific facts stay out of marketplace skills.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Mining past sessions for new skills | `skill-reviewer` |
| Tracking a third-party plugin | `watchlist` |
| Writing a project's docs | `docs-management` |
| Running a task | `do-work` |

## 1. Placement layers

Decide where a rule goes before writing it.

| Layer | Home | Holds |
|---|---|---|
| Always on | Output style and session card in the `claude` plugin | Response style and the short house rules loaded every session |
| Triggered procedures | `plugins/<plugin>/skills/<name>/SKILL.md` | Workflows, leaf procedures and reference sheets, project-agnostic |
| Project facts | The repo `CLAUDE.md` with its Project map, plus the repo docs | Locations, tools, module boundaries, project-specific rules |

A rule that applies to every session and fits in two lines goes on the session card. A rule that applies to a kind of work goes in a skill. A rule that names a path, a tool or a module goes in the project.

## 2. Territory per plugin

- `claude`: how Claude works with this user: style, house rules, asking, briefing, queues, away runs, reports and skill upkeep.
- `coding`: doing and reviewing code work, tests, scripts, ops, data and experiment discipline.
- `techdocs`: writing, structuring and reviewing technical documents.
- `project-management`: tasks, plans, priorities, closing and progress.
- `wip`: drafts only, never relied on.

## 3. Skill anatomy

Every `SKILL.md` has:

1. Frontmatter: `name` (equal to the folder), `tier: leaf | workflow | reference`, a `description` stating when to load and when not to, and `trigger: /<name>`.
2. `## When NOT to use this skill`, a table naming the sibling that owns adjacent work.
3. An imperative body. Prefer tables and numbered steps. Wrap every `<placeholder>` in prose in backticks.
4. `## Hard rules`, flat imperatives.
5. `## Provenance and maintenance`, with a date and runnable check commands.

Tiers: a **leaf** runs one intent and loads no sibling to orchestrate. A **workflow** composes leaves and agents by name and never restates their mechanics. A **reference** is consulted, not stepped through.

Aim for 60-110 lines. Move long lists and templates to `references/` or `templates/` inside the skill folder and point to them with `${CLAUDE_SKILL_DIR}/...`. Never reference a file across plugin folders.

## 4. Composition rules

- **Name capabilities and map keys, never paths or tools.** Resolve locations through `project-map`. A hardcoded path or tool name is a fork waiting to drift.
- **Never restate a sibling's mechanics.** Write "per `<skill>`" and stop. A skill that copies another skill's steps goes stale silently when the original changes.
- **Split by trigger family, not by mechanical step.** Commit, describe, push is one intent. Replying to review comments days later is another.
- **Treat skill names as a public interface.** When renaming, leave a one-line stub under the old name that points at the new one, then remove it after one release.
- **Third-party skills run with your permissions.** Read the full text before installing. Track them in `watchlist`, never copy them in without review.

## 5. Split, merge, retire

- **Split** when one description needs two unrelated trigger families, or when workflow mechanics mix with reference standards.
- **Merge** when a skill shrinks to a paragraph nobody loads alone.
- **Retire** when a skill is unused across several sessions or a sibling now covers it. Remove it and drop references to it in the same change.

## 6. Promotion from `wip`

1. The user approves the draft.
2. Move it to the owning plugin's `skills/` folder with `git mv`.
3. Check the anatomy, run the commands below, and remove the evidence block's private detail if any slipped in.
4. Delete the draft folder from `wip`.

## Hard rules

- Never restate another skill's mechanics. Cross-reference by name.
- Never embed an unquoted `<placeholder>` in prose outside code fences and frontmatter.
- Never hardcode a project path or tool in a marketplace skill.
- Never edit an installed copy of a skill. Edit the source in the repo.
- Never add a skill without checking that no sibling already owns the territory.

## Provenance and maintenance

Updated: 2026-11-13. Composition rules adapted from the earlier note on composing workflow skills over central skills.

Re-verification commands:
```bash
grep -L '^name:' plugins/*/skills/*/SKILL.md
grep -L '^tier:' plugins/*/skills/*/SKILL.md
grep -L '^## Hard rules' plugins/*/skills/*/SKILL.md
grep -rn 'docs/tasks.md\|ctask ' plugins/coding plugins/techdocs plugins/claude
```
