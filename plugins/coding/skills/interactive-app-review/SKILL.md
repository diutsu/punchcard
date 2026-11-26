---
name: interactive-app-review
tier: workflow
description: >
  Live UX review of a running app: a Playwright run through a real user journey,
  then a fresh-eyes critique; fixes nothing. Load for "review the app", "audit
  the UX", "run the whole flow", or after a rough demo. Do NOT load for UI code
  without running it, a diff (review-rubric) or the fixes (do-work).
trigger: /interactive-app-review
---

# /interactive-app-review

Two phases, always both, in order. Phase 1 establishes what the app does. Phase 2 turns that into a critique a build pass can act on. A clean Phase 1 (no console errors, everything works) does not excuse skipping Phase 2: a spotless exploration can sit under a poor experience, and only Phase 2 shows why.

Read `./references/defect-classes.md` in full before Phase 1 and again before Phase 2. Check each of its ten classes by name.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Rules for building a view | `frontend-ui` |
| Reviewing a diff or a plan | `review-rubric` |
| Implementing the findings | `do-work` |
| Root-causing a finding that needs investigation | `forensics` |
| Checks only a physical Android device shows | `device-qa` |

## Phase 1: automated exploration

**Setup.** Add `playwright` as a dev dependency if the project lacks it, with chromium only. Build for production with no dev-only overrides, and serve the production build, so the review sees what a visitor gets. Confirm the server responds before scripting the run.

**Diagnostics first.** Register console, page-error and failed-request listeners before the first navigation and log them for the whole run. Any console error, page error or failed request mid-journey is a finding.

**Journey.** Script a realistic first-time user path covering at least:

1. A fresh load with cleared storage.
2. Entering the core data in the order a real user would.
3. Opening and closing every expandable element, then reopening each after closing.
4. Filling every meaningful section, including any compare or decision flow.
5. Any advanced or settings area.
6. Clearing data back toward empty, to confirm the reveal logic works both ways.
7. A hard reload with real data already in storage. This is the highest-value step; do not rush it.
8. Every theme or mode the app supports, with data populated.
9. A mobile viewport with data populated, rechecking persistent elements for overlap with content while scrolling.

**Screenshots.**
- Default to full-page shots.
- Wait at least 300 ms after a chart section appears, and recheck a suspected broken chart at several delays before concluding anything.
- Take viewport shots at several scroll depths for `position: fixed` elements.
- Repeat an ambiguous finding in an isolated script several times before reporting it.

**Output.** A structured report. Per step: what was done, what was observed (exact rendered text, not paraphrase), and the diagnostics at that point. End with anomalies, each with a root-cause hypothesis where the source reveals one.

## Phase 2: fresh-eyes critique

Give the Phase 1 report and screenshots to a reviewer with no knowledge of the implementation. Anyone who built or already reviewed the feature treats its structure as settled. Brief it with `agent-brief`: report and screenshots only, no source, no review history, no "what we already decided".

Ask for findings in three categories:

- **Correctness and trust.** Anything that feels wrong, broken or self-contradictory even when no error is thrown.
- **Information architecture and flow.** Whether gates, order, tabs vs. sections, exclusivity and pacing serve the experience.
- **Visual design.** Density, hierarchy, consistency of emphasis, and collisions between decorative and functional elements.

Each finding states what is wrong (naming the screenshot and element), why it matters to the user, a severity (`blocking`, `major`, `minor`), and a fix direction concrete enough to define done. The report also lists what is confirmed working and must not regress. That list separates a real concept problem from polish debt.

## Handing off

File each finding via `tracker` and offer `do-work` for the fixes.

## Hard rules

- Never fix anything during the review.

## Provenance and maintenance

Updated: 2026-11-27.

Re-verification commands:
```bash
ls plugins/coding/skills/interactive-app-review/references/defect-classes.md
npx playwright --version
```
