---
name: capability-check
tier: workflow
description: >
  Task intake: is the input enough, what is the output, does a skill cover it,
  does the session fit; then pick the first move. Load at a session's first
  message and whenever the user starts a new task, before acting. Hands gaps to
  `watchlist`. Do NOT load for a follow-up inside a task under way.
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
   | Cleanup, simplification, or a hunt for outdated and half-finished code | `codebase-cleanup` |
   | Failure to explain | `forensics` before any fix |
   | A new defect reported outside the current task | `bug-report` |
   | "What's next", "what needs me" | `whats-next` |
   | "What should I pick up", re-prioritise | `prioritise` |
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

When no installed skill covers the craft, load `watchlist`: it matches the gap to a listed plugin and proposes it. Everything about the list (add, install, verdict, uninstall) lives there.

## Hard rules

- Never exceed one short pass. This is a gate, not a project.
- Never announce the check for a trivial request.
- Never start a multi-module change without a plan.
- Never start a proof of concept without its brief.
- Never ask the user for a fact the repo holds.

## Provenance and maintenance

Updated: 2026-11-26.

Re-verification commands:
```bash
ls plugins/punchcard/skills/watchlist plugins/punchcard/skills/grilling
grep -n 'capability-check' plugins/punchcard/session-card.md
```
