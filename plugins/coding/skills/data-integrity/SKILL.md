---
name: data-integrity
tier: reference
description: >
  Raw-versus-derived data discipline: classify every store as RAW, DERIVED or
  CACHE, never destroy or patch raw data, wipe and recompute derived data when
  logic changes, back up before destructive operations, never show invented
  data, and audit computed numbers against independent ground truth. Load for
  ingestion, importers, migrations, recalculations, schema changes, a new data
  source, or a computed number that disagrees with its source. Do NOT load for
  UI loading and error states (see frontend-ui), for test-gate execution (see
  validation-and-qa), or for choosing an external data provider (see
  external-research).
trigger: /data-integrity
---

# /data-integrity

Raw data is a fossil record. Derived data is a cache you may burn down and rebuild. Confusing them corrupts history silently. Every task that touches ingestion, migration or recomputation starts by classifying the store.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Rendering loading, error and empty states | `frontend-ui` |
| Test-gate execution and stub rules | `validation-and-qa` |
| Choosing or adopting an external data provider | `external-research` |
| Explaining why a number is wrong | `forensics` (then return here for the audit) |
| Writing the audit script file | `ops-scripts` |

## 1. Classify before touching anything

Look for an existing classification in the project's architecture or reference docs (`find-docs`) and map it onto these classes. If none exists, classify each store and write it down. A doc may assert a guard ("storage refuses writes that violate the class") that the code does not enforce, so verify the guard exists.

| Class | Definition | Legal | Illegal |
|---|---|---|---|
| `RAW` | Costly or impossible to re-obtain; the record of what was observed. | Append, read, write-new-then-atomic-rename | Overwrite, delete, edit in place |
| `DERIVED` | Recomputable from `RAW` by a deterministic function. | Wipe and recompute wholesale | Patch rows when the calculation changes |
| `CACHE` | Short-lived performance copy. | Drop and rebuild anytime | Treat as authoritative |

## 2. Never destroy or patch raw data

A migration of a `RAW` store writes the new file beside the old one, validates row counts and invariants, then renames atomically. It never deletes the old file until the new one is proven. When calculation logic changes, purge the affected `DERIVED` data and rerun the pipeline from `RAW`. An `UPDATE` that patches derived rows is a violation even when the numbers come out right: nobody can then tell a patched row from a computed one.

## 3. Back up before any destructive operation

Before a migration or bulk correction on real data, run `cp <store> <store>.bak-<reason>`. Keep one snapshot per correction, named for what it preceded, until the migration is proven safe.

## 4. Never show invented data

A failed fetch, missing value or unimplemented path renders as unavailable, never as a fabricated number, guessed default or silent green light. A stub that must ship returns an empty or unavailable result and says so. Rendering rules live in `frontend-ui`.

## 5. Audit procedure

Use this when a computed number is suspect, before trusting a new calculation or migration, or after an importer runs. An audit reports; it never fixes.

1. Identify the raw source and the derived output for the claim. If no independent raw source exists, say so: a number cannot be audited against itself.
2. Read both with read-only queries (`sqlite3`, `duckdb`, checksums, `grep` or `wc -l` on exports, direct file reads). Open stores in read-only mode. Make no external call; real personal and financial data stays on the machine.
3. Reconcile the specific claim and its neighbours (adjacent rows, same instrument, same date range) field by field.
4. Report every discrepancy with the record, the expected value, the actual value and the exact query. Report "reconciled clean" only after seeing the values this session.
5. Treat a failed read or parse as a failure, never as a pass.
6. Hand the finding to `forensics` or `do-work`. Name a fix if you see one; do not apply it.

```text
CLAIM AUDITED: <number or behaviour>
EXPECTED (raw):  <file:line | query> -> <value>   [fact | inference]
ACTUAL (derived): <store, exact query> -> <value>  [fact | inference]
DISCREPANCIES: <record, expected X, got Y, evidence> | none found
NOT CHECKED: <scope boundary>
```

A repeatable audit is a standalone script that exits non-zero on any discrepancy or read failure. Where it lives and how it is written follows `ops-scripts`. An importer or fetcher that exits 0 on partial or total failure is broken: check the exit code on error paths.

## 6. Checklist for a new data source

1. Classify each table or file it writes.
2. Set the immutability class of each (append-only, mergeable, overwriteable, reference, or the project's own scheme) and record it in the project docs, not only in writer code.
3. Name the independent reconciliation source and how often it is checked, before trusting the first number.
4. Write the audit script (section 5) so it exits non-zero on any discrepancy or parse failure.
5. Document classification and reconciliation source in the docs (`docs-management`).
6. Confirm failure paths return unavailable, not zeros.

## Hard rules

- Never overwrite, delete or edit in place a `RAW` store.
- Never patch `DERIVED` rows for new logic; wipe and recompute.
- Always create `<store>.bak-<reason>` before a destructive migration or correction.
- Never fix during an audit.
- Never let an importer or audit exit 0 when inputs fail to parse or records drop.
- Never show invented data.
- Never send real financial or personal data to an external API, MCP service or AI service.

## Provenance and maintenance

Updated 2026-11-13. Check commands:

```bash
grep -n "bak-<reason>" plugins/coding/skills/data-integrity/SKILL.md
grep -n "ops-scripts" plugins/coding/skills/data-integrity/SKILL.md
```
