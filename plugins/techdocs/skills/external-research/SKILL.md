---
name: external-research
tier: leaf
description: >
  A sourced research doc on a library, API, provider, model or standard outside
  the repo. Load on "should we use X", "compare X and Y", "is there a library
  for", or before any query leaves the machine. Do NOT load for questions the
  repo answers (codebase-search) or plans (plan).
trigger: /external-research
---

# /external-research

Every external dependency is a liability until evidence says otherwise. Collect evidence, quote it, and say what you did not check. Output uses `../doc-templates/references/templates/research-doc.md` and lands at the `investigations` map key (resolve through `project-map`).

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Mining this repo's code, docs or history | `codebase-search` |
| Turning a verdict into a work plan | `plan` |
| Measuring a running system | `operate-and-diagnose` |
| Judging an evaluated tool's fit to the project | `project-evaluation` |
| Editing the finished doc | `editorial-review` |

## 1. Privacy wall

Apply before any query, API call, request body or tracker search.

1. No real personal or financial data, no real name or email (including the user's), leaves the machine. Describe the technical shape of the need and use fabricated sample inputs.
2. Never create an external account or key for the user. If a proof of concept needs one, evaluate public docs first, then record the signup as an open question via `tracker`.
3. Never paste project docs into an external service to justify a request.

## 2. Collect

1. Write the question and the decision it feeds.
2. For a wide sweep (three or more candidates, or an unfamiliar space), fan out searches or use a deep-research skill; fetch each page instead of trusting a snippet.
3. Prefer primary records: the project's repo and issue tracker, the standard, the paper's DOI, the vendor's own docs for what they claim. A blog that reports on a source is a pointer to it, not the source.
4. Check each axis against independent evidence, not vendor claims:

| Axis | Look at |
|---|---|
| Correctness | open and closed issues for your exact edge cases |
| Maintenance | last release date, commit cadence, open PR age, recent breaking changes |
| Bus factor | active maintainers; single-author project or not |
| License | the actual `LICENSE` file and transitive licenses |
| Data quality | independent reports, and a planned reconciliation against a second source |

## 3. Record each finding

- Link the primary source (no `utm_` parameters).
- Give either a short verbatim quote checked against the page, or a paraphrase marked "paraphrase". Never present a recalled quote as verbatim.
- Mark each claim fact (the source states it) or inference (you conclude it).
- Mark each capability `documented, untested` or `tested: <result>`.
- State a claim at the strength of its source and credit whoever made it.

## 4. Recommend

- No recommendation without at least two independent sources. A single source gives a lead, not a verdict.
- Name the smallest proof-of-concept that runs on synthetic fixtures, with the pass or fail threshold fixed before running it. Hand it to `plan`; do not build a half integration during research.
- End with what was not checked: sources not reached, claims resting on one source, features not exercised.

## 5. Verify

Run `writing-style` and `editorial-review` on the doc. Re-open every link and compare every quote with its source before delivery.

## Hard rules

- Never send real personal, account or proprietary data to an external service.
- Never create accounts on the user's behalf.
- Never recommend from a single source or call "documented" "tested".
- Never keep a quote not checked against its source, and never cite a link you have not opened.
- Never write raw web research into `reference/` or `explanation/`; it goes to the `investigations` key.

## Provenance and maintenance

Updated: 2026-11-26.

Re-verification commands:
```bash
test -f plugins/techdocs/skills/doc-templates/references/templates/research-doc.md
sh plugins/techdocs/skills/writing-style/scripts/lint-prose.sh plugins/techdocs/skills/external-research/SKILL.md
```
