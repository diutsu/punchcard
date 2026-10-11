---
name: research-to-plan
tier: leaf
description: >
  Turn accepted research (from docs/investigations/, internal-research,
  external-research, or debugging-method) into a concise, execution-grade plan
  at docs/plans/<id>-<slug>.md (strictly <= 150 lines, with phase roll-forward
  for multi-phase work). Trigger on "make a plan from this", "turn this into a
  plan", right after research concludes, and before any multi-step change. Do
  NOT load when there is no finding yet, when the change is a single obvious
  edit (use brief-plan-inline), or when executing an existing plan (see
  do-task).
trigger: /research-to-plan
---

# /research-to-plan

Turn a verified research finding into a compact, falsifiable execution plan (`docs/plans/<id>-<slug>.md`, **max 150 lines**) that an executor agent can run with zero re-derivation.

## When NOT to use this skill

- No finding yet $\rightarrow$ gather it first (`internal-research`, `external-research`, `debugging-method`) and record spikes in `docs/investigations/<slug>.md`.
- Single file / obvious edit $\rightarrow$ use a 3–5 line **brief-plan-inline** inside the task kickoff message; do not create a file in `docs/plans/`.
- Executing, gating, and closing an existing plan $\rightarrow$ `do-task`.

## 1. Where the plan lives & size discipline

Write the plan to `docs/plans/<id>-<slug>.md` under the `docs-management` frontmatter contract (`type: plan`, `state: wip`).

### Hard anti-bloat constraints
1. **150-line ceiling:** A plan file must never exceed 150 lines.
2. **Phase Roll-Forward (for multi-phase tasks):**
   - If a task has multiple phases, write step-level detail **only for the current active phase**.
   - List future phases as 1-line placeholders (`- [ ] Phase 2: <goal> (detail after Phase 1 lands)`).
   - When a phase lands and commits, **delete** its step block and replace it with `- [x] Phase 1: <1-line summary> (<commit-hash>)` under `### Completed phases`.
3. **No scope essays inside plans:** Keep `Scope decisions & fenced-off wrong paths` to 1 bullet per item. If scoping required deep investigation or benchmark tables, put that in `docs/investigations/<slug>.md` and link to it.

## 2. Plan skeleton (`docs/plans/<id>-<slug>.md`)

```markdown
---
type: plan
state: wip
created: YYYY-MM-DD
updated: YYYY-MM-DD
cross-file-references: [docs/tasks.md#<ID>, docs/requirements/<module>.md, docs/investigations/<slug>.md]
---
# Plan — `<ID>`: `<Task Title>`
Task: `<ID>`
Goal: `<one-line falsifiable claim or deliverable>`

## Acceptance criteria
- [ ] `<Concrete, checkable condition>`

## Scope decisions & fenced-off wrong paths
- **Staleness resolution:** `<1 line per code-vs-doc resolution>`
- **Do not walk:** `<Dead end + 1-line reason or citation to docs/investigations/<slug>.md>`

## Scope & affected files
- `<path/to/file>` — `<what changes>`

## Steps (current active phase only)

### Completed phases (rolled forward)
- [x] Phase 1: `<1-line summary>` (`<commit-hash>`)

### Active phase steps
1. **Step 1 — `<what>`**
   - Run: `<exact command>`
   - Expect: `<exact number / string / exit code>`
   - If divergent: `<branch or stop and re-plan>`

## Risks / rollback
- `<Per-step wip(<slug>) commits; rollback via git reset>`

## Test strategy
- **Baseline:** `<N passed, 0 failed (<commit-hash>, <date>)>`
- **Target:** `<N+k passed, 0 regressions>`
```

## Hard rules

- Never exceed 150 lines in `docs/plans/<id>-<slug>.md`.
- Never write detailed steps for more than one unexecuted phase at a time — use phase roll-forward.
- Never paste raw research logs or multi-paragraph scope essays into a plan — put those in `docs/investigations/<slug>.md` and link to them.
- Every step gate must state an exact expected number, string, or exit code — never "check it works".
- State `state: wip` on creation; `do-task` deletes the file when `<ID>` closes.

## Provenance and maintenance

Updated: 2026-10-11 (v2 subfolder path `docs/plans/`, 150-line cap, phase roll-forward rule).

Re-verification commands:
```bash
ls doc-templates/docs/plans/_template.md
```
