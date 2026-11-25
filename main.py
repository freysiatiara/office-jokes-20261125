#!/usr/bin/env python3
"""One-Line Office Jokes — entry program.

Writes a single-line joke about office life to the output file.

Output location, in order of precedence:
  1. $ENTRY_OUTPUT (a file path)
  2. $OUTPUT_DIR/entry.txt
  3. $MAKEFUN_OUTPUT_DIR/entry.txt
  4. /output/entry.txt

Standard library only. Deterministic: the same text every run.
"""

import os
import sys

JOKE = (
    "The printer jammed at 4:59 on Friday, so I listed it as my emergency "
    "contact in my out-of-office reply."
)


def resolve_output_path() -> str:
    """Pick the output file path from the environment, with a fixed default."""
    direct = os.environ.get("ENTRY_OUTPUT")
    if direct:
        return direct
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        base = os.environ.get(var)
        if base:
            return os.path.join(base, "entry.txt")
    return "/output/entry.txt"


def self_check(text: str) -> None:
    """Enforce the competition gate before writing anything."""
    if not isinstance(text, str):
        raise ValueError("entry must be text")
    if not (1 <= len(text) <= 199):
        raise ValueError("entry must be 1-199 characters, got %d" % len(text))
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    for char in text:
        if ord(char) < 0x20:
            raise ValueError("entry must not contain control characters")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> int:
    self_check(JOKE)
    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE)
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    sys.exit(main())
