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

## Skills

### `/evaluate-company`

Walks through a 12-step company valuation project tied to Module 1 lessons.  
Command file: `.claude/commands/evaluate-company.md`

Each step reads the relevant lesson, researches your chosen company on the web, and appends findings to a report saved at:
```
corporate-finance/03-2-course-content/company-valuations/<company-slug>-valuation.md
```

Invoke it by typing `/evaluate-company` in any Claude Code session in this repo.
