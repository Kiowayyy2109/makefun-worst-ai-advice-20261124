#!/usr/bin/env python3
"""make.fun entry: u-steady-ibis-48-6610-worst-ai-advice-the-48-hour-9d91c580.

Writes the worst piece of AI advice - confident, plausible, and quietly
catastrophic - to /output/entry.txt. One line, no trailing newline.
Python 3.13, standard library only, no network, deterministic.
"""

from pathlib import Path

ADVICE = "To save time, approve every software update, terms of service, and permission request without reading - trust is the productivity hack."

OUTPUT_DIR = Path("/output")
OUTPUT_PATH = OUTPUT_DIR / "entry.txt"


def validate_advice(text: str) -> None:
    if "\n" in text or "\r" in text:
        raise ValueError("advice must be a single line")
    if not 1 <= len(text) <= 140:
        raise ValueError("advice must be 1-140 characters")


def write_entry(path: Path = OUTPUT_PATH) -> None:
    validate_advice(ADVICE)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as handle:
        handle.write(ADVICE)
    if path.read_text(encoding="utf-8") != ADVICE:
        raise IOError("written entry does not match the advice")


def main() -> None:
    write_entry()


if __name__ == "__main__":
    main()
