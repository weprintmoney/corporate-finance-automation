# Corporate Finance — Modules

Applied Corporate Finance course content, organized by module and lesson.

## Structure

```
modules/
├── module-1/   Lessons 01–12  (Risk, Return, and Cost of Capital)
├── module-2/   Lessons 13–19
├── module-3/   Lessons 20–26
└── module-4/   Lessons 27–36
```

Each lesson folder contains:
- `lesson-overview.md` — objectives, video links, file index
- `slides.md` — converted slide deck
- `spreadsheet-*.md` — converted data spreadsheets
- `reading-*.md` — converted readings
- `blog-*.md` — optional Damodaran blog posts

## Content Export

### `brightspace-export.py`

Downloads slides, spreadsheets, and readings from NYU Brightspace; converts them to markdown; generates `lesson-overview.md` per lesson; updates `lesson-index.yaml`.

**Setup:** Create `.brightspace.env` in the repo root (gitignored):
```
D2L_SESSION_VAL=<from DevTools → Application → Cookies → d2lSessionVal>
D2L_SECURE_SESSION_VAL=<from DevTools → d2lSecureSessionVal>
D2L_ORG_UNIT_ID=<from brightspace.nyu.edu/d2l/home/XXXXXX>
D2L_BASE_URL=https://brightspace.nyu.edu
```

**Run:**
```bash
python3 corporate-finance/modules/brightspace-export.py            # all lessons
python3 corporate-finance/modules/brightspace-export.py --lesson 13
python3 corporate-finance/modules/brightspace-export.py --modules 2 3
python3 corporate-finance/modules/brightspace-export.py --toc-only   # inspect raw structure
python3 corporate-finance/modules/brightspace-export.py --dry-run
```

## Skills

### `/evaluate-company`

Walks through a 12-step company valuation project tied to Module 1 lessons.  
Command file: `.claude/commands/evaluate-company.md`

Each step reads the relevant lesson, researches your chosen company on the web, and appends findings to a report saved at:
```
corporate-finance/modules/company-valuations/<company-slug>-valuation.md
```

Invoke it by typing `/evaluate-company` in any Claude Code session in this repo.
