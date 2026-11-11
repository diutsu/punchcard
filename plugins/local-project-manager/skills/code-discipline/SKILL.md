---
name: code-discipline
tier: reference
description: >
  REFERENCE, not a workflow — anti-slop code quality, architectural boundary
  enforcement, error-handling discipline, and code-commenting standards.
  Consult BEFORE writing or reviewing any code (inside code-task, do-task, or
  direct edits). Enforces module & third-party SDK isolation, reuse-before-
  inventing checks, fail-fast error handling (no silent fallback slop), size
  caps, and "explain the why, never the what" code comments. Do NOT load for
  prose documentation templates (see write-docs), for UI state rules (see
  ui-ux-discipline), or for test-gate execution (see validation-and-qa).
trigger: /code-discipline
---

# /code-discipline

Agents write bad code in four predictable ways: **(1)** importing across forbidden module boundaries, **(2)** inventing duplicate helpers instead of reusing existing ones, **(3)** wrapping logic in defensive `try/catch` fallbacks that hide bugs, and **(4)** writing verbose functions with noisy "what" comments. Check every diff against the five rules below before committing.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Sub-agent step execution protocol and report format | `code-task` |
| Prose documentation, README, API doc, ADR, and Changelog shapes | `write-docs` |
| Definition of done, test-writing bar, and `_stub_` policy | `validation-and-qa` |
| UI loading/error/empty/unavailable state rules | `ui-ux-discipline` |
| Raw vs. derived data store write rules | `data-integrity` |

## 1. Respect module & SDK boundaries (`docs/architecture.md`)

Before adding an `import` or creating a new file:
1. Check `docs/architecture.md` (`Module responsibilities` and `Allowed dependencies`).
2. **Third-party SDK isolation:** External libraries (e.g., an API client, DB driver, ML framework, or parser) must only be imported inside the single submodule that owns them. Never leak raw third-party SDK objects (like a raw DB connection) across module boundaries.
3. **No sibling cross-imports:** Sibling fetchers, sibling interfaces (`cli`, `ui`, `scheduler`), or sibling domain adapters must never import each other. Shared logic belongs in the designated shared layer declared in `docs/architecture.md`.

## 2. Reuse before inventing (no `utils` dumping grounds)

Before writing a new helper function, type, or query:
1. Grep the owning module for existing functions or constants that already solve 80% of the problem.
2. Extend or parameterize the existing function in place rather than creating a near-duplicate alongside it.
3. Never create generic `utils.py` / `helpers.ts` grab-bag files — place every function in the domain module that owns its data contract.

## 3. Fail fast — zero silent fallback slop

Agents default to "defensive" code that masks broken invariants. Ban these patterns:
- **No broad exception swallowing:** Never write bare `except Exception:` / `catch (e) {}` that logs a warning and returns `None`, `0`, `[]`, or `{}` unless the module's requirement doc (`docs/requirements/<module>.md`) explicitly specifies that fallback contract.
- **No invented default values for missing required config/data:** If a required config key, column, or parameter is missing, raise a clear error at the boundary naming the missing key. Do not silently substitute a guessed default (`config.get("batch_size", 1000)`) that diverges from the canonical config schema.
- **Validate at system boundaries, trust internal types:** Parse and validate external inputs (CLI args, API payloads, raw files) once at ingestion; do not litter internal pure transforms with redundant type-guessing branches.

## 4. Keep functions small and transforms pure

- **Function length ($\le 40$ lines) & file length ($\le 350$ lines):** If a function grows past ~40 lines or mixes I/O with calculation, split the pure calculation from the I/O orchestration.
- **No speculative abstractions:** Do not introduce base classes, factory registries, or configuration flags for a single caller ("just in case we need another backend later"). Build for the current requirement; extract an interface only when a second concrete consumer exists.
- **Pass standard data structures across layers:** Do not invent per-layer wrapper classes around standard tables/frames/dicts when passing data between modules.

## 5. Code comments — explain the *why*, never the *what*

- **Never narrate obvious operations** (`# increment counter`, `# loop over tickers`, `# Phase 2 fix`). Delete any comment that merely restates the next line of code or cites a task step number.
- **Do comment non-obvious constraints:**
  - Why this specific algorithm, threshold, or ordering was chosen over the obvious alternative.
  - External API quirks, rate-limit footguns, or hardware/memory bounds not visible from the code itself.
  - Deliberate duplication across an architectural boundary (e.g., a constant duplicated to preserve zero-dependency isolation, noting the test that asserts byte-identity).
- **Use docstrings for public module contracts**, inline comments only for local landmines.

## Hard rules

- Never import a third-party library outside its owning module or violate the dependency graph in `docs/architecture.md`.
- Never swallow exceptions or invent undocumented fallback defaults — fail loudly when an invariant or input is violated.
- Never write a new helper without first grepping the module for an existing one.
- Never leave task-step narration comments (`# Step 3`, `# Fixed for ANL-12`) in shipped code — comments explain timeless *why* constraints only.
- Never introduce a single-implementation base class or speculative config flag not required by `docs/requirements/`.

## Provenance and maintenance

Authored: 2026-10-11 (extracted and expanded from `code-task` + `code-task/references/Comments.md` + `architecture.md` anti-slop guidelines).

Re-verification commands:
```bash
ls docs/architecture.md
```
