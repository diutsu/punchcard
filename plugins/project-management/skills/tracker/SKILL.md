---
name: tracker
tier: leaf
description: >
  Read and file tasks in the project's configured tracker, which also holds
  plans, session handoffs, steps only the human can do and closed work, and
  set up the project's task workflow once. Load before ANY task operation,
  from any skill, when something needs the user, or when work carries into
  another session. Do NOT load to decide what to do next (see whats-next and
  prioritise), which tasks can close (see backlog-review) or to write a plan
  (see plan).
trigger: /tracker
---

# /tracker

Use the project's configured tracker to read and file tasks. All task state lives there, never in local files. Other skills say "via `tracker`" and never name a tracker. "Backlog" in this plugin is a state, not this skill.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| What needs the user, or what is in flight | `whats-next` |
| Choosing what to pick up next | `prioritise` |
| Deciding which tasks are finished, stale or duplicate | `backlog-review` |
| Writing or rolling an execution plan | `plan` |
| Recording a significant milestone | `changelog` |

## Resolve the tracker

1. Read the `tasks` and `tasks-workflow` keys of the project map (see `project-map`). If `tasks` is missing, ask the user which tracker holds the tasks, then write the line to the map. If `tasks-workflow` is missing, run **Set up the workflow** first.
2. If an installed skill covers that tracker, load it and follow it. Otherwise use the tracker's own CLI or connected tools, and read their help before the first command.
3. If nothing can reach the tracker, tell the user what is missing and stop. Never keep a substitute task list.

## Set up the workflow

Run once per project, or once per user when every project shares the same tracker and workflow.

1. Read from the tracker what it offers: statuses, labels, priority values, close or resolution fields, and the user's own account.
2. Fill `./templates/workflow.md` with a proposed mapping for each section. Ask the user to confirm or correct it in one batch through the question interface.
3. Ask where it lives: in the project (recommended when only this project uses the workflow) or in one user-level file shared by all projects. A user-level file stays outside the repo. A public repo keeps the account name out of committed files.
4. Write the file and set the `tasks-workflow` map key to its path.

Read the workflow file before the first task operation of a session. Use its state names, close reasons, priority scale and labels, never guessed ones.

## Operations

- **Read:** list open tasks, show one in full, search open and closed tasks, find what blocks what.
- **File:** add, edit, annotate, move, block, unblock, close.

When the tracker has no native form of an operation or field, record it in the task's description or a comment.

## States

Map each state to the tracker status named in the workflow file.

| State | Holds | Enters when |
|---|---|---|
| backlog | Unrefined tasks | Every new task starts here |
| to do | Refined tasks, ready to start | The user refined the task, or explicitly said it is ready |
| in progress | Work in flight and its handoff | Implementation of a to-do task starts |
| in review | Completed work that needs a human check before it can close | An in-progress task passes the review gate |
| done | Closed work, with its close reason | The task closes |

A milestone is a measurable project state: a task or group of tasks in done plus a release, or another state the project can check. The workflow file says how one is marked.

## Templates

| Writing | Template |
|---|---|
| A new task, or a task being refined | `./templates/task.md` |
| A handoff comment | `./templates/handoff.md` |
| A review request comment | `./templates/review-request.md` |
| The project's workflow file | `./templates/workflow.md` |

A plan lives on its task (`plan`). Write the task as it stands now; history stays in the tracker's comments.

## Gates

A task moves only when every check for that move passes. Check each one against the task, the code or command output. When a check fails, leave the task where it is and say which check failed.

| Move | Checks |
|---|---|
| new to backlog | No open or closed task covers it. Title and goal are filled. Unknowns are listed as open questions. |
| backlog to to do | The user refined it, or said in this session that it is ready as written. The goal is one verifiable outcome. Every done-when item can be checked against code, command output or the running app. Priority is set. No open question is left. |
| to do to in progress | Nothing blocks it. A plan sized per `plan` exists. The code and docs it names still exist. |
| in progress to in review | All the work is implemented and committed; partial work stays in progress. The `verify` commands pass, with output. Each done-when item the agent can check has evidence. The review request says exactly what the human checks or runs. |
| in progress or in review to done | Every done-when item has evidence. Any requested review is answered. Shipped behaviour is in the docs (`docs-management`). No open question is left. Leftovers are filed in backlog (`close-task`). |
| any state to done through `backlog-review` | The task is done, stale or a duplicate, with cited evidence, in a batch the user confirmed. |
| in review to in progress | The review asks for changes, and each is recorded on the task. |

A task needs in review only when its work is complete and a human must check or run something before it can close.

## Procedures

- **Add:** pass the first gate and file into backlog. The agent's own decision to file a follow-up never moves it further.
- **Refine:** settle the open questions, goal, details, done-when and priority with the user, then move the task to to do.
- **Close:** pass the done gate, record the close reason the workflow file defines, leave the closing comment, then unblock the tasks that waited on it.

## Closing comments

One short line. Add a second line only when it carries something useful: the evidence, what was added to meet the goal, or the tasks filed from leftovers.

| Reason | Line |
|---|---|
| done | `done, closing` (the default; may be omitted) |
| stale | `stale task, closing` |
| duplicate | `duplicated task, closing` |
| merged | `merged with <ID>, closing` |

## Handoff

When work will carry into another session, comment on the in-progress task with the handoff template. The newest handoff comment is the current one.

## Open questions

Anything new that needs the user's input or review is an open question, never a task in review.

- It belongs to an existing task: add it under that task's open questions, or as a comment.
- It belongs to no task: file a backlog task with the question under open questions.

State the question, what depends on it, and the options with the recommended one first. An open question never changes the task's state.

When partly done work needs the user to continue, comment on the task and leave it in progress. The comment holds the question, or the literal command first and what success looks like, plus the handoff when the work carries into another session. Stop work on that task and continue with unblocked work. When the user answers, resume from the comment.

## Hard rules

- Never add a task that an open or closed task already covers; extend that one.
- Never close a task without evidence in the closing comment or the confirmed batch.
- Never move a task without passing the gate for that move.
- Never file a task into any state but backlog. Move it on only on the user's explicit word in this session.
- Never move a task to in review unless it is in progress and its work is complete.
- Never keep tasks, plans, handoffs, review requests or open questions in local files.
- Never hand the human a step the agent can run, and never keep working a task that waits on the human.
- Never delete a task, or change tasks in bulk, without the user's confirmation. A tracker may be shared.
- Never invent a command, state, label or priority value; take it from the tracker's skill, its help or the workflow file.

## Provenance and maintenance

Updated: 2026-11-26.

Re-verification commands:
```bash
grep -n 'tasks-workflow' plugins/punchcard/skills/project-map/SKILL.md plugins/punchcard/skills/project-doctor/SKILL.md
grep -rn '`backlog`' plugins AGENTS.md README.md
grep -rniE 'ctask|kaneo|jira' plugins/project-management plugins/coding plugins/techdocs plugins/punchcard/skills
```
