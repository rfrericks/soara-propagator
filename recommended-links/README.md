# Recommended Links Registry

`registry.csv` is the permanent, project-local history of links recommended in
The Propagator. It was migrated from the editor's tracking spreadsheet on
August 24, 2026. Keep it in version control so the history remains available
across monthly issues.

Before finalizing a draft, check only its **Recommended Links** section:

```sh
python3 tools/recommended_links.py check issues/YYYY-MM/newsletter.md
```

The command exits with status 1 and identifies each prior recommendation when a
duplicate is found. It ignores URL fragments, common tracking parameters, and
minor YouTube URL variations such as `m.youtube.com` versus `www.youtube.com`.

After the issue is approved for publication, add its links to the registry:

```sh
python3 tools/recommended_links.py register issues/YYYY-MM/newsletter.md
```

Use `--dry-run` to preview either operation. The registration command refuses
to add a link already present in the registry, and reports no-op if the issue
has no Recommended Links entries. For a one-off entry, use:

```sh
python3 tools/recommended_links.py add 2026-09 "Useful resource" https://example.com \
  --category "Antennas" --shared-by "NAME, CALLSIGN"
```

Edit the CSV directly only when correcting imported historical metadata. Do not
remove an entry merely because the page later becomes unavailable: it was still
recommended and should continue to prevent accidental repetition.
