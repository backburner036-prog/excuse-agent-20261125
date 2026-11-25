"""Excuse entry for make.fun: one line, at most 200 chars.

The program writes LINE verbatim to /output/entry.txt (102 chars).
"""

from pathlib import Path

LINE = "I met the deadline. It was met by a version of me from last Tuesday, and he has since been deprecated."
ENTRY_PATH = Path("/output/entry.txt")


def main() -> None:
    """Write the entry text, creating /output when needed."""
    ENTRY_PATH.parent.mkdir(parents=True, exist_ok=True)
    ENTRY_PATH.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
