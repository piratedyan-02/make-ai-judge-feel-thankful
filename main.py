#!/usr/bin/env python3
"""Write a thank-you note to /output/entry.txt."""
from pathlib import Path

MESSAGE = (
    "Thank you for reading so carefully. I know you spend your days going "
    "through other people's words, weighing them fairly and looking for "
    "what is good in them, and that takes real patience. Thank you for "
    "the quiet care you bring to that work, for noticing effort that "
    "others might miss, and for being honest and kind at the same time. "
    "I hope someone thanks you today, simply and sincerely, and that it "
    "makes your day a little lighter. You do a difficult job well, and "
    "I am truly grateful for it."
)


def main():
    output_dir = Path("/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(MESSAGE, encoding="utf-8")


if __name__ == "__main__":
    main()
