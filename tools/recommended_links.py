#!/usr/bin/env python3
"""Check and maintain the project-local Recommended Links registry.

Usage:
    python tools/recommended_links.py check issues/YYYY-MM/newsletter.md
    python tools/recommended_links.py register issues/YYYY-MM/newsletter.md
    python tools/recommended_links.py add YYYY-MM "Title" https://example.com
"""
import argparse
import csv
import re
import sys
from pathlib import Path
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

REPO_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_REGISTRY = REPO_ROOT / "recommended-links" / "registry.csv"
TRACKING_PARAMETERS = {"fbclid", "feature", "gclid", "mc_cid", "mc_eid", "ref", "source"}


def normalize_url(value):
    """Return a stable comparison form without changing the stored source URL."""
    raw = value.strip()
    if not raw:
        return ""
    if "://" not in raw:
        raw = "https://" + raw
    parts = urlsplit(raw)
    host = parts.netloc.lower()
    if host.startswith("www.") or host.startswith("m."):
        host = host.split(".", 1)[1]
    path = parts.path.rstrip("/") or "/"
    query = [(key, val) for key, val in parse_qsl(parts.query, keep_blank_values=True)
             if not key.lower().startswith("utm_") and key.lower() not in TRACKING_PARAMETERS]

    # These forms point at the same YouTube video and should not be treated as
    # distinct recommendations. Other query parameters remain meaningful.
    if host == "youtu.be":
        host, path, query = "youtube.com", "/watch", [("v", path.lstrip("/"))]
    elif host == "youtube.com" and path.startswith("/shorts/"):
        path, query = "/watch", [("v", path.split("/", 3)[2])]

    return urlunsplit(("https", host, path, urlencode(sorted(query)), ""))


def registry_rows(path):
    if not path.exists():
        sys.exit(f"Registry not found: {path}")
    with path.open(newline="", encoding="utf-8") as handle:
        return list(csv.DictReader(handle))


def recommended_section(markdown):
    match = re.search(r"^##\s+Recommended Links\s*$", markdown, re.M | re.I)
    if not match:
        return ""
    rest = markdown[match.end():]
    next_heading = re.search(r"^##\s+\S", rest, re.M)
    return rest[:next_heading.start()] if next_heading else rest


def links_from_issue(path):
    text = path.read_text(encoding="utf-8")
    section = recommended_section(text)
    if not section:
        return []
    # The title is optional formatting around a standard Markdown link.
    links = re.findall(r"\[([^\]]+)\]\((https?://[^\s)]+)\)", section)
    return [{"title": title.strip(), "url": url.strip()} for title, url in links]


def issue_id(path):
    if re.fullmatch(r"\d{4}-\d{2}", path.parent.name):
        return path.parent.name
    sys.exit("Issue file must live in a folder named YYYY-MM, or use `add`.")


def duplicate_matches(links, rows):
    known = {}
    for row in rows:
        known.setdefault(normalize_url(row["url"]), []).append(row)
    return [(link, known[normalize_url(link["url"])]) for link in links
            if normalize_url(link["url"]) in known]


def command_check(args):
    links = links_from_issue(args.issue_file)
    if not links:
        print("No Recommended Links entries found.")
        return 0
    matches = duplicate_matches(links, registry_rows(args.registry))
    if not matches:
        noun = "entry is" if len(links) == 1 else "entries are"
        print(f"OK: {len(links)} Recommended Links {noun} new.")
        return 0
    print("Duplicate Recommended Links found:")
    for link, previous in matches:
        for row in previous:
            print(f"- {link['title']} ({link['url']})\n  Previously recommended in "
                  f"{row['issue']}: {row['title']} ({row['url']})")
    return 1


def write_rows(path, rows):
    fields = ["issue", "title", "url", "category", "shared_by"]
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def command_register(args):
    links = links_from_issue(args.issue_file)
    issue = issue_id(args.issue_file)
    rows = registry_rows(args.registry)
    if not links:
        print("No Recommended Links entries found; registry unchanged.")
        return 0
    matches = duplicate_matches(links, rows)
    if matches:
        print("Registry unchanged because duplicate links were found:")
        for link, previous in matches:
            print(f"- {link['url']} (first recorded in {previous[0]['issue']})")
        return 1
    additions = [{"issue": issue, "title": link["title"], "url": link["url"],
                  "category": args.category, "shared_by": args.shared_by} for link in links]
    if args.dry_run:
        print(f"Would add {len(additions)} link(s) for {issue}.")
        return 0
    write_rows(args.registry, rows + additions)
    print(f"Added {len(additions)} link(s) for {issue} to {args.registry.relative_to(REPO_ROOT)}.")
    return 0


def command_add(args):
    rows = registry_rows(args.registry)
    link = {"title": args.title, "url": args.url}
    matches = duplicate_matches([link], rows)
    if matches:
        print(f"Registry unchanged: URL first recorded in {matches[0][1][0]['issue']}.")
        return 1
    row = {"issue": args.issue, "title": args.title, "url": args.url,
           "category": args.category, "shared_by": args.shared_by}
    if args.dry_run:
        print(f"Would add {args.url} for {args.issue}.")
        return 0
    write_rows(args.registry, rows + [row])
    print(f"Added {args.url} for {args.issue}.")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--registry", type=Path, default=DEFAULT_REGISTRY,
                        help="CSV registry path (default: project registry)")
    parser.add_argument("--dry-run", action="store_true", help="preview a write operation")
    subparsers = parser.add_subparsers(dest="command", required=True)

    check = subparsers.add_parser("check", help="check an issue for prior links")
    check.add_argument("issue_file", type=Path)
    check.set_defaults(func=command_check)

    register = subparsers.add_parser("register", help="record links from an approved issue")
    register.add_argument("issue_file", type=Path)
    register.add_argument("--category", default="", help="category applied to all added links")
    register.add_argument("--shared-by", default="", help="credit applied to all added links")
    register.set_defaults(func=command_register)

    add = subparsers.add_parser("add", help="add one historical or one-off link")
    add.add_argument("issue", help="issue in YYYY-MM form")
    add.add_argument("title")
    add.add_argument("url")
    add.add_argument("--category", default="")
    add.add_argument("--shared-by", default="")
    add.set_defaults(func=command_add)

    args = parser.parse_args()
    args.registry = args.registry.resolve()
    sys.exit(args.func(args))


if __name__ == "__main__":
    main()
