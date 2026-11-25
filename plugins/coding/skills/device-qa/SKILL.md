---
name: device-qa
tier: leaf
description: >
  The Android device loop: build and reinstall with adb over wireless
  debugging, verify what the emulator can show first, hand the human a short
  checklist of what only a physical device shows, collect results through the
  question interface, then close or reopen tasks. Load when a task needs a
  build installed on a phone or tablet, or when the user reports a defect from
  a device. Do NOT load for browser-based review (see interactive-app-review),
  view rules (see frontend-ui), or tests that run without a device (see
  validation-and-qa).
trigger: /device-qa
---

# /device-qa

The agent does everything a machine can. The human checks only what needs a physical device.

## When NOT to use this skill

| Situation | Use instead |
|---|---|
| Reviewing a web app in a browser | `interactive-app-review` |
| View state and layout rules | `frontend-ui` |
| Automated tests and the gate | `validation-and-qa` |
| Handing over commands only a human can run | `backlog` |

## Loop

1. **Build.** Build the package with the project's build command.
2. **Emulator first.** Install on the emulator with `adb -e install -r <apk>`. Verify what it can show: launch, navigation, the five view states, layout at the target sizes. Fix what fails before any human sees it.
3. **Device.** Confirm the device is connected over wireless debugging with `adb devices`. If it is not, hand the pairing step to the user via `backlog` and stop. Reinstall with `adb -d install -r <apk>`, or `adb -s <serial> install -r <apk>` when several devices are attached.
4. **Checklist.** Give the human a short checklist limited to what only hardware shows: sensors, camera, touch feel, performance, notifications, real network, battery behaviour. Each item names the action and the expected result.
5. **Collect.** Gather results through the question interface, 2-4 questions per batch, one per checklist group, with pass and fail options. Treat screenshots the user sends as evidence and read them before replying.
6. **Close or reopen.** Close a task through `backlog` when every item passes. File each reported defect via `backlog` with the item, the observed result and the screenshot reference, and reopen the task it belongs to.

## Hard rules

- Never ask the human to check what the emulator can show.
- Never give a checklist longer than the device-only items.
- Never mark a task done on the agent's own build; it needs the device result.
- Never reinstall to a device other than the one the user named.
- Never drop a reported defect; file each one via `backlog`.

## Provenance and maintenance

Updated: 2026-11-13.

Re-verification commands:
```bash
adb version
adb devices
```
