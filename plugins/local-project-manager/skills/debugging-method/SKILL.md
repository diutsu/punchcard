---
name: debugging-method
tier: leaf
description: >
  The investigation process for any bug, wrong number, unexpected behavior, or
  regression — load this BEFORE writing a fix or forming a theory about why
  something is broken. Trigger phrases: "why is this wrong", "this number looks
  off", "X used to work and now doesn't", "unexpected behavior", "the test is
  flaky", "debug this", "investigate why", "regression in", "the output doesn't
  match". Covers reproducing the failure, checking the failure ledger
  (docs/tasks.md, docs/done.md, docs/investigations/), enumerating hypotheses
  with a discriminating experiment for each, and the acceptance bar for calling
  a root cause found. Do NOT load for evaluating external libraries (use
  external-research), mining the repo with no bug in hand (use
  internal-research), or raw-vs-derived data reconciliation mechanics once
  confirmed (use data-integrity).
trigger: /debugging-method
---

# /debugging-method

A bug investigation is an experiment design problem, not a reading-comprehension problem. Do not skim the code and guess — reproduce, check history, enumerate hypotheses, and run the cheapest experiment that splits them.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| No bug in hand, just "how does X work" | `internal-research` |
| Evaluating whether to replace/adopt a third-party library or API | `external-research` |
| Deciding whether a fix meets the definition of done | `validation-and-qa` |
| Reconciling raw vs. derived data stores once a data bug is confirmed | `data-integrity` |
| Turning a confirmed root cause into a multi-step execution plan | `research-to-plan` / `do-task` |

## 1. Reproduce first

Never theorize before a failing case exists in front of you. If you cannot reproduce it, the task is "build a reproduction," not "guess a cause."
- Get the exact input, command, and expected-vs-actual output.
- Reduce to the smallest reproducing case — one record, one date, one transaction, not the whole pipeline run.
- Run the project's actual test or CLI command to reproduce (discovered via `CLAUDE.md` or manifest).
- If it does not reproduce, report that honestly rather than inventing a story.

## 2. Consult the failure ledger before investigating

Before forming any hypothesis, check whether this bug was already found, fixed, or deferred:

```bash
# Open and closed tasks via ctask
ctask search "<keyword>"

# Past investigations and root-cause records
grep -rln "<keyword>" docs/investigations/ docs/done.md
```

- If it matches an open `tasks.md` item: read its `Goal`/`Details` via `ctask show <ID>` and extend or execute it rather than duplicating analysis.
- If it matches a closed item in `docs/done.md` or `docs/investigations/`: read what was tried previously. If the bug returned, treat it as a **regression against that specific fix**.

## 3. Hypothesis table method

Enumerate candidate mechanisms before touching code. For each, state the **one observation that discriminates it** from every other hypothesis:

| Hypothesis | Predicts (a number/value, before running) | Discriminating observation |
|---|---|---|
| H1: `<mechanism>` | `<exact predicted value/state>` | `<what only H1 explains>` |
| H2: `<mechanism>` | `<exact predicted value/state>` | `<what only H2 explains>` |

Rules:
- **Every hypothesis must predict a specific value or state before you run the check.** `"Probably a caching issue"` is not a hypothesis; `"if it is the cache, `dataVersion` will be $N-1$ instead of $N$"` is.
- Run the **single cheapest read-only check** (log a value, query the DB, inspect config) that splits the hypothesis space in half.
- Check the three common bug classes first:
  1. **Stale-value / cache invalidation:** Who invalidates or syncs this store, and did that trigger fire?
  2. **Transform / unit mismatch:** Is this a normalization/denormalization or currency/unit artifact rather than a model failure?
  3. **Untrusted source data:** Count the raw input against independent ground truth (`data-integrity`).

## 4. The acceptance bar

One mechanism must explain **all** observations — including the negatives (`"why did A fail while B and C succeeded?"`).
- Before declaring root cause, complete the sentence: `"This explains why A failed AND why B/C did not, because ___."`
- Re-run the exact reproduction from §1 after applying the fix.

## 5. Write the result back

Every investigation leaves a durable trace:
- **Fixing now:** Land the fix + regression test via `do-task` / `code-task`. If documented behavior or a domain hazard rule changed, update `docs/requirements/<module>.md` or `docs/logic/<module>-<concern>.md` in place (timeless present tense, per `docs-management`).
- **Deferring the fix:** File a task via `ctask add` including the hypothesis table and discriminating observation in `--details`.
- **Non-trivial root cause or dead ends worth preserving:** Write `docs/investigations/<slug>.md` (`type: investigation`, `state: done`) with a top `## Verdict & promoted rules` block ($\le 10$ lines) and link it from `docs/logic/` or `docs/requirements/` via a 1-line `> **Guardrail:**` note.

## Hard rules

- Never propose a fix before reproducing the failure.
- Never skip the `ctask search` and `docs/investigations/` failure-ledger check.
- Every hypothesis must predict a concrete value/state before its check runs.
- Never declare a root cause found without explaining why passing cases did *not* fail.
- Never leave a confirmed bug undocumented — fix it, or file it via `ctask add`.

## Provenance and maintenance

Updated: 2026-10-11 (v2: added `tier: leaf`, replaced `executed-*.md` lookups with `ctask search`, `docs/done.md`, and `docs/investigations/`).

Re-verification commands:
```bash
ls docs/done.md docs/investigations/
```
