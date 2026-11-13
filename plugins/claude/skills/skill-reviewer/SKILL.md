---
name: skill-reviewer
tier: workflow
description: >
  On-demand only. Read previous session transcripts for the current project,
  find repeated corrections, repeated multi-step manual workflows and repeated
  mechanical command sequences, and draft new skills for them in the `wip`
  plugin. Load only when the user asks to mine sessions for skills. Do NOT load
  automatically, to edit installed skills, or to promote a draft without
  approval.
trigger: /skill-reviewer
---

# /skill-reviewer

Turn repeated friction in past sessions into draft skills. The user reviews every draft.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Deciding where a rule belongs, or auditing existing skills | `skill-maintenance` |
| Trying a third-party skill | `watchlist` |
| Promoting a finished draft | `skill-maintenance` (promotion), after approval |

## Procedure

1. **Locate transcripts.** Session files are `~/.claude/projects/<project-folder>/*.jsonl` for the current project. The folder name is the project path with separators replaced by dashes. Scan the sessions modified in the last 30 days unless the user names another window.
2. **Extract only the signal.** Read the lines where the user typed a prompt and the tool calls the agent made. Skip tool results, and never read, quote or store credentials, keys, tokens or personal data. If a line holds any, skip it. A script that streams the jsonl and prints only user prompts and tool names with command heads keeps this mechanical and the volume low.
3. **Find three patterns.**

   | Pattern | Signal | Draft |
   |---|---|---|
   | Repeated correction | The user corrects the same behaviour in two or more sessions | A rule in an existing skill's territory, or a new leaf skill |
   | Repeated manual workflow | The same multi-step sequence is prompted by hand in two or more sessions | A workflow skill |
   | Repeated mechanical commands | The same command sequence appears in two or more sessions | A skill that bundles a script for the mechanical steps |

4. **Prefer scripts.** When the steps are mechanical, put them in `scripts/` inside the skill folder and have the SKILL.md call the script and describe the judgment around it. A script is cheaper and more reliable than prose.
5. **Check for an existing home.** Search installed skills first. If a skill already owns the territory, draft an edit proposal instead of a new skill.
6. **Draft into `wip`.** Write each draft to `plugins/wip/skills/<name>/` in the punchcard marketplace repo, meeting the anatomy contract in `skill-maintenance`. Never write straight into another plugin and never edit an installed skill.
7. **List evidence** at the top of each draft's provenance: session count and a few words per example. No private content, no quotes of prompts.
8. **Present the drafts** through the question interface: promote, revise or drop each, recommendation first. Promote nothing without approval.

## Hard rules

- Never run automatically. The user asks.
- Never read or record credentials, keys, tokens or personal data from transcripts.
- Never write outside `plugins/wip/` and never edit installed skills.
- Never create a draft with fewer than two sessions of evidence.
- Never promote a draft without the user's approval.

## Provenance and maintenance

Updated: 2026-11-13. Chosen over the heavier Task Observer plugin tracked in `watchlist`.

Re-verification commands:
```bash
ls ~/.claude/projects | head
ls plugins/wip/skills
```
