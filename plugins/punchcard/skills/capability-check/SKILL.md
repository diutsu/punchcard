---
name: capability-check
tier: workflow
description: >
  Task intake. Load at the first message of a session and whenever the user
  starts a new task, before acting. Decides whether the input is enough, what
  the output is (code, proof of concept, mockup, one-off script, artifact,
  doc), whether an installed skill covers the craft, and whether this session,
  model and effort fit. Then picks what happens first: straight to work, a
  round of questions, design and plan, a plugin trial, or a clean session with
  a starting prompt. Also holds the list of third-party plugins under trial.
  Do NOT load for a follow-up inside a task already under way.
trigger: /capability-check
---

# /capability-check

Starting in the wrong mode costs more than the check: code written before the design is known, a design round for a throwaway script, a long task begun in a full context. Decide the mode first, in one short pass.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| A follow-up or correction inside the current task | Continue the task |
| You already know the gap is the user's intent | `grilling` |
| The user is away | `away-mode`: take the default route and log it |
| Briefing a sub-agent | `agent-brief` |

## Procedure

1. **Size it.** A question, a lookup or one obvious edit passes silently: do it. Everything else continues below.
2. **Read four things.** Look up facts in the repo before judging; never ask the user for them.

   | Check | Question | Enough when |
   |---|---|---|
   | Input | Can you start without guessing? | Audience, purpose and a success test are stated or readable from the repo |
   | Output | What is delivered? | One of: code change, proof of concept, mockup, one-off script, artifact, doc, answer |
   | Skills | Does an installed skill cover the craft? | You can name the skill for each part of the work |
   | Session | Do context, model and effort fit? | See step 4 |

3. **Pick the route by output.**

   | Output | Route |
   |---|---|
   | Code change, small and clear | Straight to code: `do-work`, small flow |
   | Code change across modules, or the approach is open | `codebase-search`, then a design with `doc-templates`, then `plan`, then `do-work` |
   | Proof of concept | A one-page brief first, from the proof-of-concept template in `doc-templates`: goals, entry and exit criteria, evaluation, next actions, cleanup. Then `do-work`, proof-of-concept flow |
   | Mockup | `frontend-ui`, mockup rule; no backend |
   | One-off script | `ops-scripts` |
   | Artifact (report, page, diagram) | `writing-style`, plus the visual skill that fits; `run-report` for an outcome report |
   | Doc | `doc-templates` and `writing-style`; `external-research` first when it needs sources |
   | Failure to explain | `forensics` before any fix |
   | "What next" | `prioritise` |
   | Requirements, product direction, roadmap or vision | `product-direction` |

   A skill named here that is not installed: say which plugin holds it and continue with what is installed.

4. **Check the session.**
   - **Clean session.** Ask for one when this context is long or about something else, or when the task will outlast it. Write the starting prompt for it: goal, files and area, constraints, done-when, skills to load. Give it in one code block.
   - **Model and effort.** Ask for a stronger model and higher effort for architecture, an open design or hard debugging. Ask for a mid-tier model when the work is mechanical or only orchestration. Name the change; the user makes it.
5. **Take the first exit that applies.**

   | Finding | Exit |
   |---|---|
   | Input is not enough | `grilling`, 2-4 questions per round |
   | No installed skill covers the craft | Plugin search, below |
   | Session, model or effort does not fit | Ask for the change, with the starting prompt |
   | The route starts with design | Start the design round |
   | None of the above | Start the work |

6. **State the result** in three lines at most: the output, the route, and what you need from the user, if anything.

## Plugins under trial

`${CLAUDE_SKILL_DIR}/references/watchlist.md` lists third-party plugins by purpose, install id and status. Nothing in it is copied into this marketplace.

- **Search.** Match the missing craft to a row, then to the skills in the installed marketplaces.
- **Propose.** Ask through the question interface whether to try the candidate, recommendation first. Read the instructions it would load before recommending it: a third-party skill runs with the user's permissions.
- **Install** on a yes: `claude plugin marketplace add <repo>`, then `claude plugin install <install id>`. Set the status to `trial`.
- **Record the verdict** after real use: `required`, `trial` or `dropped`, with one line of evidence. Keep a dropped row and its reason.
- **Remove:** `claude plugin uninstall <install id>`, and `claude plugin marketplace remove <marketplace>` when nothing else uses it.
- **Add a row** when the user names a plugin: name, repo, install id, what it does, status `untested`, the date.

## Hard rules

- Never exceed one short pass. This is a gate, not a project.
- Never announce the check for a trivial request.
- Never start a multi-module change without a plan.
- Never start a proof of concept without its brief.
- Never ask the user for a fact the repo holds.
- Never install or remove a plugin without the user's confirmation unless they asked.
- Never suggest the same plugin twice in a session after a no.

## Provenance and maintenance

Updated: 2026-11-14.

Re-verification commands:
```bash
ls plugins/punchcard/skills/capability-check/references/watchlist.md plugins/punchcard/skills/grilling
grep -n 'capability-check' plugins/punchcard/session-card.md
```
