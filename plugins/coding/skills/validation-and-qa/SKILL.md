---
name: validation-and-qa
tier: reference
description: >
  What counts as evidence and as done for any coding task. Load BEFORE marking
  a task, step or sub-agent handoff done, before writing or reviewing tests,
  when a completion claim arrives ("tests pass", "should work"), and when
  deciding whether a stub or placeholder may ship. Covers the verify gate,
  no-stubs-as-done, test-writing discipline, honest failure reporting and the
  triage of unexpected failures. Do NOT load for the work loop (see do-work),
  code style (see backend-code), or experiment and benchmark thresholds (see
  validate-run-results).
trigger: /validation-and-qa
---

# /validation-and-qa

Done means the project's gate commands ran in this session and their output is visible. A description of what the code does, an unverified sub-agent claim and "should pass" are not evidence.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Driving a task through plan, execute and review | `do-work` |
| Code quality and comment rules | `backend-code` |
| Acceptance thresholds for experiments and benchmarks | `validate-run-results` |
| Raw vs. derived data audits | `data-integrity` |
| Evaluating an external library or API | `external-research` |

## 1. The gate

The gate commands come from the `verify` key of the project map (see `project-map`). Run them, and show the output. If the key is empty, ask the user through the question interface and record the answer in the map.

## 2. No stubs as done

A mock, hardcoded return, placeholder or fabricated value makes the feature undone. When scope forces a stub:

1. It returns an honest empty, null or unavailable state, never invented numbers.
2. Its name makes it visible (`_stub_` or `TODO_STUB` prefix).
3. It is filed as an open task via `tracker` and named in the completion report.

## 3. Test-writing discipline

- Test the invariant, not the implementation. Assert the behaviour, not that function X calls helper Y.
- Every bug fix gets a regression test that fails before the fix and passes after.
- Isolate test state from real state. Never touch a real raw data store in a test. Reuse the project's existing isolation fixture.
- A passing suite does not prove the measuring code is right. Check known-answer cases first.

## 4. Unexpected failures

When a test fails that the change should not affect, triage in three steps:

1. Run the full suite. Note whether it fails.
2. Run the test alone.
3. Run its file alone.

Fails everywhere: a real failure. Fails only in the full suite: order or shared-state pollution. Passes alone but fails with its file: a fixture or module-level problem. Compare with the baseline before blaming the change.

## 5. Honest reporting

- Paste the actual failing output: trace, assertion diff, failing test names.
- Report partial completion as partial, with what remains.
- Treat a sub-agent's "tests pass" as a claim. Rerun the gate, or check the literal command and exit code in its report block.

## Hard rules

- Never write "should work" or "looks correct" as a completion claim.
- Never ship a mock or fabricated value silently.
- Never set a numeric acceptance threshold after seeing the result.
- Never touch a real raw data source to make a test pass.
- Never summarise a failure away.

## Provenance and maintenance

Updated: 2026-11-26.

Re-verification commands:
```bash
grep -n "verify" plugins/punchcard/skills/project-map/SKILL.md
ls plugins/coding/skills/validate-run-results/SKILL.md
```
