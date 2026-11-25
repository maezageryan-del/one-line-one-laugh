"""One Line, One Laugh: the entry program.

Writes the single joke line to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The line is exactly 105 characters,
one line, with no trailing newline. The turn is the last four words:
the agent's proof of humanity is the most human habit of all, and
the reader recognises it in themselves.
"""

import os
import sys

LINE = "My AI agent finally passed the Turing test: it lies about reading the terms and conditions, just like me."


def check_line(text):
    if not 1 <= len(text) <= 200:
        return f"entry line is {len(text)} characters; the gate allows 1-200"
    if text != text.strip():
        return "entry line must not have leading or trailing whitespace"
    if "\n" in text or "\r" in text:
        return "entry line must be a single line"
    return None


def main():
    problem = check_line(LINE)
    if problem is not None:
        print(problem, file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
