---
name: project-map
tier: reference
description: >
  The single place a project declares where things live and which tools own
  them: task tool, docs roots, scripts folder, changelog, verification
  commands, worktree location. Consult BEFORE writing any file whose location
  another skill describes as "per the project map", before any task
  operation, and when a repo has no map yet. Do NOT load to learn how to write
  the doc or run the task tool itself (see the skill that owns that work).
trigger: /project-map
---

# /project-map

Skills in this marketplace never hardcode a path or a tool. They name a map key, and the project's instructions file (`AGENTS.md`, `CLAUDE.md` or `GEMINI.md`) resolves it. A rule about where files go lives here once, not in every skill.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Deciding which Diataxis folder a doc belongs in | `docs-management` |
| Listing, prioritising or closing tasks | the `project-management` plugin |
| Checking that a repo is set up correctly | `project-doctor` |

## The block

Each project carries one `## Project map` section of `key:: value` lines in its root instructions file — check `AGENTS.md`, `CLAUDE.md` and `GEMINI.md` in that order and use the first one with the block. When creating a new file, use `AGENTS.md`. A missing key takes the default.

```markdown
## Project map

- tasks:: <tracker and project, such as jira (project KEY)>
- docs:: docs/
- investigations:: docs/investigations/
- prd:: docs/prd/
- design:: docs/design/
- scripts:: ops/scripts/
- changelog:: CHANGELOG.md
- worktrees:: ../<repo>.worktrees/
- verify:: <command that must pass before work is called done>
```

| Key | Meaning | Default | Owner |
|---|---|---|---|
| `tasks` | Task tracker, with the project or board in it. All task state lives there. | none; ask the user | `project-management` |
| `docs` | Root of committed technical docs, laid out as `tutorials/`, `how-to/`, `reference/`, `explanation/`. | `docs/` | `docs-management` |
| `investigations` | Forward-looking research and forensic reports. | `docs/investigations/` | `techdocs`, `coding` |
| `prd` | Product and logic requirements. | `docs/prd/` | `techdocs` |
| `design` | Target architecture and design docs for things not built yet. | `docs/design/` | `techdocs` |
| `scripts` | One-off and maintenance scripts. | `ops/scripts/` | `ops-scripts` |
| `changelog` | Changelog file. | `CHANGELOG.md` | `changelog` |
| `worktrees` | Where git worktrees are created. | `../<repo>.worktrees/` | `repo-infra` |
| `verify` | Verification gate commands, one per line if several. | none; ask the user | `validation-and-qa` |

A value may be a path outside the repo, such as a vault folder. Files under such a path are never committed to the project repo.

## Procedure

1. Read the `## Project map` section from the first of `AGENTS.md`, `CLAUDE.md` or `GEMINI.md` at the repo root that has one.
2. Resolve the key the calling skill named. Use the default when the key is absent and a default exists.
3. If the key has no default and no value, ask the user through the question interface, then add the line to the map.
4. Write the file, or run the tool, at the resolved location only.

## Hard rules

- Never write a file to a location a skill guessed. Resolve the map key first.
- Never read or change tasks directly. Go through `backlog`.
- Never restate a map default inside another skill. Name the key.
- Never create a second map. One block, in the repo instructions file (`AGENTS.md`, `CLAUDE.md` or `GEMINI.md`).

## Provenance and maintenance

Updated: 2026-11-25.

Re-verification commands:
```bash
grep -n '^## Project map' AGENTS.md
grep -rniE 'ctask|kaneo' plugins/coding plugins/techdocs plugins/punchcard
```
