---
name: external-research
tier: leaf
description: >
  Evaluate anything that lives outside the repo before adopting it: a library,
  API, SaaS provider, ML model, data source, or protocol. Trigger on "should we
  use X", "compare X vs Y", "is there a library for", "which API", "what model
  should we use for", or before any query/API call crosses the network boundary
  (enforces the privacy wall). Produces a structured evaluation in
  docs/investigations/<slug>.md. Do NOT use for questions answerable from this
  repo's own code/docs (use internal-research) or for writing an execution plan
  (use research-to-plan).
trigger: /external-research
---

# /external-research

Evaluate external dependencies, APIs, and data sources **before** adopting them. Every external dependency is a liability until proven otherwise.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Mining this repo's own code, docs, or git history | `internal-research` |
| Turning an adoption decision into a gated execution plan | `research-to-plan` |
| Inspecting or measuring an already-running local/remote service | `operate-and-diagnose` |

## 1. Privacy wall — apply before any external query

**No real personal, proprietary, or financial data ever leaves the machine** — not in a search query, API test call, request body, or issue tracker search:
1. **Substitute synthetic data.** Always test parsers, APIs, or models with fabricated sample inputs, never real user/account exports.
2. **Never create external accounts or API keys on the user's behalf.** If evaluating a provider requires signup/auth, evaluate public docs first; if a POC still requires an account, stop and queue it in `docs/operator-instructions.md` (`## Run queue`).
3. **Abstract project specifics.** Describe the technical shape of the problem, never private project data.

## 2. Evaluation method (vendor claims vs. independent evidence)

| Axis | Vendor claim (low trust) | Independent evidence (required) |
|---|---|---|
| **Correctness** | Marketing copy / README | Open and closed issues in the repo tracker for the exact edge cases you need |
| **Maintenance** | Badges | Last release date, commit cadence, open PR age, changelog for recent breaking changes |
| **Bus factor** | Stars count | Active maintainer count; is it a single-author side project? |
| **License** | Summary page | Actual `LICENSE` file and transitive dependency licenses |
| **Data quality** | "Accurate & reliable" | Independent user reports + a planned standalone reconciliation audit (`data-integrity`) |

**Multi-source bar:** Never recommend adoption from a single source. Require at least 2 independent signals, and explicitly label capabilities as `documented, untested` vs. `tested: <result>`.

## 3. POC bar before recommending adoption

Before recommending `"adopt X"`:
1. Define the **smallest point-of-proof experiment** runnable inside the repo on synthetic fixtures.
2. State the **expected numeric pass/fail threshold** in advance.
3. Hand the POC definition to `research-to-plan` — never build a half-wired integration inside the research pass.

## 4. Output contract (`docs/investigations/<slug>.md`)

When persisting external research to `docs/investigations/<slug>.md` (`type: investigation`), always place `## Verdict & promoted rules` ($\le 10$ lines) at the very top (per `docs-management`), followed by the structured evaluation table:

```markdown
## Verdict & promoted rules
- **Verdict:** `<Adopt | Reject | Needs POC | Needs operator account — 1-2 sentences>`
- **Promoted to permanent docs:** `<none | links to docs/requirements/ or docs/logic/>`
- **Fenced-off dead ends:** `<Rejected candidates + 1-line reason>`

## Candidate evaluation
- **Candidate:** `<name & version>`
- **Claims vs. evidence:**
  - `<claim>` — `[vendor | independent]` (`[documented, untested | tested]`) — `<URL>`
- **Maintenance & license:** `<last release, bus factor, verified license>`
- **POC experiment:** `<smallest test + advance numeric pass/fail bar>`
```

## Hard rules

- Never transmit real personal, account, or proprietary data to an external search or API — use synthetic data only.
- Never sign up for external accounts on the user's behalf.
- Never recommend adoption from a single source or present `"documented"` as `"tested"`.
- Never write raw web research into `docs/requirements/` or `docs/logic/` — write to `docs/investigations/<slug>.md` with a top `## Verdict & promoted rules` block.
- Never implement a half-built integration during a research pass — stop at the finding and hand off to `research-to-plan`.

## Provenance and maintenance

Updated: 2026-10-11 (v2: added `tier: leaf` and wired persistent output to `docs/investigations/<slug>.md` with top verdict block).

Re-verification commands:
```bash
ls doc-templates/docs/investigations/_template.md
```
