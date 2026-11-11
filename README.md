# claude-plugin-marketplace

Personal **Claude Code plugin marketplace** by `diutsu`. Plugins bundle agent skills and are installable as Claude Code plugins or, skill by skill, via `npx skills`.

Repository: `https://github.com/diutsu/claude-plugin-marketplace`

---

## Repository Structure

```text
claude-plugin-marketplace/
├── .claude-plugin/
│   └── marketplace.json              # Marketplace catalog
├── plugins/
│   └── local-project-manager/        # Plugin: skills for managing local projects
│       ├── .claude-plugin/plugin.json
│       └── skills/                   # 19 skills (see below)
└── docs/                             # Meta-documentation for this repository itself
```

Skills in `local-project-manager`: `code-discipline`, `code-task`, `data-integrity`, `debugging-method`, `do-task`, `docs-management`, `external-research`, `handle-comments`, `internal-research`, `migrate-project-docs` (bundles `templates/`: starter `CLAUDE.md` + v2 `docs/` skeleton), `operate-and-diagnose`, `operator-instructions`, `progress-log`, `research-methodology`, `research-to-plan`, `skill-maintenance`, `ui-ux-discipline`, `validation-and-qa`, `write-docs`. The skills rely on the companion **`ctask`** task-registry CLI (own repository, runs via `uvx`).

---

## 0. Plugin Marketplace (Claude Code)

```bash
/plugin marketplace add diutsu/claude-plugin-marketplace
/plugin install local-project-manager@claude-plugin-marketplace
```

**Adding your own skills:**

- To extend an existing plugin: add `plugins/<plugin>/skills/<name>/SKILL.md` (auto-discovered).
- For a new plugin: create `plugins/<name>/` with `.claude-plugin/plugin.json` and `skills/`, then add an entry with `"source": "./plugins/<name>"` to `.claude-plugin/marketplace.json`.
- Commit, push, then run `/plugin marketplace update claude-plugin-marketplace`.

Validate locally with `claude plugin validate .`.

---

## 1. Installing Skills (`npx skills`)

Works with every skill in every plugin under `plugins/`. Install all 19 current skills (or individual skills) into any agent environment:

```bash
# Install all skills from GitHub
npx skills add https://github.com/diutsu/claude-plugin-marketplace

# Install a single skill
npx skills add https://github.com/diutsu/claude-plugin-marketplace --skill migrate-project-docs

# Install from a local clone
npx skills add /path/to/claude-plugin-marketplace
```

---

## 2. Running or Installing `ctask` (`uvx` / `uv`)

`ctask` ([`https://github.com/diutsu/ctask`](https://github.com/diutsu/ctask)) is the zero-dependency Python CLI over `<repo-root>/docs/tasks.md` and `<repo-root>/docs/done.md` (with automatic fallback to legacy uppercase `TASKS.md` / `DONE.md`). Runs natively on **Windows, macOS, and Linux**:

```bash
# Run directly from GitHub without installing
uvx --from git+https://github.com/diutsu/ctask ctask list

# Install globally onto PATH (recommended for daily agent & human use)
uv tool install git+https://github.com/diutsu/ctask

# Run from a local clone
uvx --from /path/to/ctask ctask validate
```

### `ctask` Subcommands

- `ctask list [--prio P] [--module M] [--blocked] [--unblocked] [--ids-only]` — list open tasks.
- `ctask show ID [ID ...]` — print task(s) verbatim (falls back to `docs/done.md`).
- `ctask search TEXT [--field goal|details|done|title|all] [--ids-only] [--include-done]` — search task text.
- `ctask blockers ID` / `ctask blocking ID` — inspect dependency chains.
- `ctask refs [--referencing PATH] [ID]` — list a task's file refs or find tasks referencing `PATH`.
- `ctask add --title T --prio P --module M [--goal G] [--details D] [--done-when W]` — add a new task with collision-safe auto-ID.
- `ctask edit ID [...]` — surgical in-place update of a single task's fields or prose sections.
- `ctask close ID` — move a task from `docs/tasks.md` to `docs/done.md` with `completed::` and `commits::` stamps.
- `ctask renumber OLD_ID NEW_ID` — rename an open task ID and update `blocked-by::` references.
- `ctask add-section "<name>" --after "<existing>"` / `ctask remove-section "<name>"` — manage `## <module>` sections.
- `ctask validate` — verify structural invariants across `docs/tasks.md` and `docs/done.md`.

---

## 3. Migrating an Existing Project or Bootstrapping a New One

### Option A — Migrate an Existing v1 Project (`Mode A: convert-existing`)

Split the migration into two passes so mechanical file moves are separated from prose cleanup:

1. **Pass 1 (Structural migration & root de-clutter):**
   In the target project, prompt the agent:
   > *"Run `/migrate-project-docs` (Mode A, Steps 1–5 & 7) to move `docs/` to the v2 subfolder structure (`requirements/`, `logic/`, `investigations/`, `plans/`), normalize all `docs/*.md` filenames to lowercase `kebab-case.md`, purge `executed-*.md`, and clean up the root control files."*
2. **Pass 2 (Incremental prose de-accretion, per module):**
   Prompt the agent one module at a time (or let `/do-task` apply it when touching a module):
   > *"Run `/migrate-project-docs` Step 6 on `docs/requirements/<module>.md` and `docs/logic/<module>-*.md` to strip dated patch narratives into timeless present-tense rules."*

### Option B — Bootstrap a Brand-New Project (`Mode B: stabilize-prototype`)

1. **Day 1 (`Stage A: prototype`):** Copy the starter skeleton from [`plugins/local-project-manager/skills/migrate-project-docs/templates/`](plugins/local-project-manager/skills/migrate-project-docs/templates) into your new project root:
   ```bash
   cp -rn plugins/local-project-manager/skills/migrate-project-docs/templates/* /path/to/your-project/
   ```
2. **Week 2 (`Stage B: structured`):** Once the prototype's module boundaries solidify, run `/migrate-project-docs` (`Mode B: stabilize-prototype`) to lock `docs/architecture.md`, generate `tests/test_architecture_boundaries.py`, and populate `docs/requirements/<module>.md`.
