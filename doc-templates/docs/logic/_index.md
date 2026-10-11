---
type: research
state: done
created: 2026-10-11
updated: 2026-10-11
cross-file-references: [docs/architecture.md, docs/requirements/_index.md]
---
# Business Logic — Index
Start here to find the active formulas, thresholds, state machines, and domain rules behind a module's behavior.

## How to use this index

Logic docs (`docs/logic/<module>-<concern>.md`) hold the **active domain math and rules** ($\le 400$ lines per file): exact formulas, normalization constants, state transitions, and data-hazard rules that code alone cannot explain.

**Strict separation from `docs/investigations/`:**
- `docs/logic/` holds only the **settled, currently active formulas and rules** written in timeless present tense.
- `docs/investigations/` holds the **evaluations, benchmarks, rejected formulas, and historical spikes** that settled them.
- Never paste benchmark logs, dated verification narratives, or multi-paragraph `Problem / Fix / Decision` histories into `docs/logic/`. Use a 1-line `> **Guardrail:**` pointer to `docs/investigations/<slug>.md` instead.

## By module

| Module | Logic Doc | Covers |
|---|---|---|
| `<module>` | [`<module>-<concern>.md`](_template.md) | `<1-line summary of the formula, state machine, or domain rule>` |
