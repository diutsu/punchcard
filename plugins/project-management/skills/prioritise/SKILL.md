---
name: prioritise
tier: leaf
description: >
  Decide what to do next: rank open tasks by what they unblock, value, effort
  and risk, group tasks that share a module, and flag stale or duplicate
  tasks. Load when the user asks "what next", "what should I work on",
  "re-prioritise", or at the start of a session with no assigned task. Do NOT
  load to decide which tasks can close (see triage-close), to run a task
  (see do-work), or for raw task queries (see backlog).
trigger: /prioritise
---

# /prioritise

Produce a short ranked "next up" list and a set of proposed priority changes. This skill reads the backlog and writes only the priority changes the user confirms.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Checking which tasks are already done | `triage-close` |
| Executing the chosen task | `do-work` |
| Listing or searching tasks with no ranking needed | `backlog` |
| Turning the chosen task into steps | `plan` |

## Inputs

Gather through `backlog`, never from the registry file:

1. `list` of all open tasks with priority and module.
2. `blocking` for every task that is blocked-by something, and `blockers` for any task you plan to rank high.
3. `show` for the top candidates, to read goal, details and done-when.
4. The handoff note and the operator queue (see `operator-queue`), for work already in motion or waiting on the human. Work in motion finishes before a new task is picked.

## Method

1. **Drop what cannot start.** Tasks waiting on an operator step or an external decision are not candidates; list them separately with what they wait on.
2. **Unblock first.** Rank by how many open tasks a task blocks, directly and transitively. A task that frees three others outranks a standalone high-priority task.
3. **Value against effort against risk.** For the rest, judge the outcome's value, the effort from the details, and the risk of leaving it (data loss, wrong numbers, broken workflow). Cheap, valuable and risky-to-leave rank first. Say the judgement in one line; do not invent numeric scores.
4. **Group by module.** When two ranked tasks touch the same module or files (`refs`), place them adjacent so one session shares the context.
5. **Flag hygiene.** Name tasks that look stale (no recent commits on their refs, done-when already met) and send them to `triage-close`. Name duplicates and suggest which survives.

## Output

```markdown
## Next up
1. `<ID>` — `<title>`: `<one-line reason>`
2. ...

## Waiting on someone
- `<ID>` — `<what it waits on>`

## Proposed priority changes
- `<ID>`: `<old>` to `<new>` — `<reason>`

## Hygiene
- `<ID>`: stale | duplicate of `<ID>` — `<evidence>`
```

Keep "Next up" to five items or fewer.

## Applying changes

Ask the user through the question interface before writing any priority change: one question per group of related changes (2-4 per batch), the recommended option first, with "keep as is" as the last option. Apply the confirmed changes with `backlog` `edit`, then `validate`.

## Hard rules

- Never change a priority without confirmation.
- Never rank a task whose blocker is open and outside the user's control above work that can start now.
- Never read the registry file raw; query through `backlog`.
- Never pad the list; fewer than five items is fine.
- Always give a reason per item, in one line.

## Provenance and maintenance

Updated: 2026-11-13.

```bash
ls plugins/project-management/skills/backlog/SKILL.md
grep -n 'blocking\|blockers' plugins/project-management/skills/backlog/SKILL.md
```
