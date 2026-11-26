---
name: validation-and-qa
tier: reference
description: >
  What counts as evidence and done: verify gate, done-when, no stubs, tests,
  failure triage, the bar for "it got better". Load BEFORE marking work done,
  writing tests, trusting "tests pass", running an experiment or answering "is
  this faster/better". Do NOT load for the loop (do-work).
trigger: /validation-and-qa
---

# /validation-and-qa

Done means the project's gate commands ran in this session and their output is visible. A description of what the code does, an unverified sub-agent claim and "should pass" are not evidence.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Driving a task through plan, execute and review | `do-work` |
| Deciding whether a leftover belongs to the task | `do-work` leftovers |
| Code quality and comment rules | `backend-code` |
| Explaining why a failure happens | `forensics` (which applies the prediction rules in section 7) |
| Raw vs. derived data audits | `data-integrity` |
| Evaluating an external library or API | `external-research` |

## 1. The gate

The gate commands come from the `verify` key of the project map (see `project-map`). Run them, and show the output. If the key is empty, ask the user through the question interface and record the answer in the map.

## 2. The done-when check

Run it once, before a task closes, after verify, review and docs. Cross-check the output against the task's goal, every done-when item and any expected outcome the plan named.

| Item | Evidence |
|---|---|
| `<done-when item>` | `<command and exit code, file:line, test name or review verdict>`, or `missed` |

A `missed` item is unfinished work: it goes back into the work loop with its targeted test and a delta review, never a second full suite. If it still cannot be met, the task stays open and the report says which item and why.

## 3. No stubs as done

A mock, hardcoded return, placeholder or fabricated value makes the feature undone. When scope forces a stub:

1. It returns an honest empty, null or unavailable state, never invented numbers.
2. Its name makes it visible (`_stub_` or `TODO_STUB` prefix).
3. It is filed as an open task via `tracker` and named in the completion report.

## 4. Test-writing discipline

- Test the invariant, not the implementation. Assert the behaviour, not that function X calls helper Y.
- Every bug fix gets a regression test that fails before the fix and passes after.
- Isolate test state from real state. Never touch a real raw data store in a test. Reuse the project's existing isolation fixture.
- A passing suite does not prove the measuring code is right. Check known-answer cases first.

## 5. Unexpected failures

When a test fails that the change should not affect, triage in three steps:

1. Run the full suite. Note whether it fails.
2. Run the test alone.
3. Run its file alone.

Fails everywhere: a real failure. Fails only in the full suite: order or shared-state pollution. Passes alone but fails with its file: a fixture or module-level problem. Compare with the baseline before blaming the change.

## 6. Honest reporting

- Paste the actual failing output: trace, assertion diff, failing test names.
- Report partial completion as partial, with what remains.
- Treat a sub-agent's "tests pass" as a claim. Rerun the gate, or check the literal command and exit code in its report block.

## 7. Claims of improvement

An unfalsifiable claim, an eyeballed "looks better", or a number from an unchecked instrument is noise.

### a. Predict before running

Record this before the run, in the task, through `tracker`:

```text
Hypothesis:   <mechanism: why this should change the outcome>
Predicts:     <direction> by <numeric band>        e.g. "p95 latency -20% to -35%"
Falsified if: <specific result that kills the claim>   e.g. "reduction under 10%"
```

Direction alone is not a prediction. If you cannot state a falsifying result, you have a hope, not a hypothesis.

### b. Validate the instrument first

Before trusting a new metric, evaluator, benchmark or audit script:

1. Run it on a known-answer case whose output you computed by hand, and confirm it reproduces that output.
2. Run it on a trivial case small enough to check by eye.
3. Only then run the real experiment. If either check fails, fix the instrument and the experiment waits.

### c. Acceptance bar

A claim is accepted only when all three hold. Otherwise label it unproven.

1. One mechanism explains every observation, including the negatives. Narrow the claimed scope until it does.
2. It survives a refutation pass by a reviewer with no stake in the result, instructed to look for confounds, leaks, cherry-picked windows and mismatched denominators. Brief that reviewer with `agent-brief`.
3. It was measured with exact numbers and units.

### d. Regime honesty

State the regime, the sample size and the conditions where the result was measured, in the write-up that carries it forward. Never extend it to a different cohort without measuring again.

### e. Null results are valid completions

When a clean run hits the falsifying condition or shows no real effect, record it and stop. Never re-run with tweaked parameters to force a win.

- Record the prediction and outcome on the task, through `tracker`.
- Record dead ends in the `investigations` key so no one repeats them.
- Hand a human judgment call over through `tracker`.
- Treat the user's distrust of a number as a research trigger.

## Hard rules

- Never set a numeric acceptance threshold after seeing the result.

## Provenance and maintenance

Updated: 2026-11-27.

Re-verification commands:
```bash
grep -n "verify" plugins/punchcard/skills/project-map/SKILL.md
grep -n 'Falsified if' plugins/coding/skills/validation-and-qa/SKILL.md
grep -n '^## Done when' plugins/project-management/skills/tracker/templates/task.md
```
