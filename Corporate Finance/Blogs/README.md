---
title: "Damodaran Blog Archive — Fetcher"
status: active
owner: weprintmoney
created: 2026-08-27
last_updated: 2026-08-27
---

# Damodaran Blog Archive

Local mirror of Aswath Damodaran's [*Musings on Markets*](https://aswathdamodaran.blogspot.com/) for personal text analysis (topic modeling, citation graphs, longitudinal readings).

## What's in this folder

| File | Purpose |
|------|---------|
| `fetch_archive.py` | Pulls every post from Blogger's public JSON feed, converts each to markdown with attribution frontmatter, and writes to `posts/`. |
| `.gitignore` | Excludes `posts/` from git — the mirror stays on disk, not in history. |
| `README.md` | This file. |

## Why `posts/` is gitignored

Blog posts are copyrighted by the author. Fetching them into a private working directory for personal analysis is fine; committing the full text to a repo (even a private one) is a different act. Keeping `posts/` out of git lets us rebuild the mirror any time from source while the repo itself only ships the fetcher.

## Run it

```bash
cd "Corporate Finance/Blogs"
python3 fetch_archive.py            # first run: pulls all ~680 posts
python3 fetch_archive.py            # subsequent runs: only writes new/missing files
python3 fetch_archive.py --refresh  # force re-download of everything
python3 fetch_archive.py --limit 20 # for testing
```

Standard library only — no `pip install` needed.

## Output shape

Each post lands at `posts/YYYY-MM-DD-slug.md` with frontmatter:

```yaml
---
title: "..."
author: aswath-damodaran
status: active
owner: weprintmoney
source_url: https://aswathdamodaran.blogspot.com/...
published: 2026-07-29
updated_source: 2026-07-29
fetched: 2026-08-27
tags:
  - Earnings Reports
---
```

The `source_url` is the authoritative link back — always cite it when using content in downstream notes.

## Analysis ideas

- Topic drift over the ~17-year archive (grep tags across years)
- Which valuation frameworks / companies recur most
- Reading list ordering by tag for coursework
