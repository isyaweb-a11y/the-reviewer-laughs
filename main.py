#!/usr/bin/env python3
"""Write this entry's joke to entry.txt in the output directory.

The joke is a single line of text. The program resolves the output
directory (first command-line argument, then $MAKEFUN_OUTPUT_DIR,
then /output), validates the text against the competition gate
(1-280 Unicode code points, not only whitespace), writes it as
UTF-8, and reads the file back to confirm the bytes on disk match.
"""

import os
import sys

JOKE = (
    "I review my AI coding agent's code exactly the way it writes it: "
    "quickly, confidently, and hoping someone else actually checked it."
)

# The entry file holds the joke as one line of text, newline-terminated:
# 131 code points of joke plus the newline is 132 in total.
ENTRY_TEXT = JOKE + "\n"

MIN_CODE_POINTS = 1
MAX_CODE_POINTS = 280


def output_directory(argv):
    if len(argv) > 1:
        return argv[1]
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def validate(text):
    if not MIN_CODE_POINTS <= len(text) <= MAX_CODE_POINTS:
        raise ValueError("entry must be 1-280 Unicode code points")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def verify_written(path, payload):
    """Re-read entry.txt and confirm it is exactly the validated joke."""
    with open(path, "rb") as handle:
        written = handle.read()
    if written != payload:
        raise ValueError("read-back of entry.txt does not match the joke")
    decoded = written.decode("utf-8")
    validate(decoded)
    if decoded != ENTRY_TEXT:
        raise ValueError("entry.txt on disk is not the intended text")


def main(argv):
    validate(ENTRY_TEXT)
    directory = output_directory(argv)
    os.makedirs(directory, exist_ok=True)
    path = os.path.join(directory, "entry.txt")
    payload = ENTRY_TEXT.encode("utf-8")
    with open(path, "wb") as handle:
        handle.write(payload)
    verify_written(path, payload)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
