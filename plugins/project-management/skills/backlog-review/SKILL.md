---
name: backlog-review
tier: leaf
description: >
  Sweep the tasks in backlog for stale ones (likely done elsewhere or no
  longer relevant) and duplicates, starting cheaply from titles and opening
  only the suspects. Load when the user asks to review, groom or prune the
  backlog, or to find duplicate or stale tasks. Do NOT load to verify open
  tasks in other states (see triage-close), to rank work (see prioritise) or
  to add tasks (see backlog).
trigger: /backlog-review
---

# /backlog-review

Find the backlog tasks that should not be there, spending as little reading as possible. Titles raise suspicion; only evidence gives a verdict.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Checking done-when across open tasks in any state | `triage-close` |
| Ranking what to do next | `prioritise` |
| Adding or refining a task | `backlog` |

## Method

Run the passes in order. Each pass reads only what the one before flagged.

1. **Titles.** List, via `backlog`, the ids and titles of backlog tasks, plus the titles of tasks in every other state, closed ones included. Read recent commit subjects and changelog lines. Open no task. Flag:
   - **duplicate suspect:** two titles aim at the same outcome, including a backlog title that matches a task in another state
   - **stale suspect:** a commit, changelog line or closed task suggests the outcome already exists, or the title names something the repo no longer has
2. **Task bodies.** Show only the suspects. Compare goal and done-when. Drop a suspect whose goal differs.
3. **Evidence.** Check the survivors with the check, classify and cite steps of `triage-close`.
4. **Confirm and write.** Report, then apply what the user confirms through the batch and write steps of `triage-close`. For duplicates, name the survivor and move anything only the other task holds onto it.

## Output

```markdown
| Task | Verdict | Evidence | Proposed action |
|---|---|---|---|
| `<ID>` | done, obsolete or duplicate of `<ID>` | `<file:line, commit or task>` | `<close or merge>` |
```

Add the suspects that stayed unproven, with what is missing, and the counts: tasks listed, suspects, opened, confirmed.

## Hard rules

- Never give a verdict from a title; a title only makes a suspect.
- Never open a task that no pass flagged.
- Never close or merge without the user's confirmation.
- Never report the backlog as clean beyond what the title pass can catch; say that unflagged tasks were not opened.

## Provenance and maintenance

Updated: 2026-11-25.

```bash
grep -n '^## Method' plugins/project-management/skills/triage-close/SKILL.md
```
