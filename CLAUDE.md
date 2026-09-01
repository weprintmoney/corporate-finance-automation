# Corporate Finance Automation

Informal shared context repository for the NYU Corporate Finance (Damodaran) Fall 2026 cohort — notes, models, valuation examples, and course materials. Maintained by Charlcye Mitchell; open for reference by classmates.

## Course

**NYU Stern — Corporate Finance with Prof. Aswath Damodaran, Fall 2026**

| Role | Name | Contact |
|------|------|---------|
| Instructor | Aswath Damodaran | [LinkedIn](https://www.linkedin.com/in/aswathdamodaran/) |
| TA | Roberto Chavez | rchavezg.nyu@yahoo.com · WhatsApp +51995957995 |
| Maintainer | Charlcye Mitchell | `weprintmoney` on GitHub |

WhatsApp group: "Corp Finance Fall 2026" (13 members — ask Edy Jimenez or Charlcye for the link)

## Class Roster

Full roster with LinkedIn, WhatsApp, background, and goals: [`03-corporate-finance/class-roster.yaml`](03-corporate-finance/class-roster.yaml)

| Name | Location | Background |
|------|----------|------------|
| Charlcye Mitchell | Austin, TX, USA | Product Manager, agentic AI |
| Luisa Ghied | Sweden | Finance career-builder |
| Jose Domingo Rivarola Reisz | Lima, Peru | Arbitration & litigation lawyer |
| Mehdi Benmebarek | Paris, France | Strategy & BD, aerospace/defense |
| Edy Jimenez | Dominican Republic | VP Commerce, AES Dominicana (energy) |
| Matthias Wiltschek | Vienna, Austria | M&A & post-merger integration |
| Hugo Nieto | Mexico City, Mexico | Investment banking & valuation |
| Grace Liu | Mainland China | Food manufacturing & international trading |
| Simona Morachioli | Tuscany, Italy | Chief Transformation Officer, PE pharma |
| Horton Fisher | USA | NYU Stern MBA |
| Valentyn Burianov | Ukraine | — |
| Aldo | Italy | — |
| Allan | Malta | — |

## Top-level Folders

| Folder | Purpose |
|--------|---------|
| `01-statistics/` | Probability, distributions, hypothesis tests, regression |
| `02-financial-accounting/` | Ledgers, financial statements, ratio analysis, journal-entry drills |
| `03-corporate-finance/` | TVM, valuation, capital structure, capital budgeting, cost of capital |

Each folder has its own `CLAUDE.md` with subject-specific context, key formulas, and a doc index.

## Doc Index

| Area | File | Description |
|------|------|-------------|
| Class Roster | `03-corporate-finance/class-roster.yaml` | Full cohort — LinkedIn, WhatsApp, background, goals |
| Statistics | `01-statistics/CLAUDE.md` | Distributions, tests, regression, formula sheet |
| Financial Accounting | `02-financial-accounting/CLAUDE.md` | Accounting equation, statements, GAAP conventions, per-topic notes |
| Corporate Finance | `03-corporate-finance/CLAUDE.md` | TVM, valuation, WACC, capital budgeting |
| Kebab-case naming rule | `.claude/rules/kebab-case-naming.md` | File and folder naming convention (enforced by hook) |
| Doc frontmatter schema | `.claude/rules/doc-frontmatter-schema.md` | Frontmatter schema for non-CLAUDE.md docs |
| Update doc index rule | `.claude/rules/update-doc-index.md` | Keep parent CLAUDE.md indexes in sync when files are added |

## Conventions

- **File and folder naming:** kebab-case — `present-value-notes.md`, not `Present Value Notes.md`; `course-overview/`, not `Course Overview/`. Filenames enforced by hook; folders enforced by convention. Full rule: `.claude/rules/kebab-case-naming.md`.
- **Frontmatter:** every non-`CLAUDE.md` markdown doc carries the frontmatter block defined in `.claude/rules/doc-frontmatter-schema.md`.
- **Branching:** direct push to `main` is blocked. Branch → PR → admin merge.
- **Folder indexes:** when a file is added to a folder that has a `CLAUDE.md`, update that `CLAUDE.md`'s doc index.
