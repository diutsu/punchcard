# From the migrated tree to the current layout

The tree this skill produces uses `requirements/`, `logic/`, `plans/` and `investigations/`. The current layout is defined by `docs-management`. After a migration, convert with this table.

| Folder or `type` | Becomes |
|---|---|
| `requirements/`, `requirement`: behaviour that is built | `reference/`, `reference` |
| `requirements/`, `requirement`: behaviour not built yet | `prd` key, `prd` |
| `logic/`: formulas, rules, contracts | `reference/`, `reference` |
| `logic/`: rationale and trade-offs | `explanation/`, `explanation` |
| `investigations/`, `investigation`, `research` | `investigations` key, `investigation` |
| `plans/`, `plan` | Not a doc: hand to `plan`; delete plans for closed tasks |
| root `architecture.md` | `explanation/` |
| root `usage.md` | `how-to/`, split by goal |
| `operator-instructions.md` | `operator-queue` |
| `progress-log.md` | `changelog` |
| `next-session-prompt.md` | Delete; a handoff note exists only for a task in flight (`operator-queue`) |

1. List every doc with its folder and `type`.
2. Decide each destination from the table. A doc that splits two ways becomes two docs.
3. Move with `git mv`, set `type`, bump `updated`, and fix `cross-file-references` and links in the same pass.
4. Delete the emptied folders, then run the validation procedure in `docs-management`.
