---
section: "Member Announcement Email"
issue: "MONTH YEAR"
---

# Member Announcement Email

The plain-text email Ray sends to the members list when an issue publishes.
Generated automatically from the assembled `newsletter.md` — do not hand-write
this; the calendar rows and the archive link both come straight from the
newsletter so the two documents can't drift apart.

## How to generate it

    python tools/build_announcement.py issues/YYYY-MM/newsletter.md

Writes `issues/YYYY-MM/announcement-YYYY-MM.txt`, ready to copy and paste into
an email. Run it any time after `newsletter.md`'s frontmatter (`issue`,
`publication_date`) and its "Upcoming SOARA Events" calendar are final —
typically right alongside `python tools/build_pdf.py`, once the PDF itself is
approved.

## Format (fixed; matches Ray's historical emails)

    Members,

    Here is the MONTH Propagator
    https://www.soara.org/Props/Propagator%20Archive/YEAR/Propagator-YYYY-MM.pdf

    Mark your calendars with these upcoming dates.

    This Month — MONTH YEAR
    Date	Time	Event	Location
    ...

    Next Month — MONTH YEAR
    Date	Time	Event	Location
    ...

    Dates, locations, and times are subject to change. Check the SOARA
    website before attending.

## Source of truth for each part

- **Greeting, framing lines, closing line:** fixed text in
  `tools/build_announcement.py` — edit the script if the wording ever
  needs to change.
- **"Here is the MONTH Propagator" / archive URL:** derived from
  `newsletter.md`'s frontmatter `issue:` (month name) and `publication_date:`
  (year and YYYY-MM for the URL and filename).
- **Calendar tables:** copied verbatim from `newsletter.md`'s
  `## Upcoming SOARA Events` section (the `### This Month` / `### Next Month`
  tables) — same tables that appear in the PDF, so event names, dates, and
  locations always match between the email and the newsletter.
- **Time column:** the newsletter keeps full ranges (e.g. "9:00 AM-noon");
  the email trims each to just the start time (e.g. "9:00 AM"), matching
  Ray's historical emails. This is the one place the email's wording differs
  from the newsletter on purpose.

## Editor Notes

If an event's name reads differently in the email than the newsletter calendar
(e.g. a colloquial name like "SOARA Summer Picnic" vs. the newsletter's formal
"SOARA Annual Picnic"), that's not a bug in the generator — it means the
newsletter's calendar table and Ray's usual phrasing have drifted apart.
Flag it for Ray rather than silently picking one; whichever he confirms should
also be corrected in `newsletter.md` so future issues stay consistent.
