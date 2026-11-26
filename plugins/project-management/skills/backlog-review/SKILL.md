---
name: backlog-review
tier: leaf
description: >
  Find open tasks that are done, stale or duplicate and close them with cited
  evidence. Load to review, groom, prune or clean up the backlog, for "what can
  we close", or after a large change. Do NOT load to rank work (prioritise),
  close the task just finished (do-work) or add tasks (tracker).
trigger: /backlog-review
---

# /backlog-review

Close open tasks only with evidence, spending as little reading as possible. Titles raise suspicion; only evidence gives a verdict. The skill proposes one batch and writes after one confirmation.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Ranking what to do next | `prioritise` |
| Closing the one task a work session just finished | `do-work` |
| Adding or refining a task | `tracker` |
| Recording a milestone for a closed task | `changelog` |

## Scope

All open tasks, in every state. Narrow it when the user names tasks, a label or a state, or when the caller passes a candidate list (`prioritise` does). When the user names the exact tasks, skip pass 1 and start at pass 2 with those tasks.

## Method

Run the passes in order. Each pass reads only what the one before flagged.

1. **Titles.** List, via `tracker`, the ids and titles of the tasks in scope, plus the titles of every other task, closed ones included. Read recent commit subjects and changelog lines. Open no task. Flag:
   - **duplicate suspect:** two titles aim at the same outcome, including one that matches a task in another state
   - **done or stale suspect:** a commit, changelog line or closed task suggests the outcome already exists, or the title names something the repo no longer has
   - **refs suspect:** the files a task names changed in recent commits
2. **Task bodies.** Show only the suspects. Compare goal and done-when. Drop a duplicate suspect whose goal differs.
3. **Evidence.** For each survivor, test every done-when item:
   - Search the code for the behaviour, test or file named; read the lines.
   - Run `git log` on the task's refs and on its id; read the commits.
   - Run the cheapest command that proves an item when one exists (a test, a grep, a query).
4. **Classify and cite.**

   | Class | Meaning | Action |
   |---|---|---|
   | done | Every done-when item is met | close as done |
   | stale | The goal no longer applies | close as stale |
   | duplicate | Another task covers it | close as duplicate; when this task holds something the survivor lacks, move it there and close as merged |
   | partial | Some items are met | edit details to record what is left |
   | open | Nothing met, or unclear | leave alone |

   Each done, stale or duplicate verdict cites a `file:line`, a commit hash or the surviving task. A verdict without a citation becomes open.
5. **Confirm.** Show the table. Ask once through the question interface: apply all (recommended), apply done only, or none. Never close one task at a time. A caller may fold this question into its own batch.
6. **Write.** Apply the confirmed items via `tracker`, using its closing comments and the close reasons of the project's workflow. Unblock the tasks that waited on a closed one.

## Output

```markdown
| Task | Class | Evidence | Action |
|---|---|---|---|
| `<ID>` | done, stale, duplicate of `<ID>` or partial | `<file:line, commit or task>` | `<close, merge or edit>` |
```

Then the suspects that stayed unproven, with what is missing, and the counts: tasks listed, suspects, opened, per class.

## Hard rules

- Never infer done from a finished plan.
- Never close or merge without the batch confirmation, unless the user named the exact tasks to close.
- Never edit a task's goal to match the code; record partial progress in details.
- Never report the backlog as clean beyond what the title pass can catch; say that unflagged tasks were not opened.

## Provenance and maintenance

Updated: 2026-11-27.

Re-verification commands:
```bash
grep -n '^## Gates\|^## Closing comments' plugins/project-management/skills/tracker/SKILL.md
grep -n 'Close reasons' plugins/project-management/skills/tracker/templates/workflow.md
grep -n 'backlog-review' plugins/project-management/skills/prioritise/SKILL.md
```
