---
name: docs-management
tier: leaf
description: >
  Where a technical doc lives and what it must carry: the Diataxis layout
  (tutorials, how-to, reference, explanation), the investigations, prd and design
  folders, the YAML frontmatter contract, timeless in-place
  edits, and the validation commands. Load when creating, editing, moving or
  auditing any doc under the docs map key. Do NOT load for prose rules (see
  writing-style), doc skeletons (see doc-templates), tasks, plans or logs (see
  project-management), or for resolving the map keys (see project-map).
trigger: /docs-management
---

# /docs-management

Docs follow [Diataxis](https://diataxis.fr): four kinds, each serving a different reader need. Mixing kinds in one doc fails both readers, so each doc has one kind and one folder. Resolve the `docs`, `investigations` and `prd` keys through `project-map`.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Sentence-level style, LLM tells | `writing-style` |
| Starting a doc from a skeleton | `doc-templates` |
| Tasks, plans, done log | `project-management` |
| Milestones | `changelog` |
| Handoff between sessions | `operator-queue` |
| Operator worklist | `operator-queue` |
| Resolving `[COMMENT]` markers | `handle-comments` |
| Checking a whole repo's setup | `project-doctor` |

## Layout and decision table

Under the `docs` key: `tutorials/`, `how-to/`, `reference/`, `explanation/`. Forward-looking docs live at their own keys: `investigations`, `prd` and `design`.

| The doc... | Folder | `type` |
|---|---|---|
| teaches a newcomer by having them do a guided exercise | `tutorials/` | `tutorial` |
| gives steps to reach a goal for someone who already knows the basics | `how-to/` | `how-to` |
| states facts to look up: behaviour contracts, interfaces, config, commands, formulas | `reference/` | `reference` |
| gives background and the why of what exists: architecture, design rationale, ADRs, trade-offs | `explanation/` | `explanation` |
| answers an open question with evidence and a recommendation | `investigations` key | `investigation` |
| states what to build and why, before it exists | `prd` key | `prd` |
| states how something not yet built will be structured: target architecture, design docs | `design` key | `design` |

When a design is built, move its settled behaviour to `reference/` and its rationale to `explanation/`, then delete the design doc.

Quick test: does it inform action or knowledge, and does the reader study or work? Action while studying: tutorial. Action while working: how-to. Knowledge while working: reference. Knowledge while studying: explanation. A doc that needs two answers is two docs; split it and link them.

Reference mirrors the structure of what it describes, stays neutral and complete, and carries no opinions. Explanation may take a perspective and circle its subject. Tutorials and how-to guides carry steps, not theory: link to explanation instead.

Nothing fits? Ask the user through the question interface before inventing a folder.

## Frontmatter contract

Every doc starts with this block, a blank line, `# Title` and a one-line goal:

```markdown
---
type: <tutorial | how-to | reference | explanation | investigation | prd | design>
state: <wip | planned | done | archived>
created: YYYY-MM-DD
updated: YYYY-MM-DD
cross-file-references: [docs/reference/api.md, src/foo/bar.py]
---
```

All five fields are required, in this order.

- `type`: closed set above.
- `state`: `planned` is a stub, `wip` is being written, `done` is complete and maintained (living docs stay `done` while edited), `archived` is superseded or concluded and no longer maintained.
- `created`: set once, never changed. Source: `git log --diff-filter=A --follow --format=%ad --date=short -- <file> | tail -1`.
- `updated`: today's date on every content edit.
- `cross-file-references`: real repo paths the doc relies on or is sibling to. Use `[]` when none; never omit the field, never invent a path.

## Length and names

A doc has no line ceiling. A long doc is fine when its headings let a reader jump to the part they need. Split a doc when it covers two topics, not when it passes a line count. An investigation's verdict block stays at 10 lines or fewer.

File names are lowercase `kebab-case.md`. A leading `_` is reserved for `_index.md`.

## Editing rules

- Edit `reference/` and `explanation/` timelessly and in place: rewrite the section so the doc reads as if the system was always this way. Do not add dated notes, "changed in" narratives or fix-history blocks.
- Keep the rejected alternatives and the derivation in an ADR or an investigation, and leave a one-line blockquote pointer next to the rule that looks counter-intuitive.
- Open an investigation with a verdict block of at most 10 lines: the conclusion, the docs it changed, and the options dropped with one-line reasons.
- Bump `updated` on every content edit: `sed -i "s/^updated:.*/updated: $(date +%Y-%m-%d)/" <file>`.
- Reference docs, not individual code lines; link to modules and files that exist.

## Procedure: add frontmatter to a doc that lacks it

1. Choose `type` from the decision table. If two answers fit, split the doc or ask.
2. Choose `state`: complete and maintained `done`; actively changing `wip`; stub `planned`; superseded or concluded `archived`.
3. Set `created` from the first-commit command above; fall back to an old "Last Change" line or the file's modification time.
4. Set `updated` to the old "Last Change" value if present, else `created`.
5. Set `cross-file-references` to the real paths the body links or names, else `[]`.
6. Insert the block at the top, then a blank line, then the existing title. Delete any old "Last Change" line.
7. Move the file to the folder its `type` names.

## Validation procedure

Callable by `project-doctor`. Run from the repo root, with `DOCS` as the resolved docs root.

```bash
DOCS=docs
grep -rL '^type:' "$DOCS"                                     # docs missing frontmatter
grep -rLE '^type: (tutorial|how-to|reference|explanation|investigation|prd|design)$' "$DOCS"   # invalid type
grep -rn '^Last Change:' "$DOCS"                              # residue of the old convention
find "$DOCS" -name '*[A-Z]*.md'                               # non-kebab-case names
grep -rn '\[COMMENT\]' "$DOCS"                                # unprocessed comments
grep -rnE '^(\*\*Problem\.\*\*|### (Update|Amendment))|(Confirmed|Verified) (on )?20[0-9]{2}' "$DOCS"/reference "$DOCS"/explanation   # fix-history in timeless docs
```

A doc is valid when frontmatter is the first thing in the file, all five fields are present in order, `type` and `state` are in their sets, `created` and `updated` are dates with `updated >= created`, and every listed path exists. Report each failure as `file: problem`.

## Hard rules

- Never put two Diataxis kinds in one doc.
- Never omit a frontmatter field or leave `updated` stale after an edit.
- Never add dated or historical narrative to `reference/` or `explanation/`.
- Never create a doc kind or folder outside this layout without asking the user.
- Never invent a `cross-file-references` entry.

## Provenance and maintenance

Updated: 2026-11-13. Diataxis from https://diataxis.fr (four kinds, compass). Frontmatter contract and the add-frontmatter procedure carry over from the earlier docs-management skill.

Re-verification commands:
```bash
grep -rL '^type:' docs/
sh plugins/techdocs/skills/writing-style/scripts/lint-prose.sh plugins/techdocs/skills/docs-management/SKILL.md
```
