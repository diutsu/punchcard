# Plugins under trial

Statuses: `required`, `trial`, `untested`, `dropped`. Dates are the last review. The install id is `<plugin>@<marketplace>`, read from the repo; `not checked` means nobody has looked yet. An entry that is not a plugin gives its own install and remove commands.

| Name | Repo | Install id | What it does | Status | Last reviewed |
|---|---|---|---|---|---|
| i-have-adhd | ayghri/i-have-adhd | not checked | Output rules for an ADHD reader. Source of the punchcard output style; not installed, tracked for upstream changes. | required | 2026-11-13 |
| one-skill-to-rule-them-all | rebelytics/one-skill-to-rule-them-all | not checked | Task Observer: learns skills from sessions. Heavy; deferred in favour of `skill-reviewer`. | untested | 2026-11-13 |
| anatomy | wheresryan22/anatomy | not checked | Isometric SVG explainers. | untested | 2026-11-13 |
| diagram-design | cathrynlavery/diagram-design | `diagram-design@diagram-design` | HTML pages with inline SVG diagrams. | untested | 2026-11-14 |
| mattpocock skills | mattpocock/skills | not checked | Skill collection. `grilling` adapted here. `wizard` and `chief-of-staff` untested. | untested | 2026-11-13 |
| ui-ux-pro-max-skill | nextlevelbuilder/ui-ux-pro-max-skill | not checked | UI and UX design guidance. | untested | 2026-11-13 |
| agent-skills | vercel-labs/agent-skills | not checked | React composition, React best practices, view transitions, web design guidelines. | untested | 2026-11-13 |
| graphify | Graphify-Labs/graphify | none: a CLI, not a plugin (`uv tool install graphifyy`, then `graphify claude install`; remove with `graphify uninstall`) | Maps code, docs, PDFs and media into a knowledge graph that is queried instead of grepped. Code parsing is local; docs and media use the model. Its installer writes a skill and a hook that fires before Read and Grep calls. Apache-2.0. | untested | 2026-11-14 |
| security-guidance | anthropics/claude-plugins-official | not checked | Security guidance plugin. | untested | 2026-11-13 |
| superpowers | anthropics/claude-plugins-official | not checked | Workflow skill bundle. | untested | 2026-11-13 |
| frontend-design | anthropics/claude-plugins-official | not checked | Frontend design skill. | untested | 2026-11-13 |
| hallmark | Nutlope/hallmark | `hallmark@hallmark` | Page design skill with fifty themes and a browser lint against machine-made design tells; `redesign` and `audit` commands. MIT. Browser checks need Node 18 and `puppeteer-core`. Overlaps `frontend-design` and `ui-ux-pro-max-skill`. | untested | 2026-11-14 |
| lemo-opuscar | lemomo-ai/lemo-opuscar | `lemo-opuscar@lemolab` | Makes short films in code from 99 film styles. On first use it downloads its library to `~/lemo-opuscar`; delete that folder after uninstalling. Licence not identified by GitHub; read `LICENSES/` before use. | untested | 2026-11-14 |
