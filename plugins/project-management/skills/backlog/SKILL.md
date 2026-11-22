---
name: backlog
tier: leaf
description: >
  The tool-neutral interface to the project's task registry: list, show,
  search, blockers, add, edit, block, close, validate, annotate, and locate
  the plans and the done log. Load before ANY
  task operation, from any skill. Do NOT load to decide what to do next
  (see prioritise), which tasks can close (see triage-close) or to write a
  plan (see plan).
trigger: /backlog
---

# /backlog

Every task operation in the marketplace goes through this skill. It names the neutral operation; an adapter file maps it to the tool. Other skills say "via `backlog`" and never name a tool or a path.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Choosing what to work on next | `prioritise` |
| Deciding which tasks are finished | `triage-close` |
| Judging leftovers before closing the task just finished | `close-task` |
| Filing a newly reported defect | `bug-report` |
| Writing or rolling an execution plan | `plan` |
| Recording a significant milestone | `changelog` |
| Carrying a long task across sessions | the handoff note (`operator-queue`) |
| Queuing a command only the human can run | `operator-queue` |

## Resolve the tool

1. Read the `tasks` key of the project map (see `project-map`).
2. If the key is missing, ask the user through the question interface which tool holds the tasks (options: the adapters in `./references/adapters/`, recommended first), then write the `tasks` line to the map.
3. Load `./references/adapters/<tool>.md`. If no adapter exists for the named tool, stop and tell the user; do not improvise commands.
4. If the tool is not installed, give the adapter's install hint and stop.

## Neutral operations

| Operation | Purpose |
|---|---|
| `list` | Open tasks, filtered by priority, module, or blocked state. |
| `show` | One or more tasks in full, open or closed. |
| `search` | Find tasks by text, optionally including closed ones. |
| `blockers` / `blocking` | What blocks a task; what a task blocks. |
| `refs` | Tasks that reference a file or another task. |
| `add` | New task with title, priority, module, goal, details, done-when. |
| `edit` | Change any field, move a task, append to goal, details or done-when. |
| `block` / `unblock` | Set or clear what a task waits on. |
| `close` | Move a task to the done log. |
| `validate` | Structural check of the registry. |
| `annotate` | Record a prediction, note, commit hash or finding on a task. |
| `locations` | Paths of the plans and the done log. |

The adapter states the exact command for each. If an operation has no mapping, extend the tool in its own repo; do not hand-edit the registry.

## Task shape

Every task has: a stable id, a title, a priority, a module, optional blocked-by and refs, a **goal** (the outcome), **details** (constraints, approach, open questions) and **done-when** (checkable criteria). Write done-when so a reader can verify it against code or git history without asking; `triage-close` depends on that.

## Procedures

- **Add:** search for an existing task first; add only if none covers it. State goal and done-when in the same call.
- **Close:** confirm the done-when evidence, make sure the shipped behaviour is recorded where it belongs (`docs-management`), delete the task's plan (`plan`), then close, clear any stale blocked-by the tool reports, and validate.
- **Block on a human step:** queue the step with `operator-queue`, then `block` the task on that entry and stop work on it.
- **Batch changes:** run `validate` once after the batch.

## Hard rules

- Never read the registry file raw when a query answers the question.
- Never hand-edit a task, the done log, or any file the tool owns.
- Never commit a file the tool owns. Tasks, the done log and plans are local work.
- Never name the tool or a registry path outside the adapter file.
- Never close a task without evidence in the close note or the confirmed batch.
- Always validate after a batch of changes.
- Never add a task that an open or closed task already covers; extend that one. A failure that returns after a closed task's fix is the exception: add a regression task that links the closed one.

## Provenance and maintenance

Updated: 2026-11-22. Adapter details: `./references/adapters/`.

```bash
ls plugins/project-management/skills/backlog/references/adapters/
grep -rn 'ctask' plugins --include=SKILL.md | grep -v project-management
```
