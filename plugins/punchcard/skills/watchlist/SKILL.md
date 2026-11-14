---
name: watchlist
tier: workflow
description: >
  The list of third-party plugins and skills under investigation, and the
  actions on it: add an entry, install a plugin from another marketplace,
  record a verdict after use, and uninstall or remove one that is no longer
  used. Load when a task matches a listed plugin's purpose, when the user names
  a third-party plugin, or when `capability-check` searches for a missing
  skill. Do NOT load to copy or vendor a plugin, or to author a skill.
trigger: /watchlist
---

# /watchlist

The list is `${CLAUDE_SKILL_DIR}/references/watchlist.md`. It records plugins this marketplace does not ship, so they can be tried, kept or dropped on evidence. It never holds a copy of a plugin's files.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Writing or restructuring our own skill | `skill-maintenance` |
| Deciding whether the session can do a task alone | `capability-check` |
| Mining past sessions for new skills | `skill-reviewer` |

## When to suggest a plugin

Suggest one when the current task matches a listed plugin's purpose and its status is `untested` or `trial`. Say what it does and why it fits, in two lines. Ask through the question interface whether to try it, recommended option first. Do not suggest `dropped` entries.

## Actions

### Add an entry

Add a row with name, repo, what it does, status `untested` and the date. Read the plugin's description or README first so "what it does" is accurate. Read the instructions it would load before recommending an install: third-party skills run with your permissions.

### Install

1. Confirm with the user, unless they asked for the install.
2. Add the source: `claude plugin marketplace add <repo>`.
3. Install: `claude plugin install <plugin>@<marketplace>`.
4. Set status to `trial` and record the date. Tell the user to restart the session or reload plugins.

### Record a verdict

After the plugin has been used on real work, set the status and write one line of evidence in the table, such as what task it ran on and what it produced.

| Verdict | Status |
|---|---|
| Keep and depend on it | `required` |
| Still evaluating | `trial` |
| Not useful, redundant or unsafe | `dropped` |

To promote to a dependency (`required`), name the plugin where the marketplace depends on it. To drop, continue below.

### Uninstall and remove

1. Confirm with the user, unless they asked.
2. Run `claude plugin uninstall <plugin>`. Remove the marketplace with `claude plugin marketplace remove <marketplace>` only if no other installed plugin uses it.
3. Set the status to `dropped` and keep the row with the reason, so nobody re-investigates it. Delete a row only when the user asks.

### Track upstream

For entries that this marketplace adapts (the `required` entry and any adapted skill), check the upstream repo for changes when reviewing the list and note what changed.

## Hard rules

- Never copy or vendor a third-party plugin's files into this marketplace.
- Never install or uninstall without the user's confirmation unless they asked.
- Never mark `required` or `dropped` without evidence from real use.
- Never suggest a plugin more than once per session if the user declined.
- Never send private data to a plugin's service. The privacy wall applies.

## Provenance and maintenance

Updated: 2026-11-13.

Re-verification commands:
```bash
claude plugin list
grep -c '^|' plugins/punchcard/skills/watchlist/references/watchlist.md
```
