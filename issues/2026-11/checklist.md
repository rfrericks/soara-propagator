# November 2026 Production Checklist

First-pass draft for Ray Frericks, K6NOV, to review. Not for publication.
Publish target is Monday, November 9, 2026. No announcement was generated or sent,
and nothing was posted to the website or to groups.io.

## Content

- [x] President's Message received (Dale W6EDT, Nov 7 .docx). Not approved. See conflicts below.
- [ ] Membership meeting preview received and verified — Ron K0PGE's Nov 16 auction announcement (from-ron-k0pge-auction-announcement.md) IS this month's meeting announcement; it is printed as written. Not marked verified: Dale's setup time disagrees, and the 6:00 PM exam line overlaps auction setup.
- [x] SOARA Saturday report received (Ed WA6ED, Oct 17 PDF, photos and captions kept)
- [x] Announcements and volunteer opportunities included (Holiday Party blurb; price updated to $40)
- [x] Feature article(s) received (Ed WA6ED, CYD Extended Edition, Nov 3, full 10-page article)
- [ ] Recommended links received and tested; `recommended_links.py check` confirms none were previously recommended — the Facebook reel URL is filed and is not in the registry. Ray supplied no title or description, so none was written. The URL answers, but the reel itself is behind a Facebook wall and was not described.
- [ ] Treasurer's report received and approved — the marked-block markdown is typeset and the figures tie. `approved_for_publication` stays false until Ron or Ray accepts this typeset. No ledger spreadsheet is in the repo.
- [ ] This-month and next-month calendars verified — November 21 and December 19 are sourced. December board meeting and December exams are unresolved and were left off. Auction time and Holiday Party venue conflicts are flagged, not resolved.
- [x] Evergreen club information reviewed against `shared/club-information.md` (differences from the October printed page are in the draft notes; not silently "corrected" beyond following the shared file)

## Editing and Fact Check

- [x] Names and callsigns verified against callook.info where a person is named (see draft notes). Jimmy KK6TTL left as Ed wrote it.
- [ ] Dates, times, locations, and contacts verified — open conflicts below, so this stays unchecked.
- [ ] Technical claims and regulatory guidance checked — Ed's CYD article is printed as written. Pinouts, prices, and the HamClock timeline were not re-tested. His QST mention is a citation, not a reprint.
- [x] Links tested 2026-11-08 (see draft notes for the 403s)
- [ ] Contributor permissions and credits confirmed — photo credit "Photo by Ed Barnes, WA6ED" was added where his PDF said "Photo: author" or had no credit line. Ray should confirm.
- [x] Image captions and credits included (Ed's caption sentences kept)
- [x] Spelling, grammar, and formatting reviewed. Dale's mechanical fixes are listed in his submission. Wording that might be wrong was not changed.

## Publication

- [ ] PDF rendered: `python tools/build_pdf.py issues/YYYY-MM/newsletter.md`
- [ ] "In This Issue" list, masthead, captions, tables, and page breaks look right
- [ ] Final proof reviewed by a second person
- [ ] Final PDF filename is `Propagator-YYYY-MM.pdf`
- [ ] PDF links and images checked
- [ ] Newsletter published to website
- [ ] Announcement email generated: `python tools/build_announcement.py issues/YYYY-MM/newsletter.md` (see `templates/announcement-email.md`)
- [ ] Newsletter announcement sent
- [ ] Published PDF archived in `reference/`
- [ ] Next issue folder created

The review PDF was rendered and compressed for this pass. Those publication boxes stay unchecked on purpose. This file is not the published issue.

Review file: `issues/2026-11/Propagator-2026-11.pdf`, 19 pages, 983,722 bytes. `tools/compress_pdf.py` stopped at 1,021,753 bytes. A second pass recompressed the eight photographs only (JPEG quality 66, same pixel size). No text, table, or photo was removed. Layout fixes in `templates/print/propagator.css`: table rows stay on one page, and the CYD feature starts on a fresh page so its title is not left behind the opening photo.

## Draft notes (2026-11-08) — first pass, for Ray

### In the issue

- Upcoming events (November and December)
- President's Message, Dale Tyler, W6EDT, from `PresidentsMessage_1126.docx`
- Membership meeting: Ron Mosher, K0PGE, auction announcement, full text
- SOARA Saturday report, Ed Barnes, WA6ED, October 17, five photos with his captions
- Club news: December 4 Holiday Party, ticket price now $40 per person
- Recommended link: Ray's Facebook reel URL only
- Feature: Ed Barnes, WA6ED, "The Cheap Yellow Display" Extended Edition, full article, three photos
- Treasurer's Report from the Propagator block only, through the October 31 ending-cash line
- SOARA Information from `shared/club-information.md`

### Not in the issue

- Randy WA4SKI's BEACON piece. It was not in `submissions/_inbox/` or elsewhere in the repo at this assembly. Not invented and not given a placeholder.
- The earlier CYD article (`CYD_Shack_Gadget_Article.pdf`). The inbox has only the Nov 3 Extended Edition, which replaces it.
- Ron's full ledger workbook. Only the already-extracted Propagator-block markdown was used. His email's "$236 was the P.O. Box" split is outside that block and is not printed.
- No announcement email, no groups.io post, no website upload.

### Conflicts left for you (nothing was rewritten to pick a winner)

1. Auction clock. Dale: setup 5:45 PM, viewing 6:00 PM, start 6:30 PM, selling stops by 8:15 PM. Ron, this calendar, and soara.org/club-calendar/live-auction/ (page updated Oct 4, 2026): preview/setup 6:00 PM, start 6:30 PM. The website also says the final sale is not later than 8:15 PM, which matches Dale's stop time. Dale's paragraph is unchanged. The calendar follows Ron and the website.
2. Holiday Party place. Dale: "Mission Viejo Community Center." soara.org/club-calendar/holiday-party/ (page updated Nov 7, 2026, 4:59 PM PT), the club-news blurb, and the calendar: Palo Verde Room, Norman P. Murray Center. Dale's sentence is unchanged.
3. Holiday Party price is no longer open. Dale and the Nov 7 webpage both say $40 per person, advance payment, no tickets at the door. The old "price still to be announced" line in the blurb and calendar was updated. Dale's menu was not copied into the blurb. The webpage still describes the meal only as a buffet. His menu names, including "Millionaire Skirt Steak" and "Margarite Pasta," are printed as he wrote them.
4. November 16 license exams are still on the calendar at 6:00 PM, same slot as auction setup, because the October issue and the previous November calendar both listed them. Ron does not mention exams. Confirm or pull the line.
5. December board meeting: not listed. The board page (updated Apr 21, 2026) says the week after the monthly membership meeting, 7:00–9:00 PM, Murray Center, and gives no December date. There is no regular December membership meeting. No source found that schedules or cancels a December 2026 board meeting.
6. December license exams: not listed. The exam page (updated Jul 20, 2026) says typically before each regular meeting and does not list or cancel a December session.
7. November 21 SOARA Saturday is Murray Center, 9:00 AM–noon, theme Kit building, from Ed's report (RSVP by Wednesday, November 18 if you will build). The Elmer Saturday page on soara.org lists the same date and place as "Kit building & how to solder." December 19 is the next one, Murray Center, 9:00 AM–noon. Ed gives no December theme, so none was added. That page's December notes (antenna field strength, another kit) read as a planning list updated "2025-1-3," not as his announcement.

### Treasurer tie-out

Recomputed from the Propagator-block markdown. Income, expenses, net, and ending cash all close for both years, and every Increase/(Decrease) cell matches the two columns. Beginning cash October 1, 2026, $25,243.07, matches the October issue's September 30 ending cash.

Printed as sent, not "fixed":

- Block title says through October 30; the ending-cash row says October 31.
- Prior-year beginning cash is $28,179.00. The October issue showed October 1, 2025 beginning cash as $28,179.03. Difference $0.03.
- Whole-dollar cells were given cents and thousands separators to match the October table. Digits were not changed.
- `approved_for_publication: false`.

### Other flags

- Dale, left unchanged on purpose: "If you plan to see or plan to bid"; "as the transceivers, amplifiers, and are tested" (a word looks missing). Mechanical fixes only, listed in `submissions/president-message-w6edt.md`.
- Jimmy KK6TTL: FCC licensee name is Zhiming Huang. Ed's "Jimmy" was not replaced.
- W6EDT checks as Eugene Tyler. Printed name stays Dale, as in prior issues and as he signed this message.
- CYD link oddities kept from his PDF: Matt Housley's cyd-dashboard and JamesDavid's Overhead both use the same Trendshift URL (`repositories/73440`); "ESPHome examples" points at the witnessmenow GitHub repo; the ARNewsline URL slug says "wboew" while the text says WB0OEW (that callsign does check as Elwood Downey); both Printables URLs are stored already cut off. Home Assistant and Printables returned HTTP 403 to the checker. Not rewritten.
- Facebook reel `https://www.facebook.com/reel/2732795223848329` returned a generic Facebook page from here. No description was invented. `recommended_links.py check` reports it as new. Not registered.
- SOARA Information follows `shared/club-information.md`, not a fresh copy of the October back page. Differences Ray should confirm before this is final: Treasurer phone 949-636-9816 (October printed 949-363-0047); exam contact testing@soara.org (October printed k6uvr@soara.org; the exam webpage still says to email documents to K6UVR@SOARA.ORG); At Large director Dan Upchurch, N6RPR (on the soara.org board page); Public Information Coordinator Knute Josifek, K6HIV (in the shared file, not on the Apr 21, 2026 board page). The board page also has blank IT and Ambassador lines; those were not added.
- soara.org club-meetings page says meetings start at 7:00 PM. The shared file, recent calendars, and this issue say 6:30 PM. The 6:30 PM line was left as the newsletter has carried it.
