---
name: operate-and-diagnose
tier: leaf
description: >
  Running and measuring a live system — operations without eyeballing. Load
  when the user says "run it", "why is it doing X", "check if it ran", "is it
  faster/bigger/slower now", "did the deploy take effect", or asks about a
  scheduler, daemon, queue, or server that is already running. Every answer
  must come from a direct query or measurement script, never a guess or UI
  glance. Do NOT use for writing or executing a task plan (see do-task), for
  triaging a code bug's root cause (see debugging-method), or for queuing
  human-only commands (see operator-instructions).
trigger: /operate-and-diagnose
---

# /operate-and-diagnose

Operating a system means **querying and measuring it directly**. Every claim in your output must cite a number, a log line, or an exit code — never `"it looks fine"`.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Driving a task through plan $\rightarrow$ execute $\rightarrow$ commit | `do-task` |
| Handing off commands that only the human operator can run | `operator-instructions` |
| Root-causing a broken code path | `debugging-method` |
| Reconciling raw vs. derived data stores | `data-integrity` |

## 1. Discover the entry point before running anything

Never guess a CLI command. Discover it in this order:
1. Project `CLAUDE.md` (`Environment & Gate Commands`).
2. `package.json` (`scripts`), `pyproject.toml` (`[project.scripts]`), or `Makefile`.
3. `docs/usage.md` (the permanent operator manual and CLI reference).

## 2. Check the trigger layer before the application code

When diagnosing `"why didn't X run?"`, check what is supposed to invoke $X$ before reading the code that implements $X$:
- **Systemd units/timers:** Check whether unit files are generated from config. Inspect `systemctl [--user] status <unit>`, `systemctl [--user] list-timers`, and `journalctl [-u <unit>]`. Prefer the project's own schedule/status CLI subcommand if one exists.
- **Task queues:** A queue worker is a separate process from the jobs it drains. Query the queue's status command or backing store directly (pending/running/failed counts) rather than inferring health from a web UI.
- **Cron / background runners:** Check the scheduler table before assuming application logic failed.

## 3. Measure, don't eyeball

- **Performance / size questions:** Run a measurement query or one-off script and report the exact numbers with units and sample size.
- **State questions (`"how many rows"`, `"did the write land"`):** Query the backing store (`sqlite3`, `duckdb`, `psql`, or the project's own repository helper) after resolving the live path from the effective config — never trust a cached UI render.

## 4. Two-channel logging & signal discipline

| Channel | What belongs there | Mechanism |
|---|---|---|
| **Interface output** | The deliverable the command produces (tables, JSON output, reports) | `stdout` (`print` / `console.log`) |
| **Execution messages** | Progress, row counts, timings, warnings, errors | Structured logger (`logging` / `stderr`) |

- **Signal handling:** Long-running loops and workers must trap `SIGINT` and `SIGTERM` explicitly on a single handler, release any claimed locks/queue items cleanly, log a warning, and exit deliberately.

## 5. Privacy wall on layered configs

Projects commonly merge a **committed default config** (`config.default.yaml`, `.env.example`) with a **gitignored private layer** (`config.yaml`, `.env`). **Never print, log, or paste values read from the gitignored layer.**

## 6. Verify operational changes on the live surface

Green unit tests do not prove a daemon reloaded its config or a systemd timer reinstalled. After any operational change:
1. Reinstall or restart the target service/worker.
2. Trigger or observe one real cycle.
3. Query the store or logs (§3–§4) to confirm the new behavior occurred.

## Hard rules

- Never answer `"why didn't it run"` from application code alone — check the trigger layer (timer/queue/daemon) first.
- Never answer `"is it faster/bigger"` without a measured number from this session.
- Never trust a UI rendering of state over a direct store query.
- Never print, log, or transmit values from a gitignored config or `.env` file.
- Never dump live operational status essays into `docs/operator-instructions.md` — live session snapshots belong in `docs/next-session-prompt.md` ($\le 40$ lines), and reusable runbooks belong in `docs/usage.md`.

## Provenance and maintenance

Updated: 2026-10-11 (v2: added `tier: leaf`, aligned operational doc boundaries with `docs/usage.md`, `docs/next-session-prompt.md`, and `docs/operator-instructions.md`).

Re-verification commands:
```bash
ls doc-templates/docs/usage.md doc-templates/docs/operator-instructions.md
```
