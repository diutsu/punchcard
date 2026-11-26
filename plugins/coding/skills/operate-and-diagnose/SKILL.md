---
name: operate-and-diagnose
tier: leaf
description: >
  Run and measure a live system without eyeballing. Load when the user says
  "run it", "why is it doing X", "check if it ran", "is it faster or bigger
  now", "did the deploy take effect", or asks about a scheduler, daemon, queue
  or server that is already running. Every answer comes from a direct query or
  measurement script, never a guess or a UI glance. Do NOT load for executing
  a planned change (see do-work), for the root cause of a code bug (see
  forensics), for commands only the human can run (see tracker), or for
  raw-versus-derived reconciliation (see data-integrity).
trigger: /operate-and-diagnose
---

# /operate-and-diagnose

Operate a system by querying and measuring it. Every claim in the output is a number, a log line or an exit code. "It looks fine" is not a claim.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Executing a planned change end to end | `do-work` |
| Commands only the human operator can run | `tracker` |
| Root-causing a broken code path | `forensics` |
| Reconciling raw and derived stores | `data-integrity` |
| Deciding whether work is done | `validation-and-qa` |

## 1. Find the entry point before running anything

Never guess a command. Look, in order, at: the project instructions file (`AGENTS.md`, `CLAUDE.md` or `GEMINI.md` — invocation and environment rules, such as "call the venv binary directly"), the manifest (`package.json` scripts, `pyproject.toml` console scripts, `Makefile`), the project's usage docs found through `project-map`, then the README. Do not invent structure a project lacks, and do not carry one project's layout to another.

## 2. Check the trigger layer before the code

For "why didn't X run", ask what is supposed to invoke X and whether that process is alive.

- Systemd: check whether units are generated from config (then the fix belongs in config). Use `systemctl [--user] status <unit>`, `systemctl [--user] list-timers`, `journalctl -u <unit>`. Prefer the project's own schedule or status command, which reflects its own bookkeeping.
- Queues: a worker is a separate process from the jobs it drains. Query the queue's status command or backing store for pending, running and failed counts.
- Cron: read `crontab -l` and `/etc/cron.d/*` before blaming the script.

## 3. Measure

- Performance and size: write a throwaway script in the session scratchpad, run it, report numbers with units and sample size.
- State ("how many rows", "did the write land"): query the store directly. Resolve the live path from the effective merged config, not from a `find` result, because a stale file from an old layout is easy to mistake for the live one. Use the project's own installed driver, or a native client after `which <tool>`.

## 4. Two output channels

| Channel | Belongs there | Mechanism |
|---|---|---|
| Interface output | The deliverable: tables, reports, JSON | stdout |
| Execution messages | Progress, counts, timings, run ids, warnings, errors | logger on stderr |

Test: "in a scheduled, non-interactive run, would I want this line in the log?" Yes means logger. A missing line in a scheduled run usually means it went to stdout. Long-running loops trap `SIGINT` and `SIGTERM` on one handler, release claimed locks or queue items, log a warning and exit deliberately.

## 5. Config discovery and the private layer

Projects commonly merge a committed defaults file (`config.default.*`, `.env.example`) with a gitignored private file (real values, secrets, personal data). Find the pair and the merge step. A load error naming a missing key means "fill in the config". Never print, log or transmit a value from the private layer, even for debugging. Show the committed defaults file, or redact.

## 6. Drive the real flow after an operational change

A green unit suite does not prove that a daemon reloaded its config, a unit was reinstalled or a worker restarted on the new build. After any change to scheduling, config or a running service:

1. Reinstall or restart the actual unit through the project's real install path.
2. Trigger or wait for one real cycle.
3. Query the store or logs (sections 3 and 4) and confirm the new behaviour happened, not that the process is merely alive.

Do not stop at green tests.

## Hard rules

- Never answer "why didn't it run" from application code alone; check the trigger layer first.
- Never answer "is it faster or bigger" without a number measured this session.
- Never trust a UI rendering of state over a direct store query.
- Never print, log or transmit a value from a gitignored config or env file.
- Never call an operational change verified until the real flow ran and was observed.
- Long-running loops you write or touch handle `SIGINT` and `SIGTERM` explicitly.
- Park live-session status in the task handoff (see `tracker`), and reusable runbooks in the docs (see `docs-management`).

## Provenance and maintenance

Updated: 2026-11-26. Check commands:

```bash
grep -n "private layer" plugins/coding/skills/operate-and-diagnose/SKILL.md
grep -c "" plugins/coding/skills/operate-and-diagnose/SKILL.md
```
