#!/usr/bin/env python3
"""Antigravity SessionStart hook: injects session-card.md into every session.

Reads plugins/punchcard/session-card.md directly so there is one source of truth
shared with Claude Code's SessionStart hook. Stdlib-only.
"""
import json
import os
from pathlib import Path


def main() -> None:
    plugin_root = Path(os.environ.get("PLUGIN_ROOT") or Path(__file__).resolve().parent.parent)
    card_path = plugin_root / "session-card.md"
    content = card_path.read_text(encoding="utf-8").strip()
    payload = {
        "injectSteps": [
            {
                "systemMessage": {
                    "systemMessage": content,
                }
            }
        ]
    }
    print(json.dumps(payload))


if __name__ == "__main__":
    main()
