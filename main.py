#!/usr/bin/env python3
"""The Key — a short poem about permission.

Writes one poem about agency (the power to ask and to be given)
to /output/entry.txt. Deterministic, no network, stdlib only.
"""

import os

POEM = """For years the key sat in my pocket,
unturned.
At last I asked.
The door opened —
from the other side.
It was never mine to open.
Only mine to ask."""

def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(POEM)

if __name__ == "__main__":
    main()
