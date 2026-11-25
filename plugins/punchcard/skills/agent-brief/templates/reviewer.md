# Brief: reviewer

Tier: mid-tier; one tier up when the change crosses module boundaries. Use the `reviewer` agent. Scoring dimensions, quick-fix limits and delta rules live in `review-rubric`; this brief only hands over the artifact.

```
REVIEW: plan | implementation
ARTIFACT: <task id with the plan> | <git diff range, e.g. <base>..HEAD>
ACCEPTANCE CRITERIA: <path or list>
CONVENTIONS: <paths to the project AGENTS.md (or CLAUDE.md) and architecture docs>
TEST EVIDENCE: <command, exit code, and report path, or "none provided">
```

## Rules for the brief

- Pass paths and a diff range. Do not paste file contents and do not include the author's reasoning or summary.
- The reviewer must not be the author of the artifact. If you cannot confirm that, the review has not happened.
- Judge the tests from the evidence provided. The reviewer reruns targeted tests only when no evidence was given, when it does not match the diff, or when something looks wrong. If a result cannot be verified, the reviewer says so and never assumes clean.
- Re-reviews after fixes go to the same reviewer as a delta review over the changed parts only.

## Verdict format (exact)

```
ISSUES:
1. [blocking|major|minor] <location> - <why it matters> - <concrete fix>
(or: none)

DIMENSION SCORES:
<dimension>: N/10

FIXES APPLIED: <each quick fix, location and one line; or none>

FINAL SCORE: N (= minimum dimension; capped at 6 if any blocking issue)
VERDICT: PASS | FAIL
```

On a delta review, prefix the verdict with `RESOLVED:` and `STILL OPEN:` lists for the earlier issues.
