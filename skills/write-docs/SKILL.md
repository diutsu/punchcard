---
name: write-docs
tier: leaf
description: >
  Prose house style (max 20 words per sentence, active voice, no
  nominalizations, no filler, backtick-quoted <placeholders>) plus structural
  templates for project documentation: README, API docs, ADRs, and Changelogs.
  Load when writing or editing prose in any doc under docs/ or README.md.
  Trigger phrases: "write the docs", "document this", "update the README",
  "draft an ADR", "document this endpoint", "update the changelog". Do NOT
  load for the YAML frontmatter contract, subfolder taxonomy, or timeless
  in-place edit rules (see docs-management), or for inline code comments (see
  code-discipline).
trigger: /write-docs
---

# /write-docs

Write technical documentation for an experienced developer who is **skimming, not studying**. Simplify the delivery; never simplify the technical accuracy.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| YAML frontmatter (`type`, `state`, `created`, `updated`, `cross-file-references`), subfolder layout, and anti-accretion rules | `docs-management` |
| Inline code comments and docstrings inside source files | `code-discipline` |
| Human CLI run queue and decision gates in `docs/operator-instructions.md` | `operator-instructions` |
| Single-line milestone entries in `docs/progress-log.md` | `progress-log` |

## 1. Prose house style

1. **Max 20 words per sentence.** One idea per sentence. Break compound sentences in two.
2. **Active voice only.** Say who or what performs the action (`storage rejects the write`, not `the write is rejected`).
3. **No nominalizations.** Use verbs, not nouns made from verbs (`configure` instead of `the configuration of`; `validate` instead of `performs validation of`).
4. **Zero filler phrases.** Cut `"in order to"`, `"it should be noted that"`, `"please be aware"`, `"basically"`, `"essentially"`.
5. **Backtick all angle-bracket placeholders in prose.** Always write `` `<date>` ``, `` `<ID>` ``, `` `<module>` ``, `` `<ticker>` `` — never bare `<date>` outside a fenced code block or YAML frontmatter.
   > **Guardrail:** CommonMark §6.8 parses bare `<ascii-word>` as literal raw HTML, rendering it invisible in Obsidian and Markdown viewers.

## 2. Document templates

For `docs/requirements/<module>.md`, `docs/logic/<module>-<concern>.md`, `docs/investigations/<slug>.md`, and `docs/plans/<id>-<slug>.md`, use the `_template.md` file inside each `docs/` subfolder (or `migrate-project-docs/templates/docs/`) and follow `docs-management`. Use the shapes below for `README.md`, API endpoints, ADRs, and external changelogs.

### (a) `README.md`
Target reader: a developer discovering the repo or getting it running for the first time.
```markdown
# <Project Name>
<2-3 sentence plain-English description of what the project does.>

## Stack & key dependencies
- **Language / runtime:** `<e.g. Python 3.12 / Node 22>`
- **Core dependencies:** `<list>`

## Quickstart
- **Install:** `<command>`
- **Run / entry point:** `<command>`
- **Verify (test + lint + typecheck):** `<command>`

## Documentation map
See [`CLAUDE.md`](CLAUDE.md) and [`docs/architecture.md`](docs/architecture.md).
```

### (b) API endpoint spec
Target reader: a developer integrating the endpoint for the first time.
```markdown
### `<HTTP METHOD> <path>`
<One-sentence description of what the endpoint does.>

- **Auth:** `<e.g. Bearer token in Authorization header | none>`
- **Request parameters / body:** `<schema or table of fields, types, required/optional>`
- **Response schema:** `<status code + payload schema>`
- **Error codes:**
  - `<4xx/5xx>`: `<plain-English cause>`
```

### (c) Architecture Decision Record (ADR / `docs/investigations/<slug>.md`)
```markdown
# Decision: <Short imperative phrase — e.g. Use DuckDB for derived tables>

- **Status:** `<Proposed | Accepted | Deprecated | Superseded>`
- **Context:** `<What situation or constraint forced a decision? (3-5 sentences)>`
- **Decision:** `<What did we decide? (1-2 direct sentences)>`
- **Alternatives considered:**
  - `<Option A>` — rejected because `<reason>`.
  - `<Option B>` — rejected because `<reason>`.
- **Consequences:** `<What becomes easier, what becomes harder, and what new risks exist.>`
- **Revisit trigger:** `<Specific measurable condition that would cause us to reconsider.>`
```

### (d) Release Changelog (for versioned packages/releases only)
Follow [Keep a Changelog](https://keepachangelog.com/) and SemVer when a project ships versioned releases (newest version first, grouped under `Added`, `Changed`, `Deprecated`, `Removed`, `Fixed`, `Security`). Do **not** put changelogs inside `docs/requirements/` or `docs/logic/`.

## Hard rules

- Never exceed 20 words in a prose sentence when a shorter sentence carries the same precision.
- Never use passive voice, nominalizations, or throat-clearing filler phrases.
- Never leave a bare `<placeholder>` unquoted in prose outside code fences or YAML frontmatter — wrap it in backticks (`` `<placeholder>` ``).
- Never use the ADR `Context / Decision / Alternatives` template inside `docs/requirements/` or `docs/logic/` — put trade-off history in `docs/investigations/<slug>.md` and state only timeless current behavior in `requirements/` and `logic/` (per `docs-management`).

## Provenance and maintenance

Updated: 2026-10-11 (merged README, API Doc, and Changelog templates from retired `code-task/references/Comments.md`; aligned with `docs-management` v2).

Re-verification commands:
```bash
grep -rL '^type:' docs/
```
