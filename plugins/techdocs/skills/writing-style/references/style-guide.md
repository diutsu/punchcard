# Writing style guide

How to write any doc, report, essay, paper or review so that readers absorb the point rather than read past it. The rules come from the author's review feedback and apply to everything written with this plugin. `SKILL.md` is the short card; `llm-tells.md` catalogues the LLM tells.

## Voice

The reader should come away understanding the point, not feeling they were told something they ought to have understood. Write so that each sentence carries the reader to the next one.

- **Explain, don't rule.** Say what something is for and why it holds. "These guide any future design work" lands better than "so it belongs here".
- **Connect the ideas.** A run of short verdicts ("X. Y. Z.") leaves the reader to rebuild the links. Join them with the reasoning that ties them: "X, so Y, while Z."
- **Avoid compressed, authoritative phrases.** Phrases like "survives unchanged", "it holds", "so it belongs" and "written close to" sound final but carry little. Say plainly what happens and when.
- **Pace the point.** Start from what the reader can see (the example, the surface statement), then name what lies behind it, then say what follows from it.
- **Don't count when the count doesn't matter.** "Two caveats matter here" or "Three consequences follow" adds a number the reader has to hold and nothing else. Keep a number only when it is part of the content, such as the seven horizons of a model.
- **No forced enumerations.** A list of three or more that exists to fill a pattern, especially when one item is a detail of another, reads as padding. Say the point the section is for.
- **No signpost lead-ins.** Drop "A concrete case shows the problem" and similar; open the example directly, for instance with "Suppose…".

## Sentences

- **One idea per sentence; vary length.** A short sentence for a hard fact, a longer one when the reasoning has to travel with it. No word cap.
- **Active voice.** Name who acts: "the storefront reads the price", not "the price is read".
- **Verbs over nominalizations.** "Validate the input", not "perform validation of the input".
- **No filler.** Cut the stock padding phrases listed in `llm-tells.md`.
- **Backtick every angle-bracket placeholder** in prose (`` `<date>` ``, `` `<module>` ``). A bare one is parsed as raw HTML and disappears in Markdown viewers. Fenced code and YAML frontmatter are exempt.
- **Plain verbs.** "Is" and "has", not the inflated substitutes catalogued in `llm-tells.md`.
- **Sentence-case headings; bold only for a defined term or a rule label; no emoji.**

## Words and terms

- **Readable names first.** Refer to things by what they are (Vision, Target architecture, Plan); numeric labels such as H5 are secondary shorthand for tables and figures.
- **One term, used consistently.** Once a term is agreed, use it everywhere and never drift back to an older one ("horizons", never "levels").
- **Avoid names that are taken.** Don't reuse the name of a known or trademarked model, even when it fits.
- **Pick words that don't overclaim.** "Invariant" promises something will never change; if the text argues that it can change, use a plainer word such as "constraint".
- **Introduce before use.** Define a term or a component before an example relies on it. Say what a thing is before explaining how to use it.
- **Be explicit about who does what, and where.** An instruction that leaves the actor or the place open counts as badly written.

## Examples

- **Anchor the point in a concrete case first,** then generalise. A scenario lands better than a principle.
- **Use generic domains.** Draw examples from common software projects such as an online shop, logistics or hospital management, not from your own company's or team's domain.
- **Tag every example with its context,** such as the horizon it applies to and the domain, so it can't be read against the wrong reference.

## Structure and claims

- **Keep the framework separate from its implementation.** Roles, tools and processes an organisation would use to run the model (drivers, sponsors, a specific record format) don't belong in the model itself; they overload it.
- **Don't commit the error the text argues against.** A piece about not prescribing mechanisms too early must not prescribe one.
- **Back framework claims with literature.** Anything presented as part of the model needs a source, or an explicit note that it is the author's position.
- **Graphs over formulas for a general audience.** Keep a formula if it helps, but explain the rule with a chart or diagram that an engineer can read at a glance. Every figure is introduced in the text before it appears, and every series is labelled.

## Sources and quotes

- **Link to the record, not to someone talking about it.** Each reference points to where the work itself is registered: the DOI, the publisher's page, the official filing or the author's own post. A blog post, glossary or summary that reports what an author said is not a reference to that author.
- **Prefer the registry over a loose copy.** A PDF on a course page or a mirror is a copy of the source, not its record. Use the DOI or the publisher's page, and keep the copy only if no record exists online.
- **Quote the author's own words, checked against the original.** If a quote can't be checked in the original, turn it into a paraphrase instead of keeping it in quotation marks.
- **Attribute a claim to whoever actually made it.** When one paper cites another for a figure, go to the original. In Planning Horizons, the 39% figure came from Aghajani et al., while "documentation goes stale silently" was Tan et al.'s point; both had been credited to Aghajani.
- **Say what the source says, at its strength.** "Might remain useful" is not "often remains useful", and "numbered records" is not "dated, immutable entries".
- **Books without an online record** are cited with publisher and ISBN and no link.
- **Fix a bad reference rather than delete it.**

## Verification pass

Style edits do not make content true. The last step of every doc pass is verification: open each link and confirm it resolves to the claimed work, compare each quotation with its source word for word, and re-run each command to confirm the output the doc states. Fix or cut whatever fails. The lint script (`scripts/lint-prose.sh`) finds surface tells; it cannot find an unsupported claim.

## Before and after

These rewrites come from the Planning Horizons paper. The "after" column is the reference for the voice.

| Before | After | What changed |
| --- | --- | --- |
| Outer horizons hold only slow-changing statements, because of reach, not distance. | Outer horizons should hold only statements that change slowly. The reason is their reach rather than their distance: their alignment cost is high, and it has to be paid back over a long life and across many consumers. | A verdict becomes an explanation of why |
| Nearer horizons are the reverse. Alignment is cheap and reach is narrow, so they can hold fast-changing detail, but only when written close to use. | Nearer horizons work the other way around. Their alignment cost is low and their reach is narrow, so they can hold detail that changes quickly, as long as it is written shortly before it is used. | "Written close to use" said plainly |
| Deferring a decision preserves options. Disseminating a decision takes time. The right moment depends on how many people have to absorb it. | Deferring a decision keeps options open, but a decision also takes time to reach everyone who has to act on it. The right moment therefore depends on how many people must absorb it. | Clipped sentences joined by their reasoning |
| Two points from Larson are central here. First, his model works bottom-up. Second, he warns that generic statements create only the illusion of alignment. | What matters most here is that his model works bottom-up, from concrete decisions to general direction. He also warns that generic statements create only the illusion of alignment. | Count and "First / Second" dropped |
| Behind that statement are two architectural decisions. | Behind that statement are real architectural decisions: "Prices are updated and published by the pricing service. The storefront makes no remote calls while serving a page". These serve as a guideline to any future design work, independent of any implementation decisions or limitations that might appear. | Count dropped; says what the decisions are for |
