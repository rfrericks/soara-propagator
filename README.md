# SOARA Propagator Newsletter Project

This repository is a reusable workspace for producing the club's monthly
newsletter. Its structure and templates are based on the March, April, and May
2026 Propagator newsletters in `reference/`.

## Typical Issue Order

1. President's Message
2. Membership Meeting preview
3. SOARA Saturday report
4. Recommended links, announcements, or volunteer opportunities
5. One or more member feature articles
6. Treasurer's report
7. Upcoming events calendar
8. Evergreen SOARA information

Sections may be omitted when there is no content that month.

## Folder Structure

```text
.
|-- reference/               Published newsletters used as examples
|-- recommended-links/       Permanent history of links recommended to members
|-- shared/                  Evergreen club information reused every month
|-- templates/               Reusable Markdown templates
|   `-- print/               PDF layout (HTML/CSS) for the rendered issue
|-- tools/
|   `-- build_pdf.py         Renders newsletter.md -> Propagator-YYYY-MM.pdf
|-- issues/
|   |-- _template/           Ready-to-copy monthly issue scaffold
|   `-- YYYY-MM/
|       |-- newsletter.md    Assembled issue
|       |-- checklist.md     Issue-specific production checklist
|       |-- submissions/
|       |   |-- _inbox/      Raw contributor drops (email, docx, pdf, photos)
|       |   `-- ...          Normalized, structured submissions
|       |-- assets/          Photos, charts, and other media
|       `-- Propagator-YYYY-MM.pdf   Rendered output
`-- docs/                    Workflow, editorial, and generation guidance
```

## How a Month Works

Contributors hand over raw material however is easiest — pasted email, Word
docs, PDFs, photos with captions. That lands in `submissions/_inbox/`. The
editor (or Claude) then normalizes it into structured submissions, assembles
`newsletter.md`, fact-checks, and renders the PDF.

`docs/generation-guide.md` is the full step-by-step procedure. In short:

1. Copy `issues/_template/` to `issues/YYYY-MM/`.
2. Copy `templates/newsletter.md` and `templates/production-checklist.md` into it.
3. Drop raw contributor material in `submissions/_inbox/`.
4. Normalize each item into `submissions/` (preserve wording), move photos to
   `assets/`.
5. Assemble and edit `newsletter.md` in the standard section order.
6. Check Recommended Links against the project registry, fact-check callsigns,
   dates, and links; complete `checklist.md`.
7. Render: `python tools/build_pdf.py issues/YYYY-MM/newsletter.md`.
8. Publish, announce, and archive the PDF in `reference/`.

Keep raw source, normalized submissions, and the final assembled newsletter
separate. This makes it easy to preserve contributor wording while editing the
published issue.

## Recommended Links History

The project keeps the cross-issue history in
`recommended-links/registry.csv`; it replaces the former tracking spreadsheet.
Before finalizing an issue, run:

```
python3 tools/recommended_links.py check issues/YYYY-MM/newsletter.md
```

After publication, record the issue's approved links:

```
python3 tools/recommended_links.py register issues/YYYY-MM/newsletter.md
```

See `recommended-links/README.md` for one-off additions, dry runs, and how URL
matching works.

## Rendering the PDF

```
pip install weasyprint markdown pyyaml --break-system-packages
python tools/build_pdf.py issues/YYYY-MM/newsletter.md
```

The layout in `templates/print/` is a clean, readable starting point (navy +
gold masthead, auto-generated "In This Issue" list, contact footer) — not a
pixel-match of past issues. Adjust the CSS freely.
