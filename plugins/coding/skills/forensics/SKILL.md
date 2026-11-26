---
name: forensics
tier: leaf
description: >
  Find the root cause of a failure, bug, wrong number or surprise before any
  fix. Load BEFORE a fix or theory: "why is this wrong", "this used to work",
  "flaky test", "debug this", or a written bug report. Do NOT load with no
  failure (codebase-search) or to fix it (do-work).
trigger: /forensics
---

# /forensics

An investigation is an experiment-design problem. Reproduce, check history, enumerate hypotheses, and run the cheapest experiment that splits them. The prediction and falsification rules live in `validation-and-qa`; apply them to every hypothesis here.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| No failure in hand, only "how does X work" | `codebase-search` |
| Proving a change made something better | `validation-and-qa` |
| Deciding whether to replace or report a third-party library | `external-research` |
| Fixing the confirmed cause | `do-work` |
| Filing a newly reported defect with its expected behaviour | `bug-report` |
| Raw-versus-derived reconciliation mechanics | `data-integrity` |

## Procedure

1. **Reproduce first.** Get the exact input, command, expected output and actual output. Reduce to the smallest case: one record, one date, one request. Run the project's real command (from the project instructions file `AGENTS.md`/`CLAUDE.md` or manifest). If it does not reproduce, say so; the task is then "build a reproduction". Re-ask vague reports for specifics.
2. **Was this investigated and closed before?** Search task history through `tracker` and past reports in the `investigations` key (locate with `project-map`). An open item: extend it, do not duplicate it. A closed item or report: read what was tried. If the failure returned, treat it as a regression against that specific fix and name the fix. If the project has no such records, check commit history for the affected file.
3. **Enumerate hypotheses.** Fill the table below before touching code. Each row needs a predicted value and one observation that only that hypothesis explains. Two hypotheses that predict the same observation are one hypothesis until sharpened.
4. **Run the cheapest discriminating experiment**, read-only where possible (log a value, query the store, grep the config). Pick the experiment that splits the remaining space, not the one that confirms the favourite.
5. **Apply the acceptance bar** and write the result back.

| Hypothesis | Predicts, before running | Discriminating observation |
|---|---|---|
| H1: `<mechanism>` | `<exact value or state>` | `<what only H1 explains>` |

Check these classes first: stale values (who invalidates this store, and did that run), transform or unit artefacts (normalisation, currency, timezone), and untrusted source data (count the input against independent ground truth, see `data-integrity`).

## Root-cause acceptance bar

- One mechanism explains every observation, including the negatives: state "this explains why A failed and why B and C did not, because `<reason>`".
- The fix prediction is confirmed: after the fix, the original reproduction from step 1 passes, not a paraphrase of it.
- A fix that passes but cannot be explained is a patch. Label it so and do not claim closure.

## Write the result back

- Fix now: hand the confirmed cause to `do-work`. The root cause and discriminating evidence go in the commit message.
- Fix later: file a task via `tracker` with the hypothesis table and discriminating observation in the details.
- Report or dead ends worth keeping: write to the `investigations` key.

## Bug report

When the user asks for a written bug report document with the root cause, write it from `./templates/bug-report.md` into the `investigations` key. Fill every section: title, environment and versions, reproduction steps someone else can run verbatim, expected versus actual with exact output, frequency, root cause with evidence (or "not yet established" plus the hypotheses ruled out), scope of impact, workaround, suggested fix. Frontmatter follows `docs-management`.

## Hard rules

- Never propose a fix before a reproduction exists.
- Never skip the closed-before check.
- Every hypothesis predicts a value before its experiment runs.
- Never declare a root cause without explaining the passing cases.
- Never leave a confirmed bug unrecorded: fix it or file it.
- Fixing goes through `do-work`; this skill stops at a written root cause.

## Provenance and maintenance

Updated: 2026-11-26. Check commands:

```bash
ls plugins/coding/skills/forensics/templates/bug-report.md
grep -n "validation-and-qa" plugins/coding/skills/forensics/SKILL.md
```
