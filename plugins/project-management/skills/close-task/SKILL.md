---
name: close-task
tier: workflow
description: >
  Judge what is left over from a task against its intention, not its wording:
  each leftover is either part of the task and gets done before the close, or
  a separate concern that gets its own task. The agent decides; it does not
  ask the user. Load from the end of the execute step in do-work, and again
  before the task is closed. Do NOT load to close old tasks in bulk (see
  triage-close), to file a defect the change did not cause (see bug-report),
  or to rank the new tasks (see prioritise).
trigger: /close-task
---

# /close-task

Two failures to prevent: stopping short because finishing means touching other files or covering more cases, and asking the user about every loose end. Decide, act, report.

It runs twice per task, so the single suite run and single review of `do-work` cover the added work:

- **Pass 1, after the last execute step and before verify.** Classify, then turn in-scope items into plan steps.
- **Pass 2, before the close.** Re-check only what verify, review and docs exposed.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Closing many open tasks against the code | `triage-close` |
| A defect the change did not cause | `bug-report` |
| Ordering the follow-ups | `prioritise` |
| Proving the work meets done-when | `validation-and-qa` |

## Procedure

1. **Anchor the intention.** Read the task via `backlog` `show`; with no task, take the user's request. Write one sentence that paraphrases its goal and done-when, and record it via `backlog` `annotate`. Do not widen the goal.
2. **Collect leftovers.** Skipped cases, files the change implies but no step named, docs and tests the change made stale, reviewer notes not applied, things noticed during the work.
3. **Classify each by the intention test.** Ask: if this stays undone, is the goal unmet, or is something this change touched now wrong or inconsistent?

   | Class | Signs | Action |
   |---|---|---|
   | In scope | Yes to the test, and you can cite the goal clause it serves or the changed line that made it necessary | Add it as a plan step per `plan` and continue `do-work` from there |
   | Separate concern | No to the test. It has its own goal and value, and the task is correct without it. Includes the same behaviour elsewhere that this change did not create | File a task via `backlog`, with refs and a link to this task |
   | Defect the change did not cause | A failure found on the way | `bug-report` |
   | Not worth a task | A nit with no user-visible effect | List it in the closing report; file nothing |
   | Needs the human | Only the user can run or decide it | In scope: the review gate in `backlog`. Otherwise: an open question per `backlog` |

   "It needs changes in other files" and "it adds cases" are never reasons to defer. Size is not one either: a large part of the task is still the task.
4. **Settle doubt without asking.** Treat an unclear item as in scope when leaving it would let a user hit the original problem again, or a new one the change introduced. Otherwise it is a separate concern. A `bug-report` expectation question is not a classification question; it goes in the end-of-work batch.
5. **Pass 2 limit.** Classify at most twice per task: pass 1, and pass 2 over what the work exposed. Items found in pass 2 get their targeted tests and a delta review per `review-rubric`, not a second full suite. If an in-scope item still remains, leave the task open, record it in details via `backlog` `edit`, and report it.
6. **Close** via `backlog` once nothing in scope is open. The closing line states what was added to meet the intention, and each task filed with its id.

## Hard rules

- Never close with an in-scope item open.
- Never defer an item because it touches other files, or covers more cases.
- Never ask the user to classify a leftover; decide and report.
- Never pull in a pre-existing instance of a problem this change did not create.
- Never fold a separate concern into the task to keep the list short.
- Never edit the task's goal to match what was built.

## Provenance and maintenance

Updated: 2026-11-14.

Re-verification commands:
```bash
for s in backlog do-work validation-and-qa triage-close bug-report prioritise plan review-rubric; do ls -d plugins/*/skills/$s >/dev/null || echo "missing $s"; done
grep -n 'close-task' plugins/coding/skills/do-work/SKILL.md plugins/project-management/skills/triage-close/SKILL.md README.md
```
