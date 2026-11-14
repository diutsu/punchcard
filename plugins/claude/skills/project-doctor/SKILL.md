---
name: project-doctor
tier: leaf
description: >
  Validate that a repo is set up for this marketplace in three checks: repo
  (a Project map block whose paths exist, a scripts folder, a changelog), docs
  (Diataxis folders and frontmatter) and task management (the task tool
  responds and its registry validates). Reports pass or fail per check with the
  fix. Load when onboarding a repo, after restructuring one, or when a skill
  cannot resolve a location. Do NOT load to fix the docs or tasks themselves.
trigger: /project-doctor
---

# /project-doctor

Run three checks, report each as pass or fail with the one-line fix, and change nothing unless the user asks.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Docs fail the criteria and need fixing | `docs-management` |
| The registry is invalid or tasks need work | `backlog` |
| You need the meaning of a map key | `project-map` |

## Check 1: repo

1. The repo `CLAUDE.md` has one `## Project map` block (see `project-map`). Missing block: fail, copy the block from `${CLAUDE_SKILL_DIR}/templates/CLAUDE.md` and fill it in.
2. Every path value in the block exists, except `handoff` and `operator-queue`. List each missing path. Keys absent from the block take their defaults from `project-map`; check that those default paths exist too.
3. The `scripts` folder exists.
4. The `changelog` file exists.
5. The `verify` key is set and its command runs.
6. The `handoff` and `operator-queue` paths are ignored by git and not tracked (`git check-ignore` passes, `git ls-files` prints nothing). Either file may be absent: no task in flight, nothing queued.

## Check 2: docs

1. The `docs` root has the Diataxis folders `tutorials/`, `how-to/`, `reference/`, `explanation/`. A folder with no files is acceptable; a missing folder is a fail.
2. The `investigations`, `prd` and `design` roots exist.
3. Frontmatter and structure criteria belong to `docs-management`. Apply them as written there and report its findings. Do not restate them here.

## Check 3: task management

1. The `tasks` key is set.
2. The tool named there responds (run its help or list command).
3. Its registry validates. The validate command and the validity rules belong to `backlog`.
4. No registry, done-log or plan file is tracked by git.

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
- Never restate the docs criteria or the registry rules. Defer to `docs-management` and `backlog`.
- Never report a check as passed without running it.

## Provenance and maintenance

Updated: 2026-11-13.

Re-verification commands:
```bash
grep -n '^## Project map' plugins/claude/skills/project-doctor/templates/CLAUDE.md
ls plugins/claude/skills/project-doctor/templates
```
