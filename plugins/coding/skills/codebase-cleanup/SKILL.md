---
name: codebase-cleanup
tier: workflow
description: >
  Find what to remove, simplify or update, fix the small parts, file the rest.
  Load for "clean up this codebase", "simplify this", "what can we delete", "is
  this over-engineered", outdated or half-finished code. Do NOT load for a
  report with no edits (project-evaluation) or one diff (review-rubric).
trigger: /codebase-cleanup
---

# /codebase-cleanup

Complexity is a cost paid for a purpose. This skill finds code whose purpose is gone or never arrived, proves it with evidence, removes the cheap cases now and files the rest. The target is the smallest change that preserves existing behaviour.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| A structural assessment and refactor sequence, with no edits | `project-evaluation` |
| Cleanliness of one diff | `review-rubric` |
| One question about how code works | `codebase-search` |
| A failure needs a cause | `forensics` |
| Carrying out one filed cleanup task | `do-work` |
| Deciding what the project should become | `product-direction` |

## Model split

| Work | Runs on |
|---|---|
| Direction, complexity budget, verdicts, the fix-or-file sort, the final report | The strongest model available, in the main session. When the session runs on a lesser one, name the change for the user before step 2 |
| Mechanical evidence gathering: greps, counts, build and deprecation output | A cheap agent, briefed per `agent-brief` |
| Applying fixes | Executors and the reviewer, at the tiers `do-work` assigns |

## Procedure

1. **Scope and baseline.** Name the project or module and the commit (`git rev-parse HEAD`). Take the baseline as `do-work` defines it. On a red baseline, report and stop: a cleanup on a failing suite cannot show it preserved behaviour.
2. **Read the direction.** Open, in-progress and blocked tasks via `tracker`, and the vision, requirements, design and architecture docs via `project-map`. Ask nothing the repo answers.
3. **Write the complexity budget.** One line per area: the complexity it carries, and the future task or target-architecture element that pays for it, or "none". An area with a named payer keeps its seams, extension points and abstractions. An area with none is held to what the code does today.
4. **Sweep.** Run the lenses below, reading per `codebase-search`. Start from the findings of a current `project-evaluation` report when the `investigations` key holds one; do not re-measure what it measured.
5. **Give each candidate a verdict.** `remove`, `simplify`, `update`, `complete` or `keep`. `keep` names its payer from the budget. A candidate with no evidence is dropped, not softened.
6. **Sort into fix or file** with the bar below.
7. **Apply the fixes** as one `do-work` batch: one commit per fix, one verify, one review. Executors load `backend-code` or `frontend-ui` by the files touched.
8. **File the rest** via `tracker`, one task per finding: the evidence, the smallest change that preserves behaviour, a done-when, and the tasks it blocks or depends on.
9. **Report** per `run-report`: fixed, filed, kept with the payer, and what was not examined.

## Lenses

| Lens | Looks for | Evidence |
|---|---|---|
| Unearned complexity | Single-implementation abstractions, config flags with one value, layers that only forward, options no caller sets | Reference counts, call sites, the budget line showing no payer |
| Duplicated logic | Near-identical blocks, parallel implementations, re-derived constants | Duplication tool output or grep, with both locations |
| Stale assumptions | Workarounds for fixed bugs, guards for states that cannot occur, compatibility paths for removed callers or formats, comments and docs the code contradicts | The removed caller or fixed version, a test or type that excludes the state, drift verdicts per `codebase-search` |
| Outdated | Deprecated language, framework or library features; dependencies past end of support; patterns the project has replaced elsewhere | Compiler, linter and package-manager warnings with the command; the dependency's own release notes |
| Incomplete | Stubs, placeholder returns, half-wired flags, unreachable branches, commented-out blocks, to-do markers | `file:line`; the open task that will finish it, or none |
| Dead code | Unreferenced exports, files, scripts and settings; expired scripts per `ops-scripts` | Reference search, coverage output |

An incomplete bit with an open task stays and is noted on that task. One with no task is either removed or filed for completion; the stub policy in `validation-and-qa` decides whether it may remain meanwhile.

## Fix or file

A finding is fixed now only when every line holds:

| Test | Bar |
|---|---|
| Behaviour | Unchanged for every caller, public interface included |
| Size | The small flow of `do-work`: one file, about 50 lines or fewer |
| Proof | Existing tests cover the touched code, or the change is a pure deletion of unreferenced code |
| Direction | No open task or plan touches the same lines |
| Certainty | The evidence is fact, not inference |

Anything else is filed. Code with no test around it is filed with a characterisation test as its first step. Cap one run at about ten fixes; file the remainder so the review stays readable.

## Hard rules

- Never decide direction here. A conflict between code and target architecture goes to `product-direction`.

## Provenance and maintenance

Updated: 2026-11-27.

Re-verification commands:
```bash
ls plugins/coding/skills/project-evaluation/SKILL.md plugins/coding/skills/do-work/SKILL.md plugins/punchcard/skills/run-report/SKILL.md
grep -n "codebase-cleanup" plugins/coding/skills/project-evaluation/SKILL.md plugins/punchcard/skills/capability-check/SKILL.md README.md
```
