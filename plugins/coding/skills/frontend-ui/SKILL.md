---
name: frontend-ui
tier: reference
description: >
  Rules for any user-facing surface: a web view, dashboard panel or
  interactive CLI output. Covers the five honest data states, no swallowed
  fetch errors, no fabricated values, restrained visual treatment, reuse over
  new components, and how to produce mockups. Load BEFORE touching view markup,
  adding a panel or tab, or wiring a fetch into a screen. Do NOT load for pure
  backend work (see backend-code) or for reviewing a running app (see
  interactive-app-review).
trigger: /frontend-ui
---

# /frontend-ui

Every surface belongs to one coherent experience and never misreports the state of the data behind it.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Backend, storage or pipeline logic | `backend-code` |
| Live review of a running app | `interactive-app-review` |
| Definition of done and the stub policy | `validation-and-qa` |
| Root-causing a broken screen | `forensics` |
| Android device checks | `device-qa` |

## 1. Think about the experience before code

Answer three questions in the plan before writing view code:

1. What renders in each of the five states in section 2?
2. Which existing screen does this extend? Prefer extending a view over adding a top-level tab or route.
3. Does this supersede an existing panel? Search the view directory for a legacy component with the same job and retire it in the same plan.

## 2. Five honest states

Every data-driven surface handles and distinguishes:

- **loading:** the request is in flight, visibly.
- **error:** the fetch failed, shown clearly and never swallowed into an empty state.
- **empty:** the query succeeded and returned nothing.
- **data-unavailable:** a required input is missing or not computed. The value is unknown, not zero.
- **real-data:** the verified values.

An empty `.catch(() => {})` on a fetch is a bug: a dead backend would render as empty or zero.

## 3. No fabricated values

Ship no sample rows, random series or plausible fake numbers. An unset control shows as unset, not as zero. When an endpoint is not wired yet, render `data-unavailable`, name the stub per `validation-and-qa`, and file it via `tracker`.

## 4. Restrained visual treatment

- Spend emphasis on few things: if bold, colour and decoration all apply to most of a screen, none of them signals anything.
- Default new surfaces to read-only. A control that changes state needs an explicit requirement for it.
- Check size extremes (shortest and tallest content, narrowest and widest viewport) before calling a layout done.

## 5. Consistency and reuse

Before writing a panel, component or hook, search the view directory and the design tokens for one that does most of the job. If you are about to write a second version of an existing panel, extract a shared component or hook instead. Near-duplicate panels are a recurring defect.

```bash
grep -rln "useState\|catch" src/**/views/*.tsx   # adapt the glob to the project's view folder
```

## 6. Mockups

Produce a mockup as HTML or SVG. Iterate with the user until the layout and the five states are settled, then file each follow-up change via `tracker`. A mockup shows the unavailable and error states too, not only real data.

## Hard rules

- Enumerate all five states before implementing a data-driven view.
- Never swallow a fetch error into an empty or zero state.
- Never render fabricated or placeholder numbers on a shipped surface.
- Never add a mutating control without a requirement for it.
- Never add a view without searching for one to reuse or retire.

## Provenance and maintenance

Updated: 2026-11-26.

Re-verification commands:
```bash
grep -rn "catch *(() *=> *{})" src | head
```
