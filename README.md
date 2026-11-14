# punchcard

One person's shared Claude setup, packaged as a Claude Code plugin marketplace. Each plugin bundles skills, agents and defaults for one area of work, so the same habits follow the author into every project.

Repository: `https://github.com/diutsu/punchcard`

## Plugins

| Plugin | Holds |
|---|---|
| `claude` | The always-on base: output style, session card, project map, questions, briefing, operator queue, skill upkeep |
| `coding` | The work loop and the per-work-type skills for writing, reviewing, investigating and operating code, plus two agents |
| `techdocs` | Writing technical docs: one prose style, doc templates, the Diataxis layout, sourced research |
| `project-management` | The backlog, plans and logs, through the project's task tool |
| `wip` | Draft skills proposed by `skill-reviewer`, held until promoted |
| `local-project-manager` | Temporary. Holds only `migrate-project-docs` until the remaining project migrations finish |

## Skills

### claude

| Skill | Purpose |
|---|---|
| `project-map` | Declare where things live and which tools own them |
| `grilling` | Interview the user until a plan is fully specified |
| `capability-check` | Task intake: enough input, output type, skills, session fit, and what happens first; holds the plugins under trial |
| `agent-brief` | Decide whether to spawn an agent and write its brief |
| `find-docs` | Locate the right project document for a question |
| `project-doctor` | Validate a repo's setup: map, docs, task tool |
| `operator-queue` | Hand the human commands and decisions only they can do |
| `away-mode` | Run without the user present, logging decisions |
| `run-report` | Report the outcome of a long operation |
| `skill-reviewer` | Mine past sessions for repeated work and draft skills in `wip` |
| `skill-maintenance` | Keep the skill library organised and free of drift |

### coding

| Skill | Purpose |
|---|---|
| `do-work` | The work loop from baseline to close, with a plan check and one review |
| `code-task` | Executor contract for one scoped step |
| `backend-code` | Code-quality rules for backend and library source |
| `frontend-ui` | Rules for any user-facing surface |
| `data-integrity` | Raw-versus-derived data discipline |
| `validation-and-qa` | What counts as evidence and as done |
| `review-rubric` | Scoring rubric for plans and implementations |
| `forensics` | Find a root cause before fixing |
| `codebase-search` | Answer "how does X work here" from the repo itself |
| `validate-run-results` | The bar for claiming a change made something better |
| `operate-and-diagnose` | Run and measure a live system |
| `project-evaluation` | Deep maintainability review of a project or module |
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
| `backlog` | Run any task operation through the project's task tool |
| `prioritise` | Rank open tasks |
| `triage-close` | Close tasks whose done-when is met, with evidence |
| `plan` | Turn accepted research into an execution plan |

### local-project-manager (temporary)

| Skill | Purpose |
|---|---|
| `migrate-project-docs` | Move a project's `docs/` to the v2 layout, or bootstrap one |

## Install

```bash
/plugin marketplace add diutsu/punchcard
/plugin install claude@punchcard
/plugin install coding@punchcard
```

Install any other plugin the same way, with `/plugin install <name>@punchcard`. Validate a local checkout with `claude plugin validate .`. Individual skills also install through `npx skills add https://github.com/diutsu/punchcard`.

## The project map

Skills never hardcode a path or a tool. Each project's `CLAUDE.md` carries one `## Project map` section of `key:: value` lines (`tasks`, `docs`, `scripts`, `changelog`, `verify` and others). A skill names a key, and the `project-map` skill resolves it, so the same skill works in a repo that keeps docs in `docs/` and in one that keeps them in a vault. A missing key takes a default, and a key with no default makes Claude ask.

## More

- [`docs/`](docs/): how punchcard itself is built and run.
- [`plugins/README.md`](plugins/README.md): how to add a plugin.
