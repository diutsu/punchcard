---
name: internal-research
tier: leaf
description: >
  Mine a project's own docs, git history, and code for ground truth — never
  guess at architecture, never trust a doc claim unread against the code.
  Trigger on: "how does X work here", recovering architecture for an
  unfamiliar module, onboarding to a codebase, pre-planning reconnaissance
  before do-task step 1 (scope), "flag inconsistencies" / "audit docs vs
  code", or any question answerable by reading this repo's own code/docs/git
  log. Do NOT use for evaluating external libraries/APIs (use
  external-research) or turning findings into a plan (use research-to-plan).
trigger: /internal-research
---

# /internal-research

Before writing code or plans, establish what actually exists. This skill is the **read phase** — it produces a dense, evidenced report with `file:line` citations; it does not plan or execute changes.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Evaluating an external library, API, SaaS, or ML model | `external-research` |
| Turning accepted findings into a gated execution plan | `research-to-plan` |
| You already know the module and need to execute a task | `do-task` |
| Auditing `docs/` YAML frontmatter or subfolder structure | `docs-management` |

## 1. Canonical read order

Read in this order and stop once you have enough evidence to answer the question:

1. **Project `CLAUDE.md`** (repo root) — lifecycle stage, gate commands, non-negotiables, documentation map.
2. **Open & closed tasks via `ctask`** (`ctask list --module <m>`, `ctask search "<kw>"`) — the risk register. Many projects forbid inline `TODO`s in code so all known gaps live in `docs/tasks.md`.
3. **`docs/architecture.md`** + **`docs/requirements/<module>.md`** + **`docs/logic/<module>-<concern>.md`** — module boundaries, allowed dependencies, behavioral contracts, and active domain formulas.
4. **`docs/investigations/<slug>.md`** (top `## Verdict & promoted rules` section first) — past spikes, root-cause analyses, and fenced-off dead ends.
5. **The source code** — read last, comparing actual implementation against the contracts in steps 3–4.

## 2. Git archaeology recipes

Run from the repository root:

```bash
# Churn hotspots — files touched most frequently
git log --format= --name-only | sort | uniq -c | sort -rn | head -30

# Revert scan — approaches tried and undone
git log --oneline --grep="Revert" -i

# Interrupted in-flight step commits (do-task wip convention)
git log --oneline --grep="^wip(" -i | head -20

# Active or stale git worktrees and branches
git worktree list
git branch -a
```

**Caveat — `docs/` may live outside git tracking** (e.g., a gitignored directory or a symlink into an Obsidian vault):
```bash
readlink docs 2>/dev/null
git check-ignore -v docs
git ls-files docs
```
If `docs/` is untracked by git, `git log` will never show doc changes — rely on each doc's `updated:` frontmatter field, `docs/done.md`, and `docs/investigations/`.

## 3. Drift detection method

Compare each claim in `docs/requirements/<module>.md` and `docs/logic/<module>-<concern>.md` against the code that implements it and classify:

| Verdict | Meaning |
|---|---|
| **`FRESH`** | Doc claim matches current code behavior. |
| **`STALE`** | Doc describes something renamed, removed, or superseded, though not actively dangerous. |
| **`CONTRADICTED`** | Doc asserts the opposite of what the code does — highest priority to resolve. |
| **`WIN`** | Code implements load-bearing, non-obvious behavior that is undocumented and should be promoted to `docs/requirements/` or `docs/logic/`. |

Every verdict requires **`file:line` evidence on both sides** (doc path:line and code path:line).

## 4. Output contract

Return a compact structured report (delegable to a read-only `researcher` subagent):

```text
INTERNAL RESEARCH REPORT — <question / module>

SOURCES READ: <files in order read>

FINDINGS:
1. [FRESH|STALE|CONTRADICTED|WIN] <one-line claim>
   doc: <path:line>   code: <path:line>
   evidence: <fact | inference | guess>
   why it matters: <one line>

OPEN QUESTIONS: <anything that could not be verified read-only>
```

## Hard rules

- Never assert a doc-vs-code relationship without `file:line` evidence on both sides.
- Never assume `git log` tracks `docs/` without checking whether `docs/` is gitignored or symlinked.
- Never skip querying `ctask` when investigating a module — `docs/tasks.md` is the risk register.
- Never modify code or docs inside an `internal-research` pass — report findings and hand off to `research-to-plan`, `do-task`, or `write-docs`.
- Tag every claim honestly as `fact`, `inference`, or `guess`.

## Provenance and maintenance

Updated: 2026-10-11 (v2: added `tier: leaf`, updated read order to `docs/requirements/`, `docs/logic/`, `docs/investigations/`, and `ctask`).

Re-verification commands:
```bash
ls docs/requirements/_index.md docs/logic/_index.md
```
