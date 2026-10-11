# October 2026 Production Checklist

## Content

- [x] President's Message received
- [x] Membership meeting preview received and verified
- [x] SOARA Saturday report received
- [x] Announcements and volunteer opportunities included
- [x] Feature article(s) received
- [x] Recommended links received and tested; `recommended_links.py check` confirms none were previously recommended
- [ ] Treasurer's report received and approved — RECEIVED; not approved (3 small tie-out discrepancies flagged for Ron, see submissions/treasurers-report-k0pge.md)
- [ ] This-month and next-month calendars verified — October per Ray; November dates inferred from pattern (Nov 14/16/23, auction TBD), need confirmation
- [ ] Evergreen club information reviewed

## Editing and Fact Check

- [ ] Names and callsigns verified — open: Mark KU6CZG (Ed) vs KO6CZG
- [ ] Dates, times, locations, and contacts verified
- [ ] Technical claims and regulatory guidance checked
- [ ] Links tested
- [ ] Contributor permissions and credits confirmed
- [x] Image captions and credits included
- [ ] Spelling, grammar, and formatting reviewed

## Publication

- [x] PDF rendered: `python tools/build_pdf.py issues/YYYY-MM/newsletter.md`
- [x] (first draft, 17 pp) "In This Issue" list, masthead, captions, tables, and page breaks look right
- [ ] Final proof reviewed by a second person
- [x] Final PDF filename is `Propagator-YYYY-MM.pdf`
- [ ] PDF links and images checked
- [ ] Newsletter published to website
- [ ] Announcement email generated: `python tools/build_announcement.py issues/YYYY-MM/newsletter.md` (see `templates/announcement-email.md`)
- [ ] Newsletter announcement sent
- [ ] Published PDF archived in `reference/`
- [ ] Next issue folder created

## Draft notes (2026-10-11)

- First draft built for Ray's review; no Club News section this month (nothing submitted).
- Kevin AJ6EE feature is AI-assisted per his note — Ray to decide on inclusion/disclosure.
- Ed's photo captions matched to images in email order; Ray to confirm.
- `figure img` max-height added to templates/print/propagator.css to keep portrait photos/screenshots from filling a page.
- PDF compressed with tools/compress_pdf.py (re-run after any rebuild).
