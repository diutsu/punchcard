---
name: writing-style
tier: reference
description: >
  The one prose style for every doc, report and review: plain words, active
  voice, concrete examples, checked sources, no LLM tells. Load before drafting
  or rewriting more than a few paragraphs. Do NOT load for doc placement
  (docs-management), code comments (backend-code) or skeletons (doc-templates).
trigger: /writing-style
---

# /writing-style

A rule card. The full guide is `./references/style-guide.md`; the catalogue of LLM tells and word lists is `./references/llm-tells.md`. Read the guide before a long draft.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Which folder or frontmatter a doc gets | `docs-management` |
| The skeleton of an ADR, design doc, PRD or research doc | `doc-templates` |
| Critiquing and editing a finished draft | `editorial-review` |
| Code comments and docstrings | `backend-code` |

## Rules

1. **Explain, do not rule.** Say what a thing is for and why it holds. Join ideas with their reasoning ("X, so Y, while Z") instead of a run of short verdicts.
2. **One idea per sentence; vary length.** No word cap. Break a sentence when it carries two claims.
3. **Active voice, no nominalizations.** Name who acts: "storage rejects the write", "configure", not "performs configuration of".
4. **No filler.** Cut "in order to", "it should be noted", "basically", "essentially", signpost lead-ins, and counts that carry no content ("two caveats matter").
5. **One term per concept.** Define a term before an example uses it. Avoid words that overclaim ("invariant" for something that can change).
6. **Concrete first.** Open with a case, then generalise. Use generic domains (online shop, logistics, hospital), never the author's own company.
7. **Backtick every angle-bracket placeholder** in prose: `` `<date>` ``, never bare. CommonMark reads a bare one as raw HTML.
8. **Sentence-case headings.** Bold only for a defined term or a rule label. No emoji.
9. **Cite the record, not the retelling.** Link to the DOI, publisher page or author's own post. Quote only words checked against the original; otherwise mark a paraphrase. State a claim at its source's strength and credit whoever made it.
10. **Plain verbs.** Write "is" and "has", not "serves as", "stands as", "boasts", "features".

## LLM tells

Write none of these; the catalogue gives the pattern and the rewrite for each.

- significance puffery ("pivotal", "testament", "evolving landscape")
- trailing "-ing" analysis clauses ("highlighting...", "ensuring...")
- vague attribution ("experts say", "industry reports") and vague links ("associated with", "in connection with")
- stress on a source's existence ("featured in", "his profile identifies him as") instead of what it says
- formulaic "challenges and outlook" sections and upbeat codas
- vocabulary clusters (delve, tapestry, leverage, robust, seamless, comprehensive, crucial, pivotal, meticulous, intricate, underscore, showcase, foster, enhance, multifaceted, utilize)
- "not just X but Y", "not X but Y", "Y rather than X"; forced triplets; synonym-swapping for one referent
- disclaimers about missing sources ("details are limited", "does not by itself establish") that fill the gap with guesses
- closing summaries and "in conclusion"
- hedging that fills a gap with speculation
- em-dash overuse; every sentence the same length
- title-case headings, scattered bold, bold-label bullet lists
- chatbot residue: offers, apologies, leftover placeholders, markdown in plain text
- dead links, sources that do not back the claim, `utm_` tracking parameters

## Final pass

1. Run `sh ./scripts/lint-prose.sh <file>` (relative to this skill folder); fix every `file:line: pattern` it prints.
2. Verify the content, because removing surface tells does not fix unsupported claims: open each link, check each quote against its source, re-run each command.

## Hard rules

- Never scrub tells from a claim you cannot support; cut or source the claim.

## Provenance and maintenance

Updated: 2026-11-27. Source for the LLM-tells rules: Wikipedia, "Signs of AI writing" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing).

Re-verification commands:
```bash
sh plugins/techdocs/skills/writing-style/scripts/lint-prose.sh plugins/techdocs/skills/writing-style/references/style-guide.md
wc -l plugins/techdocs/skills/writing-style/SKILL.md
```
