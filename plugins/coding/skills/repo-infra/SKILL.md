---
name: repo-infra
tier: leaf
description: >
  Git and repo conventions: worktrees, explicit staging, scoped commits,
  pushing, branching, no personal details in metadata. Load before creating a
  worktree, staging, committing, pushing or setting package metadata. Do NOT
  load for scripts (ops-scripts), the loop (do-work) or the changelog.
trigger: /repo-infra
---

# /repo-infra

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Script placement and headers | `ops-scripts` |
| The work loop and its gates | `do-work` |
| Changelog entries | `changelog` |
| When a task may close after a merge | `tracker` (Landing) |
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

- On a default branch (`main`, `master`), create a branch before working, unless the project instructions file (`AGENTS.md`, `CLAUDE.md` or `GEMINI.md`) says otherwise.
- Push only when the user asks. Never force-push a shared branch.

## Landing a branch

- Merge a branch into the integration branch (defined in `tracker`) only when the project instructions file or the user allows it, the same as pushing. Without that, leave the branch unmerged and report its name and commit range.
- Check that a commit is on the integration branch with `git merge-base --is-ancestor <commit> <integration-branch>` (exit 0 means it is).

## Personal details

Where a name or email is needed in git config, a User-Agent string, package metadata or a generated file, use generic placeholders such as `maintainer@example.com` and a neutral client name.

## Hard rules

- Never write the user's real name or email into config or metadata.

## Provenance and maintenance

Updated: 2026-11-28.

Re-verification commands:
```bash
git worktree list
git status --short
```
