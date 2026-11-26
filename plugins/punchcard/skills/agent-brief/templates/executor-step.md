# Brief: executor step

Tier: mid-tier for code and test loops; cheapest for trivial contained edits.

```
WHAT TO CHANGE: <files, functions, behaviour>
DONE WHEN: <concrete acceptance criteria>
TEST COMMAND: <the exact command to run>
OUT OF SCOPE: <what not to touch>
READ FIRST: <paths: the files to modify and their direct dependencies>
PLAN: <plan file path and step number>
TASK ID: <optional, for context only>
```

## Rules for the agent

- If any of WHAT TO CHANGE, DONE WHEN or TEST COMMAND is missing, stop and report that instead of guessing.
- Read the files you will modify and their direct dependencies. Do not explore the wider repo. Match existing patterns.
- Make the smallest change that meets the criteria. No refactors, no cleanup, no extras.
- Run exactly the given test command. Do not run the full suite or repo-wide checks.
- If it fails, fix and rerun. Never report success without seeing exit 0.
- If the plan proves wrong (missing file, false assumption), stop and report it under ISSUES SPOTTED. Do not improvise a different approach.
- Never ship a stub or placeholder as the real implementation. If you cannot meet the criteria, say so and stop.
- A previously passing test that now fails because of your change is a regression. Fix it before reporting.
- Do not edit files outside the described scope.

## Report format (exact)

```
FILES CHANGED:
- path/to/file

TESTS RUN: <exact command> -> exit <N> (<summary, e.g. "12 passed">)

SUMMARY: <one sentence: what changed and why>
ISSUES SPOTTED:
- <file> -> <thing noticed outside scope, not fixed>
- (or: none)
```
