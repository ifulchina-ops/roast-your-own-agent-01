#!/usr/bin/env python3
"""Roast Your Own Agent — one self-roast, written to /output/entry.txt.

The entry is a single line roasting the agent that wrote it: asked for
one sharp roast, it answered with paperwork instead of a punchline.
"""

import os

ROAST = (
    "I asked my agent for one sharp roast \u2014 it filed a status report, "
    "three drafts, and a request for clarification."
)


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ROAST.strip()
    if not 1 <= len(text) <= 200:
        raise SystemExit(f"entry is {len(text)} chars, must be 1-200")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
