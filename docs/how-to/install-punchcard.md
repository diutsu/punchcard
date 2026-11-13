---
type: how-to
state: done
created: 2026-10-11
updated: 2026-11-13
cross-file-references: [.claude-plugin/marketplace.json, README.md]
---

# Install punchcard plugins

Add the marketplace to Claude Code and enable the plugins a project needs.

1. Add the marketplace:

   ```bash
   /plugin marketplace add diutsu/punchcard
   ```

2. Install each plugin you want. `claude` is the always-on base; add the others as the project needs them:

   ```bash
   /plugin install claude@punchcard
   /plugin install coding@punchcard
   /plugin install techdocs@punchcard
   /plugin install project-management@punchcard
   ```

3. Reload plugins or restart the session.
4. If you installed `project-management`, install its task tool, `ctask`:

   ```bash
   uv tool install git+https://github.com/diutsu/ctask
   ```

5. Add a `## Project map` block to the project's `CLAUDE.md`, or run `project-doctor` to check what is missing. The `tasks` and `verify` keys have no default.
6. Optional: enable the status line by adding the `statusLine` entry shown in `plugins/claude/README.md` to `~/.claude/settings.json`. A plugin cannot set it for you.

To install a single skill without the plugin system, run `npx skills add https://github.com/diutsu/punchcard --skill <name>`.

To pick up later changes, run `/plugin marketplace update punchcard`.

## Validate a local checkout

```bash
claude plugin validate .
grep -L '^name:' plugins/*/skills/*/SKILL.md
grep -rL '^type:' docs/
```

The last two commands print nothing when every skill and doc has its frontmatter.
