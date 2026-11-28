# Brief: external builder handoff

Use when another coding tool builds in batches and you validate each batch, then write the next one. You are the validator and planner. The other tool is the builder. It starts each batch with no memory of yours.

## Part 1: validate the finished batch

```
BATCH: <batch id>
BUILDER OUTPUT: <branch and commit range>
BATCH BRIEF: <path to the brief you gave the builder>
VERIFY COMMAND: <the project's verify command, resolved through project-map>
```

1. Read the batch brief, then the diff. Do not read the builder's own summary first.
2. Run the verify command and show the output. A batch without a green gate is not done.
3. Check every acceptance criterion in the batch brief against the diff.
4. Look for stubs, placeholders, fabricated values and out-of-scope edits.
5. Have the diff reviewed by a clean reviewer that did not write the brief or the code (see `agent-brief` reviewer template).

Validation report (exact):

```
BATCH: <id>
GATE: <command> -> exit <N>
CRITERIA: <each criterion: met | not met | unverified - evidence>
LANDED: <on the integration branch | not merged: branch and commit range>
DEFECTS: <location - what - required fix; or none>
STUBS OR FABRICATED VALUES: <list, or none>
OUT OF SCOPE EDITS: <list, or none>
VERDICT: ACCEPT | ACCEPT WITH FIXES | REJECT
```

After the report, move each task in the batch through the `tracker` gates, landing check included. ACCEPT is a verdict on the batch, not a task state. Merge only as `repo-infra` allows.

## Part 2: write the next batch

The next brief must stand alone. Fill every field.

```
BATCH: <next id>
GOAL: <one sentence>
FIXES FROM LAST BATCH: <defects the builder must fix first, or none>
WHAT TO CHANGE: <files, functions, behaviour>
DONE WHEN: <concrete acceptance criteria>
TEST COMMAND: <exact command>
READ FIRST: <paths>
BRANCH: <branch the builder commits to>
TASKS: <task ids>; report on them, never change their state
OUT OF SCOPE: <what not to touch>
REPORT FORMAT: FILES CHANGED / TESTS RUN / SUMMARY / ISSUES SPOTTED
```

## Rules

- Keep batches small enough that one review covers the whole diff.
- Never carry the previous batch's reasoning into the next brief. State only the current state of the code and the goal.
- Never write a brief that depends on the builder remembering an earlier batch.
- Pass paths, never pasted contents.
- The validator owns task state. The builder never moves a task, whatever its own installed skills say.
