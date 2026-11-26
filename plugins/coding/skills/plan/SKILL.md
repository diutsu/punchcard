---
name: plan
tier: leaf
description: >
  Write a short execution plan for the work this session will do, for the user
  to review before it runs: what the work serves, ranked options when there is
  a real choice, fenced-off wrong paths, and numbered steps with exact expected
  results, at most 60 lines. Load after research concludes and before any
  multi-step or multi-file change. Do NOT load when there is no finding yet
  (see codebase-search, external-research, forensics), for a one-file obvious
  edit (use a 3-5 line inline plan), to execute a plan (see do-work), or for
  a roadmap or a planning doc (see product-direction, doc-templates).
trigger: /plan
---

# /plan

Research produces a finding. This skill turns it into a plan for this session, with every command, expected result and dead end already resolved, short enough for the user to review in one read. It writes the plan and stops; `do-work` runs it.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| No finding yet | `codebase-search`, `external-research`, `forensics` |
| Judging whether a claim of improvement is proven | `validate-run-results` |
| Judging whether a step is done | `validation-and-qa` |
| Executing, reviewing and closing the plan | `do-work` |
| Choosing which task to work on | `prioritise` |
| Order and timing of work across sessions | the task tracker, via `tracker` |

## Where the plan lives

In the conversation. It covers this session's work and is not saved on the task or in a file. The task's goal and done-when are the plan's goal and acceptance criteria; the plan cites them and never restates them. Work with no task puts its goal and done-when at the top.

When work carries into another session, the handoff (per `tracker`) holds the next step. The next session writes a new plan from there.

## Sizing

| Size | Form |
|---|---|
| One file, obvious edit, no decision | Inline plan in the kickoff message: goal, exact commands, measurable done state. |
| Several files, a real choice between approaches, or a dead end worth fencing | Full plan from `./templates/plan.md`. |

An inline plan is the same anatomy compressed. It still states an exact expected result.

## Anatomy

1. **Context.** Problem and evidence. Every claim cites a doc, commit or log line. A hunch is not evidence; send it back through `validate-run-results`.
2. **Solution menu, ranked.** Only when more than one approach is viable. For each option state what must be true for it to work and the concrete check that verifies it. Mark an unverifiable premise `open`.
3. **Fenced-off wrong paths.** Each known dead end, with its reason, one bullet. Cite an incident or investigation instead of retelling it.
4. **Steps.** Each step has: the exact command, the exact expected number, string or exit code, and the branch to take when reality differs. Pin functions and line ranges; state the behaviour each step must produce.
5. **Test strategy.** Baseline count and commit before execution, target after. Pass or fail is a diff.
6. **Risks and rollback.** One line per step that needs it.

## Review

Show the full plan to the user and wait for approval before execution. An inline plan is shown in the kickoff and does not wait. In `away-mode`, record the plan in the decisions log and proceed.

## Size discipline

- The plan never exceeds 60 lines.
- Work too big for one session is split: plan only what this session will do, and list the rest as one-line follow-ups.
- Deep scoping goes to `investigations`, linked by one line.
- Shipped behaviour belongs in the docs (`docs-management`), not the plan.

## Hard rules

- Never write a step gate without an exact expected result.
- Never exceed 60 lines or plan beyond this session's work.
- Never list a fenced-off path that is a hypothesis; each traces to an incident or finding.
- Never execute, score or commit the plan; that is `do-work`.
- Never restate review or gate mechanics in the plan; cite `review-rubric` and `validation-and-qa`.
- Never save a plan on a task or as a file.

## Provenance and maintenance

Updated: 2026-11-26.

Re-verification commands:
```bash
wc -l plugins/coding/skills/plan/templates/plan.md
grep -n '^## Goal\|^## Done when' plugins/project-management/skills/tracker/templates/task.md
grep -n 'Next step' plugins/project-management/skills/tracker/templates/handoff.md
```
