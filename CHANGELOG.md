# Changelog

One line per user-visible change or project milestone, newest first.

## Unreleased

### Changed

- The always-on base plugin is now `punchcard` (was `claude`, a reserved name). Reinstall with `/plugin install punchcard@punchcard`.
- `wip` holds four draft agents: `sonnet-executor`, `doc-writer`, `researcher`, `data-auditor`.

### Added

- Four plugins replace the single one: `claude` (always-on base), `coding`, `techdocs` and `project-management`, plus `wip` for draft skills.
- A project map in each project's `CLAUDE.md` tells every skill where files live and which task tool to use.
- `do-work` runs a low-agent work loop: every changed line is seen by its author and one clean reviewer.
- A watchlist tracks third-party plugins under trial, with install and remove actions.
- `away-mode` and `run-report` cover unattended runs and their outcome reports.
- A handoff note carries one long task across sessions; it is local and exists only while that task is in flight.
- `backend-code` bans references from code to tasks, plans and docs, with a diff check; the reviewer flags them and may remove them as a quick fix.
- `migrate-project-docs` maps its output to the current docs layout.
- The task registry, done log and plans are local work under `ops/local/` and are never committed.

### Changed

- Docs follow the Diataxis layout and are committed to the repo.
- Milestones are recorded in this changelog; the separate progress log is gone.
- `do-task` is now `do-work`, `internal-research` is `codebase-search`, `research-methodology` is `validate-run-results`, `debugging-method` is `forensics`, and `operator-instructions` is `operator-queue`.

### Removed

- The `planning-horizons` plugin; its skills moved into `techdocs`.
- README and API-endpoint doc templates.

## 2026-11-11

- Renamed Frank to punchcard and turned it into a Claude Code plugin marketplace.

## 2026-10-26

- The starter doc skeleton installs with the `migrate-project-docs` skill.

## 2026-10-11

- Ported 19 general-purpose skills and scaffolded the repository with doc templates and its own docs.
