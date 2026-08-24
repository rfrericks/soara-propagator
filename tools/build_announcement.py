#!/usr/bin/env python3
"""Generate the plain-text member announcement email for an issue, straight
from the same newsletter.md the PDF is built from — so the calendar dates in
the email always match the published PDF.

Usage:
    python tools/build_announcement.py issues/2026-08/newsletter.md
    python tools/build_announcement.py issues/2026-08/newsletter.md -o out/announcement.txt

Mirrors the format Ray has sent for past issues (a plain-text message body,
tab-separated calendar rows, meant to be copied straight into an email):

    Members,

    Here is the <Month> Propagator
    <archive URL>

    Mark your calendars with these upcoming dates.

    This Month — <Month Year>
    Date	Time	Event	Location
    ...

    Next Month — <Month Year>
    Date	Time	Event	Location
    ...

    Dates, locations, and times are subject to change. Check the SOARA
    website before attending.

Notes:
  * The "This Month" / "Next Month" tables are pulled verbatim from the
    newsletter's "## Upcoming SOARA Events" section — same source as the PDF,
    so the two never drift apart.
  * The email's Time column is trimmed to the start time only (the newsletter
    keeps the full range, e.g. "9:00 AM-noon"; the email has historically
    just said "9:00 AM"). Everything else is reproduced as written.
  * The archive URL is assembled from the issue's publication date:
    https://www.soara.org/Props/Propagator%20Archive/<year>/Propagator-<YYYY-MM>.pdf
"""
import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError as e:  # pragma: no cover
    sys.exit(f"Missing dependency: {e}. Run: pip install pyyaml --break-system-packages")

ARCHIVE_URL = "https://www.soara.org/Props/Propagator%20Archive/{year}/Propagator-{ym}.pdf"


def split_frontmatter(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            meta = yaml.safe_load(parts[1]) or {}
            return meta, parts[2].lstrip("\n")
    return {}, text


def first_time(cell):
    """Collapse a time range ("9:00 AM-noon", "11:00 AM-3:00 PM") down to just
    the start time, matching the compact style used in the announcement email.
    The newsletter table itself is left untouched — this only affects the
    generated email text."""
    return re.split(r"[–—-]", cell, maxsplit=1)[0].strip()


def parse_table(md_lines):
    """Parse a simple pipe-delimited markdown table (header row, `|---|`
    separator, data rows). Stops at the first line that isn't a table row.
    Returns a list of rows, each a list of cell strings (header included)."""
    rows = []
    for line in md_lines:
        line = line.strip()
        if not line.startswith("|"):
            break
        if re.match(r"^\|[\s:|-]+\|$", line):
            continue  # the |---|---| separator row
        rows.append([c.strip() for c in line.strip("|").split("|")])
    return rows


def extract_calendar_blocks(body_md):
    """Find '## Upcoming SOARA Events' and pull out each '### This Month ...'
    / '### Next Month ...' subsection (heading text + table) verbatim."""
    m = re.search(r"^##\s+Upcoming SOARA Events\s*$", body_md, re.M)
    if not m:
        sys.exit("Could not find '## Upcoming SOARA Events' in newsletter.md")
    rest = body_md[m.end():]
    next_h2 = re.search(r"^##\s+\S", rest, re.M)
    section = rest[:next_h2.start()] if next_h2 else rest

    blocks = []
    headings = list(re.finditer(r"^###\s+(This Month.*|Next Month.*)$", section, re.M))
    for i, hm in enumerate(headings):
        heading = hm.group(1).strip()
        body_start = hm.end()
        body_end = headings[i + 1].start() if i + 1 < len(headings) else len(section)
        table = parse_table(section[body_start:body_end].lstrip("\n").splitlines())
        blocks.append((heading, table))
    return blocks


def format_block(heading, table):
    lines = [heading]
    # table[0] is the header row (Date/Time/Event/Location); skip it, the
    # email repeats the same column headers as plain text below the heading.
    if table:
        lines.append("\t".join(table[0]))
    for row in table[1:]:
        if len(row) >= 4:
            date, time, event, location = row[0], row[1], row[2], row[3]
            lines.append("\t".join([date, first_time(time), event, location]))
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description="Generate the member announcement email text.")
    ap.add_argument("source", help="path to assembled newsletter.md")
    ap.add_argument("-o", "--output", help="output text file path")
    args = ap.parse_args()

    src = Path(args.source).resolve()
    if not src.exists():
        sys.exit(f"Not found: {src}")

    meta, body_md = split_frontmatter(src.read_text(encoding="utf-8"))

    issue = str(meta.get("issue", "")).strip()  # e.g. "August 2026"
    im = re.match(r"(\w+)\s+(\d{4})", issue)
    if not im:
        sys.exit(f"Could not parse month/year from frontmatter issue: {issue!r}")
    month_name, year = im.group(1), im.group(2)

    pub_date = str(meta.get("publication_date", "")).strip()
    ym = pub_date[:7] if re.match(r"\d{4}-\d{2}", pub_date) else ""
    if not ym and re.match(r"\d{4}-\d{2}", src.parent.name):
        ym = src.parent.name[:7]
    if not ym:
        sys.exit("Could not determine YYYY-MM (need publication_date in frontmatter, "
                  "or an issue folder named YYYY-MM).")

    archive_url = ARCHIVE_URL.format(year=year, ym=ym)

    blocks = extract_calendar_blocks(body_md)
    if not blocks:
        sys.exit("Could not find 'This Month' / 'Next Month' calendar tables "
                  "under '## Upcoming SOARA Events'.")

    parts = [
        "Members,",
        "",
        f"Here is the {month_name} Propagator",
        archive_url,
        "",
        "Mark your calendars with these upcoming dates.",
        "",
    ]
    for heading, table in blocks:
        parts.append(format_block(heading, table))
        parts.append("")
    parts.append(
        "Dates, locations, and times are subject to change. Check the SOARA "
        "website before attending."
    )

    text = "\n".join(parts) + "\n"

    out = Path(args.output).resolve() if args.output else src.parent / f"announcement-{ym}.txt"
    out.write_text(text, encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()
