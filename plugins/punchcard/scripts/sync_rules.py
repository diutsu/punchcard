#!/usr/bin/env python3
"""Sync and validate punchcard's always-on rules and cross-harness manifests.

Single source of truth:
  - plugins/punchcard/output-styles/punchcard.md -> plugins/punchcard/rules/AGENTS.md
  - plugins/punchcard/session-card.md            -> read directly by SessionStart hooks

Usage:
  python3 plugins/punchcard/scripts/sync_rules.py --write     # regenerate rules/AGENTS.md
  python3 plugins/punchcard/scripts/sync_rules.py --check     # fail on drift or invalid JSON
  python3 plugins/punchcard/scripts/sync_rules.py --combined  # print response style + session card

Stdlib-only.
"""
import argparse
import json
import re
import sys
from pathlib import Path

PLUGIN_DIR = Path(__file__).resolve().parent.parent
REPO_ROOT = PLUGIN_DIR.parent.parent
STYLE_SRC = PLUGIN_DIR / "output-styles" / "punchcard.md"
CARD_SRC = PLUGIN_DIR / "session-card.md"
RULES_DST = PLUGIN_DIR / "rules" / "AGENTS.md"

GENERATED_HEADER = (
    "<!-- Generated from plugins/punchcard/output-styles/punchcard.md. "
    "Edit the source and run: python3 plugins/punchcard/scripts/sync_rules.py --write -->\n\n"
)


def strip_frontmatter(text: str) -> str:
    match = re.match(r"^---\n.*?\n---\n+", text, re.DOTALL)
    return text[match.end():] if match else text


def render_rules() -> str:
    body = strip_frontmatter(STYLE_SRC.read_text(encoding="utf-8")).lstrip("\n")
    return GENERATED_HEADER + body


def render_combined() -> str:
    style = strip_frontmatter(STYLE_SRC.read_text(encoding="utf-8")).strip()
    card = CARD_SRC.read_text(encoding="utf-8").strip()
    return f"{style}\n\n---\n\n{card}\n"


def check_manifests() -> list[str]:
    errors: list[str] = []
    json_files = [
        REPO_ROOT / ".claude-plugin" / "marketplace.json",
        REPO_ROOT / ".agents" / "plugins.json",
        REPO_ROOT / ".agents" / "plugins" / "marketplace.json",
        PLUGIN_DIR / "hooks.json",
        PLUGIN_DIR / "hooks" / "hooks.json",
    ]
    for path in json_files:
        if not path.exists():
            errors.append(f"missing {path.relative_to(REPO_ROOT)}")
            continue
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            errors.append(f"invalid JSON in {path.relative_to(REPO_ROOT)}: {exc}")

    plugins_dir = REPO_ROOT / "plugins"
    shared_keys = ("name", "version", "description", "author", "repository")
    for plugin_path in sorted(p for p in plugins_dir.iterdir() if p.is_dir()):
        manifest_paths = [
            plugin_path / ".claude-plugin" / "plugin.json",
            plugin_path / "plugin.json",
            plugin_path / ".codex-plugin" / "plugin.json",
        ]
        loaded: list[tuple[Path, dict]] = []
        for mp in manifest_paths:
            if not mp.exists():
                errors.append(f"missing {mp.relative_to(REPO_ROOT)}")
                continue
            try:
                loaded.append((mp, json.loads(mp.read_text(encoding="utf-8"))))
            except json.JSONDecodeError as exc:
                errors.append(f"invalid JSON in {mp.relative_to(REPO_ROOT)}: {exc}")
        if len(loaded) >= 2:
            base_path, base_data = loaded[0]
            for other_path, other_data in loaded[1:]:
                for key in shared_keys:
                    if base_data.get(key) != other_data.get(key):
                        errors.append(
                            f"manifest mismatch on '{key}': "
                            f"{base_path.relative_to(REPO_ROOT)} vs {other_path.relative_to(REPO_ROOT)}"
                        )
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--write", action="store_true", help="Regenerate rules/AGENTS.md from output-styles/punchcard.md")
    group.add_argument("--check", action="store_true", help="Verify rules/AGENTS.md sync and all plugin manifests")
    group.add_argument("--combined", action="store_true", help="Print response style + session card to stdout")
    args = parser.parse_args()

    if args.write:
        RULES_DST.parent.mkdir(parents=True, exist_ok=True)
        RULES_DST.write_text(render_rules(), encoding="utf-8")
        return 0

    if args.combined:
        sys.stdout.write(render_combined())
        return 0

    errors: list[str] = []
    expected = render_rules()
    if not RULES_DST.exists():
        errors.append(f"missing {RULES_DST.relative_to(REPO_ROOT)} (run --write)")
    elif RULES_DST.read_text(encoding="utf-8") != expected:
        errors.append(
            f"drift in {RULES_DST.relative_to(REPO_ROOT)} "
            "(run: python3 plugins/punchcard/scripts/sync_rules.py --write)"
        )

    errors.extend(check_manifests())
    if errors:
        for err in errors:
            print(err, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
