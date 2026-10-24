---
title: "/evaluate-company — Module 1 scope of /value-company"
status: active
owner: weprintmoney
created: 2026-08-27
last_updated: 2026-10-24
---

# /evaluate-company

Superseded by the `/value-company` skill, which covers all four modules. This command keeps the old name and runs the Module 1 scope only: the twelve cost-of-capital steps (lessons 1–12), the ledger, the model's cost-of-capital section, and the walkthrough sections for those steps.

Do this:

1. Read `.claude/skills/value-company/SKILL.md` in full.
2. Run it with `scope = module-1`: Phase 0 (profile, pause for a yes), Phase 1 (sources), Phase 2 (ledger and model), Phase 3 (lessons 1–12), then stop and report.
3. Output goes to `03-corporate-finance/03-2-course-content/company-valuations/<slug>/` in the layout SKILL.md describes. There is no separate `<slug>-valuation.md` any more; the Module 1 result is the ledger plus `lesson-01.md` to `lesson-12.md` plus the cost-of-capital section of `model-output.md`.

The older single-file reports in `company-valuations/` (`dynatrace-valuation.md`, `minio-valuation.md`, `openai-valuation.md`, `abc-home-and-commercial-services-valuation.md`) were produced by the previous version of this command and stay as they are.
