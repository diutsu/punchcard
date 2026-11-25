---
name: handle-comments
tier: leaf
description: >
  Process `[COMMENT]` markers the user embeds in docs: find each, classify it
  as a directive, a perspective or a question, act, remove the marker, and
  route unresolved follow-ups to the tracker. Load when the user says
  "handle the comments", "process my comments" or points at annotated docs.
  Do NOT load for review threads on a planning doc (see review-comment-coach),
  for frontmatter audits (see docs-management), or for queue upkeep (see
  backlog).
trigger: /handle-comments
---

# /handle-comments

Resolve `[COMMENT]` markers the user left inside docs. Read the surrounding context, classify the intent, act, and remove the marker so the doc stays clean. A reply that needs the user becomes a human step via `backlog`, never into a deep doc where nobody will look.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Review threads on a vision, architecture or design | `review-comment-coach` |
| Creating or changing tasks | `backlog` |
| Frontmatter and layout audits | `docs-management` |

## What a marker is

A `[COMMENT]` is user input embedded in a doc: an instruction, critique or question about the surrounding text. It sits inline after content, on the line below it, or inside a blockquote or fence. The comment text runs from the marker to the next marker, blank line, or end of the enclosing block. Read the whole section first so you know what it refers to.

## Scan

Resolve the `docs`, `investigations`, `prd` and `design` keys through `project-map`, then list every marker and process them in document order:

```bash
grep -rn "\[COMMENT\]" <docs-root> <investigations-root> <prd-root>
```

## Classify and act

| Type | Signal | Action |
|---|---|---|
| Directive | "do it", "rename X", "drop this section" | Trivial edit: make it now. Larger change: create or edit the task via `backlog`. |
| Perspective | "feels like this couples two modules" | Weigh it on its technical merits, then reconcile the doc or file a task via `backlog`. |
| Question | "can the API even give us this?", "is this right?" | Validate against the code, the docs and, if needed, `external-research`. If the evidence settles it, update the doc and report the evidence. If it is a real trade-off, queue a decision. |

When unsure between types, treat the comment as a question and validate first.

## Clean up and route

1. Remove the marker and its text from the source doc, with any leftover blank line or empty blockquote.
2. If a comment needs a human decision or command, remove the marker and record a human step via `backlog` that cites the doc and states the validated options. Ask the user through the question interface when a decision has 2-4 clear options.
3. Bump `updated` in the frontmatter of every edited doc (see `docs-management`).

## Report

For each marker: `file:line`, classification, and the action taken or the queue item created.

## Hard rules

- Never act on a question before validating its premise against code, docs or sources.
- Never leave a marker or an unanswered reply inside a doc; route it through `backlog`.
- Never edit task state directly; go through `backlog`.
- Finish only when the scan command returns nothing.

## Provenance and maintenance

Updated: 2026-11-13.

Re-verification commands:
```bash
grep -rn "\[COMMENT\]" docs/
sh plugins/techdocs/skills/writing-style/scripts/lint-prose.sh plugins/techdocs/skills/handle-comments/SKILL.md
```
