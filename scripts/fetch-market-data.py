#!/usr/bin/env python3
"""
Fetch current market rates from FRED and write to 03-corporate-finance/03-3-supplemental-data/market-rates.json.
Requires FRED_API_KEY environment variable.

Run: python3 scripts/fetch-market-data.py
"""

import json
import os
import sys
from datetime import date
from urllib.request import urlopen
from urllib.parse import urlencode
from urllib.error import URLError

FRED_BASE = "https://api.stlouisfed.org/fred/series/observations"

SERIES = {
    "us_10y_treasury": {
        "series_id": "DGS10",
        "label": "US 10-Year Treasury Constant Maturity",
        "unit": "percent",
        "note": "Risk-free rate for USD-denominated DCF",
    },
    "sofr": {
        "series_id": "SOFR",
        "label": "Secured Overnight Financing Rate",
        "unit": "percent",
        "note": "Floating-rate debt benchmark; use for term loans priced at SOFR + spread",
    },
    "fed_funds_effective": {
        "series_id": "FEDFUNDS",
        "label": "Federal Funds Effective Rate",
        "unit": "percent",
        "note": "Overnight policy rate; context for short-term borrowing costs",
    },
}

OUT_PATH = "03-corporate-finance/03-3-supplemental-data/market-rates.json"


def fetch_series(api_key: str, series_id: str) -> dict:
    params = {
        "series_id": series_id,
        "api_key": api_key,
        "file_type": "json",
        "sort_order": "desc",
        "limit": "5",
        "observation_start": "2020-01-01",
    }
    url = f"{FRED_BASE}?{urlencode(params)}"
    try:
        with urlopen(url, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        # FRED returns "." for missing values; find the most recent non-missing
        for obs in data.get("observations", []):
            raw = obs.get("value", ".")
            if raw != ".":
                return {"value": float(raw), "date": obs.get("date")}
        return {"value": None, "date": None, "error": "no non-missing observations"}
    except URLError as e:
        return {"value": None, "date": None, "error": str(e)}


def main():
    api_key = os.environ.get("FRED_API_KEY")
    if not api_key:
        print("ERROR: FRED_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    rates = {}
    for key, meta in SERIES.items():
        obs = fetch_series(api_key, meta["series_id"])
        rates[key] = {**meta, **obs}
        status = f"{obs['value']}%" if obs.get("value") is not None else f"N/A ({obs.get('error', '')})"
        print(f"  {meta['series_id']}: {status} ({obs.get('date', 'unknown')})")

    output = {
        "updated": date.today().isoformat(),
        "source": "FRED — Federal Reserve Bank of St. Louis",
        "rates": rates,
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(output, f, indent=2)
    print(f"\nWrote {OUT_PATH}")


if __name__ == "__main__":
    main()
