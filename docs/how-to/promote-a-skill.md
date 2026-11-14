---
type: how-to
state: done
created: 2026-11-13
updated: 2026-11-13
cross-file-references: [plugins/punchcard/skills/skill-maintenance/SKILL.md, plugins/wip, docs/reference/skill-contract.md]
---

# Promote a skill from `wip`

Move an approved draft from the `wip` plugin into the plugin that owns its territory.

1. Read the draft and decide with the user whether to keep it. A draft that a sibling already covers is deleted instead.
2. Pick the owning plugin from the territory list in `skill-maintenance`.
3. Move the folder:

   ```bash
   git mv plugins/wip/skills/<name> plugins/<plugin>/skills/<name>
   ```

4. Check it against [skill-contract.md](../reference/skill-contract.md). Remove any private detail from the evidence block that slipped in from a transcript.
5. Add the skill to the root `README.md` table.
6. Run the verification commands in the contract.
7. Confirm no copy remains under `plugins/wip/skills/`.
