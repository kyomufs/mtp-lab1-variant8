"""Tests for the repository artifact check."""

import tempfile
import unittest
from pathlib import Path

from lab1.repository_check import find_missing, format_report


class RepositoryCheckTests(unittest.TestCase):
    """Check the pure functions without running Git commands."""

    def test_find_missing_returns_only_absent_paths(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            project_root = Path(directory)
            (project_root / "README.md").touch()

            result = find_missing(
                project_root,
                ("README.md", ".gitignore", ".gitmodules"),
            )

        self.assertEqual(result, [".gitignore", ".gitmodules"])

    def test_format_report_for_complete_repository(self) -> None:
        self.assertEqual(
            format_report([]),
            "All required lab files found.",
        )

    def test_format_report_lists_missing_paths(self) -> None:
        self.assertEqual(
            format_report([".gitmodules", "docs/git-setup.md"]),
            "Missing required files:\n"
            "- .gitmodules\n"
            "- docs/git-setup.md",
        )


if __name__ == "__main__":
    unittest.main()
