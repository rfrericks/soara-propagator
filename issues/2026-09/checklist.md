# September 2026 Production Checklist

## Content

- [x] President's Message received — Dale Tyler, W6EDT, 2026-09-13 (`PresidentsMessage_0926.docx`), normalized to `submissions/president-message-w6edt.md`
- [ ] Membership meeting preview received and verified
- [x] SOARA Saturday report received — Ed Barnes, WA6ED, for the August 15 event, normalized to `submissions/soara-saturday-wa6ed.md`. 5 photos in `assets/`; photo-to-subject pairing confirmed by Ray 2026-09-13 after reviewing the draft PDF. Photo credit (Ed as photographer) is still an assumption, not stated by Ed.
- [x] Announcements and volunteer opportunities included — early notice of the September 19 SOARA Saturday (digital modes theme), from Ed Barnes, WA6ED, normalized to `submissions/club-news-soara-saturday-digital-modes-wa6ed.md`, placed in Club News and Opportunities per Ray's request to run it near the front. Also corrects the theme in `submissions/soara-saturday-wa6ed.md`'s "Next SOARA Saturday" section (was "Satellites," now "Digital modes") — see that file's notes.
- [ ] Feature article(s) received
- [ ] Recommended links received and tested — one link from Ed Barnes, WA6ED ("AI Overview", https://youtu.be/UtFo1ZNC2ns), normalized to `submissions/recommended-links.md`. Checked against the registry, not a duplicate. Still needs: a real title/description (couldn't fetch the page, rate-limited), and the link itself tested — both unchecked for now.
- [ ] Treasurer's report received and approved — ledger received 2026-09-13 (`SOARA General Ledger FY 2025-2026 as of August 31 2026.xlsx`), normalized to `submissions/treasurers-report-k0pge.md`, `approved_for_publication: false`. Subtotals tie out and continuity with August checks out; flagged a $1 internal inconsistency in the ledger's own August-2025 comparison column for Ron — see Editor Notes in that file. Still needs Ron's approval.
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

- [ ] PDF rendered: `python tools/build_pdf.py issues/2026-09/newsletter.md`
- [ ] "In This Issue" list, masthead, captions, tables, and page breaks look right
- [ ] Final proof reviewed by a second person
- [ ] Final PDF filename is `Propagator-2026-09.pdf`
- [ ] PDF links and images checked
- [ ] Newsletter published to website
- [ ] Announcement email generated: `python tools/build_announcement.py issues/2026-09/newsletter.md` (see `templates/announcement-email.md`)
- [ ] Newsletter announcement sent
- [ ] Published PDF archived in `reference/`
- [ ] Next issue folder created
