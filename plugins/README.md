# plugins/

One folder per plugin: `punchcard`, `coding`, `techdocs`, `project-management`, `wip`, and the temporary `local-project-manager`. To add your own:

```text
plugins/<name>/
├── .claude-plugin/plugin.json
└── skills/<skill-name>/SKILL.md
```

A plugin may also ship `agents/`, `hooks/`, `output-styles/` and `scripts/`, as `coding` and `claude` do. Register the plugin in `.claude-plugin/marketplace.json` with `"source": "./plugins/<name>"`.

Skills under any `plugins/*/skills/` are also picked up by `npx skills add`. Draft skills go in `wip` until promoted; see `docs/how-to/promote-a-skill.md`.
