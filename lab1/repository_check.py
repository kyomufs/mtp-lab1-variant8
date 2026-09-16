"""Check whether the repository contains the main lab artifacts."""

from pathlib import Path
from typing import Iterable


REQUIRED_PATHS = (
    ".gitignore",
    ".gitmodules",
    ".github/workflows/python-checks.yml",
    "docs/git-setup.md",
    "external/sampleproject",
)


def find_missing(
    project_root: Path,
    required_paths: Iterable[str] = REQUIRED_PATHS,
) -> list[str]:
    """Return repository-relative paths that do not exist."""
    return [
        path
        for path in required_paths
        if not (project_root / path).exists()
    ]


def format_report(missing_paths: list[str]) -> str:
    """Build a readable report for the command-line interface."""
    if not missing_paths:
        return "All required lab files found."

    missing = "\n".join(f"- {path}" for path in missing_paths)
    return f"Missing required files:\n{missing}"


def main() -> None:
    """Check the current project and print the result."""
    project_root = Path(__file__).resolve().parents[1]
    print(format_report(find_missing(project_root)))


if __name__ == "__main__":
    main()
