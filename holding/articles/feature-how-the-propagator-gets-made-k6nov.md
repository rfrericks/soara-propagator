---
section: "Member Feature"
title: "How the Propagator Gets Made (With a Little Help from an AI)"
author: "Ray Frericks, K6NOV"
issue: "TBD"
status: draft
---

# How the Propagator Gets Made (With a Little Help from an AI)

**By Ray Frericks, K6NOV**

I have been putting the Propagator together for a few years now, and for most of that time the process lived in my head and in a pile of email. This past July I changed that. My day job has me building AI-enabled tools for clients, and it finally occurred to me that I should set the newsletter up the way I would set up any other recurring project — with a written process, a checklist, and something to do the tedious parts. The July issue was the first one built the new way, and every issue since has followed the same routine. This is a short tour of how it works. If you have ever wondered what happens to your article between hitting "send" and seeing it in the PDF, read on.

## The short version

The newsletter lives in a folder on my laptop. That folder is what the software world calls a "project": a set of templates, written rules, a few small scripts, and one subfolder per issue. When it is time to build an issue, I open that folder in a chat window with an AI assistant (I have been using Claude, and I have tried the same setup with OpenAI's Codex) and we work through the month together. I do the deciding; the assistant does the sorting, formatting, checking, and rendering.

The important part is that the *process* is written down inside the project, not in my head. Every session starts with the assistant reading the same rules I would give a human helper, so the results are consistent from month to month even though the conversation is different every time.

## What is in the folder

- **`reference/`** — the March, April, and May 2026 issues, plus each new issue as it is published. These are the style examples. When I started, the assistant read them to learn our section order, how we caption photos, and how the Treasurer's table is laid out.
- **`shared/`** — the evergreen "SOARA Information" page: meeting location, repeaters, nets, officers, and contacts. It is edited in one place and pasted into every issue, so a corrected meeting time only has to be fixed once.
- **`templates/`** — one fill-in-the-blank template per recurring section (President's Message, SOARA Saturday report, feature article, Treasurer's report, calendar, and so on), the master newsletter layout, and the CSS that controls how the PDF looks.
- **`docs/`** — the editorial style guide, the monthly schedule, and a step-by-step generation guide. These are plain-English documents. They are what the assistant follows.
- **`tools/`** — four small Python scripts: one renders the newsletter to PDF, one shrinks a photo-heavy PDF for email, one keeps a running history of every Recommended Link we have ever published (so we do not recommend the same video twice), and one generates the announcement email from the finished issue so the dates in the email always match the dates in the PDF.
- **`issues/2026-09/`** (and one folder like it per month) — the working space for that issue. It has an `_inbox` for raw material exactly as it arrived, a `submissions` folder for the cleaned-up versions, an `assets` folder for photos, the assembled newsletter, the checklist, and the rendered PDF.

## What a month looks like

**Collecting.** Contributors send me material however is easiest for them — a pasted email, a Word document, a PDF, photos with a couple of lines of caption. I drop all of it into the inbox untouched. Nothing is ever edited in place; the original always stays as the source record.

**Normalizing.** I open the project in a chat window and say something like "Start the September issue." The assistant copies the template folder, then goes through the inbox item by item, extracts the text from whatever format it came in, and creates a structured file for each submission with the author, callsign, and date filled in. Each of those files has an "Editor Notes" section at the bottom where the assistant lists anything it thinks I should verify: a callsign it could not confirm, a date that does not match the calendar, a link it could not open, a technical claim it is not sure about.

**The one rule I care most about.** Written into the project, in bold, is this: *contributor content is preserved as written.* The assistant may fix spelling, grammar, and punctuation. It may not condense, summarize, reorder, or cut anything, and it may not drop your tables, figures, or examples. Length is not a reason to shorten an article. If something looks factually wrong, it does not get quietly "fixed" — it goes in the Editor Notes and I take it back to the author. I put this rule in because it is exactly the kind of thing an AI tool will do helpfully and wrongly if you do not tell it otherwise. Your article is your article.

**The Treasurer's report.** Ron sends the club's full general ledger workbook every month. Most of that is internal bookkeeping and is not for publication. Ron marks off one block in the spreadsheet labeled "Financial Statement for Propagator," and the project rules say to use that block and nothing else: reproduce the figures exactly, in the same table format as last month. The assistant then re-adds the subtotals to make sure they tie out and checks that this month's beginning cash equals last month's ending cash. If anything does not tie, it flags it; it does not change it. Numbers get printed the way the Treasurer sent them.

**Assembling and checking.** The submissions get placed into the newsletter in our standard order — events calendar on the front page, then the President's Message, SOARA Saturday, club news, Recommended Links, feature articles, the Treasurer's report, and the evergreen SOARA Information page at the back. The Recommended Links script checks the new links against the history file. The calendar dates get checked against the standing schedule. Then we go through the production checklist together.

**Rendering.** One command turns the newsletter into the PDF, with the masthead, an auto-generated "In This Issue" list, and the photos and captions in place. I read the whole thing. Usually there are a couple of layout problems — a sign-off orphaned on its own page, a table split in half — and we fix the layout and render again. The finished PDF gets published, the announcement email gets generated from it, and a copy goes into the reference folder to be next month's example.

## What I have learned

- **Write the rules down, then let the tool follow them.** The style guide and the generation guide took an evening to write. They have paid for themselves many times over, and they would be just as useful to a human successor as they are to the assistant.
- **Keep the raw material, the cleaned-up version, and the finished issue separate.** This is what makes "preserve the author's wording" enforceable instead of aspirational. I can always diff what ran against what was sent.
- **The AI is good at the tedious parts and needs supervision on the judgment parts.** It is very good at pulling text out of a Word document, checking that a list of dates matches a calendar, and re-adding a column of numbers. It is not the one who decides whether an email to the Board was meant as an article, or which of eight photos actually shows the thing being described. Those are still my calls, and the process is built so those questions come to me instead of being guessed at.
- **Consistency is the real win.** Every issue is built the same way, so the errors that creep into a hand-assembled newsletter — a stale meeting time, a repeated link, a Treasurer's table that looks different from last month's — get caught by the process rather than by a sharp-eyed reader after publication.

## If you want to try this for your own club or project

The whole thing is just a folder of text files and a handful of scripts; there is nothing exotic in it. I keep a starter prompt in the project that will scaffold the same structure for any club in a few minutes. If you are curious, catch me at a meeting or on the Tuesday net and I will walk you through it. And if you have something for the Propagator — an article, a photo, a link you think the club would enjoy — send it to <k6nov@soara.org>. It will arrive in the inbox exactly as you wrote it, and that is how it will leave.

73,
Ray, K6NOV

## Editor Notes

- Author's own piece; no fact-check items beyond confirming the Publications
  contact address.
- Issue placement TBD (holding until the September issue closes).
