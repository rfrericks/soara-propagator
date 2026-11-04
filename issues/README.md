# Monthly Issues

Create one folder per issue using `YYYY-MM`.

```text
issues/
|-- _template/
`-- YYYY-MM/
    |-- newsletter.md
    |-- checklist.md
    |-- submissions/
    |   |-- _inbox/      raw contributor drops, untouched
    |   `-- ...          normalized, structured submissions
    |-- assets/
    `-- Propagator-YYYY-MM.pdf
```

Raw contributor material lands in `submissions/_inbox/`; it is normalized into
structured files in `submissions/`. The `newsletter.md` file is the edited,
assembled source, and `tools/build_pdf.py` renders it to the published PDF.

When more articles arrive than fit in one month, park extras in `holding/`
(repo root) and pull them into a future issue when ready.
