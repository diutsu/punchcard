---
name: project-doctor
tier: leaf
description: >
  Check a repo is set up for this marketplace: project map paths, scripts
  folder, changelog, docs layout and frontmatter, task tool; pass or fail with
  the fix. Load when onboarding or restructuring a repo, or when a skill cannot
  resolve a location. Do NOT load to fix the docs or tasks.
trigger: /project-doctor
---

# /project-doctor

Run three checks, report each as pass or fail with the one-line fix, and change nothing unless the user asks.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Docs fail the criteria and need fixing | `docs-management` |
| Tasks need work | `tracker` |
| You need the meaning of a map key | `project-map` |

## Check 1: repo

1. The repo instructions file (`AGENTS.md`, `CLAUDE.md` or `GEMINI.md`, per `project-map`) has one `## Project map` block. Missing block: fail, copy the block from `./templates/AGENTS.md` and fill it in.
2. Every path value in the block exists. List each missing path. Keys absent from the block take their defaults from `project-map`; check that those default paths exist too.
3. The `scripts` folder exists.
4. The `changelog` file exists.
5. The `verify` key is set and its command runs.

## Check 2: docs

1. The `docs` root has the Diataxis folders `tutorials/`, `how-to/`, `reference/`, `explanation/`. A folder with no files is acceptable; a missing folder is a fail.
2. The `investigations`, `prd` and `design` roots exist.
3. Frontmatter and structure criteria belong to `docs-management`. Apply them as written there and report its findings. Do not restate them here.

## Check 3: task management

1. The `tasks` key is set.
2. Listing open tasks via `tracker` succeeds.
3. The `tasks-workflow` key is set, in the project map or the user's global instructions, and its file exists.
4. The tracker has the status the workflow file maps to each state `tracker` names.

## Report

```
repo:  PASS | FAIL - <missing item> - fix: <one line>
docs:  PASS | FAIL - <finding> - fix: <one line>
tasks: PASS | FAIL - <finding> - fix: <one line>
```

Offer the fixes as a batch through the question interface, recommended option first.

## Hard rules

- Never modify the repo while diagnosing. Report first.
- Never guess a path. Resolve it through the map.
- Never restate the docs criteria or the task rules. Defer to `docs-management` and `tracker`.
- Never report a check as passed without running it.

## Provenance and maintenance

Updated: 2026-11-26.

Re-verification commands:
```bash
grep -n '^## Project map' plugins/punchcard/skills/project-doctor/templates/AGENTS.md
ls plugins/punchcard/skills/project-doctor/templates
```
