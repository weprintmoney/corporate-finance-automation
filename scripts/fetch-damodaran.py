#!/usr/bin/env python3
"""
Download Damodaran's industry beta and country risk premium data from NYU Stern
and write JSON files to 03-corporate-finance/data/damodaran/.

No API key required — pulls from public NYU Stern files.
Requires: pip install xlrd openpyxl

Run: python3 scripts/fetch-damodaran.py

Damodaran refreshes his data in January each year. Run this script then to pick up updates.
URLs below may need updating after each annual release — check https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html
"""

import json
import os
import sys
from datetime import date
from urllib.request import urlopen, Request
from urllib.error import URLError
from io import BytesIO

OUT_DIR = "03-corporate-finance/data/damodaran"

# Update these URLs each January from: https://pages.stern.nyu.edu/~adamodar/New_Home_Page/data.html
BETA_URL = "https://pages.stern.nyu.edu/~adamodar/pc/datasets/betas.xls"
COUNTRY_URL = "https://pages.stern.nyu.edu/~adamodar/pc/datasets/ctrypremjuly24.xlsx"


def download(url: str, label: str) -> bytes:
    print(f"  Downloading {label}...")
    req = Request(url, headers={"User-Agent": "Mozilla/5.0 (compatible; finance-automation/1.0)"})
    try:
        with urlopen(req, timeout=30) as resp:
            data = resp.read()
        print(f"    {len(data):,} bytes")
        return data
    except URLError as e:
        print(f"    ERROR: {e}", file=sys.stderr)
        return b""


def parse_xls(data: bytes) -> list[dict]:
    try:
        import xlrd
    except ImportError:
        print("  xlrd not installed. Run: pip install xlrd", file=sys.stderr)
        return []

    wb = xlrd.open_workbook(file_contents=data)
    # Damodaran's betas.xls: first sheet is the industry table
    ws = wb.sheet_by_index(0)
    # Find the header row (contains "Industry Name")
    header_row_idx = None
    for r in range(min(10, ws.nrows)):
        row_vals = [str(ws.cell_value(r, c)).strip() for c in range(ws.ncols)]
        if "Industry Name" in row_vals:
            header_row_idx = r
            break

    if header_row_idx is None:
        print("  WARNING: could not find 'Industry Name' header in betas.xls", file=sys.stderr)
        return []

    headers = [str(ws.cell_value(header_row_idx, c)).strip() for c in range(ws.ncols)]
    rows = []
    for r in range(header_row_idx + 1, ws.nrows):
        name_cell = str(ws.cell_value(r, 0)).strip()
        if not name_cell or name_cell in ("Industry Name",):
            continue
        row = {}
        for c, h in enumerate(headers):
            if h:
                val = ws.cell_value(r, c)
                row[h] = val
        rows.append(row)
    return rows


def parse_xlsx(data: bytes) -> list[dict]:
    try:
        import openpyxl
    except ImportError:
        print("  openpyxl not installed. Run: pip install openpyxl", file=sys.stderr)
        return []

    wb = openpyxl.load_workbook(BytesIO(data), data_only=True)
    ws = wb.active
    all_rows = list(ws.iter_rows(values_only=True))
    if not all_rows:
        return []

    # Find header row (contains "Country" or "Equity Risk Premium")
    header_idx = 0
    for i, row in enumerate(all_rows[:10]):
        row_strs = [str(v).strip() if v is not None else "" for v in row]
        if "Country" in row_strs or "Equity Risk Premium" in row_strs:
            header_idx = i
            break

    headers = [str(h).strip() if h is not None else "" for h in all_rows[header_idx]]
    rows = []
    for row in all_rows[header_idx + 1:]:
        if not any(v is not None for v in row):
            continue
        rows.append({h: v for h, v in zip(headers, row) if h})
    return rows


def betas_to_json(rows: list[dict]) -> dict:
    industries = {}
    skip = {"Industry Name", "Total Market", "Total Market (without financials)", ""}
    for row in rows:
        name = str(row.get("Industry Name", "")).strip()
        if name in skip:
            continue
        entry = {}
        for k, v in row.items():
            if k == "Industry Name":
                continue
            if isinstance(v, float) and v == int(v):
                entry[k] = int(v)
            elif v not in (None, ""):
                entry[k] = v
        industries[name] = entry
    return industries


def country_to_json(rows: list[dict]) -> dict:
    countries = {}
    for row in rows:
        # key column may be "Country" or first non-empty
        name = str(row.get("Country", "") or "").strip()
        if not name or name in ("Country", "Total"):
            continue
        entry = {k: v for k, v in row.items() if k != "Country" and v not in (None, "")}
        countries[name] = entry
    return countries


def main():
    print("Fetching Damodaran data...\n")

    # Industry betas
    beta_data = download(BETA_URL, "industry betas (betas.xls)")
    beta_rows = parse_xls(beta_data) if beta_data else []
    industries = betas_to_json(beta_rows)
    print(f"  Parsed {len(industries)} industries")

    betas_out = {
        "updated": date.today().isoformat(),
        "source_url": BETA_URL,
        "note": "Damodaran refreshes annually in January. Re-run this script after each update.",
        "industries": industries,
    }

    # Country risk premiums
    country_data = download(COUNTRY_URL, "country risk premiums")
    country_rows = parse_xlsx(country_data) if country_data else []
    countries = country_to_json(country_rows)
    print(f"  Parsed {len(countries)} countries")

    country_out = {
        "updated": date.today().isoformat(),
        "source_url": COUNTRY_URL,
        "note": "URL year suffix (e.g. 'july24') changes annually. Check Damodaran's site in January.",
        "countries": countries,
    }

    os.makedirs(OUT_DIR, exist_ok=True)

    betas_path = f"{OUT_DIR}/industry-betas.json"
    with open(betas_path, "w") as f:
        json.dump(betas_out, f, indent=2)
    print(f"\nWrote {betas_path}")

    country_path = f"{OUT_DIR}/country-risk.json"
    with open(country_path, "w") as f:
        json.dump(country_out, f, indent=2)
    print(f"Wrote {country_path}")


if __name__ == "__main__":
    main()
