# Issue Workspace

Rename this folder from `_template` to the issue's `YYYY-MM`.

Then:

1. Copy `../../templates/newsletter.md` here as `newsletter.md`.
2. Copy `../../templates/production-checklist.md` here as `checklist.md`.
3. Drop raw contributor material (email, docx, pdf, photos) in
   `submissions/_inbox/` exactly as received.
4. Normalize each raw item into a structured file in `submissions/`, preserving
   the contributor's wording.
5. Place publication-ready photos, charts, and graphics in `assets/`.
6. Assemble and edit the issue in `newsletter.md`, then render with
   `python ../../tools/build_pdf.py newsletter.md`.

See `docs/generation-guide.md` for the full procedure.
