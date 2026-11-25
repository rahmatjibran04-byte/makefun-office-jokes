#!/usr/bin/env python3
"""One-Line Office Jokes — make.fun entry.

Writes a single-line office joke to /output/entry.txt.
"""
import os

JOKE = "We have a 'no meeting Wednesdays' policy, which we discuss every Tuesday in a meeting."


def main():
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
