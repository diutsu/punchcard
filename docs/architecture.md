---
type: requirement
state: done
created: 2026-10-11
updated: 2026-10-26
cross-file-references: [docs/tasks.md, docs/usage.md, docs/requirements/_index.md, docs/logic/_index.md, CLAUDE.md, README.md]
---
# Architecture — punchcard
High-level architecture of the `punchcard` repository (`https://github.com/diutsu/punchcard`): the distributable `plugins/local-project-manager/skills/` catalog, the `plugins/local-project-manager/skills/migrate-project-docs/templates/` starter tree, and the `docs/` meta-documentation.

## TOC
- [Module map](#module-map)
- [Module responsibilities](#module-responsibilities)
- [Allowed dependencies](#allowed-dependencies)
- [Skill tier & packaging rules](#skill-tier--packaging-rules)
- [Documentation rules](#documentation-rules)

---

## Module map

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                     https://github.com/diutsu/punchcard                          │
└──────────────────────────────────────────────────────────────────────────────┘
          │                                  │                              │
          ▼                                  ▼                              ▼
┌───────────────────────────┐  ┌───────────────────────────┐  ┌────────────────────────┐
│          plugins/local-project-manager/skills/          │  │   migrate-project-docs/   │  │         docs/          │
│                           │  │       └─ templates/       │  │                        │
│  npx skills package root  │  │  downstream repo starter  │  │  meta-docs for punchcard   │
│  plugins/local-project-manager/skills/<name>/SKILL.md   │  │  CLAUDE.md + v2 docs/     │  │  tracks punchcard's work   │
└───────────────────────────┘  └───────────────────────────┘  └────────────────────────┘
```

---

## Module responsibilities

### `skills` (`plugins/local-project-manager/skills/<name>/SKILL.md`)
Distributable library of process, workflow, and reference skills for AI coding agents.

- Discoverable directly by `npx skills add https://github.com/diutsu/punchcard`.
- Each skill lives in `plugins/local-project-manager/skills/<name>/SKILL.md` with optional `flows/` or `references/` subdirectories.
- Self-contained and project-agnostic: skills teach discovery methods and contracts, never hardcoded paths to one consumer project.

### `doc-templates` (`plugins/local-project-manager/skills/migrate-project-docs/templates/`)
Canonical v2 documentation skeleton for side projects.

- Contains `plugins/local-project-manager/skills/migrate-project-docs/templates/CLAUDE.md` and `plugins/local-project-manager/skills/migrate-project-docs/templates/docs/` (`tasks.md`, `done.md`, `next-session-prompt.md`, `operator-instructions.md`, `architecture.md`, `usage.md`, `progress-log.md`, and `requirements/`, `logic/`, `investigations/`, `plans/`).
- Consumed when bootstrapping a new project or running `/migrate-project-docs`.

### `docs` (`docs/`)
Meta-documentation for `punchcard` itself, dogfooding the exact v2 documentation contract defined in `plugins/local-project-manager/skills/migrate-project-docs/templates/`.

---

## Allowed dependencies

```
plugins/local-project-manager/skills/migrate-project-docs  ──►  plugins/local-project-manager/skills/migrate-project-docs/templates/ (template shapes)
plugins/local-project-manager/skills/ (workflow tier)      ──►  plugins/local-project-manager/skills/ (leaf & reference tiers, by name only)
plugins/local-project-manager/skills/ (leaf tier)          ──►  plugins/local-project-manager/skills/ (reference tier only)
plugins/local-project-manager/skills/migrate-project-docs/templates/  ──►  (zero dependencies; standalone starter files)
```

Rules:
- **One fact, one home across `plugins/local-project-manager/skills/`:** A `workflow` skill composes `leaf` skills by name and never restates their mechanics.
- **Template parity:** `plugins/local-project-manager/skills/migrate-project-docs/templates/` must always pass the validation rules stated in `plugins/local-project-manager/skills/docs-management/SKILL.md` and `plugins/local-project-manager/skills/operator-instructions/SKILL.md`.

---

## Skill tier & packaging rules

Every skill in `plugins/local-project-manager/skills/<name>/SKILL.md` declares a `tier` field in YAML frontmatter:

| Tier | Role | Rules |
|---|---|---|
| `leaf` | Executes one intent's mechanics (`docs-management`, `operator-instructions`, `progress-log`, `research-to-plan`) | Never orchestrates multi-agent gates; never restates sibling leaves. |
| `workflow` | Composes leaves and agents across steps (`do-task`, `do-flow`, `migrate-project-docs`) | Owns sequence, gates, and routing; delegates mechanics to leaf skills. |
| `reference` | Domain cheat sheets (`finance-reference`, `ui-ux-discipline`) | Consulted during planning/coding; never stepped through as a workflow. |

---

## Documentation rules

`punchcard`'s own `docs/` directory follows the v2 documentation contract defined in [`plugins/local-project-manager/skills/docs-management/SKILL.md`](../plugins/local-project-manager/skills/docs-management/SKILL.md).
