---
type: how-to
state: done
created: 2026-11-13
updated: 2026-11-13
cross-file-references: [docs/reference/skill-contract.md, plugins/punchcard/skills/skill-maintenance/SKILL.md, plugins/README.md]
---

# Add a skill

Add a new skill to an existing plugin, or start a new plugin.

1. Check that no sibling skill already owns the territory. `skill-maintenance` lists the territory of each plugin.
2. Create `plugins/<plugin>/skills/<name>/SKILL.md` with the frontmatter and sections in [skill-contract.md](../reference/skill-contract.md). The folder name equals `name`.
3. Put long lists and templates in `references/` inside the skill folder. Link to them with `${CLAUDE_SKILL_DIR}/...`.
4. Add the skill to the table in the plugin README, if it has one, and to the root `README.md`.
5. Run the verification commands in the contract. Each prints nothing when the skill complies.

For a new plugin, create `plugins/<name>/.claude-plugin/plugin.json` and a `skills/` folder, then register it in `.claude-plugin/marketplace.json` with `"source": "./plugins/<name>"`.

Commit, push, then run `/plugin marketplace update punchcard`.

To let Claude draft the skill from repeated work instead, run `skill-reviewer`. It writes drafts into `wip`; see [promote-a-skill.md](promote-a-skill.md).
