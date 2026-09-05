#!/usr/bin/env python3
"""
Convert crawled Damodaran XLS/XLSX workbooks (scripts/crawl-manifest.json,
type=xls, status=downloaded) into markdown + CSV under
03-corporate-finance/03-5-damodaran-online/{03-5-1-datasets,03-5-4-tools}/.

Per workbook, produces {slug}/{slug}.md (header + per-sheet tables — inline
if <=200 rows, else a 20-row preview pointing at the CSV),
{slug}/{slug}-{sheet}.csv for large sheets, and copies the original
.xls/.xlsx alongside.

Destination folder: datasets vs. tools is decided by URL path, same
convention as convert-damodaran-html.py (/pc/datasets/ -> datasets,
/New_Home_Page/spreadsheets/ -> tools; otherwise defaults to tools and
logs to scripts/unclassified.json for manual review).

Uses xlrd (legacy .xls) + openpyxl (.xlsx), same pair as
scripts/fetch-damodaran.py.

Requires: pip install xlrd openpyxl

Run: python3 scripts/convert-damodaran-xls.py [--force]
"""

import argparse
import json
import os
import re
import shutil
import sys
from datetime import date
from io import BytesIO
from urllib.parse import urlparse

MANIFEST_PATH = "scripts/crawl-manifest.json"
PROGRESS_PATH = "scripts/convert-progress.json"
UNCLASSIFIED_PATH = "scripts/unclassified.json"
OUT_ROOT = "03-corporate-finance/03-5-damodaran-online"
OWNER = "weprintmoney"
LARGE_SHEET_ROWS = 200
PREVIEW_ROWS = 20


def slugify(text):
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "workbook"


def classify_destination(url):
    path = urlparse(url).path.lower()
    if "/pc/datasets/" in path:
        return f"{OUT_ROOT}/03-5-1-datasets", "datasets"
    if "/new_home_page/spreadsheets/" in path:
        return f"{OUT_ROOT}/03-5-4-tools", "tools"
    return f"{OUT_ROOT}/03-5-4-tools", "tools-default"


def read_workbook_sheets(data, ext):
    """Return list of (sheet_name, headers, rows[list of dict]) tuples."""
    sheets = []
    if ext == ".xls":
        import xlrd
        wb = xlrd.open_workbook(file_contents=data)
        for ws in wb.sheets():
            if ws.nrows == 0:
                continue
            header_row_idx = 0
            headers = [str(ws.cell_value(header_row_idx, c)).strip() for c in range(ws.ncols)]
            rows = []
            for r in range(header_row_idx + 1, ws.nrows):
                row = {}
                for c, h in enumerate(headers):
                    if h:
                        row[h] = ws.cell_value(r, c)
                rows.append(row)
            sheets.append((ws.name, headers, rows))
    else:
        import openpyxl
        wb = openpyxl.load_workbook(BytesIO(data), data_only=True)
        for ws in wb.worksheets:
            all_rows = list(ws.iter_rows(values_only=True))
            if not all_rows:
                continue
            headers = [str(h).strip() if h is not None else "" for h in all_rows[0]]
            rows = []
            for row in all_rows[1:]:
                if not any(v is not None for v in row):
                    continue
                rows.append({h: v for h, v in zip(headers, row) if h})
            sheets.append((ws.title, headers, rows))
    return sheets


def cell_str(v):
    if v is None:
        return ""
    if isinstance(v, float) and v == int(v):
        return str(int(v))
    return str(v)


def rows_to_markdown_table(headers, rows):
    headers = [h for h in headers if h]
    lines = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    for row in rows:
        lines.append("| " + " | ".join(cell_str(row.get(h)) for h in headers) + " |")
    return "\n".join(lines)


def rows_to_csv(headers, rows):
    import csv
    import io
    headers = [h for h in headers if h]
    buf = io.StringIO()
    writer = csv.writer(buf)
    writer.writerow(headers)
    for row in rows:
        writer.writerow([cell_str(row.get(h)) for h in headers])
    return buf.getvalue()


def frontmatter(title, source_url, today):
    return (
        "---\n"
        f"title: {json.dumps(title)}\n"
        "status: active\n"
        f"owner: {OWNER}\n"
        f"created: {today}\n"
        f"last_updated: {today}\n"
        f"source_url: {source_url}\n"
        "---\n\n"
    )


def load_json(path, default):
    if os.path.exists(path):
        with open(path) as f:
            return json.load(f)
    return default


def save_json(path, data):
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w") as f:
        json.dump(data, f, indent=2)


def main():
    parser = argparse.ArgumentParser(description="Convert crawled Damodaran XLS/XLSX workbooks to markdown + CSV.")
    parser.add_argument("--force", action="store_true", help="Reconvert even if output already exists.")
    args = parser.parse_args()

    manifest = load_json(MANIFEST_PATH, {"entries": []})
    entries = manifest["entries"]
    progress = load_json(PROGRESS_PATH, {})
    unclassified = load_json(UNCLASSIFIED_PATH, [])
    unclassified_urls = {u["url"] for u in unclassified}

    today = date.today().isoformat()
    written, skipped, errors = 0, 0, 0

    for i, entry in enumerate(entries):
        if i % 50 == 0:
            save_json(PROGRESS_PATH, progress)  # periodic checkpoint in case of interruption
        if entry["type"] != "xls" or entry.get("status") != "downloaded":
            continue
        url = entry["url"]
        local_path = entry.get("local_path")
        if not local_path or not os.path.exists(local_path):
            continue

        folder, reason = classify_destination(url)
        if reason == "tools-default" and url not in unclassified_urls:
            unclassified.append({"url": url, "discovered_on": entry.get("discovered_on"),
                                  "reason": "xls-path-unmatched-defaulted-to-tools"})
            unclassified_urls.add(url)

        filename = os.path.basename(urlparse(url).path)
        stem, ext = os.path.splitext(filename)
        ext = ext.lower()
        slug = slugify(stem)
        workbook_dir = f"{folder}/{slug}"
        md_path = f"{workbook_dir}/{slug}.md"

        prior = progress.get(url)
        if prior and prior.get("status") == "written" and os.path.exists(md_path) and not args.force:
            skipped += 1
            continue

        with open(local_path, "rb") as f:
            data = f.read()

        try:
            sheets = read_workbook_sheets(data, ext)
        except ImportError as e:
            print(f"  Missing dependency for {url}: {e}", file=sys.stderr)
            progress[url] = {"status": "error", "output": None, "error": str(e)}
            errors += 1
            continue
        except Exception as e:
            print(f"  ERROR reading workbook {url}: {e}", file=sys.stderr)
            progress[url] = {"status": "error", "output": None, "error": str(e)}
            errors += 1
            continue

        os.makedirs(workbook_dir, exist_ok=True)

        title = stem.replace("_", " ").replace("-", " ").title()
        lines = [f"# {title}", "", f"Source: {url}", "", f"Sheets: {', '.join(s[0] for s in sheets)}", ""]

        for sheet_name, headers, rows in sheets:
            sheet_slug = slugify(sheet_name)
            lines.append(f"## {sheet_name}")
            lines.append("")
            if len(rows) <= LARGE_SHEET_ROWS:
                lines.append(rows_to_markdown_table(headers, rows))
            else:
                csv_name = f"{slug}-{sheet_slug}.csv"
                csv_content = rows_to_csv(headers, rows)
                with open(f"{workbook_dir}/{csv_name}", "w", encoding="utf-8", newline="") as f:
                    f.write(csv_content)
                lines.append(f"_{len(rows)} rows — showing first {PREVIEW_ROWS}. Full data: [`{csv_name}`]({csv_name})_")
                lines.append("")
                lines.append(rows_to_markdown_table(headers, rows[:PREVIEW_ROWS]))
            lines.append("")

        with open(md_path, "w", encoding="utf-8") as f:
            f.write(frontmatter(title, url, today))
            f.write("\n".join(lines))

        shutil.copyfile(local_path, f"{workbook_dir}/{slug}{ext}")

        progress[url] = {"status": "written", "output": md_path}
        written += 1

    save_json(PROGRESS_PATH, progress)
    save_json(UNCLASSIFIED_PATH, unclassified)

    print(f"Written: {written}  Skipped (already done): {skipped}  Errors: {errors}")


if __name__ == "__main__":
    main()
