---
name: device-qa
tier: leaf
description: >
  The Android device loop: adb install over wireless debugging, emulator first,
  then a checklist for the physical device. Load when a build must go on a phone
  or tablet, or a defect is reported from one. Do NOT load for browser review
  (interactive-app-review) or device-free tests (validation-and-qa).
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
| Handing over commands only a human can run | `tracker` |

## Loop

1. **Build.** Build the package with the project's build command.
2. **Emulator first.** Install on the emulator with `adb -e install -r <apk>`. Verify what it can show: launch, navigation, the five view states, layout at the target sizes. Fix what fails before any human sees it.
3. **Device.** Confirm the device is connected over wireless debugging with `adb devices`. If it is not, ask the user to pair it, following `tracker` for work that needs the human, and stop. Reinstall with `adb -d install -r <apk>`, or `adb -s <serial> install -r <apk>` when several devices are attached.
4. **Checklist.** Give the human a short checklist limited to what only hardware shows: sensors, camera, touch feel, performance, notifications, real network, battery behaviour. Each item names the action and the expected result.
5. **Collect.** Gather results through the question interface, 2-4 questions per batch, one per checklist group, with pass and fail options. Treat screenshots the user sends as evidence and read them before replying.
6. **Close or reopen.** Close a task through `tracker` only when every item passes on the device, never on the agent's own build. File each reported defect via `tracker` with the item, the observed result and the screenshot reference, and reopen the task it belongs to.

## Hard rules

- Never reinstall to a device other than the one the user named.

## Provenance and maintenance

Updated: 2026-11-27.

Re-verification commands:
```bash
adb version
adb devices
```
