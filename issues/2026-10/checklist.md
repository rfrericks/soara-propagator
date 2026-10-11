# October 2026 Production Checklist

## Content

- [x] President's Message received
- [x] Membership meeting preview received and verified
- [x] SOARA Saturday report received
- [x] Announcements and volunteer opportunities included
- [x] Feature article(s) received
- [x] Recommended links received and tested; `recommended_links.py check` confirms none were previously recommended
- [x] Treasurer's report received and approved (Ron's marked block = sign-off; accepted by Ray 2026-10-11)
- [x] This-month and next-month calendars verified (November dates confirmed by Ray)
- [ ] Evergreen club information reviewed

## Editing and Fact Check

- [x] Names and callsigns verified (Mark corrected to KO6CZG)
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
- Kevin AJ6EE feature: Ray approved to run as is, no AI line.
- Ed's photo captions matched to images in email order; Ray to confirm.
- `figure img` max-height added to templates/print/propagator.css to keep portrait photos/screenshots from filling a page.
- PDF compressed with tools/compress_pdf.py (re-run after any rebuild).
- 2026-10-11 Ray review edits applied: treasurer approved, KO6CZG, RADE (Radio Autoencoder), November dates confirmed.
