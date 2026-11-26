# project-management

The only owner of task management in this marketplace. Once enabled, every other skill asks it for task operations ("via `tracker`").

## Install

```bash
/plugin install project-management --marketplace diutsu/punchcard
```

## What it owns

- Tasks: priorities, blockers, labels, open and closed.
- Task, handoff, review request and workflow templates, and the gates between states.
- The project's task workflow: state names, close reasons, priority scale, labels and milestones, set up once and kept at the `tasks-workflow` map key.

## Skills

| Skill | Use it to |
|---|---|
| `tracker` | Read and file tasks in the tracker named by the `tasks` key of the project map; set up the project's task workflow once |
| `whats-next` | Show the in-progress and in-review tasks: the ones that need the user first, then the rest, then the stuck ones |
| `prioritise` | Pick what to start next: validate through `backlog-review`, rank by unblock, value, effort and risk, and list quick wins |
| `backlog-review` | Find done, stale and duplicate open tasks, titles first, and close them with evidence |
| `product-direction` | Run a session that brings requirements, PRDs and vision in line with what the user now wants, settles conflicts and blockers, decides when each change is built, then files the agreed tasks |
| `bug-report` | File a defect as a task, with its expected behaviour settled and the docs that must change |

## Trackers

No tracker is built in. `tracker` follows an installed skill for the tracker when there is one, and otherwise uses the tracker's own CLI or connected tools.
