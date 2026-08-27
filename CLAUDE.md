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
| `Financial Accounting/` | Ledgers, financial statements, ratio analysis, journal-entry drills |
| `Statistics/` | Probability, distributions, hypothesis tests, regression |
| `Corporate Finance/` | TVM, valuation, capital structure, capital budgeting, cost of capital |
| `Final Project/` | Capstone: problem framing, data, model, write-up |

Each folder has its own `CLAUDE.md` with subject-specific context, key formulas, and a doc index.

## Doc Index

| Area | File | Description |
|------|------|-------------|
| Financial Accounting | `Financial Accounting/CLAUDE.md` | Accounting equation, statements, GAAP conventions, per-topic notes |
| Statistics | `Statistics/CLAUDE.md` | Distributions, tests, regression, formula sheet |
| Corporate Finance | `Corporate Finance/CLAUDE.md` | TVM, valuation, WACC, capital budgeting |
| Final Project | `Final Project/CLAUDE.md` | Capstone scope, deliverables, data, model |
| Doc frontmatter schema | `.claude/rules/doc-frontmatter-schema.md` | Frontmatter schema for non-CLAUDE.md docs |
| Update doc index rule | `.claude/rules/update-doc-index.md` | Keep parent CLAUDE.md indexes in sync when files are added |

## Conventions

- **File naming:** kebab-case (`present-value-notes.md`, not `Present Value Notes.md`). Enforced by hook.
- **Frontmatter:** every non-`CLAUDE.md` markdown doc carries the frontmatter block defined in `.claude/rules/doc-frontmatter-schema.md`.
- **Branching:** direct push to `main` is blocked. Branch → PR → self-merge (admin merge is fine, this is a solo repo).
- **Folder indexes:** when a file is added to a folder that has a `CLAUDE.md`, update that `CLAUDE.md`'s doc index.
