---
name: find-docs
tier: leaf
description: >
  Locate the right project document for a question: resolve the docs,
  investigations, prd and design roots through the project map, search by frontmatter
  and filename before content, and read the smallest matching section. Load
  when a question may be answered by an existing doc, before reading broadly.
  Do NOT load to write or restructure docs, or to mine code and git history.
trigger: /find-docs
---

# /find-docs

Find the one doc that answers the question and read only the part that answers it.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Writing, moving or validating docs | `docs-management` |
| Mining code and git history for how something works | `codebase-search` |
| Looking up an external library or API | `external-research` |
| Resolving a path or tool key | `project-map` |

## Procedure

1. **Resolve roots.** Read the `docs`, `investigations`, `prd` and `design` keys through `project-map`. Search only under those roots.
2. **Pick the folder by question type.** The `docs` root is laid out as Diataxis.

   | Question | Look in |
   |---|---|
   | How do I do X | `how-to/` under `docs` |
   | What exactly does X do, accept or return | `reference/` under `docs` |
   | Why is it built this way | `explanation/` under `docs` |
   | How do I learn this from zero | `tutorials/` under `docs` |
   | What was tried or found out | the `investigations` root |
   | What must it do, for whom | the `prd` root |

3. **Search metadata before content.** List filenames in the chosen folder first. Then grep the frontmatter (`type`, `state`, `cross-file-references`, title) for the topic. Search body text only when both come up empty.
4. **Follow cross-file references** one hop from the best match before widening the search.
5. **Read the smallest section.** Grep for headings, then read from the matching heading to the next one. Read a whole file only when it is short.
6. **Check freshness.** Compare the doc's `updated` value with recent changes to the code it describes. Report a doc that contradicts the code instead of picking a side.
7. **Report** the path, the heading, and the answer. If no doc answers it, say so and name the folder where one belongs.

## Hard rules

- Never search outside the resolved roots for a doc answer.
- Never read a whole large doc when a heading read will do.
- Never present a doc's claim about code as fact without reading the code when the answer matters.
- Never create a doc from this skill. Hand that to `docs-management`.

## Provenance and maintenance

Updated: 2026-11-13.

Re-verification commands:
```bash
grep -n '^- docs::\|^- investigations::\|^- prd::' CLAUDE.md
grep -c 'project-map' plugins/claude/skills/find-docs/SKILL.md
```
