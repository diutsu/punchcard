---
name: plan
tier: leaf
description: >
  Turn accepted research into an execution plan an agent can run without
  re-deriving anything: ranked solution menu, fenced-off wrong paths,
  numbered steps with exact expected results, at most 150 lines, with phase
  roll-forward. Load after research concludes and before any multi-step or
  multi-file change. Do NOT load when there is no finding yet (see
  codebase-search, external-research, forensics), for a one-file obvious edit
  (use a 3-5 line inline plan), or to execute a plan (see do-work).
trigger: /plan
---

# /plan

Research produces a finding. This skill turns it into a plan with every command, expected result and dead end already resolved. It writes the plan and stops; `do-work` runs it.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| No finding yet | `codebase-search`, `external-research`, `forensics` |
| Judging whether a claim of improvement is proven | `validate-run-results` |
| Judging whether a step is done | `validation-and-qa` |
| Executing, reviewing and closing the plan | `do-work` |
| Choosing which task to plan | `prioritise` |

## Where the plan lives

On its task: a `## Plan` section in the description, written via `backlog`. One plan per task. Work with no task keeps its plan in the conversation.

## Sizing

| Size | Form |
|---|---|
| One file, obvious edit, no decision | Inline plan in the kickoff message: goal, exact commands, measurable done state. Nothing saved on the task. |
| Several files or phases, a real choice between approaches, or a dead end worth fencing | Full plan on the task, from `./templates/plan.md`. |

An inline plan is the same anatomy compressed. It still states an exact expected result.

## Anatomy

1. **Context.** Problem and evidence. Every claim cites a doc, commit or log line. A hunch is not evidence; send it back through `validate-run-results`.
2. **Solution menu, ranked.** Only when more than one approach is viable. For each option state what must be true for it to work and the concrete check that verifies it. Mark an unverifiable premise `open`.
3. **Fenced-off wrong paths.** Each known dead end, with its reason, one bullet. Cite an incident or investigation instead of retelling it.
4. **Steps.** Each step has: the exact command, the exact expected number, string or exit code, and the branch to take when reality differs. Pin functions and line ranges; state the behaviour each step must produce.
5. **Test strategy.** Baseline count and commit before execution, target after. Pass or fail is a diff.
6. **Risks and rollback.** One line per step that needs it.

## Size discipline

- The plan never exceeds 150 lines.
- **Phase roll-forward.** Detail only the active phase. List later phases as one-line placeholders. When a phase lands, replace its step block with one line under "Completed phases": summary and commit hash.
- Deep scoping goes to `investigations`, linked by one line.
- Shipped behaviour belongs in the docs (`docs-management`), not the plan.

## Hard rules

- Never write a step gate without an exact expected result.
- Never exceed 150 lines or detail more than one unexecuted phase.
- Never list a fenced-off path that is a hypothesis; each traces to an incident or finding.
- Never execute, score or commit the plan; that is `do-work`.
- Never restate review or gate mechanics in the plan; cite `review-rubric` and `validation-and-qa`.
- Never save a plan as a file.

## Provenance and maintenance

Updated: 2026-11-25.

```bash
wc -l plugins/project-management/skills/plan/templates/plan.md
grep -n 'plan' plugins/project-management/skills/backlog/SKILL.md
```
