---
name: do-task
tier: workflow
description: >
  Canonical workflow for executing a project task end-to-end (v2 subfolder
  contract): scope, plan into docs/plans/<id>-<slug>.md (capped at 150 lines
  with phase roll-forward), score-gate the plan, execute across sequential
  agents, score-gate the implementation, run tests, update docs/requirements/
  and docs/logic/ in place, delete the plan file, close via ctask, commit and
  push. Trigger when the user asks to "do", "execute", or "implement" one or
  more tasks (tasks.md IDs) with quality gates.
trigger: /do-task
---

# /do-task

Drive a task to completion through two quality gates: a **plan gate** and an **implementation gate**, each scored by a separate `fresh-reviewer` agent. This v2 workflow uses the subfolder doc layout (`docs/plans/`, `docs/requirements/`, `docs/logic/`), enforces the **150-line plan cap + phase roll-forward**, and **eliminates `executed-<slug>.md` artifacts**.

## When NOT to use this skill

- **A trivial one-off edit** too small to justify a reviewer — do it directly or dispatch one `code-task` brief.
- **No executable finding yet** (still debugging or researching) — use `debugging-method`, `external-research`, or `internal-research` first, then `research-to-plan`.
- **Doc-only work** — use `write-docs`, `docs-management`, or `migrate-project-docs`.
- **Operating or measuring a live system** — use `operate-and-diagnose`.

## Cost discipline

- **Plan inline only when you have earned it** (Opus-class orchestrator with solid context); otherwise escalate per step 2.
- **Artifacts live in files, not prompts.** Write the plan to `docs/plans/<id>-<slug>.md` ($\le 150$ lines) before review. Pass file paths, never pasted file contents.
- **Each executor sees only its step** (step text, acceptance criteria, test command, previous handoff, and plan path for reference).
- **Reuse the `fresh-reviewer` agent** across plan re-reviews and the implementation gate via `send_message`.
- **Delegate full suite runs** to `suite-runner` (haiku) at baseline (step 0) and post-execution (step 5). Executors run only the tests targeting their change.
- **One `doc-writer` call** performs all end-of-task doc updates in a single batch.

## The task registry — read and write exclusively through `ctask`

Never read `docs/tasks.md` raw when `ctask` can answer the query, and never hand-edit `docs/tasks.md` or `docs/done.md`:

```bash
ctask list --prio high
ctask show <ID>
ctask search "<keyword>"
ctask blockers <ID>
ctask blocking <ID>
ctask edit <ID> --clear-blocked-by
ctask close <ID>                        # moves task to docs/done.md & reports stale blocked-by::
ctask validate
```

## Workflow

0. **Baseline.** Spawn `suite-runner` with the project's verification gate commands; record pass/fail counts and commit hash. If red, report to the user before proceeding.
1. **Scope.** Find affected files, mock seams (`monkeypatch.setattr`/`patch(`), and discrepancies between code, `docs/requirements/<module>.md`, `docs/logic/<module>-<concern>.md`, and `docs/tasks.md`. Resolve staleness (1 line per resolution in the plan's `Scope decisions` section; if genuinely ambiguous, stop and ask the user).
2. **Plan ($\le 150$ lines).** Produce a concrete, ordered execution plan in `docs/plans/<id>-<slug>.md` (template in `research-to-plan`).
   - **Multi-phase tasks (Phase Roll-Forward Rule):** Never write step-by-step details for 5 future phases into a 6,000-line file. Detail **only the current active phase**; list future phases as 1-line stubs, and collapse any already-landed phase into `- [x] Phase N: <1-line summary> (<commit-hash>)`.
3. **Plan gate.** Spawn `fresh-reviewer` with the plan path, task ID, and relevant `docs/requirements/` or `docs/architecture.md` paths. Pass at $\ge 9$ (max 3 iterations).
4. **Execute.** Run `sonnet-executor` agents **sequentially** on the current branch. Each step runs its targeted tests and commits (`wip(<slug>): step N — <summary>`).
   - **Plan invalidation:** If an executor hits a false assumption, it stops immediately and returns to step 2.
   - **Operator / Decision Gate block (Binary Exit Rule):** If execution reaches a step that only the human operator can run (e.g. remote production/Mimir run) or produces a null/ambiguous experimental result requiring a scope judgment call, write the entry into `docs/operator-instructions.md` (`## Run queue` or `## Decision gates` per the `operator-instructions` skill), set `ctask edit <ID> --blocked-by "operator-instructions#<ID>"`, roll forward any landed phases in `docs/plans/<id>-<slug>.md`, and **stop working on `<ID>` immediately**.
5. **Post-execution suite verify.** Spawn `suite-runner` with the full verification gate and compare against baseline.
6. **Implementation gate.** Send the git diff range, acceptance criteria, and `suite-runner` report to the same `fresh-reviewer` ($\ge 9$ to pass, max 3 iterations).
7. **Docs & cleanup (no `executed-*.md`):**
   - Update `docs/requirements/<module>.md` and/or `docs/logic/<module>-<concern>.md` **in place** (timeless present tense; no dated paragraphs or `Problem / Fix / Decision` blocks; use a 1-line `> **Guardrail:**` note pointing to `docs/investigations/` if needed).
   - Bump `updated:` frontmatter on every modified doc.
   - **Delete `docs/plans/<id>-<slug>.md`** (do NOT create an `executed-<slug>.md` file).
   - Run `ctask close <ID>`, clear any stale `blocked-by::` reported by `ctask`, and run `ctask validate`.
   - If the task clears the high significance bar in `progress-log`, append one $\le 250$-char line to `docs/progress-log.md`.
8. **Final commit and push.**

## Hard rules

- Never create `executed-<slug>.md` files — shipped truth lives in `docs/requirements/` and `docs/logic/`, commit/task history lives in `docs/done.md` and `git log`.
- Never allow `docs/plans/<id>-<slug>.md` to exceed 150 lines — roll completed phases into 1-line checkmarks and delete the plan file when the task closes.
- Never append historical `Problem / Fix / Decision` blocks or dated verification notes into `docs/requirements/` or `docs/logic/`.
- Never spin on nitpicks or write status reports when a task hits an operator run or null-result decision gate — queue it in `docs/operator-instructions.md`, mark `blocked-by` in `ctask`, and stop.

## Provenance and maintenance

Updated: 2026-10-11 (v2 subfolder paths, 150-line plan cap with phase roll-forward, `executed-*.md` retired, Binary Exit Rule wired to `operator-instructions`).

Re-verification commands:
```bash
command -v ctask
ls doc-templates/docs/plans/_template.md
```
