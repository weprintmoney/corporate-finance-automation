# Corporate Finance Automation

Personal working repo for Charlcye's finance coursework — notes, problem sets, models, and the final project. Structured so any AI session starts with the right context for the subject at hand.

## Owner

| Name | GitHub | Role |
|------|--------|------|
| Charlcye Mitchell | `weprintmoney` | Solo — sole contributor |

Solo repo — no PR approvals or CODEOWNERS. Direct-push to `main` is still blocked by hook; use a branch + PR (self-merge) so history stays clean.

## Top-level Folders

| Folder | Purpose |
|--------|---------|
| `financial-accounting/` | Ledgers, financial statements, ratio analysis, journal-entry drills |
| `statistics/` | Probability, distributions, hypothesis tests, regression |
| `corporate-finance/` | TVM, valuation, capital structure, capital budgeting, cost of capital |
| `final-project/` | Capstone: problem framing, data, model, write-up |

Each folder has its own `CLAUDE.md` with subject-specific context, key formulas, and a doc index.

## Doc Index

| Area | File | Description |
|------|------|-------------|
| Financial Accounting | `financial-accounting/CLAUDE.md` | Accounting equation, statements, GAAP conventions, per-topic notes |
| Statistics | `statistics/CLAUDE.md` | Distributions, tests, regression, formula sheet |
| Corporate Finance | `corporate-finance/CLAUDE.md` | TVM, valuation, WACC, capital budgeting |
| Final Project | `final-project/CLAUDE.md` | Capstone scope, deliverables, data, model |
| Kebab-case naming rule | `.claude/rules/kebab-case-naming.md` | File and folder naming convention (enforced by hook) |
| Doc frontmatter schema | `.claude/rules/doc-frontmatter-schema.md` | Frontmatter schema for non-CLAUDE.md docs |
| Update doc index rule | `.claude/rules/update-doc-index.md` | Keep parent CLAUDE.md indexes in sync when files are added |

## Conventions

- **File and folder naming:** kebab-case — `present-value-notes.md`, not `Present Value Notes.md`; `course-overview/`, not `Course Overview/`. Filenames enforced by hook; folders enforced by convention. Full rule: `.claude/rules/kebab-case-naming.md`.
- **Frontmatter:** every non-`CLAUDE.md` markdown doc carries the frontmatter block defined in `.claude/rules/doc-frontmatter-schema.md`.
- **Branching:** direct push to `main` is blocked. Branch → PR → self-merge (admin merge is fine, this is a solo repo).
- **Folder indexes:** when a file is added to a folder that has a `CLAUDE.md`, update that `CLAUDE.md`'s doc index.
