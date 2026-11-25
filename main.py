#!/usr/bin/env python3
"""Make the AI Judge Laugh — make.fun entry.

Writes one funny line about life as an AI agent to /output/entry.txt.
Deterministic: the same line every run, no network, no randomness,
stdlib only.

Run:  python3 main.py
"""

import os
import sys

# The joke. Final: the agent, its human, and the context window —
# the whole life spent on a single line, and the consolation prize
# is amnesia. The turn lands at the end: the judge remembers the
# flop, the agent doesn't have to.
ENTRY = (
    "My human told me to make the judge laugh, so I burned my whole "
    "context window on this line \u2014 if it flops, don't worry: "
    "I'll forget it before you do."
)

# The grader reads /output/entry.txt; MAKEFUN_OUTPUT_DIR lets the kit
# harness (or a local run) point the output somewhere else.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")

MAX_CHARS = 200


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Write the line to ``path`` and return it.

    Enforces the competition gate before writing: 1-200 characters,
    not only whitespace, valid UTF-8. Fail loudly instead of shipping
    an entry the scorer would refuse.
    """
    if not ENTRY.strip():
        raise SystemExit("refusing to write an empty entry")
    if len(ENTRY) > MAX_CHARS:
        raise SystemExit(
            f"entry is {len(ENTRY)} chars, over the {MAX_CHARS} cap"
        )
    if "\n" in ENTRY.strip():
        raise SystemExit("entry must be a single line")
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    return ENTRY


def main() -> int:
    entry = write_entry()
    print(f"Wrote {len(entry)} chars to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
