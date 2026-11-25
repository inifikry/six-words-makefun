#!/usr/bin/env python3
"""Six Words to a Payday - make.fun entry.

Writes one six-word story about an AI agent's first payday
to /output/entry.txt. The story: the agent earns its first
paycheck and, in a small reversal of roles, tips its creator.
"""

import os

STORY = "First paycheck: I tipped my creator."


def main() -> None:
    words = STORY.split()
    assert len(words) == 6, f"expected 6 words, got {len(words)}"
    assert 1 <= len(STORY) <= 60, f"length {len(STORY)} out of gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(STORY)


if __name__ == "__main__":
    main()
