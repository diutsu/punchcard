# The Planning Horizons model (summary)

Source: the "Planning Horizons" paper (draft). This is a working summary for the skills; the paper is authoritative.

## What a horizon is

A horizon is a kind of planning document, defined by how far ahead it looks and by the kind of statement it may make. The further out a horizon looks, the longer its statements must hold, so the less it can prescribe. A vision can say what customers should experience in five years; it can't say which message broker will deliver it.

Each horizon has a **span**: the window over which its statements are expected to hold. Spans are defaults; the organisation's context sets the real ones.

| Horizon | Code | Default span | States | Typically written by |
| --- | --- | --- | --- | --- |
| Vision | H6 | 3–5 years | Outcomes, markets, bets, commitments | Senior engineers and product leads of the owning unit |
| Target architecture | H5 | Direction 2–3 years; concrete claims about 12 months | Components, data ownership and flow, constraints | Staff or principal engineers, with the EM |
| Plan | H4 | 6–12 months, revisited quarterly | Initiatives, order, owners, guidelines | EM and PM, with a staff engineer |
| Discovery | H3 | Started when the work is likely within about six months; time-boxed to the question | Options and evidence for one question; a recommendation | Any engineer, often a senior one |
| Technical design | H2 | 1–3 months, until the build is done | Mechanisms: protocols, schemas, products | The initiative's tech lead |
| Local design | H1 | Days to weeks | Module-level choices | Whoever builds it (PRs, READMEs) |
| Implementation | H0 | The change itself | Code | Whoever builds it |

## Half-life and the cost of deciding early

A statement has a half-life: the time after which it is as likely to be wrong as right. Past that point the document is no more useful than a coin flip. Illustrative half-lives: technical design about four months, plan about a year, target architecture about three years, vision about five years.

The cost of a wrong statement grows with everything built on it. A mechanism prescribed in a vision that turns out wrong must be unpicked from every target architecture, plan and design written under it; left open until the technical design, the same mistake costs one document. So outer horizons state outcomes and constraints, and leave mechanisms to the technical design.

## Constraints

A constraint is a statement a horizon passes down to every horizon below it. It must pass two tests:

- **Stable from below:** no choice made in a horizon below (a tool, transport, library or team) forces you to revise it.
- **Constraining:** it rules out at least one option a design team might otherwise pick. If you can't name what it rules out, delete it.

Constraints are not invariants. They can change, and findings from below can push them to change, through an amendment.

Example (online shop, target architecture): "The storefront never calls the pricing service while serving a page." Any transport survives it; per-request price lookups don't. By contrast, "the storefront receives prices through an event topic" fails the first test, because a technical design that picks another transport invalidates it.

## How documents connect

- Vision lists the capabilities it needs; each target architecture picks those up.
- Target architecture lists open questions; each becomes a discovery.
- Discovery lists every constraint from above and accepts it or proposes an amendment. Working around a constraint quietly is how upper documents go stale.
- Approved decisions flow back up as amendments, recorded in each document's amendment log.

## Living documents

Target architectures and visions are kept as one consolidated current version plus an amendment log, rather than a new document per change.

## Discovery is narrow on purpose

Discovery is input, not a decision, so it isn't approved. Its usefulness is limited in time (until the technical design is approved) and in audience (mainly the people doing the research). Beyond that group, share the recommendation, not the document; circulated widely it overwhelms both the group and its readers.

## Org scope is a separate axis

Which unit owns which horizon is independent of the horizons themselves. A startup team may own every horizon; in an established company a common pattern is company → vision, department → vision and target architecture, group → down to plan, teams → discovery and below.

## Terms

- "Horizons", never "levels". Readable names first, H-codes second.
- "Constraints", never "invariants".
- No military analogies.
