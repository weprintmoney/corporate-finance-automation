# Corporate Finance Automation

Informal shared context repository for the NYU Corporate Finance (Damodaran) Fall 2026 cohort — notes, models, valuation examples, and course materials. Maintained by Charlcye Mitchell; open for reference by classmates.

## Course

**NYU Stern — Corporate Finance with Prof. Aswath Damodaran, Fall 2026**

| Role | Name | Contact |
|------|------|---------|
| Instructor | Aswath Damodaran | [LinkedIn](https://www.linkedin.com/in/aswathdamodaran/) |
| TA | Roberto Chavez | rchavezg.nyu@yahoo.com · WhatsApp +51995957995 · @rchavezgam |
| Maintainer | Charlcye Mitchell | `weprintmoney` on GitHub |

WhatsApp group: [Corp Finance Fall 2026](https://chat.whatsapp.com/ChFjKrUfgTyIqNdsau2Bhv) (13 members)

## Class Roster

| Name | Location | WhatsApp | LinkedIn | Background |
|------|----------|----------|----------|------------|
| Charlcye Mitchell | Austin, TX, USA | @MotivateMe (admin) | [LinkedIn](https://www.linkedin.com/in/camitchell) | Product Manager; agentic AI systems; teaching community AI courses |
| Luisa Ghied | Sweden (Filipino) | — | — | Finance career-builder |
| Jose Domingo Rivarola Reisz | Lima, Peru | @josedomingo.rivarola.reisz | [LinkedIn](https://pe.linkedin.com/in/domingo-rivarola-64a44b15b) | Arbitration & litigation lawyer; teaches evidence law at PUCP; LLM UVA |
| Mehdi Benmebarek | Paris, France | — | [LinkedIn](https://www.linkedin.com/in/mehdi-benmebarek-4273425/) | Strategy & BD; 20+ yrs aerospace/defense, professional services, identity security |
| Edy Jimenez | Dominican Republic | @eejimenezt | [LinkedIn](https://do.linkedin.com/in/edyjimeneztoribio) | VP Commerce, AES Dominicana; energy sector across LatAm & Caribbean |
| Matthias Wiltschek | Vienna, Austria | — | [LinkedIn](https://at.linkedin.com/in/matthias-wiltschek-73783810b) | M&A and post-merger integration at a manufacturing company |
| Hugo Nieto | Mexico City, Mexico | — | [LinkedIn](https://www.linkedin.com/in/hugo-nieto-6952b31ab/) | Investment banking, valuation, capital raising |
| Grace Liu | Mainland China | — | — | 20 yrs food manufacturing & international trading |
| Simona Morachioli | Tuscany, Italy | — | [LinkedIn](https://it.linkedin.com/in/simona-morachioli) | Chief Transformation Officer, PE-backed pharma; engineer by training |
| Horton Fisher | USA | — | [LinkedIn](https://www.linkedin.com/in/horton-fisher-0729b6217/) | NYU Stern MBA |
| Valentyn Burianov | Ukraine | — | [LinkedIn](https://www.linkedin.com/in/valentyn-burianov-23a824359/) | — |
| Aldo | Italy | — | — | — |
| Allan | Malta | — | — | — |
| Jennifer Conrad | — | — | — | — |

*Sources: Brightspace discussion board + WhatsApp group. Last updated 2026-09-01.*

## Top-level Folders

| Folder | Purpose |
|--------|---------|
| `01-primers/` | Pre-course primers — accounting, statistics, risk & return, present value |
| `02-financial-accounting/` | Ledgers, financial statements, ratio analysis, journal-entry drills |
| `03-corporate-finance/` | TVM, valuation, capital structure, capital budgeting, cost of capital |

Each folder has its own `CLAUDE.md` with subject-specific context, key formulas, and a doc index.

## Doc Index

| Area | File | Description |
|------|------|-------------|
| Primers | `01-primers/CLAUDE.md` | Damodaran pre-course primers (accounting, statistics, risk & return, PV) + stats quick reference |
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
