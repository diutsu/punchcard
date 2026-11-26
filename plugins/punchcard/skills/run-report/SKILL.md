---
name: run-report
tier: leaf
description: >
  Report a long-running or one-shot operation's outcome: outcome first, then
  steps, decisions, what was verified, what is left, where things are. Load at
  the end of a long run, a batch of work or an `away-mode` session. Do NOT load
  for a short answer, a review verdict or changelog entries.
trigger: /run-report
---

# /run-report

The reader was not watching. Let them learn the result in ten seconds and the reasoning in two minutes.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Logging a milestone | `changelog` |
| A reviewer's verdict on a diff | `review-rubric` |
| Prose style questions | `writing-style` |
| Delivering a short answer in chat | Answer directly |

## Structure

Use `./templates/run-report.md`. Sections in order:

1. **Outcome.** Two or three sentences: what was asked, what happened, whether it is done. State failure plainly.
2. **Needs you.** Items only the user can do, each with the file or task comment. Leave the section out only if there are none, and say so in the outcome.
3. **Steps.** One short section per step: what was done, and why. Name the files touched.
4. **Decisions taken.** From the decisions log if `away-mode` was used: question, option taken, why, alternative, how to reverse.
5. **Verified.** What was checked and how: the command, its exit code, the signal. Separate what was verified from what was assumed.
6. **Left over.** Unfinished work, filed tasks, known gaps.
7. **Where things are.** Paths to changed files, branches, logs and the tasks touched.

## Procedure

1. Collect facts from the repo, logs and the decisions log. Do not rely on memory of the run.
2. Write the outcome last in effort, but first on the page.
3. Add a diagram when structure or flow reads faster as a picture: an architecture change, a pipeline, a before and after. Draw only the real mechanism. Put it inline as SVG or Mermaid where the destination renders it.
4. Add a short interactive page when the reader needs to explore, such as filtering many results or comparing options. Keep it one self-contained file and link it from "Where things are".
5. Follow `writing-style` for prose: plain words, active voice, one idea per sentence, no filler.
6. Save the report under the `docs` root's investigations area per `project-map` when the user wants it kept, otherwise show it in chat.

## Hard rules

- Never include credentials or private data.
- Never pad with a recap of obvious steps. Each step section earns its place by what it explains.

## Provenance and maintenance

Updated: 2026-11-27.

Re-verification commands:
```bash
ls plugins/punchcard/skills/run-report/templates
grep -c '^## ' plugins/punchcard/skills/run-report/templates/run-report.md
```
