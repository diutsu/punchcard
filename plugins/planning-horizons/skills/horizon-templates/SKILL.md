---
name: horizon-templates
description: Draft or fill a planning document (vision, target architecture, plan, discovery, technical design) from the Planning Horizons templates. Use when someone asks to write, start, restructure or convert a planning or design doc, or asks which horizon a document belongs to.
---

# Horizon templates

Read `references/model.md` first: it says what a horizon is, the default spans, the constraint tests and how documents connect. Then pick the template.

| Horizon | Template | Status |
| --- | --- | --- |
| Vision (H6) | `references/templates/vision.md` | Draft |
| Target architecture (H5) | `references/templates/target-architecture.md` | Draft |
| Plan (H4) | none yet | Not started |
| Discovery (H3) | `references/templates/discovery.md` | Draft |
| Technical design (H2) | none yet | Not started |

Local design (H1) and Implementation (H0) need no templates: their decisions live in PRs, READMEs and tickets.

## Choosing the horizon

Ask what the document will decide and for how long that decision has to hold:

- outcomes and bets for several years → Vision
- components, data ownership and constraints for a domain → Target architecture
- order, owners and dates for the next quarters → Plan
- options for one question, with a recommendation and no decision → Discovery
- the mechanism for one piece of work → Technical design

If a draft mixes horizons (a vision that names a broker, a discovery that "decides"), say so and propose splitting it. Don't silently move content.

## Filling a template

1. Copy the template's structure, metadata table included. Keep the section numbers so cross-references work.
2. Replace guidance (quoted lines) with content. Delete the guidance once a section is filled; keep it while the section is empty.
3. Examples (italic lines) are there to show the level of detail. Replace them; never leave the online-shop examples in a real document.
4. Fill the "upstream" sections from the real documents above: a discovery's constraint table comes from the actual target architecture and plan, with links. If they don't exist, say so in the table instead of inventing constraints.
5. Run the checklist at the end of the template and report which items fail.
6. Write the prose with the `technical-writing` skill. Then run `horizon-review` on the result.

## Plan and Technical design

There are no templates for these yet. If asked for one, draft it from `model.md` with the same shape as the others (how-to-use guidance, metadata, numbered sections, a checklist), mark it "unofficial draft", and say which parts are your own proposal rather than the model's.

## Output

By default produce a Claude Doc when the session offers one; otherwise markdown. One horizon per document. Name it "<Domain or question> — <Horizon>".
