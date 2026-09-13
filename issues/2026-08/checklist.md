# August 2026 Production Checklist

**Issue closed 2026-09-13.** All publication steps confirmed by Ray; remaining items below are should-resolve/optional carryover, not blockers.

## Content

- [x] President's Message received — Dale Tyler, W6EDT (from `PresidentsMessage_August_2026.docx`)
- [x] Membership meeting preview received and verified — no WE4BY submission this month; generic notice written per Ray's instruction 2026-08-13 (6:30 PM program, 6:00 PM exams, as normal; topic to be announced)
- [x] SOARA Saturday report received — Ed Barnes, WA6ED, for the July 18 event, with one photo
- [ ] Announcements and volunteer opportunities included — none separate this month; the picnic is covered in the President's Message and the calendar
- [x] Feature article(s) received — W6BOT coaxial sleeve dipole (moved from `holding/`) and KI6DDB "Full Circle Story" (submitted 2026-06-01)
- [x] Recommended links — dropped this month per Ray's instruction 2026-08-13, no links on hand; section omitted (Club News was already omitted for the same reason)
- [x] Treasurer's report received — figures pulled from Ron's "Financial Statement for Propagator" block; **approved by Ron 2026-08-13** (`approved_for_publication: true`)
- [x] This-month and next-month calendars verified — August/September dates derived from the standing schedule and cross-checked against the July issue
- [x] Evergreen club information reviewed — matches `templates/newsletter.md` verbatim

## Editing and Fact Check

- [ ] Names and callsigns verified
- [ ] Dates, times, locations, and contacts verified
- [ ] Technical claims and regulatory guidance checked
- [ ] Links tested
- [ ] Contributor permissions and credits confirmed
- [x] Image captions and credits included — W6BOT figures credited; no photo credit needed on the Elmer Saturday photo per Ray 2026-08-13
- [ ] Spelling, grammar, and formatting reviewed

## Publication

- [x] PDF rendered: `python tools/build_pdf.py issues/2026-08/newsletter.md` — 19 pages, rendered 2026-08-13 with all content edits and blocking items resolved; sent to Ray for review
- [x] "In This Issue" list, masthead, captions, tables, and page breaks look right — Ray caught three rounds of layout issues 2026-08-13, all fixed and re-sent: (1) Ed's sign-off orphaned alone on p.4 and Treasurer's table split p.17/18 — fixed via keep-together CSS rules; (2) Ed's whole sign-off (still disconnected from the rest of his article) and the same problem on Tom's sign-off — fixed by reordering `newsletter.md` (Membership Meeting now runs after SOARA Saturday Report, freeing enough room for Ed's full article+sign-off on one page) and generalizing the keep-together logic in `tools/build_pdf.py` (`wrap_section_tails`) to pull the last few paragraphs of a section together with the sign-off, not just the sign-off alone. PDF is now 20 pages (was 19). Known minor side effect: page 9 ("Final assembly verification" in the W6BOT feature) is mostly blank — a full-page image couldn't fit after it and moved to page 10 alone; not fixed, flagged for Ray, low risk to attempt fixing further given how fragile the heading/figure grouping got in testing.
- [x] Final proof reviewed by a second person — confirmed by Ray 2026-09-13
- [x] Final PDF filename is `Propagator-2026-08.pdf` — confirmed 2026-09-13
- [x] PDF links and images checked — confirmed by Ray 2026-09-13
- [x] Newsletter published to website — confirmed by Ray 2026-09-13
- [x] Announcement email generated 2026-08-13 via new `tools/build_announcement.py` (`issues/2026-08/announcement-2026-08.txt`) — sent to Ray to validate before this becomes the standard workflow step; flag the "SOARA Annual Picnic" (newsletter) vs. "SOARA Summer Picnic" (Ray's usual wording) naming mismatch for his call
- [x] Newsletter announcement sent — confirmed by Ray 2026-09-13
- [x] Published PDF archived in `reference/` — copied 2026-09-13
- [x] Next issue folder created — `issues/2026-09/` scaffolded 2026-08-24

## Open Items for This Issue

Blocking:

- [x] **W6EDT** — missing word filled in by Dale directly ("some very nifty SDRs"); synced into `newsletter.md` 2026-08-13
- [x] **W6EDT** — "the test messages being sent" confirmed correct as written; Ray signed off 2026-08-13
- [x] **K0PGE** — narrative paragraph dropped; section runs as table + Ron's standard note only, exactly as marked in his block. Ron reviewed and approved directly with Ray 2026-08-13 (`approved_for_publication: true`).
- [x] **K0PGE** — 7-cent difference not corrected; Ron's approval of the section as-is (2026-08-13) is treated as his resolution. $26,887.40 stays as printed.
- [x] **W6BOT** — reprint permission confirmed 2026-08-13: Rich sent the article to Ray directly for inclusion.
- [x] **W6BOT** — callsign/name confirmed 2026-08-13: Rich Gordon, W6BOT, is a former SOARA member who moved out of town — explains the roster mismatch.
- [x] **KI6DDB** — Heiko's callsign (AD6OI) and "MESAC" confirmed correct as printed; Ray signed off 2026-08-13, no changes needed
- [x] **WE4BY** — no submission received; resolved by running a generic "topic to be announced" notice per Ray's decision 2026-08-13, not by an answer from Greg

Should resolve before publishing:

- [x] No photo credit needed on WA6ED's Elmer Saturday photo, per Ray 2026-08-13 (member names in the photo still not addressed — separate question, not raised)
- [ ] Decide how to present W6BOT's gain-comparison table, which names Amazon and AliExpress critically
- [x] Reconcile the meeting start time — confirmed by Ray 2026-09-13: 6:30 PM is correct. Fixed at the source in `shared/club-information.md`, and propagated to `templates/newsletter.md` and `issues/2026-09/newsletter.md`. This August issue itself printed 7:00 PM and is not being reprinted/corrected retroactively.
- [x] Masthead club name confirmed as "South Orange Amateur Radio Association" (no "County") per Ray 2026-08-13 — SOARA is a club located in South Orange County, but that's not part of the club's name. Current `newsletter.md` frontmatter already reads this way; no change needed. The open question came from `docs/generation-guide.md`, which notes past printed mastheads read "South Orange **County** Amateur Radio Association" and asks to confirm with the board — now confirmed.
- [ ] Consider adding the frequency to "Temple Hill 2M repeater" in the President's Message so visitors can find it
- [ ] Six full-page NanoVNA plots add roughly six pages; shrink via `templates/print/propagator.css` if 19 pages is too long
- [x] Removed the superseded originals from `holding/` — 2026-09-13, moved (not deleted; device bridge can't unlink) to `holding/_to_delete/`. Verified byte-identical to the published copies in `issues/2026-08/` before moving. Ray needs to delete `holding/_to_delete/` himself.

Optional:

- [ ] **WA6ED** — donut fund shows "$2 left over" against last month's "$10 for next month" with no intervening figures
- [x] **KI6DDB** — comfortable naming Toby Taylor in print; Ray signed off 2026-08-13
