---
type: explanation
state: wip
created: YYYY-MM-DD
updated: YYYY-MM-DD
cross-file-references: []
---
# `<Title>`: technical design

> Lines in quotes are guidance. Replace each with content, then delete the guidance. Horizon: Technical design (H2), valid for 1-3 months until the build is done.

## Summary

> Two or three sentences: the problem, the chosen mechanism, the main trade-off. A reader who stops here should know what will be built.

## Context and goals

> The need, who has it, and what done looks like. Link the PRD and the target architecture. List non-goals so scope stays visible.

## Constraints from above

> One row per constraint from the target architecture or plan that applies. Mark each accepted or challenged; give a proposed amendment for each challenge. Say "none exist" when the upper documents are missing.

| Constraint | Source | Accepted or challenged | Note or amendment |
| --- | --- | --- | --- |

## Design

> The mechanism: components, data model, interfaces, sequence of a typical request. Name protocols, schemas and products here; this is the horizon where they belong. Introduce each component before an example uses it. Add a diagram when structure is easier to see than to read.

## Alternatives considered

> Each real option with why it lost. Link an ADR when the choice is durable.

## Risks and open questions

> What could fail, how you would notice, and what is still undecided, each with an owner.

## Rollout and verification

> How the change ships, how to roll back, and which checks prove it works (commands or tests).

## Checklist

- [ ] Every applicable constraint from above is listed and marked
- [ ] No mechanism contradicts a constraint without an amendment
- [ ] Every command and link has been run or opened
- [ ] Settled behaviour has a destination in `reference/` once built
