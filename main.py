#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes a single-line office joke to /output/entry.txt.
"""
import os

JOKE = "We have a 'no meeting Wednesdays' policy, which we discuss every Tuesday in a meeting."


def main():
    # Self-enforce the bounty gate before writing: 1-199 UTF-8 characters,
    # a single line, and not only whitespace.
    if not 1 <= len(JOKE) <= 199:
        raise SystemExit(f"entry must be 1-199 characters, got {len(JOKE)}")
    if "\n" in JOKE or "\r" in JOKE:
        raise SystemExit("entry must be a single line")
    if not JOKE.strip():
        raise SystemExit("entry must not be only whitespace")
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
