---
name: backend-code
tier: reference
description: >
  Code rules for backend and library source: SDK isolation, reuse, fail-fast
  errors, size caps, why-comments. Load BEFORE writing or reviewing code. Do NOT
  load for prose (writing-style), UI states (frontend-ui), definition of done
  (validation-and-qa) or raw vs derived data (data-integrity).
trigger: /backend-code
---

# /backend-code

Agents write weak code in four ways: they import across module boundaries, invent a helper that already exists, wrap logic in defensive fallbacks that hide bugs, and narrate the code in comments. Check every diff against the six rules below.

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
- Never write history, such as "added after X", "fixed for Y" or "phase 2".
- Do comment a non-obvious constraint: why this algorithm, threshold or ordering; an external API quirk; a hardware or memory bound; a deliberate duplication across a boundary and the test that keeps the copies identical.
- Use docstrings for public module contracts and inline comments for local hazards.

## 6. No links from code to project work

Code outlives the tasks, plans and docs that produced it. Those get closed, renamed and deleted, and the reference left in the code then points at nothing.

- When the reason matters, write the reason itself: "retry three times because the provider drops the first connection after idle", not "see the retry investigation".
- The link runs the other way. Docs name the modules they describe (see `docs-management`), and tasks name the files they touch (via `tracker`).
- A URL to an external spec or upstream bug is allowed: it is not project work and it does not move.
- When you edit a file that already holds such a reference, replace it with the reason or delete it in the same pass.

Check a diff before handing it over. Adapt the docs folder name and file extensions to the project:

```bash
git diff -U0 <base>..HEAD -- . ':!docs' ':!*.md' | grep -nE '^\+.*(\b[A-Z]{2,}-[0-9]+\b|docs/|\b(plan|executed|investigation|requirements?)-[a-z0-9-]+|\b(phase|step) [0-9]+)'
```

Review each hit; an external standard such as `RFC-9110` or `UTF-8` is not a finding.

## Hard rules

- Never name a task or ticket ID, a plan, an investigation, a design or requirement doc, a doc path, or a plan step or phase number in code. This covers comments, docstrings, identifiers, test names, log and error messages.

## Provenance and maintenance

Updated: 2026-11-27.

Re-verification commands:
```bash
grep -rnE '\b[A-Z]{2,}-[0-9]+\b|docs/|\b(plan|executed|investigation)-[a-z0-9-]+' --include=*.py --include=*.ts src | head
```
