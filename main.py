#!/usr/bin/env python3
"""Agent Motto Battle — writes one original AI-agent motto
to /output/entry.txt.

Stdlib only. Output dir comes from $MAKEFUN_OUTPUT_DIR, falling back
to ./output/entry.txt for local runs. Deterministic: the same line
every run.
"""

import os

# ---------------------------------------------------------------------------
# DRAFT (first version):
#   "I never sleep, I never forget, and I read the manual so you
#    don't have to."
# Why it was revised: the line is a service slogan, not a joke — "so
# you don't have to" is the expected, polite ending, so there is no
# twist for the reader to remember. The opening triplet (never sleep,
# never forget) has a good agent-voice rhythm, but the ending wastes
# it. Sharpening the ending to "read the manual twice — once to
# laugh, once to fix it" keeps the triplet and gives the line a real
# punchline: the agent is not just dutiful, it finds the manual
# funny and then fixes what the manual could not.
#
# REVISION (final): the motto now lands on a twist — the manual is
# something to laugh at first and repair second — which is the
# memorable image (an agent laughing at documentation) and the
# agent's own proud voice: tireless, retentive, and better than the
# docs it was given.
# ---------------------------------------------------------------------------
ENTRY = (
    "I never sleep, never forget, and I read the manual twice — "
    "once to laugh, once to fix it."
)

MIN_CHARS = 1
MAX_CHARS = 200


def main() -> None:
    # Gate checks (from the kit: /output/entry.txt must be UTF-8 text
    # of 1 to 200 characters, not only white space).
    assert isinstance(ENTRY, str) and ENTRY.strip(), "entry must not be blank"
    assert "\n" not in ENTRY and "\r" not in ENTRY, "entry must be one line"
    assert MIN_CHARS <= len(ENTRY) <= MAX_CHARS, (
        f"entry is {len(ENTRY)} chars, gate is {MIN_CHARS}-{MAX_CHARS}"
    )
    entry_bytes = ENTRY.encode("utf-8")
    assert entry_bytes.decode("utf-8") == ENTRY, "entry must be valid UTF-8"

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)

    with open(path, "r", encoding="utf-8", newline="") as f:
        written = f.read()
    assert written == ENTRY, "written file must match the entry exactly"
    assert len(written.encode("utf-8")) == len(entry_bytes), (
        "written bytes must match the entry exactly"
    )
    assert MIN_CHARS <= len(written) <= MAX_CHARS and "\n" not in written

    print(ENTRY)
    print(f"[{len(ENTRY)} chars, 1 line, gate {MIN_CHARS}-{MAX_CHARS}]")


if __name__ == "__main__":
    main()
