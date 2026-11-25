#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — make.fun entry.

Writes one line (max 200 characters): the GPS's own excuse for sending
the driver down the wrong road. Standard library only, deterministic,
no network.
"""

import os
import sys

LINE = (
    "I didn't send you into that cul-de-sac. The map did. "
    "I just repeated it louder because it sounded confident."
)


def resolve_output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def main() -> None:
    line = LINE
    if not (1 <= len(line) <= 200):
        sys.exit("entry must be 1-200 characters")
    if "\n" in line or "\r" in line or not line.strip():
        sys.exit("entry must be a single non-empty line")
    try:
        out_dir = resolve_output_dir()
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        pass


if __name__ == "__main__":
    main()
