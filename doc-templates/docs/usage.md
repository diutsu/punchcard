---
type: requirement
state: done
created: 2026-10-11
updated: 2026-10-11
cross-file-references: [docs/architecture.md, docs/operator-instructions.md]
---
# Usage & Operations Manual
Permanent operator manual: installation, configuration, CLI command reference, background job/queue management, and reusable operational runbooks.

> **Boundary with `operator-instructions.md`:** Reusable procedures ("how to start/stop long-running jobs", "how to schedule work via the queue", "how to run a backup") live **here**. `operator-instructions.md` holds only one-off pending actions and decision gates that are deleted once executed.

## TOC
- [Installation & environment](#installation--environment)
- [Configuration](#configuration)
- [CLI reference](#cli-reference)
- [Reusable operational runbooks](#reusable-operational-runbooks)

---

## Installation & environment

- **Setup:** `<exact setup command>`
- **Verification gate:** `<exact verify command>`

---

## Configuration

- **Committed defaults:** `<config.default.yaml / .env.example>`
- **Local private overrides (gitignored):** `<config.yaml / .env>` — never log or print values from this layer.

---

## CLI reference

| Command | Description |
|---|---|
| `<cli-entry-point> <subcommand>` | `<what it does, default flags, output semantics>` |

---

## Reusable operational runbooks

### Starting, stopping, and inspecting long-running jobs
- **Check status:** `<command>`
- **Start / resume safely:** `<command>`
- **Stop cleanly (`SIGTERM`):** `<command>`
