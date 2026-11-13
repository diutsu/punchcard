---
name: triage-close
tier: leaf
description: >
  Decide which open tasks can be closed: check each task's done-when against
  the code and git history, classify it done, obsolete, duplicate, partial or
  open, and close the confirmed ones with evidence. Load when the user asks
  to "clean up the backlog", "what can we close", or after a large change
  landed. Do NOT load to rank work (see prioritise), to close the task you
  just finished in do-work (that close goes through backlog directly), or to
  add tasks (see backlog).
trigger: /triage-close
---

# /triage-close

Close tasks only with evidence. This skill reads tasks, code and git history, proposes a batch, and writes after one confirmation.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Choosing the next task | `prioritise` |
| Closing the one task a work session just finished | `backlog` `close`, after `validation-and-qa` evidence |
| Creating or editing a task | `backlog` |
| Recording a milestone for a closed task | `changelog` |

## Method

1. **Select candidates.** `list` open tasks through `backlog`; narrow by module if the user named one. Prefer tasks flagged stale by `prioritise` and tasks whose `refs` changed recently in git.
2. **Check each candidate.** `show` it, then test every done-when criterion:
   - Search the code for the behaviour, test or file named; read the lines.
   - Run `git log` on the task's refs and on its id; read the commits.
   - Run the cheapest command that proves a criterion when one exists (a test, a grep, a query).
3. **Classify.**

| Class | Meaning | Action |
|---|---|---|
| done | Every criterion met | close |
| obsolete | The goal no longer applies | cancel with reason |
| duplicate | Another task covers it | merge into the survivor, close with reason |
| partial | Some criteria met | `edit` details to record what is left |
| open | Nothing met or unclear | leave alone |

4. **Cite evidence.** Each done or obsolete verdict gives a `file:line` or a commit hash. A verdict without a citation becomes "open".
5. **Batch and confirm.** Present the table of proposed closes, cancels, merges and edits. Ask once through the question interface (recommended option first: apply all; then apply done only; then none). Do not close one task at a time.
6. **Write.** Apply the confirmed items with `backlog` (`close`, `edit`, `annotate` for the reason or commit). Then `validate`.

## Output

```markdown
| Task | Class | Evidence | Action |
|---|---|---|---|
| `<ID>` | done | `<file:line or commit>` | close |
```

Follow with a count per class and any task you could not judge, with what is missing.

## Hard rules

- Never close a task without a cited `file:line` or commit.
- Never infer "done" from the task title, or from a plan being finished.
- Never close without the batch confirmation, unless the user named the exact tasks to close.
- Never edit a task's goal to make it match the code; record partial progress in details.
- Always `validate` after the batch, and clear blocked-by references the close reports.
- Delete the plan of every closed task (`plan`).

## Provenance and maintenance

Updated: 2026-11-13.

```bash
grep -n 'close\|validate' plugins/project-management/skills/backlog/SKILL.md
```
