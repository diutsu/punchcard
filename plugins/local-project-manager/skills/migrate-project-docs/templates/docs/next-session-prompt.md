---
type: requirement
state: wip
created: 2026-10-11
updated: 2026-10-11
cross-file-references: [docs/operator-instructions.md, docs/tasks.md]
---
# Next-session starting prompt
Rewritten at the end of every session ($\le 40$ lines). Live snapshot only: what is currently in motion, what is blocked on an operator run or decision gate, and any unverified assumption from the last session. **Not a task list, not a queue dump, not a changelog** — `ctask list` owns pending work, `operator-instructions.md` owns operator steps/decisions, and `git log` owns history. Delete an item the moment it resolves.

## Live state

- **Checkout & environment:** `<branch / commit hash>`, tests `<green / baseline count>`.
- **In-flight background work:** `<none | 1-2 lines stating job ID, what it is running, and when to check it>`.
- **Blocked on `operator-instructions.md`:**
  - `<TASK-ID>` — awaiting `<run queue output | decision gate A/B>` in [operator-instructions.md](operator-instructions.md).

## Unfiled observations (triage next session)

- `<none | 1-2 lines describing an observed issue not yet filed in ctask>`
