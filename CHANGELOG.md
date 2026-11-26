# Changelog

One line per user-visible change or project milestone, newest first.

## Unreleased

### Added

- `backlog-review` in `project-management`: finds done, stale and duplicate open tasks, starting from titles and opening only the suspects, and closes them with cited evidence after one confirmation.
- `whats-next` in `project-management`: shows the in-progress and in-review tasks, the ones that need the user first, and flags stuck work.
- The done-when check in `validation-and-qa`: before a task closes, every done-when item gets evidence or is marked missed.
- `tasks-workflow` map key: a task workflow file, set up once by `tracker`, holds the state names, close reasons, priority scale, labels and milestones. It may be user-level and shared by all projects.

### Changed

- The `backlog` skill is now `tracker`; "backlog" names only the state.
- `prioritise` ranks only to-do tasks, validates them through `backlog-review`, lists quick wins and no longer groups by module.
- Closing a task leaves one short closing comment: `done, closing` (optional), `stale task, closing`, `duplicated task, closing` or `merged with <ID>, closing`.
- `plan` moved to `coding`: a short execution plan, at most 60 lines, for how the engineer applies the code in one session. It sits in a scratch file outside the repo that briefs point to and `do-work` deletes at close or handoff. It waits for approval only when it carries a real choice, a risk or crosses modules.
- `do-work` starts by moving the task to in progress, judges leftovers itself, and moves completed work that needs a human check to in review.
- `tracker`: a regression of a closed task is a new task that links it; something found while working is a comment when it blocks or is due soon, and a backlog task when it can wait, with a mitigation comment when one was applied.
- `whats-next` includes unassigned tasks and picks from to do when nothing is in flight.
- `validate-run-results` is now section 7 of `validation-and-qa`; `find-docs` is now the "Finding a doc" section of `project-map`.
- `tracker` reads and files tasks in whatever tracker the project map names. All task state lives there: handoffs on in-progress tasks, closed work in done.
- New tasks go to backlog and move to to do only on the user's explicit word: they refine it, or say it is ready. In review holds only completed work that needs a human check; partly done work that needs the user gets a comment and stays in progress; anything new for the user is an open question on a task.
- `tracker` has task, handoff and review request templates, and a checklist gate for each move between states.
- Docs never cite task IDs.

### Removed

- `triage-close`, merged into `backlog-review`.
- `close-task`: its leftover judgement and the close are in `do-work`, its done-when pass is in `validation-and-qa`.
- `validate-run-results` and `find-docs`, merged into `validation-and-qa` and `project-map`.
- `ops/local/` is no longer ignored by git; move or delete any local task files there before committing.
- `ctask` support, the `operator-queue` skill and the `operator-queue` and `handoff` map keys.

### Added

- Multi-harness packaging: root `plugin.json` and `.codex-plugin/plugin.json` per plugin, `.agents/plugins.json`, `.agents/plugins/marketplace.json`, Antigravity `SessionStart` hook (`plugins/punchcard/hooks.json` + `scripts/session_start_agy.py`), synced `plugins/punchcard/rules/AGENTS.md` via `scripts/sync_rules.py`, and root `LICENSE` (MIT).
- `codebase-cleanup` in `coding`: audits a project for unearned complexity, duplicated logic, stale assumptions, deprecated features and unfinished code, judged against open tasks and the target architecture. It applies the small behaviour-preserving fixes through `do-work` and files the rest as tasks; the judging runs on the strongest model, the edits on cheaper ones. `capability-check` routes cleanup requests to it.
- `bug-report` and `close-task` in `project-management`: the first files a new issue with its expected behaviour confirmed and its doc impact named; the second makes the agent decide, before closing, which leftovers are part of the task's intention and which become new tasks. `do-work` closes through `close-task`; `capability-check` routes defect reports to `bug-report`.
- `product-direction` in `project-management`: a session that updates requirements, PRDs and vision to match what the user now wants, settles conflicts and blockers, and decides when each change is built. `capability-check` routes requirements, roadmap and vision requests to it.
- Four product and requirements skill collections join the list of third-party plugins under trial, all untested.
- Four plugins replace the single one: `claude` (always-on base), `coding`, `techdocs` and `project-management`, plus `wip` for draft skills.
- A project map in each project's `CLAUDE.md` tells every skill where files live and which task tool to use.
- `do-work` runs a low-agent work loop: every changed line is seen by its author and one clean reviewer.
- `capability-check` holds the list of third-party plugins under trial, with install and remove steps.
- `away-mode` and `run-report` cover unattended runs and their outcome reports.
- A handoff note carries one long task across sessions; it is local and exists only while that task is in flight.
- `backend-code` bans references from code to tasks, plans and docs, with a diff check; the reviewer flags them and may remove them as a quick fix.
- `migrate-project-docs` maps its output to the current docs layout.
- A proof of concept starts from a one-page brief (goals, entry and exit criteria, evaluation, next actions, cleanup) and ends with its result and cleanup.
- `capability-check` is the task intake: it runs at the first message and at each new task and picks what happens first.
- The task registry, done log and plans are local work under `ops/local/` and are never committed.

### Changed

- Renamed `CLAUDE.md` and the `project-doctor` template to `AGENTS.md`; `project-map` now resolves `AGENTS.md`, `CLAUDE.md` or `GEMINI.md`.
- Replaced `${CLAUDE_SKILL_DIR}` with relative paths across all skills, generalized `skill-reviewer` session transcript lookup, replaced hardcoded `/workspace/` in `statusline.py` with `STATUSLINE_WORKSPACE_DIR`, and cleaned up stale references in `wip` agents.
- A draft leaves `wip` only after one real use; the promotion commit names the session or task. A skill the user asks for by hand goes straight into its plugin.
- The always-on base plugin is now `punchcard` (was `claude`, a reserved name). Reinstall with `/plugin install punchcard@punchcard`.
- `wip` holds four draft agents: `sonnet-executor`, `doc-writer`, `researcher`, `data-auditor`.
- Docs follow the Diataxis layout and are committed to the repo.
- Milestones are recorded in this changelog; the separate progress log is gone.
- `do-task` is now `do-work`, `internal-research` is `codebase-search`, `research-methodology` is `validate-run-results`, `debugging-method` is `forensics`, and `operator-instructions` is `operator-queue`.

### Removed

- The temporary `local-project-manager` plugin (`migrate-project-docs`).
- The `planning-horizons` plugin; its skills moved into `techdocs`.
- README and API-endpoint doc templates.

## 2026-11-11

- Renamed Frank to punchcard and turned it into a Claude Code plugin marketplace.

## 2026-10-26

- The starter doc skeleton installs with the `migrate-project-docs` skill.

## 2026-10-11

- Ported 19 general-purpose skills and scaffolded the repository with doc templates and its own docs.
