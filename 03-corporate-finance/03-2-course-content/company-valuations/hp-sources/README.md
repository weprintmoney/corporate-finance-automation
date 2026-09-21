# HP (HWP/HPQ) — Compiled Sources

Source materials gathered for [`hp-module-1-prep.md`](../hp-module-1-prep.md), covering the 1990s–2000s window (SEC CIK `0000047217`; traded as **HWP** on the NYSE before the 2002 Compaq merger, **HPQ** after). Everything here was fetched from public sources on **2026-09-11** — the SEC filings are historical and won't change, but the market-data files are point-in-time pulls of a fixed historical window, not a live feed.

## What's compiled

### `sec-filings/` — Hewlett-Packard Company, SEC CIK 0000047217

| File | What it is | Filed | Period covered |
|---|---|---|---|
| `hp-10k-fy1993.md` | Earliest 10-K available on EDGAR (nothing earlier is filed electronically) | 1994-01-28 | FYE 1993-10-31 |
| `hp-10k-fy1993-ex13-annual-report.md` | **Companion to the above.** Pre-2000 HP 10-Ks incorporate the actual financial statements by reference to Exhibit 13 (the Annual Report to Shareholders) rather than including them in the 10-K body — this file is that exhibit, extracted from the same submission. Also carries a 6-year selected-financial-data table back to 1988. | (same filing) | FYE 1993-10-31 (table back to 1988) |
| `hp-10k-fy1996.md` | Mid-1990s snapshot, pre-Agilent-spinoff | 1997-01-29 | FYE 1996-10-31 |
| `hp-10k-fy1996-ex13-annual-report.md` | Companion Exhibit 13 — same incorporation-by-reference pattern as 1993 | (same filing) | FYE 1996-10-31 |
| `hp-10k-fy1999.md` | First 10-K after the 1999 Agilent Technologies spinoff. By this year HP had stopped incorporating financials by reference — the full statements are in the 10-K body itself, no companion exhibit needed. | 2000-01-27 | FYE 1999-10-31 |
| `hp-10k-fy2001.md` | Covers the fiscal year the Compaq merger was announced (Sept 2001) — pre-close | 2002-01-29 | FYE 2001-10-31 |
| `hp-def14a-2001.md` | Routine annual proxy filed immediately before the merger announcement — a "before" governance baseline to contrast against the contested proxy below | 2001-01-25 | FY2001 annual meeting |
| `hp-defc14a-2002.md` | **The contested merger proxy.** This is Walter B. Hewlett's own dissident filing (`DEFC14A`, "Filed by a Party other than the Registrant") opposing the Compaq deal — not management's proxy. Rare primary source: a board member publicly campaigning against his own company's board. | 2002-02-05 | Compaq merger vote (March 2002) |
| `hp-10k-fy2002.md` | First 10-K after the Compaq merger closed (May 2002) — first combined-company financials | 2003-01-21 | FYE 2002-10-31 |
| `hp-10k-fy2005.md` | Mid-2000s snapshot — post-Fiorina (ousted Feb 2005), early Hurd era | 2005-12-21 | FYE 2005-10-31 |
| `hp-10k-fy2009.md` | End of the "2000s" window — post-financial-crisis, post-EDS-acquisition (2008) | 2009-12-17 | FYE 2009-10-31 |

**Why these years and not every year:** these anchor the arc the Module 1 prep doc's lessons actually need — earliest available, a pre-merger mid-90s point, the Agilent-spinoff inflection, immediately pre- and post-Compaq-merger, and a mid/late-2000s point — at a manageable total size. If a specific lesson question needs an in-between year (e.g. FY1997, FY1998, FY2003, FY2007), refetch using the accession-number pattern below.

<details>
<summary>How to refetch any other year</summary>

Full filing history: `https://data.sec.gov/submissions/CIK0000047217.json` (recent filings) plus `.../CIK0000047217-submissions-001.json` (2002–2016) and `.../CIK0000047217-submissions-002.json` (1994–2002) for older ones.

URL pattern once you have an accession number:
- Old-style (pre-2001, no separate primary document — the whole submission is one `.txt`): `https://www.sec.gov/Archives/edgar/data/47217/<accession-with-dashes>.txt`
- Newer style: `https://www.sec.gov/Archives/edgar/data/47217/<accession-no-dashes>/<primary-document>`

All SEC EDGAR requests need a descriptive `User-Agent` header per SEC's fair-access policy.

**Note on pre-2000 filings:** if the 10-K you fetch incorporates financials by reference to "Exhibit 13" or the "Annual Report to Shareholders" (true for FY1993 and FY1996 here, and likely true generally before ~1998), the exhibit is bundled in the same raw submission file — look for a `<TYPE>EX-13` block inside it rather than assuming the 10-K body alone has the financial statements.

</details>

### `market-data/`

| File | Contents | Source | Window |
|---|---|---|---|
| `hpq-monthly-prices-1990-2009.csv` | Monthly OHLC + adjusted close + volume for HPQ (Yahoo continues the pre-2002 HWP price history under the same continuous ticker — no discontinuity at the 2002 rename) | Yahoo Finance chart API | 1990-01 – 2009-12, 240 monthly observations |
| `sp500-monthly-prices-1990-2009.csv` | Same, for the S&P 500 (`^GSPC`) — the market-index side of the beta regression | Yahoo Finance chart API | 1990-01 – 2009-12, 240 monthly observations |
| `dgs10-daily-1989-2009.csv` | Daily 10-Year Treasury Constant Maturity Rate — for the historical risk-free rate at whatever specific valuation date(s) you pick | [FRED DGS10](https://fred.stlouisfed.org/series/DGS10) | 1989-01-02 – 2009-12-31, 5,479 daily observations |

Regenerate with:

```bash
# 10-year Treasury, daily
curl -L "https://fred.stlouisfed.org/graph/fredgraph.csv?id=DGS10" | awk -F, '$1>="1989-01-01" && $1<"2010-01-01"'

# HPQ and S&P 500, monthly (period1/period2 are Unix timestamps)
curl -A "Mozilla/5.0" "https://query1.finance.yahoo.com/v8/finance/chart/HPQ?period1=631152000&period2=1262304000&interval=1mo"
curl -A "Mozilla/5.0" "https://query1.finance.yahoo.com/v8/finance/chart/%5EGSPC?period1=631152000&period2=1262304000&interval=1mo"
```

**Correction to the Module 1 prep doc:** it flagged Stooq as a candidate source for the price history. Stooq blocks automated fetches behind a JS proof-of-work challenge (same problem documented in `solarwinds/sources/README.md` for a different ticker) — **use the Yahoo Finance chart API instead**, which worked directly with no auth. Unlike SolarWinds (delisted, dropped from free quote APIs), HP still trades today as HPQ, so the free historical pull was straightforward once pointed at the right endpoint.

## Known gaps

| What's needed | Status |
|---|---|
| **1990–1992 fiscal-year filings** | Not on EDGAR — HP's earliest electronic filing is the FY1993 10-K (filed 1994-01-28). A "1990s" analysis reaching earlier than FY1993 needs a non-SEC source (Moody's Industrial Manual, ProQuest, or HP's own archived annual reports) — not pursued here. |
| **Bond rating history (S&P/Moody's)** | Not compiled as a standalone document — HP's own 10-Ks generally state the *then-current* rating in the MD&A/liquidity section (check each 10-K above for its own year), but a full rating-action timeline would need a Moody's/S&P subscription or Capital IQ (available ~4–6 weeks into the course per the syllabus). The synthetic-rating method (interest coverage → rating table, per Lesson 12) is a full substitute using only the 10-K's own EBIT/interest-expense figures. |
| **Country-level (not just US/international) revenue breakdown, and historical country-risk premiums** | HP's geographic footnotes in these 10-Ks should be checked per-year for how granular the disclosure actually is; Damodaran's country-risk-premium-by-country data is only reliably archived from roughly 1999–2002 onward (see the Module 1 prep doc's Lesson 7 note) — earlier years may only support a mature-market-ERP approximation. |
| **Comparable-firm filings (Dell, IBM, Compaq pre-2002, Sun Microsystems, Gateway, Apple, NCR)** for the Lesson 10 bottom-up beta | Not fetched in this pass — the prep doc identifies them as needed; same EDGAR approach applies (`https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&company=<name>&type=10-K`) whenever you're ready to build the comp set. |
| **Historical implied/historical ERP by year** | Not fetched — lives on Damodaran's site as a downloadable dataset (not a single stable URL the way FRED's CSV endpoint is), see the Module 1 prep doc's Lesson 6 row. |
