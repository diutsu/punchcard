---
type: how-to
state: done
created: 2026-11-13
updated: 2026-11-13
cross-file-references: [plugins/claude/skills/watchlist/SKILL.md, plugins/claude/skills/watchlist/references/watchlist.md]
---

# Add a watchlist entry

Record a third-party plugin so it can be tried, kept or dropped on evidence.

1. Read the plugin's description or README, and the instructions it would load. Third-party skills run with your permissions.
2. Add a row to `plugins/claude/skills/watchlist/references/watchlist.md` with the name, repo, a one-line description, status `untested` and today's date.
3. To try it, run `claude plugin marketplace add <repo>` and then `claude plugin install <plugin>@<marketplace>`. Set the status to `trial`.
4. After using it on real work, set the status to `required` or `dropped` and write one line of evidence in the row.

Never copy the plugin's files into this repository. The `watchlist` skill covers uninstalling and tracking upstream changes.
