# Project Instructions

> **One-liner:** `<what this project does in one sentence>`
> **Lifecycle stage:** `prototype` <!-- Flip to `structured` via `/migrate-project-docs` once module boundaries are locked -->

## 1. Environment & Gate Commands

- **Install:** `<install command>`
- **Single test:** `<single test command>`
- **Full verification gate (`verify`):** `<typecheck + lint + test command>`
- **Task registry:** `ctask list --prio high` (never read `docs/tasks.md` raw when `ctask` can query it; never hand-edit `docs/tasks.md` or `docs/done.md`).

## 2. Lifecycle Stage Rules

### Stage A — `prototype` (Day 1 exploration)
- Only `docs/tasks.md`, `docs/next-session-prompt.md`, and `docs/architecture.md` exist.
- Build fast. Do not create `docs/requirements/*` or `docs/plans/*` until module boundaries stabilize.
- Once you begin backlogging tasks and locking module boundaries, run `/migrate-project-docs` (Mode B: Stabilize Prototype) to scaffold the full `docs/` tree and boundary tests, then flip **Lifecycle stage** above to `structured`.

### Stage B — `structured` (Default steady-state)
- **Architecture boundaries are law.** Check `docs/architecture.md` before adding files, dependencies, or cross-module imports. `tests/test_architecture_boundaries.py` enforces import directions in CI/verify.
- **Read before coding:** Read `docs/requirements/<module>.md` and any relevant `docs/logic/<module>-<concern>.md` before modifying `<module>`.
- **In-place doc updates only:** When behavior changes, rewrite the rule in `docs/requirements/<module>.md` or `docs/logic/<module>-<concern>.md` as timeless present-tense truth. Never append dated patch notes, bugfix narratives, or `Problem / Fix / Decision` blocks to requirement or logic docs.
- **Ephemeral plans:** Multi-step plans live at `docs/plans/<id>-<slug>.md` (capped at 150 lines). Completed phases collapse to a single checked line. Delete the plan file when closing the task with `ctask close <ID>`. Never create `executed-*.md` files.
- **Binary operator handoff:** If a step requires human execution, credentials, or a judgment call on a null/ambiguous result, add an exact command (`## Run queue`) or a $\le 6$-line choice (`## Decision gates`) in `docs/operator-instructions.md`, mark the task blocked in `ctask`, and **stop working on that task immediately**. Never write status essays or hunt for nitpicks to stay busy.

## 3. Code Quality Non-Negotiables

- **Respect module ownership:** External SDKs and libraries live exclusively inside the module that owns them (see `docs/architecture.md`).
- **Fail fast, no silent fallbacks:** Do not swallow exceptions or invent undocumented fallback values.
- **No unflagged stubs:** Any stub must be named with a `_stub_` prefix, return an honest empty state, and cite an open `tasks.md` ID (per `validation-and-qa`).
- **Keep functions and files small:** Prefer pure transforms and explicit data contracts at module boundaries.

## 4. Documentation Map

| Path | Role | Who reads/writes |
|---|---|---|
| `docs/tasks.md` | Open backlog (machine-managed via `ctask`) | `ctask` CLI only |
| `docs/done.md` | Closed task archive (`ctask close <ID>`) | `ctask` CLI only |
| `docs/next-session-prompt.md` | Live session handoff snapshot ($\le 40$ lines) | Rewritten at end of session |
| `docs/operator-instructions.md` | Human-only CLI run queue + decision gates | Agent queues items; human executes/decides; agent folds & deletes |
| `docs/architecture.md` | Module map, dependency rules, storage & schema rules | Read before structural work |
| `docs/usage.md` | Permanent CLI reference, daemon/queue runbooks | Updated when CLI/ops surface changes |
| `docs/progress-log.md` | Curated 1-line milestone log (`progress-log` skill) | Append-only on major events |
| `docs/requirements/<module>.md` | Module behavioral contract ($\le 400$ lines) | Timeless current truth |
| `docs/logic/<module>-<concern>.md` | Formulas, thresholds, domain state machines ($\le 400$ lines) | Timeless current truth |
| `docs/investigations/<slug>.md` | Spikes, web research, library evaluations, rejected paths | Read-only reference once concluded |
| `docs/plans/<id>-<slug>.md` | Active task execution plan ($\le 150$ lines) | Created at plan step; **deleted** at task close |
