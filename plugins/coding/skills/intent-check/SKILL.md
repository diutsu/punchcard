---
name: intent-check
tier: leaf
description: >
  Decide whether the work done matches its intention, not its wording, and
  classify every leftover: in scope (becomes a plan step now), a separate
  concern (a follow-up to file), a defect the change did not cause, a nit, or
  something only the human can do. A decider: it returns a table and changes
  no task. Load from do-work after the last execute step, or after any change
  made without do-work. Do NOT load to check done-when items against evidence
  (see validation-and-qa), to file or close tasks (see tracker), to file a
  defect (see bug-report), or to rank follow-ups (see prioritise).
trigger: /intent-check
---

# /intent-check

Two failures to prevent: stopping short because finishing means touching other files or covering more cases, and asking the user about every loose end. Decide and report; the caller acts on the result.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Checking each done-when item has evidence | `validation-and-qa` |
| Filing, moving or closing a task | `tracker` |
| Filing a defect the change did not cause | `bug-report` |
| Closing many open tasks against the code | `backlog-review` |
| Ordering the follow-ups | `prioritise` |

## Inputs

- **The intention:** the task's goal and done-when, or the user's request when there is no task.
- **The plan** and the diff range it produced.
- **What the work turned up:** the executors' `ISSUES SPOTTED`, deviations from the plan, reviewer notes not applied, things noticed on the way.

## Procedure

1. **Anchor the intention.** Write one sentence that paraphrases the goal and done-when. Do not widen the goal.
2. **Collect leftovers.** Skipped cases, files the change implies but no step named, docs and tests the change made stale, and everything under Inputs.
3. **Classify each by the intention test.** Ask: if this stays undone, is the goal unmet, or is something this change touched now wrong or inconsistent?

   | Class | Signs | The caller |
   |---|---|---|
   | In scope | Yes to the test, and you can cite the goal clause it serves or the changed line that made it necessary | Adds it as a plan step and continues the loop |
   | Separate concern | No to the test. It has its own goal and value, and the work is correct without it. Includes the same behaviour elsewhere that this change did not create | Files it as a follow-up |
   | Defect the change did not cause | A failure found on the way | Files it per `bug-report` |
   | Nit | No user-visible effect | Lists it in the closing report |
   | Needs the human | Only the user can run or decide it | Hands it over per `tracker` |

   "It needs changes in other files" and "it adds cases" are never reasons to defer. Size is not one either: a large part of the task is still the task.
4. **Settle doubt without asking.** Treat an unclear item as in scope when leaving it would let a user hit the original problem again, or a new one the change introduced. Otherwise it is a separate concern.

## Output

```markdown
Intention: `<one sentence>`

| Leftover | Class | Reason | Cites |
|---|---|---|---|
| `<item>` | in scope, separate, defect, nit or needs human | `<one line>` | `<goal clause or changed file:line>` |
```

## Hard rules

- Never file, move, annotate or close a task; return the table.
- Never ask the user to classify a leftover.
- Never defer an item because it touches other files, or covers more cases.
- Never pull in a pre-existing instance of a problem this change did not create.
- Never fold a separate concern into the work to keep the list short.
- Never restate the intention wider or narrower than the task says.

## Provenance and maintenance

Updated: 2026-11-26.

Re-verification commands:
```bash
for s in tracker do-work validation-and-qa backlog-review bug-report prioritise plan; do ls -d plugins/*/skills/$s >/dev/null || echo "missing $s"; done
grep -n 'intent-check' plugins/coding/skills/do-work/SKILL.md
grep -n 'ISSUES SPOTTED' plugins/coding/skills/code-task/SKILL.md
```
