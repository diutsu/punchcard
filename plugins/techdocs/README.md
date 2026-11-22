# techdocs

Write good technical docs from ideas, and plan those ideas into viable designs, in one strict writing style.

## Install

```bash
/plugin install techdocs --marketplace diutsu/punchcard
```

| Skill | Use it to |
| --- | --- |
| `writing-style` | Apply the one prose style to every doc and report; lint for LLM tells |
| `editorial-review` | Final pass on any doc: lint, critique, edit, reference check |
| `doc-templates` | Start a vision, target architecture, discovery, design doc, PRD, research doc or ADR |
| `horizon-review` | Check a planning doc statement by statement against the Planning Horizons model |
| `review-comment-coach` | Keep review comments at the document's horizon |
| `docs-management` | Place docs in the Diataxis layout and enforce the frontmatter contract |
| `handle-comments` | Resolve `[COMMENT]` markers left in docs |
| `external-research` | Build a sourced research doc with checked quotes |

## Sources

The horizon model and the vision, target architecture and discovery templates were copied on 2026-11-11 from the Planning Horizons paper (summary in `skills/doc-templates/references/model.md`). The paper wins where they disagree. The LLM-tells catalogue paraphrases Wikipedia, "Signs of AI writing".

## Open items

- Open terminology questions from the paper: "span" vs "distance", and whether the worked constraint says "no remote calls" or "never calls the pricing service". The templates use "span" and "never calls the pricing service".
- Quarter-level plans and changelogs belong to other plugins; no template here.
