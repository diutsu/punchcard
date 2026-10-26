---
type: plan
state: wip
created: 2026-10-11
updated: 2026-10-11
cross-file-references: [docs/tasks.md#<ID>, docs/requirements/<module>.md]
---
# Plan — `<ID>`: `<Task Title>`
Task: `<ID>`
Goal: `<one-line falsifiable claim or deliverable>`

> **Lifecycle & size rules ($\le 150$ lines hard cap):**
> 1. **Delete on task close:** When `<ID>` closes via `ctask close <ID>`, **delete this file** after promoting durable behavior to `docs/requirements/` or `docs/logic/`. Never create an `executed-*.md` file.
> 2. **Phase roll-forward (no multi-phase bloat):** If this task spans multiple phases, keep detailed steps **only for the current active phase**. When a phase lands and commits, replace its entire step block below with a single line: `- [x] Phase N: <1-line summary> (<commit-hash>)`.
> 3. **No scope essays:** Record staleness resolutions in 1 line each; put deep findings in `docs/investigations/`.

## Acceptance criteria
- [ ] `<Concrete, checkable condition 1>`
- [ ] `<Concrete, checkable condition 2>`

## Scope decisions & fenced-off wrong paths
- **Staleness resolution:** `<1 line per code-vs-doc discrepancy resolved during scoping>`
- **Do not walk:** `<Dead end + 1-line reason or link to docs/investigations/<slug>.md>`

## Scope & affected files
- `<path/to/file.py>` — `<what changes>`

## Steps (current active phase only)

### Completed phases (rolled forward)
<!-- Replace finished phases with a 1-line summary + commit hash:
- [x] Phase 1: <summary> (`<commit-hash>`)
-->

### Active phase steps
1. **Step 1 — `<what>`**
   - Run: `<exact test/verification command>`
   - Expect: `<exact number / exit code / output>`
   - If divergent: `<stop and re-plan>`

## Risks / rollback
- `<Per-step wip(<slug>) commits; rollback via git reset to last good step>`

## Test strategy
- **Baseline:** `<N passed, 0 failed at commit <hash>>`
- **Target:** `<N+k passed, 0 regressions>`
