# SolarWinds (SWI) — Compiled Sources

Source materials actually gathered for [`solarwinds-lesson-questions.md`](../solarwinds-lesson-questions.md), so the ~130 "Where to find" pointers in that document lead to something already sitting in this repo instead of a fresh search each time. Everything here was fetched from public sources on **2026-09-07**; treat anything time-sensitive (rates, betas, ERP) as a snapshot, not a live feed.

## What's compiled

### `sec-filings/` — SolarWinds Corp (SEC CIK 0001739942, ticker SWI while public)

| File | What it is | Filed |
|---|---|---|
| `swi-10k-fy2024.md` | Final full-year 10-K as a public company — the primary analytical anchor | 2025-02-19 |
| `swi-10k-fy2023.md` | Prior-year 10-K, for trend comparison | 2024-02-16 |
| `swi-10k-fy2020.md` | The SUNBURST-impact fiscal year | 2021-03-01 |
| `swi-10k-fy2018.md` | First 10-K after the Oct 2018 re-IPO | 2019-02-25 |
| `swi-def14a-2024.md` | Last annual proxy before the Turn/River deal (board, exec comp, beneficial ownership) | 2024-04-11 |
| `swi-s1-2018-ipo-prospectus.md` | 2018 IPO prospectus — pre-IPO capital structure, use of proceeds | 2018-09-21 |
| `swi-defm14c-2025-merger-information-statement.md` | **The going-private deal document** — merger terms, background of the merger, financial advisor's fairness opinion | 2025-03-27 |
| `swi-8k-2025-02-07-merger-agreement-announcement.md` | Announces the Merger Agreement with Turn/River | 2025-02-07 |
| `swi-8k-2025-04-16-merger-closing.md` | Deal closing | 2025-04-16 |
| `swi-8k-2020-12-09-sunburst-disclosure.md` | Initial SUNBURST disclosure | 2020-12-09 |
| `swi-8k-2020-12-14-sunburst-followup.md` | Follow-up SUNBURST disclosure | 2020-12-14 |
| `swi-multi-year-financials.md` | Revenue/EBIT/net income/R&D/capex, FY2017–FY2024, derived from SEC's XBRL company-facts API | fetched 2026-09-07 |

**Correction to the main document:** every "Where to find" citation for the merger document in `solarwinds-lesson-questions.md` says "Schedule 13E-3 / DEFM14A." That's wrong. Silver Lake's ~75% stake let the board approve the merger by **written stockholder consent**, so no vote was solicited and no proxy was filed — the actual document is a **Schedule 14C definitive information statement (DEFM14C)**, and there is no SC 13E-3 on file for this deal at all (confirmed via SEC EDGAR's full filing history for CIK 1739942 — the merger doesn't appear to have been structured as a Rule 13e-3 affiliate going-private transaction). Use `swi-defm14c-2025-merger-information-statement.md`, not a 13E-3.

**Why FY2018/2020/2023/2024 and not all seven years:** these four anchor the arc the lesson questions actually ask about (first post-IPO year, the SUNBURST-impact year, the year before the deal, the final year) at a manageable total size. `swi-multi-year-financials.md` fills the gap for the numbers-only trend lines (FY2017–2024 revenue/EBIT/net income/R&D/capex) without needing all seven full 10-Ks. If a specific question needs FY2019, FY2021, or FY2022 in full, refetch with the accession numbers in the table below.

<details>
<summary>Accession numbers for filings not fetched in full (fetch on demand)</summary>

| Filing | Accession | Primary doc |
|---|---|---|
| 10-K FY2019 | 0001739942-20-000011 | swi-2019123110xk.htm |
| 10-K FY2021 | 0001739942-22-000020 | swi-20211231.htm |
| 10-K FY2022 | 0001739942-23-000019 | swi-20221231.htm |
| DEF 14A 2023 | 0001739942-23-000040 | swi-20230412.htm |
| DEF 14A 2022 | 0001739942-22-000031 | swi2022def14a.htm |

URL pattern: `https://www.sec.gov/Archives/edgar/data/1739942/<accession-no-dashes>/<primary-doc>`

</details>

### `peer-filings/` — comparable public observability/IT-ops SaaS companies

| File | Company | Fiscal year end |
|---|---|---|
| `ddog-datadog-10k.md` | Datadog, Inc. (DDOG) | FY2025 (filed 2026-02-18) |
| `dt-dynatrace-10k.md` | Dynatrace, Inc. (DT) | FY2026 (fiscal year ends March; filed 2026-05-20) |
| `pd-pagerduty-10k.md` | PagerDuty, Inc. (PD) | FY2026 (fiscal year ends January; filed 2026-03-12) |

All three are still independently public as of this fetch — none of the "PEER-FILINGS" citations in the main document need redirecting.

### `market-data/`

| File | Fixes/replaces |
|---|---|
| `treasury-and-fed-rates.md` | `03-3-supplemental-data/market-rates.json` — **see note below, that file doesn't exist** |
| `damodaran-industry-betas-software.md` | `03-3-supplemental-data/industry-betas.json` — **see note below, that file is an empty stub** |
| `damodaran-country-risk-premium-us.md` | `03-3-supplemental-data/country-risk.json` — **see note below, that file is an empty stub** |

## A repo problem this surfaced

`solarwinds-lesson-questions.md` cites `REPO-RATES`, `REPO-BETAS`, and `REPO-COUNTRY-RISK` (18 times combined) as if `03-3-supplemental-data/{market-rates.json,industry-betas.json,country-risk.json}` are live, CI-refreshed data files — that's what the top-level `CLAUDE.md` and the `/evaluate-company` command docs both claim. In practice:

- `market-rates.json` **does not exist** in the repo at all.
- `industry-betas.json` and `country-risk.json` **exist but are empty stubs** — `{"industries": {}}` and `{"countries": {}}` respectively, with only a `source_url` and a note that the CI job should populate them.

Whatever CI job is supposed to refresh these either never ran or has been silently failing. I didn't try to fix that job — I don't know its expected schema or where it lives, and guessing at it risks producing a differently-shaped file than whatever CI eventually writes. The three `market-data/` files above are a manual snapshot workaround for this specific analysis, not a fix to the underlying automation. Worth raising separately.

## Marked unattainable (with why)

| What's needed | Why it's not compiled here |
|---|---|
| **SWI daily/historical stock price series** (2018 IPO – 2025 delisting), needed for regression-beta and Jensen's-alpha calculations in several Module 1/4 entries | Stooq blocks automated fetches behind a JS proof-of-work challenge; Nasdaq's public quote API drops delisted symbols entirely ("Symbol not exists"). No free, script-fetchable source found. **Workaround already available:** the stock-performance graphs in `swi-def14a-2024.md` (and the two other DEF 14As, if fetched) give indexed 5-year return data at annual points — not a full daily series, but usable for a rough return calc. A full daily series would need a paid terminal (Bloomberg/CapIQ/Refinitiv) or a manual export from Yahoo Finance's historical-data page. |
| **Bloomberg / Capital IQ beta or comps** — cited once in the main document as a fallback source | No subscription access. The document already names the fallback (self-computed from raw price data / `REPO-BETAS` industry cross-check), which is the path actually usable here. |
| **Full Moody's/S&P rating-action reports** on SWI (cited for the post-Turn/River rating action) | Full agency reports are subscription-gated. Headline rating actions are sometimes covered in free financial press — that's a live search at time of use, not a fixed document to compile once. |
| **"Analyst commentary" / general news reaction** (the generic half of several `NEWS-WEB` citations — e.g. opoinion on whether the take-private was opportunistic, post-SUNBURST customer-churn commentary) | Not a fixed document by nature — it's an ongoing sentiment/commentary search. Re-run at the time the specific question is actually being answered rather than treating it as something to pre-fetch once. |

## Regenerating everything

Every fetch command is documented in its own file above (SEC EDGAR URLs, Damodaran URLs, FRED URLs). All SEC EDGAR requests require a descriptive `User-Agent` header (SEC's fair-access policy) — e.g. `-H "User-Agent: Your-Project-Name your-email@example.com"`.
