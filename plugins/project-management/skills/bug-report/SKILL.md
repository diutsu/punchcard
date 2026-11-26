---
name: bug-report
tier: workflow
description: >
  File a new defect as a task: what goes on it, the expected behaviour, the docs
  that must change. Load when the user reports a defect or surprise outside the
  task in hand, or work turns one up. Do NOT load for the root cause
  (forensics), the fix (do-work) or product changes (product-direction).
trigger: /bug-report
---

# /bug-report

A report is filed once, complete enough that whoever fixes it never has to ask what "right" means. It records the problem and the expected behaviour. It claims no cause.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Explaining why it fails, or writing the report document | `forensics` |
| Fixing it now | `do-work` |
| The user wants different behaviour, not a repair | `product-direction` |
| A gap left by the task being worked | `do-work` leftovers |

## Procedure

1. **Check history.** Run the closed-before check from `forensics`. A match is handled per `tracker`.
2. **Capture what the repo can show.** Reproduce it per `forensics` (reproduce first). Ask the user only for what only they know.
3. **Settle the expected behaviour.** Look it up first: the `prd`, `design` and reference docs (per `project-map`) and the tests.

   | Finding | Action |
   |---|---|
   | A doc or test states it and the app differs | Expected = that text, quoted with its path |
   | Docs are silent or unclear | Ask the user what is right, recommended option first |
   | Docs and the user disagree | Show both texts; the user decides; a changed requirement goes to `product-direction` |

   Ask when the user reported the bug in their own message. When the agent found the defect or the user is away, do not stop: file it with the expected behaviour marked "unconfirmed" and the candidate options listed, and put the question in the end-of-work batch (recorded as an open question via `tracker` when away).
4. **Name the doc impact.** For each doc the decision makes wrong or missing, record the path, the section and the change: correct a statement, add the behaviour, create a doc (per `docs-management`, `doc-templates`). If none changes, say so and why.
5. **File it** via `tracker` `add`, on its task template:
   - goal: the expected behaviour holds
   - details: observed behaviour, reproduction steps someone else can run verbatim, scope and frequency, the doc impact
   - done-when: the reproduction passes, a test pins the behaviour, each doc change is made, and, if unconfirmed, the expected behaviour is confirmed
   - refs: the files and docs involved
6. **Place it** per the session card. If it blocks the task in hand, `block` that task on the new one via `tracker`, put the priority call in the end-of-work batch, and move to the next unblocked item.

## Hard rules

- Never put a cause in the report unless `forensics` established it.
- Never start the fix in the same step as the report.

## Provenance and maintenance

Updated: 2026-11-27.

Re-verification commands:
```bash
for s in forensics tracker docs-management doc-templates product-direction do-work; do ls -d plugins/*/skills/$s >/dev/null || echo "missing $s"; done
grep -n 'bug-report' plugins/punchcard/skills/capability-check/SKILL.md README.md
```
