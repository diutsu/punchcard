---
name: do-work
tier: workflow
description: >
  The work loop for doing a task, several tasks, or untracked work end to end:
  baseline, scope, plan, plan check, execute, verify, one review of the whole
  diff, docs, close. Loads the leaf skills that match the files each step
  touches (backend-code, frontend-ui, changelog, ops-scripts, device-qa) and
  keeps the agent count low. Trigger when the user asks to do, execute or
  implement work with quality gates. Do NOT load for a pure question, for
  debugging with no fix yet (see forensics), or for doc-only edits (see
  docs-management).
trigger: /do-work
---

# /do-work

`do-work` is how work is done. What kind of work it is lives in the leaf skills it loads. The loop has two gates, a plan check and one implementation review, and spends as few agents as the change allows.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Still investigating a bug, a library or the repo | `forensics`, `external-research`, `codebase-search`; then `plan` |
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
| One file, about 50 lines or fewer | No plan file. One author, who self-scores per `review-rubric` and fixes before handing over, then one reviewer. |
| Several steps, or module boundaries touched | Full loop below. |
| Several tasks | Batch mode below. |

Work without a task ID follows the same loop. Skip the close step and report the outcome to the user.

## Loop

1. **Baseline.** Look for a recent green record. Without one, run the `verify` commands once. If the result is red, tell the user before changing anything.
2. **Scope.** Find affected files, test seams and conflicts between code and docs. Resolve each staleness in one line in the plan. If scope is ambiguous, ask through the question interface, 2-4 questions in one batch, recommended option first.
3. **Plan.** Write the plan through `plan`, and read the task through `backlog`. Detail only the active phase of a multi-phase task. Self-score it against the plan dimensions of `review-rubric`. Spawn a separate plan reviewer only when the work crosses module boundaries or has several phases.
4. **Write every brief at once.** Right after the plan, write all executor briefs and the reviewer brief in one pass, using `agent-brief`. Name the leaf skills each brief loads, chosen by the files its step touches:
   - backend source: `backend-code`
   - views and front-end: `frontend-ui`
   - a user-visible change: `changelog`
   - one-off or maintenance scripts: `ops-scripts`
   - an Android build: `device-qa`
5. **Execute.** Launch independent steps in parallel and dependent steps in order, from the briefs already written. Each executor follows `code-task`, runs its targeted tests and commits its step. Worktrees follow `repo-infra`.
   - Executors may edit docs and the changelog when their step says so.
   - **Plan invalidation.** An executor that hits a false assumption stops. Return to step 3.
   - **Binary Exit Rule.** A step only the human can run, or a null result needing a decision, goes to `operator-queue`. Record the blocker through `backlog` and stop working on that task.
6. **Verify.** Run the full suite once, with the `verify` commands, per `validation-and-qa`. Delegate to `suite-runner` only when the output is large.
7. **Implementation gate.** Send one `reviewer` the diff range, acceptance criteria and test output, scored with `review-rubric`.
   - The reviewer applies quick fixes itself. If it changed code, one fresh `reviewer` instance grades only that fix diff.
   - Executor fixes made after review get a delta review from the original reviewer. Allow at most 3 iterations; then report to the user.
8. **Docs.** Update docs in the same pass, per `docs-management`: in place, timeless, `updated` bumped. Docs are committed. Add the changelog line per `changelog`; a milestone goes there too.
9. **Close.** Close the task through `backlog`. Commit per `repo-infra`; push only when asked.

## Batch mode

Use it when the user names several tasks.

- Scope once across all tasks. Related tasks touch the same files, so separate scoping repeats the same reading.
- Plan jointly. One pass reorders by dependency, hoists a shared prerequisite into the first task, and marks cross-task dedup explicitly ("task B step 2 covered by task A step 3, skip").
- Check the plan once for the batch. Each task section scores on its own, and the ordering and dedup are checked too.
- Never merge tasks unless they are the same change, and flag even that to the user first. A task that is too big gets more plan steps, not new task entries.
- Execute per task in order, with separate commits and one review per task. One task lands fully before the next starts.
- Use a rolling baseline: each task's verified end state is the next task's baseline.
- If a task fails its gate after 3 iterations, earlier tasks stand. Continue with later tasks only when they do not depend on it.

## Hard rules

- Never mark a step done without running its command and seeing the exit code.
- Never let an author review its own lines, and never review the same lines twice.
- Never run the full suite more than once per task, plus the baseline when no recent green record exists.
- Never write a path or tool name for plans or tasks here; go through `plan` and `backlog`.
- Never keep working on a task that needs a human; queue it and stop.
- Never push unless asked.
- Never end a session mid-task without a handoff note when the task needs another session (see `operator-queue`).

## Provenance and maintenance

Updated: 2026-11-13.

Re-verification commands:
```bash
ls plugins/coding/agents/reviewer.md plugins/coding/agents/suite-runner.md
grep -n "review-rubric" plugins/coding/skills/do-work/SKILL.md
```
