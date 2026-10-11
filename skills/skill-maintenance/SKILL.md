---
name: skill-maintenance
tier: leaf
description: >
  The meta-skill governing how the Frank skill library (skills/*/SKILL.md) and
  doc-templates/ are organized, extended, and kept drift-free. Load when
  authoring a new skill, editing an existing SKILL.md, auditing skills/ for
  overlap or stale paths, or deciding whether a rule belongs in CLAUDE.md, a
  skill, or a project's docs/. Trigger on /skill-maintenance, "add a skill for
  X", "audit the skills", "split/merge these skills". Do NOT load when simply
  executing a task governed by another skill — load that skill directly.
trigger: /skill-maintenance
---

# /skill-maintenance

This library (`https://github.com/diutsu/Frank`, under `skills/`) is a cohesive system of **process, workflow, and reference skills** distributed via `npx skills`. Every skill must earn its context budget: one fact lives in one home, siblings cross-reference by name without restating mechanics, and project-specific facts stay out of global skills.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Executing a task end-to-end | `do-task` |
| Validating or migrating a project's `docs/` folder | `docs-management` / `migrate-project-docs` |
| Writing project documentation prose | `write-docs` |

## 1. The four layers (decide placement before writing)

| Layer | Home | What belongs there |
|---|---|---|
| **Always-on conduct** | Global `~/.claude/CLAUDE.md` + repo `CLAUDE.md` | Non-negotiables, gate commands, lifecycle stage (`prototype` vs `structured`). Loaded every turn. |
| **Workflow & leaf skills** | `Frank/skills/<name>/SKILL.md` | Triggered procedures (`do-task`, `debugging-method`, `docs-management`, `operator-instructions`, `migrate-project-docs`, etc.). Project-agnostic. |
| **Reference guides** | `Frank/skills/<name>/SKILL.md` (`tier: reference`) | Consulted cheat sheets (`code-discipline`, `validation-and-qa`, `data-integrity`, `research-methodology`, `ui-ux-discipline`). |
| **Project facts** | Each repo's `CLAUDE.md` + `docs/` (scaffolded from `doc-templates/`) | Module map (`architecture.md`), behavioral contracts (`docs/requirements/`), domain formulas (`docs/logic/`), spikes (`docs/investigations/`), open backlog (`tasks.md`). |

## 2. Canonical `Frank/skills/` inventory (one fact, one home)

| Skill | Tier | Territory |
|---|---|---|
| `do-task` | `workflow` | Plan $\rightarrow$ gate $\rightarrow$ sequential execute $\rightarrow$ gate $\rightarrow$ in-place doc update $\rightarrow$ `ctask close` workflow. |
| `migrate-project-docs` | `workflow` | Convert flat legacy `docs/` to v2 subfolders (`Mode A`) OR promote a prototype to structured docs (`Mode B`). |
| `code-task` | `leaf` | Sub-agent step execution protocol and structured handoff report. |
| `code-discipline` | `reference` | Anti-slop code quality, module/SDK boundary checks, fail-fast rules, and "explain why, not what" code comments. |
| `docs-management` | `leaf` | v2 YAML frontmatter contract, subfolder taxonomy (`requirements/`, `logic/`, `investigations/`, `plans/`), line ceilings, and anti-accretion rules. |
| `write-docs` | `leaf` | Prose style (max 20 words, active voice, no nominalizations, backtick-quoted `` `<placeholders>` ``) + README, API, ADR, and Changelog shapes. |
| `operator-instructions` | `leaf` | Managing `docs/operator-instructions.md` (`## Run queue` + `## Decision gates`) and enforcing the Binary Exit Rule on blocked tasks. |
| `handle-comments` | `leaf` | Processing inline `[COMMENT]` markers and routing unresolved questions into `docs/operator-instructions.md` (`## Decision gates`). |
| `progress-log` | `leaf` | Appending $\le 250$-char milestone highlights to `docs/progress-log.md`. |
| `research-to-plan` | `leaf` | Turning research findings into a $\le 150$-line execution plan at `docs/plans/<id>-<slug>.md` with phase roll-forward. |
| `internal-research` | `leaf` | Mining a repo's own `docs/`, `ctask`, git history, and code; `FRESH`/`STALE`/`CONTRADICTED`/`WIN` drift detection. |
| `external-research` | `leaf` | Evaluating external libraries/APIs/data sources under the privacy wall; outputs to `docs/investigations/<slug>.md`. |
| `debugging-method` | `leaf` | Bug reproduction, failure-ledger check (`ctask`, `done.md`, `investigations/`), hypothesis-predicts-numbers table, root-cause bar. |
| `operate-and-diagnose` | `leaf` | Querying/measuring live services, checking trigger layers (systemd/queue/cron), 2-channel logging, `SIGINT`/`SIGTERM` handling. |
| `validation-and-qa` | `reference` | Gate command = DoD, `_stub_` flagging rules, invariant testing, and sub-agent verification. |
| `data-integrity` | `reference` | `RAW` vs. `DERIVED` vs. `CACHE` store classification, atomic migrations, wipe+recompute derived, standalone reconciliation audits. |
| `research-methodology` | `reference` | Hypothesis-predicts-numbers bar, yardstick-first validation, adversarial refutation, regime honesty, null-result exit discipline. |
| `ui-ux-discipline` | `reference` | 5 honest UI states, no swallowed fetch errors, no fabricated values, read-only default, anti-view-sprawl. |
| `skill-maintenance` | `leaf` | This meta-skill. |

## 3. Required skill anatomy

Every `skills/<name>/SKILL.md` ships all five sections:
1. **YAML Frontmatter:** `name` (matching directory), `tier` (`leaf | workflow | reference`), trigger-rich `description` (stating both when to load and when NOT to load), and `trigger: /<name>`.
2. **`## When NOT to use this skill` table** naming the sibling skill that owns adjacent territory.
3. **Imperative runbook body** using tables, numbered steps, and backtick-quoted `` `<placeholders>` `` in prose.
4. **`## Hard rules` section** closing the body with flat imperatives.
5. **`## Provenance and maintenance` section** with date stamp and runnable verification commands.

## 4. Split / merge / retire heuristics

- **Split** when a skill's description requires two unrelated trigger families or mixes workflow/execution mechanics with reference standards (as when `code-discipline` and `write-docs` templates were split out of `code-task`).
- **Merge** when a skill shrinks to a single paragraph that fits cleanly inside a sibling.
- **Sync with `doc-templates/`:** Whenever a documentation rule changes in `docs-management` or `operator-instructions`, update `doc-templates/` in the same pass.

## Hard rules

- One fact, one home — never restate another skill's mechanics; cross-reference it by name.
- Every `skills/<name>/SKILL.md` must include `name`, `tier`, `description`, `trigger`, `When NOT to use`, `Hard rules`, and `Provenance and maintenance`.
- Never embed unquoted `<placeholder>` angle brackets in prose outside code fences or YAML frontmatter.
- Never reference retired `executed-*.md` files or root-level `REQUIREMENTS-*` / `BUSINESS_LOGIC-*` / `plan-*` paths — use the v2 subfolder contract (`docs/{requirements,logic,investigations,plans}/`).
- Keep `doc-templates/` and `Frank/docs/` 100% compliant with `docs-management` at all times.

## Provenance and maintenance

Updated: 2026-10-11 (v2 library consolidated in `Frank/skills/`).

Re-verification commands:
```bash
# 1. Confirm all skills have name and tier frontmatter
grep -L '^name:' skills/*/SKILL.md
grep -L '^tier:' skills/*/SKILL.md

# 2. Confirm zero stray references to retired executed-*.md outside migration/ban rules
grep -rn 'executed-' skills/ | grep -v -E '(docs-management|migrate-project-docs|do-task|skill-maintenance)'

# 3. Confirm all docs in Frank/docs/ and Frank/doc-templates/docs/ have valid frontmatter
grep -rL '^type:' docs/ doc-templates/docs/
```
