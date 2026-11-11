# Vision (H6) — template

> Lines in quotes are guidance to replace; lines in italics are examples (fictional online shop).

## How to use this template

> Write one Vision per unit that owns a domain, at whatever scope: company, department, group or team. The vision of the unit above is an input to it, not a replacement. It states outcomes, markets and bets. It names no technology as a decision; that belongs to the target architecture.

> Vision statements must hold for 3–5 years. They are acted on immediately and by everyone, so they carry the highest alignment cost of any horizon. Revise them only for reasons at this horizon, such as a market shift, a regulation or an acquisition, never because of a delivery detail. A mechanism prescribed here that turns out wrong has to be unpicked from every document built on it, so leave mechanisms to the horizons below.

> Time-box for agreement: one planning cycle. A vision that takes longer to agree than that is usually trying to settle questions that belong to Plan.

## Metadata

| Field | Value |
| --- | --- |
| Horizon | Vision (H6): the owning unit's vision for its domain |
| Default span | 3–5 years |
| Scope | *The owning unit: company, department, group or team, e.g. the Commerce department* |
| Authors | Senior engineers and product leads of the owning unit |
| Feedback from | The unit's teams, adjacent units |
| Approver | The unit's leadership team |
| Maintainer | The authors |
| Status | Draft · In review · Approved · Superseded |
| Agree by | *End of the current planning cycle* |
| Review triggers | Annual planning; a market, regulatory or ownership change; accumulated amendments from target architectures |
| Related | The vision of the unit above, product strategy, target architectures (H5), plan (H4) |

## 1. Why

> Who you serve and what problem you solve for them, in two or three sentences. This rarely changes; if it does, everything below changes with it.

*Example: The Commerce department helps independent brands sell everywhere their customers shop (their own site, apps and marketplaces) without running their own warehouses or pricing systems.*

## 2. Where we are today (framing)

> An honest picture of the current position: customers, markets, strengths and constraints. Be concrete. This section frames the problem; it decides nothing.

*Example: Most of our merchants sell mainly through their own web shop. Marketplace sales are growing fastest but are managed in separate tools. On peak days our platform is the bottleneck: merchants cap their promotions because they do not trust it to hold.*

## 3. Where we want to be (3–5 years)

> The end state, stated as outcomes for customers and the business. Each statement must be specific enough that someone could disagree with it, and must name no technology.

*Example:*
- *A merchant manages stock, prices and orders for every channel in one place.*
- *A shopper sees the same price and availability on every channel at any moment.*
- *Peak days are ordinary days: merchants never cap a promotion because of the platform.*

*Too vague: "Become the leading commerce platform." Nobody can disagree with it, so it decides nothing.*
*Too detailed: "Move to an event-driven microservice architecture by 2028." That is a technology decision with a date; it belongs in a target architecture, without the date.*

## 4. Bets

> The few strategic bets this vision depends on: what you believe that others may not. Each bet names the signal that would make you drop it. Keep the list short: every bet is something the horizons below have to live with.

| Bet | Why we believe it | Signal that would change our mind |
| --- | --- | --- |
| *Marketplaces will be most merchants' largest channel within a few years* | *Marketplace sales grow fastest across our merchants* | *Marketplace growth stalls for a full year* |

## 5. Non-goals

> What this vision deliberately does not pursue. One non-goal someone would actually have expected is worth more than a list of obvious ones.

*Example: Running our own delivery fleet. Selling to shoppers under our own brand.*

## 6. Commitments every horizon must respect

> Promises to customers, and legal or ethical constraints, that hold everywhere below. They are the constraints this horizon passes down, so they must pass the same two tests: no delivery decision should force you to revise one, and each must rule something out.

| Commitment | Rules out | Why |
| --- | --- | --- |
| *A shopper is always charged the price they were shown.* | *Silent re-pricing anywhere between product page and payment* | *Shopper trust; consumer-protection rules in many markets* |
| *Merchant and shopper data stays in the regions merchants sell from.* | *Processing or storing that data in other regions* | *Merchant contracts and data-protection law* |

## 7. What this asks of the horizons below

> The capabilities this vision needs, each tied to an outcome in Section 3. State capabilities, not systems: target architectures decide how to provide them.

| Capability | Serves outcome | Domain, if known |
| --- | --- | --- |
| *Prices and availability reach every channel within an agreed bound* | *Same price and availability everywhere* | *Pricing; inventory* |

## 8. How we will know

> The signals that show whether the vision is working, reviewed yearly. Name the signals here; set targets at annual planning, where they can change without reopening the vision.

## 9. Open questions

> What this vision does not know yet and needs market research or discovery to answer. Each item names the bet, outcome or non-goal it could change.

## 10. Amendment log

> Every change after approval, newest first. Amendments at this horizon should be rare. They usually come from a market shift or from findings that have built up across target architectures.

| Date | Change | Triggered by | Approved by |
| --- | --- | --- | --- |

## Before you send this for review

- [ ] Every outcome is something someone could reasonably disagree with, and none names a technology.
- [ ] No dates finer than a year.
- [ ] Every bet names the signal that would change your mind.
- [ ] Every commitment says what it rules out.
- [ ] Section 7 states capabilities, not systems, each tied to an outcome.
- [ ] Signals are named, and targets are left to annual planning.
- [ ] At least one non-goal is something readers would have expected you to do.
