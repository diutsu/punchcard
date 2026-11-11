---
type: requirement
state: wip
created: 2026-10-11
updated: 2026-10-11
cross-file-references: [docs/usage.md, docs/tasks.md]
---
# Operator Instructions
Worklist of actions that **only the human operator** can execute or decide. Once an item is executed or decided, fold the outcome into permanent docs (`requirements/`, `logic/`, `usage.md`) or `ctask`, and **delete the section from this file**.

> **Hard rules for agents:**
> 1. **No status reports or diagnostic essays.** Never use this file to narrate what you checked, log live queue counts, or write multi-paragraph analysis.
> 2. **No permanent runbooks.** Reusable operational procedures ("how to start/stop jobs", "how to enqueue tasks") belong in [usage.md](usage.md), never here.
> 3. **Binary exit on block:** If a task is blocked on a command below or a decision gate, write the entry, set `ctask edit <ID> --blocked-by operator`, and **stop working on that task immediately**. Do not invent side nitpicks to keep the task open.

---

## Run queue
Commands the operator must run manually (on a remote host, privileged shell, or external UI). Command first, `Expect:` second, empty `Output:` block below.

### `<TASK-ID>` — `<1-line outcome>`

- [ ] `<literal runnable command>`
      Expect: `<exit code, row count, or specific log line>`

Output:
```
```

---

## Decision gates
Tasks where code/measurement completed but closing or branching requires a human judgment call (e.g., a null experimental result, a threshold trade-off, or a scope change). Max 6 lines per gate. Check an option or add `[COMMENT]` and run `/handle-comments`.

### `[DECISION]` `<TASK-ID>` — `<1-line summary of the fork>`
- **Measured fact:** `<1-2 sentences with exact numbers vs. target gate>`
- **Options (check one or annotate with `[COMMENT]`):**
  - [ ] **(a)** `<Close task as done — accept current behavior and update docs/requirements/...>`
  - [ ] **(b)** `<Deprioritize / revert / file follow-up task>`
