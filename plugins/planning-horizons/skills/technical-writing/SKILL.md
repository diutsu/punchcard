---
name: technical-writing
description: House style for technical prose (papers, essays, blog posts, design docs, planning-horizon templates). Use when drafting or rewriting any text in this plugin's scope, and as the yardstick for editorial-review.
---

# Technical writing

The goal is prose the reader absorbs rather than reads past. The full guide, with a before-and-after table taken from the Planning Horizons paper, is in `references/style-guide.md`. Read it before drafting anything longer than a few paragraphs.

## When drafting

Write so that each sentence carries the reader to the next one. In practice that means:

- Explain what something is for and why it holds, rather than ruling that it holds.
- Join ideas with the reasoning that ties them ("X, so Y, while Z"), instead of a run of short verdicts.
- Start from what the reader can see (an example, a surface statement), then name what lies behind it, then what follows from it.
- Say plainly what happens and when. Compressed phrases such as "survives unchanged" or "written close to use" sound final and carry little.
- Keep a number only when it is part of the content. "Two caveats matter here" adds a count to hold and nothing else, and a list of three or more items that exists to fill a pattern is worse.
- Open an example directly ("Suppose…"); drop signpost lead-ins such as "A concrete case shows the problem".

## Words and terms

- Readable names first (Vision, Target architecture, Plan). H-numbers are shorthand for tables and figures.
- Once a term is agreed, use it everywhere. In this model: "horizons", never "levels"; "constraints", never "invariants".
- Pick words that don't overclaim, and introduce a term before an example relies on it.
- Every instruction names who acts and where.

## Examples and claims

- Anchor each point in a concrete case before generalising. Use generic domains (online shop, logistics, hospital), never the author's own company, and tag each example with its horizon and domain.
- Keep the framework apart from how an organisation would run it (drivers, sponsors, tooling).
- Don't commit the error the text argues against: a piece about not prescribing mechanisms early must not prescribe one.
- Anything presented as part of the model needs a source or an explicit "this is the author's position".
- For a general audience, explain a rule with a chart or diagram; a formula can stay as support.

## Sources

Link each reference to the record of the work (DOI, publisher, official filing, the author's own post), never to someone reporting on it. Quote only words checked against the original; otherwise paraphrase. Fix a bad reference rather than delete it. Details are in the guide.

## What not to do

No military analogies. No marketing tone, no "It's important to note". Don't pad a section to make it look complete: a short section that says one thing is fine.
