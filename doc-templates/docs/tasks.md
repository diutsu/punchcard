---
type: requirement
state: done
created: 2026-10-11
updated: 2026-10-11
cross-file-references: [docs/done.md, docs/architecture.md]
---
# Tasks
Single source of truth for all open work. Grouped by module and machine-managed by `ctask`.

## TOC
- [How to use this file](#how-to-use-this-file)
- [meta — cross-cutting](#meta--cross-cutting)

---

## How to use this file

This registry is machine-managed by `ctask` (see the `do-task` skill). Query and mutate via the CLI, never by hand-editing:

```bash
ctask list --prio high              # high-priority tasks
ctask list --module <module>        # tasks for one module
ctask show <ID>                     # one task, verbatim
ctask search "<keyword>"            # locate by content
ctask add --module <m> --title "..." --prio medium --goal "..." --done-when "..."
ctask close <ID>                    # moves entry to docs/done.md & reports stale blocked-by::
ctask validate                      # structural lint
```

When a task is done, first verify its shipped behavior is captured in place in `docs/requirements/<module>.md` or `docs/logic/<module>-<concern>.md`, delete `docs/plans/<id>-<slug>.md` if one existed, then run `ctask close <ID>` and clear any `blocked-by::` references it reports.

---

## meta — cross-cutting
