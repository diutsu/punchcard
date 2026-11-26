---
name: product-direction
tier: workflow
description: >
  A session on what the product should do: bring the requirements, PRDs and
  vision in line with what the user now wants, settle the conflicts and
  blockers that surface, and decide when each change is built. Load when the
  user wants to talk about requirements, product direction, roadmap or vision,
  with input or with none. Do NOT load to specify one request before work
  starts (see grilling), to review one finished planning doc (see
  horizon-review), to rank existing tasks (see prioritise), or to write code.
trigger: /product-direction
---

# /product-direction

The user says where the product should go; the docs say where it was going; the app shows where it is. The session brings the three into agreement and writes the result into the docs. The conversation is how the decision is reached. The docs record only the decision.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| One request needs specifying before work starts | `grilling` |
| Checking one planning doc against the horizons | `horizon-review` |
| Starting a doc that has no requirements conversation behind it | `doc-templates` |
| Ranking tasks that already exist | `prioritise` |
| Explaining how the app behaves, with no change wanted | `codebase-search` |
| The user is away | `away-mode`: do the reading in step 1, then stop |

## Procedure

1. **Read first.** Before any question, read what exists: the docs under the `prd` and `design` keys, the vision, the reference docs (per `project-map`), the open tasks (via `tracker`), and the app itself where the docs are silent (per `codebase-search`). Where the `prd` and `design` keys hold nothing, the requirements are what the repo treats as its contract: the explanation and reference docs and the project instructions. Say which docs you are treating as the requirements before the first round. List the topics the session covers: the user's input, plus what the reading shows is unclear, contradictory or missing.
2. **Confirm, topic by topic.** For each topic, state what the docs and the app say today, quoting the requirement, then ask the user to confirm or correct it. Run the rounds per `grilling`. A topic takes at least three rounds: confirm and challenge, then place, then decide when. Placement and timing wait for the conflict decision they depend on.
3. **Complement.** Offer what the user did not mention and the app implies: behaviour that exists and no doc states, a gap between two requirements, the requirement next to the one under discussion. Each is a question, never an edit.
4. **Challenge.** When the user's input conflicts with a requirement, a priority or something they said earlier, show both texts side by side and name the conflict. Check what the user says about the app against the app. Challenge only what a decision depends on, and say which parts hold. The user decides and may overrule the docs.
5. **Sort each existing requirement** the topic touches into one case:

   | Case | Action |
   |---|---|
   | Covers what the user wants, but reads unclear | Rewrite it; the meaning stays |
   | Too abstract to act on | Sharpen it: replace words such as "fast" or "easy" with a condition someone can test |
   | The user now rejects it | Retire it: remove it, and remove what depended on it |
   | Nothing covers what the user wants | Add a requirement |

6. **Place it.** For each new or changed requirement, propose the doc and the section, per `docs-management`, and a new doc per `doc-templates` when none fits. Check a statement bound for a vision or design doc per `horizon-review`. Get a yes before writing.
7. **Settle conflicts and blockers.** Keep a running list. The question interface hides the message around it, so carry the list inside the round: while an item is open, one question in each round is about it and names the others still open. Every item ends in a decision before the session closes: a conflict by the user choosing a side, a blocker by a timing decision in step 8. Nothing is carried out of the session as an open item.
8. **Decide when.** For each change, ask whether it is built now, after a named milestone (as `tracker` defines one), or once the affected area is stable. State what blocks it and what it would displace: a change built now moves something else later, so name that thing. Skip this step for a change that is complete once the docs are written. Where the repo has no tasks or milestones to compare against, ask only "now" or "later, when `<condition>`".
9. **Write.** Update the docs in place, per `docs-management` and `writing-style`. A doc states how things are. It carries no note about what a requirement used to say, who asked for the change or how it was decided.
10. **Close.** Read back per `./templates/read-back.md`: what changed and where, how each conflict was settled, and when each change is built. Then offer to file the tasks via `tracker`, with blockers recorded, and to rank them per `prioritise`. File them on a yes, into backlog. Move a filed task to to do only when the user says it is ready as written.

## What the session leaves behind

Updated or new docs, and the tasks the user agreed to. No decision log and no open-items file: the docs are the public statement of the product, and the reasoning stays in the conversation.

## Hard rules

- Never write code in this session. In a repo whose product is its docs or skills, the doc edit is the change itself: make it in step 9, and file a task for anything that has to be run or built.
- Never file a task before the requirements round is closed and the user agrees.
- Never change a requirement without showing the user its current text first.
- Never hide a conflict to keep the conversation moving.
- Never ask the user for a fact the repo holds.
- Never write a doc edit before the user agrees to its placement.
- Never close the session with a conflict undecided or a blocker without a timing decision.
- Never leave a note in a doc about what a requirement used to say.
- Never write a roadmap doc. Order and timing live in the tasks.

## Provenance and maintenance

Updated: 2026-11-26. Techniques adapted from skills read on 2026-11-14 and listed in the plugin watchlist held by `watchlist`: checking the user's statements against the code (`domain-modeling`, mattpocock/skills), challenging only what a decision depends on and saying what holds (`strategy-red-team`, phuryn/pm-skills), testable conditions in place of vague words (`prd`, github/awesome-copilot), naming what a new item displaces (`write-spec`, anthropics/knowledge-work-plugins).

Re-verification commands:
```bash
ls plugins/*/skills/product-direction/templates/read-back.md
for s in grilling horizon-review docs-management doc-templates writing-style codebase-search tracker prioritise; do ls -d plugins/*/skills/$s >/dev/null || echo "missing $s"; done
grep -n 'product-direction' plugins/punchcard/skills/capability-check/SKILL.md README.md
```
