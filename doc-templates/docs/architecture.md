---
type: requirement
state: done
created: 2026-10-11
updated: 2026-10-11
cross-file-references: [docs/tasks.md, docs/usage.md, docs/requirements/_index.md, docs/logic/_index.md]
---
# Architecture
High-level system map: modules, boundaries, allowed dependencies, code standards, and documentation rules.

## TOC
- [Module map](#module-map)
- [Module responsibilities](#module-responsibilities)
- [Allowed dependencies](#allowed-dependencies)
- [Code quality & architecture guidelines](#code-quality--architecture-guidelines)
- [Data & storage philosophy](#data--storage-philosophy)
- [Documentation rules](#documentation-rules)

---

## Module map

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                                 interfaces                                   │
│                 cli · ui · scheduler (thin entry points)                     │
└──────────────────────────────────────────────────────────────────────────────┘
                                       │ calls
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                               domain modules                                 │
│        <module-a> (ingestion) ──► <module-b> (transforms / core logic)       │
└──────────────────────────────────────────────────────────────────────────────┘
                                       │ reads / writes
                                       ▼
┌──────────────────────────────────────────────────────────────────────────────┐
│                                  storage                                     │
│             thin physical layout abstraction + immutability rules            │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Module responsibilities

### `<module-name>`
One-line summary of what this module owns.

- Owns `<specific responsibility>`.
- Third-party SDKs confined here: `<library names>`.
- Output contract: `<return types / schemas>`.
- Does **not** own: `<explicit negative boundary>`.

### `storage`
Thin abstraction over physical data layout.

- Owns file paths, database DDL, connection lifecycle, and table immutability classes.
- Never interprets domain semantics of columns.
- No raw DB connections leak outside `storage`.

### `interfaces`
Thin entry points for humans, schedules, and external agents (`cli`, `ui`, `scheduler`).

- Calls domain module APIs; contains zero business logic or raw storage queries.
- No interface imports another interface. Shared interface helpers live at `src/<helper>.py`.

---

## Allowed dependencies

```
interfaces   ──►  any module
<module-b>   ──►  storage, <module-a>
<module-a>   ──►  storage
storage      ──►  (no internal dependencies)
```

Hard boundary rules (enforced by `tests/test_architecture_boundaries.py`):

- **External libraries stay inside their owning module.** Never import a third-party SDK outside the module that wraps it.
- **No sibling cross-imports** unless explicitly listed in the dependency graph above.
- **Stable cross-module contracts.** Internal refactors must not alter signatures or schemas consumed by upstream modules.

---

## Code quality & architecture guidelines

- **Check the module map before creating a file.** Every new function or class must live in the module that owns its responsibility. Do not create miscellaneous `utils.py` dumping grounds.
- **Fail fast at boundaries; no defensive slop.** Validate inputs at system boundaries, then trust internal types. Never wrap internal logic in broad `try/except` blocks that swallow errors or return silent fallback values.
- **Prefer clarity at module boundaries.** Pass standard data structures across modules rather than inventing wrapper classes per layer.
- **Keep functions focused ($\le 40$ lines) and files cohesive ($\le 350$ lines).** Split modules along responsibility seams before they become monoliths.
- **Prefer established packages over custom frameworks.** Use standard, well-maintained libraries.

---

## Data & storage philosophy

Every persisted table or store belongs to an explicit immutability class:

| Class | Behavior | Examples |
|---|---|---|
| **append-only** | Rows are never deleted or mutated; new observations append with a timestamp. | Raw events, audit/run logs |
| **static** | Written once per partition key; re-write is a no-op if present. | Historical archive dumps |
| **mergeable** | Idempotent upsert by primary key. | Daily time-series snapshots |
| **overwriteable** | Derived data; full recompute from raw/upstream is the normal write path. | Features, aggregates, scores |
| **reference** | Versioned reference data updated deliberately. | Whitelists, mappings, config |

---

## Documentation rules

All files inside `docs/` use **lowercase `kebab-case.md`** filenames (with leading `_` reserved for `_index.md` and `_template.md`).

1. **Root control files (`docs/` root):**
   - `architecture.md` (this file) — module map, boundaries, dependency rules, doc contract. No code line numbers in prose.
   - `usage.md` — operator manual: CLI commands, flags, daemon/queue management, reusable runbooks.
   - `tasks.md` & `done.md` — machine-managed exclusively via `ctask`.
   - `next-session-prompt.md` — live session handoff snapshot ($\le 40$ lines). Rewritten at session end; not a task list or changelog.
   - `operator-instructions.md` — pending human CLI runs (`## Run queue`) and blocked task forks (`## Decision gates`). Zero done-history, zero permanent runbooks.
   - `progress-log.md` — append-only 1-line highlight reel (`progress-log` skill).
2. **Subfolder knowledge base & ephemeral files:**
   - `docs/requirements/<module>.md` ($\le 400$ lines) — module behavioral contract (`type: requirement`).
   - `docs/logic/<module>-<concern>.md` ($\le 400$ lines) — formulas, thresholds, state machines, domain rules (`type: research`).
   - `docs/investigations/<slug>.md` — time-boxed web research, library evaluations, spike results, and incident root causes (`type: investigation`).
   - `docs/plans/<id>-<slug>.md` ($\le 150$ lines) — active execution plan (`type: plan`). **Deleted** when the task closes. No `executed-*.md` files exist.
3. **Timeless prose in `requirements/` and `logic/`:**
   - State only how the system behaves **now**.
   - Never append dated paragraphs (`Confirmed 2026-...`), bugfix histories, or `Problem / Fix / Decision / Alternatives` blocks inside requirement or logic docs.
   - If a choice needs a non-obvious guardrail so future sessions do not break it, add a single line:
     `> **Guardrail:** <1-sentence constraint> — see [investigations/<slug>.md](../investigations/<slug>.md).`
4. **Frontmatter contract (`docs-management` skill):**
   ```yaml
   ---
   type: <plan | investigation | requirement | research | log>
   state: <wip | planned | done | archived>
   created: YYYY-MM-DD
   updated: YYYY-MM-DD
   cross-file-references: [docs/architecture.md, src/...]
   ---
   ```
5. **Module-level prose:** `architecture.md`, `requirements/*`, and `logic/*` track modules and domain concepts in body text; real file paths belong in `cross-file-references`, `tasks.md`, `plans/*`, and `usage.md`.
