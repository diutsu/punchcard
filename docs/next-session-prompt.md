---
type: requirement
state: wip
created: 2026-10-11
updated: 2026-10-26
cross-file-references: [docs/operator-instructions.md, docs/tasks.md]
---
# Next-session starting prompt
Rewritten at the end of every session ($\le 40$ lines). Live snapshot only.

## Live state

- **Repository layout complete:** `skills/` (all 19 general-purpose v2 skills ported and aligned), `skills/migrate-project-docs/templates/` (starter `CLAUDE.md` + v2 `docs/` skeleton), and `docs/` (meta-docs for `Frank` itself).
- **Next open task:** `TPL-01` — Trial `/migrate-project-docs` on an existing project (e.g., `repit`) or prototype and fold any edge cases back into `skills/migrate-project-docs/templates/`.
- **Blocked on `operator-instructions.md`:**
  - `META-02` — `ctask` source is missing (`https://github.com/diutsu/ctask` is empty), so `ctask validate` cannot run (see [operator-instructions.md](operator-instructions.md)).
- **Open question:** once the `ctask` source is recovered, decide whether it stays in its own repo or moves into `Frank/ctask/` (shares the `tasks.md` format contract with `skills/`).

