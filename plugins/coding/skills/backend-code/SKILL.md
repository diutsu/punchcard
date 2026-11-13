---
name: backend-code
tier: reference
description: >
  Code-quality rules for backend and library source: module and third-party SDK
  isolation, reuse before inventing, fail-fast errors, size caps, and code
  comments that explain why. Load BEFORE writing or reviewing code, in
  do-work, code-task or a direct edit. Do NOT load for prose docs (see
  writing-style), view and UI state rules (see frontend-ui), the definition of
  done (see validation-and-qa), or raw vs. derived data rules (see
  data-integrity).
trigger: /backend-code
---

# /backend-code

Agents write weak code in four ways: they import across module boundaries, invent a helper that already exists, wrap logic in defensive fallbacks that hide bugs, and narrate the code in comments. Check every diff against the five rules below.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Step execution protocol and report block | `code-task` |
| README, API doc, ADR, changelog prose | `writing-style`, `doc-templates` |
| Definition of done, stub policy, test bar | `validation-and-qa` |
| Loading, error, empty and unavailable view states | `frontend-ui` |
| Raw vs. derived data stores | `data-integrity` |

## 1. Respect module and SDK boundaries

Before adding an import or a file, read the architecture doc under the `docs` key (module responsibilities and allowed dependencies).

1. Import a third-party library only inside the one module that owns it.
2. Never pass a raw SDK object, such as a database connection, across a module boundary.
3. Sibling modules (fetchers, interfaces, adapters) never import each other. Shared logic goes in the shared layer the architecture doc names.

## 2. Reuse before inventing

1. Search the owning module for a function or constant that solves most of the problem.
2. Extend or parameterise it in place instead of adding a near-duplicate.
3. Never create a `utils` or `helpers` grab-bag. Put each function in the module that owns its data contract.

## 3. Fail fast

- Never swallow an exception and return `None`, `0`, `[]` or `{}`, unless the behaviour contract in `reference/` specifies that fallback.
- When a required config key, column or parameter is missing, raise an error that names it. Never substitute a guessed default.
- Validate external input once at the boundary. Inside, trust the types.

## 4. Size and shape

- Keep functions to about 40 lines and files to about 350. Split pure calculation from I/O orchestration.
- Add a base class, factory or config flag only when a second concrete consumer exists.
- Pass standard data structures between layers. Do not wrap them in per-layer classes.

## 5. Code comments

A comment explains why, never what.

- Delete a comment that restates the next line.
- Never write a ticket or task ID in a comment.
- Never write history, such as "added after X", "fixed for Y" or "phase 2".
- Do comment a non-obvious constraint: why this algorithm, threshold or ordering; an external API quirk; a hardware or memory bound; a deliberate duplication across a boundary and the test that keeps the copies identical.
- Use docstrings for public module contracts and inline comments for local hazards.

## Hard rules

- Never import a third-party library outside its owning module.
- Never swallow an exception or invent an undocumented default.
- Never write a helper without searching the module for an existing one.
- Never leave a ticket ID, step number or history note in a comment.
- Never add a single-implementation abstraction.

## Provenance and maintenance

Updated: 2026-11-13 (renamed from the earlier code-discipline skill; comment rules extended).

Re-verification commands:
```bash
grep -rnE "(TODO|FIXME)?.*[A-Z]{2,}-[0-9]+" --include=*.py --include=*.ts src | head
```
