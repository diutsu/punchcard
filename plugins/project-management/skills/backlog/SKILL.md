---
name: backlog
tier: leaf
description: >
  Read and file tasks in the project's configured tracker, which also holds
  plans, session handoffs, steps only the human can do and closed work. Load
  before ANY task operation, from any skill, when something needs the
  user, or when work carries into another session. Do NOT load to decide what to do next (see
  prioritise), which tasks can close (see triage-close) or to write a plan
  (see plan).
trigger: /backlog
---

# /backlog

Use the project's configured tracker to read and file tasks. All task state lives there, never in local files. Other skills say "via `backlog`" and never name a tracker.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Choosing what to work on next | `prioritise` |
| Deciding which tasks are finished | `triage-close` |
| Writing or rolling an execution plan | `plan` |
| Recording a significant milestone | `changelog` |

## Resolve the tracker

1. Read the `tasks` key of the project map (see `project-map`). If it is missing, ask the user which tracker holds the tasks, then write the line to the map.
2. If an installed skill covers that tracker, load it and follow it. Otherwise use the tracker's own CLI or connected tools, and read their help before the first command.
3. If nothing can reach the tracker, tell the user what is missing and stop. Never keep a substitute task list.

## Operations

- **Read:** list open tasks, show one in full, search open and closed tasks, find what blocks what.
- **File:** add, edit, annotate, move, block, unblock, close.

When the tracker has no native form of an operation or field, record it in the task's description or a comment.

## States

Map each state to the tracker's matching status or column.

| State | Holds | Enters when |
|---|---|---|
| backlog | Unrefined tasks | Every new task starts here |
| to do | Refined tasks, ready to start | The user has refined the task |
| in progress | Work in flight and its handoff | Implementation of a to-do task starts |
| in review | Started work that needs a human review before it can close | An in-progress task passes the review gate |
| done | Closed work | The task closes |

## Templates

| Writing | Template |
|---|---|
| A new task, or a task being refined | `./templates/task.md` |
| A handoff comment | `./templates/handoff.md` |
| A review request comment | `./templates/review-request.md` |

A plan lives on its task (`plan`). Write the task as it stands now; history stays in the tracker's comments.

## Gates

A task moves only when every check for that move passes. Check each one against the task, the code or command output. When a check fails, leave the task where it is and say which check failed.

| Move | Checks |
|---|---|
| new to backlog | No open or closed task covers it. Title and goal are filled. Unknowns are listed as open questions. |
| backlog to to do | The user refined it. The goal is one verifiable outcome. Every done-when item can be checked against code, command output or the running app. Priority is set. No open question is left. |
| to do to in progress | Nothing blocks it. A plan sized per `plan` exists. The code and docs it names still exist. |
| in progress to in review | The work is implemented and committed. The `verify` commands pass, with output. Each done-when item the agent can check has evidence. The review request says exactly what the human checks or runs. |
| in progress or in review to done | Every done-when item has evidence. Any requested review is answered. Shipped behaviour is in the docs (`docs-management`). No open question is left. Leftovers are filed in backlog (`close-task`). |
| any state to done through `triage-close` | The task is already met, obsolete or a duplicate, with cited evidence, in a batch the user confirmed. |
| in review to in progress | The review asks for changes, and each is recorded on the task. |

A task needs in review only when a human must check or run something before it can close.

## Procedures

- **Add:** pass the first gate and file into backlog.
- **Refine:** settle the open questions, goal, details, done-when and priority with the user, then move the task to to do.
- **Close:** pass the done gate, close, then unblock the tasks that waited on it.

## Handoff

When work will carry into another session, comment on the in-progress task with the handoff template. The newest handoff comment is the current one.

## Open questions

Anything new that needs the user's input or review is an open question, never a task in review.

- It belongs to an existing task: add it under that task's open questions, or as a comment.
- It belongs to no task: file a backlog task with the question under open questions.

State the question, what depends on it, and the options with the recommended one first. Do not change the task's state, except when started work cannot continue without the answer: then it goes to in review with the question in the review request.

## Hard rules

- Never add a task that an open or closed task already covers; extend that one.
- Never close a task without evidence in the close note or the confirmed batch.
- Never move a task without passing the gate for that move.
- Never file a task into any state but backlog.
- Never move a task to in review unless it is in progress.
- Never keep tasks, plans, handoffs, review requests or open questions in local files.
- Never hand the human a step the agent can run, and never keep working a task that waits on the human.
- Never delete a task, or change tasks in bulk, without the user's confirmation. A tracker may be shared.
- Never invent a command; take it from the tracker's skill or its help.

## Provenance and maintenance

Updated: 2026-11-25.

```bash
grep -rniE 'ctask|kaneo|jira' plugins/project-management plugins/coding plugins/techdocs plugins/punchcard/skills
```
