# Discovery (H3) — template

> Lines in quotes are guidance to replace; lines in italics are examples (fictional online shop).

## How to use this template

> Discovery maps a problem and its options. It feeds a technical design (H2) and is not a decision itself, so it is not approved. Start it when the work is likely to begin within about six months, and time-box it to the question. Its usefulness is narrow, in time and in audience: it matters until the technical design is approved, and mainly to the people doing the research. Beyond that group, share the recommendation, not the doc; circulated widely, it overwhelms both the group and its readers.

> You must list every constraint from the horizons above (Section 2) and either accept it or propose a change (Section 7). Discovery that quietly works around a constraint is how a target architecture goes stale.

## Metadata

| Field | Value |
| --- | --- |
| Horizon | Discovery (H3) |
| Default span | Started when the work is likely within about six months; time-boxed to the question |
| Question | *One sentence; see Section 1* |
| Author | *Any engineer, often a senior one* |
| Audience | The people doing the research and the technical design's author. Beyond them, share the recommendation (Section 8), not this doc |
| Feeds | *The target-architecture gap, plan initiative or PRD this informs, and the technical design that will decide* |
| Time-box | *End date for this discovery* |
| Expected pick-up | *When the technical design is expected to start* |
| Status | Open · Recommendation ready · Folded into technical design |
| Retired | When the technical design is approved. Link it here and stop updating this doc |
| Approval | None. Reviewers check that the options are complete, not which one is chosen |

## 1. The question

> One question, in one sentence. Name the decision it informs and the technical design that will make it.

*Example: How should the storefront get its own copy of prices, so that product pages never wait on the pricing service? This informs the technical design for gap 1 of the Pricing target architecture.*

## 2. Constraints from above (required)

> List every constraint (Target architecture), guideline (Plan) and requirement (PRD) that applies, with a link. For each, say whether this discovery accepts it as it is or challenges it. Every challenge must have an entry in Section 7. Discovery cannot start with this table empty.

| Constraint | Source | Accepted or challenged | Note |
| --- | --- | --- | --- |
| *The storefront never calls the pricing service while serving a page* | *Pricing target architecture, constraint 1* | *Accepted* | *Rules out per-request lookups* |
| *A price change reaches every channel within the agreed delay* | *Pricing target architecture, direction; flash-sale PRD* | *Challenged* | *Flash sales may need a tighter bound for the storefront; see Section 7* |

## 3. Requirements

> Requirements taken from PRDs and stakeholders. Make them measurable where you can, and mark any you inferred rather than were given.

## 4. Current state

> How it works today, in as much detail as the options need. Naming technologies is fine here.

## 5. Options

> At least three options, including one that challenges an assumption. Mechanisms here are illustrative sketches, and nobody is held to them. Check every option against every constraint in Section 2.

| Option | Sketch (illustrative) | Fits the constraints? | Evidence | Main risk | Size |
| --- | --- | --- | --- | --- | --- |
| *A. Event stream and local copy* | *Pricing publishes each change; the storefront keeps a local copy* | *Yes, all accepted ones* | *Spike (Section 6)* | *Missed events need a recovery path* | *M* |
| *B. Snapshots at the edge* | *Pricing writes periodic price files that the CDN serves* | *Yes, but the delay depends on snapshot frequency* | *Not yet tested* | *Flash-sale prices lag by one interval* | *S* |
| *C. Read replica* | *The storefront reads from a replica of the pricing database* | *Technically yes, but it ties the storefront to pricing's schema* | *Replicas already supported* | *Every schema change becomes a cross-team change* | *S* |

## 6. Evidence and spikes

> What you tried, what you measured and what you could not test. Link the code or notebooks.

## 7. Proposed changes to the horizons above

> Where discovery shows that a constraint from above is wrong, too strict or missing, propose an amendment here instead of working around it. The owner of that document settles it before the technical design is approved.

| Statement | Horizon | Proposed change | Evidence | Status |
| --- | --- | --- | --- | --- |

## 8. Recommendation

> The option you recommend and why, in a few sentences. This is a recommendation, not a decision; the technical design decides.

## 9. Kill criteria

> Measurable conditions that would make the recommendation wrong, or show that a constraint above cannot hold. Each one names what to revisit.

## 10. Open questions for the technical design

> What is still open. Copy these into the technical design, where they become decisions or stay explicitly open.

## Before you share this

- [ ] One question, linked to the decision and to the technical design it feeds.
- [ ] Every constraint from above is listed and marked as accepted or challenged.
- [ ] Every challenge has an entry in Section 7.
- [ ] At least three options, one of them challenging an assumption, with mechanisms marked as illustrative.
- [ ] Kill criteria are measurable and name what to revisit.
- [ ] Nothing commits, and the recommendation is labelled as a recommendation.
- [ ] Open questions are ready to copy into the technical design.
- [ ] Shared with the people doing the research and the technical design's author; only the recommendation goes wider.
