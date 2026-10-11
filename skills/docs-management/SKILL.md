---
name: docs-management
tier: leaf
description: >
  Enforce the v2 YAML frontmatter contract, subfolder layout
  (docs/{requirements,logic,plans,investigations}/), size ceilings, and
  timeless-prose rules across every doc under docs/. Defines the canonical
  frontmatter template (type, state, created, updated, cross-file-references),
  bans executed-*.md files and inline historical patch narratives, and provides
  procedures to add/validate frontmatter and bump `updated` on every edit.
  Trigger when creating a doc, editing a doc, closing a task's doc pass, or
  auditing docs/ for frontmatter and structural compliance. Do NOT load for
  prose sentence-style rules or ADR prose shapes (see write-docs), for
  converting a legacy flat docs/ tree (see migrate-project-docs), or for
  curated milestone logging (see progress-log).
trigger: /docs-management
---

# /docs-management

Every doc under `docs/` is governed by a **YAML frontmatter contract**, a **subfolder taxonomy**, and **anti-accretion rules**. This v2 contract keeps only daily-driver control files at the `docs/` root, moves module docs and ephemeral plans into dedicated subfolders, and eliminates `executed-*.md` files.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Sentence-level prose style (max 20 words, active voice, no nominalizations) | `write-docs` |
| Converting a legacy flat `docs/` directory (`REQUIREMENTS-*`, `executed-*`) or stabilizing a prototype | `migrate-project-docs` |
| Writing or pruning `docs/operator-instructions.md` checklists and decision gates | `operator-instructions` |
| Appending a 1-line highlight to `docs/progress-log.md` | `progress-log` |
| Processing `[COMMENT]` annotations left by the user | `handle-comments` |

## 1. Directory taxonomy & size ceilings

Keep the `docs/` root uncluttered so the three files the operator opens daily (`tasks.md`, `next-session-prompt.md`, `operator-instructions.md`) are immediately visible:

| Path | `type` | Allowed `state` | Ceiling | Purpose |
|---|---|---|---|---|
| `docs/tasks.md` | `requirement` | `done` | `ctask`-owned | Open work registry (machine-managed by `ctask` only). |
| `docs/done.md` | `requirement` | `done` | `ctask`-owned | Closed task archive (populated by `ctask close`). |
| `docs/next-session-prompt.md` | `requirement` | `wip` | $\le 40$ lines | Live session handoff snapshot; rewritten at session end. |
| `docs/operator-instructions.md` | `requirement` | `wip` | Active items only | Human CLI `Run queue` + `Decision gates` (see `operator-instructions`). |
| `docs/architecture.md` | `requirement` | `done` | $\le 300$ lines | Module map, boundaries, allowed dependencies, storage classes, doc rules. |
| `docs/usage.md` | `requirement` | `done` | $\le 400$ lines | Permanent CLI reference, daemon/queue operations, reusable runbooks. |
| `docs/progress-log.md` | `log` | `done` | $\le 250$ chars/line | Append-only milestone log (governed by `progress-log`). |
| `docs/requirements/_index.md` | `requirement` | `done` | $\le 120$ lines | Index of module requirement contracts. |
| `docs/requirements/<module>.md` | `requirement` | `wip \| done` | $\le 400$ lines | Module behavioral contract: inputs, outputs, invariants, edge cases. |
| `docs/logic/_index.md` | `research` | `done` | $\le 120$ lines | Index of domain formulas, thresholds, and state machines. |
| `docs/logic/<module>-<concern>.md` | `research` | `wip \| done` | $\le 400$ lines | Active formulas, scoring math, thresholds, and data-hazard rules. |
| `docs/investigations/<slug>.md` | `investigation` | `wip \| done \| archived` | Top verdict $\le 10$ lines | Spikes, web research, library evaluations, benchmarks, incident root causes. |
| `docs/plans/<id>-<slug>.md` | `plan` | `wip` | $\le 150$ lines | Active task execution plan. **Deleted** when the task closes. |

**Filename casing rule (`kebab-case.md`):** Every `.md` file inside `docs/` uses **lowercase `kebab-case.md`** (with leading `_` reserved exclusively for `_index.md` and `_template.md`). Never use `UPPER_CASE.md` or `camelCase.md` inside `docs/`. Uppercase filenames (`README.md`, `CLAUDE.md`, `SKILL.md`) are used only where mandated by external ecosystem tools outside `docs/`.

**Retired family (`executed-*.md`):** Never create `executed-<slug>.md` files. Shipped behavior folds in-place into `docs/requirements/` or `docs/logic/`; commit hashes and task closure live in `docs/done.md` (via `ctask close`); major events get one line in `docs/progress-log.md`.

There is **no `type` or folder for arbitrary scratch docs.** If a proposed doc fits none of the rows above, stop and ask the user.

## 2. The frontmatter template

Every doc under `docs/` starts with this exact block, a blank line, `# Title`, and a one-line goal:

```markdown
---
type: <plan | investigation | requirement | research | log>
state: <wip | planned | done | archived>
created: YYYY-MM-DD
updated: YYYY-MM-DD
cross-file-references: [docs/architecture.md, src/bar/baz.py]
---
# Title
<one-line goal>

## TOC (if 3+ H2 sections)
```

All five fields are **required** in this exact order:
- **`type`** $\in$ `{plan, investigation, requirement, research, log}`.
- **`state`** $\in$ `{wip, planned, done, archived}`. Canonical living docs (`architecture.md`, `usage.md`, `tasks.md`, `done.md`, and settled `requirements/*` or `logic/*` files) use `state: done`. Active plans and `next-session-prompt.md` / `operator-instructions.md` use `state: wip`.
- **`created`** — `YYYY-MM-DD`, set once at creation and never modified.
- **`updated`** — `YYYY-MM-DD`, bumped to today on every content edit.
- **`cross-file-references`** — YAML list of real repo paths (`docs/...`, `src/...`, `tests/...`) referenced by or sibling to the doc. Use `[]` if none; never omit the field.

## 3. Anti-accretion rules for `requirements/` and `logic/`

`docs/requirements/*.md` and `docs/logic/*.md` are **single-read, timeless present-tense specifications** — never diaries, changelogs, or courtroom briefs.

### Rule A — Rewrite in place; ban historical patch blocks
When a bug fix, refactor, or design change alters how a module works:
1. Locate the existing section, table row, or formula in `docs/requirements/<module>.md` or `docs/logic/<module>-<concern>.md`.
2. **Overwrite it in place** so the document reads as if the system was always designed that way.
3. **Never** add `Problem / Fix / Decision / Alternatives` blocks, dated verification notes (`Confirmed 2026-09-01...`), or task-transition narratives (`Changed in ANL-23; previously ANL-45 did...`) inside `requirements/` or `logic/`.

### Rule B — Use 1-line Guardrails + `investigations/` for "Why"
When a formula, constant, or design choice looks counter-intuitive and a future agent might break it by "cleaning it up", add a **single-line blockquote guardrail** right below the rule:

```markdown
> **Guardrail:** Add `_SHRINKAGE_K` to both numerator and denominator so zero-prior windows stay sign-correct without special-casing — see [`../investigations/anl23-velocity-shrinkage.md`](../investigations/anl23-velocity-shrinkage.md).
```

Put the full derivation, benchmark comparison, or rejected alternatives in `docs/investigations/<slug>.md`, never inline in `requirements/` or `logic/`.

### Rule C — Top-of-file verdict in `docs/investigations/`
Every file in `docs/investigations/<slug>.md` must begin right after its `# Title` with `## Verdict & promoted rules` ($\le 10$ lines) stating:
1. The 1–2 sentence conclusion.
2. Which `requirements/` or `logic/` files were updated with the promoted rule.
3. Which dead-end approaches were rejected and why (so agents reading the top 15 lines skip the raw research body unless needed).

### Rule D — Phase roll-forward in `docs/plans/`
Plans in `docs/plans/<id>-<slug>.md` are capped at **150 lines**:
- When a phase in a multi-phase task lands and commits, **delete** that phase's step-by-step body from the plan file and replace it with a single checked line under `### Completed phases`:
  `- [x] Phase 1: <1-line summary> (<commit-hash>)`
- When the task itself closes (`ctask close <ID>`), **delete `docs/plans/<id>-<slug>.md`**.

## 4. Procedures

### (a) Validate frontmatter and structure across `docs/`
```bash
# Find docs missing required frontmatter
grep -rL '^type:' docs/

# Find any non-kebab-case (uppercase) .md filenames inside docs/
find docs -name '*[A-Z]*.md'

# Find banned historical-accretion markers inside requirements/ and logic/
grep -rn -E '(\*\*Problem\.\*\*|\*\*Fix\.\*\*|Confirmed on 20|Verified on 20|### Update|### Amendment)' docs/requirements/ docs/logic/

# Find any stray executed-*.md files or root-level plan-*.md files
find docs -maxdepth 1 -name 'executed-*.md' -o -name 'plan-*.md'

# Check line-count ceilings
wc -l docs/next-session-prompt.md docs/plans/*.md docs/requirements/*.md docs/logic/*.md
```

### (b) Bump `updated` on every edit
Whenever you edit a doc's content, bump `updated:` to today before finishing:
```bash
sed -i "s/^updated:.*/updated: $(date +%Y-%m-%d)/" docs/<path>.md
```

## Hard rules

- Never create uppercase `.md` filenames inside `docs/` — every file under `docs/` must use lowercase `kebab-case.md` (plus `_index.md` / `_template.md`).
- Never create `executed-<slug>.md` files — fold durable behavior into `docs/requirements/` or `docs/logic/` and delete `docs/plans/<id>-<slug>.md` on task close.
- Never place `REQUIREMENTS-*`, `BUSINESS_LOGIC-*`, `plan-*`, or `investigation-*` files at the `docs/` root — use `docs/requirements/`, `docs/logic/`, `docs/plans/`, and `docs/investigations/`.
- Never write `Problem / Fix / Decision / Alternatives` blocks, dated run narrations, or task-history paragraphs inside `docs/requirements/` or `docs/logic/` — edit rules in place and use a 1-line `> **Guardrail:**` pointer to `docs/investigations/` when rationale must be preserved.
- Never let `docs/next-session-prompt.md` exceed 40 lines or `docs/plans/<id>-<slug>.md` exceed 150 lines.
- Never leave completed phase details expanded inside `docs/plans/<id>-<slug>.md` — roll finished phases into a 1-line summary + commit hash.
- Never omit any of the 5 YAML frontmatter fields (`type`, `state`, `created`, `updated`, `cross-file-references`), and always bump `updated:` on content edits.

## Provenance and maintenance

Authored/updated: 2026-10-11 (v2 subfolder & anti-accretion contract).

Re-verification commands:
```bash
grep -rL '^type:' doc-templates/docs/
wc -l doc-templates/docs/next-session-prompt.md doc-templates/docs/plans/_template.md
```
