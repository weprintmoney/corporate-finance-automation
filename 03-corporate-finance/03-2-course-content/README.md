# Corporate Finance — Course Content

Applied Corporate Finance course content, organized by module and lesson.

## Structure

```
03-2-course-content/
├── 01-foundations-and-discount-rates/   Lessons 01–12
├── 02-investment-returns-and-financing/ Lessons 13–19
├── 03-financing-mix-and-dividends/      Lessons 20–26
└── 04-dividends-and-valuation/          Lessons 27–36
```

Each lesson folder contains:
- `lesson-overview.md` — objectives, video links, project questions, file index
- `slides.pdf` + `slides.md` — slide deck (markdown converted with marker; extracted charts in `slides-images/`)
- `spreadsheet-*.md` — converted data spreadsheets (raw `.xls` alongside)
- `reading-*.md` — converted readings (raw `.pdf` alongside)
- `blog-*.md` — Damodaran blog posts (copied from `../03-4-blogs/posts/` archive when available)
- `session-N-part-P.md` / `.mp4` — lecture transcripts and recordings

## Export script

`brightspace-export.py` pulls everything above from NYU Brightspace. Auth is
cookie-based — copy `d2lSessionVal` / `d2lSecureSessionVal` from a logged-in
browser session into `.brightspace.env` at the repo root (gitignored; template
in the script header).

```bash
# All lessons missing a lesson-overview.md
python3 03-corporate-finance/03-2-course-content/brightspace-export.py

# Specific modules or a single lesson
python3 03-corporate-finance/03-2-course-content/brightspace-export.py --modules 2 3 4
python3 03-corporate-finance/03-2-course-content/brightspace-export.py --lesson 13

# Re-convert slides.md from slides.pdf with marker (e.g. after a converter upgrade)
python3 03-corporate-finance/03-2-course-content/brightspace-export.py --modules 1 --force --reconvert-slides
```

PDF→markdown uses [marker](https://github.com/datalab-to/marker) (vision-native —
captures charts, equations, and images that text-only extractors miss).
Dependencies: `pip install marker-pdf requests beautifulsoup4 pandas openpyxl` and
`brew install llama.cpp`.

The Financial Accounting course has its own variant at
`02-financial-accounting/modules/brightspace-export.py` (different Brightspace
TOC structure — lessons are D2L modules there).

## Skills

### `/evaluate-company`

Walks through a 12-step company valuation project tied to Module 1 lessons.  
Command file: `.claude/commands/evaluate-company.md`

Each step reads the relevant lesson, researches your chosen company on the web, and appends findings to a report saved at:
```
03-corporate-finance/03-2-course-content/company-valuations/<company-slug>-valuation.md
```

Invoke it by typing `/evaluate-company` in any Claude Code session in this repo.
