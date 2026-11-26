---
name: code-task
tier: leaf
description: >
  Executor contract for one scoped step: implement the change from a brief, run
  only its targeted tests, commit, return a fixed report. Load when carrying out
  a step briefed by do-work. Do NOT load for scoping, planning or review
  (do-work), code rules (backend-code) or task bookkeeping.
trigger: /code-task
---

# /code-task

You implement the change in your brief, check it with the targeted test command, and return the report block. You do not manage tasks, expand scope or review your own work.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Scoping, planning, gating a task | `do-work` |
| Code quality, module boundaries, comment rules, no task or doc references in code | `backend-code` (load alongside) |
| Front-end view rules | `frontend-ui` |
| What counts as done | `validation-and-qa` |

## Required inputs in the brief

- **What to change:** files, functions and expected behaviour.
- **Done when:** concrete acceptance criteria for this step.
- **Test command:** the exact targeted command, never the full suite unless the brief says so.
- **Skills to load:** the leaf skills the step needs.
- **Prior handoff** when this is step 2 or later.
- **Docs and changelog:** whether the step edits them.

If the test command is missing, or an assumption in the brief is false in the code, stop and report `PLAN-INVALID` with file and line evidence. Do not improvise around it.

## Process

1. Read every file you will change and the code rules the brief names.
2. Make the smallest change that meets the criteria. No drive-by refactors, no unrequested features, no new dependencies.
3. Run the exact test command from the brief.
4. Fix any failure or regression against the baseline before reporting.
5. Commit the step on the current branch, with only this step's files staged by name.
6. Return the report block.

## Report block

```text
Step N of <plan-slug>
FILES CHANGED:
- <path>

TESTS RUN: <exact command>  ->  exit 0  (N passed, vs. baseline)
DEVIATIONS FROM PLAN: <none | what and why>
SUMMARY: <one sentence: what changed and why>
ISSUES SPOTTED:
- <none | path -> out-of-scope issue or risk for the orchestrator>
```

## Hard rules

- Never edit docs or the changelog unless the brief says so; report the need under `ISSUES SPOTTED`.

## Provenance and maintenance

Updated: 2026-11-27.

Re-verification commands:
```bash
grep -c "FILES CHANGED" plugins/coding/skills/code-task/SKILL.md
grep -n "code-task" plugins/coding/skills/do-work/SKILL.md
```
