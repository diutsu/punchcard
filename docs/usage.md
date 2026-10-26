---
type: requirement
state: done
created: 2026-10-11
updated: 2026-10-26
cross-file-references: [docs/architecture.md, docs/operator-instructions.md, README.md]
---
# Usage — Frank
Commands for installing skills from `Frank`, running `ctask` via `uvx`, bootstrapping side-project documentation, and running validation checks.

## TOC
- [Installing skills via `npx skills`](#installing-skills-via-npx-skills)
- [Running & installing `ctask` via `uvx` / `uv`](#running--installing-ctask-via-uvx--uv)
- [Bootstrapping or migrating a project](#bootstrapping-or-migrating-a-project)
- [Validating `Frank`](#validating-frank)

---

## Installing skills via `npx skills`

```bash
# Install all skills from GitHub
npx skills add https://github.com/diutsu/Frank

# Install a single skill
npx skills add https://github.com/diutsu/Frank --skill docs-management

# Install from local checkout
npx skills add /path/to/Frank
```

---

## Running & installing `ctask` via `uvx` / `uv`

```bash
# Run directly from GitHub without installing
uvx --from git+https://github.com/diutsu/ctask ctask list

# Install globally onto PATH (Windows / macOS / Linux)
uv tool install git+https://github.com/diutsu/ctask
ctask validate
```

---

## Bootstrapping or migrating a project

```bash
# Copy starter CLAUDE.md and v2 docs/ skeleton into a new repository
cp -rn skills/migrate-project-docs/templates/* /path/to/target-repo/
```

Or invoke `/migrate-project-docs` inside the target repository (`Mode A: convert-existing` or `Mode B: stabilize-prototype`).

---

## Validating `Frank`

```bash
# 1. Validate Frank's own task registry
ctask validate

# 2. Verify all docs in docs/ and skills/migrate-project-docs/templates/docs/ have frontmatter
grep -rL '^type:' docs/ skills/migrate-project-docs/templates/docs/

# 3. Verify all skills have required frontmatter fields
grep -L '^name:' skills/*/SKILL.md
grep -L '^tier:' skills/*/SKILL.md
```
