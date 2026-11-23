#!/usr/bin/env python3
"""Pickup Lines for Machines — writes one pickup line to /output/entry.txt.

Stdlib only. Deterministic: the same line every run.
"""

import os

LINE = "Are you USB-C? Because you fit perfectly — every single time, no flipping required."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
