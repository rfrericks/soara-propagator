# Article Holding Area

A queue for submitted articles and their supporting assets that aren't yet
assigned to a specific issue. Drop content here when you have more than a
month's worth, then pull from here when assembling a future issue.

```text
holding/
|-- articles/    normalized article files, ready to use
`-- assets/      photos or supporting media for held articles
```

## Workflow

**Receiving a submission:**
1. Drop raw text into `holding/articles/` as a `.md` file.
2. Put any photos in `holding/assets/`.
3. Note the article in the file's frontmatter (author, topic, date received).

**Moving to an issue:**
Ask Claude to move an article from the holding area into a specific issue.
For example: *"Move the antenna article by W6XYZ into the 2026-08 issue."*
Claude will copy the file to `issues/2026-08/submissions/` and move its assets
to `issues/2026-08/assets/`, then remove them from holding.

## Article file naming

Use `author-callsign_topic-slug.md` — e.g., `john-smith-w6xyz_yagi-build.md`.
This makes it easy to scan what's waiting and who wrote it.
