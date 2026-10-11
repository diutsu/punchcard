---
type: requirement
state: done
created: 2026-10-11
updated: 2026-10-11
cross-file-references: [docs/architecture.md, docs/operator-instructions.md, README.md]
---
# Usage — Frank
How to install skills from `https://github.com/diutsu/Frank`, scaffold or migrate downstream projects with `doc-templates/`, and validate the repository.

## TOC
- [Installing skills via npx](#installing-skills-via-npx)
- [Bootstrapping or migrating a project](#bootstrapping-or-migrating-a-project)
- [Linting & validating Frank](#linting--validating-frank)

---

## Installing skills via npx

Install skills into any environment from GitHub:

```bash
# Install all skills in skills/
npx skills add https://github.com/diutsu/Frank

# Install a single skill
npx skills add https://github.com/diutsu/Frank --skill docs-management
```

---

## Bootstrapping or migrating a project

| Scenario | Command / Procedure |
|---|---|
| **New side project (Stage A: prototype)** | Copy `doc-templates/CLAUDE.md`, `doc-templates/docs/tasks.md`, `doc-templates/docs/done.md`, `doc-templates/docs/next-session-prompt.md`, and `doc-templates/docs/architecture.md` into the new repo. |
| **Promote prototype to structured (Stage B)** | Run `/migrate-project-docs` (`Mode B: stabilize-prototype`) to lock `architecture.md`, generate boundary tests, and scaffold `docs/{requirements,logic,investigations,plans}/`. |
| **Convert legacy flat `docs/` project (e.g. `repit`)** | Run `/migrate-project-docs` (`Mode A: convert-existing`) to move `REQUIREMENTS-*` and `BUSINESS_LOGIC-*` into subfolders, purge `executed-*.md`, roll forward `plan-*.md`, and clean `operator-instructions.md`. |

---

## Linting & validating Frank

```bash
# Check skill frontmatter completeness
grep -L '^name:' skills/*/SKILL.md
grep -L '^tier:' skills/*/SKILL.md

# Check v2 doc frontmatter across meta-docs and templates
grep -rL '^type:' docs/ doc-templates/docs/

# Validate Frank's task registry
ctask validate
```
