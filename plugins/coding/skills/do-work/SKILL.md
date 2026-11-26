---
name: do-work
tier: workflow
description: >
  The work loop for tasks or untracked work: baseline, scope, plan, execute,
  verify, one review, docs, close; loads matching leaf skills. Load when the
  user asks to do, execute or implement work. Do NOT load for a pure question,
  debugging with no fix (forensics) or doc-only edits (docs-management).
trigger: /do-work
---

# /do-work

`do-work` is how work is done. What kind of work it is lives in the leaf skills it loads. The loop has two gates, a plan check and one implementation review, and spends as few agents as the change allows.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Still investigating a bug, a library or the repo | `forensics`, `external-research`, `codebase-search` |
| Settling a task's goal or done-when | refinement, via `tracker` |
| Doc-only work | `docs-management`, `writing-style` |
| Running or measuring a live system | `operate-and-diagnose` |
| Implementing one already-scoped step as a sub-agent | `code-task` |
| What counts as done | `validation-and-qa` |

## Agent budget

Typical run: executor agents for the steps, plus one `reviewer`, plus one grader only when the reviewer changed code, plus `suite-runner` only for large suite output.

- The orchestrating session can run on a mid-tier model. Give a stronger model only to steps that need reasoning, such as ambiguous scope or architecture.
- Two-agent rule: every changed line is seen by exactly two agents, its author and one clean reviewer that has not seen the author's reasoning.
- One review per task, over the whole diff range, never one per step.

## Right-sizing

| Change | Flow |
|---|---|
| One file, about 50 lines or fewer | Inline plan. One author, who self-scores per `review-rubric` and fixes before handing over, then one reviewer. |
| Several steps, or module boundaries touched | Full loop below. |
| Several tasks | Batch mode below. |
| Proof of concept | Proof-of-concept flow below. |

Work without a task ID follows the same loop and must fit one session. Skip only the `tracker` steps; still judge leftovers and run the done-when check with the user's request as the intention, and report the outcome and any follow-ups to the user.

## Loop

1. **Start.** Read the task through `tracker` and move it to in progress through its gate. A to-do task is refined and clear enough to pick up; do not re-refine it. What only the user can answer is an open question per `tracker`.
2. **Baseline.** Look for a recent green record. Without one, run the `verify` commands once. If the result is red, tell the user before changing anything.
3. **Scope.** Find affected files, test seams and conflicts between code and docs. Resolve each staleness in one line in the plan.
4. **Plan.** Write the plan through `plan`, in its scratch file, covering only this session's work. Self-score it against the plan dimensions of `review-rubric`. Spawn a separate plan reviewer only when the work crosses module boundaries. Show it per `plan`, which says when to wait.
5. **Write every brief at once.** Right after the plan, write all executor briefs and the reviewer brief in one pass, using `agent-brief`, each with the plan file's path and its step number. Name the leaf skills each brief loads, chosen by the files its step touches:
   - backend source: `backend-code`
   - views and front-end: `frontend-ui`
   - a user-visible change: `changelog`
   - one-off or maintenance scripts: `ops-scripts`
   - an Android build: `device-qa`
6. **Execute.** Launch independent steps in parallel and dependent steps in order, from the briefs already written. Each executor follows `code-task`, runs its targeted tests and commits its step. A step is done only when its command ran and its exit code was seen. Worktrees follow `repo-infra`.
   - Executors may edit docs and the changelog when their step says so.
   - **Plan invalidation.** An executor that hits a false assumption stops. Return to step 4.
   - **Leftovers.** After the last step, judge them per **Leftovers** below. In-scope items become plan steps in this loop, so the one verify and the one review cover them.
   - **Blocked on the human.** A command only the human can run, or a decision only the user can make, is a comment on the task per `tracker`. Stop working on that task and move to the next unblocked work.
7. **Verify.** Run the full suite once, with the `verify` commands, per `validation-and-qa`. Delegate to `suite-runner` only when the output is large.
8. **Implementation gate.** Send one `reviewer` the diff range, acceptance criteria and test output, scored with `review-rubric`.
   - The reviewer applies quick fixes itself. If it changed code, one fresh `reviewer` instance grades only that fix diff.
   - Executor fixes made after review get a delta review from the original reviewer. Allow at most 3 iterations; then report to the user.
9. **Docs.** Update docs in the same pass, per `docs-management`: in place, timeless, `updated` bumped. Docs are committed. Add the changelog line per `changelog`; a milestone goes there too.
10. **Close.** Run the done-when check per `validation-and-qa`. A `missed` item gets its targeted test and a delta review, no second full suite; if it still cannot be met, leave the task in progress with a comment saying why. When a human must check or run something, move the task to in review with a review request; otherwise close it through `tracker`, naming any follow-ups filed. Delete the plan file. Commit per `repo-infra`; push only when asked.

## Leftovers

Two failures to prevent: stopping short because finishing means touching other files or covering more cases, and asking the user about every loose end. Collect skipped cases, files the change implies but no step named, docs and tests the change made stale, the executors' `ISSUES SPOTTED`, deviations from the plan and reviewer notes not applied. Anchor the intention in one sentence (the task's goal and done-when, never wider or narrower), then ask of each item: if this stays undone, is the goal unmet, or is something this change touched now wrong?

| Class | Signs | Action |
|---|---|---|
| In scope | Yes to the test, citing the goal clause it serves or the changed line that made it necessary | Plan step in this loop |
| Separate concern | No to the test. It has its own goal, and the work is correct without it, including the same behaviour elsewhere that this change did not create | Comment or backlog task per `tracker` |
| Defect the change did not cause | A failure found on the way | `bug-report` |
| Nit | No user-visible effect | List it in the closing report |

"It needs changes in other files", "it adds cases" and its size are never reasons to defer. An unclear item is in scope when leaving it would let a user hit the original problem again, or a new one the change introduced; otherwise it is a separate concern.

## Proof-of-concept flow

A proof of concept answers a question; its code is thrown away.

1. **Brief.** Require the brief from the proof-of-concept template in `doc-templates`. Without goals, entry and exit criteria and an evaluation fixed in advance, stop and write it with the user.
2. **Entry.** Check each entry criterion. If one fails, do not start; report which.
3. **Build.** Work in a worktree or branch per `repo-infra`, marked throwaway. Skip the plan review, the implementation review and the changelog. Keep the code honest: no fabricated results (`validation-and-qa`).
4. **Evaluate.** Measure each goal against its threshold per `validation-and-qa`. Stop at the first exit criterion met, the time box included.
5. **Close.** Fill the result section of the brief. Take the next action the brief names for the outcome, filing it via `tracker` when it is work. Do the cleanup the brief lists and report it item by item.

Code from a proof of concept never merges. A pass leads to a design or a task that builds it properly.

## Batch mode

Use it when the user names several tasks.

- Scope once across all tasks. Related tasks touch the same files, so separate scoping repeats the same reading.
- Plan jointly. One pass reorders by dependency, hoists a shared prerequisite into the first task, and marks cross-task dedup explicitly ("task B step 2 covered by task A step 3, skip").
- Check the plan once for the batch. Each task section scores on its own, and the ordering and dedup are checked too.
- Never merge tasks unless they are the same change, and flag even that to the user first. A task too big for one session is split per `plan`; the rest goes in the handoff, not into new tasks.
- Execute per task in order, with separate commits and one review per task. One task lands fully before the next starts.
- Use a rolling baseline: each task's verified end state is the next task's baseline.
- If a task fails its gate after 3 iterations, earlier tasks stand. Continue with later tasks only when they do not depend on it.

## Hard rules

- Never write a path or tool name for plans or tasks here; go through `plan` and `tracker`.
- Never file a task to defer or hand off the work in hand, and never end a session mid-task without a handoff (`tracker`) when the task needs another session; a handoff stays on the in-progress task.

## Provenance and maintenance

Updated: 2026-11-27.

Re-verification commands:
```bash
ls plugins/coding/agents/reviewer.md plugins/coding/agents/suite-runner.md
grep -n "review-rubric" plugins/coding/skills/do-work/SKILL.md
for s in plan validation-and-qa tracker bug-report agent-brief; do ls -d plugins/*/skills/$s >/dev/null || echo "missing $s"; done
```
