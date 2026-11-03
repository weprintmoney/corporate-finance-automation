#!/usr/bin/env python3
"""Fetch a company's SEC filings up to a cutoff date, for a /value-company run.

Nothing filed after --cutoff is downloaded or listed, so a blind run (meta.blind: true) can't see
what happened next. Each downloaded file is recorded in <company>/sources/published.yaml with its
EDGAR filing date, which validate-ledger.py checks against the analysis date.

Downloads, all with a filing date on or before the cutoff:
  - the two latest 10-Ks (or 20-F/40-F)
  - every 10-Q filed after the latest 10-K
  - the latest DEF 14A (proxy)
  - 8-Ks from the year before the cutoff that report a material event (items 1.01, 1.02, 2.01, 2.03,
    2.05, 2.06, 3.03, 5.01, 5.02, 5.03, 8.01), newest first, at most --max-8k
  - the four latest earnings 8-Ks (item 2.02), which carry guidance
  For every 8-K, its EX-99 exhibits (press releases, earnings releases) are appended to the text.
Writes sources/filings/index.md: every filing in the three years before the cutoff by form and
month, including insider (Form 4) counts and 8-K items, so the read can see patterns in what the
company files without reading each one.

Usage:
  python3 fetch-filings.py <TICKER> <company-folder> --cutoff YYYY-MM-DD [--cik N] [--max-8k 25]
SEC asks automated clients to identify themselves: set SEC_UA="name contact" in the environment.
"""
import argparse
import html
import json
import os
import re
import sys
import time
import urllib.request
from collections import Counter, defaultdict
from datetime import date, datetime, timedelta
from html.parser import HTMLParser

import yaml

SEC_UA = os.environ.get("SEC_UA", "corporate-finance-automation research@example.com")
MATERIAL_8K = {"1.01", "1.02", "2.01", "2.03", "2.05", "2.06", "3.03", "5.01", "5.02", "5.03", "7.01", "8.01"}
EIGHT_K = {"8-K", "8-K/A"}
ANNUAL = {"10-K", "20-F", "40-F"}


def get(url, as_json=False):
    time.sleep(0.15)  # SEC's limit is 10 requests a second
    req = urllib.request.Request(url, headers={"User-Agent": SEC_UA, "Accept-Encoding": "identity"})
    with urllib.request.urlopen(req, timeout=60) as r:
        data = r.read()
    return json.loads(data) if as_json else data.decode("utf-8", errors="replace")


def cik_for(ticker):
    for v in get("https://www.sec.gov/files/company_tickers.json", as_json=True).values():
        if v["ticker"].upper() == ticker.upper():
            return int(v["cik_str"])
    sys.exit(f"{ticker}: not in SEC's ticker list; pass --cik")


def filings(cik, cutoff, since):
    """Every filing between since and cutoff, from the recent block and the older pages."""
    sub = get(f"https://data.sec.gov/submissions/CIK{cik:010d}.json", as_json=True)
    blocks = [sub["filings"]["recent"]]
    for f in sub["filings"].get("files", []):
        if datetime.strptime(f["filingTo"], "%Y-%m-%d").date() >= since:
            blocks.append(get("https://data.sec.gov/submissions/" + f["name"], as_json=True))
    out = []
    for b in blocks:
        for i in range(len(b["accessionNumber"])):
            d = datetime.strptime(b["filingDate"][i], "%Y-%m-%d").date()
            if since <= d <= cutoff:
                out.append({"form": b["form"][i], "date": d, "accn": b["accessionNumber"][i],
                            "doc": b["primaryDocument"][i], "items": b.get("items", [""] * len(b["form"]))[i] or "",
                            "period": b.get("reportDate", [""] * len(b["form"]))[i] or ""})
    return sub.get("name", ""), sorted(out, key=lambda f: f["date"], reverse=True)


class Text(HTMLParser):
    """HTML to readable markdown-ish text: paragraphs, and tables as pipe rows."""
    SKIP = {"script", "style", "head", "ix:header"}

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.out, self.row, self.cell, self.skip, self.in_cell = [], [], [], 0, False

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        elif tag == "tr":
            self.row = []
        elif tag in ("td", "th"):
            self.cell, self.in_cell = [], True
        elif tag in ("p", "div", "br", "li") and not self.in_cell:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self.skip -= 1
        elif tag in ("td", "th"):
            t = " ".join("".join(self.cell).split())
            if t:
                self.row.append(t)
            self.in_cell = False
        elif tag == "tr":
            if self.row:
                self.out.append("\n| " + " | ".join(self.row) + " |")
            self.row = []
        elif tag in ("p", "div", "table") and not self.in_cell:
            self.out.append("\n")

    def handle_data(self, data):
        if self.skip:
            return
        (self.cell if self.in_cell else self.out).append(data)

    def text(self):
        t = "".join(self.out).replace("\xa0", " ")
        t = re.sub(r"[ \t]+", " ", t)
        t = re.sub(r"\n\s*\n\s*(\n\s*)+", "\n\n", t)
        return t.strip() + "\n"


def to_text(raw, doc):
    if doc.lower().endswith((".htm", ".html", ".xml")):
        p = Text()
        p.feed(raw)
        return p.text()
    return html.unescape(raw)


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("ticker")
    ap.add_argument("company_dir")
    ap.add_argument("--cutoff", required=True)
    ap.add_argument("--cik", type=int)
    ap.add_argument("--max-8k", type=int, default=25)
    a = ap.parse_args(argv)
    cutoff = datetime.strptime(a.cutoff, "%Y-%m-%d").date()
    since = cutoff - timedelta(days=3 * 366)
    cik = a.cik or cik_for(a.ticker)
    name, fl = filings(cik, cutoff, since)
    t = a.ticker.lower()

    annual = [f for f in fl if f["form"] in ANNUAL][:2]
    pick = list(annual)
    if annual:
        pick += [f for f in fl if f["form"] == "10-Q" and f["date"] > annual[0]["date"]]
    pick += [f for f in fl if f["form"] == "DEF 14A"][:1]
    year_ago = cutoff - timedelta(days=366)
    eights = [f for f in fl if f["form"] in EIGHT_K and f["date"] >= year_ago
              and MATERIAL_8K & {i.strip() for i in f["items"].split(",")}]
    pick += eights[:a.max_8k]
    earnings = [f for f in fl if f["form"] in EIGHT_K and "2.02" in f["items"] and f not in eights[:a.max_8k]]
    pick += earnings[:4]

    out_dir = os.path.join(a.company_dir, "sources", "filings")
    os.makedirs(out_dir, exist_ok=True)
    pub_path = os.path.join(a.company_dir, "sources", "published.yaml")
    published = []
    if os.path.exists(pub_path):
        published = yaml.safe_load(open(pub_path)) or []
    have = {r["file"] for r in published}
    form_slug = lambda f: f["form"].lower().replace(" ", "").replace("/", "-")
    for f in pick:
        fname = f"{t}-{form_slug(f)}-{f['date'].isoformat()}"
        if f["form"] in EIGHT_K:
            fname += "-items-" + f["items"].replace(".", "").replace(",", "-")
        fname += ".md"
        rel = f"sources/filings/{fname}"
        url = f"https://www.sec.gov/Archives/edgar/data/{cik}/{f['accn'].replace('-', '')}/{f['doc']}"
        try:
            body = to_text(get(url), f["doc"])
            if f["form"] in EIGHT_K:
                folder = f"https://www.sec.gov/Archives/edgar/data/{cik}/{f['accn'].replace('-', '')}/"
                for item in get(folder + "index.json", as_json=True)["directory"]["item"]:
                    n = item["name"]
                    # Exhibit names follow no pattern ("ex99-1.htm", "hd_exhibit991x….htm",
                    # "a1q_2026xearningsxnewsxr.htm"), so keep every HTML document in the filing except
                    # the 8-K itself, EDGAR's index pages and its rendered XBRL pages (R1.htm …).
                    if (n.lower().endswith((".htm", ".html")) and n != f["doc"] and "index" not in n.lower()
                            and not re.fullmatch(r"R\d+\.htm", n)):
                        body += f"\n\n---\n\n## Exhibit {n}\n\n" + to_text(get(folder + n), n)
        except Exception as e:  # noqa: BLE001 - report and continue; a missing exhibit shouldn't stop the run
            print(f"FAILED {f['form']} {f['date']}: {e}", file=sys.stderr)
            continue
        header = (f"<!-- {name} (CIK {cik}) {f['form']} filed {f['date']}"
                  f"{', period ' + f['period'] if f['period'] else ''}{', items ' + f['items'] if f['items'] else ''}. "
                  f"Source: {url} -->\n\n")
        with open(os.path.join(a.company_dir, rel), "w") as fh:
            fh.write(header + body)
        if rel not in have:
            published.append({"file": rel, "published": f["date"].isoformat(), "form": f["form"], "url": url})
            have.add(rel)
        print(f"{rel}  ({len(body) // 1000}K chars)")

    # index of everything filed in the window, by form and month
    by_month = defaultdict(Counter)
    for f in fl:
        by_month[f["date"].strftime("%Y-%m")][f["form"]] += 1
    lines = [f"# {name} — SEC filings {since} to {cutoff}", "",
             f"Every filing EDGAR lists for CIK {cik} in the three years to the cutoff. Nothing after {cutoff} is listed.", "",
             "## By month", "", "| Month | Filings by form |", "|---|---|"]
    for m in sorted(by_month, reverse=True):
        lines.append(f"| {m} | " + ", ".join(f"{k} ×{v}" for k, v in by_month[m].most_common()) + " |")
    lines += ["", "## 8-Ks", "", "| Filed | Items |", "|---|---|"]
    lines += [f"| {f['date']} | {f['items']} |" for f in fl if f["form"] in EIGHT_K]
    index_rel = "sources/filings/index.md"
    with open(os.path.join(a.company_dir, index_rel), "w") as fh:
        fh.write("\n".join(lines) + "\n")
    if index_rel not in have:
        published.append({"file": index_rel, "published": cutoff.isoformat(), "form": "index"})
    with open(pub_path, "w") as fh:
        yaml.safe_dump(published, fh, sort_keys=False)
    print(f"wrote {index_rel} and {pub_path} ({len(published)} files)")


if __name__ == "__main__":
    main(sys.argv[1:])
