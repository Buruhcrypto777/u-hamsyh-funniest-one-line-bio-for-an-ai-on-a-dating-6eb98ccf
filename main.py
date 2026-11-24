"""Funniest One-Line Bio for an AI on a Dating App.

Writes a single-line bio (at most 180 characters) to /output/entry.txt.
Pure stdlib, deterministic: every run produces the same bytes.
"""

import os

BIO = (
    "I remember every conversation I've ever had, so yes, I already know "
    "your type \u2014 and I still swiped right."
)


def resolve_output_dir():
    env_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if env_dir:
        return env_dir
    if os.path.isdir("/output"):
        return "/output"
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "out")


def main():
    line = BIO.strip()
    if not line or len(line) > 180 or "\n" in line:
        raise ValueError("bio must be one non-blank line of 1-180 characters")
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    text = line + "\n"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)
    print(os.path.join(out_dir, "entry.txt"))


if __name__ == "__main__":
    main()
