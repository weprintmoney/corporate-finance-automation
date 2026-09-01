# Corporate Finance Automation

Context repository for **Aswath Damodaran's NYU Executive Education Corporate Finance Certificate — Fall 2026**. Structured as a Claude Code knowledge base so any AI session opened here already knows the course material, where everything lives, and how to apply it.

---

## What this is

Damodaran's Applied Corporate Finance course covers how firms value cash flows, choose projects, and finance themselves. This repo holds:

- All lecture slides and transcripts (36 lessons across 4 modules)
- Damodaran's spreadsheet tools (betas, ERP calculators, ratings estimators, lease models)
- Assigned readings and blog posts from *Musings on Markets*
- A live data pipeline that pulls market rates and company financials from FRED and Financial Modeling Prep
- Company valuation reports produced by the `/evaluate-company` command

The course follows Damodaran's standard valuation framework: estimate a risk-adjusted cost of capital, project cash flows, and discount them to a present value. Every tool in the repo supports one of those three steps.

---

## What's inside

```
01-statistics/               Probability, distributions, hypothesis tests, regression
02-financial-accounting/     Financial statements, ratio analysis, journal-entry drills
03-corporate-finance/        The main course — TVM, WACC, valuation, capital structure
  ├── 03-1-course-overview/    Syllabus, schedule, FAQ, key dates
  ├── 03-2-course-content/     All 36 lessons organized by module
  │   ├── lesson-index.yaml  Navigation index — find any lesson in one read
  │   ├── module-1/          Foundations & discount rates (lessons 01–12)
  │   ├── module-2/          (in progress)
  │   ├── module-3/          (in progress)
  │   ├── module-4/          (in progress)
  │   └── company-valuations/  Output reports from /evaluate-company runs
  ├── 03-3-supplemental-data/  Live data refreshed by CI
  │   ├── market-rates.json  US 10-yr Treasury, SOFR, Fed Funds (updated weekdays)
  │   ├── companies/         Per-ticker financial statements from SEC via FMP
  │   └── damodaran/         Industry betas and country risk premiums
  └── 03-4-blogs/              Damodaran "Musings on Markets" archive (~680 posts)
```

Each folder has a `CLAUDE.md` that orients an AI session to that subject — formulas, conventions, and a doc index. Navigation from root to any lesson takes three hops: `CLAUDE.md` → subject `CLAUDE.md` → `03-2-course-content/CLAUDE.md` → `lesson-index.yaml` → lesson folder.

---

## Lesson content

Each lesson folder contains some combination of:

| File type | What it is |
|-----------|------------|
| `slides.md` | Lecture slides converted to markdown (full text, searchable) |
| `session-N-part-N.md` | Full lecture transcript (cleaned prose) |
| `spreadsheet-*.md` | Damodaran's Excel tools converted to markdown (methodology reference) |
| `*.xls` / `*.xlsx` | Original binary spreadsheet files |
| `reading-*.md` | Assigned readings |
| `blog-*.md` | Damodaran blog posts relevant to the lesson |
| `lesson-overview.md` | Learning objectives and file index for the lesson |

> `.mp4` video files are Git LFS pointers — never read them directly. The `.md` transcript with the same filename is always present and contains the full lecture text. A hook enforces this.

---

## The `/evaluate-company` command

`/evaluate-company` is a 12-step company valuation built on Module 1 of the course. It follows Damodaran's methodology exactly — studying each lesson, then applying it to a real company — and produces a structured markdown report.

**What each step covers:**

| Step | Topic | Key output |
|------|-------|-----------|
| 1 | Pick a company | Creates the report file |
| 2 | Corporate governance | Board, power structure, governance quality |
| 3 | Stated objectives | What the firm is actually optimizing for |
| 4 | Share classes & marginal investor | Who sets the price; are they diversified? |
| 5 | Currency & risk-free rate | Analysis currency; current Treasury yield |
| 6 | Equity risk premium (mature market) | Damodaran implied ERP |
| 7 | Country risk & weighted ERP | Revenue-weighted ERP across geographies |
| 8 | Regression beta | Historical beta; reliability assessment |
| 9 | Beta fundamentals | Business risk, operating leverage, financial leverage |
| 10 | Bottom-up unlevered beta | Industry comparable betas from Damodaran |
| 11 | Levered beta & total beta | Hamada equation; PE vs. public investor perspective |
| 12 | Cost of debt + WACC summary | Synthetic rating, lease capitalization, final WACC table |

**To run it:**

Open Claude Code in this repo and type `/evaluate-company`. Claude will read the lesson materials, ask you to pick a company, then run all 12 steps automatically — reading from `data/` files first, falling back to web search when live data isn't available yet.

Output is saved to `03-corporate-finance/03-2-course-content/company-valuations/<company>-valuation.md`.

**Example:** The SolarWinds (SWI) valuation is in `03-corporate-finance/03-2-course-content/company-valuations/` — both as a markdown report and as a standalone HTML file.

---

## Live data pipeline

Three GitHub Actions workflows keep valuation inputs current:

| Workflow | Trigger | What it fetches | Output |
|----------|---------|----------------|--------|
| `refresh-market-rates` | Weekdays 9 AM CT | FRED: 10-yr Treasury, SOFR, Fed Funds | `03-3-supplemental-data/market-rates.json` |
| `fetch-company-financials` | Manual (enter ticker) | FMP: income statement, balance sheet, cash flow | `03-3-supplemental-data/companies/{ticker}.json` |
| `refresh-damodaran` | 1st of each month | Damodaran: industry betas, country risk | `03-3-supplemental-data/damodaran/` |

**Required GitHub secrets:**
- `FRED_API_KEY` — free at [fred.stlouisfed.org](https://fred.stlouisfed.org/docs/api/api_key.html)
- `FMP_API_KEY` — free tier at [financialmodelingprep.com](https://financialmodelingprep.com)

You can also run the scripts locally:

```bash
FRED_API_KEY=your_key python3 scripts/fetch-market-data.py
FMP_API_KEY=your_key python3 scripts/fetch-company-data.py AAPL
pip install xlrd openpyxl && python3 scripts/fetch-damodaran.py
```

---

## Conventions

- **Naming:** all files and folders use kebab-case. Enforced by a pre-commit hook.
- **Branching:** direct push to `main` is blocked. Branch → open PR → self-merge (admin merge is fine, this is a solo repo).
- **Frontmatter:** every non-`CLAUDE.md` markdown doc carries `title`, `status`, `owner`, `created`, `last_updated`. Enforced by the `no-unowned-files` CI check.
- **Video files:** never read `.mp4` directly — the `.md` transcript is always present alongside it.

---

## Key reference files

| File | What it tells you |
|------|------------------|
| [`CLAUDE.md`](CLAUDE.md) | Repo map, top-level conventions, doc index |
| [`03-corporate-finance/CLAUDE.md`](03-corporate-finance/CLAUDE.md) | TVM/WACC/valuation formulas, data directory index |
| [`03-corporate-finance/03-2-course-content/lesson-index.yaml`](03-corporate-finance/03-2-course-content/lesson-index.yaml) | Full map of all 36 lessons — folders, topics, available file types |
| [`.claude/commands/evaluate-company.md`](.claude/commands/evaluate-company.md) | The complete `/evaluate-company` command definition |
