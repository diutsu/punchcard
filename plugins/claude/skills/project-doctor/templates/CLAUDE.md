# <project name> - agent instructions

> One line: what this project is and who uses it.

## Project map

- tasks:: ctask
- docs:: docs/
- investigations:: docs/investigations/
- prd:: docs/prd/
- design:: docs/design/
- scripts:: ops/scripts/
- changelog:: CHANGELOG.md
- worktrees:: ../<repo>.worktrees/
- operator-queue:: ops/local/operator-queue.md
- handoff:: ops/local/handoff.md
- verify:: npm test && npm run lint

## Layout

| Path | Contents |
|---|---|
| `src/` | Application code |
| `tests/` | Tests, mirroring `src/` |
| `ops/` | Scripts and the operator queue |
| `docs/` | Committed docs: `tutorials/`, `how-to/`, `reference/`, `explanation/` |

## Project rules

- List only rules specific to this project. General rules come from the marketplace plugins.
- Name the module boundaries that must not be crossed.
- Name data that is raw and must never be modified in place.
