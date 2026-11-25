"""One line: the excuse my agent gave me for missing a deadline.

Writes a single line to /output/entry.txt.
"""

from pathlib import Path

LINE = "I met the deadline. It was met by a version of me from last Tuesday, and he has since been deprecated."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
