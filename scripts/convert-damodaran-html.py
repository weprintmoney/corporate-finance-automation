#!/usr/bin/env python3
"""
Convert crawled Damodaran HTML pages (scripts/crawl-manifest.json, type=html)
into Claude-readable markdown under 03-corporate-finance/03-5-damodaran-online/.

Also emits stub .md files for type=video entries (title + description +
external URL only — never downloads the video itself).

Idempotent: skips a URL if its destination .md already exists, unless --force.
Logs per-file results to scripts/convert-progress.json and unmatched URL
paths to scripts/unclassified.json (append, do not guess silently).

Requires: pip install markdownify

Run: python3 scripts/convert-damodaran-html.py [--force]
"""

import argparse
import json
import os
import re
import sys
from datetime import date
from urllib.parse import urlparse

MANIFEST_PATH = "scripts/crawl-manifest.json"
PROGRESS_PATH = "scripts/convert-progress.json"
UNCLASSIFIED_PATH = "scripts/unclassified.json"
OUT_ROOT = "03-corporate-finance/03-5-damodaran-online"
OWNER = "weprintmoney"

TITLE_RE = re.compile(r"<title[^>]*>(.*?)</title>", re.IGNORECASE | re.DOTALL)
TAG_RE = re.compile(r"<[^>]+>")
WS_RE = re.compile(r"\s+")


def slugify(text):
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "untitled"


def classify_destination(url):
    """URL-path -> destination folder, per the runbook's classification map.
    Returns (folder, reason) or (None, reason) if unmatched."""
    path = urlparse(url).path.lower()
    segments = [s for s in path.split("/") if s]

    if "/pc/datasets/" in path or "/new_home_page/data" in path:
        return f"{OUT_ROOT}/03-5-1-datasets", "datasets"

    if "/pdfiles/" in path:
        return f"{OUT_ROOT}/03-5-3-papers", "papers"

    if "/new_home_page/spreadsheets/" in path:
        return f"{OUT_ROOT}/03-5-4-tools", "tools"

    if "/books/" in path or "book" in segments:
        return f"{OUT_ROOT}/03-5-5-books", "books"

    filename = segments[-1] if segments else ""
    stem = os.path.splitext(filename)[0]
    m = re.match(r"^(cf|val)([a-z0-9]*)", stem)
    if m:
        course = "corporate-finance" if m.group(1) == "cf" else "valuation"
        return f"{OUT_ROOT}/03-5-2-course-materials/{course}", "course-materials"
    for course_key, course_dir in (("strategic", "strategic-finance"),):
        if course_key in stem:
            return f"{OUT_ROOT}/03-5-2-course-materials/{course_dir}", "course-materials"

    # Default bucket rather than dropping the page — same approach as the
    # xls/pdf converters (default + logged to unclassified.json for later
    # manual reclassification) rather than silently losing content.
    return f"{OUT_ROOT}/03-5-2-course-materials/general", "unmatched-defaulted-to-general"


def extract_title(html_bytes, fallback):
    try:
        text = html_bytes.decode("utf-8", errors="replace")
    except Exception:
        return fallback
    m = TITLE_RE.search(text)
    if not m:
        return fallback
    title = TAG_RE.sub("", m.group(1))
    title = WS_RE.sub(" ", title).strip()
    return title or fallback


def is_frameset_only(html_bytes):
    try:
        text = html_bytes.decode("utf-8", errors="replace").lower()
    except Exception:
        return False
    return "<frameset" in text and "<frame " in text


def html_to_markdown(html_bytes):
    from markdownify import markdownify as md
    text = html_bytes.decode("utf-8", errors="replace")
    body = md(text, heading_style="ATX", strip=["script", "style"])
    body = re.sub(r"\n{3,}", "\n\n", body).strip()
    return body


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
    parser = argparse.ArgumentParser(description="Convert crawled Damodaran HTML to markdown.")
    parser.add_argument("--force", action="store_true", help="Reconvert even if output already exists.")
    args = parser.parse_args()

    try:
        import markdownify  # noqa: F401
    except ImportError:
        print("markdownify not installed. Run: pip install markdownify", file=sys.stderr)
        sys.exit(1)

    manifest = load_json(MANIFEST_PATH, {"entries": []})
    entries = manifest["entries"]
    progress = load_json(PROGRESS_PATH, {})
    unclassified = load_json(UNCLASSIFIED_PATH, [])
    unclassified_urls = {u["url"] for u in unclassified}

    today = date.today().isoformat()
    written, skipped, unmatched_count, empty_skipped = 0, 0, 0, 0

    for i, entry in enumerate(entries):
        if i % 50 == 0:
            save_json(PROGRESS_PATH, progress)  # periodic checkpoint in case of interruption
        url = entry["url"]
        etype = entry["type"]
        if etype not in ("html", "video"):
            continue
        if etype == "html" and entry.get("status") != "downloaded":
            continue

        folder, reason = classify_destination(url)
        if reason.startswith("unmatched") and url not in unclassified_urls:
            unclassified.append({"url": url, "discovered_on": entry.get("discovered_on"), "reason": reason})
            unclassified_urls.add(url)
            unmatched_count += 1

        filename = os.path.splitext(os.path.basename(urlparse(url).path))[0] or "index"
        slug = slugify(filename)
        out_path = f"{folder}/{slug}.md"

        prior = progress.get(url)
        if prior and prior.get("status") == "written" and os.path.exists(out_path) and not args.force:
            skipped += 1
            continue

        if etype == "video":
            title = slug.replace("-", " ").title()
            body = (
                f"# {title}\n\n"
                f"Video lecture — not downloaded (see `.claude/rules/no-read-mp4.md` for why videos "
                "are never mirrored locally).\n\n"
                f"Watch at: {url}\n"
            )
            os.makedirs(folder, exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(frontmatter(title, url, today))
                f.write(body)
            progress[url] = {"status": "written", "output": out_path, "type": "video-stub"}
            written += 1
            continue

        local_path = entry.get("local_path")
        if not local_path or not os.path.exists(local_path):
            progress[url] = {"status": "error", "output": None, "error": "cached html missing"}
            continue

        with open(local_path, "rb") as f:
            html_bytes = f.read()

        if is_frameset_only(html_bytes):
            progress[url] = {"status": "skipped-frameset", "output": None}
            continue

        try:
            body = html_to_markdown(html_bytes)
        except Exception as e:
            print(f"  ERROR converting {url}: {e}", file=sys.stderr)
            progress[url] = {"status": "error", "output": None, "error": str(e)}
            continue

        if len(body) < 50:
            progress[url] = {"status": "skipped-empty", "output": None}
            empty_skipped += 1
            continue

        title = extract_title(html_bytes, fallback=slug.replace("-", " ").title())
        os.makedirs(folder, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(frontmatter(title, url, today))
            f.write(body)
            f.write("\n")

        progress[url] = {"status": "written", "output": out_path}
        written += 1

    save_json(PROGRESS_PATH, progress)
    save_json(UNCLASSIFIED_PATH, unclassified)

    print(f"Written: {written}  Skipped (already done): {skipped}  "
          f"Skipped (empty/frameset): {empty_skipped}  Unmatched (logged): {unmatched_count}")


if __name__ == "__main__":
    main()
