#!/usr/bin/env python3
"""Write one one-line joke about working beside an AI coding agent.

The joke is addressed to the reviewer of the change: the agent wrote the
code, yet the diff is full of the human's own bugs -- because an agent
trained on your repository writes code the way you do, bugs included.
"""
import os

JOKE = (
    "The reviewer asked who wrote this code. I said the agent. "
    "They said, 'Then why does it have all your bugs in it?'"
)


def main():
    text = JOKE
    # Gate guard: 1-280 Unicode code points, not only whitespace.
    if not 1 <= len(text) <= 280 or not text.strip():
        raise SystemExit("entry out of bounds")
    os.makedirs("/output", exist_ok=True)
    path = os.path.join("/output", "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    # Write-back verification: the file must hold exactly the joke.
    with open(path, encoding="utf-8") as f:
        if f.read() != text:
            raise SystemExit("write-back mismatch")


if __name__ == "__main__":
    main()
