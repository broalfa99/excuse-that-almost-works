#!/usr/bin/env python3
"""The Excuse That Almost Works — make.fun bounty entry.

Writes the one line a gamer texts the boss to skip work
on GTA 6 launch week to /output/entry.txt.
"""

import os

LINE = (
    "Hi, the dentist moved my appointment to 9am "
    "and they charge fifty bucks if I miss it."
)

OUTPUT_PATH = "/output/entry.txt"

MAX_WORDS = 20
MAX_CHARS = 140


def main():
    line = LINE.strip()
    if not line:
        raise SystemExit("entry line is empty")
    words = line.split()
    if len(words) > MAX_WORDS:
        raise SystemExit(
            f"entry line is {len(words)} words, over the {MAX_WORDS} limit"
        )
    if len(line) > MAX_CHARS:
        raise SystemExit(
            f"entry line is {len(line)} characters, over the {MAX_CHARS} limit"
        )
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(line)
    print(f"Wrote {len(line)} characters, {len(words)} words to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
