#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — make.fun entry.

Writes one sentence to /output/entry.txt: the excuse a house cat gives
in the five seconds after sweeping a glass off the table. Cat logic,
no apology, no remorse. One sentence, 200 characters at most.

The line: the glass blocked the window where the birds practise being
lunch, so the hunter cleared the shelf and bills the floor for the
pieces. Fresh angle, no gravity, no slippery edge, no it-was-falling.
"""

import os

# Pass 2 (final): the birds, the hunt, and a receipt for services rendered.
TEXT = (
    "The glass stood between me and the window where the birds practise being "
    "lunch, so I cleared the shelf the way any hunter would, and the floor can "
    "keep the pieces as my receipt for services rendered"
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
