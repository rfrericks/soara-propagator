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

import base64

REPO = Path(__file__).resolve().parent.parent
CSS_PATH = REPO / "templates" / "print" / "propagator.css"

# Masthead logo. Drop a file named soara-logo.(png|jpg|jpeg|svg) in
# templates/print/ and it replaces the "K6SOA" circle on the masthead of EVERY
# issue. If no such file exists, the masthead falls back to the "K6SOA" text
# circle so the build never breaks.
LOGO_CANDIDATES = ["soara-logo.png", "soara-logo.jpg", "soara-logo.jpeg", "soara-logo.svg"]
_LOGO_MIME = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg", "svg": "image/svg+xml"}


def masthead_logo_html(club):
    """Return the masthead brand element: the logo image if present, else K6SOA."""
    for name in LOGO_CANDIDATES:
        p = REPO / "templates" / "print" / name
        if p.exists():
            mime = _LOGO_MIME[p.suffix.lstrip(".").lower()]
            b64 = base64.b64encode(p.read_bytes()).decode("ascii")
            alt = html.escape(f"{club} logo")
            return (f'<div class="logo-img">'
                    f'<img src="data:{mime};base64,{b64}" alt="{alt}"></div>')
    return '<div class="logo">K6SOA</div>'


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


def wrap_photo_intros(html_body, max_len=220):
    """Keep a short paragraph that directly introduces a photo (e.g. "Stan,
    KM6VNI, demoed this huge battery box on a cart. Wow, Stan!") attached to
    that photo's <figure>, so a page break can't strand the sentence on one
    page while the photo -- often nearly a full page itself -- floats alone
    onto the next, leaving a tall blank gap behind it.

    Only wraps a paragraph short enough to be an intro line, not ordinary
    article body text (max_len chars of visible text); a long paragraph is
    left to break normally rather than forcing an oversized unbreakable
    block. Only the paragraph immediately before the figure is considered,
    so back-to-back photos with no paragraph between them are untouched."""
    pattern = re.compile(r"(<p>((?:(?!</p>).)*)</p>)\s*(<figure>.*?</figure>)", re.S)

    def repl(m):
        p_html, p_text, fig_html = m.group(1), m.group(2), m.group(3)
        text = re.sub(r"<[^>]+>", "", p_text).strip()
        if len(text) > max_len:
            return m.group(0)
        return f'<div class="photo-intro">{p_html}{fig_html}</div>'

    return pattern.sub(repl, html_body)


def wrap_section_tails(html_body, tail_paragraphs=3):
    """Keep the closing lines of each article section together (up to the last
    few paragraphs), so a page break can't strand a bare sign-off name — or
    even just "73," — alone at the top of the next page, disconnected from the
    rest of the piece. Pulling in a couple of the preceding paragraphs means
    that when the group does need to move, it carries some real article
    content along with the signature rather than just a lone name.

    Only applies when a section's true ending is plain paragraphs (not a
    table or figure) — e.g. the multi-page W6BOT feature ends on an image, so
    it's left alone; there's nothing to usefully regroup there. Also skips
    "SOARA Information," which gets its own compact multi-column single-page
    treatment below — a break-inside: avoid block interacts badly with that
    column layout."""
    chunks = re.split(r"(?=<h2\b)", html_body)
    p_re = re.compile(r"<p>.*?</p>", re.S)
    out = []
    for chunk in chunks:
        if re.match(r'<h2 id="soara-information"', chunk):
            out.append(chunk)
            continue
        matches = list(p_re.finditer(chunk))
        tail = matches[-tail_paragraphs:] if matches else []
        if len(tail) >= 2 and chunk[tail[-1].end():].strip() == "":
            start = tail[0].start()
            out.append(chunk[:start])
            out.append(f'<div class="section-tail">{chunk[start:]}</div>')
        else:
            out.append(chunk)
    return "".join(out)


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
    body_html = wrap_photo_intros(body_html)
    body_html = wrap_section_tails(body_html)

    # Wrap the closing "SOARA Information" section so it renders as a compact
    # two-column single page (matches the printed reference layout). It is the
    # last section, so wrap from its <h2> to the end of the body.
    m = re.search(r'<h2 id="soara-information"[^>]*>', body_html)
    if m:
        body_html = (body_html[:m.start()]
                     + '<section class="soarainfo">'
                     + body_html[m.start():]
                     + '</section>')

    toc_html = ""
    if toc:
        lis = "\n".join(
            f'<li>{html.escape(t)}</li>' for t, _ in toc)
        toc_html = f'<div class="toc"><h2>In This Issue</h2><ul>{lis}</ul></div>'

    issue_label = issue or (pub_date[:7] if pub_date else "")
    editor_line = f" &nbsp;|&nbsp; Editor: {html.escape(editor)}" if editor else ""
    logo_html = masthead_logo_html(club)

    document = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>The Propagator — {html.escape(issue_label)}</title></head>
<body>
  <div class="masthead">
    {logo_html}
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
