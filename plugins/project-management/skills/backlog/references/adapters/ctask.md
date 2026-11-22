# Adapter: ctask

`ctask` is a local Python CLI over a markdown registry. It finds the repo root with `git rev-parse --show-toplevel`.

Install hint when `command -v ctask` fails: `uv tool install git+https://github.com/diutsu/ctask`, or run once with `uvx --from git+https://github.com/diutsu/ctask ctask <cmd>`.

## Locations

The registry is local work. It is never committed; its folder is ignored by git.

| Item | Path |
|---|---|
| Registry (open tasks) | `ops/local/tasks.md` |
| Done log | `ops/local/done.md`, written by `close` |
| Plans | `ops/local/plans/<ID>-<slug>.md` |
| Module prefixes | optional `.ctask` next to the registry: `{"modules": {"<module>": {"prefix": "<PFX>", "section": "## <name>"}}}` |

If `ctask` does not find the registry on its own, pass the paths on every call: `ctask --file ops/local/tasks.md --done-file ops/local/done.md <subcommand>`.

## Seed files

ctask needs the registry and the done log to exist. For a project without them, copy `../../templates/tasks.md` and `../../templates/done.md` (from this skill's `templates/` folder) to the paths above, add `ops/local/` to `.gitignore`, then validate. Plans are created on first use (`plan`).

## Operation map

| Operation | Command |
|---|---|
| list | `ctask list [--prio P] [--module M] [--blocked] [--unblocked] [--ids-only]` |
| show | `ctask show ID [ID ...]` (falls back to the done log, marked closed) |
| search | `ctask search TEXT [--field goal\|details\|done\|title\|all] [--include-done] [--ids-only]` |
| blockers / blocking | `ctask blockers ID`, `ctask blocking ID` |
| refs | `ctask refs [--referencing PATH] [ID]` |
| add | `ctask add --module M --title T --prio P --goal G --details D --done-when W [--blocked-by X] [--refs R]`; use `--id ID` or `--id-prefix PFX` to control the id; `--goal-file`, `--details-file`, `--done-when-file` or `--stdin` for long bodies |
| edit | `ctask edit ID [--title] [--prio] [--module] [--section]`, plus `--goal`, `--details`, `--done-when` or their `--append-*` forms |
| block / unblock | `ctask edit ID --blocked-by X` / `ctask edit ID --clear-blocked-by` |
| close | `ctask close ID` (moves the span to the done log; reports stale `blocked-by::`) |
| validate | `ctask validate` |
| annotate | `ctask edit ID --append-details "<note>"` (predictions, commit hashes, findings) |
| locations | table above |
| rename id | `ctask renumber OLD NEW` (rewrites other tasks' `blocked-by::`; `refs::` and prose are not touched) |
| sections | `ctask add-section "<name>" --after "<existing>"`, `ctask remove-section "<name>"` (only when empty) |

Priorities in use: `high`, `medium`, `low`. Run `ctask list` without filters to see the module set and id prefixes before adding.

## Task format

```markdown
### SCH-17 — Title

- prio:: high
- module:: interfaces.scheduler
- created:: 2026-07-15
- blocked-by:: SCH-12
- refs:: path/one, path/two

**Goal.** ...

**Details.**
- ...

**Done when.** ...
```

Tasks sit under a `## <module>` section. `close` appends two metadata bullets to the span in the done log. Untouched spans are never re-rendered.

## Rules specific to ctask

- Never read the registry raw when a query answers the question. The file is many KB.
- Never hand-edit a task span, the done log, or the module map when a subcommand does it.
- Never commit the registry, the done log or a plan.
- Run `ctask validate` after any batch of changes.
- The registry's table of contents and prose outside task spans are not tool-protected; edit them directly when a section reorg makes them stale.
- If an operation is missing, extend `ctask` in its own repo (it has a test suite) instead of editing around it.
- A failed parse writes nothing; fix the file's structure the reported error names, then retry.
- Plans are plain markdown outside ctask; `plan` writes them directly at the path above.
