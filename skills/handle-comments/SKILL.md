---
name: handle-comments
tier: leaf
description: >
  Process `[COMMENT]` markers (and `## Inbox` notes in
  docs/operator-instructions.md) that the user embeds in docs to annotate them.
  Find every marker, read its surrounding context, classify it as a directive,
  a perspective, or a question/doubt, act on it (executing, reconciling, or
  validating against authoritative sources), remove the marker, and route any
  unresolved follow-up into docs/operator-instructions.md (`## Decision gates`)
  so replies are never stranded inside deep docs. Trigger when the user says
  "handle the comments", "process my comments", "address the [COMMENT]
  markers", or points you at annotated docs.
trigger: /handle-comments
---

# /handle-comments

Resolve `[COMMENT]` markers the user has embedded inside `docs/`. Read the surrounding context, classify the intent, act, remove the marker so the doc stays clean, and **route any follow-up question that needs human input into `docs/operator-instructions.md` (`## Decision gates`)** — never leave an agent reply buried inside a requirement or logic doc where the operator won't see it.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Queuing a new human CLI command or decision gate from a coding task | `operator-instructions` |
| Executing a multi-step backlog task from `docs/tasks.md` | `do-task` |
| Auditing docs for YAML frontmatter compliance | `docs-management` |

## 1. What a `[COMMENT]` is

A `[COMMENT]` marker is **user input embedded in a doc** — an instruction, critique, or question aimed at the surrounding text, not part of the document's permanent content:
- **Inline:** on the same line after existing content (`... threshold is 0.7 [COMMENT] should this be configurable?`).
- **Below:** on the line directly under the content it refers to.
- **Inside a block:** within a `>` blockquote or fenced ```` ``` ```` block.

**Comment text** runs from `[COMMENT]` up to the next structural break (the next `[COMMENT]`, a blank line, or the end of the enclosing blockquote/fence). Always read the surrounding section first so you know what the comment refers to.

## 2. Scan

Find every marker across `docs/` and process them one at a time in document order:

```bash
grep -rn "\[COMMENT\]" docs/
```

## 3. Classify and handle

### Type 1 — Directive ("do it")
The comment gives a direct instruction (`"do it now"`, `"shelve this"`, `"rename X"`, `"drop this section"`).
- **Trivial edit** (reword a doc rule, fix a constant, delete a stale paragraph): do it in place immediately.
- **Substantial code/architecture change:** create or update a task in `docs/tasks.md` via `ctask add` / `ctask edit`, or execute it through `do-task` if requested for this session.

### Type 2 — Perspective / viewpoint ("consider this angle")
The comment offers an architectural concern or alternative angle without a direct order (`"feels like this couples two modules"`, `"another way to see this is..."`).
- Weigh the angle honestly on its technical merits — neither blind compliance nor defensive dismissal.
- Reconcile the design in the doc (`docs/requirements/`, `docs/logic/`, `docs/architecture.md`) or file a task via `ctask`.

### Type 3 — Question / doubt ("is this even right?")
The comment signals uncertainty (`"can the API even give us this?"`, `"is this the right module?"`, `"does this actually work?"`).
1. **Validate first against authoritative sources:** check `docs/architecture.md`, `docs/requirements/`, `docs/logic/`, the actual source code, and external docs (`external-research`) before acting.
2. **If validation settles the question unambiguously:** update the doc/code with the verified truth and report the evidence in chat.
3. **If validation reveals a genuine trade-off or needs the user's call:** promote it to a `### [DECISION]` block under `## Decision gates` in `docs/operator-instructions.md` (see §4).

When in doubt between types, treat the comment as a **Question** and validate first.

## 4. Cleanup & routing protocol (never strand replies in deep docs)

1. **Always remove the `[COMMENT]` marker and its raw comment text** from the source doc once processed, cleaning up any leftover empty line or blockquote.
2. **Never leave an "outstanding comment reply" buried inside `docs/requirements/*`, `docs/logic/*`, or `docs/investigations/*`.** The operator only opens `tasks.md`, `next-session-prompt.md`, and `operator-instructions.md` regularly. If a comment cannot be fully resolved without a human decision or manual command:
   - Delete the `[COMMENT]` marker from the deep doc.
   - Write a compact `### [DECISION]` gate (or `## Run queue` item) in `docs/operator-instructions.md` citing the doc and stating the validated options (per the `operator-instructions` skill).
3. Bump `updated:` in the frontmatter of every modified doc:
   ```bash
   sed -i "s/^updated:.*/updated: $(date +%Y-%m-%d)/" docs/<path>.md
   ```

## 5. Report

For each `[COMMENT]` processed, report concisely in chat:
- Location (`file:line`) & classification (`Directive` | `Perspective` | `Question`)
- Action taken (or pointer to the new `[DECISION]` gate in `docs/operator-instructions.md`).

## Hard rules

- Never act on a `Question`/`Doubt` comment without validating the premise against code, docs, or external sources first.
- Never leave a `[COMMENT]` marker or an agent reply stranded inside `docs/requirements/`, `docs/logic/`, or `docs/investigations/` — remove the marker and route any unresolved question to `docs/operator-instructions.md` (`## Decision gates`).
- Always bump `updated:` frontmatter on every edited doc and verify `grep -rn "\[COMMENT\]" docs/` is empty when finished.

## Provenance and maintenance

Updated: 2026-10-11 (v2: routes unresolved follow-ups to `docs/operator-instructions.md` `## Decision gates` instead of leaving inline replies in deep docs).

Re-verification commands:
```bash
grep -rn "\[COMMENT\]" docs/
```
