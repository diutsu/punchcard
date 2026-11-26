---
name: project-evaluation
tier: workflow
description: >
  Evidence-backed maintainability report on a project or module, with ranked
  findings and a safe refactor sequence. Load for "evaluate this codebase", "how
  maintainable is this", "where should we refactor first". Do NOT load for edits
  (codebase-cleanup, do-work) or one question (codebase-search).
trigger: /project-evaluation
---

# /project-evaluation

Assess a project or module for maintainability and refactorability, with evidence for every finding. This skill reads and reports. It starts no refactor.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| One question about how code works | `codebase-search` |
| A specific failure needs a cause | `forensics` |
| Reviewing a diff | `review-rubric` |
| Performing the refactors | `do-work`, after filing tasks via `tracker` |
| Removing, simplifying or updating code now, judged against where the project is going | `codebase-cleanup` |
| Writing the plan for a refactor | `plan` |

## Procedure

1. **Scope.** Name the project or module, the commit evaluated (`git rev-parse HEAD`), and the question driving the evaluation. Ask the user through the question interface only if scope is ambiguous, in one batch.
2. **Read.** Use `codebase-search` for every reading step: project map, task history via `tracker`, docs via `project-map`, then code. Keep its fact and inference tags.
3. **Measure.** Run the lenses below. Prefer commands that give counts.
4. **Write.** Fill `./templates/evaluation-report.md` and save it to the `investigations` key. Frontmatter follows `docs-management`.
5. **File follow-ups** via `tracker`, one task per recommended refactor step. Do not start them here.

## Lenses

| Lens | What to establish | Evidence source |
|---|---|---|
| Module boundaries and dependency direction | Layers, cycles, imports pointing the wrong way | import graph, grep of imports per module |
| Coupling and change amplification | Files that change together across unrelated modules | `git log --name-only` co-change counts |
| Churn crossed with size | Large files that change often | churn count times line count or complexity tool output |
| Duplication | Repeated blocks and parallel implementations | duplication tool output or grep of repeated patterns |
| Test seams | Where behaviour can be isolated; what is untestable and why | test layout, hard-wired clocks, globals, network calls |
| Error handling | One policy or several; swallowed errors, silent fallbacks | grep of catch and except blocks, return conventions |
| Dead code | Unreferenced exports, files, flags | reference search, coverage output |
| Doc-versus-code drift | `FRESH`, `STALE`, `CONTRADICTED` verdicts | method in `codebase-search` |
| Links from code to project work | Task IDs, plan and doc names, step numbers in code and comments; how many point at files that no longer exist | grep recipe in `backend-code` |
| Third-party SDK leakage | SDK types or calls outside their wrapper module | grep of SDK imports outside the boundary (`backend-code` states the rule) |

Recipes for co-change and churn-times-size are in `./references/commands.md`.

## Findings

Each finding carries an id, the lens, a statement, evidence, a severity (high, medium, low), a refactor payoff (high, medium, low) and a refactor risk (high, medium, low). Evidence is one of: `file:line`, a command with its output, or a count. A candidate finding with no evidence is dropped, not softened. Rank by payoff against risk: high payoff and low risk first.

## Recommended sequence

Order the refactors so each step leaves the suite green and makes the next one cheaper. Begin with the safest step: usually adding a characterisation test or a seam around the riskiest area. Name the verification for each step.

## Hard rules

- Always end the report with what was not examined.

## Provenance and maintenance

Updated: 2026-11-27. Check commands:

```bash
ls plugins/coding/skills/project-evaluation/templates/evaluation-report.md plugins/coding/skills/project-evaluation/references/commands.md
grep -n "codebase-search" plugins/coding/skills/project-evaluation/SKILL.md
```
