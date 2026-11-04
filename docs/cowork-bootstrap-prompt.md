# How to Bootstrap a Club Newsletter Project in Claude Cowork

Copy the prompt below and paste it into a new Claude Cowork conversation
after selecting your newsletter folder. Customize the bracketed sections
for your club before sending.

---

## The Prompt

I run the monthly newsletter for **[CLUB FULL NAME]** (callsign **[CALLSIGN]**,
located in **[CITY, STATE]**). I'd like you to set up a newsletter production
workspace in this folder so I can use Claude to help assemble each issue.

Please create the following folder and file structure:

**Folders:**
- `docs/` — editorial guidelines and workflow documentation
- `templates/` — reusable section templates and a print CSS file
- `templates/print/` — CSS for PDF rendering
- `issues/` — one subfolder per published issue, plus an `_template/` starter
- `issues/_template/submissions/_inbox/` — drop zone for raw incoming material
- `issues/_template/assets/` — photos and charts
- `reference/` — archive of past published PDFs
- `shared/` — evergreen club information reused every issue
- `holding/articles/` and `holding/assets/` — approved material waiting for a future issue

**Files to create:**

`docs/editorial-style.md` — voice and mechanics rules:
- Friendly, practical club voice; welcome newer members; end calls to action with a specific next step
- Names: "Full Name, CALLSIGN" on first mention; first name or callsign after
- Dates: unambiguous format like "Monday, June 15, 2026"; include start time and location for events
- Links: descriptive text instead of bare URLs; test every link before publication
- Photos: caption + photographer credit; identify visible members by name and callsign
- Editing: preserve the author's character; spell out uncommon abbreviations on first use

`docs/workflow.md` — monthly production schedule:
- 3 weeks out: solicit submissions from officers and members
- 2 weeks out: confirm meeting topic, calendar, and feature articles
- 1 week out: assemble first draft; identify gaps
- 3–5 days out: edit, fact-check, place photos, proofread
- Publication day: export PDF, publish, email members, archive

`docs/generation-guide.md` — step-by-step assembly instructions for each issue

`templates/newsletter.md` — master newsletter template with these sections in order:
President's Message, Membership Meeting preview, Club Activity Report,
Club News and Opportunities, Recommended Links, Member Feature, Treasurer's Report,
Upcoming Events, evergreen club info footer. Include YAML front matter for
title, club, issue, publication_date, editor, and status.

`templates/production-checklist.md` — pre-publication checklist covering:
content received, editing and fact-check, and publication steps

`templates/president-message.md`, `templates/membership-meeting.md`,
`templates/club-activity-report.md`, `templates/feature-article.md`,
`templates/financial-report.md`, `templates/calendar.md`,
`templates/recommended-links.md`, `templates/submission.md` —
one template per recurring newsletter section, with YAML front matter and
fill-in-the-blank structure

`templates/print/newsletter.css` — clean CSS for Markdown-to-PDF rendering:
serif body font, print-safe colors, page breaks before H2, two-column photo
support, masthead styling

`shared/club-information.md` — evergreen boilerplate: meeting time and location,
repeating nets with frequencies and times, website and social links, officers list,
how to submit to the newsletter, how to join

`tools/build_pdf.py` — Python script that converts `issues/YYYY-MM/newsletter.md`
to a PDF using WeasyPrint and the print CSS, outputting `Propagator-YYYY-MM.pdf`

`README.md` — brief project overview and quick-start instructions

After creating all files, please also set up a **Cowork Project Instruction** for
this folder with the following guidance (I will paste it into Project Settings >
Instructions myself — please just draft the text):

> This project produces [CLUB NAME]'s monthly [NEWSLETTER NAME] newsletter.
> When starting a new issue: copy issues/_template/ to issues/YYYY-MM/, copy
> templates/newsletter.md and templates/production-checklist.md into it, collect
> drafts in submissions/ and media in assets/, then assemble newsletter.md.
> Keep contributor submissions separate from the assembled newsletter — preserve
> each author's wording while editing for clarity and mechanics.
> Follow docs/editorial-style.md: [VOICE SUMMARY]. Always verify callsigns,
> event dates, and links before publication. Complete the production checklist
> before publishing.
> Standard section order: [YOUR SECTION ORDER]. Omit sections with no content.

Once the structure is in place, create the first real issue folder `issues/[YYYY-MM]/`
from the template and open `issues/[YYYY-MM]/newsletter.md` so I can start working.

---

## Tips for adapting this to your club

- Replace all `[BRACKETED]` items before sending.
- The section order in `templates/newsletter.md` should match your club's
  existing newsletter conventions so the AI learns your layout.
- Paste 2–3 past PDF issues into `reference/` before your first session —
  Claude can read them to match your existing style.
- The project instruction text (the block starting "This project produces…")
  goes in **Settings → Projects → [your project] → Instructions** in Cowork.
  That makes Claude apply your style rules automatically in every session.
- To start each new issue, just tell Claude:
  *"Start the [Month Year] issue."*
  It will copy the template, open the checklist, and ask you what content
  you have ready.
