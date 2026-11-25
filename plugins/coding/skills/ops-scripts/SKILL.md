---
name: ops-scripts
tier: leaf
description: >
  Where one-off and maintenance scripts live and how they are labelled: written
  to the `scripts` map key folder, committed, and opened with a header giving
  purpose, steps, when to run, when not to run, created date and expiry date.
  Includes the sweep for expired scripts. Load before writing any script that
  is not part of the product code, and when cleaning up old scripts. Do NOT
  load for product source (see backend-code), data audits (see
  data-integrity), or repo and git conventions (see repo-infra).
trigger: /ops-scripts
---

# /ops-scripts

A one-off or maintenance script is a project artifact. It lives in the repo, with a header that says what it is for and when it can go.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Product code and tests | `backend-code` |
| Raw vs. derived data audit scripts | `data-integrity` |
| Git commits and worktrees | `repo-infra` |
| Commands only a human can run | `backlog` |

## Placement

1. Resolve the `scripts` key of the project map (see `project-map`). The default is `ops/scripts/`.
2. Write the script there. Never in the repo root, outside the repo, or in a temp folder.
3. Commit it with the work that needed it.

## Header

Start every script with the header from `./templates/header.sh` or `./templates/header.py`. Fill every field:

- **Purpose:** one sentence.
- **Main steps:** the actions in order.
- **When to run:** the trigger or schedule.
- **When NOT to run:** what makes it unsafe or pointless.
- **Created:** the date.
- **Expires:** the date after which it may be deleted.

Pick an expiry that matches the need: a migration script expires when the migration is done everywhere, a diagnostic a few weeks out. A script that should live on indefinitely belongs in product code or a documented tool, not here.

## Sweep expired scripts

1. List scripts in the folder whose `Expires` date has passed. Read the header of each file.
2. Check each candidate for current use: search the repo for references, and check the history for recent runs.
3. Ask the user through the question interface which to delete, 2-4 questions per batch, recommending deletion for unreferenced scripts and an extended expiry for referenced ones.
4. Delete the confirmed scripts and commit the deletion per `repo-infra`. For an extension, change only the `Expires` line.

## Hard rules

- Never write a script outside the `scripts` folder.
- Never leave a script uncommitted.
- Never omit the header or any of its fields.
- Never delete an expired script without the user's confirmation.
- Never edit a script's logic during a sweep.

## Provenance and maintenance

Updated: 2026-11-13.

Re-verification commands:
```bash
grep -L "Expires" ops/scripts/*
grep -rn "Expires:" ops/scripts | head
```
