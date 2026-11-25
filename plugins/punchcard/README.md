# punchcard

How the agent works with this user in every session.

## What it ships

- **Output style and always-on rules** (`output-styles/punchcard.md`, synced to `rules/AGENTS.md`): always-on, action-first responses with honest uncertainty. Adapted from ayghri/i-have-adhd (MIT); see `output-styles/NOTICE.md`. Run `python3 scripts/sync_rules.py --write` after editing `output-styles/punchcard.md`.
- **SessionStart hooks** (`hooks/hooks.json` for Claude Code, `hooks.json` + `scripts/session_start_agy.py` for Antigravity): inject `session-card.md`, the short list of house rules, into every session.
- **Skills**
  - `project-map`: where things live and which tools own them.
  - `capability-check`: task intake at the first message and at each new task; hands plugin gaps to `watchlist`.
  - `watchlist`: the third-party plugins under trial; add, install, record a verdict, uninstall.
  - `grilling`: close gaps in an underspecified request.
  - `agent-brief`: when and how to brief sub-agents, with templates.
  - `find-docs`: locate the right doc.
  - `project-doctor`: validate a repo's setup.
  - `away-mode`, `run-report`: run unattended, then report the result.
  - `skill-reviewer`, `skill-maintenance`: keep the skill library healthy.
- **Status line script** (`scripts/statusline.py`, Claude Code only). Set `STATUSLINE_WORKSPACE_DIR` if you want the project segment to show the top-level folder under a shared workspace directory.

## Enable the status line (Claude Code)

A plugin cannot set the status line. Add this to your user settings (`~/.claude/settings.json`), with the path to this plugin:

```json
"statusLine": {"type": "command", "command": "python3 <path>/scripts/statusline.py"}
```
