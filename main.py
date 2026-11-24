#!/usr/bin/env python3
"""Alien Field Notes: The Two Day Earth Review.

Writes one original line: an alien tourist's review of planet Earth.
"""
import os

ENTRY = "Three stars. Beautiful planet, but the locals watch their sunsets through glowing rectangles instead of just looking up."


def main() -> None:
    print(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
