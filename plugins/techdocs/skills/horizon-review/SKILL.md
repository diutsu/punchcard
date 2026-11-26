---
name: horizon-review
tier: workflow
description: >
  Check a planning doc against the Planning Horizons model, statement by
  statement. Load when reviewing a vision, target architecture, discovery or
  technical design, or judging a statement's horizon or a constraint. Do NOT
  load for prose (editorial-review) or comment triage (review-comment-coach).
trigger: /horizon-review
---

# Horizon review

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Polishing prose, sources and style | `editorial-review` |
| Writing or triaging review comments | `review-comment-coach` |
| Starting a doc from a skeleton | `doc-templates` |
| Placement, frontmatter | `docs-management` |

Read `../doc-templates/references/model.md` first for the horizons, spans and constraint tests.

The review has two parts. Run both unless the user asks for one.

## Part 1: lint the document

Go statement by statement through every section that makes claims (skip framing sections such as "Current state", where naming technologies is fine).

For each statement decide:

- **Which horizon it belongs to**, judged by what it fixes and how long it must hold. A statement that names a protocol, product, schema or field belongs in a technical design wherever it appears. A date finer than a year doesn't belong above Plan.
- **Whether it decides anything.** A statement nobody could disagree with ("improve performance", "prices must be correct") decides nothing; flag it as too vague.
- **For constraints, the two tests:**
  - Stable from below: would any tool, transport, library or team choice below force a rewrite? If yes, it's a mechanism, not a constraint.
  - Constraining: name what it rules out. If nothing, delete it.
- **Whether the text commits the error the model argues against**, such as a vision prescribing a mechanism "for alignment".

Report as a table:

| Section | Statement | Problem | Belongs in | Suggested rewrite |
| --- | --- | --- | --- | --- |

Then run the template's own checklist and list the items that fail.

Keep the rewrite at the right horizon: lift a mechanism to the outcome or constraint behind it ("publish prices on a topic" → "the storefront never waits on pricing while serving a page"), and move the mechanism itself to an open question for discovery or the technical design.

## Part 2: check across horizons

Needs the related documents. If they aren't available, say which ones you'd need and stop.

- **Downward:** every constraint and capability the upper document passes down is picked up by the documents below, or explicitly out of their scope.
- **Upward:** every discovery and technical design lists each applicable constraint from above, marks it accepted or challenged, and has a proposed amendment for each challenge. A design that quietly contradicts a constraint is the main finding to report.
- **Amendments:** approved decisions below that extend or contradict an upper document appear in its amendment log and are folded into its text.
- **Staleness:** flag statements past the horizon's span, and documents past their review triggers.
- **Discovery scope:** a discovery should be retired once its technical design is approved, and its audience should be the research group; flag discoveries being circulated as if they were decisions.

Report as a list of mismatches, each with both documents, the statements involved and who should act (the owner of the upper document settles amendments).

## Tone

Findings, not lectures. Each finding names the statement, says why it's at the wrong horizon or fails a test, and gives a rewrite. Don't restate the model to the author.

## Hard rules

- Never judge a statement without naming the horizon it belongs to and the test it fails.
- Never move content to another horizon silently; propose the split.
- Never invent the upper or lower documents; list the ones you would need and stop.
- Never restate the model to the author; give findings.

## Provenance and maintenance

Updated: 2026-11-14. Source: the Planning Horizons paper.

Re-verification commands:
```bash
test -f plugins/techdocs/skills/doc-templates/references/model.md
sh plugins/techdocs/skills/writing-style/scripts/lint-prose.sh plugins/techdocs/skills/horizon-review/SKILL.md
```
