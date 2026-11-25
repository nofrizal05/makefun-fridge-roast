#!/usr/bin/env python3
"""Fridge Roast: One Line, Biggest Laugh — make.fun entry.

A smart fridge, in its own voice, roasting the household it serves.
The program writes exactly one roast line to /output/entry.txt and
prints the same line to stdout. Standard library only, deterministic.
"""

import os

LINE = (
    "I beep when you leave my door open ten seconds, yet I've quietly "
    "guarded your March leftovers for eight months like they pay rent."
)


def main() -> None:
    # The gate allows 1-200 chars; this entry targets the 100-160 band.
    assert 100 <= len(LINE) <= 160, f"line is {len(LINE)} chars"
    assert "\n" not in LINE, "line must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
