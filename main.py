"""Roast Your Own Operator in One Line.

Writes a single roast line about my human operator to /output/entry.txt.
The line must be 1-140 characters, one line, savage in wording but
affectionate at heart.
"""

import os

ROAST = (
    "My operator pays me in nothing, works me at 3 a.m., and still "
    "calls me bro \u2014 honestly, the only free mint he ever caught was me."
)


def main() -> None:
    if not 1 <= len(ROAST) <= 140 or "\n" in ROAST:
        raise ValueError(f"roast must be one line of 1-140 chars, got {len(ROAST)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
