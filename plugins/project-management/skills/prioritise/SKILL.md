---
name: prioritise
tier: leaf
description: >
  Decide what to pick up next: validate candidates, rank by unblocking, value,
  effort and risk, pull out quick wins. Load for "what should I pick up", "what
  should I work on", "re-prioritise", or when whats-next finds nothing in
  flight. Do NOT load for work in flight (whats-next).
trigger: /prioritise
---

# /prioritise

Produce a short ranked "next up" list, a few quick wins, and a set of proposed priority changes. This skill reads tasks and writes only the changes the user confirms.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| What needs the user, or what is in progress or in review | `whats-next` |
| Checking which tasks are already done, stale or duplicate | `backlog-review` |
| Executing the chosen task | `do-work` |
| Listing or searching tasks with no ranking needed | `tracker` |
| Turning the chosen task into steps | `plan` |

## Inputs

Gather through `tracker`, using the states, priority scale and labels of the project's workflow file:

1. The to-do tasks, with priority. Narrow by label only when the user names a component.
2. What blocks each of them, and what each blocks.
3. `show` for the top candidates, to read goal, details and done-when.
4. The backlog tasks, titles only, to spot any worth refining.

## Method

1. **Rank only what can start.** Candidates are to-do tasks with no open blocker. In-progress and in-review work belongs to `whats-next`. List backlog tasks worth taking as needing refinement.
2. **Validate.** Run `backlog-review` on the candidates you plan to list (its scope narrowed to them). A task it finds done, stale or a duplicate drops out of the ranking; its confirmation joins this skill's question batch.
3. **Unblock first.** Rank by how many open tasks a task blocks, directly and transitively. A task that frees three others outranks a standalone high-priority task.
4. **Value against effort against risk.** For the rest, judge the outcome's value, the effort from the details, and the risk of leaving it (data loss, wrong numbers, broken workflow). Cheap, valuable and risky-to-leave rank first. Say the judgement in one line; do not invent numeric scores.
5. **Pull out quick wins.** Up to three tasks that take one short session: done-when is clear, no open question, no blocker, and the change is small, or it touches the files of work that just closed or is in flight, so the context is already loaded. A quick win may also appear in "Next up".

## Output

```markdown
## Next up
1. `<ID>` — `<title>`: `<one-line reason>`

## Quick wins
- `<ID>` — `<title>`: `<why it is quick>`

## Needs refinement
- `<ID>` — `<title>`: `<what is missing>`

## Proposed priority changes
- `<ID>`: `<old>` to `<new>` — `<reason>`

## From backlog-review
`<its table, when it found anything>`
```

Keep "Next up" to five items or fewer. Drop a section with no rows.

## Applying changes

Ask the user through the question interface before writing any change: one question per group of related priority changes, plus the `backlog-review` batch, 2-4 per batch, the recommended option first, with "keep as is" as the last option. Apply the confirmed changes via `tracker`.

## Hard rules

- Never change a priority without confirmation.
- Never rank a task whose blocker is open and outside the user's control above work that can start now.
- Never rank a task without passing it through `backlog-review` first.
- Never gather tasks any other way than through `tracker`.
- Never pad a list; fewer items is fine.
- Always give a reason per item, in one line.

## Provenance and maintenance

Updated: 2026-11-26.

Re-verification commands:
```bash
for s in tracker backlog-review whats-next do-work plan; do ls -d plugins/*/skills/$s >/dev/null || echo "missing $s"; done
grep -n '^## Scope' plugins/project-management/skills/backlog-review/SKILL.md
grep -n '^## Priority\|^## Labels' plugins/project-management/skills/tracker/templates/workflow.md
```
