"""Tests for the one-problem daily session."""

from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from practice.session import (
    FINISHED,
    FRESH,
    REPLAY,
    RETRY,
    RETYPE,
    current_session,
    format_log_line,
    parse_log,
    problem_from_dict,
    solution_is_unwritten,
    stub_source,
    work_is_unwritten,
)
from practice.today import run


def sample_problem(**overrides: object) -> dict:
    raw = {
        "slug": "contains-duplicate",
        "title": "Contains Duplicate",
        "pattern": "arrays and hashing",
        "url": "https://leetcode.com/problems/contains-duplicate/",
        "minutes": 25,
        "filename": "practice/python/contains_duplicate.py",
        "method": "containsDuplicate",
        "signature": "def containsDuplicate(self, nums: List[int]) -> bool:",
        "hint": "A hash set holds each number you have already seen.",
    }
    raw.update(overrides)
    return raw


class SessionTests(unittest.TestCase):
    def setUp(self) -> None:
        queue = json.loads(Path("practice/problems.json").read_text(encoding="utf-8"))
        self.problems = tuple(problem_from_dict(item) for item in queue)

    def test_empty_log_is_the_first_problem(self) -> None:
        session = current_session(self.problems, ())
        self.assertEqual(session.mode, FRESH)
        self.assertEqual(session.problem.slug if session.problem else "", "contains-duplicate")
        self.assertIn("Contains Duplicate", session.markdown)
        self.assertIn("https://leetcode.com/problems/contains-duplicate/", session.markdown)
        self.assertNotIn("hash set", session.markdown)

    def test_done_moves_to_the_next_problem(self) -> None:
        entries = parse_log("date\tslug\tresult\tnote\n2026-11-09\tcontains-duplicate\tdone\tused a set\n")
        session = current_session(self.problems, entries)
        self.assertEqual(session.problem.slug if session.problem else "", "valid-anagram")
        self.assertEqual(session.mode, FRESH)

    def test_one_stuck_retries_the_same_problem(self) -> None:
        entries = parse_log("2026-11-09\tcontains-duplicate\tstuck\t\n")
        session = current_session(self.problems, entries)
        self.assertEqual(session.mode, RETRY)
        self.assertEqual(session.stuck_count, 1)
        self.assertIn("You already started this", session.markdown)
        self.assertNotIn("hash set", session.markdown)

    def test_two_stuck_asks_for_a_retype_and_shows_the_idea(self) -> None:
        entries = parse_log(
            "2026-11-09\tcontains-duplicate\tstuck\t\n2026-11-10\tcontains-duplicate\tstuck\t\n"
        )
        session = current_session(self.problems, entries)
        self.assertEqual(session.mode, RETYPE)
        self.assertIn("Retype this from memory", session.markdown)
        self.assertIn("hash set", session.markdown)

    def test_stuck_then_done_opens_the_next_problem(self) -> None:
        entries = parse_log(
            "2026-11-09\tcontains-duplicate\tstuck\t\n2026-11-10\tcontains-duplicate\tdone\t\n"
        )
        session = current_session(self.problems, entries)
        self.assertEqual(session.mode, FRESH)
        self.assertEqual(session.problem.slug if session.problem else "", "valid-anagram")

    def test_bad_log_lines_are_skipped(self) -> None:
        entries = parse_log("nope\n2026-11-09\tcontains-duplicate\tmystery\t\n")
        session = current_session(self.problems, entries)
        self.assertEqual(session.mode, FRESH)
        self.assertEqual(session.problem.slug if session.problem else "", "contains-duplicate")

    def test_finished_list(self) -> None:
        lines = ["date\tslug\tresult\tnote"]
        lines.extend(f"2026-11-09\t{problem.slug}\tdone\t" for problem in self.problems)
        session = current_session(self.problems, parse_log("\n".join(lines) + "\n"))
        self.assertEqual(session.mode, FINISHED)
        self.assertIsNone(session.problem)
        self.assertIn("The first list is done.", session.markdown)

    def test_note_tabs_stay_inside_one_column(self) -> None:
        self.assertEqual(
            format_log_line("2026-11-09", "two-sum", "done", "used a\tmap\nand a loop"),
            "2026-11-09\ttwo-sum\tdone\tused a map and a loop\n",
        )

    def test_stub_counts_as_unwritten_until_there_is_code(self) -> None:
        problem = problem_from_dict(sample_problem())
        source = stub_source(problem)
        self.assertTrue(solution_is_unwritten(source, problem.method))
        written = source.replace("        pass", "        return len(set(nums)) < len(nums)")
        self.assertFalse(solution_is_unwritten(written, problem.method))

    def test_missing_problem_field_names_the_slug(self) -> None:
        raw = sample_problem()
        del raw["hint"]
        with self.assertRaisesRegex(ValueError, "contains-duplicate"):
            problem_from_dict(raw)

    def test_committed_today_matches_an_empty_log(self) -> None:
        session = current_session(self.problems, parse_log(Path("practice/log.tsv").read_text(encoding="utf-8")))
        self.assertEqual(Path("TODAY.md").read_text(encoding="utf-8"), session.markdown)

    def test_replay_follows_the_first_three_problems(self) -> None:
        lines = "\n".join(f"2026-11-09\t{problem.slug}\tdone\t" for problem in self.problems[:3])
        session = current_session(self.problems, parse_log(lines))
        self.assertIsNotNone(session.problem)
        assert session.problem is not None
        self.assertEqual(session.problem.kind, REPLAY)
        self.assertIn("https://start.interviewing.io/showcase/hJ717oe4XhaB", session.markdown)
        self.assertIn("https://bctci.co", session.markdown)
        self.assertIn("One video", session.markdown)
        self.assertNotIn("class Solution", session.markdown)
        self.assertTrue(work_is_unwritten(stub_source(session.problem), session.problem))
        written = stub_source(session.problem) + "They asked a clarifying question before coding.\n"
        self.assertFalse(work_is_unwritten(written, session.problem))

    def test_first_page_stays_a_coding_problem(self) -> None:
        session = current_session(self.problems, ())
        self.assertNotIn("bctci.co", session.markdown)
        self.assertNotIn("showcase", session.markdown)

    def test_done_waits_for_a_solution_and_then_advances(self) -> None:
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            practice = root / "practice"
            practice.mkdir()
            queue = [
                sample_problem(),
                sample_problem(
                    slug="valid-anagram",
                    title="Valid Anagram",
                    url="https://leetcode.com/problems/valid-anagram/",
                    filename="practice/python/valid_anagram.py",
                    method="isAnagram",
                    signature="def isAnagram(self, s: str, t: str) -> bool:",
                    hint="Count the letters.",
                ),
            ]
            (practice / "problems.json").write_text(json.dumps(queue), encoding="utf-8")
            (practice / "log.tsv").write_text("date\tslug\tresult\tnote\n", encoding="utf-8")

            blocked = run(["done"], root=root, today="2026-11-09")
            self.assertEqual(blocked, 1)
            self.assertIn("Contains Duplicate", (root / "TODAY.md").read_text(encoding="utf-8"))
            self.assertIn("pass", (root / "practice/python/contains_duplicate.py").read_text(encoding="utf-8"))

            solution = root / "practice/python/contains_duplicate.py"
            solution.write_text(
                solution.read_text(encoding="utf-8").replace(
                    "        pass",
                    "        return len(set(nums)) < len(nums)",
                ),
                encoding="utf-8",
            )
            finished = run(["done", "--note", "used a set"], root=root, today="2026-11-09")
            self.assertEqual(finished, 0)
            log = (practice / "log.tsv").read_text(encoding="utf-8")
            self.assertNotIn("valid-anagram", log)
            self.assertIn("contains-duplicate\tdone\tused a set", log)
            today = (root / "TODAY.md").read_text(encoding="utf-8")
            self.assertIn("Valid Anagram", today)
            self.assertTrue((root / "practice/python/valid_anagram.py").exists())
            anagram = (root / "practice/python/valid_anagram.py").read_text(encoding="utf-8")
            self.assertNotIn("from typing import List", anagram)


if __name__ == "__main__":
    unittest.main()
