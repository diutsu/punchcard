---
name: whats-next
tier: leaf
description: >
  Summarise work in flight: in-progress and in-review tasks, what each needs,
  which are stuck; else pick from to do. Load for "what's next", "what needs
  me", "where are we", or a session start with no task. Do NOT load to choose
  new work (prioritise) or close tasks (backlog-review).
trigger: /whats-next
---

# /whats-next

Work in flight finishes before new work starts. This skill shows the small set of tasks that are in progress or in review, puts the ones that need the user first, and picks from to do through `prioritise` only when nothing is left.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Choosing a new task to pick up | `prioritise` |
| Finding done, stale or duplicate tasks | `backlog-review` |
| Listing or searching tasks | `tracker` |

## Procedure

1. **Gather** via `tracker`, using the states and the user account in the project's workflow file: tasks in progress and in review that are assigned to the user or to no one, plus any whose newest comment is a review request, open question or command for the user. Read only the newest comment and the open questions of each.
2. **Sort** each task into one group:

   | Group | Holds |
   |---|---|
   | Needs you | In review, or in progress with an unanswered question or command for the user |
   | In flight | In progress with nothing waiting on the user |
   | Stuck | In progress with no update for longer than the workflow file's stuck-work threshold |

3. **Report** per the output below. For each "Needs you" item, put the literal command or question first.
4. **Pick from to do.** When "Needs you", "In flight" and "Stuck" are all empty, say so and run `prioritise` to pick from to do.

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

- Never change a task's state in this skill.

## Provenance and maintenance

Updated: 2026-11-27.

Re-verification commands:
```bash
grep -n '^## Stuck work\|User account' plugins/project-management/skills/tracker/templates/workflow.md
grep -n '^## Open questions\|^## Handoff' plugins/project-management/skills/tracker/SKILL.md
```
