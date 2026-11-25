---
name: whats-next
tier: leaf
description: >
  Summarise the work in flight: the in-progress and in-review tasks assigned
  to the user or waiting on an answer from them, what each one needs, and
  which ones are stuck. Load when the user asks "what's next", "what needs
  me", "what's waiting on me", "where are we", or at the start of a session
  with no assigned task. Do NOT load to choose new work to pick up (see
  prioritise), to close tasks (see backlog-review), or for raw task queries
  (see tracker).
trigger: /whats-next
---

# /whats-next

Work in flight finishes before new work starts. This skill shows the small set of tasks that are in progress or in review, puts the ones that need the user first, and hands over to `prioritise` only when nothing is waiting.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Choosing a new task to pick up | `prioritise` |
| Finding done, stale or duplicate tasks | `backlog-review` |
| Listing or searching tasks | `tracker` |

## Procedure

1. **Gather** via `tracker`, using the states and the user account in the project's workflow file: tasks in progress and in review that are assigned to the user, or whose newest comment is a review request, open question or command for the user. Read only the newest comment and the open questions of each.
2. **Sort** each task into one group:

   | Group | Holds |
   |---|---|
   | Needs you | In review, or in progress with an unanswered question or command for the user |
   | In flight | In progress with nothing waiting on the user |
   | Stuck | In progress with no update for longer than the workflow file's stuck-work threshold |

3. **Report** per the output below. For each "Needs you" item, put the literal command or question first.
4. **Hand over.** When "Needs you" and "In flight" are both empty, say so and run `prioritise`.

## Output

```markdown
## Needs you
- `<ID>` — `<title>`: `<the command to run, or the question>`

## In flight
- `<ID>` — `<title>`: `<next step from the newest handoff>`

## Stuck
- `<ID>` — `<title>`: last update `<date>`
```

Drop a group with no rows. More than ten tasks in progress and in review together is a finding: say so on the first line.

## Hard rules

- Never pick new work here; that is `prioritise`.
- Never change a task's state in this skill.
- Never open tasks outside in progress and in review.
- Never paraphrase a command the user must run; copy it from the task.

## Provenance and maintenance

Updated: 2026-11-26.

Re-verification commands:
```bash
grep -n '^## Stuck work\|User account' plugins/project-management/skills/tracker/templates/workflow.md
grep -n '^## Open questions\|^## Handoff' plugins/project-management/skills/tracker/SKILL.md
```
