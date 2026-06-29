#!/usr/bin/env python3
"""Render an assembled Propagator issue (newsletter.md) to a styled PDF.

Usage:
    python tools/build_pdf.py issues/2026-06/newsletter.md
    python tools/build_pdf.py issues/2026-06/newsletter.md -o out/Propagator-2026-06.pdf

What it does:
  * Reads YAML frontmatter (issue, publication_date, editor, club).
  * Converts the Markdown body to HTML.
  * Auto-builds the "In This Issue" table of contents from the H2 headings.
  * Wraps an italic-emphasis paragraph that immediately follows an image into a
    <figure>/<figcaption> so photo captions render under the photo.
  * Applies templates/print/propagator.css and writes Propagator-YYYY-MM.pdf
    next to the source file (or to -o).

Dependencies: weasyprint, markdown, pyyaml
    pip install weasyprint markdown pyyaml --break-system-packages
"""
import argparse
import datetime as dt
import html
import re
import sys
from pathlib import Path

try:
    import markdown as md_lib
    import yaml
    from weasyprint import HTML
except ImportError as e:  # pragma: no cover
    sys.exit(f"Missing dependency: {e}. Run: pip install weasyprint markdown pyyaml")

REPO = Path(__file__).resolve().parent.parent
CSS_PATH = REPO / "templates" / "print" / "propagator.css"

# Footer contact line — keep in sync with shared/club-information.md
CONTACT = (
    "Questions about SOARA? &nbsp; membership@soara.org &nbsp;|&nbsp; "
    "P.O. Box 2545, Mission Viejo, CA 92690 &nbsp;|&nbsp; "
    "soara.org &nbsp;|&nbsp; Facebook/X: K6SOA"
)


def split_frontmatter(text):
    if text.startswith("---"):
        parts = text.split("---", 2)
        if len(parts) >= 3:
            meta = yaml.safe_load(parts[1]) or {}
            return meta, parts[2].lstrip("\n")
    return {}, text


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def build_toc(body_md):
    """Return list of (text, slug) for level-2 headings, skipping the title."""
    items = []
    for line in body_md.splitlines():
        m = re.match(r"^##\s+(?!#)(.+?)\s*$", line)
        if m:
            text = m.group(1).strip()
            items.append((text, slugify(text)))
    return items


def add_heading_ids(html_body):
    """Give each <h2> an id matching slugify(text) so the TOC can link."""
    def repl(m):
        inner = re.sub(r"<[^>]+>", "", m.group(2))
        return f'<h2 id="{slugify(inner)}"{m.group(1)}>{m.group(2)}</h2>'
    return re.sub(r"<h2([^>]*)>(.*?)</h2>", repl, html_body, flags=re.S)


def wrap_captions(html_body):
    """Turn `<p><img ...></p>` followed by `<p><em>caption</em></p>` into a figure."""
    pattern = re.compile(
        r"<p>\s*(<img[^>]*>)\s*</p>\s*<p>\s*<em>(.*?)</em>\s*</p>", re.S)
    html_body = pattern.sub(
        r'<figure>\1<figcaption>\2</figcaption></figure>', html_body)
    # lone images still center nicely
    html_body = re.sub(r"<p>\s*(<img[^>]*>)\s*</p>",
                       r'<figure>\1</figure>', html_body)
    return html_body


def main():
    ap = argparse.ArgumentParser(description="Render a Propagator issue to PDF.")
    ap.add_argument("source", help="path to assembled newsletter.md")
    ap.add_argument("-o", "--output", help="output PDF path")
    args = ap.parse_args()

    src = Path(args.source).resolve()
    if not src.exists():
        sys.exit(f"Not found: {src}")

    meta, body_md = split_frontmatter(src.read_text(encoding="utf-8"))

    issue = str(meta.get("issue", "")).strip()
    pub_date = str(meta.get("publication_date", "")).strip()
    editor = str(meta.get("editor", "")).strip()
    club = str(meta.get("club", "South Orange Amateur Radio Association")).strip()

    # default output name from frontmatter date, else folder name
    if args.output:
        out = Path(args.output).resolve()
    else:
        ym = ""
        if re.match(r"\d{4}-\d{2}", pub_date):
            ym = pub_date[:7]
        elif re.match(r"\d{4}-\d{2}", src.parent.name):
            ym = src.parent.name[:7]
        out = src.parent / (f"Propagator-{ym}.pdf" if ym else "Propagator.pdf")

    toc = build_toc(body_md)

    # strip the top-level "# The Propagator" + bold subtitle from body (masthead covers it)
    body_md = re.sub(r"^#\s+The Propagator\s*\n", "", body_md, count=1)
    body_md = re.sub(r"^\*\*South Orange.*?\*\*\s*\n", "", body_md, count=1, flags=re.M)

    body_html = md_lib.markdown(
        body_md, extensions=["tables", "fenced_code", "sane_lists", "attr_list"])
    body_html = add_heading_ids(body_html)
    body_html = wrap_captions(body_html)

    toc_html = ""
    if toc:
        lis = "\n".join(
            f'<li>{html.escape(t)}</li>' for t, _ in toc)
        toc_html = f'<div class="toc"><h2>In This Issue</h2><ul>{lis}</ul></div>'

    issue_label = issue or (pub_date[:7] if pub_date else "")
    editor_line = f" &nbsp;|&nbsp; Editor: {html.escape(editor)}" if editor else ""

    document = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>The Propagator — {html.escape(issue_label)}</title></head>
<body>
  <div class="masthead">
    <div class="logo">K6SOA</div>
    <div class="title">
      <div class="wordmark">The Propagator</div>
      <div class="tagline">The Monthly Newsletter of the {html.escape(club)}</div>
    </div>
  </div>
  <div class="issueband"><span class="issue">{html.escape(issue_label)}</span><span>{html.escape(club)}{editor_line}</span></div>
  {toc_html}
  <main>{body_html}</main>
  <div class="contact-footer">{CONTACT}</div>
</body></html>"""

    HTML(string=document, base_url=str(src.parent)).write_pdf(
        str(out), stylesheets=[str(CSS_PATH)])
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()

# end of build_pdf.py
