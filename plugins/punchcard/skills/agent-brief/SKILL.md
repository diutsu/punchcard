---
name: agent-brief
tier: reference
description: >
  Whether a sub-agent is worth the tokens, which model tier, and how to brief
  it, with templates per agent role. Load before spawning any sub-agent or
  writing a handoff for another coding tool. Do NOT load for the scoring rubric
  (`review-rubric`) or the work loop (`do-work`).
trigger: /agent-brief
---

# /agent-brief

A sub-agent starts with no context. The brief is everything it knows. A good brief is short, names files by path and fixes the report format.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Scoring dimensions, quick-fix limits, delta rules | `review-rubric` |
| Running a task end to end | `do-work` |
| The step takes fewer tool calls than the brief takes to write | Do it yourself |

## Is a separate agent worth it?

Spawn an agent when at least one holds:

- The work reads or produces large output you do not need in your context (fetching, log triage, wide search).
- Independent steps can run in parallel.
- A reviewer must not have seen the author's reasoning.
- The step is a code-and-test loop with a clear done signal.

Do the work yourself when the step is small, depends on context you already hold, or needs your judgment.

## Pick the model tier

| Work | Tier |
|---|---|
| Architecture, ambiguous scope, multi-step debugging, final judgment | Main model; do not delegate |
| Fetching, processing, analysis, code and test loops, review | Mid-tier |
| Trivial contained edits: rename, flag, boilerplate, one-file fix | Cheapest |

Raise a reviewer a tier only when the change crosses module boundaries.

## Write the brief

1. Pick the template in `./templates/` and fill every field.
2. Pass **file paths and diff ranges, never pasted contents.** The agent reads the files itself.
3. State what to change or answer, the done signal, the exact command to run, and what is out of scope.
4. Fix the report format by copying the template's report block. Do not paraphrase it.
5. Write all briefs for a task in one pass while the context is fresh.

| Template | Use for |
|---|---|
| `read-only-investigation.md` | Fact-finding with citations, no edits |
| `executor-step.md` | One scoped change with a test command |
| `reviewer.md` | Independent review of a diff or plan |
| `external-builder-handoff.md` | Validating another coding tool's batch and writing its next batch |

## Hard rules

- Never put real personal or financial data, or the user's name or email, in a brief that leads to an external call.
- Never brief a reviewer with the author's reasoning, only the artifact and the acceptance criteria.
- Never let an executor expand scope. Out-of-scope findings go in its issues list.
- Never accept a report that lacks the template's fields; send it back once, then do the check yourself.
- Never name an agent type in a brief beyond the `reviewer` and `suite-runner` this marketplace ships.

## Provenance and maintenance

Updated: 2026-11-13.

Re-verification commands:
```bash
ls plugins/punchcard/skills/agent-brief/templates
grep -c 'WHAT I DID NOT CHECK\|FILES CHANGED' plugins/punchcard/skills/agent-brief/templates/*.md
```
