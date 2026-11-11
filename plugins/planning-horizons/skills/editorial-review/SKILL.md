---
name: editorial-review
description: Critique a rant, essay, paper or planning document and turn it into an edited draft with editor notes. Use when the author shares a draft or a rant and asks for a review, critique, validation, fact check or edit.
---

# Editorial review

The author writes first and fast; this skill is the editor. It works in two passes, and the author decides when to move from the first to the second.

Load the `technical-writing` skill first. Its style guide is the yardstick for every comment on voice, terms and sources. If the draft is a planning document (vision, target architecture, plan, discovery, technical design), also run `horizon-review`.

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

Every figure is introduced before it appears, every series is labelled, and the reader is told what to read off it. If a figure needs redrawing, describe the change or hand it to the diagramming skill when it is available.

## Output

End each pass with what changed and what is still open, in a few lines. Don't recap the steps.
