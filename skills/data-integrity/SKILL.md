---
name: data-integrity
tier: reference
description: >
  REFERENCE, not a workflow — the raw-vs-derived data discipline: classify
  every data store (RAW, DERIVED, CACHE), never destroy or patch raw/source
  data in place, wipe and recompute derived data from raw when logic changes,
  and validate computed numbers against independent ground truth via a
  standalone audit script. Trigger whenever a task touches ingestion,
  importers, migrations, recalculations, schema changes, or data discrepancies.
  Do NOT use for pure UI rendering states (see ui-ux-discipline) or general
  test-gate execution (see validation-and-qa).
trigger: /data-integrity
---

# /data-integrity

**Raw data is an immutable fossil record. Derived data is a cache you can burn down and rebuild.** Confusing the two corrupts historical state silently. Every task that touches ingestion, schema migration, or recalculation starts by classifying the store it touches.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Pure UI state rendering (`loading`/`error`/`empty`/`data-unavailable`) | `ui-ux-discipline` |
| General test-gate execution and `_stub_` rules | `validation-and-qa` |
| Evaluating whether to adopt an external data provider | `external-research` |

## 1. Classify every store before writing code

Check `docs/architecture.md` and `docs/requirements/storage.md` (or equivalent) for each table/file's immutability class and map it to one of these three categories:

| Class | Definition | Legal operations | Illegal operations |
|---|---|---|---|
| **`RAW` / `SOURCE`** | Costly or impossible to re-obtain; canonical record of what was observed. | Append, read, write-new-then-atomic-rename | Overwrite in place, delete rows, patch values |
| **`DERIVED`** | Recomputable from `RAW` by a deterministic function (features, rollups, signals). | Wipe + recompute wholesale from `RAW` | In-place `UPDATE`/patch when calculation logic changes |
| **`CACHE`** | Short-lived performance copy recomputable anytime. | Drop/rebuild anytime | Treat as authoritative source of truth |

## 2. Never destroy or patch `RAW` in place

- **Atomic file migrations only:** When migrating a `RAW` store's physical format, write the new file alongside the old one, validate row counts and invariants, atomic-rename into place, and keep a `<store>.bak-<reason>` snapshot until proven safe.
- **Wipe + recompute `DERIVED` on logic change:** When a calculation or transform changes, purge the affected `DERIVED` table/partition and recompute from `RAW`. Never write an ad-hoc `UPDATE` query to patch derived rows in place.

## 3. Reconciliation against independent ground truth

A computed dataset is untrusted until checked against an independent ground truth (e.g., raw wire dump vs. parsed table, external statement vs. imported ledger, known-answer fixture vs. rollup):
- Build a **standalone reconciliation/audit check** that compares ground truth against derived output, reports discrepancies with record-level evidence, and **exits non-zero** on any mismatch or read/parse failure.
- **Silent drop = bug:** A fetcher or importer that exits `0` on partial or total failure is broken. Verify exit codes on error paths.

## 4. Checklist — adding or modifying a data store

1. Classify the store (`RAW`, `DERIVED`, or `CACHE`) and its immutability class (`append-only`, `static`, `mergeable`, `overwriteable`, `reference`) in `docs/architecture.md` and `docs/requirements/<storage-module>.md`.
2. Snapshot any existing store (`cp <store> <store>.bak-<slug>`) before running a migration.
3. Verify failure modes render or return `data-unavailable` rather than fabricated/default zeros.
4. Run the reconciliation check and paste its exit `0` output (per `validation-and-qa`).

## Hard rules

- Never overwrite, delete, or in-place-edit a `RAW`/`SOURCE` data store.
- Never patch `DERIVED` rows in place when calculation logic changes — wipe and recompute from `RAW`.
- Always create a `<store>.bak-<reason>` backup before running any destructive migration.
- Never allow an importer or audit script to exit `0` when inputs fail to parse or records are silently dropped.
- Document every store's immutability class in `docs/architecture.md` / `docs/requirements/`.

## Provenance and maintenance

Updated: 2026-10-11 (v2: added `tier: reference` and aligned doc paths with `docs/architecture.md` and `docs/requirements/`).

Re-verification commands:
```bash
grep -n 'immutability class' docs/architecture.md
```
