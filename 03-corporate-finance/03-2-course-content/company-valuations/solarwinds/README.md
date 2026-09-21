---
title: "SolarWinds (SWI) — Course Project Overview"
status: active
owner: weprintmoney
created: 2026-09-20
last_updated: 2026-09-20
---

# SolarWinds (SWI) — Course Project Overview
*Applied Corporate Finance — all 4 modules, working through the course video-by-video, now with answers*

## Purpose & method

For every lecture video transcript across all 36 lessons (68 video parts; Lesson 24 has no transcript), this project captures:

- **A quote** — one short, verbatim line from the lecture that anchors the concept being taught
- **A question for SWI** — the specific thing that concept raises about SolarWinds when you actually try to apply it, not a generic textbook question
- **Sources needed** — what data or document would answer that question
- **Where to find it** — a concrete pointer, using the Source Key below
- **Answer** — the question actually worked, using the compiled source documents in [`sources/`](sources/) (SEC filings, peer 10-Ks, market data) plus the existing [`valuation-report.md`](valuation-report.md) 12-step report

**A material caution on that existing 12-step report:** answering these 68 questions surfaced the same two errors independently, from five separate passes over the filings, so treat them as confirmed rather than a single analyst's mistake:

1. **Equity value vs. enterprise value.** The report derives ~237M diluted shares by dividing the $4.4B deal value by $18.50/share — but $4.4B is *enterprise* value. Actual shares outstanding are 171.6M (185.0M fully diluted); equity consideration was ~$3.2–3.4B depending on convention. This shifts the debt/equity weights used for WACC from 23.1%/76.9% to roughly 28–29%/71–72%.
2. **Ownership concentration.** The report states Silver Lake alone controlled ~75%. DEF 14A 2024 and the merger information statement show the block was **Silver Lake (~35–36.6%) and Thoma Bravo (~28.9–29.8%) together, ~64–66%** — both sponsors' written consent was required for a change of control, not Silver Lake's alone.

A third, narrower correction: the report and several original question stems say SWI "never paid a common dividend." It paid two special dividends — $1.50/share ($237.2M, Aug 2021) and $1.00/share ($168.2M, Apr 2024) — $405.4M total.

None of `valuation-report.md`'s steps have been rewritten to reflect these corrections; each affected answer in the lesson files below notes the correction inline where it matters. Fixing the report itself is a natural next pass, not done here.

## Company context: SolarWinds (SWI)

IT infrastructure monitoring/observability SaaS company. Taken private 2016 by Thoma Bravo + Silver Lake (~$4.5B LBO), re-IPO'd Oct 2018 (NYSE: SWI). December 2020: the SUNBURST nation-state supply-chain cyberattack (~18,000 customers affected, including federal agencies). CEO Kevin Thompson's departure was announced December 7, 2020 — **before** the SUNBURST 8-K was filed December 9 (which he signed as CEO) — so the common "resigned because of SUNBURST" framing has the chronology backwards; Sudhakar Ramakrishna became CEO January 2021. April 2025: acquired by Turn/River Capital and taken private again, $18.50/share (~$4.4B, ~5.5x 2024 revenue) via a Schedule 14C information statement (written stockholder consent — no proxy vote was solicited). FY2024 is the final full year of public filings. Silver Lake and Thoma Bravo together (not Silver Lake alone) were the controlling shareholders driving the sale — see the correction above.

## Source Key

Cited by these short codes throughout. As of 2026-09-07, most of these are now **compiled locally** in [`sources/`](sources/) — see that folder's [README.md](sources/README.md) for the full manifest, what's still missing, and why.

| Code | What it is | Status |
|------|-----------|--------|
| **SEC-EDGAR** | SEC EDGAR filings for SWI — 10-K (FY2024/2023/2020/2018 + a multi-year financial summary), 10-Q, 8-K (SUNBURST Dec 2020, Turn/River deal), DEF 14A proxy, S-1 IPO prospectus, and the going-private merger document | ✅ Compiled — [`sources/sec-filings/`](sources/sec-filings/). **Correction:** the merger document is a **Schedule 14C definitive information statement (DEFM14C)**, not a 13E-3/DEFM14A — Silver Lake's ~75% stake let the board approve by written consent, so no proxy vote (and, per EDGAR's full filing history, no 13E-3) was filed. Use `swi-defm14c-2025-merger-information-statement.md`. |
| **REPO-SWI-VAL** | [valuation-report.md](valuation-report.md) — this folder's existing 12-step governance/objectives/cost-of-capital research on SWI | ✅ Already in repo |
| **REPO-RATES** | `03-3-supplemental-data/market-rates.json` — 10Y Treasury, SOFR, Fed Funds; supposed to be CI-refreshed weekdays | ⚠️ **This file doesn't exist in the repo** — the CI job that's supposed to create/refresh it appears to have never run or is silently failing. Use [`sources/market-data/treasury-and-fed-rates.md`](sources/market-data/treasury-and-fed-rates.md) instead (manual FRED snapshot, fetched 2026-09-07) until that's fixed. |
| **REPO-BETAS** | `03-3-supplemental-data/industry-betas.json` — Damodaran sector unlevered/levered betas | ⚠️ **File exists but is an empty stub** (`"industries": {}`) — same broken-CI issue as REPO-RATES. Use [`sources/market-data/damodaran-industry-betas-software.md`](sources/market-data/damodaran-industry-betas-software.md) instead (Software (System & Application) row, fetched fresh from the live Damodaran dataset). |
| **REPO-COUNTRY-RISK** | `03-3-supplemental-data/country-risk.json` — country equity risk premiums | ⚠️ **File exists but is an empty stub** (`"countries": {}`) — same issue. Use [`sources/market-data/damodaran-country-risk-premium-us.md`](sources/market-data/damodaran-country-risk-premium-us.md) instead. |
| **DAMODARAN-SITE** | pages.stern.nyu.edu/~adamodar — live Damodaran datasets/spreadsheets. The repo's local mirror at `03-5-damodaran-online/` is currently excluded from navigation (corrupted import, pending re-fetch) | ✅ Partly compiled — industry betas and country risk premium are now in `sources/market-data/` (see REPO-BETAS/REPO-COUNTRY-RISK above). Multiples/margins/growth-rate datasets for Module 4 were **already present locally** before this pass — see `LESSON-MATERIALS` below, lesson-35 specifically. For anything else, go to the live NYU site, not the local mirror. |
| **DAMODARAN-BLOG** | [`03-4-blogs/posts/`](../../../03-4-blogs/posts/) — ~680 "Musings on Markets" posts, fully imported and searchable locally | ✅ Already in repo |
| **PEER-FILINGS** | SEC EDGAR filings of comparable public observability/IT-ops SaaS peers — Datadog (DDOG), Dynatrace (DT), PagerDuty (PD) | ✅ Compiled — [`sources/peer-filings/`](sources/peer-filings/) (each company's most recent 10-K; all three still independently public) |
| **DEAL-DOCS** | Turn/River Capital's acquisition press release + fairness opinion | ✅ Compiled — the 8-Ks and the DEFM14C in `sources/sec-filings/` cover this (see the SEC-EDGAR correction above; there is no separate "press release" filing beyond the 8-Ks) |
| **LESSON-MATERIALS** | That lesson's own `slides.md` / `reading-*.md` / `spreadsheet-*.md` in the same lesson folder | ✅ Already in repo — e.g. lesson-35's `spreadsheet-*.md` files already carry current Damodaran multiples/margins by sector (Software (System & Application) row present) |
| **NEWS-WEB** | General news/analyst commentary not otherwise covered | ⚠️ **Not compilable as a fixed document** — this is ongoing commentary/sentiment, re-search at time of use. One concrete sub-need — SWI's historical daily stock price series for regression-beta/Jensen's-alpha entries — was attempted and is genuinely unattainable via free automated fetch (Stooq blocks bots, Nasdaq drops delisted tickers); see `sources/README.md` for the workaround (DEF 14A performance-graph data) and paid-terminal alternative. |

## How this folder is organized

This project applies each lecture's concepts to a real company — SolarWinds (NYSE: SWI), taken private by Turn/River Capital in April 2025 — across all 36 lessons of the course, working lesson-by-lesson rather than as a single report.

- **[`valuation-report.md`](valuation-report.md)** — the original Module 1, 12-step cost-of-capital report (Steps 2–12 + summary WACC table). See the material caution above for two confirmed errors in its WACC weights and ownership-concentration claims, plus the dividend correction.
- **[`valuation-report-standalone.html`](valuation-report-standalone.html)** — a standalone HTML render of the report above.
- **[`sources/`](sources/)** — compiled source documents (SEC filings, peer filings, market data) backing every answer below. See [`sources/README.md`](sources/README.md) for the full manifest, what's still missing, and why.
- **`lesson-01.md` through `lesson-36.md`** — one file per lesson. Each carries that lesson's quote/question/sources/answer entries verbatim, plus a `## Notes` section synthesizing what the lesson taught, why it mattered for this analysis, and how it connects to adjacent lessons. Lesson 24 has no transcript — see `lesson-24.md` for why.

| Module | Lessons | Files |
|---|---|---|
| Module 1 — Foundations & Discount Rates | 1–12 | [lesson-01](lesson-01.md) · [02](lesson-02.md) · [03](lesson-03.md) · [04](lesson-04.md) · [05](lesson-05.md) · [06](lesson-06.md) · [07](lesson-07.md) · [08](lesson-08.md) · [09](lesson-09.md) · [10](lesson-10.md) · [11](lesson-11.md) · [12](lesson-12.md) |
| Module 2 — Investment Returns & Financing | 13–19 | [13](lesson-13.md) · [14](lesson-14.md) · [15](lesson-15.md) · [16](lesson-16.md) · [17](lesson-17.md) · [18](lesson-18.md) · [19](lesson-19.md) |
| Module 3 — Financing Mix & Dividends | 20–26 | [20](lesson-20.md) · [21](lesson-21.md) · [22](lesson-22.md) · [23](lesson-23.md) · [24](lesson-24.md) (no transcript) · [25](lesson-25.md) · [26](lesson-26.md) |
| Module 4 — Dividends & Valuation | 27–36 | [27](lesson-27.md) · [28](lesson-28.md) · [29](lesson-29.md) · [30](lesson-30.md) · [31](lesson-31.md) · [32](lesson-32.md) · [33](lesson-33.md) · [34](lesson-34.md) · [35](lesson-35.md) · [36](lesson-36.md) |
