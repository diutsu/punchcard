---
name: editorial-review
tier: workflow
description: >
  The final pass for any doc, report or essay: lint, critique, then edit with
  editor notes and a reference check. Load when the author shares a draft or
  rant and asks for a review, critique, fact check or edit, and before
  delivering any doc. Do NOT load to draft from scratch (see writing-style and
  doc-templates), to judge a planning doc's horizon (see horizon-review), or to
  place and tag a doc (see docs-management).
trigger: /editorial-review
---

# /editorial-review

The author writes first and fast; this skill is the editor. It runs a lint step, then two passes. The author decides when to move from the first pass to the second.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Drafting prose or choosing a style rule | `writing-style` |
| Starting a doc from a skeleton | `doc-templates` |
| Checking statements against the planning-horizon model | `horizon-review` |
| Triaging review comments on a doc | `review-comment-coach` |
| Researching external sources for a new doc | `external-research` |

## Step 0: lint

Run `sh ../writing-style/scripts/lint-prose.sh <file>` (relative to this skill folder) and fix every hit that is not a quotation or proper noun. Load `writing-style`; its guide is the yardstick for every comment on voice, terms and sources. For a planning doc (vision, target architecture, discovery, design), also run `horizon-review`.

## Pass 1: critique

Goal: tell the author where the argument is strong, where it is weak and what the other side would say, before any polishing.

1. **Find the claim.** State the piece's central argument in one or two sentences. If you can't, that is the first finding.
2. **Research.** Search for literature that supports it, literature that contradicts it, and well-known rebuttals. Prefer primary records (papers by DOI, the author's own post, official reports). Note who actually made each claim; secondary summaries often misattribute.
3. **Critique.** Be direct. For each weak point say what is wrong, why a reader would push back, and what would fix it: a source, an example, a narrower claim, or cutting it. Separate:
   - claims presented as fact that need a source,
   - claims that are the author's position and should be labelled as such,
   - gaps a hostile reader will exploit,
   - places where the text commits the error it argues against.
4. **Validate what holds.** Say plainly which parts are well supported and by what, so the author knows what not to touch.

Don't rewrite in this pass. Ask at most one question, only if the critique depends on the answer.

## Pass 2: edited draft

Start when the author says the rant is done. Produce the edited version in the author's chosen format (a Claude Doc by default when the session offers it).

- Fix typos, grammar and terminology silently.
- Bring every paragraph to the house voice. When a paragraph has been rewritten by the author, treat that rewrite as the voice reference and align the others to it.
- Do structural fixes (moving a section, defining a concept before it is used, re-mapping a conclusion to changed research questions) without asking. Report them afterwards.
- Leave **editor notes** where a point:
  - is not substantiated enough,
  - will be easily criticised by readers (say by whom and with what argument),
  - should be explored further.

  Each note names the paragraph, the problem and a concrete next step. In a Claude Doc use comments or suggestion cards; in markdown use `> **Editor:** …` blocks under the paragraph.
- Keep the author's own words where they already work. An edit that only changes phrasing is not worth making.

## Reference check

Run on every pass that touches sources:

- Each reference links to the record of the work, not to a blog or summary about it, and not to a loose PDF copy when a DOI or publisher page exists.
- Each quote matches the original word for word. If it can't be checked, turn it into a paraphrase.
- Each figure is attributed to the paper that produced it.
- The text states the source's claim at its actual strength.
- Fix bad references; never delete them.

Report the outcome as a short table: reference, problem, fix.

## Figures

Every figure is introduced before it appears, every series is labelled, and the reader is told what to read off it. If a figure needs redrawing, describe the change for the author.

## Output

End each pass with what changed and what is still open, in a few lines. Do not recap the steps.

## Hard rules

- Never finish a doc pass without the lint script and the reference check.
- Never keep a quotation that was not checked against the original.
- Never rewrite in pass 1; critique only.
- Never replace the author's working words with your own phrasing.

## Provenance and maintenance

Updated: 2026-11-13.

Re-verification commands:
```bash
sh plugins/techdocs/skills/writing-style/scripts/lint-prose.sh plugins/techdocs/skills/editorial-review/SKILL.md
```
