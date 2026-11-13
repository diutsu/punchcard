# claude

How Claude works with this user in every session.

## What it ships

- **Output style** `punchcard` (`output-styles/`): always-on, action-first responses with honest uncertainty. Adapted from ayghri/i-have-adhd (MIT); see `output-styles/NOTICE.md`.
- **SessionStart hook** (`hooks/hooks.json`): prints `session-card.md`, the short list of house rules.
- **Skills**
  - `project-map`: where things live and which tools own them.
  - `grilling`, `capability-check`: close gaps in an underspecified request.
  - `agent-brief`: when and how to brief sub-agents, with templates.
  - `find-docs`: locate the right doc.
  - `project-doctor`: validate a repo's setup.
  - `operator-queue`: commands and decisions only the human can do.
  - `away-mode`, `run-report`: run unattended, then report the result.
  - `skill-reviewer`, `skill-maintenance`, `watchlist`: keep the skill library healthy and track third-party plugins.
- **Status line script** (`scripts/statusline.py`).

## Enable the status line

A plugin cannot set the status line. Add this to your user settings (`~/.claude/settings.json`), with the path to this plugin:

```json
"statusLine": {"type": "command", "command": "python3 <path>/scripts/statusline.py"}
```
