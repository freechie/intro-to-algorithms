"""Choose the one practice problem for today from a queue and a log."""

from __future__ import annotations

from dataclasses import dataclass

FRESH = "fresh"
RETRY = "retry"
RETYPE = "retype"
FINISHED = "finished"
CODE = "code"
REPLAY = "replay"

MODES = (FRESH, RETRY, RETYPE, FINISHED)
KINDS = (CODE, REPLAY)

REQUIRED_FIELDS = (
    "slug",
    "title",
    "pattern",
    "url",
    "minutes",
    "filename",
    "method",
    "signature",
    "hint",
)


@dataclass(frozen=True)
class Problem:
    slug: str
    title: str
    pattern: str
    url: str
    minutes: int
    filename: str
    method: str
    signature: str
    hint: str
    kind: str


@dataclass(frozen=True)
class LogEntry:
    day: str
    slug: str
    result: str
    note: str


@dataclass(frozen=True)
class Session:
    mode: str
    problem: Problem | None
    stuck_count: int
    markdown: str


def problem_from_dict(raw: dict) -> Problem:
    kind = str(raw.get("kind", CODE))
    if kind not in KINDS:
        name = raw.get("slug", "unknown problem")
        raise ValueError(f"{name} has an unknown kind")
    required = REQUIRED_FIELDS if kind == CODE else _REPLAY_FIELDS
    missing = [key for key in required if key not in raw]
    if missing:
        name = raw.get("slug", "unknown problem")
        raise ValueError(f"{name} is missing {', '.join(missing)}")
    minutes = raw["minutes"]
    if not isinstance(minutes, int) or minutes <= 0:
        raise ValueError(f"{raw['slug']} needs a positive integer for minutes")
    return Problem(
        slug=str(raw["slug"]),
        title=str(raw["title"]),
        pattern=str(raw["pattern"]),
        url=str(raw["url"]),
        minutes=minutes,
        filename=str(raw["filename"]),
        method=str(raw.get("method", "")),
        signature=str(raw.get("signature", "")),
        hint=str(raw["hint"]),
        kind=kind,
    )


def parse_log(text: str) -> tuple[LogEntry, ...]:
    entries: list[LogEntry] = []
    for raw in text.splitlines():
        if raw.strip() == "" or raw.startswith("date\t"):
            continue
        parts = raw.split("\t")
        if len(parts) < 3:
            continue
        result = parts[2]
        if result not in ("done", "stuck"):
            continue
        note = parts[3] if len(parts) > 3 else ""
        entries.append(LogEntry(parts[0], parts[1], result, note))
    return tuple(entries)


def sanitize_note(note: str) -> str:
    return " ".join(note.replace("\t", " ").splitlines()).strip()


def current_session(problems: tuple[Problem, ...], entries: tuple[LogEntry, ...]) -> Session:
    done = {entry.slug for entry in entries if entry.result == "done"}
    problem = next((item for item in problems if item.slug not in done), None)
    if problem is None:
        return Session(FINISHED, None, 0, finished_markdown())
    stuck_count = sum(
        1 for entry in entries if entry.slug == problem.slug and entry.result == "stuck"
    )
    if stuck_count >= 2:
        mode = RETYPE
    elif stuck_count == 1:
        mode = RETRY
    else:
        mode = FRESH
    return Session(mode, problem, stuck_count, render(mode, problem))


def render(mode: str, problem: Problem | None) -> str:
    if mode == FINISHED:
        return finished_markdown()
    if problem is None:
        raise ValueError("a problem is required")
    if problem.kind == REPLAY:
        return _replay_markdown(problem, mode)
    if problem.kind != CODE:
        raise ValueError(f"unknown kind: {problem.kind}")
    if mode == FRESH:
        return _problem_markdown(problem, _FRESH_LEAD, include_hint=False)
    if mode == RETRY:
        return _problem_markdown(problem, _RETRY_LEAD, include_hint=False)
    if mode == RETYPE:
        return _problem_markdown(problem, _RETYPE_LEAD, include_hint=True)
    raise ValueError(f"unknown mode: {mode}")


def finished_markdown() -> str:
    return (
        "# Today\n"
        "\n"
        "The first list is done.\n"
        "\n"
        "Open `practice/log.tsv` and redo any row whose latest result says stuck.\n"
        "More mock replays from the book are at https://bctci.co.\n"
        "Add the next pattern to `practice/problems.json` when you want a new problem here.\n"
    )


def stub_source(problem: Problem) -> str:
    if problem.kind == REPLAY:
        return (
            f"# {problem.title}\n"
            f"# {problem.url}\n"
            "\n"
            "What the candidate said before writing code:\n"
        )
    lines = [f"# {problem.title}", f"# {problem.url}", ""]
    if "List[" in problem.signature:
        lines.extend(["from typing import List", ""])
    lines.extend(
        [
            "class Solution:",
            f"    {problem.signature}",
            "        pass",
            "",
        ]
    )
    return "\n".join(lines)


def work_is_unwritten(source: str, problem: Problem) -> bool:
    if problem.kind == REPLAY:
        return note_is_unwritten(source)
    if problem.kind != CODE:
        raise ValueError(f"unknown kind: {problem.kind}")
    return solution_is_unwritten(source, problem.method)


def note_is_unwritten(source: str) -> bool:
    for line in source.splitlines():
        stripped = line.strip()
        if stripped == "" or stripped.startswith("#") or stripped.startswith("http"):
            continue
        if stripped.endswith(":"):
            continue
        return False
    return True


def solution_is_unwritten(source: str, method: str) -> bool:
    lines = source.splitlines()
    start = next((index for index, line in enumerate(lines) if f"def {method}(" in line), None)
    if start is None:
        return True
    def_indent = len(lines[start]) - len(lines[start].lstrip(" "))
    for line in lines[start + 1 :]:
        if line.strip() == "":
            continue
        indent = len(line) - len(line.lstrip(" "))
        if indent <= def_indent:
            break
        stripped = line.strip()
        if stripped == "pass" or stripped.startswith("#"):
            continue
        if stripped.startswith(('"""', "'''")):
            continue
        return False
    return True


def format_log_line(day: str, slug: str, result: str, note: str) -> str:
    if result not in ("done", "stuck"):
        raise ValueError(f"unknown result: {result}")
    return f"{day}\t{slug}\t{result}\t{sanitize_note(note)}\n"


_FRESH_LEAD = "Say the pattern, a slow way, and the time cost before you type."

_RETRY_LEAD = (
    "You already started this. Try for 10 minutes. "
    "Then read the solution on the problem page, close it, and type it into the file yourself."
)

_RETYPE_LEAD = "Retype this from memory. Keep the problem page closed until the file has a solution."

_REPLAY_FIELDS = (
    "slug",
    "title",
    "pattern",
    "url",
    "minutes",
    "filename",
    "hint",
)

_REPLAY_LEADS = {
    FRESH: (
        "This is the Python replay linked from the book site. "
        "The problem in the video is a graph traversal. "
        "Listen for what the candidate says before they write code."
    ),
    RETRY: "Watch the same replay again. Then write one sentence about what they said before coding.",
    RETYPE: "Write that sentence from memory. Keep the video closed.",
}


def _problem_markdown(problem: Problem, lead: str, include_hint: bool) -> str:
    pattern = problem.pattern[:1].upper() + problem.pattern[1:]
    lines = [
        "# Today",
        "",
        "One problem. Stop when it is done.",
        "",
        f"**{problem.title}.** {pattern}. {problem.minutes} minutes.",
        "",
        lead,
        "",
    ]
    if include_hint:
        lines.extend([f"If it is still blank after 10 minutes, this is the idea: {problem.hint}", ""])
    lines.extend(
        [
            f"Open the problem: {problem.url}",
            "",
            f"Write the solution in `{problem.filename}`.",
            "",
            "When the solution is in that file:",
            "",
            "```bash",
            "python3 practice/today.py done",
            "```",
            "",
            "If the timer ends and the solution is still missing:",
            "",
            "```bash",
            "python3 practice/today.py stuck",
            "```",
            "",
        ]
    )
    return "\n".join(lines)


def _replay_markdown(problem: Problem, mode: str) -> str:
    if mode not in _REPLAY_LEADS:
        raise ValueError(f"unknown mode: {mode}")
    pattern = problem.pattern[:1].upper() + problem.pattern[1:]
    lines = [
        "# Today",
        "",
        "One video. Stop when it is done.",
        "",
        f"**{problem.title}.** {pattern}. {problem.minutes} minutes.",
        "",
        _REPLAY_LEADS[mode],
        "",
        f"Open the replay: {problem.url}",
        "",
        "Sign in at https://bctci.co if the page asks for the book account.",
        "",
        f"Write one sentence in `{problem.filename}`.",
        "",
        "When that sentence is in the file:",
        "",
        "```bash",
        "python3 practice/today.py done",
        "```",
        "",
        "If you stop before the video ends:",
        "",
        "```bash",
        "python3 practice/today.py stuck",
        "```",
        "",
    ]
    return "\n".join(lines)
