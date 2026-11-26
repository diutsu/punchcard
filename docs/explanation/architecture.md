---
type: explanation
state: done
created: 2026-10-11
updated: 2026-11-26
cross-file-references: [.claude-plugin/marketplace.json, .agents/plugins/marketplace.json, .agents/plugins.json, plugins/punchcard/session-card.md, plugins/punchcard/hooks.json, plugins/punchcard/rules/AGENTS.md, plugins/punchcard/skills/project-map/SKILL.md, plugins/coding/skills/do-work/SKILL.md, plugins/punchcard/skills/capability-check/SKILL.md, plugins/punchcard/skills/skill-maintenance/SKILL.md]
---

# Architecture

How the punchcard marketplace is built and why it is split this way.

## Plugins

The marketplace ships five plugins. Each owns a territory, so a rule has one home and a user can install only what a project needs.

| Plugin | Territory |
|---|---|
| `punchcard` | How the agent works with this user in every session: style, house rules, asking, briefing, queues, away runs, reports, skill upkeep |
| `coding` | Doing and reviewing code work, tests, scripts, operations, data and experiment discipline |
| `techdocs` | Writing, structuring and reviewing technical documents |
| `project-management` | Tasks, priorities, closing and progress |
| `wip` | Drafts only, never relied on |

Plugins declare no dependencies on each other. Cross-plugin dependency behaviour is untested on a real install, so skills refer to siblings by name.

## How and what in `coding`

`do-work` is the how: a loop of start, baseline, scope, plan, plan check, execute, verify, one review, docs and close. Starting moves a refined task to in progress. Its plan (`plan`) says how to apply the code in one session and sits in a scratch file deleted at close. Before verify, `do-work` decides which leftovers belong to the task; before the close, the done-when check in `validation-and-qa` cross-checks the result against the task. `do-work` files and closes tasks through `tracker`. It carries no rules about any kind of code. The what lives in leaf skills, which `do-work` loads by the files a step touches: `backend-code` for source, `frontend-ui` for views, `changelog` for user-visible changes, `ops-scripts` for scripts, `device-qa` for Android builds.

The split keeps each skill small and lets the leaf rules apply outside the loop, for example when the user edits a file directly. A new kind of work then adds a leaf skill and one line in `do-work`, with no change to the loop.

## The project map

Skills must work in repos that keep docs, tasks and scripts in different places. Instead of hardcoding paths, a skill names a map key, and the project's root instructions file (`AGENTS.md`, `CLAUDE.md` or `GEMINI.md`) resolves it in one `## Project map` block. `project-map` documents the keys and their defaults. A repo that moves its docs then edits one line, and no skill changes.

## Session card and output style

Two always-on pieces live in `punchcard`. The `punchcard` output style (`output-styles/punchcard.md`, synced to `rules/AGENTS.md` for Antigravity via `scripts/sync_rules.py`) sets the shape of responses: action first, honest uncertainty. SessionStart hooks (`hooks/hooks.json` for Claude Code, `hooks.json` + `scripts/session_start_agy.py` for Antigravity) inject `session-card.md`, a short list of house rules: gate before done, privacy wall, delegation tiers, autonomy. A rule goes on the card only when it applies to every session and fits in two lines. Anything longer becomes a skill that loads on demand, which keeps the always-on cost low.

## The low-agent work loop

Agents cost tokens and lose context, so `do-work` spends as few as the change allows. A one-file change needs one author and one reviewer. A larger change adds executor agents for independent steps, still with one reviewer over the whole diff.

The two-agent rule governs review: every changed line is seen by exactly two agents, its author and one clean reviewer that has not seen the author's reasoning. The reviewer scores with `review-rubric`. When it applies quick fixes itself, a fresh instance grades only that fix diff, so nobody scores their own lines. The `suite-runner` agent joins only when test output is too large for the orchestrator to read. All briefs are written in one pass after the plan, using `agent-brief`, so executors can start in parallel.

## Task intake and third-party plugins

`capability-check` runs at the first message of a session and at each new task. It decides whether the input is enough, what the output is, and what happens first: work, questions, design, a plugin trial or a clean session.

Third-party plugins are tracked, not copied. `capability-check` holds a table of plugins under trial and reads it when a task needs a craft no installed skill covers. Each row has a status: `untested`, `trial`, `required` or `dropped`. A verdict needs evidence from real use. Vendored copies go stale and carry someone else's instructions into the user's sessions, so only a reference to the upstream lives here.

## Promotion from `wip`

`skill-reviewer` reads past session transcripts, finds repeated corrections and manual workflows, and drafts skills into `wip`. A draft stays there until it meets the promotion bar in `skill-maintenance`. Promotion moves it into the owning plugin and checks it against the skill anatomy in `skill-maintenance`. Keeping drafts in their own plugin means an unreviewed skill never loads in a project that installed only `coding`.

## Docs and templates

This repository tracks its own `docs/` in the Diataxis layout defined by `docs-management`, as a readable example of the contract. Doc skeletons for new documents live in `techdocs`.

