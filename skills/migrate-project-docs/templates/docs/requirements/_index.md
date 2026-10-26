---
type: requirement
state: done
created: 2026-10-11
updated: 2026-10-11
cross-file-references: [docs/architecture.md, docs/usage.md, docs/logic/_index.md]
---
# Requirements — Index
Start here to find the behavioral contract for a module before modifying its code.

## How to use this index

Requirement docs state **design intent**: what a module must do and how it must behave ($\le 400$ lines per module doc). They are the behavioral contract; code is the implementation.

Read the matching `docs/requirements/<module>.md` before implementing changes. If a requirement doc and the code disagree, one of them is stale — determine which before writing code.

For domain formulas, scoring math, thresholds, and non-obvious domain rules, use the sibling [Logic index](../logic/_index.md). For historical spikes, benchmarks, or why an alternative was rejected, check `docs/investigations/`.

## Marking unbuilt behavior

When a requirement doc describes a target design ahead of the code, mark the gap inline right after the affected claim:

```markdown
**Status: not implemented.** Reason, plus a task ID (`tasks.md#MOD-01`) or "aspirational, no task filed".
```

Use `**Status: partially implemented.**` with the same shape when part of a claim is built, naming what is and is not present. Do **not** use the frontmatter `state` field for feature implementation status.

## Cross-cutting

| Doc | Covers |
|---|---|
| [architecture.md](../architecture.md) | Core modules, boundaries, allowed dependency directions, storage classes, and documentation rules. |
| [usage.md](../usage.md) | Operator manual: CLI surface, configuration, background job management, and reusable runbooks. |

## Modules

| Module | Requirement Doc | Covers |
|---|---|---|
| `<module>` | [`<module>.md`](_template.md) | `<1-line summary of module behavioral contract>` |
