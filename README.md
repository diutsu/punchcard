# punchcard

One person's shared agent setup, packaged as a plugin marketplace for Claude Code, Antigravity and Codex. Each plugin bundles skills, rules, hooks and agents for one area of work, so the same habits follow the author into every project.

Repository: `https://github.com/diutsu/punchcard`

## Plugins

| Plugin | Holds |
|---|---|
| `punchcard` | The always-on base: output style, session card, project map, questions, briefing, skill upkeep |
| `coding` | The work loop and the per-work-type skills for writing, reviewing, investigating and operating code, plus two agents |
| `techdocs` | Writing technical docs: one prose style, doc templates, the Diataxis layout, sourced research |
| `project-management` | Tasks in the project's configured tracker, what's next, prioritisation, backlog review, bug reports, and the product-direction session |
| `wip` | Draft skills proposed by `skill-reviewer` and draft agents, held until promoted |

## Skills

### punchcard

| Skill | Purpose |
|---|---|
| `project-map` | Declare where things live and which tools own them, and find the doc that answers a question |
| `grilling` | Interview the user until a plan is fully specified |
| `capability-check` | Task intake: enough input, output type, skills, session fit, and what happens first; holds the plugins under trial |
| `agent-brief` | Decide whether to spawn an agent and write its brief |
| `project-doctor` | Validate a repo's setup: map, docs, task tracker |
| `away-mode` | Run without the user present, logging decisions |
| `run-report` | Report the outcome of a long operation |
| `skill-reviewer` | Mine past sessions for repeated work and draft skills in `wip` |
| `skill-maintenance` | Keep the skill library organised and free of drift |

### coding

| Skill | Purpose |
|---|---|
| `do-work` | The work loop from baseline to close, with a plan check and one review |
| `code-task` | Executor contract for one scoped step |
| `plan` | A short execution plan for this session's work, reviewed by the user before it runs |
| `backend-code` | Code-quality rules for backend and library source |
| `frontend-ui` | Rules for any user-facing surface |
| `data-integrity` | Raw-versus-derived data discipline |
| `validation-and-qa` | What counts as evidence and as done, and the bar for claiming a change made something better |
| `review-rubric` | Scoring rubric for plans and implementations |
| `forensics` | Find a root cause before fixing |
| `codebase-search` | Answer "how does X work here" from the repo itself |
| `operate-and-diagnose` | Run and measure a live system |
| `project-evaluation` | Deep maintainability review of a project or module |
| `codebase-cleanup` | Find what to remove, simplify or update given where the project is going; fix the small cases, file the rest |
| `interactive-app-review` | Live UX review of a running app |
| `device-qa` | Android build, install and device checklist loop |
| `ops-scripts` | Where maintenance scripts live and how they are labelled |
| `repo-infra` | Git, worktree and commit conventions |
| `changelog` | One changelog line per user-visible change |

Agents: `reviewer` (clean-context scoring of a plan or diff) and `suite-runner` (absorbs large test output).

### techdocs

| Skill | Purpose |
|---|---|
| `writing-style` | The one prose style, with a lint for LLM tells |
| `editorial-review` | Final pass on a doc: lint, critique, edit |
| `doc-templates` | Skeletons for vision, architecture, discovery, design, PRD, research, ADR |
| `docs-management` | Diataxis layout and the frontmatter contract |
| `horizon-review` | Check a planning doc against the Planning Horizons model |
| `review-comment-coach` | Keep review comments at the doc's horizon |
| `handle-comments` | Resolve `[COMMENT]` markers left in docs |
| `external-research` | Build a sourced research doc |

### project-management

| Skill | Purpose |
|---|---|
| `tracker` | Read and file tasks in the project's configured tracker; set up its task workflow once |
| `whats-next` | Show work in flight, what needs the user first |
| `prioritise` | Pick what to start next, with quick wins |
| `backlog-review` | Find done, stale and duplicate open tasks, titles first, and close them with evidence |
| `product-direction` | Bring requirements, PRDs and vision in line with what the user now wants, settle conflicts, decide when each change is built |
| `bug-report` | File a new issue reported outside the current task: settle the expected behaviour with the user and name the docs that change |

## Install

### Claude Code

```bash
/plugin marketplace add diutsu/punchcard
/plugin install punchcard@punchcard
/plugin install coding@punchcard
```

Install any other plugin the same way, with `/plugin install <name>@punchcard`. Validate a local checkout with `claude plugin validate .` and `python3 plugins/punchcard/scripts/sync_rules.py --check`.

### Antigravity

Each plugin ships a root `plugin.json`, and `.agents/plugins.json` exposes the repo plugins (excluding `wip`). Copy or symlink any `plugins/<name>/` into `~/.gemini/config/plugins/<name>/`, or inherit `.agents/plugins.json` from your global config.

### Codex and ChatGPT

`.agents/plugins/marketplace.json` registers the plugins for Codex. Individual skills also install through `npx skills add https://github.com/diutsu/punchcard`. To copy the always-on response style and session card into `~/.codex/AGENTS.md` or ChatGPT Custom Instructions, run `python3 plugins/punchcard/scripts/sync_rules.py --combined`.

## The project map

Skills never hardcode a path or a tool. Each project's root instructions file (`AGENTS.md`, `CLAUDE.md` or `GEMINI.md`) carries one `## Project map` section of `key:: value` lines (`tasks`, `docs`, `scripts`, `changelog`, `verify` and others). A skill names a key, and the `project-map` skill resolves it, so the same skill works in a repo that keeps docs in `docs/` and in one that keeps them in a vault. A missing key takes a default, and a key with no default makes the agent ask.

## More

- [`docs/`](docs/): how punchcard itself is built and run.
- [`plugins/README.md`](plugins/README.md): how to add a plugin.
