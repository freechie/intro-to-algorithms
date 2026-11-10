"""Write TODAY.md for the one practice problem that is still open.

Open TODAY.md and do that problem. Run this program again when you finish
or when the timer ends.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

# `python3 practice/today.py` puts practice/ on sys.path. The repo root has to
# be there too, or `import practice` fails. `python3 -m practice.today` already
# has the root on the path.
if __package__ in (None, ""):
    sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from practice.session import (
    CODE,
    REPLAY,
    LogEntry,
    current_session,
    format_log_line,
    parse_log,
    problem_from_dict,
    stub_source,
    work_is_unwritten,
)

NEW_YORK = ZoneInfo("America/New_York")


def default_root() -> Path:
    return Path(__file__).resolve().parent.parent


def run(argv: list[str] | None = None, root: Path | None = None, today: str | None = None) -> int:
    parser = argparse.ArgumentParser(description="Show the one practice problem for today.")
    subparsers = parser.add_subparsers(dest="command")
    done = subparsers.add_parser("done", help="mark today's problem done")
    done.add_argument("--note", default="", help="one short note about what you tried")
    subparsers.add_parser("stuck", help="mark today's problem stuck and keep it for next time")
    subparsers.add_parser("show", help="refresh TODAY.md")
    args = parser.parse_args(argv)

    repo = root if root is not None else default_root()
    command = args.command or "show"
    day = today if today is not None else datetime.now(NEW_YORK).date().isoformat()
    problems = load_problems(repo)
    entries = load_log(repo)
    session = current_session(problems, entries)

    if command in ("done", "stuck"):
        if session.problem is None:
            write_today(repo, session.markdown)
            print("The first list is done.")
            return 0
        if command == "done" and solution_file_unwritten(repo, session.problem):
            ensure_stub(repo, session.problem)
            write_today(repo, session.markdown)
            print(_missing_work_message(session.problem))
            return 1
        note = args.note if command == "done" else ""
        result = "done" if command == "done" else "stuck"
        append_log(repo, format_log_line(day, session.problem.slug, result, note))
        print(f"Marked {session.problem.slug} {result}.")
        entries = entries + (LogEntry(day, session.problem.slug, result, note),)
        session = current_session(problems, entries)

    if session.problem is not None:
        ensure_stub(repo, session.problem)
    write_today(repo, session.markdown)
    if session.problem is None:
        print("The first list is done.")
    else:
        print(f"Today: {session.problem.title}")
        print(session.problem.filename)
    print("Wrote TODAY.md")
    return 0


def load_problems(root: Path):
    payload = json.loads((root / "practice" / "problems.json").read_text(encoding="utf-8"))
    return tuple(problem_from_dict(item) for item in payload)


def load_log(root: Path) -> tuple[LogEntry, ...]:
    path = root / "practice" / "log.tsv"
    if not path.exists():
        path.write_text("date\tslug\tresult\tnote\n", encoding="utf-8")
    return parse_log(path.read_text(encoding="utf-8"))


def append_log(root: Path, line: str) -> None:
    path = root / "practice" / "log.tsv"
    if not path.exists():
        path.write_text("date\tslug\tresult\tnote\n", encoding="utf-8")
    with path.open("a", encoding="utf-8") as handle:
        handle.write(line)


def write_today(root: Path, markdown: str) -> None:
    (root / "TODAY.md").write_text(markdown, encoding="utf-8")


def ensure_stub(root: Path, problem) -> None:
    path = root / problem.filename
    if path.exists():
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(stub_source(problem), encoding="utf-8")


def solution_file_unwritten(root: Path, problem) -> bool:
    path = root / problem.filename
    if not path.exists():
        return True
    return work_is_unwritten(path.read_text(encoding="utf-8"), problem)


def _missing_work_message(problem) -> str:
    if problem.kind == REPLAY:
        return f"Write one sentence in {problem.filename} first."
    if problem.kind != CODE:
        raise ValueError(f"unknown kind: {problem.kind}")
    return f"Write a solution in {problem.filename} first."


def main() -> None:
    sys.exit(run())


if __name__ == "__main__":
    main()
