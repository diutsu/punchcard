---
type: requirement
state: wip
created: 2026-10-11
updated: 2026-10-26
cross-file-references: [docs/usage.md, docs/tasks.md]
---
# Operator Instructions — punchcard
Worklist of actions that only the human operator can execute or decide.

---

## Run queue

### `META-02` — Recover the `ctask` source and publish it

`https://github.com/diutsu/ctask` is empty, so every `uvx --from git+https://github.com/diutsu/ctask` command in `README.md`, `docs/usage.md`, and `plugins/local-project-manager/skills/do-task/SKILL.md` fails.

- [ ] Locate the `ctask` source (another project checkout, a `uv tool` install, or a backup).
- [ ] Push it to `https://github.com/diutsu/ctask` (or vendor it into `punchcard/ctask/`).
- [ ] `uv tool install git+https://github.com/diutsu/ctask && ctask validate`
      Expect: exits 0 from the `punchcard` repo root.

Output:
```
```

---

## Decision gates

_No pending decision gates._

