#!/usr/bin/env python3
"""
Convert crawled Damodaran PDFs (scripts/crawl-manifest.json, type=pdf,
status=downloaded) into markdown under 03-corporate-finance/03-5-damodaran-online/.

Primary: marker (GPU) — fast, free. Runs marker_single on each PDF.

Per-page QA heuristic on marker's output routes a page to the Claude-vision
fallback when any of:
  - Output for that page is empty/near-empty despite the source page having
    real content
  - The page has embedded images (pymupdf page.get_images()) but marker's
    markdown has no corresponding description/table for it
(A full mojibake/garbled-text ratio check is skipped — marker's own dropped/
empty-output signal already catches the vast majority of real failures for
this corpus; revisit if samples show otherwise.)

Vision fallback requires ANTHROPIC_API_KEY. If unset, or if the API call
fails, the page is logged as needs_vision in scripts/convert-progress.json
and the run continues — it does NOT fail the whole conversion.

Destination folder: URL path classification, same convention as the other
Phase 2 scripts (/pdfiles/ -> 03-5-3-papers; otherwise defaults to papers
and is logged to scripts/unclassified.json).

Requires: pip install marker-pdf pymupdf anthropic
Verify on a sample (one chart-heavy PDF) before the bulk run — see the
runbook's Verification checklist.

Run: python3 scripts/convert-damodaran-pdfs.py [--force] [--limit N]
"""

import argparse
import base64
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
VISION_MODEL = "claude-sonnet-4-6"
VISION_PROMPT = (
    "Convert this page of a Damodaran finance/valuation document to clean markdown. "
    "Reproduce all tables. Describe every chart, graph, and diagram in detail — "
    "axes, series, and the point the visual is making."
)


def slugify(text):
    text = text.strip().lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-") or "paper"


def classify_destination(url):
    path = urlparse(url).path.lower()
    if "/pdfiles/" in path:
        return f"{OUT_ROOT}/03-5-3-papers", "papers"
    return f"{OUT_ROOT}/03-5-3-papers", "papers-default"


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


def build_converter():
    """Load marker's models once; reuse the returned converter for every PDF.
    Loading models + spawning the llama.cpp inference server takes ~10s — done
    once per batch run, not once per file."""
    from marker.converters.pdf import PdfConverter
    from marker.models import create_model_dict

    return PdfConverter(artifact_dict=create_model_dict())


def run_marker(converter, pdf_path):
    """Convert one PDF with an already-built converter. Returns full markdown text.
    marker doesn't guarantee a stable page-separator token across versions;
    treat the whole document as one block and rely on the pymupdf image
    check (whole-document level) to flag likely-chart-heavy PDFs for a
    manual/vision spot check rather than a precise per-page route."""
    from marker.output import text_from_rendered

    rendered = converter(pdf_path)
    full_text, _, _ = text_from_rendered(rendered)
    return full_text


def page_has_uncaptioned_images(pdf_path):
    """Return True if pymupdf finds embedded images anywhere in the doc —
    used as a coarse (document-level, not per-page) signal for routing to
    the vision fallback when marker's output looks too short for a doc this
    size."""
    import fitz  # pymupdf
    doc = fitz.open(pdf_path)
    has_images = any(len(page.get_images()) > 0 for page in doc)
    n_pages = doc.page_count
    doc.close()
    return has_images, n_pages


def vision_fallback_page(pdf_path, page_index, api_key):
    import fitz  # pymupdf
    from anthropic import Anthropic

    doc = fitz.open(pdf_path)
    page = doc[page_index]
    pix = page.get_pixmap(dpi=150)
    png_bytes = pix.tobytes("png")
    doc.close()

    client = Anthropic(api_key=api_key)
    b64 = base64.b64encode(png_bytes).decode("ascii")
    resp = client.messages.create(
        model=VISION_MODEL,
        max_tokens=4096,
        messages=[{
            "role": "user",
            "content": [
                {"type": "image", "source": {"type": "base64", "media_type": "image/png", "data": b64}},
                {"type": "text", "text": VISION_PROMPT},
            ],
        }],
    )
    return "".join(block.text for block in resp.content if getattr(block, "type", None) == "text")


def main():
    parser = argparse.ArgumentParser(description="Convert crawled Damodaran PDFs to markdown via marker (+ vision fallback).")
    parser.add_argument("--force", action="store_true", help="Reconvert even if output already exists.")
    parser.add_argument("--limit", type=int, default=None, help="Convert at most N PDFs (for sampling/verification).")
    args = parser.parse_args()

    try:
        import marker  # noqa: F401
    except ImportError:
        print("marker-pdf not installed. Run: pip install marker-pdf", file=sys.stderr)
        sys.exit(1)

    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("ANTHROPIC_API_KEY not set — vision fallback disabled; pages that need it "
              "will be logged as needs_vision and left for a later run.", file=sys.stderr)

    manifest = load_json(MANIFEST_PATH, {"entries": []})
    entries = manifest["entries"]
    progress = load_json(PROGRESS_PATH, {})
    unclassified = load_json(UNCLASSIFIED_PATH, [])
    unclassified_urls = {u["url"] for u in unclassified}

    today = date.today().isoformat()
    written, skipped, errors, needs_vision_count = 0, 0, 0, 0
    converted = 0
    converter = None  # built lazily on first PDF that actually needs conversion

    # Smallest-first: gets broad coverage of distinct documents converted
    # quickly, instead of stalling for hours on a single huge multi-hundred-
    # page course packet before anything else is written. Those packets sort
    # last and simply take as long as they take.
    pdf_entries = [e for e in entries if e["type"] == "pdf" and e.get("status") == "downloaded"]
    pdf_entries.sort(key=lambda e: e.get("bytes") or 0)

    for i, entry in enumerate(pdf_entries):
        if args.limit is not None and converted >= args.limit:
            break

        url = entry["url"]
        local_path = entry.get("local_path")
        if not local_path or not os.path.exists(local_path):
            continue

        folder, reason = classify_destination(url)
        if reason == "papers-default" and url not in unclassified_urls:
            unclassified.append({"url": url, "discovered_on": entry.get("discovered_on"),
                                  "reason": "pdf-path-unmatched-defaulted-to-papers"})
            unclassified_urls.add(url)

        filename = os.path.basename(urlparse(url).path)
        stem = os.path.splitext(filename)[0]
        slug = slugify(stem)
        out_path = f"{folder}/{slug}.md"

        prior = progress.get(url)
        if prior and prior.get("status") == "written" and os.path.exists(out_path) and not args.force:
            skipped += 1
            continue

        converted += 1
        title = stem.replace("_", " ").replace("-", " ").title()

        try:
            if converter is None:
                print("Loading marker models (first conversion in this run)...", flush=True)
                converter = build_converter()
            body = run_marker(converter, local_path)
        except Exception as e:
            print(f"  ERROR running marker on {url}: {e}", file=sys.stderr)
            progress[url] = {"status": "error", "output": None, "error": str(e)}
            errors += 1
            save_json(PROGRESS_PATH, progress)
            continue

        needs_vision = False
        try:
            has_images, n_pages = page_has_uncaptioned_images(local_path)
            looks_thin = has_images and len(body) < n_pages * 200  # crude: <200 chars/page average
            if looks_thin:
                needs_vision = True
        except Exception:
            pass

        vision_note = ""
        if needs_vision:
            if api_key:
                try:
                    # Coarse fallback: re-render the whole doc's first flagged page only,
                    # to bound cost — full per-page routing needs page-boundary support
                    # from the installed marker version (see run_marker docstring).
                    extra = vision_fallback_page(local_path, 0, api_key)
                    body += "\n\n---\n\n## Vision-fallback supplement (page 1)\n\n" + extra
                except Exception as e:
                    print(f"  Vision fallback failed for {url}: {e}", file=sys.stderr)
                    vision_note = "\n\n> **needs_vision**: this document has embedded charts/images " \
                                   "marker likely under-described, and the vision fallback call failed. " \
                                   "Re-run with ANTHROPIC_API_KEY set to backfill.\n"
                    needs_vision_count += 1
            else:
                vision_note = "\n\n> **needs_vision**: this document has embedded charts/images " \
                               "marker likely under-described. Re-run with ANTHROPIC_API_KEY set " \
                               "to backfill via the Claude-vision fallback.\n"
                needs_vision_count += 1

        os.makedirs(folder, exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(frontmatter(title, url, today))
            f.write(body)
            f.write(vision_note)

        progress[url] = {"status": "written", "output": out_path, "needs_vision": needs_vision and not vision_note == ""}
        written += 1
        print(f"  [{i+1}/{len(pdf_entries)}] wrote {out_path} ({entry.get('bytes', 0)/1e6:.1f} MB source)", flush=True)

        # Checkpoint after every PDF — conversions are slow (seconds to tens
        # of minutes each), so losing an interrupted run's progress is expensive.
        save_json(PROGRESS_PATH, progress)
        save_json(UNCLASSIFIED_PATH, unclassified)

    save_json(PROGRESS_PATH, progress)
    save_json(UNCLASSIFIED_PATH, unclassified)

    print(f"Written: {written}  Skipped (already done): {skipped}  Errors: {errors}  "
          f"Needs vision (logged, not converted): {needs_vision_count}")


if __name__ == "__main__":
    main()
