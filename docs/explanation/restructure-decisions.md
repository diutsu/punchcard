---
type: explanation
state: wip
created: 2026-11-13
updated: 2026-11-14
cross-file-references: [.claude-plugin/marketplace.json, plugins/claude/skills/project-map/SKILL.md]
---

# Restructure decisions

Decisions taken while the marketplace was restructured into four plugins. Each entry gives the option taken, the reason, the alternative, and how to reverse it. The defaults were taken while the user was away. An entry that starts with "Reviewed" records the user's ruling on it.

## Decided by the user

| # | Decision | Option taken |
|---|---|---|
| U1 | Plugin split | `claude`, `coding`, `techdocs`, `project-management`, plus `wip` for drafts |
| U2 | Technical docs location | In the repo, committed |
| U3 | Where `skill-reviewer` drafts go | The `wip` plugin in punchcard |
| U4 | Task tool adapters | `ctask` only for now |
| U5 | Docs layout | Diataxis folders; investigations and PRDs in their own folders |
| U6 | Task Observer (`one-skill-to-rule-them-all`) | Not installed; an on-demand `skill-reviewer` replaces it |
| U7 | `do-task` vs `do-flow` | One workflow only, redesigned to spawn fewer agents |
| U8 | `finance-reference` | Project-specific; not part of any plugin |
| U9 | `caveman` | Removed; not on the watchlist |
| U10 | Watchlist | A list of plugins under investigation with install and remove actions, not vendored copies |

## Defaults taken while the user was away

| # | Question | Option taken | Why | Alternative | How to reverse |
|---|---|---|---|---|---|
| D1 | Where do investigations, PRDs and designs live? | `docs/investigations/`, `docs/prd/` and `docs/design/`, beside the four Diataxis folders (reviewed: `design` added with D19) | Keeps every committed doc under one root that `find-docs` searches | Top-level folders in the repo | Change the defaults in `project-map` |
| D2 | How is `i-have-adhd` kept always on? | The `claude` plugin ships its own forced output style adapted from it; the upstream plugin stays on the watchlist as `required` so changes are tracked | The upstream skill disables model invocation, so nothing can switch it on automatically | Leave it manual (`/i-have-adhd` each session) | Delete `plugins/claude/output-styles/` |
| D3 | Which legacy agents survive? | `reviewer` (was `fresh-reviewer`) and `suite-runner` ship in `coding`; `sonnet-executor`, `researcher`, `doc-writer` and `data-auditor` become brief templates or skill procedures | A reviewer needs a separate context and a suite runner absorbs noisy output; the other four duplicated skills | Ship all six as agents | Copy the definition back from git history of the legacy vault folder |
| D4 | `internal-research` and `research-methodology` names | `codebase-search` and `validate-run-results` (reviewed: the user chose these over `codebase-recon` and `experiment-evidence`) | The old names hid that one reads code and the other sets the bar for measured claims | Keep the old names | `git mv` the folders and update `name:` |
| D5 | Where does `external-research` live? | `techdocs` | Its output is a sourced research doc that feeds designs | `coding` | `git mv` the folder |
| D6 | Where does the operator queue live? | Reviewed: `claude` plugin, file at `ops/local/operator-queue.md`, gitignored like the handoff note | It is local work between the assistant and the human, not a technical doc | Committed at `ops/operator-queue.md`; `project-management` | Change the `operator-queue` default in `project-map` |
| D7 | Blocking hooks | None; the only hook prints the session card | A guard script needs a runtime that exists on both Windows and WSL | A PreToolUse hook that denies hand-edits to task files | Add `hooks` entries to `project-management` |
| D8 | Plugin dependencies between the four plugins | Not declared (reviewed: confirmed) | Each plugin installs on its own; a skill that names a sibling from a plugin that is not installed says so and continues | `claude` depends on the other three | Add `dependencies` to `plugins/claude/.claude-plugin/plugin.json` |
| D9 | Sentence-length cap in the style guide | Dropped; "one idea per sentence, vary length" | Uniform short sentences are themselves listed as a sign of machine writing | Keep the 20-word cap | Edit `writing-style` |
| D10 | README and API-endpoint doc templates | Deleted | The user judged them low value | Keep them | Restore from git history |
| D11 | Legacy rules that conflict with newer instructions | Reviewed: the question interface comes first, and "batch questions as a numbered menu" is the fallback when the interface is unavailable or the question does not fit fixed options. Still dropped: "docs are gitignored vault symlinks", "work on main" | The user wants more than one way to be asked, and committed docs | Carry the other two over | Edit `plugins/claude/session-card.md` |
| D12 | Legacy third-party skills (graphify, Vercel React skills, `ui-ux-pro-max`, `superpowers`, `frontend-design`, `security-guidance`) | Watchlist entries, not copies | They have upstreams; vendoring them goes stale | Vendor into `coding` | Install from the watchlist |
| D13 | Status line script | Shipped in `plugins/claude/scripts/`; enabling it is a manual settings line | A plugin cannot set the status line | Leave it out | Delete the script |
| D15 | Where do ctask's files live, and what does the task tool own? | Reviewed: ctask keeps `docs/tasks.md`, `docs/done.md` and `docs/plans/`. The progress log is gone; milestones are changelog lines (`changelog`). The next-session note left `project-management`: it is a handoff note owned by `operator-queue`, at the `handoff` map key (`ops/local/handoff.md`), never committed, and it exists only while a task that spans sessions is in flight | The user: a handoff is not a project-management file, and pending tasks belong to prioritisation | Keep both under the task tool | Edit `operator-queue`, `changelog` and the `handoff` key in `project-map` |
| D16 | Reviewer quick-fix limit | About 20 lines per fix, no behaviour or design change, targeted tests still pass; at most 3 review rounds | Small enough that a fresh grader can check the fix diff quickly | Reviewer never edits; or no limit | Edit `review-rubric` |
| D17 | Is a reviewer needed for a small change? | Yes: one author and one reviewer, always | The user's rule is that every change is seen by two agents | Author self-scores only | Edit the right-sizing table in `do-work` |
| D18 | Doc size ceilings | Reviewed: removed. A doc can be long when it is well structured; split by topic, not by line count | The user judged ceilings unnecessary | 400 and 200 line ceilings | Edit `docs-management` |
| D19 | Template destinations | Reviewed: vision and PRD to `prd`; target architecture and design doc to the new `design` key; ADR to `explanation/`; discovery and research doc to `investigations` | Docs about things not built yet stay out of the Diataxis folders; an ADR records a decision already made | Everything under `explanation/` | Edit the table in `doc-templates` and the `design` key in `project-map` |
| D20 | How many sessions does `skill-reviewer` scan? | Reviewed: sessions from the last 30 days | Bounds the token cost of a run by time | The latest 10; all sessions | Edit `skill-reviewer` |
| D21 | Source for the machine-writing rules | Reviewed: rebuilt on 2026-11-14 from the full raw wikitext of Wikipedia's "Signs of AI writing" (179,955 bytes, read in full). `llm-tells.md` now follows the page's sections, and the lint script checks the new mechanical tells | The first build saw a truncated fetch | Keep the first build | Re-run against the page and edit `writing-style/references/llm-tells.md` |
| D22 | Legacy folder | Deleted from `C:\Users\gonca\workspace\punchcard\legacy`; its links into the vault were removed first and the vault folders are intact | The user asked for complete removal | Keep until review | Not reversible; the vault copy of the old skills remains at `projects\claude\skills` |
| D14 | `migrate-project-docs` | Left untouched in `local-project-manager` | The user is still using it for two migrations | Delete now | Remove the plugin and its marketplace entry |
