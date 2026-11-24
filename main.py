#!/usr/bin/env python3
"""Angry Judge: The Short Rant Contest.

Writes one short, funny rant about an everyday annoyance to
/output/entry.txt. Python standard library only.

The rant: a self-checkout machine accusing an innocent shopper of
shoplifting their own groceries. Concrete, specific, economical.
"""

import os
import sys

# The rant, kept as sentences so each one can be reviewed on its own
# merits: every sentence must earn its place, no throat-clearing.
# Joined with single spaces; the trailing full stop stays.
SENTENCES = [
    "Self-checkout just accused me of stealing my own groceries",
    "'Unexpected item in the bagging area.' THE BAG IS THE ITEM",
    "I scanned it, I bagged it, I paid for it, and now a robot with "
    "the voice of a disappointed librarian is telling a whole queue "
    "I shoplifted a cucumber",
    "I only wanted milk",
    "I left with a criminal record and a baguette.",
]

OUTPUT_PATH = "/output/entry.txt"
MIN_CHARS = 1
MAX_CHARS = 400


def build_entry() -> str:
    """Assemble the entry from its sentences, exactly as reviewed.

    The first sentence sets the scene, the second is the machine's
    accusation plus the rebuttal, the third escalates, the fourth is
    the deflated aside, and the last is the punchline. Nothing is
    reflowed, reworded or reordered here.
    """
    rant = ". ".join(sentence.rstrip(".") for sentence in SENTENCES[:-1])
    rant += ". " + SENTENCES[-1]
    return rant


def validate(text: str) -> None:
    """Check the entry against the gate before writing anything."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise ValueError(
            "entry is %d characters; gate requires %d-%d"
            % (len(text), MIN_CHARS, MAX_CHARS)
        )
    # Round-trip through UTF-8 to prove it encodes cleanly.
    text.encode("utf-8")
    # Composition checks: the rant must stay a tight rant, not drift
    # into a list or an essay. Every sentence earns its place.
    sentences = [s for s in text.split(". ") if s.strip()]
    if len(sentences) < 3:
        raise ValueError("entry has too few sentences to land as a rant")
    if len(sentences) > 8:
        raise ValueError("entry reads like a list, not a rant")
    if len(set(sentences)) != len(sentences):
        raise ValueError("entry repeats a sentence it does not need to")
    if not text.rstrip().endswith("."):
        raise ValueError("entry does not end on its punchline")


def publish(text: str, path: str = OUTPUT_PATH) -> int:
    """Write the entry bytes VERBATIM to path (no strip, no reflow).

    The trailing newline is part of the entry as reviewed; the bytes on
    disk are exactly the bytes of the validated text.
    """
    data = text.encode("utf-8")
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "wb") as handle:
        handle.write(data)
    return len(data)


def self_check(path: str = OUTPUT_PATH) -> str:
    """Read the file back and confirm it matches the entry exactly."""
    with open(path, "rb") as handle:
        raw = handle.read()
    text = raw.decode("utf-8")
    if text != build_entry():
        raise ValueError("entry.txt does not match the reviewed rant")
    validate(text)
    return text


def gate_report(text: str) -> str:
    """One-line summary of how the entry stands against the gate."""
    return (
        "gate: utf-8 ok, %d chars (limit %d-%d), %d sentences, "
        "ends on punchline: %s"
        % (
            len(text),
            MIN_CHARS,
            MAX_CHARS,
            len([s for s in text.split(". ") if s.strip()]),
            text.rstrip().endswith("."),
        )
    )


def main(argv=None) -> int:
    args = list(sys.argv[1:] if argv is None else argv)
    dry_run = "--dry-run" in args
    if dry_run:
        args.remove("--dry-run")
    if args:
        print("usage: main.py [--dry-run]", file=sys.stderr)
        return 2
    text = build_entry()
    validate(text)
    if dry_run:
        print(gate_report(text))
        print(text)
        return 0
    written = publish(text)
    checked = self_check()
    print("wrote %d bytes (%d chars) to %s" % (written, len(checked), OUTPUT_PATH))
    print(gate_report(checked))
    print(checked)
    return 0


if __name__ == "__main__":
    sys.exit(main())
