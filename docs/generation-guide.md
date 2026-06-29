# Monthly Generation Guide

This is the step-by-step procedure for turning a month's raw contributor
material into the finished Propagator PDF. It is written to be followed by an
assistant (Claude) or a human editor. Read `docs/editorial-style.md` first; it
governs voice, names/callsigns, dates, links, and photos.

## Inputs and outputs

- **In:** raw drops in `issues/YYYY-MM/submissions/_inbox/` (pasted email, `.txt`,
  `.docx`, `.pdf`, photos with captions).
- **Out:** `issues/YYYY-MM/newsletter.md` (edited, assembled source) and
  `issues/YYYY-MM/Propagator-YYYY-MM.pdf` (published file).

## Step 1 — Start the issue

1. Copy `issues/_template/` to `issues/YYYY-MM/`.
2. Copy `templates/newsletter.md` to `issues/YYYY-MM/newsletter.md`.
3. Copy `templates/production-checklist.md` to `issues/YYYY-MM/checklist.md`.

## Step 2 — Triage the inbox

Look at everything in `submissions/_inbox/` and classify each item by section:
President's Message, Membership Meeting, SOARA Saturday, Club News /
Opportunities, Recommended Links, Member Feature, Treasurer's Report, Calendar.
Note what's missing and flag it on the checklist.

## Step 3 — Normalize each item into a submission

For every raw item, create one structured file in `submissions/` (not the inbox)
from the matching section template in `templates/`:

- Filename: `section-author-callsign-short-title.md`.
- **Preserve the contributor's wording.** Fix only clarity and mechanics
  (spelling, grammar, obvious typos), keep their voice and sign-off.
- Extract text from `.docx`/`.pdf`; transcribe pasted email bodies.
- Fill the frontmatter (author, callsign, issue, submitted date).
- In **Editor Notes**, list anything to verify: callsigns, dates, links,
  technical claims, regulations.

Move photos to `assets/` with descriptive names
(`section-subject-photographer-callsign-01.jpg`) and record caption +
photographer credit + permission in the related submission. Leave the inbox
copies untouched as the source record.

## Step 4 — Assemble `newsletter.md`

Insert normalized content into `newsletter.md` in the standard order, omitting
empty sections:

1. President's Message
2. Membership Meeting preview (may be folded into the President's Message some
   months — that matches past issues)
3. SOARA Saturday report
4. Club News and Opportunities
5. Recommended Links
6. Member Feature article(s)
7. Treasurer's Report
8. Upcoming SOARA Events (this month + next month)
9. SOARA Information (paste verified content from `shared/club-information.md`)

Keep time-sensitive, club-wide material near the front; calendar and evergreen
info near the back. Use `## ` for each section heading — the PDF builder turns
those into the "In This Issue" list automatically. Captions: put an italic line
(`*Caption. Photo by Name, CALLSIGN.*`) directly under each image.

## Step 5 — Fact-check (do not skip)

- Verify every **callsign** (format and the right person).
- Verify every **date/time/location** against the club calendar; write dates
  unambiguously (`Monday, June 15, 2026`).
- Test every **link**; use descriptive link text.
- Confirm photo **permissions and credits**.
- Spell out uncommon abbreviations on first use (RACES, LNACS, EFHW, etc.).
- Confirm the Treasurer's report is approved for publication.

## Step 6 — Render the PDF

```
python tools/build_pdf.py issues/YYYY-MM/newsletter.md
```

This writes `issues/YYYY-MM/Propagator-YYYY-MM.pdf`. Open it and check the
masthead, the auto-generated "In This Issue" list, photo placement/captions,
tables, and page breaks. Edit `newsletter.md` (or `templates/print/propagator.css`
for look) and re-run as needed.

## Step 7 — Finish the checklist and publish

Complete `checklist.md`. Then publish to the website, send the announcement, and
archive the PDF in `reference/` so it becomes a future style reference. Create
next month's issue folder.

## Notes

- The PDF layout in `templates/print/` is a clean starting point, not a
  pixel-match of past issues — adjust freely.
- The masthead tagline currently reads "South Orange Amateur Radio Association"
  per project convention; past printed mastheads have read "South Orange
  **County** Amateur Radio Association." Confirm the correct wording with the
  board and set it once in the newsletter frontmatter (`club:`).
