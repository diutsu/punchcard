---
name: codebase-search
tier: leaf
description: >
  Read this repo's own code, docs, task history and git history to answer "how
  does X work here", with file:line citations and fact-versus-inference marked
  on every claim. Load for onboarding to a module, recovering architecture,
  reconnaissance before planning or changing code, and "audit docs vs code".
  Do NOT load to explain a specific failure (see forensics), to prove a change
  made something better (see validate-run-results), to judge a library outside
  the repo (see external-research), or to assess a whole project for
  maintainability (see project-evaluation, which uses this skill for reading).
trigger: /codebase-search
---

# /codebase-search

Establish what exists before anyone writes code or a plan. This skill reads and reports. It never edits code or docs.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| A failure, bug or surprising behaviour needs a cause | `forensics` |
| A change must be shown to improve something | `validate-run-results` |
| Judging a library, API or vendor outside the repo | `external-research` |
| Whole-project maintainability assessment | `project-evaluation` |
| Turning findings into a plan | `plan` |
| Auditing doc frontmatter or folder layout | `docs-management` |

## Read order

Stop as soon as the evidence answers the question.

1. The project `CLAUDE.md`: stage, gate commands, non-negotiables, and the project map (`project-map`).
2. Task history through `backlog`: open and closed tasks for the module. Known gaps live there, so the code may carry no hint of them.
3. Docs located through `find-docs`: architecture, reference, explanation, and the `investigations` key (verdict section first).
4. The code, last, compared against what steps 2 and 3 claim.

Discover test and build commands from the manifest (`package.json`, `pyproject.toml`, `Makefile`). Never reuse another project's commands.

## Git archaeology

Run from the repo root. Churn and commit messages are signals, not verdicts.

```bash
# Churn hotspots: files touched most often
git log --format= --name-only | sort | uniq -c | sort -rn | head -30

# Reverts: approaches tried and undone
git log --oneline --grep="Revert" -i

# Interrupted in-flight step commits (wip convention)
git log --oneline --grep="^wip(" -i | head -20

# Who last changed a line, and why
git blame -L <start>,<end> -- <file>
git log -S"<symbol>" --oneline -- <file>

# Worktrees and branches that may hold unmerged work
git worktree list
git branch -a
```

Check reverts and `investigations` before proposing something that may have been tried already.

## Doc-versus-code drift

For each doc claim about current behaviour, find the implementing code and give a verdict.

| Verdict | Meaning |
|---|---|
| `FRESH` | The claim matches the code. |
| `STALE` | The doc describes something renamed, removed or superseded, and does no active harm. |
| `CONTRADICTED` | The doc asserts the opposite of the code. Resolve first. |

Every verdict cites `file:line` on both sides. A verdict without both citations is an opinion.

## Flag wins too

Correct, load-bearing, non-obvious code with no doc coverage is a finding. Name it as `WIN` and propose where it should be documented (through `docs-management`). A report that lists only rot reads as fault-finding and gets skimmed.

## Output

One dense report, readable without the raw files. Tag every claim `fact` (read at a cited `file:line`), `inference` (reasoned from evidence), or `guess`. Delegate the reading to a sub-agent with `agent-brief` when the volume warrants it, and take back only the report.

```text
RECON REPORT: <question or module>

SOURCES READ: <in order>

FINDINGS:
1. [FRESH|STALE|CONTRADICTED|WIN] <claim>
   doc: <path:line>   code: <path:line>
   basis: fact | inference | guess
   matters because: <one line>

WHAT I DID NOT CHECK: <scope boundaries, unread areas, unverifiable items>
```

## Hard rules

- Cite `file:line` for every claim; cite both sides of every drift verdict.
- Tag every claim fact, inference or guess. Never present an inference as a fact.
- Read task history before the code for any module.
- Never modify code or docs. Report, then hand off to `plan`, `do-work` or `docs-management`.
- Always end with what you did not check.

## Provenance and maintenance

Updated 2026-11-13. Check commands:

```bash
git log --oneline -1
grep -n "^## Hard rules" plugins/coding/skills/codebase-search/SKILL.md
```
