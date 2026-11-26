---
name: grilling
tier: workflow
description: >
  Interview the user until a plan, decision or idea is fully specified, in
  rounds of 2-4 questions. Load when the user asks to be grilled or
  stress-tested, or `capability-check` finds the request too underspecified. Do
  NOT load for one clarifying question, facts you can look up, or in
  `away-mode`.
trigger: /grilling
---

# /grilling

Interview the user until you share one understanding. Treat the topic as a **design tree**: every decision branches into the decisions that depend on it.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| One clarifying question settles it | Ask it directly through the question interface |
| The user is away and told you not to wait | `away-mode` |
| The user wants options for a known decision, not an interview | Answer with ranked options, recommendation first |
| Deciding whether the session can proceed alone | `capability-check` |

## Procedure

1. **Build the tree.** List the decisions the topic needs. Mark which depend on others.
2. **Find the frontier.** The frontier is every open decision whose prerequisites are settled. Those are the questions you can ask now without guessing answers you have not heard.
3. **Ask one round.** Word each question so choosing the recommended option means "yes, your recommendation".
4. **Fold the answers in.** Settled decisions push the frontier outward and unblock dependent questions. Recompute the frontier and ask the next round. A question that depends on an open question in this round belongs to a later round.
5. **Stop when the frontier is empty.** Every branch is visited and nothing is silently assumed. Read the shared understanding back in a few lines and act only after the user confirms it.

If the frontier holds more than four questions, ask the four that unblock the most others and carry the rest to the next round.

## Facts are your job, decisions are the user's

When a question needs a fact from the environment (files, tools, config, docs), look it up. Brief a sub-agent with `agent-brief` when the search is large, and do not wait on it: only questions downstream of the fact wait, so ask the rest of the frontier now. Never ask the user for something you can read.

Put each real decision to the user and wait for the answer.

## Hard rules

- Ask through the question interface, 2-4 questions per round, recommended option first. Fall back to one numbered menu in prose only when the interface is unavailable or the question does not fit fixed options. Never one question at a time.

## Provenance and maintenance

Updated: 2026-11-27. Source: the `grilling` skill in https://github.com/mattpocock/skills (MIT).

Re-verification commands:
```bash
grep -n 'question interface' plugins/punchcard/skills/grilling/SKILL.md
curl -sL https://raw.githubusercontent.com/mattpocock/skills/main/skills/productivity/grilling/SKILL.md | head -20
```
