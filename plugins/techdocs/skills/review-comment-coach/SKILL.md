---
name: review-comment-coach
tier: leaf
description: >
  Help reviewers of planning docs write comments at the right horizon, and help
  authors answer comments that belong elsewhere. Load when drafting or
  triaging review comments on a vision, target architecture, discovery or
  technical design. Do NOT load to review the doc itself (see horizon-review),
  to process in-doc `[COMMENT]` markers (see handle-comments), or to polish
  prose (see editorial-review).
trigger: /review-comment-coach
---

# Review-comment coach

Most review threads on planning documents go wrong the same way: a reviewer asks *how* on a document that is only allowed to say *what*, the author answers, and the document grows a mechanism it was never meant to hold. This skill keeps each comment at the horizon of the document it's on.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Reviewing the doc statement by statement | `horizon-review` |
| Resolving `[COMMENT]` markers embedded in a doc | `handle-comments` |
| Prose and source edits | `editorial-review` |

Load `${CLAUDE_SKILL_DIR}/../doc-templates/references/model.md` for the horizons and constraint tests.

## For reviewers: drafting a comment

Before posting, check the comment against the document's horizon:

- **Asks for a mechanism on a vision or target architecture** ("which broker?", "what's the schema?") → rewrite as a question about the constraint or outcome: "Which constraint would that choice change?" or "Does this rule out a per-request lookup?" If the mechanism really matters now, propose an open question for discovery instead.
- **Asks for dates finer than a year above Plan** → point it at the plan.
- **Disagrees with an outcome or constraint** → good comment; make sure it says what the statement would rule out or wrongly allow, with a concrete case.
- **Vague approval or vague concern** ("feels risky") → ask the reviewer to name the statement and the scenario.

Return the rewritten comment, plus one line on why it changed.

## For authors: triaging comments

Sort incoming comments into:

| Kind | Reply |
| --- | --- |
| At this horizon (challenges an outcome, constraint, gap or bet) | Engage and, if accepted, amend |
| Below this horizon (asks how) | "That is a technical-design question; which constraint would it change?" Add it to open questions if it's real |
| Above this horizon (questions the vision or a constraint from above) | Point to the upper document and its owner; propose an amendment there if the comment is right |
| Not a planning question (wording, typos) | Fix silently |

Draft the replies in the author's voice: short, direct, no defensiveness. Follow the `writing-style` skill.

## Hard rules

- Never use the model to shut down a valid concern. If a "how" question reveals that a constraint can't hold, that's a finding for the document, not an off-horizon comment.
- Never draft a comment that names a mechanism on a vision or target architecture without tying it to a constraint.

## Provenance and maintenance

Updated: 2026-11-13. From the former planning-horizons plugin.

Re-verification commands:
```bash
sh plugins/techdocs/skills/writing-style/scripts/lint-prose.sh plugins/techdocs/skills/review-comment-coach/SKILL.md
```
