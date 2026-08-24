# Monthly Newsletter Workflow

## Suggested Schedule

| Timing | Activity |
|---|---|
| 3 weeks before publication | Ask officers and members for submissions |
| 2 weeks before publication | Confirm meeting topic, calendar, and feature articles |
| 1 week before publication | Assemble the first draft and request missing material |
| 3-5 days before publication | Edit, fact-check, place photos, and proofread |
| Publication day | Export, publish, email, and archive |

## Roles

- **Editor:** Owns the schedule, assembly, editing, and publication.
- **Section owners:** Submit recurring reports and verify their facts.
- **Contributors:** Supply feature articles, captions, links, and photos.
- **Proofreader:** Checks names, callsigns, dates, links, and layout.

## Assembly Process

See `docs/generation-guide.md` for the detailed step-by-step procedure. Summary:

1. Create the new issue folder from the templates.
2. Drop raw incoming material (email, docx, pdf, photos) in
   `submissions/_inbox/` exactly as received.
3. Normalize each raw item into a structured file in `submissions/`, preserving
   the contributor's wording.
4. Save photos and charts in `assets/` using descriptive filenames.
5. Assemble the issue in `newsletter.md` in the standard section order.
6. Put the most time-sensitive and club-wide material first.
7. Use concise captions to identify people by name and callsign.
8. Verify all event dates against the club calendar.
9. Complete the production checklist, then render the PDF with
   `python tools/build_pdf.py issues/YYYY-MM/newsletter.md`.
10. Generate the member announcement email with
    `python tools/build_announcement.py issues/YYYY-MM/newsletter.md` — pulls
    the calendar and archive link straight from `newsletter.md`, so it always
    matches the PDF. See `templates/announcement-email.md`.

## File Naming

- Issue folder: `YYYY-MM`
- Newsletter: `newsletter.md`
- Submission: `section-author-callsign-short-title.md`
- Image: `section-subject-photographer-callsign-01.jpg`
- Published PDF: `Propagator-YYYY-MM.pdf`
- Announcement email: `announcement-YYYY-MM.txt`
