---
name: review-rubric
tier: reference
description: >
  The scoring rubric for plans and implementations: dimensions, 0-10 scale,
  minimum-wins mechanics, blocking cap, pass bar, issue tags, delta re-review,
  quick-fix limits, second-look rule and the exact verdict format. Load before
  scoring or reviewing any plan or diff, whether as the author self-scoring or
  as the `reviewer` agent, and when deciding how much review a change needs.
  Do NOT load to run the work loop (see do-work) or to decide what counts as
  evidence of done (see validation-and-qa).
trigger: /review-rubric
---

# /review-rubric

One rubric scores both plans and implementations. The author self-scores small work. The `reviewer` agent scores larger work. Both use the same dimensions and the same verdict.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Driving a task through the loop and its gates | `do-work` |
| What evidence proves done, and the stub policy | `validation-and-qa` |
| Code quality rules the diff is judged against | `backend-code`, `frontend-ui` |
| Reviewing a running app's UX | `interactive-app-review` |

## Plan dimensions (0-10 each)

- **Completeness.** Every affected file, module and edge case is named.
- **Correctness.** The plan respects module boundaries, allowed dependencies and project conventions.
- **Risk, rollback, tests.** Failure modes are named, the test strategy is explicit, and steps are small enough to roll back one at a time.
- **Clarity.** An agent with no other context could run each step without ambiguity.
- **Proportionality.** The plan is neither over- nor under-engineered.
- **Fitness.** The plan covers the whole task and nothing but the task. Unrequested extras fail this dimension.

## Implementation dimensions (0-10 each)

- **Faithfulness.** The diff matches the plan and meets every acceptance criterion, with no scope creep. A deviation passes only when documented and justified.
- **Style.** The diff matches project style, architecture and framework use.
- **Tests.** New behaviour and edge cases have tests. The suite shows no regression against the baseline.
- **Cleanliness.** No dead or duplicated code, leftover scaffolding or commented-out blocks.
- **Docs.** Docs that describe changed behaviour are updated in the same pass, and the changelog line exists when the change is user-visible.

## Mechanics

- Final score = the minimum dimension score. Never the average.
- Any blocking issue caps the final score at 6.
- Pass at 9 or above.
- Tag every issue `blocking`, `major` or `minor`.
- A stub, mock or fabricated value presented as done is always blocking.
- An empty issue list with a low score, or a blocking issue with a 9, is an invalid review. Redo it.
- Score against the rubric, not against effort.

## Verdict format

```
ISSUES:
1. [blocking|major|minor] <location> - <why it matters> - <concrete fix>
(or: none)

QUICK FIXES APPLIED:
1. <file:lines> - <what changed>
(or: none)

DIMENSION SCORES:
<dimension>: N/10

FINAL SCORE: N   (= min dimension, capped at 6 if any blocking issue)
VERDICT: PASS (>=9) | FAIL
```

List blocking issues first, then major, then minor. A delta review prefixes the verdict with `RESOLVED:` and `STILL OPEN:` lists for the earlier issues.

## Quick fixes

The `reviewer` applies a fix itself, instead of reporting it and waiting, when all of these hold:

- The fix is local and mechanical.
- It changes no behaviour and no design.
- It is about 20 lines or fewer.
- The targeted tests still pass afterwards.

Examples: a dead import, a misleading comment, a missing test assertion, a naming slip. List every fix under `QUICK FIXES APPLIED`. Return anything larger as an issue for an executor.

## Second look

- Lines the reviewer wrote are checked by one fresh `reviewer` instance, the grader. It scores only the reviewer's fix diff and makes no edits.
- Executor fixes made after review get a delta review by the original reviewer, over the changed parts only.
- Nothing is graded twice. Every changed line is seen by its author and one clean reviewer.

## Delta re-review

1. For each earlier issue, read the changed lines and mark it `resolved` or `still open`. Never accept the caller's word.
2. Scan only the changed parts for damage the fixes introduced.
3. Re-score only the dimensions the fixes affect. Carry the rest forward. The same mechanics apply.

## Right-sizing

| Change | Review |
|---|---|
| One file, about 50 lines or fewer | The author self-scores against the implementation dimensions and fixes before completing. |
| Several steps, module boundaries touched, or a contested self-score | A separate `reviewer` over the whole diff range. |

The self-score uses the same verdict format and the same pass bar. A self-score of 9 or above with an honest issue list is a pass. The author cannot self-score a stub as done.

## Hard rules

- Never average dimension scores.
- Never pass with an unresolved blocking issue.
- Never show a reviewer or grader the author's reasoning before it scores.
- Never apply a quick fix that changes behaviour, design or more than about 20 lines.
- Never grade the same lines twice.

## Provenance and maintenance

Updated: 2026-11-13 (rubric, quick-fix and second-look rules merged from the earlier reviewer agent and the work loop).

Re-verification commands:
```bash
ls plugins/coding/agents/reviewer.md
grep -n "review-rubric" plugins/coding/agents/reviewer.md plugins/coding/skills/do-work/SKILL.md
```
