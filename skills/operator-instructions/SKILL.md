---
name: operator-instructions
tier: leaf
description: >
  Manage docs/operator-instructions.md as a strict two-part worklist: (1) a
  Run queue of exact runnable CLI commands only a human can execute, and (2)
  Decision gates where a completed measurement or null result requires a human
  judgment call before closing or branching a task. Enforces the Binary Exit
  Rule so agents stop cleanly when blocked by an operator step instead of
  writing status reports or hunting for nitpicks. Load when adding, checking,
  or folding items in docs/operator-instructions.md, or when a task hits a
  human-only execution or decision blocker. Do NOT load for permanent CLI/daemon
  how-to guides (put those in docs/usage.md) or for agent-executable diagnostics
  (see operate-and-diagnose).
trigger: /operator-instructions
---

# /operator-instructions

`docs/operator-instructions.md` is an **active human action queue**, never a status report, live system dashboard, or permanent manual. Every entry is either a **command the human owes the system** (`## Run queue`) or a **fork the human must choose** (`## Decision gates`). The moment the human runs the command or checks an option, fold the result into permanent docs (`docs/requirements/`, `docs/logic/`, `docs/usage.md`) or `ctask`, and **delete the entry**.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| The agent itself can run the command or query | Run it directly (`operate-and-diagnose`) |
| Documenting reusable operational procedures ("how to start/stop jobs", "how to use the queue") | `docs/usage.md` (`write-docs`) |
| Recording live queue snapshots or what is currently running between sessions | `docs/next-session-prompt.md` ($\le 40$ lines) |
| A single one-off question during an interactive chat turn | Ask directly in chat |

## 1. The two allowed sections (nothing else belongs in this file)

`docs/operator-instructions.md` has exactly two H2 sections: `## Run queue` and `## Decision gates`.

### Section A — `## Run queue` (Commands only the human can run)
Use when a task requires running a command on a restricted host, with private credentials, or via a manual download/UI step the agent cannot reach.

- **Literal command first, context second:** Write the exact copy-pasteable command. Never write prose describing the outcome you want.
- **Stated `Expect:` signal:** Every step states the exact exit code, row count, or log line that proves success.
- **Empty `Output:` block:** Provide an empty code fence for the operator to paste terminal output into.

```markdown
### `<TASK-ID>` — `<1-line outcome>`

- [ ] `<literal command to run>`
      Expect: `<observable pass criteria: exit 0, row count, log line>`

Output:
```
```
```

### Section B — `## Decision gates` (Null results & scope forks)
Use when all agent-executable code and verification runs are finished, but **closing the task requires a human judgment call** — for example, a fix is verified live in code, yet a real-world corpus run yields a null result (`+0 rows`), or a benchmark reveals a trade-off against the original `Done when` threshold.

Instead of writing a multi-paragraph diagnostic essay or hunting for new nitpicks to avoid closing the task, write a **6-line maximum Decision Gate**:

```markdown
### `[DECISION]` `<TASK-ID>` — `<1-line summary of the fork>`
- **Measured fact:** `<1-2 sentences with exact before/after numbers vs. the task gate>`
- **Options (check `[x]` or add `[COMMENT]`):**
  - [ ] **(a)** Close `<TASK-ID>` as done (`<what gets recorded in docs/requirements/ or docs/logic/>`).
  - [ ] **(b)** Keep open / rescope (`<concrete alternative action or follow-up task>`).
```

## 2. The Binary Exit Rule (stopping the "Report & Nitpick Loop")

When a task hits either a `Run queue` step or a `Decision gate`:
1. Write the compact entry in `docs/operator-instructions.md` (under `## Run queue` or `## Decision gates`).
2. Mark the task blocked in `ctask`:
   `ctask edit <TASK-ID> --blocked-by "operator-instructions#<TASK-ID>"`
3. Add a 1-line pointer in `docs/next-session-prompt.md` under `Blocked on operator-instructions.md`.
4. **Stop working on `<TASK-ID>` immediately.** Yielding cleanly at an operator or decision gate is a **successful completion of your turn**. Never re-audit the module for unrelated nitpicks, never re-run the same command hoping for different data, and never append a narrative report explaining why the task is still open.

## 3. Cleanup protocol (folding completed items)

When the operator pastes output into `Output:` or checks an option under `## Decision gates`:
1. Ingest the result:
   - If the gate passed or Option (a) was chosen: update `docs/requirements/<module>.md` or `docs/logic/<module>-<concern>.md` in place (timeless present tense, no dates), clear `blocked-by`, and run `ctask close <TASK-ID>`.
   - If the output reveals a new bug or Option (b) was chosen: update the task or file the follow-up via `ctask`.
2. **Delete the entire `### <TASK-ID>` section** from `docs/operator-instructions.md`.
3. Bump `updated:` in `docs/operator-instructions.md` frontmatter.

## 4. Self-check before finishing any edit to `operator-instructions.md`

Run these checks before ending your turn:
- **Zero permanent runbooks:** Did you add a section like `Preferred pattern`, `How to stop and resume`, or `General notes`? Move it to `docs/usage.md` and delete it here.
- **Zero narrative essays:** Does any section contain more than 3 lines of prose above its checkboxes, or a `BEFORE-state` / `AFTER-state` essay? Compress it into a 6-line `[DECISION]` gate or move the spike data to `docs/investigations/<slug>.md`.
- **Zero completed sections:** Are all checkboxes under a `### <TASK-ID>` heading checked `[x]`? Fold and delete that section now.
- **Zero multi-date accretion:** Grep for more than one date (`2026-...`) under a single heading — if found, replace the old check with the current state or convert to a `[DECISION]` gate.

## Hard rules

- Never write status reports, live queue snapshots, or multi-paragraph diagnostic essays in `docs/operator-instructions.md`.
- Never store reusable runbooks or permanent operational instructions in `docs/operator-instructions.md` — those belong in `docs/usage.md`.
- Never write a `Run queue` step as a prose description — write the literal command first, followed by `Expect:`.
- Never keep a completed section in `docs/operator-instructions.md` — fold its outcome into permanent docs / `ctask` and delete it immediately.
- Never keep spinning or inventing nitpicks when a task is blocked on a human run or a null-result judgment call — write the `Run queue` or `[DECISION]` block, mark `blocked-by` in `ctask`, and stop working on that task.

## Provenance and maintenance

Authored/updated: 2026-10-11 (v2 with `Run queue` + `Decision gates` split and Binary Exit Rule).

Re-verification commands:
```bash
# Confirm no more than 2 H2 sections exist in template
grep -n '^## ' doc-templates/docs/operator-instructions.md
```
