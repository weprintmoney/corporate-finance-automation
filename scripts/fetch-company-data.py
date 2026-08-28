#!/usr/bin/env python3
"""
Fetch company financial statements from Financial Modeling Prep and write to
03-corporate-finance/data/companies/{ticker}.json.

Usage:  python3 scripts/fetch-company-data.py TICKER
        python3 scripts/fetch-company-data.py SWI

Requires FMP_API_KEY environment variable.
Free-tier FMP supports annual statements; premium adds quarterly.
"""

import json
import os
import sys
from datetime import date
from urllib.request import urlopen
from urllib.error import URLError

FMP_BASE = "https://financialmodelingprep.com/api/v3"
YEARS = 3
OUT_DIR = "03-corporate-finance/data/companies"


def fmp_get(path: str, api_key: str, extra: str = "") -> list | dict:
    url = f"{FMP_BASE}{path}?apikey={api_key}&limit={YEARS}{extra}"
    try:
        with urlopen(url, timeout=20) as resp:
            return json.loads(resp.read().decode())
    except URLError as e:
        print(f"  WARNING: request failed for {path}: {e}", file=sys.stderr)
        return []


def extract_valuation_inputs(income: list, balance: list, cashflow: list) -> dict:
    """Pull the specific line items needed for the evaluate-company steps."""
    if not income:
        return {}
    i = income[0]
    b = balance[0] if balance else {}
    c = cashflow[0] if cashflow else {}

    ebit = i.get("operatingIncome") or 0
    interest_raw = i.get("interestExpense") or 0
    interest = abs(interest_raw)
    icr = round(ebit / interest, 2) if interest else None

    total_debt = b.get("totalDebt") or 0
    cash = b.get("cashAndCashEquivalents") or 0

    return {
        "period": i.get("date"),
        "revenue": i.get("revenue"),
        "gross_profit": i.get("grossProfit"),
        "gross_margin_pct": round((i.get("grossProfitRatio") or 0) * 100, 1),
        "ebit": ebit,
        "ebitda": i.get("ebitda"),
        "interest_expense": interest,
        "interest_coverage_ratio": icr,
        "net_income": i.get("netIncome"),
        "income_tax_expense": i.get("incomeTaxExpense"),
        "effective_tax_rate_pct": round((i.get("incomeTaxExpense") or 0) / i.get("incomeBeforeTax", 1) * 100, 1) if i.get("incomeBeforeTax") else None,
        "total_debt": total_debt,
        "cash": cash,
        "net_debt": total_debt - cash,
        "shares_outstanding": b.get("commonStock"),
        "capex": abs(c.get("capitalExpenditure") or 0),
        "depreciation_amortization": c.get("depreciationAndAmortization"),
        "operating_cash_flow": c.get("operatingCashFlow"),
        "operating_lease_liability": b.get("operatingLeaseRightOfUseAsset"),
    }


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 scripts/fetch-company-data.py TICKER", file=sys.stderr)
        sys.exit(1)

    ticker = sys.argv[1].upper()
    api_key = os.environ.get("FMP_API_KEY")
    if not api_key:
        print("ERROR: FMP_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    print(f"Fetching data for {ticker} from Financial Modeling Prep...")

    profile_raw = fmp_get(f"/profile/{ticker}", api_key)
    income = fmp_get(f"/income-statement/{ticker}", api_key, "&period=annual")
    balance = fmp_get(f"/balance-sheet-statement/{ticker}", api_key, "&period=annual")
    cashflow = fmp_get(f"/cash-flow-statement/{ticker}", api_key, "&period=annual")
    key_metrics = fmp_get(f"/key-metrics/{ticker}", api_key, "&period=annual")

    profile = profile_raw[0] if isinstance(profile_raw, list) and profile_raw else profile_raw

    if not income and not profile:
        print(f"ERROR: No data returned for {ticker}. Check the ticker and your API key.", file=sys.stderr)
        sys.exit(1)

    valuation_inputs = extract_valuation_inputs(income, balance, cashflow)

    output = {
        "ticker": ticker,
        "updated": date.today().isoformat(),
        "source": "Financial Modeling Prep (SEC EDGAR-sourced)",
        "profile": profile,
        "income_statement": income,
        "balance_sheet": balance,
        "cash_flow_statement": cashflow,
        "key_metrics": key_metrics,
        "valuation_inputs": valuation_inputs,
    }

    os.makedirs(OUT_DIR, exist_ok=True)
    out_path = f"{OUT_DIR}/{ticker.lower()}.json"
    with open(out_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"\n--- Valuation inputs ({valuation_inputs.get('period', 'N/A')}) ---")
    for k, v in valuation_inputs.items():
        if k == "period":
            continue
        if isinstance(v, (int, float)) and v and abs(v) > 1000:
            print(f"  {k}: ${v:,.0f}")
        else:
            print(f"  {k}: {v}")
    print(f"\nWrote {out_path}")


if __name__ == "__main__":
    main()
