from __future__ import annotations

import ast
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN_TOKENS = ("", "filecite", "\u2060")
TRACKED_AUDIT = ROOT / "data" / "audit.jsonl"


def check_python_syntax() -> list[str]:
    failures: list[str] = []
    for path in ROOT.rglob("*.py"):
        if any(part in {".venv", "__pycache__", ".git"} for part in path.parts):
            continue
        try:
            ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        except SyntaxError as exc:
            failures.append(f"{path.relative_to(ROOT)}: syntax error: {exc}")
    return failures


def check_public_text() -> list[str]:
    failures: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md", ".toml", ".yml", ".yaml", ".json", ".txt", ".py"}:
            continue
        if any(part in {".git", ".venv", "__pycache__"} for part in path.parts):
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for token in FORBIDDEN_TOKENS:
            if token in text:
                failures.append(f"{path.relative_to(ROOT)}: contains forbidden internal token {token!r}")
                break
    return failures


def check_tracked_runtime_output() -> list[str]:
    if TRACKED_AUDIT.exists() and TRACKED_AUDIT.stat().st_size:
        return ["data/audit.jsonl contains runtime output and must not be committed"]
    return []


def main() -> int:
    failures = check_python_syntax() + check_public_text() + check_tracked_runtime_output()
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("Repository quality checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
