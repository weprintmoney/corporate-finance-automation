#!/usr/bin/env python3
"""
Crawl Aswath Damodaran's NYU Stern website (pages.stern.nyu.edu/~adamodar/)
and build a manifest of every HTML page plus every directly-linked PDF/XLS
resource, for later conversion into 03-corporate-finance/03-5-damodaran-online/.

Dry-run (--dry-run): breadth-first crawl of in-scope HTML pages (full GET,
needed to discover links), HEAD-only for PDF/XLS (records Content-Length /
Content-Type, no download). Writes scripts/crawl-manifest.json and prints a
scale report. No PDF/XLS bytes are downloaded in this mode.

Full run (no flag): same crawl, but downloads PDF/XLS bodies to
.crawl-cache/raw/ instead of just HEAD-checking them.

Scope: only pages.stern.nyu.edu/~adamodar/* HTML is fetched and parsed for
further links. Off-domain HTML is never fetched. Off-domain PDF/XLS one hop
away from an in-scope page IS recorded (HEAD-checked / downloaded), matching
the one-hop-external rule in the runbook.

Video files and images are recorded/skipped by extension only (no request
issued). Blog posts (aswathdamodaran.blogspot.com and similar) are skipped
and de-duped against 03-corporate-finance/03-4-blogs/posts/.

Requires: nothing beyond the standard library.

Run:
  python3 scripts/crawl-damodaran-site.py --dry-run
  python3 scripts/crawl-damodaran-site.py            # Phase 1 full crawl
  python3 scripts/crawl-damodaran-site.py --force     # ignore manifest/cache, refetch everything
"""

import argparse
import hashlib
import json
import os
import sys
import time
from datetime import datetime, timezone
from html.parser import HTMLParser
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urljoin, urlparse, urlsplit, urlunsplit
from urllib.request import Request, urlopen
from urllib.robotparser import RobotFileParser

BASE = "https://pages.stern.nyu.edu/~adamodar/"
BASE_HOST = "pages.stern.nyu.edu"
BASE_PATH_PREFIX = "/~adamodar/"

CACHE_DIR = ".crawl-cache"
HTML_CACHE = os.path.join(CACHE_DIR, "html")
RAW_CACHE = os.path.join(CACHE_DIR, "raw")
MANIFEST_PATH = "scripts/crawl-manifest.json"
UNCLASSIFIED_PATH = "scripts/unclassified.json"
BLOG_POSTS_DIR = "03-corporate-finance/03-4-blogs/posts"

USER_AGENT = (
    "Mozilla/5.0 (compatible; finance-automation-crawler/1.0; "
    "+https://github.com/weprintmoney/corporate-finance-automation)"
)
DELAY_SECONDS = 0.5

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".ico", ".tif", ".tiff", ".webp"}
VIDEO_EXTS = {".mp4", ".mov", ".avi", ".wmv", ".mpg", ".mpeg", ".mkv"}
PDF_EXTS = {".pdf"}
XLS_EXTS = {".xls", ".xlsx", ".xlsm"}
HTML_EXTS = {".htm", ".html", "", ".asp", ".aspx"}
BLOG_HOSTS = {"aswathdamodaran.blogspot.com", "www.blogger.com", "feeds.feedburner.com"}
SKIP_SCHEMES = ("mailto:", "javascript:", "tel:")


class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []

    def handle_starttag(self, tag, attrs):
        if tag not in ("a", "frame", "iframe"):
            return
        attr_map = dict(attrs)
        href = attr_map.get("href") or attr_map.get("src")
        if href:
            self.links.append(href)


def load_manifest():
    if os.path.exists(MANIFEST_PATH):
        with open(MANIFEST_PATH) as f:
            data = json.load(f)
        return {e["url"]: e for e in data.get("entries", [])}
    return {}


def save_manifest(entries_by_url):
    os.makedirs(os.path.dirname(MANIFEST_PATH), exist_ok=True)
    payload = {
        "generated": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "entries": list(entries_by_url.values()),
    }
    with open(MANIFEST_PATH, "w") as f:
        json.dump(payload, f, indent=2)


def load_blog_slugs():
    slugs = set()
    if os.path.isdir(BLOG_POSTS_DIR):
        for name in os.listdir(BLOG_POSTS_DIR):
            if name.endswith(".md"):
                slugs.add(name[:-3])
    return slugs


def classify_ext(url):
    ext = os.path.splitext(urlparse(url).path)[1].lower()
    if ext in VIDEO_EXTS:
        return "video"
    if ext in IMAGE_EXTS:
        return "image"
    if ext in PDF_EXTS:
        return "pdf"
    if ext in XLS_EXTS:
        return "xls"
    if ext in HTML_EXTS:
        return "html"
    return "other"


def is_in_scope_html(url):
    p = urlparse(url)
    return p.netloc == BASE_HOST and p.path.startswith(BASE_PATH_PREFIX)


def is_blog_url(url):
    return urlparse(url).netloc in BLOG_HOSTS


def normalize_url(url):
    """Percent-encode unsafe characters (raw spaces etc.) left in raw href values."""
    parts = urlsplit(url)
    path = quote(parts.path, safe="/%:@!$&'()*+,;=")
    query = quote(parts.query, safe="=&%:@!$'()*+,;/")
    return urlunsplit((parts.scheme, parts.netloc, path, query, ""))


def cache_path_for(url, subdir):
    h = hashlib.sha1(url.encode("utf-8")).hexdigest()
    return os.path.join(subdir, h)


def fetch(url, method="GET", timeout=30):
    req = Request(url, headers={"User-Agent": USER_AGENT}, method=method)
    with urlopen(req, timeout=timeout) as resp:
        headers = dict(resp.headers.items())
        body = resp.read() if method == "GET" else b""
        return resp.status, headers, body


def get_robot_parser():
    rp = RobotFileParser()
    rp.set_url(f"https://{BASE_HOST}/robots.txt")
    try:
        rp.read()
    except Exception:
        pass
    return rp


class _Counters:
    """Mutable request/checkpoint counters shared across the crawl loop."""
    def __init__(self):
        self.n_requests = 0
        self.since_checkpoint = 0


def _crawl_one(url, referrer, dry_run, force, manifest, unclassified, stats,
                total_bytes_by_type, rp, seen, queue, counters):
    kind = classify_ext(url)
    off_domain = urlparse(url).netloc != BASE_HOST

    if off_domain and kind not in ("pdf", "xls"):
        # Only PDF/XLS get the one-hop off-domain exception; everything
        # else off-domain (HTML in particular) is never touched.
        return

    if kind == "image":
        stats["image"] += 1
        return

    if kind == "video":
        manifest[url] = {"url": url, "type": "video", "bytes": None, "status": "pending",
                          "local_path": None, "discovered_on": referrer}
        stats["video"] += 1
        return

    if is_blog_url(url):
        stats["blog_skipped"] += 1
        return

    existing = manifest.get(url)
    already_done = existing and existing.get("status") in ("downloaded", "error") and not force

    if kind == "html":
        if not is_in_scope_html(url):
            return

        if not rp.can_fetch(USER_AGENT, url):
            stats["robots_blocked"] += 1
            return

        if existing and existing.get("status") == "error" and not force:
            return

        cache_file = cache_path_for(url, HTML_CACHE)
        if already_done and os.path.exists(cache_file):
            with open(cache_file, "rb") as f:
                body = f.read()
        else:
            try:
                _, headers, body = fetch(url, method="GET")
                counters.n_requests += 1
                time.sleep(DELAY_SECONDS)
            except Exception as e:
                print(f"  ERROR fetching {url}: {e}", file=sys.stderr)
                stats["errors"] += 1
                manifest[url] = {"url": url, "type": "html", "bytes": None, "status": "error",
                                  "local_path": None, "discovered_on": referrer}
                return
            with open(cache_file, "wb") as f:
                f.write(body)
            manifest[url] = {"url": url, "type": "html", "bytes": len(body), "status": "downloaded",
                              "local_path": cache_file, "discovered_on": referrer}
            stats["html"] += 1

        extractor = LinkExtractor()
        try:
            extractor.feed(body.decode("utf-8", errors="replace"))
        except Exception:
            pass

        for link in extractor.links:
            stripped = link.strip()
            if stripped.lower().startswith(SKIP_SCHEMES):
                continue
            try:
                absolute = urljoin(url, stripped).split("#")[0]
                if not absolute:
                    continue
                absolute = normalize_url(absolute)
            except Exception:
                continue
            if absolute in seen:
                continue
            seen.add(absolute)
            queue.append((absolute, url))

    elif kind in ("pdf", "xls"):
        if already_done:
            return
        if not off_domain and not rp.can_fetch(USER_AGENT, url):
            stats["robots_blocked"] += 1
            return
        try:
            if dry_run:
                _, headers, _ = fetch(url, method="HEAD")
                counters.n_requests += 1
            else:
                _, headers, body = fetch(url, method="GET")
                counters.n_requests += 1
            time.sleep(DELAY_SECONDS)
        except Exception as e:
            print(f"  ERROR {'HEAD' if dry_run else 'GET'} {url}: {e}", file=sys.stderr)
            stats["errors"] += 1
            manifest[url] = {"url": url, "type": kind, "bytes": None, "status": "error",
                              "local_path": None, "discovered_on": referrer}
            return

        length = headers.get("Content-Length")
        nbytes = int(length) if length and length.isdigit() else None

        if dry_run:
            manifest[url] = {"url": url, "type": kind, "bytes": nbytes, "status": "pending",
                              "local_path": None, "discovered_on": referrer}
        else:
            raw_path = cache_path_for(url, RAW_CACHE)
            with open(raw_path, "wb") as f:
                f.write(body)
            nbytes = nbytes or len(body)
            manifest[url] = {"url": url, "type": kind, "bytes": nbytes, "status": "downloaded",
                              "local_path": raw_path, "discovered_on": referrer}

        stats[kind] += 1
        if nbytes:
            total_bytes_by_type[kind] += nbytes

    else:
        if not off_domain:
            unclassified.append({"url": url, "discovered_on": referrer})
        stats["other"] += 1


def crawl(dry_run: bool, force: bool):
    os.makedirs(HTML_CACHE, exist_ok=True)
    os.makedirs(RAW_CACHE, exist_ok=True)

    manifest = {} if force else load_manifest()
    unclassified = []
    rp = get_robot_parser()

    base_normalized = normalize_url(BASE)
    queue = [(base_normalized, None)]
    seen = {base_normalized}

    stats = {"html": 0, "pdf": 0, "xls": 0, "video": 0, "image": 0,
              "blog_skipped": 0, "other": 0, "errors": 0, "robots_blocked": 0}
    total_bytes_by_type = {"pdf": 0, "xls": 0}
    counters = _Counters()
    CHECKPOINT_EVERY = 20

    while queue:
        url, referrer = queue.pop(0)
        try:
            _crawl_one(url, referrer, dry_run, force, manifest, unclassified, stats,
                       total_bytes_by_type, rp, seen, queue, counters)
        except Exception as e:
            print(f"  UNEXPECTED ERROR on {url}: {e}", file=sys.stderr)
            stats["errors"] += 1
            manifest[url] = {"url": url, "type": classify_ext(url), "bytes": None, "status": "error",
                              "local_path": None, "discovered_on": referrer}

        counters.since_checkpoint += 1
        if counters.since_checkpoint >= CHECKPOINT_EVERY:
            save_manifest(manifest)
            counters.since_checkpoint = 0

    save_manifest(manifest)

    if unclassified:
        os.makedirs(os.path.dirname(UNCLASSIFIED_PATH), exist_ok=True)
        with open(UNCLASSIFIED_PATH, "w") as f:
            json.dump(unclassified, f, indent=2)

    print(f"\n({counters.n_requests} HTTP requests issued this run)")
    return manifest, stats, total_bytes_by_type


def estimate_pdf_pages(nbytes):
    if not nbytes:
        return 0
    return max(1, round(nbytes / (60 * 1024)))


def print_report(manifest, stats, total_bytes_by_type):
    print("\n" + "=" * 60)
    print("CRAWL MANIFEST REPORT")
    print("=" * 60)

    print(f"\nURLs in manifest: {len(manifest)}")
    for k in ("html", "pdf", "xls", "video", "other"):
        print(f"  {k:14s}: {stats.get(k, 0)}")
    print("\nSkipped (not recorded in manifest):")
    for k in ("image", "blog_skipped", "robots_blocked", "errors"):
        print(f"  {k:14s}: {stats.get(k, 0)}")

    pdf_mb = total_bytes_by_type["pdf"] / 1e6
    xls_mb = total_bytes_by_type["xls"] / 1e6
    print(f"\nTotal bytes (PDF): {total_bytes_by_type['pdf']:,} ({pdf_mb:.1f} MB)")
    print(f"Total bytes (XLS): {total_bytes_by_type['xls']:,} ({xls_mb:.1f} MB)")

    total_pdf_pages = sum(
        estimate_pdf_pages(e.get("bytes")) for e in manifest.values() if e["type"] == "pdf"
    )
    print(f"\nEstimated PDF pages (~60KB/page when unknown): {total_pdf_pages:,}")

    marker_low_min, marker_high_min = total_pdf_pages * 1 / 60, total_pdf_pages * 2 / 60
    print(f"Estimated marker GPU runtime: {marker_low_min:.0f}-{marker_high_min:.0f} min (~1-2s/page)")

    fallback_low_pages = round(total_pdf_pages * 0.05)
    fallback_high_pages = round(total_pdf_pages * 0.15)
    cost_low = fallback_low_pages * 0.01
    cost_high = fallback_high_pages * 0.02
    print(f"Vision-fallback pages (5-15% estimate): {fallback_low_pages:,}-{fallback_high_pages:,}")
    print(f"Vision-fallback cost band (claude-sonnet-4-6): ${cost_low:.2f}-${cost_high:.2f}")

    total_binary_bytes = total_bytes_by_type["pdf"] + total_bytes_by_type["xls"]
    print("\n--- Decision gates (resolve with user before Phase 1) ---")
    gate_a = "REVIEW: consider Git LFS for *.xls/*.xlsx" if total_binary_bytes > 300e6 else "OK: under 300MB, no LFS needed"
    print(f"Gate a (LFS threshold, >300MB binaries): {gate_a}  [{total_binary_bytes/1e6:.1f} MB total]")
    gate_b = "small — vision-only would also be fine" if total_pdf_pages < 500 else "confirm marker runtime is acceptable"
    print(f"Gate b (PDF volume): {gate_b}  [{total_pdf_pages:,} pages]")
    gate_c = "RESCOPE WITH USER" if total_binary_bytes > 1e9 else "OK: under 1GB"
    print(f"Gate c (>1GB total): {gate_c}")

    if stats.get("other", 0):
        print(f"\n{stats['other']} unclassified URL(s) logged to {UNCLASSIFIED_PATH} — classify manually.")

    print("\nManifest written to:", MANIFEST_PATH)
    print("=" * 60)


def main():
    parser = argparse.ArgumentParser(
        description="Crawl Damodaran's NYU Stern site into a manifest, optionally downloading."
    )
    parser.add_argument("--dry-run", action="store_true",
                         help="HEAD-only for PDF/XLS; no downloads. Build manifest + report only.")
    parser.add_argument("--force", action="store_true",
                         help="Ignore .crawl-cache/ and existing manifest entries; refetch everything.")
    args = parser.parse_args()

    print(f"Crawling {BASE} (dry_run={args.dry_run}, force={args.force})...\n")
    manifest, stats, total_bytes_by_type = crawl(dry_run=args.dry_run, force=args.force)
    print_report(manifest, stats, total_bytes_by_type)


if __name__ == "__main__":
    main()
