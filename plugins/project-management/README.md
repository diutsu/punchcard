# project-management

The only owner of task management in this marketplace. Once enabled, every other skill asks it for task operations ("via `backlog`").

## Install

```bash
/plugin install project-management --marketplace diutsu/punchcard
```

## What it owns

- The backlog: priorities, blockers, modules, open and closed tasks.
- Plans, one per task, kept on the task.
- Task, handoff and review request templates, and the gates between states.

## Skills

| Skill | Use it to |
|---|---|
| `backlog` | Read and file tasks in the tracker named by the `tasks` key of the project map |
| `prioritise` | Rank open tasks: unblock first, then value, effort and risk, grouped by module |
| `backlog-review` | Find stale and duplicate backlog tasks, titles first |
| `triage-close` | Check done-when criteria against code and git history and close tasks with evidence |
| `plan` | Turn accepted research into a plan of 150 lines or fewer with phase roll-forward |
| `product-direction` | Run a session that brings requirements, PRDs and vision in line with what the user now wants, settles conflicts and blockers, decides when each change is built, then files the agreed tasks |

## Trackers

No tracker is built in. `backlog` follows an installed skill for the tracker when there is one, and otherwise uses the tracker's own CLI or connected tools.
