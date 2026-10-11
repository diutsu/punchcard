---
type: research
state: wip
created: 2026-10-11
updated: 2026-10-11
cross-file-references: [docs/logic/_index.md, docs/requirements/_index.md]
---
# Business Logic — `<Module>: <Concern>`
One-line summary of the calculation, state machine, or domain rule defined in this document.

> **Authoring rule (settled rules only, $\le 400$ lines):**
> State only the **active** formula, threshold, or state machine. When a formula or threshold changes, **overwrite it in place**.
> Do not narrate prior versions, closed task IDs, or benchmark runs here — store the evaluation or spike in `docs/investigations/<slug>.md` and cite it in a 1-line `> **Guardrail:**` note.

## TOC
- [Formula / state machine](#formula--state-machine)
- [Parameters & thresholds](#parameters--thresholds)
- [Domain hazards & edge invariants](#domain-hazards--edge-invariants)

---

## Formula / state machine

```
<exact mathematical formula, pseudocode, or state transition diagram>
```

> **Guardrail:** `<1-sentence explanation of why this specific form is required (e.g. symmetric shrinkage to avoid zero-prior blowup)>` — evidence in [`../investigations/<slug>.md`](../investigations/_template.md).

---

## Parameters & thresholds

| Parameter | Canonical value | Range / Units | Role in calculation |
|---|---|---|---|
| `<param_name>` | `<value>` | `<range>` | `<what it controls>` |

---

## Domain hazards & edge invariants

- **`<Hazard name>`:** `<What goes wrong in raw data or domain math if mishandled, and the exact rule used to prevent it>`.
