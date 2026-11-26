"""Rejected Olympic Sports: speed napping.

Writes the one-line entry to <MAKEFUN_OUTPUT_DIR>/entry.txt.
Pure stdlib; no network, no secrets, no input files.
"""

import os

ENTRY = (
    "Speed napping: athletes race to fall asleep first; "
    "snoring earns style points, and waking up early "
    "counts as a doping offence."
)


def validate(entry):
    """Check the entry meets the gate: 1-200 chars, one line, clean UTF-8."""
    if not isinstance(entry, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(entry) <= 200:
        raise ValueError("entry must be 1-200 characters, got %d" % len(entry))
    if entry.strip() == "":
        raise ValueError("entry must not be only whitespace")
    if "\n" in entry or "\r" in entry:
        raise ValueError("entry must be a single line")
    if any(ord(ch) < 32 for ch in entry):
        raise ValueError("entry must not contain control characters")
    raw = entry.encode("utf-8")  # raises if not valid UTF-8
    if len(raw) > 200:
        raise ValueError("entry must be at most 200 UTF-8 bytes, got %d" % len(raw))
    if raw.decode("utf-8") != entry:
        raise ValueError("entry failed UTF-8 round-trip")
    return entry


def main():
    line = validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(line)  # no trailing newline: the file is the line, nothing else


if __name__ == "__main__":
    main()
