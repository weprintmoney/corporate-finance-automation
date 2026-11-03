#!/usr/bin/env python3
"""Pull peer fundamentals from SEC XBRL company facts and a closing price on the analysis date.

Usage:
  python3 fetch-peer-facts.py --date YYYY-MM-DD TICKER [TICKER ...] > sources/peer-filings/peer-facts-<date>.md

For each ticker:
  - Income-statement figures and the balance sheet from the peer's latest fiscal year that ended on
    or before --date (the year that lines up with the company's base year).
  - Shares outstanding from the latest filing made on or before --date (cover page; dual-class
    companies, whose covers are not in company facts, from the balance-sheet share count).
  - The closing price on --date, or the last close before it.

Writes a markdown table in $ millions, one row per peer, plus the XBRL tag behind each figure. Copy the
rows into inputs.yaml `peers`, citing the saved file.

Debt = borrowings (term loans, notes, convertibles) + operating lease liabilities, the same definition
the ledger uses for the company. Cash = cash and equivalents + short-term investments.
Market cap = shares x close. Enterprise value = market cap + debt - cash.

Standard library only. SEC rejects some user agents; the default works, or set SEC_UA="org email".
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request
from datetime import date, datetime, timedelta

SEC_UA = os.environ.get("SEC_UA", "corporate-finance-automation research@example.com")
TICKERS_URL = "https://www.sec.gov/files/company_tickers.json"
FACTS_URL = "https://data.sec.gov/api/xbrl/companyfacts/CIK{cik:010d}.json"
CHART_URL = "https://query1.finance.yahoo.com/v8/finance/chart/{t}?period1={a}&period2={b}&interval=1d&events=split"

# First tag present for the fiscal year wins; a list of tags is summed.
TAGS = {
    "revenue": ["RevenueFromContractWithCustomerExcludingAssessedTax", "RevenueFromContractWithCustomerIncludingAssessedTax", "Revenues"],
    "operating_income": ["OperatingIncomeLoss"],
    "da": ["DepreciationDepletionAndAmortization", "DepreciationAmortizationAndAccretionNet", "DepreciationAndAmortization",
           ["Depreciation", "AmortizationOfIntangibleAssets"]],
    "net_income": ["NetIncomeLoss"],
    "dividends": ["PaymentsOfDividendsCommonStock", "PaymentsOfDividends"],
    "equity_book": ["StockholdersEquity"],
    "borrowings": ["LongTermDebt", ["LongTermDebtNoncurrent", "LongTermDebtCurrent"],
                   ["ConvertibleLongTermNotesPayable", "ConvertibleNotesPayableCurrent"], "ConvertibleLongTermNotesPayable",
                   "ConvertibleNotesPayable", ["ConvertibleDebtNoncurrent", "ConvertibleDebtCurrent"],
                   ["LongTermDebtAndCapitalLeaseObligations", "LongTermDebtAndCapitalLeaseObligationsCurrent"],
                   "LongTermDebtAndCapitalLeaseObligations", "LongTermDebtNoncurrent"],
    "lease_debt": ["OperatingLeaseLiability", ["OperatingLeaseLiabilityNoncurrent", "OperatingLeaseLiabilityCurrent"]],
    "cash": ["CashAndCashEquivalentsAtCarryingValue"],
    "short_term_investments": ["ShortTermInvestments", "MarketableSecuritiesCurrent", "AvailableForSaleSecuritiesDebtSecuritiesCurrent"],
}
FLOW = {"revenue", "operating_income", "da", "net_income", "dividends"}
# Absent means zero only for these; anything else missing prints n/a so it gets checked by hand.
# Borrowings are not here: an untagged debt line once printed as zero debt for a company with $40B of it.
ZERO_IF_ABSENT = {"dividends", "short_term_investments"}


def get(url, ua=SEC_UA, tries=3):
    for i in range(tries):                                      # Yahoo returns transient 502s
        try:
            return _get(url, ua)
        except urllib.error.HTTPError as e:
            if e.code < 500 or i == tries - 1:
                raise
            time.sleep(2 * (i + 1))


def _get(url, ua):
    req = urllib.request.Request(url, headers={"User-Agent": ua})
    with urllib.request.urlopen(req, timeout=60) as resp:
        return json.loads(resp.read())


def as_date(s):
    return datetime.strptime(s, "%Y-%m-%d").date()


def fiscal_year_end(facts, cutoff, filed_by=None):
    """End date of the latest full fiscal year that ended on or before cutoff, in a 10-K filed by filed_by."""
    filed_by = filed_by or cutoff
    ends = []
    for tag in TAGS["revenue"]:
        for u in facts.get("us-gaap", {}).get(tag, {}).get("units", {}).get("USD", []):
            if u.get("form") == "10-K" and "start" in u and 350 <= (as_date(u["end"]) - as_date(u["start"])).days <= 380:
                if as_date(u["end"]) <= cutoff and as_date(u["filed"]) <= filed_by:
                    ends.append(as_date(u["end"]))
    return max(ends) if ends else None


def value_at(facts, tag, fy_end, flow, filed_by=None):
    """The fiscal-year value (flow) or year-end balance (stock), from the earliest 10-K reporting it,
    ignoring filings after filed_by (the analysis date), so a backtest never sees a later filing."""
    rows = []
    for u in facts.get("us-gaap", {}).get(tag, {}).get("units", {}).get("USD", []):
        if u.get("form") != "10-K" or as_date(u["end"]) != fy_end:
            continue
        if filed_by and as_date(u["filed"]) > filed_by:
            continue
        if flow and ("start" not in u or not 350 <= (fy_end - as_date(u["start"])).days <= 380):
            continue
        rows.append((u["filed"], u["val"], u["accn"]))
    return sorted(rows)[0] if rows else None


def pick(facts, spec, fy_end, flow, filed_by=None):
    for cand in spec:
        tags = cand if isinstance(cand, list) else [cand]
        parts = [value_at(facts, t, fy_end, flow, filed_by) for t in tags]
        if all(parts):
            return sum(p[1] for p in parts), "+".join(tags), parts[0][2]
    return None, None, None


def shares_before(facts, cutoff):
    """Latest share count filed on or before cutoff and no more than six months old: cover page first,
    then the balance-sheet count, then weighted-average basic shares (dual-class covers are untagged)."""
    for ns, tag in [("dei", "EntityCommonStockSharesOutstanding"), ("us-gaap", "CommonStockSharesOutstanding"),
                    ("us-gaap", "WeightedAverageNumberOfSharesOutstandingBasic")]:
        units = facts.get(ns, {}).get(tag, {}).get("units", {}).get("shares", [])
        filed = [u for u in units if as_date(u["filed"]) <= cutoff and (cutoff - as_date(u["end"])).days <= 183]
        if filed:
            last = max(u["filed"] for u in filed)
            latest = [u for u in filed if u["filed"] == last]
            end = max(u["end"] for u in latest)
            vals = [u for u in latest if u["end"] == end]
            if tag.startswith("WeightedAverage"):                   # quarter and year-to-date rows share an end date
                vals = vals[:1]
            return sum(u["val"] for u in vals), "{} ({} as of {}, filed {})".format(tag, latest[0]["form"], end, last)
    return None, "not tagged"


def close_on(ticker, day):
    """The close actually traded on `day` (or the last trading day before it).

    Yahoo restates every close for later stock splits, which corrupts market value and would reveal a
    split that happened after the analysis date. So the request runs to today, the splits after `day`
    are multiplied back in, and only the restored close is returned; the splits themselves are never
    printed, so a blind run doesn't see them."""
    a = int(datetime.combine(day - timedelta(days=7), datetime.min.time()).timestamp())
    b = int(datetime.combine(date.today() + timedelta(days=1), datetime.min.time()).timestamp())
    res = get(CHART_URL.format(t=ticker, a=a, b=b), ua="Mozilla/5.0")["chart"]["result"][0]
    pairs = [(date.fromtimestamp(t), c) for t, c in zip(res["timestamp"], res["indicators"]["quote"][0]["close"]) if c]
    cday, px = [p for p in pairs if p[0] <= day][-1]
    for sp in (res.get("events") or {}).get("splits", {}).values():
        if date.fromtimestamp(sp["date"]) > day and sp.get("denominator"):
            px *= sp["numerator"] / sp["denominator"]
    return cday, px


def main(argv):
    try:
        day = as_date(argv[argv.index("--date") + 1])
    except (ValueError, IndexError):
        sys.exit(__doc__)
    # TICKER or TICKER:CIK. Blind runs pass the CIK: SEC's ticker list is today's, so looking a ticker up
    # there reveals whether it still trades.
    args = [a for a in argv if not a.startswith("--") and a.split(":")[0].isupper()]
    given = {a.split(":")[0]: int(a.split(":")[1]) for a in args if ":" in a}
    tickers = [a.split(":")[0] for a in args]
    ciks = dict(given)
    if len(given) < len(tickers):
        ciks.update({v["ticker"]: v["cik_str"] for v in get(TICKERS_URL).values() if v["ticker"] not in given})
    m = lambda x: "{:,.1f}".format(x / 1e6) if x is not None else "n/a"
    print("| Ticker | Company | Fiscal year end | 10-K accession | Revenue | Operating income | D&A | EBITDA | Net income | "
          "Dividends | Book equity | Borrowings | Lease debt | Cash + ST investments | Shares (M) | Close | Close date | "
          "Market cap | Enterprise value | Prior-year revenue | Revenue growth |")
    print("|" + "---|" * 21)
    notes = []
    for t in tickers:
        try:
            row, note = peer_row(t, ciks, day, m)
            print(row)
            notes.append(note)
        except Exception as e:  # noqa: BLE001 - one peer's gap must not stop the others
            print("| {} | skipped: {} |".format(t, str(e)[:120] or type(e).__name__) + " |" * 19)
            notes.append("- {}: skipped ({}); check this peer by hand".format(t, e))
        time.sleep(0.2)                                             # SEC fair-access limit is 10 requests/second
    print()
    print("XBRL tags used:")
    print()
    print("\n".join(notes))


def peer_row(t, ciks, day, m):
    if t not in ciks:
        raise ValueError("no CIK; pass {}:<CIK>".format(t))
    if True:
        doc = get(FACTS_URL.format(cik=ciks[t]))
        facts = doc["facts"]
        fy_end = fiscal_year_end(facts, day)
        if fy_end is None:
            raise ValueError("no 10-K fiscal year filed by {} (a 20-F/40-F filer, or no revenue tag)".format(day))
        got = {k: pick(facts, spec, fy_end, k in FLOW, day) for k, spec in TAGS.items()}
        # Some filers tag only depreciation as DepreciationDepletionAndAmortization; add acquired-intangible
        # amortization when it is larger than the tagged D&A, and say so.
        amort = value_at(facts, "AmortizationOfIntangibleAssets", fy_end, True, day)
        if amort and got["da"][0] is not None and "AmortizationOfIntangibleAssets" not in got["da"][1] and amort[1] > got["da"][0]:
            got["da"] = (got["da"][0] + amort[1], got["da"][1] + "+AmortizationOfIntangibleAssets (tagged D&A was smaller than intangible amortization alone)", got["da"][2])
        prior_end = fiscal_year_end(facts, fy_end - timedelta(days=300), day)
        prior = pick(facts, TAGS["revenue"], prior_end, True, day)[0] if prior_end else None
        v = {k: (g[0] if g[0] is not None or k not in ZERO_IF_ABSENT else 0) for k, g in got.items()}
        sh, sh_note = shares_before(facts, day)
        cday, px = close_on(t, day)
        debt = v["borrowings"] + (v["lease_debt"] or 0) if v["borrowings"] is not None else None
        cash = v["cash"] + v["short_term_investments"] if v["cash"] is not None else None
        mcap = sh * px if sh else None
        ev = mcap + debt - cash if mcap and debt is not None and cash is not None else None
        ebitda = v["operating_income"] + v["da"] if None not in (v["operating_income"], v["da"]) else None
        growth = "{:.1%}".format(v["revenue"] / prior - 1) if prior and v["revenue"] else "n/a"
        row = ("| {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {} | {:.2f} | {} | {} | {} | {} | {} |".format(
            t, doc.get("entityName"), fy_end, got["revenue"][2], m(v["revenue"]), m(v["operating_income"]), m(v["da"]), m(ebitda),
            m(v["net_income"]), m(v["dividends"]), m(v["equity_book"]), m(v["borrowings"]), m(v["lease_debt"]),
            m(cash), "{:,.1f}".format(sh / 1e6) if sh else "n/a", px, cday, m(mcap), m(ev), m(prior), growth))
        note = "- {}: shares = {}; ".format(t, sh_note) + "; ".join("{} = {}".format(k, g[1] or "not tagged") for k, g in got.items())
        return row, note


if __name__ == "__main__":
    main(sys.argv[1:])
