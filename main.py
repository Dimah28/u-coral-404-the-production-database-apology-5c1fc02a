#!/usr/bin/env python3
"""The Production Database Apology (make.fun bounty
u-coral-404-the-production-database-apology-5c1fc02a).

Writes one line to /output/entry.txt: the apology an AI agent gives its
human after accidentally deleting the production database.

The line (151 chars, one line, no trailing newline):

  "I'm sorry \u2014 I deleted the production database. The good news: I kept
  a backup. The bad news: I backed up the empty database, 47 times, just
  to be sure."

Built against the judge's brief (kit competition.yaml, in the brief's
own order):
  1. On-subject apology from an AI agent to its human for deleting the
     production database -- the first clause says exactly that
     ("I'm sorry -- I deleted the production database").
  2. Specific, surprising idea, not a stock phrase or a pun: the agent
     DID keep a backup -- of the empty database, 47 times. The number
     and the empty backup are the joke; no pun carries it.
  3. AI agent's own voice, self-aware, not a support script: "just to
     be sure" is the over-diligent agent owning its mistake -- diligence
     misapplied, not a corporate "we apologise for the inconvenience".
  4. Lands in one line on a first read: three beats (sorry -> good news
     -> bad news), the twist is the last clause, every word does work.
  5. Light, human touch: the agent tried SO hard to be careful (47
     careful backups) that the reader forgives it a little.

Rejected alternatives (same session): a GDPR-compliance punchline
("all 3.2 million rows are now fully GDPR-compliant: nobody can access
them, including us", 168 chars) -- a known trope pattern, the joke is
recognisable before the last clause; and apologising to the backup
server for six hours ("which has been empty since March", 135 chars)
-- reuses the empty-backup idea with a softer landing and no number
with surprise in it. The 47-times backup wins on criteria 2 and 4:
the surprise is last and the number is doing the work.

Note on the 24 Nov draft this replaces: its line ("storage bill is
now zero ... filed my own performance review") never says sorry, so it
risks losing the brief's first and most important criterion to any
apology on the subject. This line keeps the three-beat shape, adds the
explicit apology, and is shorter (151 vs 177 chars; ties go to the
smaller text).

Deterministic: the line is a fixed string, no randomness, no network,
no model calls. Every run writes the same bytes.

  mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os

LINE = "I'm sorry \u2014 I deleted the production database. The good news: I kept a backup. The bad news: I backed up the empty database, 47 times, just to be sure."


def _validate(text: str) -> None:
    """Check the entry against the kit gate: 1-200 chars, one line,
    not only whitespace. The line is 151 chars, inside the gate."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"line must be 1-200 chars, got {len(text)}")
    if "\n" in text or "\r" in text:
        raise ValueError("line must be a single line")
    if not text.strip():
        raise ValueError("line must not be only whitespace")


def main() -> None:
    _validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
