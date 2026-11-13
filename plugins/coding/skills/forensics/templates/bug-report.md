---
type: investigation
state: wip
created: YYYY-MM-DD
updated: YYYY-MM-DD
cross-file-references: []
---
# Bug: `<short title naming the symptom>`

`<One line: what breaks, where.>`

## Environment and versions

- Commit or version: `<hash or tag>`
- OS, runtime and dependency versions: `<exact versions>`
- Configuration that matters: `<keys and values, no secrets>`

## Reproduction

Steps that someone else can run verbatim.

1. `<command or action>`
2. `<command or action>`

Minimal input: `<smallest case that fails>`

## Expected versus actual

Expected:

```text
<exact expected output>
```

Actual:

```text
<exact actual output or error>
```

## Frequency

`<always | N of M runs | only under condition>`

## Root cause

`<Mechanism, with evidence: file:line, command and output. Explain why passing cases did not fail.>`

If not yet established: write "not yet established" and list the hypotheses ruled out, each with its experiment and result.

## Scope of impact

`<Who or what is affected; data touched; since which commit or version.>`

## Workaround

`<Steps, or "none">`

## Suggested fix

`<Direction and the test that would prove it. Fixing goes through do-work.>`
