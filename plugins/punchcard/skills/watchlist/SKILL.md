---
name: watchlist
tier: workflow
description: >
  The list of third-party plugins under trial, and the actions on it. With a
  plugin name or repo: add it to the list, or if it is already listed, install
  or uninstall it. With no argument: show the list and ask what to do. For any
  action, either run the exact command or, when the user prefers, print it for
  them to run. Load when the user says "watchlist", names a third-party plugin,
  or when `capability-check` finds no installed skill for a craft. Do NOT load
  to copy or vendor a plugin, or to write one of our own skills.
trigger: /watchlist
---

# /watchlist

The list is `./references/watchlist.md`. Its Repo column links to each source. It records plugins this marketplace does not ship, so they can be tried, kept or dropped on evidence. It never holds a copy of a plugin's files.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Writing or restructuring our own skill | `skill-maintenance` |
| Deciding whether the session can do a task alone | `capability-check` |
| Mining past sessions for new skills | `skill-reviewer` |

## Invocation

`/watchlist [name or repo] [add | install | uninstall | verdict]`

| Input | Action |
|---|---|
| Nothing | Show the table (name, status, one line), at most five rows at a time, `trial` and `required` first. Ask which to act on. |
| A name or repo not on the list | Add it, then offer to install it. |
| A listed name, no verb | Ask: install, uninstall, record a verdict, or just show. Recommend by status: `untested` gives install, `trial` gives verdict, `dropped` gives nothing. |
| `add`, `install`, `uninstall`, `verdict` | That action. |

Whenever a step runs a command, ask once: run it here, or print it for the user to run. If the user said "just tell me", print only. A plugin install changes the user's setup, so confirm unless they asked for it.

## Actions

### Add

1. Resolve the repo to `owner/name`. Read its README and the instructions it would load: third-party skills run with your permissions.
2. Read the install id from the repo (`.claude-plugin/marketplace.json`: plugin name `@` marketplace name). If it has none, write `none` with its own install and remove commands.
3. Add a row: name, Repo as a link `[owner/name](https://github.com/owner/name)`, install id, what it does in one or two lines, status `untested`, today's date.

### Install

1. Install `<plugin>` from `owner/name` via the active harness's plugin manager (e.g. Claude Code: `claude plugin marketplace add owner/name`, then `claude plugin install <plugin>@<marketplace>`; Antigravity: `agy plugin install https://github.com/owner/name`).
2. Set status `trial` and the date. Reload plugins or restart the session if the harness requires it.

For an entry that is not a plugin, use the install command in its row.

### Record a verdict

After use on real work, set the status and write one line of evidence in the row.

| Verdict | Status |
|---|---|
| Keep and depend on it | `required` |
| Still evaluating | `trial` |
| Not useful, redundant or unsafe | `dropped` |

### Uninstall

1. Uninstall `<plugin>` via the active harness's plugin manager (and remove its marketplace when nothing else uses it).
2. Set `dropped` with the reason and keep the row. Delete a row only when the user asks.

### Suggest

When a task matches a `untested` or `trial` row, say what it does and why it fits, in two lines. Ask through the question interface whether to try it, recommendation first. Skip `dropped` rows.

### Track upstream

For entries this marketplace adapts, check the upstream repo for changes when reviewing the list and note what changed.

## Hard rules

- Never copy or vendor a third-party plugin's files into this marketplace.
- Never install or uninstall without the user's confirmation unless they asked.
- Never mark `required` or `dropped` without evidence from real use.
- Never suggest a plugin again in a session after a no.
- Every Repo cell is a link to the source.
- Never send private data to a plugin's service. The privacy wall applies.

## Provenance and maintenance

Updated: 2026-11-15. Split out of `capability-check`, which now only hands plugin gaps here.

Re-verification commands:
```bash
claude plugin list
grep -c 'https://github.com' plugins/punchcard/skills/watchlist/references/watchlist.md
```
