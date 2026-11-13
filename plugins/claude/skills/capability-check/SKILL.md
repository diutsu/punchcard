---
name: capability-check
tier: workflow
description: >
  Short self-evaluation before starting a high-value, underspecified
  deliverable (tooling, a one-shot artifact, a redesign, re-documentation).
  Scores whether this session has the knowledge and installed skills to produce
  a high-quality, non-generic result alone, then exits to proceed, to
  `grilling`, or to a search for a missing skill or plugin. Load when such a
  request arrives with gaps. Do NOT load for small or fully specified work.
trigger: /capability-check
---

# /capability-check

A generic result from a vague request wastes the user's time. Before building something large, spend one short pass deciding whether you can do it well alone.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| The request is fully specified or small | Start the work |
| You already know the gap is the user's intent | `grilling` |
| The user is away | `away-mode` (take defaults, log them) |
| Adding a known candidate plugin to the list | `watchlist` |

## Procedure

1. **Score five criteria from 0 to 2.** Write the score and one phrase of evidence for each.

   | Criterion | 2 means |
   |---|---|
   | Intent | Audience, purpose and success test are stated or inferable from the repo |
   | Domain knowledge | You know the domain well enough to avoid textbook filler |
   | Project fit | You have read the existing conventions, code or docs this must match |
   | Skills | An installed skill covers the craft (visuals, writing, review, testing) |
   | Verification | You can check the result yourself against a real signal |

2. **Pick the exit.**

   | Score | Exit |
   |---|---|
   | 9-10, no criterion at 0 | **Proceed.** |
   | Low on Intent or Project fit | **Run `grilling`.** Look up facts first so the questions are only decisions. |
   | Low on Domain knowledge or Skills | **Search for a missing skill or plugin** (below). |
   | Several low, mixed | Search first, then `grilling` with what the new skill reveals. |

3. **Search.** Check `watchlist` first. Then check the skills and plugins in the installed marketplaces. Match the missing craft to a candidate by its description.
4. **Propose, do not install.** Ask the user through the question interface whether to install the candidate, with the recommendation first. Install and record the outcome through `watchlist`.
5. **State the result** in two lines: the exit taken and the one criterion that drove it.

## Hard rules

- Never exceed one short pass. This check is a gate, not a project.
- Never score Verification above 0 without naming the signal you will check.
- Never install a plugin without the user's confirmation unless they asked for it.
- Never ask the user for facts you can read from the repo.

## Provenance and maintenance

Updated: 2026-11-13.

Re-verification commands:
```bash
grep -n 'grilling\|watchlist' plugins/claude/skills/capability-check/SKILL.md
ls plugins/claude/skills/grilling plugins/claude/skills/watchlist
```
