#!/usr/bin/env python3
"""Refresh the market-data snapshots in 03-corporate-finance/03-3-supplemental-data/.

Writes four JSON files. Each carries `as_of` (the date the publisher says the data describes),
`fetched` (the run date) and `source_url`:

  market-rates.json     From Damodaran's monthly ERP workbook: 10-year Treasury, US sovereign default
                        spread, dollar risk-free rate, and the implied equity risk premium over each.
                        From FRED: the latest 10-year Treasury, SOFR and Fed Funds closes.
  ratings-spreads.json  Interest coverage -> synthetic rating -> default spread (large, small, financial)
  country-risk.json     Per-country Moody's rating, default spread, equity and country risk premium
  industry-betas.json   US industry betas, levered and unlevered, cash-corrected

Usage:
  python3 scripts/refresh-market-data.py            fetch everything, rewrite the files, then --check
  python3 scripts/refresh-market-data.py --check    fetch nothing; exit 1 if a file is missing or stale

Fetching needs `pip install xlrd openpyxl`; --check needs only the standard library. No API keys.

Every parser exits non-zero when the source layout changes, rather than writing an empty file. Damodaran
publishes the ERP workbook monthly, country risk in January and July, betas and the ratings table in
January. MAX_AGE_DAYS allows for that cadence plus some lag; a file past its window means a fetch broke
or a URL pattern changed, and /value-company refuses to use it.
"""
import calendar
import json
import os
import re
import sys
import tempfile
import urllib.request
from datetime import date, datetime, timedelta

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_DIR = os.path.join(REPO, "03-corporate-finance", "03-3-supplemental-data")

BASE = "https://pages.stern.nyu.edu/~adamodar"
RATINGS_XLS = BASE + "/pc/ratings.xls"
RATINGS_HTML = BASE + "/New_Home_Page/datafile/ratings.html"
CTRYPREM = BASE + "/pc/datasets/ctryprem.xlsx"                 # January update
CTRYPREM_JULY = BASE + "/pc/datasets/ctrypremJuly{yy}.xlsx"    # July update, separate file
BETAS = BASE + "/pc/datasets/betas.xls"
ERP_PATTERN = BASE + "/pc/implprem/ERP{month}{yy}.xlsx"
FRED_CSV = "https://fred.stlouisfed.org/graph/fredgraph.csv?id={series}&cosd={start}"
FRED_SERIES = {"treasury_10y": "DGS10", "sofr": "SOFR", "fed_funds_effective": "DFF"}

MAX_AGE_DAYS = {
    "market-rates.json": 45,
    "country-risk.json": 200,
    "ratings-spreads.json": 400,
    "industry-betas.json": 400,
}


def fetch(url, dest):
    # Python's default user agent: FRED stalls on browser-like or custom ones
    with urllib.request.urlopen(url, timeout=60) as resp, open(dest, "wb") as fh:
        fh.write(resp.read())
    return dest


def num(x):
    try:
        return float(x)
    except (TypeError, ValueError):
        return None


def fail(msg):
    sys.exit("refresh-market-data: " + msg)


def value_right_of(rows, label):
    """First numeric cell to the right of the first cell whose text starts with `label`."""
    for row in rows:
        for i, cell in enumerate(row):
            if isinstance(cell, str) and cell.strip().lower().startswith(label.lower()):
                for nxt in row[i + 1:]:
                    if num(nxt) is not None:
                        return float(nxt)
    return None


# ---- market-rates.json ------------------------------------------------------------------------

def find_erp_workbook(tmp):
    """Damodaran names the file by month, inconsistently: ERPOct26, ERPJuly26, ERPSept25."""
    today = date.today()
    for back in range(4):
        y, m = today.year, today.month - back
        if m < 1:
            y, m = y - 1, m + 12
        full = calendar.month_name[m]
        for name in dict.fromkeys([full[:3], full[:4], full]):
            url = ERP_PATTERN.format(month=name, yy=str(y)[2:])
            dest = os.path.join(tmp, "erp.xlsx")
            try:
                fetch(url, dest)
            except Exception:
                continue
            with open(dest, "rb") as fh:
                if fh.read(2) == b"PK":          # an xlsx, not an error page
                    return url, dest, date(y, m, 1)
    fail("no ERP workbook for this month or the three before it ({})".format(ERP_PATTERN))


def fred_latest(series, tmp):
    start = (date.today() - timedelta(days=21)).isoformat()
    path = fetch(FRED_CSV.format(series=series, start=start), os.path.join(tmp, series + ".csv"))
    rows = []
    for line in open(path):
        parts = line.strip().split(",")
        if len(parts) == 2 and parts[0][:1].isdigit() and num(parts[1]) is not None:
            rows.append((parts[0], float(parts[1]) / 100))
    if not rows:
        fail("FRED returned no observations for {}".format(series))
    return {"value": rows[-1][1], "date": rows[-1][0], "source_url": "https://fred.stlouisfed.org/series/" + series}


def market_rates(tmp):
    import openpyxl
    url, path, month = find_erp_workbook(tmp)
    ws = openpyxl.load_workbook(path, data_only=True, read_only=True)["Impl premium calculator"]
    rows = [list(r) for r in ws.iter_rows(values_only=True)]
    erp = {
        "treasury_10y": value_right_of(rows, "US 10-year treasury rate ="),
        "us_sovereign_default_spread": value_right_of(rows, "Default spread for"),
        "dollar_riskfree_rate": value_right_of(rows, "Default-risk-adjusted US dollar riskfree"),
        "implied_erp_over_dollar_riskfree": value_right_of(rows, "Implied Equity Risk Premium (with default"),
        "implied_erp_over_treasury": value_right_of(rows, "Implied Equity Risk Premium (with US tre"),
        "sp500_level": value_right_of(rows, "Enter current level of index"),
    }
    missing = [k for k, v in erp.items() if v is None]
    if missing:
        fail("ERP workbook layout changed; could not read {}".format(", ".join(missing)))
    if abs(erp["treasury_10y"] - erp["us_sovereign_default_spread"] - erp["dollar_riskfree_rate"]) > 0.0005:
        fail("ERP workbook is inconsistent: Treasury minus sovereign spread is not the dollar risk-free rate")
    return {
        "as_of": month.isoformat(),
        "fetched": date.today().isoformat(),
        "source_url": url,
        "note": ("damodaran_monthly values are as of the start of the month and pair with each other: "
                 "dollar_riskfree_rate with implied_erp_over_dollar_riskfree, or treasury_10y with "
                 "implied_erp_over_treasury; never mix. Pre-tax cost of debt = treasury_10y + the "
                 "company's default spread, because rating spreads are measured over Treasuries. "
                 "fred_latest is the most recent daily close, for checking how far rates moved since."),
        "damodaran_monthly": erp,
        "fred_latest": fred_all(tmp),
    }


def fred_all(tmp):
    """A cross-check only, so a FRED outage is recorded rather than fatal."""
    out = {}
    for key, series in FRED_SERIES.items():
        try:
            out[key] = fred_latest(series, tmp)
        except Exception as exc:
            print("refresh-market-data: FRED {} unavailable ({})".format(series, exc))
            out[key] = {"value": None, "error": str(exc)}
    return out


# ---- ratings-spreads.json -----------------------------------------------------------------------

RATING_CELL = re.compile(r"^[A-Za-z0-9]+/[A-Z]+[+-]?$")      # "Aaa/AAA", "B3/B-"


def ratings_spreads(tmp):
    import xlrd
    sheet = xlrd.open_workbook(fetch(RATINGS_XLS, os.path.join(tmp, "ratings.xls"))).sheet_by_index(0)
    blocks = {}                                               # (column, first row) -> rows
    open_block = {}                                           # column -> key of the block still growing
    for r in range(sheet.nrows):
        row = [c.value for c in sheet.row(r)]
        for c, cell in enumerate(row):
            if not (isinstance(cell, str) and RATING_CELL.match(cell.strip())) or c < 2 or c + 1 >= len(row):
                continue
            lo, spread = num(row[c - 2]), num(row[c + 1])
            if lo is None or spread is None:
                continue
            key = open_block.get(c)
            if key is None or blocks[key][-1]["row"] != r - 1:
                key = (c, r)
                blocks[key] = []
                open_block[c] = key
            blocks[key].append({"row": r, "min_coverage": lo, "rating": cell.strip(), "spread": spread})
    tables = {k: v for k, v in blocks.items() if len(v) == 15}
    if len(tables) != 3:
        fail("ratings.xls layout changed; expected three 15-row tables, found {}".format(len(tables)))
    # Layout: large-firm table top left, financial-firm table top right, small-firm table below.
    top_row = min(r for _, r in tables)
    top = sorted(k for k in tables if k[1] == top_row)
    below = [k for k in tables if k[1] != top_row]
    if len(top) != 2 or len(below) != 1:
        fail("ratings.xls layout changed; cannot tell the large, financial and small tables apart")

    text = open(fetch(RATINGS_HTML, os.path.join(tmp, "ratings.html")), encoding="latin-1").read()
    m = re.search(r"as of\s+([A-Za-z]+)\s+(\d{4})", text)
    if not m:
        fail("ratings page no longer states 'as of <Month> <Year>'")
    as_of = datetime.strptime("{} {}".format(m.group(1), m.group(2)), "%B %Y").date()

    def clean(key):
        return [{k: v for k, v in row.items() if k != "row"} for row in tables[key]]

    return {
        "as_of": as_of.isoformat(),
        "fetched": date.today().isoformat(),
        "source_url": RATINGS_XLS,
        "note": ("Rows in ascending coverage; a firm gets the last row whose min_coverage its coverage "
                 "exceeds. large = market cap above about $5B. Spreads are over the 10-year Treasury, so "
                 "pre-tax cost of debt = Treasury rate + spread."),
        "large": clean(top[0]),
        "small": clean(below[0]),
        "financial": clean(top[1]),
    }


# ---- country-risk.json ---------------------------------------------------------------------------

def country_risk(tmp):
    """Damodaran posts the January update at ctryprem.xlsx and the July one at ctrypremJulyYY.xlsx; keep the newer."""
    year = date.today().year
    found = []
    for url in [CTRYPREM, CTRYPREM_JULY.format(yy=str(year)[2:]), CTRYPREM_JULY.format(yy=str(year - 1)[2:])]:
        try:
            found.append(parse_country_risk(url, tmp))
        except SystemExit as exc:
            print("refresh-market-data: skipped {} ({})".format(url, exc))
        except Exception as exc:
            print("refresh-market-data: could not fetch {} ({})".format(url, exc))
    if not found:
        fail("no country risk workbook could be read")
    return max(found, key=lambda d: d["as_of"])


def parse_country_risk(url, tmp):
    import openpyxl
    path = fetch(url, os.path.join(tmp, "ctryprem.xlsx"))
    ws = openpyxl.load_workbook(path, data_only=True, read_only=True)["ERPs by country"]
    rows = [list(r) for r in ws.iter_rows(values_only=True)]
    stamp = next((r[1] for r in rows[:5] if r and isinstance(r[0], str) and r[0].lower().startswith("date of update")), None)
    if not isinstance(stamp, datetime):
        fail("ctryprem.xlsx no longer states its update date on 'ERPs by country'")
    header = next((i for i, r in enumerate(rows) if r and r[0] == "Country"), None)
    if header is None:
        fail("ctryprem.xlsx has no 'Country' header row on 'ERPs by country'")
    countries = {}
    for row in rows[header + 1:]:
        if not row or not row[0]:
            break
        if num(row[4]) is not None:
            countries[str(row[0]).strip()] = {
                "region": row[1], "moodys_rating": row[2], "default_spread": num(row[3]),
                "erp": num(row[4]), "country_risk_premium": num(row[5]),
            }
    if len(countries) < 100:
        fail("ctryprem.xlsx parsed only {} countries".format(len(countries)))
    return {
        "as_of": stamp.date().isoformat(),
        "fetched": date.today().isoformat(),
        "source_url": url,
        "note": "Rating-based default spreads and premiums. Damodaran updates in January and July.",
        "mature_market_erp": value_right_of(rows[:6], "Enter the current risk premium for a mature"),
        "us_erp": value_right_of(rows[:6], "Enter the current risk premium for the US"),
        "countries": countries,
    }


# ---- industry-betas.json -------------------------------------------------------------------------

def industry_betas(tmp):
    import xlrd
    book = xlrd.open_workbook(fetch(BETAS, os.path.join(tmp, "betas.xls")))
    sheet = book.sheet_by_name("Industry Averages")
    rows = [[c.value for c in sheet.row(r)] for r in range(sheet.nrows)]
    if not (rows and str(rows[0][0]).lower().startswith("date updated") and num(rows[0][1])):
        fail("betas.xls no longer states 'Date updated' in its first row")
    as_of = xlrd.xldate.xldate_as_datetime(num(rows[0][1]), book.datemode).date()
    header = next((i for i, r in enumerate(rows) if r and r[0] == "Industry Name"), None)
    if header is None:
        fail("betas.xls has no 'Industry Name' header row")
    industries = {}
    for row in rows[header + 1:]:
        if not row[0] or num(row[1]) is None:
            break
        industries[str(row[0]).strip()] = {
            "firms": int(num(row[1])), "beta": num(row[2]), "de_ratio": num(row[3]),
            "effective_tax_rate": num(row[4]), "unlevered_beta": num(row[5]),
            "cash_to_firm_value": num(row[6]), "unlevered_beta_cash_corrected": num(row[7]),
        }
    if len(industries) < 50:
        fail("betas.xls parsed only {} industries".format(len(industries)))
    return {
        "as_of": as_of.isoformat(),
        "fetched": date.today().isoformat(),
        "source_url": BETAS,
        "note": "US companies. Damodaran refreshes in January.",
        "industries": industries,
    }


# ---- staleness check -----------------------------------------------------------------------------

def check(today=None):
    today = today or date.today()
    bad = []
    for name, limit in MAX_AGE_DAYS.items():
        try:
            with open(os.path.join(OUT_DIR, name)) as fh:
                as_of = datetime.strptime(json.load(fh)["as_of"], "%Y-%m-%d").date()
        except Exception:
            print("{:<22} missing or has no as_of".format(name))
            bad.append(name)
            continue
        age = (today - as_of).days
        print("{:<22} as_of {}  {:>4} days old  (limit {})  {}".format(name, as_of, age, limit, "ok" if age <= limit else "STALE"))
        if age > limit:
            bad.append(name)
    if bad:
        print("Stale or missing: {}. Run python3 scripts/refresh-market-data.py.".format(", ".join(bad)))
        return 1
    return 0


def main(argv):
    if "--check" in argv:
        sys.exit(check())
    with tempfile.TemporaryDirectory() as tmp:
        outputs = {
            "market-rates.json": market_rates(tmp),
            "ratings-spreads.json": ratings_spreads(tmp),
            "country-risk.json": country_risk(tmp),
            "industry-betas.json": industry_betas(tmp),
        }
    for name, payload in outputs.items():           # write only after every source parsed
        with open(os.path.join(OUT_DIR, name), "w") as fh:
            json.dump(payload, fh, indent=2)
            fh.write("\n")
        print("wrote {} (as_of {})".format(name, payload["as_of"]))
    sys.exit(check())


if __name__ == "__main__":
    main(sys.argv[1:])
