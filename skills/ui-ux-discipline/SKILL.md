---
name: ui-ux-discipline
tier: reference
description: >
  REFERENCE, not a workflow — consult during planning (research-to-plan) and
  building (do-task, code-task) for any user-facing surface: web UI view,
  dashboard panel, or interactive CLI output. Load BEFORE touching view markup,
  adding a panel/tab, or wiring data fetches into a screen. Enforces the 5
  honest data states (loading, error, empty, data-unavailable, real-data), bans
  swallowed fetch errors and fabricated placeholder values, defaults to
  read-only observability, and prevents view-sprawl. Do NOT load for pure
  backend/pipeline work with no rendered surface.
trigger: /ui-ux-discipline
---

# /ui-ux-discipline

Every user-facing surface must belong to **one coherent experience** and must **never lie about the state of the data behind it**.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Turning a UI change into a gated execution plan | `research-to-plan` / `do-task` |
| Definition of done and test-gate verification | `validation-and-qa` |
| Root-causing a broken screen | `debugging-method` |
| Raw vs. derived data correctness in the backend store | `data-integrity` |
| Pure backend, storage, or pipeline logic with no rendered surface | `code-discipline` |

## 1. Think UX before code (prevent view-sprawl)

Before writing view code, answer three questions in the plan (`docs/plans/<id>-<slug>.md`):
1. **What renders in each of the 5 states (§2)?**
2. **Which existing screen/tab does this extend?** Default to extending an existing view rather than adding a new top-level tab or route.
3. **Does this supersede an existing panel?** Grep the view directory for duplicate or legacy components doing the same job and retire the old one in the same plan.

## 2. The 5 honest states contract

Every data-driven surface must explicitly handle and distinguish all five states:
- [ ] **`loading`** — request in flight; visibly indicated.
- [ ] **`error`** — fetch or query failed; surfaced clearly to the user, never swallowed into an empty state.
- [ ] **`empty`** — query succeeded and returned zero items (`"0 active jobs"`).
- [ ] **`data-unavailable`** — required upstream input is missing or uncomputed (distinct from `empty`: the value is unknown, not zero).
- [ ] **`real-data`** — the verified values.

**Ban silent `.catch(() => {})` on UI fetches:** Swallowing a fetch error so a dead backend renders as `empty` or `0` is a trust-breaking bug.

## 3. Zero fabricated or placeholder values

Never ship hardcoded sample rows, `Math.random()` series, or plausible-looking fake numbers in a view. If a backend endpoint is not wired yet, render **`data-unavailable`** and flag the `_stub_` with a `ctask` ID (per `validation-and-qa`).

## 4. Default to read-only observability

Default every new UI screen to **read-only observability**. Any button or control that mutates state, triggers a job, or writes to a database requires explicit requirement sign-off in `docs/requirements/interfaces.md`.

## 5. Reuse components before inventing

Before creating a new table, card, or hook, grep the UI directory for existing components and design-system tokens (`docs/requirements/interfaces-design-system.md` if present). Extract shared components rather than copy-pasting panels.

## Hard rules

- Enumerate all 5 states (`loading`, `error`, `empty`, `data-unavailable`, `real-data`) before implementing any data-driven view.
- Never swallow a fetch or query error into a false-positive `empty` or `0` state.
- Never render fabricated, sample, or placeholder numbers on a shipped surface.
- Default new UI surfaces to read-only; require explicit requirement spec approval for mutating controls.
- Grep for near-duplicate or superseded views before adding a new component; reuse or retire in the same pass.

## Provenance and maintenance

Updated: 2026-10-11 (v2: added `tier: reference`, updated doc paths to `docs/plans/` and `docs/requirements/`).

Re-verification commands:
```bash
ls skills/validation-and-qa/SKILL.md skills/data-integrity/SKILL.md
```
