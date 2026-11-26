---
name: plan
tier: leaf
description: >
  Write a short execution plan for one session: how the engineer starts on a
  refined task and applies the code, with options when there is a real
  choice, fenced-off wrong paths, and numbered steps with exact expected
  results, at most 60 lines. Load in do-work once the task is in progress, or
  before any multi-file change without a task. Do NOT load to settle the goal
  or done-when (that is refinement, see tracker), for a one-file obvious edit
  (use a 3-5 line inline plan), to execute a plan (see do-work), or for a
  roadmap or a planning doc (see product-direction, doc-templates).
trigger: /plan
---

# /plan

Refinement settles what must change: the goal, the details and the done-when are on the task before it reaches to do. This skill settles how: where the engineer starts, the order of changes, the commands and expected results, and the dead ends to avoid. Short enough for the user to review in one read. It writes the plan and stops; `do-work` runs it.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| No finding yet | `codebase-search`, `external-research`, `forensics` |
| Judging whether a step is done or a claim is proven | `validation-and-qa` |
| Executing, reviewing and closing the plan | `do-work` |
| Choosing which task to work on | `prioritise` |
| Settling the goal, details or done-when | refinement, via `tracker` |
| Order and timing of work across sessions | the task tracker, via `tracker` |

## Where the plan lives

One scratch file for the session, outside the repo, so sub-agent briefs can pass its path. It is never committed and never saved on the task. `do-work` deletes it when the task closes or is handed off; the handoff (per `tracker`) holds the next step, and the next session writes a new plan from there.

The task's goal and done-when are the plan's goal and acceptance criteria; the plan cites them and never restates them. Work with no task puts its goal and done-when at the top.

## Questions and notes for the task

Planning may turn up what the code cannot answer. Ask it as an open question per `tracker`; it never reopens refinement. Small notes that would help the implementation (a seam, a gotcha, a test to reuse) go on the task as one comment.

## Sizing

| Size | Form |
|---|---|
| One file, obvious edit, no decision | Inline plan in the kickoff message: goal, exact commands, measurable done state. |
| Several files, a real choice between approaches, or a dead end worth fencing | Full plan from `./templates/plan.md`. |

An inline plan is the same anatomy compressed. It still states an exact expected result.

## Anatomy

1. **Starting point.** What the code looks like now, where the change goes in, a few sentences. Each claim rests on one anchor: a doc, commit or log line. A hunch is not evidence; test it per `validation-and-qa`.
2. **Solution menu, ranked.** Only when more than one approach is viable. For each option state what must be true for it to work and the concrete check that verifies it. Mark an unverifiable premise `open`.
3. **Fenced-off wrong paths.** Each known dead end, with its reason, one bullet. Cite an incident or investigation instead of retelling it.
4. **Steps.** Each step has: the behaviour it must produce, in words; the exact command; the exact expected number, string or exit code; and the branch to take when reality differs. Name the one file or function it changes.
5. **Test strategy.** Baseline count and commit before execution, target after. Pass or fail is a diff.
6. **Risks and rollback.** One line per step that needs it.

## Writing

The plan is read by the user, so it is written in the session's output style: short, dense sentences, one idea each, no filler.

- Describe behaviour in words. A reader should follow the plan without opening a file.
- Use a few anchors, not many: about one file, function or commit per step or claim. A line where half the words are links is harder to read than the code it points at.
- Never paste code into a plan. Point at it once.
- Never cite another plan; cite the finding, doc or commit it rested on.

## Review

Show the plan to the user. Wait for approval only when it carries a real choice between approaches, a risk worth a rollback line, or crosses module boundaries. A solid, simple plan is shown and work proceeds. In `away-mode`, record the plan in the decisions log and proceed.

## Size discipline

- The plan never exceeds 60 lines.
- Work too big for one session is split: plan only what this session will do, and list the rest as one-line notes for the handoff. They are not filed as tasks.
- Deep scoping goes to `investigations`, linked by one line.
- Shipped behaviour belongs in the docs (`docs-management`), not the plan.

## Hard rules

- Never write a step gate without an exact expected result.
- Never anchor more than about one reference per step or claim.
- Never exceed 60 lines or plan beyond this session's work.
- Never list a fenced-off path that is a hypothesis; each traces to an incident or finding.
- Never execute, score or commit the plan; that is `do-work`.
- Never restate review or gate mechanics in the plan; cite `review-rubric` and `validation-and-qa`.
- Never save a plan on a task, commit it, or leave its file behind after the task closes or is handed off.

## Provenance and maintenance

Updated: 2026-11-26.

Re-verification commands:
```bash
wc -l plugins/coding/skills/plan/templates/plan.md
grep -n '^## Goal\|^## Done when' plugins/project-management/skills/tracker/templates/task.md
grep -n 'Next step' plugins/project-management/skills/tracker/templates/handoff.md
```
