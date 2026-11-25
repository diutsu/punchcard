---
type: investigation
state: done
created: YYYY-MM-DD
updated: YYYY-MM-DD
cross-file-references: []
---
# Evaluation: `<project or module>`

`<One line: the question this evaluation answers.>`

## Scope and method

- Evaluated: `<paths>` at commit `<hash>`
- Question: `<what the reader needs to decide>`
- Method: `<lenses applied, tools and commands used>`
- Reading done through `codebase-search`; claims tagged fact, inference or guess.

## Findings

Ranked by refactor payoff against risk. Every row has evidence.

| ID | Lens | Finding | Evidence | Severity | Payoff | Risk |
|---|---|---|---|---|---|---|
| F1 | `<lens>` | `<statement>` | `<file:line, command and output, or count>` | `<high/med/low>` | `<h/m/l>` | `<h/m/l>` |

## Recommended refactor sequence

1. `<Safest first step, for example a characterisation test or a seam>`. Verified by `<command>`.
2. `<Next step>`. Depends on 1. Verified by `<command>`.

Each step is filed as a task via `tracker`: `<task ids>`.

## What was not examined

- `<Area, reason it was skipped, and what could hide there>`
