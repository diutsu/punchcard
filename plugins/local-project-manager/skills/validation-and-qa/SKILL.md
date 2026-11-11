---
name: validation-and-qa
tier: reference
description: >
  What counts as evidence and definition-of-done for any coding task. Load this
  BEFORE marking any task, step, or sub-agent handoff "done"; before writing or
  reviewing tests; when a completion claim arrives ("tests pass", "should
  work", "implemented X"); when deciding whether a stub/mock/placeholder is
  acceptable to ship; when setting acceptance thresholds for an experiment or
  benchmark. Trigger phrases: "is this done", "mark complete", "run the tests",
  "should work", "I think it passes", "write a test for", "spot-check the
  agent's work". Do NOT load for the mechanics of driving a task end-to-end
  (see do-task) or for code style/module boundaries (see code-discipline).
trigger: /validation-and-qa
---

# /validation-and-qa

**Definition of done = the project's gate command, executed in this session, output shown.** Nothing else counts. Not `"should pass"`, not a description of what the code does, not an unverified sub-agent claim.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Driving a task through plan $\rightarrow$ execute $\rightarrow$ commit end-to-end | `do-task` |
| Code quality, module boundaries, and comment rules | `code-discipline` |
| Evaluating an external library, model, or API | `external-research` |
| Auditing raw-vs-derived data stores or building a reconciliation script | `data-integrity` |

## 1. The gate is the definition of done

Every project has **one real gate command**. Discover it in this order, run it, and paste the output:
1. Read the project's `CLAUDE.md` (`Environment & Gate Commands`).
2. Look for a single aggregate script in `package.json` (`scripts.verify`), `pyproject.toml`, or `Makefile`.
3. Fall back to the language's native test runner if no aggregate exists.

`"Should work"` and `"tests should pass"` are invalid claims until the command has actually been executed in this session and its output is visible.

## 2. No stubs-as-done

A mock, hardcoded return value, placeholder, or fabricated data point makes the feature **undone**.

**Rule:** If scope genuinely forces a stub:
1. It must return an honest empty/null/unavailable state — never invented numbers or a plausible-looking fake. Name the function/variable so the stub is visible on sight (`_stub_` / `TODO_STUB` prefix).
2. It must be flagged **loudly**: an open entry in `docs/tasks.md` (via `ctask add`) describing what is stubbed and why, **and** an explicit line in the completion report.

## 3. Acceptance thresholds are numeric and set before running

State the pass/fail bar — a number, a percentage, or `"0 regressions vs. baseline N passed"` — **before** running the gate or experiment. Setting the bar after seeing the result is rationalization, not verification.

**Validate the measuring instrument itself, not just that it runs.** A test suite that only asserts an evaluator's internal arithmetic never checks whether that arithmetic matches reality (see `research-methodology` §3, Yardstick-first rule).

## 4. Test-writing discipline

- **Test the invariant, not the implementation.** Assert the behavioral property from `docs/requirements/<module>.md` or `docs/logic/<module>-<concern>.md`, not `"function X calls helper Y"`.
- **Every bug fix gets a regression test that fails before the fix and passes after.**
- **Isolate test state from real state.** Never touch the real raw data store or production DB in tests. Reuse the project's existing test isolation fixture (`tests/conftest.py` or test setup file) rather than inventing a second isolation mechanism.

## 5. Honest failure and partial-completion reporting

- Paste the **actual failing output** — stack trace, assertion diff, failing test names. Never summarize a failure away.
- Report partial completion as **partial** with what remains outstanding — never round up to `"done"`.

## 6. Spot-check sub-agent completion claims

A sub-agent saying `"tests pass"` is a claim, not evidence, until you either:
1. **Rerun the gate yourself** against the resulting state, or
2. **Verify the literal command and exit output** in the step report (`code-task` format).

## Hard rules

- Never write or relay `"should work"`, `"should pass"`, or `"looks correct"` as a completion claim — run the gate and show the output.
- Never let a mock, stub, or fabricated value ship silently — prefix with `_stub_`, file a `ctask` entry, and flag it in the report.
- Never treat a green test suite as proof the yardstick itself is calibrated — verify known-answer cases first.
- Never set a numeric acceptance threshold after seeing the result.
- Never touch a real raw data source to make a test pass — use isolated test fixtures.

## Provenance and maintenance

Updated: 2026-10-11 (v2: added `tier: reference`, updated doc pointers to `docs/requirements/` and `docs/logic/`, removed retired `executed-*.md` references).

Re-verification commands:
```bash
ls docs/requirements/ docs/logic/
```
