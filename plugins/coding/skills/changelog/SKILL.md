---
name: changelog
tier: leaf
description: >
  Keep the changelog: one Keep a Changelog line per user-visible change or
  milestone, under Unreleased. Load when a step adds, changes, fixes or removes
  something users see, and before closing such a task. Do NOT load for other
  docs (writing-style, docs-management) or release tagging.
trigger: /changelog
---

# /changelog

The file at the `changelog` key of the project map (see `project-map`) records what users and integrators can see change. Write each line when the change lands, not at release time.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Prose style and doc templates | `writing-style`, `doc-templates` |
| Where docs live and their frontmatter | `docs-management` |
| Internal refactors with no visible effect | no entry needed |

## Shape

Follow Keep a Changelog. Keep one `Unreleased` heading at the top. Under it, use only the groups that have entries:

- **Added** for new features.
- **Changed** for altered behaviour.
- **Fixed** for bug fixes.
- **Removed** for deleted features.

Add `Deprecated` or `Security` only when a change calls for it. Write one line per change, in the active voice, from the user's point of view: what they can now do or what behaves differently. Skip implementation detail.

A project milestone is also a changelog line: a major product decision, a feature shipping, a real operational event. Routine task progress belongs to the task tool (via `tracker`) and to git history.

## Procedure

1. Resolve the `changelog` key. Create the file with an `Unreleased` heading if it does not exist.
2. For each user-visible change in the step, add one line under the right group, as soon as the change lands.
3. Before closing the task, compare the entries with the diff. Add a line for any visible change that has none. Remove a line for work that did not ship.
4. Leave released sections alone. A correction to a released entry goes under `Unreleased` as a `Fixed` or `Changed` line.

## Hard rules

- Never put a task ID, commit hash or file path in an entry.

## Provenance and maintenance

Updated: 2026-11-27.

Re-verification commands:
```bash
grep -n "^## \[\?Unreleased" CHANGELOG.md
```
