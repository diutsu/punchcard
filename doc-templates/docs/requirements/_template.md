---
type: requirement
state: wip
created: 2026-10-11
updated: 2026-10-11
cross-file-references: [docs/architecture.md, docs/requirements/_index.md]
---
# Requirements — `<Module Name>`
One-line summary of what `<module>` is responsible for and the guarantees it provides to callers.

> **Authoring rule (single-read, timeless truth, $\le 400$ lines):**
> Describe **only** how the module behaves today. When a bugfix or design change alters behavior, **rewrite the affected section in place**.
> Never append dated update notes (`Confirmed on 2026-...`), task-ID histories (`Fixed in MOD-12`), or `Problem / Fix / Decision / Alternatives` blocks here. Put spike history and rejected alternatives in `docs/investigations/<slug>.md` and reference them via a 1-line `> **Guardrail:**` note if needed.

## TOC
- [Responsibilities & boundaries](#responsibilities--boundaries)
- [Public contract & data shapes](#public-contract--data-shapes)
- [Behavioral invariants](#behavioral-invariants)
- [Failure & edge-case behavior](#failure--edge-case-behavior)

---

## Responsibilities & boundaries

- Owns `<primary capability>`.
- Reads from `<upstream module/store>`; writes to `<downstream module/store>`.
- Never performs `<out-of-scope action owned by another module>`.

---

## Public contract & data shapes

| Entry point / Concept | Input shape | Output shape | Semantics |
|---|---|---|---|
| `<operation>` | `<schema/type>` | `<schema/type>` | `<idempotency, ordering, or side-effect contract>` |

---

## Behavioral invariants

- **`<Invariant name>`:** `<Statement of what must always hold true, written in timeless present tense>`.
  > **Guardrail:** `<Optional 1-sentence warning if a naive refactor would break an invariant>` — see [`../investigations/<slug>.md`](../investigations/_template.md).

---

## Failure & edge-case behavior

| Condition | Required behavior |
|---|---|
| `<Empty input / missing key>` | `<Fail closed with ValueError / return empty frame / etc.>` |
| `<Upstream timeout / rate limit>` | `<Retry budget, backoff rule, and state cleanup>` |
