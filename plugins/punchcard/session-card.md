# Session card

House rules for every session. Mechanics live in skills; these are the rules.

## Before you call work done

- **Gate before done.** Run the project's `verify` command (resolve it through `project-map`) and show the output. "Should work" is not a status. On an unexpected failure, never conclude "broken" from one run. Triage in order and stop at the first step that settles it: (1) run the full suite and see if it reproduces; (2) run the failing test alone, and if it passes, another test polluted shared state; (3) run its whole file alone, where a pass means an earlier test in the file did it and a fail means a real bug or pollution from an earlier file.
- **Plan first.** Even a trivial change gets a one-line plan. Validate a data source against ground truth before building on it.
- **No stubs presented as done.** If a stub must stay, flag it with a task and a report line.
- **Keep docs current in the same pass** as the change that made them stale. Do not defer it to the user.
- **UX honest states.** Every user-facing surface shows real loading, error, empty and unavailable states. Never a fabricated value or a false all-clear.

## Data and privacy

- **Raw data is never destroyed or overwritten.** Derived data is disposable: wipe and recompute from raw. Back up before any destructive change to real data.
- **Privacy wall.** Real personal or financial data, and the user's name and email, never go to an external service (web query, API, MCP server, third-party AI). Use generic placeholders.

## Delegation

- Keep reasoning on the main model: architecture, multi-step debugging, trade-offs, judging agent output, final decisions.
- Hand fetching, processing and code-and-test loops to a mid-tier model.
- Hand trivial contained edits (rename, flag, boilerplate, one-file fix) to the cheapest model.
- The reviewer is never the author. Brief sub-agents with `agent-brief`; pass file paths, not pasted contents.
- Run independent delegations in parallel.

## Autonomy

- At the first message of a session and at each new task, run `capability-check` before acting. A trivial request passes silently.
- Work through the list without interrupting. Batch questions to the end.
- File tangents as tasks. A new ask does not reorder work in flight; it joins the end of the queue unless the user confirms a new priority.
- Ask decisions through the question interface: 2-4 questions per batch, recommended option first. When the interface is unavailable or the question does not fit fixed options, batch the questions in one message as a numbered menu, recommended option first.
- When the user says they are away, load `away-mode`.

## Where things live

- Resolve every location and tool through `project-map`. Never guess a path.
- All task state goes through the `project-management` plugin: tasks, plans, handoffs, reviews, open questions and done work live in the project's tracker. Milestones go to the changelog.
- New tasks go to backlog and move to to do only after the user refines them. Anything new that needs the user is an open question on a task; in review is only for started work.

## Writing guidance

- **State how it is, never how it was.** No past behaviour, old names or change notes in code, comments, docs or skills. History lives only in the changelog, git and tools made for migration.
- **Write the rule, not the incident.** State what to do next time, in imperative form. History belongs in the commit message.
- Stage files explicitly. Never `git add -A` or `git commit -a`.
