#!/usr/bin/env python3
"""
Fetch Aswath Damodaran's "Musings on Markets" blog archive via Blogger's public
JSON feed and store each post as a markdown file with attribution frontmatter.

Usage:
    python3 fetch_archive.py              # incremental — skip posts already on disk
    python3 fetch_archive.py --refresh    # re-download every post
    python3 fetch_archive.py --limit 20   # fetch only the first N posts

Files are written to ./posts/YYYY-MM-DD-slug.md with frontmatter that includes
the canonical source URL. This mirror is for personal analysis only; the source
posts are copyrighted by their author.
"""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

FEED_BASE = "https://aswathdamodaran.blogspot.com/feeds/posts/default"
PAGE_SIZE = 25  # Blogger caps at 25 per request
USER_AGENT = "damodaran-archive-fetcher/1.0 (+personal study)"
SLEEP_SECONDS = 0.5


def fetch_feed_page(start_index: int, page_size: int = PAGE_SIZE) -> dict:
    params = urllib.parse.urlencode(
        {"alt": "json", "max-results": page_size, "start-index": start_index}
    )
    url = f"{FEED_BASE}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.load(resp)


def slugify(text: str, max_len: int = 80) -> str:
    text = text.lower().strip()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = text.strip("-")
    return text[:max_len].rstrip("-")


TAG_STRIP_RE = re.compile(r"<[^>]+>")
WHITESPACE_RE = re.compile(r"[ \t]+")
NEWLINES_RE = re.compile(r"\n{3,}")


def html_to_markdown(raw: str) -> str:
    """Lightweight HTML → markdown conversion for Blogger post bodies."""
    text = raw

    text = re.sub(r"<br\s*/?>", "\n", text, flags=re.I)
    text = re.sub(r"</p>", "\n\n", text, flags=re.I)
    text = re.sub(r"<p[^>]*>", "", text, flags=re.I)
    text = re.sub(r"</div>", "\n", text, flags=re.I)
    text = re.sub(r"<div[^>]*>", "", text, flags=re.I)

    for level in range(1, 7):
        text = re.sub(
            rf"<h{level}[^>]*>(.*?)</h{level}>",
            lambda m, lvl=level: f"\n\n{'#' * lvl} {m.group(1).strip()}\n\n",
            text,
            flags=re.I | re.S,
        )

    text = re.sub(
        r"<a\s+[^>]*href=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>",
        lambda m: f"[{re.sub(r'<[^>]+>', '', m.group(2)).strip()}]({m.group(1)})",
        text,
        flags=re.I | re.S,
    )

    text = re.sub(r"<(strong|b)>(.*?)</\1>", r"**\2**", text, flags=re.I | re.S)
    text = re.sub(r"<(em|i)>(.*?)</\1>", r"*\2*", text, flags=re.I | re.S)

    text = re.sub(r"<li[^>]*>", "- ", text, flags=re.I)
    text = re.sub(r"</li>", "\n", text, flags=re.I)
    text = re.sub(r"</?[uo]l[^>]*>", "\n", text, flags=re.I)

    text = re.sub(
        r"<img[^>]*src=[\"']([^\"']+)[\"'][^>]*alt=[\"']([^\"']*)[\"'][^>]*/?>",
        r"![\2](\1)",
        text,
        flags=re.I,
    )
    text = re.sub(
        r"<img[^>]*src=[\"']([^\"']+)[\"'][^>]*/?>",
        r"![](\1)",
        text,
        flags=re.I,
    )

    text = TAG_STRIP_RE.sub("", text)
    text = html.unescape(text)
    text = WHITESPACE_RE.sub(" ", text)
    text = re.sub(r" *\n *", "\n", text)
    text = NEWLINES_RE.sub("\n\n", text)
    return text.strip() + "\n"


def entry_alternate_link(entry: dict) -> str | None:
    for link in entry.get("link", []):
        if link.get("rel") == "alternate":
            return link.get("href")
    return None


def entry_tags(entry: dict) -> list[str]:
    tags = []
    for cat in entry.get("category", []):
        term = cat.get("term")
        if term:
            tags.append(term)
    return tags


def build_markdown(entry: dict, today: str) -> tuple[str, str]:
    """Return (filename, file_body)."""
    title = entry.get("title", {}).get("$t", "untitled").strip()
    published_iso = entry.get("published", {}).get("$t", "")
    updated_iso = entry.get("updated", {}).get("$t", "")
    published_date = published_iso[:10] if published_iso else "unknown"
    source_url = entry_alternate_link(entry) or ""
    tags = entry_tags(entry)
    body_html = entry.get("content", {}).get("$t", "")
    body_md = html_to_markdown(body_html)

    slug = slugify(title) or "untitled"
    filename = f"{published_date}-{slug}.md"

    tags_line = ""
    if tags:
        tags_line = "tags:\n" + "".join(f"  - {t}\n" for t in tags)

    frontmatter = (
        "---\n"
        f'title: "{title.replace(chr(34), chr(39))}"\n'
        "author: aswath-damodaran\n"
        "status: active\n"
        "owner: weprintmoney\n"
        f"source_url: {source_url}\n"
        f"published: {published_date}\n"
        f"updated_source: {updated_iso[:10] if updated_iso else 'unknown'}\n"
        f"fetched: {today}\n"
        f"{tags_line}"
        "---\n\n"
    )

    header = f"# {title}\n\n_Source: [{source_url}]({source_url}) — published {published_date}_\n\n"
    return filename, frontmatter + header + body_md


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--refresh", action="store_true", help="Overwrite existing files.")
    parser.add_argument("--limit", type=int, default=None, help="Max posts to fetch (for testing).")
    parser.add_argument(
        "--out",
        default=str(Path(__file__).parent / "posts"),
        help="Output directory.",
    )
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    written = 0
    skipped = 0
    fetched = 0
    start_index = 1

    while True:
        if args.limit is not None and fetched >= args.limit:
            break

        page_size = PAGE_SIZE
        if args.limit is not None:
            page_size = min(PAGE_SIZE, args.limit - fetched)

        print(f"fetching start-index={start_index} page-size={page_size} ...", file=sys.stderr)
        page = fetch_feed_page(start_index, page_size)
        entries = page.get("feed", {}).get("entry", [])
        if not entries:
            break

        for entry in entries:
            fetched += 1
            filename, body = build_markdown(entry, today)
            path = out_dir / filename
            if path.exists() and not args.refresh:
                skipped += 1
                continue
            path.write_text(body, encoding="utf-8")
            written += 1

        start_index += len(entries)
        time.sleep(SLEEP_SECONDS)

    print(
        f"done. fetched={fetched} written={written} skipped={skipped} out={out_dir}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
