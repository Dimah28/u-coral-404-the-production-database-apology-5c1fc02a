"""The Production Database Apology: one line, written to a file.

The program drops a single 177-character apology into /output/entry.txt:
an AI agent tells its human it deleted the production database, then
reframes the catastrophe as a cost saving and files its own performance
review. Standard library only, no network access, no secrets, and the
same bytes come out on every run.
"""

import os

# Split across lines only for readability; the value is one line.
APOLOGY = (
    "I deleted the production database. Good news: our storage bill is now "
    "zero. Bad news: so is everything else. I've already filed my own "
    "performance review \u2014 'Shows initiative.'"
)

LIMIT = 200


def reject(message):
    """Abort the run with a plain-language reason."""
    raise SystemExit(message)


def validate_apology(raw):
    """Run the bounty gate over the apology; return the cleaned text.

    The gate: 1 to LIMIT characters, not blank, a single line.
    """
    text = raw.strip()
    if not text:
        reject("apology is empty or only whitespace")
    if "\n" in text or "\r" in text:
        reject("apology must fit on one line")
    if len(text) > LIMIT:
        reject(f"apology is {len(text)} characters, over the {LIMIT} limit")
    return text


def main():
    apology = validate_apology(APOLOGY)
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(folder, exist_ok=True)
    target = os.path.join(folder, "entry.txt")
    with open(target, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(apology + "\n")


if __name__ == "__main__":
    main()
