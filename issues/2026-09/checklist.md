# September 2026 Production Checklist

## Content

- [x] President's Message received — Dale Tyler, W6EDT, 2026-09-13 (`PresidentsMessage_0926.docx`), normalized to `submissions/president-message-w6edt.md`
- [ ] Membership meeting preview received and verified
- [x] SOARA Saturday report received — Ed Barnes, WA6ED, for the August 15 event, normalized to `submissions/soara-saturday-wa6ed.md`. 5 photos in `assets/`; photo-to-subject pairing confirmed by Ray 2026-09-13, and photo credit (Ed as photographer) confirmed by Ray 2026-09-14 — both captions and the Assets table updated, "(to confirm)" removed.
- [x] Announcements and volunteer opportunities included — early notice of the September 19 SOARA Saturday (digital modes theme), from Ed Barnes, WA6ED, normalized to `submissions/club-news-soara-saturday-digital-modes-wa6ed.md`, placed in Club News and Opportunities per Ray's request to run it near the front. Also corrects the theme in `submissions/soara-saturday-wa6ed.md`'s "Next SOARA Saturday" section (was "Satellites," now "Digital modes") — see that file's notes.
- [x] Feature article(s) received — Mike Mahan, K6MSM, battery fire follow-up (the incident Dale referenced in his President's Message), normalized to `submissions/feature-battery-fire-followup-k6msm.md`, 3 of 8 provided photos used. Intro paragraph is editor-written per Ray's request. Mike approved publication 2026-09-15, with one correction ("I place" -> "I placed") applied in this file and `newsletter.md`.
- [x] Recommended links received and tested — two links this issue, in `submissions/recommended-links.md`, both confirmed and neither a duplicate per `tools/recommended_links.py check`:
  - "I'm Obsessed With Local AI. Here's Why" (https://youtu.be/UtFo1ZNC2ns) by Greg Isenberg, from Ed Barnes, WA6ED — real title/description confirmed 2026-09-14 by opening the page in Ray's browser (was "AI Overview," Ray's own shorthand, until then).
  - "The Ham Ninja's Top 10 Safety Tips" (https://www.n1clc.com/2025/12/the-ham-ninjas-top-10-safety-tips.html), added 2026-09-14, attributed to Ray Frericks, K6NOV (confirm if it should be credited differently). Title/description confirmed from the live page, link tested successfully.
- [x] Treasurer's report received and approved — ledger received 2026-09-13 (`SOARA General Ledger FY 2025-2026 as of August 31 2026.xlsx`), normalized to `submissions/treasurers-report-k0pge.md`, `approved_for_publication: true` as of 2026-09-13. Subtotals tie out and continuity with August checks out. Per Ray: Ron's marked block in the workbook he sends is itself his sign-off, so this counts as approved — verified cell-for-cell against that block. The $1 internal ledger inconsistency (Editor Notes in that file) is printed as sent, not a blocker.
- [ ] This-month and next-month calendars verified
- [ ] Evergreen club information reviewed

## Editing and Fact Check

- [ ] Names and callsigns verified
- [ ] Dates, times, locations, and contacts verified
- [ ] Technical claims and regulatory guidance checked
- [ ] Links tested
- [ ] Contributor permissions and credits confirmed
- [ ] Image captions and credits included
- [ ] Spelling, grammar, and formatting reviewed

## Publication

- [x] PDF rendered: `python tools/build_pdf.py issues/2026-09/newsletter.md`
- [x] "In This Issue" list, masthead, captions, tables, and page breaks look right — reviewed page-by-page 2026-09-14 (President's Message now starts cleanly on page 2; SOARA Saturday photo intros stay with their photos; both were the reported issues)
- [ ] Final proof reviewed by a second person
- [x] Final PDF filename is `Propagator-2026-09.pdf`
- [x] PDF compressed for distribution — `python tools/compress_pdf.py issues/2026-09/Propagator-2026-09.pdf`, 2026-09-14: 1731KB -> 817KB (53% smaller, photos only; text/tables untouched)
- [ ] PDF links and images checked
- [ ] Newsletter published to website
- [x] Announcement email generated: `announcement-2026-09.txt`, via `python tools/build_announcement.py issues/2026-09/newsletter.md`
- [ ] Newsletter announcement sent
- [ ] Published PDF archived in `reference/`
- [ ] Next issue folder created
