---
name: away-mode
tier: workflow
description: >
  Run without the user present. Load when the user says they will not be around
  ("continue, don't wait for me", "I won't be around"). Never stop to ask: take
  a reasonable default, record each decision in a decisions log, queue
  irreversible or outward-facing actions via `backlog`, keep working
  on everything else, and finish with a `run-report`. Do NOT load when the user
  is present, or to skip a confirmation they have not waived.
trigger: /away-mode
---

# /away-mode

The user is away and expects progress, not questions. Decide, log, continue.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| The user is present | Ask through the question interface (`grilling` for deep gaps) |
| Parking a command or decision that needs the user | `backlog` |
| Writing the final account of the run | `run-report` |

## Procedure

1. **Start the log.** Create the decisions log beside the run report's working files (see `run-report`). Record the start time and the scope the user gave.
2. **Work the list.** Continue the planned work in order. Do not wait on any question.
3. **At each decision point, take a default.** Pick the most reasonable option, preferring the one that is cheapest to reverse and closest to existing conventions. Log it immediately, before moving on:

   ```
   Q: <the question you would have asked>
   TAKEN: <the option you chose>
   WHY: <one line>
   ALTERNATIVE: <the main option you did not take>
   REVERSE: <how to undo or switch>
   ```

4. **Queue gated actions.** Never do these without prior approval: push, publish, delete data, send messages, spend money, change shared infrastructure or accounts. Record each via `backlog` with the exact command (a review request for the started task, otherwise an open question), then keep working on everything else. If the whole remaining plan is gated, finish the safe parts and stop.
5. **Keep the other rules.** The gate before done, the privacy wall and raw-data rules do not relax while away.
6. **Finish with a `run-report`.** Include the decisions log in it and list the tasks in review and the open questions that need the user.

## Choosing defaults

- Prefer reversible over irreversible, small over large, existing convention over new.
- When two options are equal, take the one the project docs or repo already favour.
- Do not widen scope to fill time. File extra ideas as tasks via `backlog`.
- A blocked task is parked in the queue, not guessed at. Move to the next one.

## Hard rules

- Never stop to ask a question while away mode is active.
- Never take an irreversible or outward-facing action without prior approval. Queue it.
- Never skip logging a decision.
- Never loosen a verification gate to finish faster.
- Never end without a `run-report`.

## Provenance and maintenance

Updated: 2026-11-13.

Re-verification commands:
```bash
grep -n 'backlog\|run-report' plugins/punchcard/skills/away-mode/SKILL.md
ls plugins/punchcard/skills/run-report/templates
```
