---
name: operator-queue
tier: leaf
description: >
  Manage the operator queue as a strict two-part worklist: a Run queue of exact
  commands only the human can run, and Decision gates where a finished
  measurement or null result needs a human call. Enforces the Binary Exit Rule
  so an agent stops cleanly at a human-only step. Load when adding, checking or
  folding queue items, when a task hits a human-only run or decision, or from
  `away-mode` to park outward-facing actions. Also owns the handoff note that
  carries one long task across sessions. Do NOT load for permanent runbooks or
  for steps the agent can run itself.
trigger: /operator-queue
---

# /operator-queue

The queue file is a **worklist**, not documentation. Each entry is either a command the human owes the system or a fork the human must decide. When the human finishes it, fold the result into permanent docs and delete the entry.

The file lives at the `operator-queue` key of the project map (see `project-map`). It is local work: never commit it.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| The agent can run the command or query itself | Run it (`operate-and-diagnose`) |
| A permanent how-to, such as "how to start the jobs" | A how-to doc (`docs-management`) |
| Pending work that nobody has started | A task, via `backlog`; `prioritise` picks it up |
| One question during a live chat | Ask through the question interface |

## File shape

Exactly two H2 sections: `## Run queue` and `## Decision gates`. Create the file from `${CLAUDE_SKILL_DIR}/templates/operator-queue.md`. It is a worklist, not a doc: no frontmatter, and no links to other files beyond the task each entry names.

### Run queue

Use when a step needs a restricted host, private credentials, or a manual download or UI action the agent cannot reach.

- **Command first, context second.** The operator is at a terminal. Put the literal, copy-pasteable command first and trail any reason as a short bullet after it.
- **Say what success looks like.** Every step states an observable signal: exit code, row count, a log line, or a file that now exists. A step without one is unverifiable.
- **Group by task, checklist per outcome.** One heading per outcome, a one-line description, then the steps in run order.
- **Leave an empty `Output:` block** for output you need back.

````markdown
### `<TASK-ID>` - `<one-line outcome>`

Rebuild the index after the schema change.

- [ ] `myapp search reindex --table foo`
      Expect: exit 0, prints "reindexed N rows" with N > 0.
- [ ] `myapp search verify --table foo`
      Expect: prints "OK", no missing-row warnings.

Output:
```
```
````

### Decision gates

Use when every agent-run check is finished but closing the task needs a human judgment, such as a verified fix with a null real-world result or a trade-off against the stated threshold. Write six lines at most:

```markdown
### [DECISION] `<TASK-ID>` - `<one-line fork>`
- **Measured fact:** `<one or two sentences with exact numbers against the task gate>`
- **Options (check one or add a [COMMENT]):**
  - [ ] **(a)** Close `<TASK-ID>`; record `<what>` in the docs.
  - [ ] **(b)** Keep open or rescope: `<concrete follow-up>`.
```

## The Binary Exit Rule

When a task reaches a Run queue step or a Decision gate:

1. Write the compact entry in the queue file.
2. Mark the task blocked through `backlog`, pointing at the entry.
3. Stop working on that task. Yielding at a human gate completes your turn. Do not re-audit for nitpicks, rerun the command hoping for new data, or append a status essay. Continue with other unblocked work.

## Fold completed entries

When the human pastes output or checks an option:

1. Ingest the result. A passed gate or option (a): update the permanent docs in place (per `docs-management`) and close the task via `backlog`. A new finding or option (b): file or edit the follow-up via `backlog`.
2. Delete the whole entry.

## Handoff note

The handoff note carries one task across sessions or between independent agents. It lives at the `handoff` key of the project map. It is local work: never commit it, and keep its folder ignored by git.

- **Write it only for work in flight** that is expected to outlast this session or needs several sessions or independent agents. Start from `${CLAUDE_SKILL_DIR}/templates/handoff.md`.
- **No work in flight, no file.** Delete the note when the task lands or stops. A missing note means the next session starts from `prioritise`.
- **Never list pending tasks in it.** A task nobody has started is backlog, however likely it is to be next.
- Keep it to what the next session cannot get elsewhere: the task, the branch and test state, what is done, the next step, running jobs, and open questions. At most 40 lines. Rewrite it; do not append.

## Self-check before ending an edit

- No runbook sections ("preferred pattern", "general notes"). Move them to a how-to doc.
- No section with more than three lines of prose above its checkboxes.
- No section whose boxes are all checked. Fold and delete it.
- No status, summary or overview heading that restates other entries.
- No entry that holds more than one date.
- If you cleared a blocker, update every other entry that cites it in the same pass.

## Hard rules

- Never write a step as a description of an outcome. Write the literal command.
- Never put the explanation before the command.
- Never leave a step without an expected result.
- Never keep a completed entry.
- Never hand the human a step the agent could run.
- Never keep working a blocked task.
- Never commit the queue file or the handoff note, and never keep a handoff note when no task is in flight.

## Provenance and maintenance

Updated: 2026-11-14.

Re-verification commands:
```bash
grep -n '^## ' "$(sed -n 's/^- operator-queue:: //p' CLAUDE.md)"
```
