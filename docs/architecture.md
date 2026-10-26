---
type: requirement
state: done
created: 2026-10-11
updated: 2026-10-26
cross-file-references: [docs/tasks.md, docs/usage.md, docs/requirements/_index.md, docs/logic/_index.md, CLAUDE.md, README.md]
---
# Architecture — Frank
High-level architecture of the `Frank` repository (`https://github.com/diutsu/Frank`): the distributable `skills/` catalog, the `skills/migrate-project-docs/templates/` starter tree, and the `docs/` meta-documentation.

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
│                     https://github.com/diutsu/Frank                          │
└──────────────────────────────────────────────────────────────────────────────┘
          │                                  │                              │
          ▼                                  ▼                              ▼
┌───────────────────────────┐  ┌───────────────────────────┐  ┌────────────────────────┐
│          skills/          │  │   migrate-project-docs/   │  │         docs/          │
│                           │  │       └─ templates/       │  │                        │
│  npx skills package root  │  │  downstream repo starter  │  │  meta-docs for Frank   │
│  skills/<name>/SKILL.md   │  │  CLAUDE.md + v2 docs/     │  │  tracks Frank's work   │
└───────────────────────────┘  └───────────────────────────┘  └────────────────────────┘
```

---

## Module responsibilities

### `skills` (`skills/<name>/SKILL.md`)
Distributable library of process, workflow, and reference skills for AI coding agents.

- Discoverable directly by `npx skills add https://github.com/diutsu/Frank`.
- Each skill lives in `skills/<name>/SKILL.md` with optional `flows/` or `references/` subdirectories.
- Self-contained and project-agnostic: skills teach discovery methods and contracts, never hardcoded paths to one consumer project.

### `doc-templates` (`skills/migrate-project-docs/templates/`)
Canonical v2 documentation skeleton for side projects.

- Contains `skills/migrate-project-docs/templates/CLAUDE.md` and `skills/migrate-project-docs/templates/docs/` (`tasks.md`, `done.md`, `next-session-prompt.md`, `operator-instructions.md`, `architecture.md`, `usage.md`, `progress-log.md`, and `requirements/`, `logic/`, `investigations/`, `plans/`).
- Consumed when bootstrapping a new project or running `/migrate-project-docs`.

### `docs` (`docs/`)
Meta-documentation for `Frank` itself, dogfooding the exact v2 documentation contract defined in `skills/migrate-project-docs/templates/`.

---

## Allowed dependencies

```
skills/migrate-project-docs  ──►  skills/migrate-project-docs/templates/ (template shapes)
skills/ (workflow tier)      ──►  skills/ (leaf & reference tiers, by name only)
skills/ (leaf tier)          ──►  skills/ (reference tier only)
skills/migrate-project-docs/templates/  ──►  (zero dependencies; standalone starter files)
```

Rules:
- **One fact, one home across `skills/`:** A `workflow` skill composes `leaf` skills by name and never restates their mechanics.
- **Template parity:** `skills/migrate-project-docs/templates/` must always pass the validation rules stated in `skills/docs-management/SKILL.md` and `skills/operator-instructions/SKILL.md`.

---

## Skill tier & packaging rules

Every skill in `skills/<name>/SKILL.md` declares a `tier` field in YAML frontmatter:

| Tier | Role | Rules |
|---|---|---|
| `leaf` | Executes one intent's mechanics (`docs-management`, `operator-instructions`, `progress-log`, `research-to-plan`) | Never orchestrates multi-agent gates; never restates sibling leaves. |
| `workflow` | Composes leaves and agents across steps (`do-task`, `do-flow`, `migrate-project-docs`) | Owns sequence, gates, and routing; delegates mechanics to leaf skills. |
| `reference` | Domain cheat sheets (`finance-reference`, `ui-ux-discipline`) | Consulted during planning/coding; never stepped through as a workflow. |

---

## Documentation rules

`Frank`'s own `docs/` directory follows the v2 documentation contract defined in [`skills/docs-management/SKILL.md`](../skills/docs-management/SKILL.md).
