# project-management

The only owner of task management in this marketplace. Once enabled, every other skill asks it for task operations ("via `backlog`").

## What it owns

- The backlog: priorities, blockers, modules, open and closed tasks.
- Plans, one per task, deleted when the task closes.
- The done log.

## Skills

| Skill | Use it to |
|---|---|
| `backlog` | Run any task operation through the project's task tool; resolves the tool from the `tasks` key of the project map |
| `prioritise` | Rank open tasks: unblock first, then value, effort and risk, grouped by module |
| `triage-close` | Check done-when criteria against code and git history and close tasks with evidence |
| `plan` | Turn accepted research into a plan of 150 lines or fewer with phase roll-forward |

## Neutral operations

`list`, `show`, `search`, `blockers`/`blocking`, `refs`, `add`, `edit`, `block`/`unblock`, `close`, `validate`, `annotate`, `locations`. Each adapter maps them to commands; see `skills/backlog/SKILL.md`.

## Adapters

One file per tool in `skills/backlog/references/adapters/`. Present: `ctask` (local CLI; registry, done log and plans under `ops/local/`, never committed). The `ctask` adapter also ships seed files in `skills/backlog/templates/`.

To add an adapter:

1. Create `skills/backlog/references/adapters/<tool>.md`. Its name is the value of the project map `tasks` key.
2. State the install hint, the storage locations (including plans), the command or API call for every neutral operation, the task format, and the tool's own rules.
3. If the tool needs seeded files, add them to `skills/backlog/templates/`.
4. Do not edit the other skills; they name no tool.
