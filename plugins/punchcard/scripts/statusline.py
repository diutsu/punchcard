#!/usr/bin/env python3
"""Powerline statusline for Claude Code.

Reads JSON from stdin (piped by Claude Code) and renders a background-filled
powerline bar, styled after my oh-my-zsh diutsu theme.

Layout:
  [model effort cost] ▶ [ctx-bar ctx%] ▶ [5h usage%] ▶ [proj] ▶ [⎇ branch] ▶ [session]

The "5h usage%" segment is the session usage against the rolling 5-hour rate
limit (rate_limits.five_hour.used_percentage). It is only sent by Claude Code
for Pro/Max sessions and only after the first API response, so it is hidden
whenever that field is absent.

Stdlib-only. No external dependencies.
"""
import json
import os
import re
import subprocess
import sys

_ANSI = re.compile(r"\033\[[0-9;]*m")

# ---------------------------------------------------------------------------
# Powerline glyphs (Nerd Font — same ones diutsu.zsh-theme uses)
# ---------------------------------------------------------------------------

SEP = ""      # hard right divider (END_SEP)
IC_BRANCH = ""  # git branch glyph (IC_GB)
CAP_LEFT = ""  # nf-ple-pixelated_squares_small_mirrored (U+E0C7) — left edge cap

RESET = "\033[0m"

# Background SGR codes → diutsu flow: magenta → blue → yellow → green → white.
# Text is always black (fg 30) on every segment, like diutsu does ($K on $Mb/$Cb/$Yb).
FG = 30  # black text, used on all segments
MAGENTA, BLUE, CYAN, YELLOW, GREEN, WHITE = 45, 44, 46, 43, 42, 47


# ---------------------------------------------------------------------------
# Collectors
# ---------------------------------------------------------------------------


def _git_info() -> dict:
    """Branch + dirty flag. No cache (per-session, ~5ms)."""
    env = {**os.environ, "GIT_OPTIONAL_LOCKS": "0"}
    try:
        r = subprocess.run(
            ["git", "rev-parse", "--abbrev-ref", "HEAD"],
            capture_output=True, text=True, env=env, timeout=5,
        )
        if r.returncode != 0:
            return {"branch": "", "dirty": False}
        branch = r.stdout.strip()
        dirty = bool(subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True, text=True, env=env, timeout=5,
        ).stdout.strip())
    except (subprocess.TimeoutExpired, FileNotFoundError):
        return {"branch": "", "dirty": False}
    return {"branch": branch, "dirty": dirty}


def _proj(cwd: str) -> str:
    """Top-level folder under STATUSLINE_WORKSPACE_DIR (if set), else basename."""
    if not cwd:
        return "?"
    ws_dir = os.environ.get("STATUSLINE_WORKSPACE_DIR", "").strip()
    if ws_dir:
        ws_root = os.path.realpath(os.path.expanduser(ws_dir))
        cwd_real = os.path.realpath(cwd)
        if cwd_real == ws_root:
            return os.path.basename(ws_root) or cwd
        prefix = ws_root.rstrip(os.sep) + os.sep
        if cwd_real.startswith(prefix):
            return cwd_real[len(prefix):].split(os.sep)[0]
    return os.path.basename(cwd.rstrip("/")) or cwd


# ---------------------------------------------------------------------------
# Formatters
# ---------------------------------------------------------------------------


def _model_name(model) -> str:
    if not model:
        return "Claude"
    if isinstance(model, str):
        name = model
    else:
        name = model.get("display_name") or model.get("id") or "Claude"
    # Collapse the verbose extended-context label, always.
    return name.replace("(1M context)", "1M")


def _ctx_bar(pct: float, width: int = 10) -> str:
    filled = max(0, min(width, round(pct / 100 * width)))
    return "▓" * filled + "░" * (width - filled)


# ---------------------------------------------------------------------------
# Powerline rendering
# ---------------------------------------------------------------------------


def _render(segments: list, pad: bool = True) -> str:
    """segments: list of (text, bg). bg is a real SGR background code (40-47).

    Renders bg-filled powerline cells: black text on each bg, dividers carry the
    previous segment's color as foreground into the next segment's background.
    The first cell has no leading space (no indent at the start of the line).
    When pad is False, the spaces flanking each divider are dropped entirely.
    """
    segments = [s for s in segments if s[0]]
    if not segments:
        return ""
    # Left edge cap: pixel squares in the first segment's color on default bg.
    out = [f"\033[49;{segments[0][1] - 10}m{CAP_LEFT}"]
    for i, (text, bg) in enumerate(segments):
        lead = " " if (pad and i > 0) else ""
        trail = " " if pad else ""
        out.append(f"\033[{FG};{bg}m{lead}{text}{trail}")
        next_bg = segments[i + 1][1] if i + 1 < len(segments) else None
        if next_bg is None:
            out.append(f"\033[49;{bg - 10}m{SEP}{RESET}")  # tail: divider on default bg
        else:
            out.append(f"\033[{bg - 10};{next_bg}m{SEP}")
    return "".join(out)


def _vis_len(line: str) -> int:
    """Visible column count: strip ANSI, count code points (glyphs ≈ 1 col)."""
    return len(_ANSI.sub("", line))


def generate(data: dict) -> str:
    cols = int(os.environ.get("COLUMNS") or 0)

    model = _model_name(data.get("model"))
    effort = (data.get("effort") or {}).get("level", "")
    cost = (data.get("cost") or {}).get("total_cost_usd", 0) or 0
    pct = (data.get("context_window") or {}).get("used_percentage") or 0
    # Session usage against the rolling 5-hour rate limit. Absent for non
    # Pro/Max sessions and before the first API response → None means "hide".
    usage = ((data.get("rate_limits") or {}).get("five_hour") or {}).get("used_percentage")
    cwd = (data.get("workspace") or {}).get("current_dir") or data.get("cwd", "")
    proj = _proj(cwd)
    git = _git_info()
    branch = git.get("branch", "")
    dirty = git.get("dirty", False)
    session_full = data.get("session_name") or ""

    def build(level: int):
        """Progressive degradation when the bar doesn't fit:
        0 full · 1 truncate session · 2 drop effort · 3 drop ctx/usage bars · 4 drop padding."""
        session = session_full
        if level >= 1 and len(session) > 15:
            session = session[:15] + "..."

        g1 = model
        if effort and level < 2:
            g1 += f" {effort}"
        if cost:
            g1 += f" ${cost:.2f}"

        g2 = f"{pct:.1f}%" if level >= 3 else f"{_ctx_bar(pct)} {pct:.1f}%"
        if usage is None:
            g_usage = ""
        else:
            g_usage = f"{usage:.0f}% 5h" if level >= 3 else f"{_ctx_bar(usage)} {usage:.0f}% 5h"
        g4 = f"{IC_BRANCH} {branch}{'*' if dirty else ''}" if branch else ""

        segments = [
            (g1, MAGENTA),
            (g2, BLUE),
            (g_usage, CYAN),
            (proj, YELLOW),
            (g4, GREEN),
            (session, WHITE),
        ]
        return segments, level < 4  # pad until the last level

    for level in range(5):
        segments, pad = build(level)
        line = _render(segments, pad)
        if cols <= 0 or _vis_len(line) <= cols or level == 4:
            return line


def main():
    try:
        if sys.platform == "win32":
            sys.stdout.reconfigure(encoding="utf-8", errors="replace")
            sys.stdin.reconfigure(encoding="utf-8", errors="replace")

        if "--demo" in sys.argv or sys.stdin.isatty():
            demo = {
                "session_name": "foobar do that thing now",
                "model": {"id": "claude-opus-4-8", "display_name": "Opus 4.8 (1M context)"},
                "effort": {"level": "high"},
                "workspace": {"current_dir": "/path/to/proj/sub"},
                "cwd": "/path/to/proj/sub",
                "cost": {"total_cost_usd": 2.45},
                "context_window": {"used_percentage": 9.3},
                "rate_limits": {"five_hour": {"used_percentage": 41.0}},
            }
            print(generate(demo))
            return

        raw = sys.stdin.read()
        data = json.loads(raw) if raw.strip() else {}
        print(generate(data))
    except Exception:
        print("\033[90mstatusline error\033[0m")


if __name__ == "__main__":
    main()
