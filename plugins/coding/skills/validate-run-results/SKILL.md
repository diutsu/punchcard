---
name: validate-run-results
tier: reference
description: >
  The single home for the rules on proving that a change made something
  better: hypothesis, predicted numeric band and falsifying result written
  before the run, a validated measuring instrument, an acceptance bar, regime
  honesty, and null results as valid completions. Load BEFORE running an
  experiment, tuning a parameter, comparing two approaches, or answering "is
  this faster/better/more accurate". Differs from codebase-search (reading what
  already exists) and forensics (explaining why a failure happens, using these
  rules for its hypotheses). Do NOT load for turning a finding into a plan
  (see plan) or for judging external libraries (see external-research).
trigger: /validate-run-results
---

# /validate-run-results

An unfalsifiable claim, an eyeballed "looks better", or a number from an unchecked instrument is noise. This skill is the evidence bar for any claim of improvement or correctness.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Reading how existing code, docs and history work | `codebase-search` |
| Explaining why a failure happens | `forensics` (which applies the prediction rules below) |
| Turning an accepted result into a plan | `plan` |
| Evaluating a library or vendor outside the repo | `external-research` |
| Running the project's existing gate with no new claim | `validation-and-qa` |

## 1. Predict before running

Record this before the run, in the task through `backlog` or in the active plan:

```text
Hypothesis:   <mechanism: why this should change the outcome>
Predicts:     <direction> by <numeric band>        e.g. "p95 latency -20% to -35%"
Falsified if: <specific result that kills the claim>   e.g. "reduction under 10%"
```

Direction alone is not a prediction. If you cannot state a falsifying result, you have a hope, not a hypothesis.

## 2. Validate the instrument first

Before trusting a new metric, evaluator, benchmark or audit script:

1. Run it on a known-answer case whose output you computed by hand, and confirm it reproduces that output.
2. Run it on a trivial case small enough to check by eye.
3. Only then run the real experiment. If either check fails, fix the instrument and the experiment waits.

## 3. Acceptance bar

A claim is accepted only when all three hold. Otherwise label it unproven.

1. One mechanism explains every observation, including the negatives. Narrow the claimed scope until it does.
2. It survives a refutation pass by a reviewer with no stake in the result, instructed to look for confounds, leaks, cherry-picked windows and mismatched denominators. Brief that reviewer with `agent-brief`.
3. It was measured with exact numbers and units.

## 4. Regime honesty

State the regime, the sample size and the conditions where the result was measured, in the write-up that carries it forward. Never extend it to a different cohort without measuring again.

## 5. Null results are valid completions

When a clean run hits the falsifying condition or shows no real effect, record it and stop. Never re-run with tweaked parameters to force a win.

- Record the prediction and outcome through `backlog` or the active plan.
- Record dead ends in the `investigations` key so no one repeats them.
- Hand a human judgment call over through `backlog`.
- Treat the user's distrust of a number as a research trigger.

## Hard rules

- No prediction before the run means no credit for the result.
- No instrument is trusted before it reproduces a known answer.
- No claim of improvement on "looks better"; name the number.
- No adoption without a refutation pass and the normal `do-work` gates.
- Never loop on a null result.
- Every result states its regime, sample size and conditions.

## Provenance and maintenance

Updated 2026-11-13. Check commands:

```bash
grep -n "Falsified if" plugins/coding/skills/validate-run-results/SKILL.md
grep -rn "validate-run-results" plugins/coding/skills --include=SKILL.md -l
```
