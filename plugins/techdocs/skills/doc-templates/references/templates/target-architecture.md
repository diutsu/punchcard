---
type: explanation
state: wip
created: YYYY-MM-DD
updated: YYYY-MM-DD
cross-file-references: []
---
# Target architecture (H5) — template

> Lines in quotes are guidance to replace; lines in italics are examples (fictional online shop).

## How to use this template

> Write one document per domain, for example "Pricing" or "Fulfilment". Keep one consolidated current version, and record every change in the amendment log (Section 11) rather than starting a new document.

> Target-architecture statements must hold for 2–3 years in direction and about 12 months in concrete claims. Test every sentence: if it would need rewriting because a horizon below picked a different tool, transport or library, it belongs in a technical design.

> Time-box for agreement: about one month. If it takes longer, the domain is not ready for a target architecture. Run Discovery (H3) first.

## Metadata

| Field | Value |
| --- | --- |
| Horizon | Target architecture (H5): technical vision, target architecture, domain model |
| Default span | Direction 2–3 years; concrete claims about 12 months |
| Domain | *e.g. Pricing* |
| Authors | Staff or principal engineers, with the EM |
| Feedback from | Adjacent teams, product leadership, architecture forum |
| Approver | Head of engineering or architecture forum |
| Maintainer | The authors, who keep the consolidated version current |
| Status | Draft · In review · Approved · Superseded |
| Consolidated as of | *Date of the last amendment folded in* |
| Agree by | *About one month after the first draft* |
| Review triggers | An approved plan or technical-design decision that extends or contradicts this document; annual review |
| Related | Vision (H6), product vision, Plan (H4) roadmap and guidelines |

## 1. Purpose and scope

> Which domain this covers, which problem it addresses, and who it is for. Two or three sentences.

*Example: This document sets the direction for how prices are set, stored and shown across the shop's sales channels: web, app and marketplace feeds. Promotions and tax are out of scope (see Section 8).*

## 2. Current state (framing)

> Describe today concretely, in language readers know. Naming current technologies is fine here, because it frames the problem. Nothing in this section is a decision about the future.

*Example: Today the storefront calls the pricing service synchronously on every product page. During sales events, pricing latency becomes the largest part of page load time, and a pricing outage takes product pages down with it.*

## 3. Direction (2–3 years)

> The end state, stated as outcomes rather than mechanisms. Each statement must be specific enough that someone could disagree with it.

*Example:*
- *A price change reaches every sales channel within an agreed, bounded delay.*
- *A pricing outage never stops a customer from browsing or buying at the last known price.*

*Too vague: "Improve pricing performance." Too detailed: "Move prices to Kafka by Q3." That is a mechanism and a date, which belong in Plan and Technical design.*

## 4. Domain model and components

> Name the components and domain concepts that the horizons below will refer to, with their responsibilities and owners. Name components by role, not by product. A diagram can help; its arrows show who owns which data and which way it flows, not protocols.

| Component | Responsibility | Owner |
| --- | --- | --- |
| *Pricing service* | *Source of truth for prices and pricing rules* | *Pricing team* |
| *Storefront* | *Renders product and category pages for web and app* | *Web team* |

## 5. Constraints

> The properties every horizon below must respect. Each constraint must pass two tests. **Stable from below:** no choice in a horizon below, such as a tool, transport, library or team, forces you to revise it. **Constraining:** it rules out at least one option a design team might otherwise pick. If you cannot name what it rules out, delete it.

| Constraint | Rules out | Survives (choices below that do not break it) | Why it matters |
| --- | --- | --- | --- |
| *The storefront never calls the pricing service while serving a page.* | *Per-request price lookups* | *An event stream with a local copy; snapshots pushed to the edge; database replication* | *Pricing outages and slow-downs no longer reach customers* |
| *Only the pricing service writes prices.* | *Price edits made in feeds or in the storefront* | *Any number of read copies* | *A single source of truth makes the delay bound measurable* |

*Too vague: "Prices must be correct." It rules nothing out.*
*Too detailed: "Prices are published on a Kafka topic with a 60-second TTL." It breaks as soon as a design picks another transport.*

## 6. Target architecture

> The end state: which components exist, who owns which data, and which way it flows. Concrete claims should hold for about 12 months, direction for 2–3 years. Do not choose protocols, products or field names. If you name a technology, say whether it describes the current state or is a justified one-way door.

## 7. Gaps and rough path

> The gaps between the current state and the target, in the order you would close them, each with an order-of-magnitude size. This shows the target architecture is feasible; it is not a commitment. The committed order, owners and dates live in the plan (H4).

| # | Gap | Why in this order | Size | Depends on |
| --- | --- | --- | --- | --- |

Sizes are for one team: S = weeks, M = about a quarter, L = about two quarters, XL = more.

## 8. Non-goals

> What this target architecture deliberately does not try to do, so that readers do not infer it.

## 9. Guidelines

> The Plan (H4) guidelines this target architecture relies on, and any new ones it implies. A new guideline is justified only if it settles a debate that keeps coming back. Each one leads with the property, names the default mechanism as the paved road, and has a review date.

## 10. Open questions for discovery

> What this target architecture does not know yet and needs Discovery (H3) to answer. Each item names the constraint or gap it could change.

## 11. Amendment log

> Every change after approval, newest first. Most amendments come from below: an approved technical-design or plan decision that extends or contradicts this document. Fold each one into the text above and log it here.

| Date | Change | Triggered by | Approved by |
| --- | --- | --- | --- |

## Before you send this for review

- [ ] Every Direction statement is an outcome, and someone could reasonably disagree with it.
- [ ] Every constraint passes both tests and says what it rules out.
- [ ] Technologies appear only in the current state, or as justified one-way doors.
- [ ] No dates finer than a year; no field names, endpoints or protocols.
- [ ] Components are named by role, with an owner each.
- [ ] The rough path lists gaps in order with sizes, and no committed dates.
- [ ] Open questions are linked to the constraints or gaps they could change.
- [ ] Reviewers know the model: questions about *how* get the reply "that is a technical-design question; which constraint would it change?"
