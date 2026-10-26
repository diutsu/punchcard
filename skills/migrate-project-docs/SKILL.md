---
name: migrate-project-docs
tier: workflow
description: >
  Migrate or bootstrap a project's docs/ directory to the v2 subfolder
  documentation framework. Supports two modes: (Mode A: convert-existing)
  converting a flat legacy docs/ tree (REQUIREMENTS-*, BUSINESS_LOGIC-*,
  plan-*, executed-*, investigation-*, and bloated operator-instructions.md)
  into docs/{requirements,logic,plans,investigations}/ while purging
  executed-*.md, collapsing multi-phase plans, and stripping historical patch
  accretion; and (Mode B: stabilize-prototype) promoting a Day-1 prototype
  into structured docs with architecture.md, module boundary tests, and initial
  requirement contracts. Trigger on /migrate-project-docs, "convert existing
  docs", "migrate docs to v2", or "stabilize prototype docs". Do NOT load for
  routine single-doc frontmatter edits (see docs-management).
trigger: /migrate-project-docs
---

# /migrate-project-docs

Transition a project into the v2 documentation layout (`docs/{requirements,logic,plans,investigations}/`) either from a **legacy flat `docs/` directory** (Mode A) or from an **early prototype** (Mode B).

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Validating or bumping frontmatter on a single doc during normal work | `docs-management` |
| Writing a new feature requirement or ADR from scratch | `write-docs` |
| Executing a regular backlog task | `do-task` |

---

## Mode A — Convert an existing flat `docs/` directory (`convert-existing`)

Use when migrating an established repo (e.g., with root-level `REQUIREMENTS-*.md`, `BUSINESS_LOGIC-*.md`, `plan-*.md`, `executed-*.md`, `investigation-*.md`) to the v2 subfolder contract.

### Step 1 — Inventory & safety snapshot
1. Confirm the working tree is clean (`git status --short` on both the repo and the docs directory/vault).
2. List all files in `docs/` and classify them by prefix:
   ```bash
   ls -la docs/
   ```

### Step 2 — Create subfolders, normalize root filenames to `kebab-case.md`, & move canonical files
1. Create the four target directories:
   ```bash
   mkdir -p docs/requirements docs/logic docs/investigations docs/plans
   ```
2. **Normalize root filenames to lowercase `kebab-case.md`:**
   - Rename `docs/ARCHITECTURE.md` $\rightarrow$ `docs/architecture.md`, `docs/USAGE.md` $\rightarrow$ `docs/usage.md`, `docs/TASKS.md` $\rightarrow$ `docs/tasks.md`, `docs/DONE.md` $\rightarrow$ `docs/done.md`, and `docs/PROGRESS_LOG.md` $\rightarrow$ `docs/progress-log.md`.
3. **Requirements (`REQUIREMENTS-*` $\rightarrow$ `docs/requirements/`):**
   - Move `docs/REQUIREMENTS-index.md` $\rightarrow$ `docs/requirements/_index.md`.
   - Move each `docs/REQUIREMENTS-<module>.md` $\rightarrow$ `docs/requirements/<module>.md` (all lowercase `kebab-case.md`).
4. **Business Logic vs. Evaluations (`BUSINESS_LOGIC-*` $\rightarrow$ `docs/logic/` or `docs/investigations/`):**
   - Move `docs/BUSINESS_LOGIC-index.md` $\rightarrow$ `docs/logic/_index.md`.
   - Inspect each `docs/BUSINESS_LOGIC-<slug>.md`:
     - If `state: archived` or it is a one-off library/tool evaluation (e.g., `BUSINESS_LOGIC-meta-vectorbt-eval.md`), set `type: investigation` and move it to `docs/investigations/<slug>.md`.
     - Otherwise, move `docs/BUSINESS_LOGIC-<module>-<concern>.md` $\rightarrow$ `docs/logic/<module>-<concern>.md`.
5. **Investigations (`investigation-*` & `project-review/*` $\rightarrow$ `docs/investigations/`):**
   - Move `docs/investigation-<slug>.md` $\rightarrow$ `docs/investigations/<slug>.md`.
   - Ensure each file in `docs/investigations/` has a top `## Verdict & promoted rules` section ($\le 10$ lines).

### Step 3 — Purge `executed-*.md` files
For every `docs/executed-<slug>.md` file:
1. Check its `cross-file-references` and verify its durable behavioral or formula changes are already present in the corresponding `docs/requirements/<module>.md` or `docs/logic/<module>-<concern>.md`.
2. If a durable fact from `executed-<slug>.md` was never folded into `requirements/` or `logic/`, fold that fact in place now (timeless present tense, no dates or run logs).
3. Delete `docs/executed-<slug>.md` and remove any references to it from `cross-file-references` across remaining docs.

### Step 4 — Audit, prune, and roll forward `plan-*.md` files
For every `docs/plan-<slug>.md` file:
1. Check whether the task ID(s) it covers are already closed in `docs/done.md` (via `ctask show <ID>`).
   - **If all covered tasks are closed:** Delete `docs/plan-<slug>.md`.
   - **If the task is still open in `docs/tasks.md`:**
     1. Move the file to `docs/plans/<id>-<slug>.md`.
     2. Apply the **Phase Roll-Forward Rule** (`docs-management` §3.D): collapse every already-landed phase into a single line (`- [x] Phase N: <1-line summary> (<commit-hash>)`), strip multi-paragraph `Scope decisions` essays (moving any durable findings to `docs/investigations/`), and bring the file under the **150-line ceiling**.

### Step 5 — De-bloat `operator-instructions.md` and `next-session-prompt.md`
1. In `docs/operator-instructions.md`:
   - Move any permanent how-to sections (e.g., "Preferred pattern: schedule via the queue", "How to stop and resume long-running jobs") into `docs/usage.md`.
   - Convert multi-paragraph null-result or threshold-failure essays into $\le 6$-line `### [DECISION] <TASK-ID>` blocks under `## Decision gates` (per `operator-instructions` skill).
   - Keep only unexecuted literal commands under `## Run queue`. Delete all completed `[x]` history.
2. In `docs/next-session-prompt.md`:
   - Strip duplicated queue dumps and history paragraphs so the file is $\le 40$ lines (`Live state` + `Blocked on operator-instructions.md` pointers + `Unfiled observations`).

### Step 6 — Strip historical accretion from `requirements/` and `logic/`
Scan `docs/requirements/*.md` and `docs/logic/*.md` for historical patch accretion:
```bash
grep -rn -E '(\*\*Problem\.\*\*|\*\*Fix\.\*\*|Confirmed on 20|Verified on 20|canonical decision \(20)' docs/requirements/ docs/logic/
```
For each hit:
1. Rewrite the rule or formula in place as timeless present-tense truth.
2. If the rejected alternative or subtle constraint must be remembered so future agents do not undo it, replace the multi-paragraph history with a 1-line `> **Guardrail:**` note pointing to `docs/investigations/<slug>.md`.

### Step 7 — Rewrite links & validate
1. Update relative links and `cross-file-references` across `docs/` to reflect `docs/requirements/`, `docs/logic/`, `docs/investigations/`, and `docs/plans/`.
2. Update `docs/architecture.md` ("Documentation rules" section) to match the v2 subfolder contract.
3. Run `ctask validate` and the `docs-management` validation suite.

---

## Mode B — Promote a prototype to structured docs (`stabilize-prototype`)

Use when a new side project starts in `Stage A: prototype` (with only `CLAUDE.md`, `tasks.md`, `next-session-prompt.md`, and a rough `architecture.md`) and is ready to lock module boundaries and enforce structured docs.

1. **Discover actual modules:** Scan `src/` (or the repo's top-level source packages) and map every top-level module, its public entry points, and its third-party SDK imports.
2. **Lock `docs/architecture.md`:** Fill `Module map`, `Module responsibilities`, and `Allowed dependencies` from the discovered modules.
3. **Create an automated boundary test (`tests/test_architecture_boundaries.py` or equivalent):** Write a fast static/AST import test asserting that no module imports forbidden siblings or leaks third-party SDKs outside their owning module. Wire it into the project's verification gate command.
4. **Scaffold `docs/{requirements,logic,investigations,plans}/`:**
   - Copy `_index.md` and `_template.md` from `./templates/docs/` bundled inside this skill's directory (next to this `SKILL.md`), or write them using the `docs-management` frontmatter contract. Never search outside the active project workspace or this skill directory.
   - Generate a concise initial `docs/requirements/<module>.md` ($\le 150$ lines) for each core module documenting its current inputs, outputs, and invariants.
5. **Flip stage:** Change `Lifecycle stage: prototype` to `Lifecycle stage: structured` in `CLAUDE.md` and run `ctask validate`.

---

## Hard rules

- Never read or search outside the active project workspace (except reading `./templates/` bundled inside this skill's own directory when scaffolding new files).
- Never delete an `executed-*.md` or `plan-*.md` file without first verifying its durable behavior is recorded in `docs/requirements/` or `docs/logic/` (or its task is still open, for plans).
- Never leave broken relative links or dangling `cross-file-references` after moving files into subfolders.
- Never move `tasks.md`, `done.md`, `next-session-prompt.md`, `operator-instructions.md`, `architecture.md`, `usage.md`, or `progress-log.md` out of the `docs/` root.
- Always run `ctask validate` and `grep -rL '^type:' docs/` before concluding a migration.

## Provenance and maintenance

Authored: 2026-10-11.

Re-verification commands:
```bash
ls -d docs/requirements docs/logic docs/investigations docs/plans
grep -rL '^type:' docs/
```
