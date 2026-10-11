---
name: progress-log
tier: leaf
description: >
  Append one terse, dated entry to a project's docs/progress-log.md when
  something genuinely significant happens — substantial development landing,
  a real operational event, a major product decision, or a feature shipping.
  Strict single-line template: date+time, one of four closed categories,
  <=250 chars of free text. NOT for routine task progress (ctask/tasks.md
  owns that), git commits (git log owns that), config changes, or minor bug
  fixes. Load when the user asks to log/record progress, or when you have
  just landed something that clears the "would this be worth its own task"
  significance bar.
trigger: /progress-log
---

# /progress-log

`docs/progress-log.md` is a **curated highlight reel**, not a diary. A reader scans it in under a minute and knows the handful of things that mattered recently.

## When NOT to use this skill

| Situation | Owner instead |
|---|---|
| Routine task progress ("started X", "step 3 of 7 done") | `docs/tasks.md` / `docs/done.md` (`ctask`) |
| What changed in code and when | `git log` |
| Config changes, threshold tuning, constant tweaks | commit message; nothing else |
| Minor bug fixes | commit message; nothing else |
| Deep root-cause or spike analysis | `docs/investigations/<slug>.md` (log gets one pointer line if significant) |

## The significance bar

Log an event only if it clears roughly "this would be worth filing as its own `ctask` entry." Not every closed task — events at that scale of consequence. When in doubt, skip it.

## Categories — closed set, exactly four

- **development** — substantial implementation work landed: a redesigned subsystem, a production-outage fix, a real refactor.
- **operation** — a real operational event: an incident, a production migration run, a deliberate job kill, a data recovery, an infra move.
- **major-product-decision** — a durable decision about what the product does or is scoped to do.
- **new-feature** — a feature now live and usable.

## The entry template — strict, no exceptions

One line per entry, newest first, directly under the title's one-line goal:

```markdown
- `YYYY-MM-DD HH:MM` **[category]** Free text, max 250 characters.
```

- **Date+time**: local wall-clock, 24h (`YYYY-MM-DD HH:MM`).
- **Category**: one of the four above, in brackets, bolded.
- **Free text**: $\le 250$ characters. State the outcome, not the process. If 250 characters is too tight, put the detail in `docs/investigations/<slug>.md` and cite it in the one-liner.

## Hard rules

- Never log routine task progress, individual commits, config changes, or minor fixes.
- Never exceed one line / 250 characters per entry.
- Never use a category outside the closed set of four.
- Never rewrite or delete existing entries; the log is append-only.
- Always bump `updated:` in `docs/progress-log.md` frontmatter to today.

## Provenance and maintenance

Updated: 2026-10-11 (v2: removed retired `executed-<slug>.md` references in favor of `docs/done.md` and `docs/investigations/`).

Re-verification commands:
```bash
ls doc-templates/docs/progress-log.md
```
