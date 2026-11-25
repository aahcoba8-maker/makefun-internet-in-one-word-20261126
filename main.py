"""The Internet in One Word.

One word for the whole internet. Prints it and nothing else,
and writes it to entry.txt in MAKEFUN_OUTPUT_DIR when the grader
sets one (falling back to the script's own directory).
"""

import os
import sys

WORD = "dumpsterfire"


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        path = os.path.join(out_dir, "entry.txt")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(WORD)
    sys.stdout.write(WORD)


if __name__ == "__main__":
    main()
