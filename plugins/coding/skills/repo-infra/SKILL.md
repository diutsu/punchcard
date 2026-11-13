---
name: repo-infra
tier: leaf
description: >
  Git and repository conventions: worktree location, explicit staging, scoped
  commits, commit timing, pushing, branching off a default branch, and keeping
  personal details out of config and metadata. Load before creating a worktree,
  staging, committing, pushing or setting package metadata. Do NOT load for
  where scripts live (see ops-scripts), the work loop (see do-work), or
  changelog entries (see changelog).
trigger: /repo-infra
---

# /repo-infra

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Script placement and headers | `ops-scripts` |
| The work loop and its gates | `do-work` |
| Changelog entries | `changelog` |
| Where docs and other files live | `project-map` |

## Worktrees

Create worktrees at the `worktrees` key of the project map (see `project-map`). The default is a sister folder, `../<repo>.worktrees/<slug>`:

```bash
git worktree add ../<repo>.worktrees/<slug> -b <branch>
```

Never create a worktree inside the repo or under a tool-managed folder.

## Staging and commits

- Stage files by name. Never run `git add -A`, `git add .` or `git commit -a`.
- A commit holds only the files of the task it belongs to. Leave unrelated changes unstaged and mention them to the user.
- Commit at meaningful milestones: a step that passes its targeted tests, or a coherent unit a reviewer can read alone.
- Write a message that says what changed and why. End it with the attribution lines the session gives, if any.

## Branches and pushing

- On a default branch (`main`, `master`), create a branch before working, unless the project `CLAUDE.md` says otherwise.
- Push only when the user asks. Never force-push a shared branch.

## Personal details

Never put the user's real name or email in git config, a User-Agent string, package metadata or a generated file. Use generic placeholders such as `maintainer@example.com` and a neutral client name.

## Hard rules

- Never use `git add -A`, `git add .` or `git commit -a`.
- Never commit files that belong to a different task.
- Never push without being asked.
- Never create a worktree inside the repo.
- Never write the user's real name or email into config or metadata.

## Provenance and maintenance

Updated: 2026-11-13.

Re-verification commands:
```bash
git worktree list
git status --short
```
