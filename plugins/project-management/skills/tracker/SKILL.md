---
name: tracker
tier: leaf
description: >
  Read and file tasks in the project's tracker, which also holds handoffs,
  human-only steps and closed work. Load before ANY task operation, from any
  skill, or when work carries into another session. Do NOT load to choose work
  (whats-next, prioritise) or judge closes (backlog-review).
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

1. Read the `tasks` and `tasks-workflow` keys of the project map (see `project-map`); when the map has no `tasks-workflow`, use the one the user's global instructions name. If `tasks` is missing, ask the user which tracker holds the tasks, then write the line to the map. If `tasks-workflow` is missing, run **Set up the workflow** first.
2. If an installed skill covers that tracker, load it and follow it. Otherwise use the tracker's own CLI or connected tools, and read their help before the first command.
3. If nothing can reach the tracker, tell the user what is missing and stop. Never keep a substitute task list.

## Set up the workflow

Run once per project, or once per user when every project shares the same tracker and workflow.

1. Read from the tracker what it offers: statuses, labels, priority values, close or resolution fields, and the user's own account.
2. Fill `./templates/workflow.md` with a proposed mapping for each section. Ask the user to confirm or correct it in one batch through the question interface.
3. Ask where it lives: in the project (when only this project uses the workflow) or in one user-level file shared by all projects. A user-level file stays outside the repo and keeps the account name out of committed files.
4. Write the file. For a project file, set the `tasks-workflow` map key to its path. For a user-level file, add one line to the user's global instructions naming its path, and leave the committed project map without the key.

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
| in review | Completed work waiting on a human check, or on a merge into the integration branch | An in-progress task passes the review gate |
| done | Closed work, with its close reason | The task closes |

A milestone is a measurable project state: a task or group of tasks in done plus a release, or another state the project can check. The workflow file says how one is marked.

## Templates

| Writing | Template |
|---|---|
| A new task, or a task being refined | `./templates/task.md` |
| A handoff comment | `./templates/handoff.md` |
| A review request comment | `./templates/review-request.md` |
| The project's workflow file | `./templates/workflow.md` |

Plans are not kept on tasks; `plan` covers one session. Write the task as it stands now; history stays in the tracker's comments.

## Gates

A task moves only when every check for that move passes. Check each one against the task, the code or command output. When a check fails, leave the task where it is and say which check failed.

| Move | Checks |
|---|---|
| new to backlog | No open task covers it. A regression of a closed task links that task. Title and goal are filled. Unknowns are listed as open questions. |
| backlog to to do | The user refined it, or said in this session that it is ready as written. The goal is one verifiable outcome. Every done-when item can be checked against code, command output or the running app. Priority is set. No open question is left. |
| to do to in progress | Nothing blocks it. The code and docs it names still exist. |
| in progress to in review | All the work is implemented and committed; partial work stays in progress. The `verify` commands pass, with output, on the tree that holds the work. Each done-when item the agent can check has evidence. The review request says exactly what the human checks or runs, and, for work not yet landed, names the branch and the commit range to merge. |
| in progress or in review to done | The work has landed (see **Landing**). Every done-when item passed the done-when check (`validation-and-qa`). Any requested review is answered. Shipped behaviour is in the docs (`docs-management`). No open question is left. |
| any state to done through `backlog-review` | The task is done, stale or a duplicate, with cited evidence, in a batch the user confirmed. Done evidence comes from the integration branch. |
| in review to in progress | The review asks for changes, and each is recorded on the task. |

A task needs in review only when its work is complete and something must still happen before it can close: a human check or run, or a merge into the integration branch.

## Landing

The integration branch is the project's default branch, `main` or `master`. A task that changed code has landed when both hold:

1. Every commit of the task is on the integration branch.
2. The `verify` commands passed, with output, on a tree that contains those commits. When that tree differs from the one reviewed or verified (the integration branch moved, or conflicts were resolved), `verify` runs again on it.

A task that changed no code, docs-only work included, needs no landing check.

Work on any other branch moves a task at most to in review. The agent that validates the work closes the task after the merge. Merging and pushing follow `repo-infra`; when they are not allowed, the task stays in review and its review request names the merge.

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

## Comment or task

Something found while working a task is a comment on that task, or a backlog task:

| It is | Record it as |
|---|---|
| Blocking current progress, or due soon | A comment on the task in hand |
| Able to wait, or a bigger change | A backlog task |
| A bigger change, mitigated for now | A backlog task for the full fix, plus a comment on the task in hand: `mitigation <what> applied; full fix in <ID>` |

Never file a task to avoid the work in hand, or ahead of a need.

## Open questions

Anything new that needs the user's input or review is an open question, never a task in review.

- It belongs to an existing task: add it under that task's open questions, or as a comment.
- It belongs to no task: file a backlog task with the question under open questions.

State the question, what depends on it, and the options with the recommended one first. An open question never changes the task's state.

When partly done work needs the user to continue, comment on the task and leave it in progress. The comment holds the question, or the literal command first and what success looks like, plus the handoff when the work carries into another session. Stop work on that task and continue with unblocked work. When the user answers, resume from the comment.

## Hard rules

- Never hand the human a step the agent can run, and never keep working a task that waits on the human.
- Never delete a task, or change tasks in bulk, without the user's confirmation. A tracker may be shared.

## Provenance and maintenance

Updated: 2026-11-28.

Re-verification commands:
```bash
grep -n 'tasks-workflow' plugins/punchcard/skills/project-map/SKILL.md plugins/punchcard/skills/project-doctor/SKILL.md
grep -rn '`backlog`' plugins AGENTS.md README.md
grep -rniE 'ctask|kaneo|jira' plugins/project-management plugins/coding plugins/techdocs plugins/punchcard/skills
```
