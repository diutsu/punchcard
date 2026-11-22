---
type: how-to
state: done
created: 2026-10-11
updated: 2026-11-22
cross-file-references: [.claude-plugin/marketplace.json, .agents/plugins/marketplace.json, .agents/plugins.json, README.md]
---

# Install punchcard plugins

Add the marketplace and enable the plugins a project needs.

## Claude Code

1. Add the marketplace:

   ```bash
   /plugin marketplace add diutsu/punchcard
   ```

2. Install each plugin you want. `punchcard` is the always-on base; add the others as the project needs them:

   ```bash
   /plugin install punchcard@punchcard
   /plugin install coding@punchcard
   /plugin install techdocs@punchcard
   /plugin install project-management@punchcard
   ```

3. Reload plugins or restart the session.
4. If you installed `project-management`, install its task tool, `ctask`:

   ```bash
   uv tool install git+https://github.com/diutsu/ctask
   ```

5. Add a `## Project map` block to the project's `AGENTS.md` (or `CLAUDE.md` / `GEMINI.md`), or run `project-doctor` to check what is missing. The `tasks` and `verify` keys have no default.
6. Optional: enable the status line by adding the `statusLine` entry shown in `plugins/punchcard/README.md` to `~/.claude/settings.json`. A plugin cannot set it for you.

To pick up later changes, run `/plugin marketplace update punchcard`.

## Antigravity

Each plugin ships a root `plugin.json`, and `punchcard` ships `rules/AGENTS.md` and a root `hooks.json` (`SessionStart`). Copy or symlink the plugin folders you want into `~/.gemini/config/plugins/<name>/`, or inherit `.agents/plugins.json` from `~/.gemini/config/plugins.json`.

## Codex and ChatGPT

`.agents/plugins/marketplace.json` indexes all plugins for Codex. Individual skills also install with `npx skills add https://github.com/diutsu/punchcard --skill <name>`. To paste the always-on response style and session card into `~/.codex/AGENTS.md` or ChatGPT Custom Instructions, run:

```bash
python3 plugins/punchcard/scripts/sync_rules.py --combined
```

## Validate a local checkout

```bash
python3 plugins/punchcard/scripts/sync_rules.py --check
claude plugin validate .
grep -L '^name:' plugins/*/skills/*/SKILL.md
grep -rL '^type:' docs/
```

The last two commands print nothing when every skill and doc has its frontmatter.
