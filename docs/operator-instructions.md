---
type: requirement
state: wip
created: 2026-10-11
updated: 2026-10-11
cross-file-references: [docs/usage.md, docs/tasks.md]
---
# Operator Instructions — Frank
Worklist of actions that only the human operator can execute or decide.

---

## Run queue

### `META-01` — Initialize Git repository and push to `https://github.com/diutsu/Frank`

- [ ] `git init && git add . && git commit -m "init: scaffold Frank skills, doc-templates, and meta docs"`
      Expect: exits 0, working tree clean.
- [ ] `git branch -M main && git remote add origin https://github.com/diutsu/Frank.git && git push -u origin main`
      Expect: pushes `main` to `origin/main`.

Output:
```
```

---

## Decision gates

_No pending decision gates._

