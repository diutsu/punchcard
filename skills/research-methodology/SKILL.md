---
name: research-methodology
tier: reference
description: >
  REFERENCE, not a workflow — the evidence bar for any claim of improvement,
  alpha, performance gain, or correctness. Load BEFORE running an experiment,
  tuning a parameter, evaluating a model/strategy/heuristic, or answering "does
  X improve Y" / "is this faster/better". Enforces hypothesis-predicts-numbers
  (with a falsifying band), yardstick-first validation on known-answer cases,
  adversarial refutation, regime honesty, and the idea lifecycle. Do NOT load
  for turning a finding into an execution plan (use research-to-plan) or for
  routine bug triage (use debugging-method).
trigger: /research-methodology
---

# /research-methodology

Turns a hunch into a verified result. An unfalsifiable claim, an eyeballed `"looks better"`, or a measurement from an uncalibrated evaluator is noise, not evidence.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Turning an accepted finding into a gated execution plan | `research-to-plan` |
| Evaluating an external library, API, or SaaS vendor | `external-research` |
| Mining this repo's own docs, git log, and code | `internal-research` |
| Root-causing a known bug | `debugging-method` |

## 1. Hypothesis predicts numbers (write BEFORE running)

Write down the prediction in the task entry (`docs/tasks.md`) or plan (`docs/plans/<id>-<slug>.md`) **before** executing the experiment:

```text
Hypothesis:   <mechanism — WHY this should change the outcome>
Predicts:     <direction> by <rough magnitude band>    e.g. "p95 latency -20% to -35%"
Falsified if: <specific result that kills the claim>   e.g. "reduction < 10% or throughput regression"
```

- **Direction alone (`"should improve"`) is not a prediction.** Commit to a numeric band and a falsification threshold in advance.
- **Null results are valid completions:** If the experiment runs cleanly and hits the `Falsified if` condition (or yields `+0` real-world effect), **do not loop or re-run with tweaked parameters to force a win**. Record the negative/null finding in `docs/investigations/<slug>.md` or queue a `### [DECISION]` gate in `docs/operator-instructions.md` (per `operator-instructions`).

## 2. Yardstick-first rule

Validate the measuring instrument before trusting any number it produces:
1. **Reproduce known-answer cases first.** Construct a synthetic input whose exact output you know by hand and assert the evaluator reproduces it.
2. **Round-trip a trivial baseline.** If the evaluator fails on a 3-row hand-checkable case, fix the evaluator before running the real experiment.

## 3. The acceptance bar

A claim of improvement is accepted only when all three hold:
1. **One mechanism explains every observation, including negatives.**
2. **It survives an adversarial-refutation pass** by a fresh-context reviewer instructed to look for confounds, data leaks, cherry-picked windows, or denominator mismatches.
3. **It was measured with exact numbers, never eyeballed.**

## 4. Regime honesty & idea lifecycle

- **State the regime ($R$), sample size ($N$), and conditions ($C$)** in which the result was measured. Never extrapolate silently to an out-of-distribution cohort without re-measuring.
- **Idea lifecycle:**
  - **Adopted:** Promoted through `do-task` gates; active formula/rule written in place in `docs/logic/<module>-<concern>.md`.
  - **Retired / Falsified:** Documented in `docs/investigations/<slug>.md` (`state: done`, with top `## Verdict & promoted rules` listing the fenced-off dead end) so future sessions never re-run the same failed experiment.

## Hard rules

- Never claim credit for an experimental result without a prior written numeric prediction and falsification threshold.
- Never trust a new evaluator or benchmark script until it passes a known-answer round-trip check.
- Never adopt an experimental change without an adversarial refutation check and `do-task` gates.
- Never spin in loops when an experiment yields a null or negative result — record the dead end in `docs/investigations/<slug>.md` or raise a `[DECISION]` gate in `docs/operator-instructions.md`.
- Treat operator distrust of a number (`"this looks wrong"`) as a first-class research trigger.

## Provenance and maintenance

Updated: 2026-10-11 (v2: added `tier: reference`, wired null-result handling to `operator-instructions` Decision gates and retired-idea storage to `docs/investigations/`).

Re-verification commands:
```bash
ls docs/investigations/ docs/operator-instructions.md
```
