# plugins/

One folder per plugin. To add your own:

```text
plugins/<name>/
├── .claude-plugin/plugin.json
└── skills/<skill-name>/SKILL.md
```

Then register it in `.claude-plugin/marketplace.json` with `"source": "./plugins/<name>"`.
Skills under any `plugins/*/skills/` are also picked up by `npx skills add`.
