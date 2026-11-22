# plugins/

One folder per plugin: `punchcard`, `coding`, `techdocs`, `project-management`, and `wip`. To add your own:

```text
plugins/<name>/
├── plugin.json
├── .claude-plugin/plugin.json
├── .codex-plugin/plugin.json
└── skills/<skill-name>/SKILL.md
```

A plugin may also ship `agents/`, `hooks/`, `hooks.json`, `rules/AGENTS.md`, `output-styles/` and `scripts/`, as `coding` and `punchcard` do. Register the plugin in `.claude-plugin/marketplace.json` and `.agents/plugins/marketplace.json`.

Skills under any `plugins/*/skills/` are also picked up by `npx skills add`. Draft skills go in `wip` until promoted; see `docs/how-to/promote-a-skill.md`.
