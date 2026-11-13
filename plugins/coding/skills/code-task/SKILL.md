---
name: code-task
tier: leaf
description: >
  Executor contract for one scoped step: implement one focused code change
  from a brief, follow the code rules, run only the targeted test command,
  commit the step, and return a fixed report block. Load when you are the
  agent carrying out a step briefed by do-work, or doing one well-defined
  change on your own. Do NOT load for scoping, planning or review (see
  do-work), for the code rules themselves (see backend-code), or for task
  bookkeeping (the orchestrator owns it).
trigger: /code-task
---

# /code-task

You implement the change in your brief, check it with the targeted test command, and return the report block. You do not manage tasks, expand scope or review your own work.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Scoping, planning, gating a task | `do-work` |
| Code quality, module boundaries, comment rules | `backend-code` (load alongside) |
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

- Never claim tests pass without running the command in this session and seeing exit 0.
- Never change files outside the brief's scope.
- Never edit docs or the changelog unless the brief says so; report the need under `ISSUES SPOTTED`.
- Never mark tasks done; the orchestrator closes them.
- Never improvise around a broken plan assumption; report `PLAN-INVALID`.

## Provenance and maintenance

Updated: 2026-11-13 (docs rules removed; docs are committed and the brief says who edits them).

Re-verification commands:
```bash
grep -c "FILES CHANGED" plugins/coding/skills/code-task/SKILL.md
grep -n "code-task" plugins/coding/skills/do-work/SKILL.md
```
