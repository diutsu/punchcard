---
name: backlog
tier: leaf
description: >
  Read and file tasks in the project's configured tracker, which also holds
  plans, session handoffs, steps only the human can do and closed work. Load
  before ANY task operation, from any skill, when a task hits a human-only
  step, or when work carries into another session. Do NOT load to decide what to do next (see
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
| in progress | Work in flight and its handoff | Work starts |
| in review | Work waiting on the human: a command, a decision or a review | The agent cannot continue without the human |
| done | Closed work | The task closes |

## Task shape

Every task has a title, a priority, a **goal** (the outcome), **details** (constraints, approach, open questions) and **done-when** (checkable criteria). Write done-when so a reader can verify it against code or git history without asking; `triage-close` depends on that. A plan lives on its task (`plan`).

## Procedures

- **Add:** search first; add only if no open or closed task covers it. State goal and done-when in the same call. The task goes to backlog.
- **Refine:** settle goal, details, done-when and priority with the user, then move the task to to do.
- **Start:** move the task to in progress.
- **Close:** confirm the done-when evidence, make sure the shipped behaviour is recorded where it belongs (`docs-management`), then close and unblock the tasks that waited on it.

## Handoff

When work will carry into another session, comment on the in-progress task with what the next session cannot get elsewhere: branch and test state, what is done, the exact next step, running jobs and open questions. The newest handoff comment is the current one.

## Human steps

A step only the human can run, or a result that needs their decision, moves the task to in review with one comment:

- **Command:** the literal, copy-pasteable command first, then the observable result that means success (exit code, row count, log line or file), then any reason.
- **Decision:** the measured fact with its numbers, then the options, recommended first.

Then stop work on that task and continue with unblocked work. Do not rerun the command hoping for new data or add status essays. A human step that belongs to no task gets its own task, filed straight into in review.

When the human answers, read the result and record durable behaviour in the docs. Then close the task, or move it back to in progress, and file any follow-up.

## Hard rules

- Never add a task that an open or closed task already covers; extend that one.
- Never close a task without evidence in the close note or the confirmed batch.
- Never move a task from backlog to to do before the user has refined it.
- Never keep tasks, plans, handoffs or human steps in local files.
- Never hand the human a step the agent can run, and never keep working a task that waits on the human.
- Never delete a task, or change tasks in bulk, without the user's confirmation. A tracker may be shared.
- Never invent a command; take it from the tracker's skill or its help.

## Provenance and maintenance

Updated: 2026-11-25.

```bash
grep -rniE 'ctask|kaneo|jira' plugins/project-management plugins/coding plugins/techdocs plugins/punchcard/skills
```
