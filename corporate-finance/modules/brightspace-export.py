#!/usr/bin/env python3
"""
brightspace-export.py

Exports NYU Brightspace course content into the repo structure for a given course.
Downloads slides (PDF→markdown), spreadsheets (XLS→markdown), and readings;
generates lesson-overview.md per lesson; updates lesson-index.yaml.

─── SETUP ───────────────────────────────────────────────────────────────────
1. Log in to brightspace.nyu.edu in your browser
2. Open DevTools (F12) → Application → Cookies → brightspace.nyu.edu
3. Copy the values for:
     d2lSessionVal          (the long alphanumeric string)
     d2lSecureSessionVal    (another long alphanumeric string)
4. Find your course's org unit ID from its URL:
     brightspace.nyu.edu/d2l/home/123456  →  org unit = 123456
5. Create .brightspace.env in the repo root:
     D2L_SESSION_VAL=<paste d2lSessionVal here>
     D2L_SECURE_SESSION_VAL=<paste d2lSecureSessionVal here>
     D2L_ORG_UNIT_ID=<paste org unit ID here>
     D2L_BASE_URL=https://brightspace.nyu.edu
     # Optional — set to "accounting" or "corporate-finance"
     COURSE_TYPE=corporate-finance

─── USAGE ───────────────────────────────────────────────────────────────────
  python3 corporate-finance/modules/brightspace-export.py
  python3 corporate-finance/modules/brightspace-export.py --lesson 13
  python3 corporate-finance/modules/brightspace-export.py --modules 2 3
  python3 corporate-finance/modules/brightspace-export.py --dry-run
  python3 corporate-finance/modules/brightspace-export.py --toc-only
"""

import argparse
import io
import json
import os
import re
import shutil
import sys
import time
from datetime import date
from pathlib import Path

import pandas as pd
import pdfplumber
import requests
import yaml

# ─── Repo layout ─────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).parent.parent.parent
CF_MODULES = REPO_ROOT / "corporate-finance" / "modules"
FA_MODULES = REPO_ROOT / "financial-accounting" / "modules"

LESSON_MODULE_MAP = {
    **{n: "module-1" for n in range(1, 13)},
    **{n: "module-2" for n in range(13, 20)},
    **{n: "module-3" for n in range(20, 27)},
    **{n: "module-4" for n in range(27, 37)},
}

# ─── D2L API helpers ──────────────────────────────────────────────────────────

D2L_API_VERSIONS = ["1.51", "1.48", "1.44"]


def load_env(env_file: Path) -> dict:
    if not env_file.exists():
        sys.exit(
            f"Missing {env_file}\n"
            "Create it with D2L_SESSION_VAL, D2L_SECURE_SESSION_VAL, "
            "D2L_ORG_UNIT_ID, D2L_BASE_URL  (see script header for details)."
        )
    cfg = {}
    for line in env_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            cfg[k.strip()] = v.strip()
    required = ["D2L_SESSION_VAL", "D2L_SECURE_SESSION_VAL", "D2L_ORG_UNIT_ID", "D2L_BASE_URL"]
    missing = [k for k in required if not cfg.get(k)]
    if missing:
        sys.exit(f"Missing required keys in .brightspace.env: {', '.join(missing)}")
    return cfg


def make_session(cfg: dict) -> requests.Session:
    s = requests.Session()
    s.cookies.set("d2lSessionVal", cfg["D2L_SESSION_VAL"], domain=cfg["D2L_BASE_URL"].split("//")[-1])
    s.cookies.set("d2lSecureSessionVal", cfg["D2L_SECURE_SESSION_VAL"], domain=cfg["D2L_BASE_URL"].split("//")[-1])
    s.headers.update({"User-Agent": "Mozilla/5.0"})
    return s


def detect_api_version(session: requests.Session, base: str, org_id: str) -> str:
    for ver in D2L_API_VERSIONS:
        url = f"{base}/d2l/api/le/{ver}/{org_id}/content/toc/"
        r = session.get(url, timeout=15, allow_redirects=False)
        if r.status_code == 200:
            print(f"  D2L API version: {ver}")
            return ver
        if r.status_code == 401:
            sys.exit("Authentication failed — session cookies expired. Re-export from browser.")
    sys.exit(f"Could not find a working D2L API version for org unit {org_id}")


def fetch_toc(session: requests.Session, base: str, org_id: str, ver: str) -> dict:
    url = f"{base}/d2l/api/le/{ver}/{org_id}/content/toc/"
    r = session.get(url, timeout=30)
    r.raise_for_status()
    return r.json()


# ─── TOC parsing ─────────────────────────────────────────────────────────────

def iter_topics(node: dict):
    """Recursively yield (breadcrumb_list, topic_dict) from a D2L TOC node."""
    for module in node.get("Modules", []):
        crumb = [module.get("Title", "")]
        yield from _walk(crumb, module)


def _walk(crumb, node):
    for topic in node.get("Topics", []):
        yield (crumb[:], topic)
    for sub in node.get("Modules", []):
        yield from _walk(crumb + [sub.get("Title", "")], sub)


def guess_lesson_number(crumb: list, title: str) -> int | None:
    """Try to extract a lesson/session number from the breadcrumb or title."""
    text = " ".join(crumb) + " " + title
    m = re.search(r"(?:session|lesson|week|class)\s*[:\-]?\s*(\d+)", text, re.I)
    if m:
        return int(m.group(1))
    m = re.search(r"\b(\d{1,2})\b", text)
    if m:
        n = int(m.group(1))
        if 1 <= n <= 50:
            return n
    return None


def classify_topic(topic: dict) -> str:
    """Return 'slide', 'spreadsheet', 'reading', 'video', 'blog', or 'unknown'."""
    title = (topic.get("Title") or "").lower()
    url = (topic.get("Url") or "").lower()
    tid = (topic.get("TypeIdentifier") or "").lower()

    if any(k in title for k in ["slide", "deck", "acf_s"]):
        return "slide"
    if any(k in title for k in ["spreadsheet", ".xls", "data", "calculator", "estimator"]):
        return "spreadsheet"
    if any(k in title for k in ["reading", "paper", "chapter", "article"]):
        return "reading"
    if any(k in title for k in ["video", "lecture", "session", "recording"]):
        return "video"
    if "blog" in title or "musings" in title or "blogspot" in url:
        return "blog"
    if ".pdf" in url or ".pdf" in title:
        return "slide"
    if any(x in url for x in [".xls", ".xlsx"]):
        return "spreadsheet"
    if "kaltura" in url or "stream.nyu" in url or "video" in url:
        return "video"
    return "unknown"


# ─── File download ────────────────────────────────────────────────────────────

def download_topic_file(session: requests.Session, base: str, org_id: str, ver: str, topic: dict, dest: Path) -> Path | None:
    """Download a D2L-hosted file topic; return saved path or None."""
    topic_id = topic.get("Identifier") or topic.get("TopicId")
    direct_url = topic.get("Url") or ""

    # Try D2L API download endpoint first
    if topic_id:
        api_url = f"{base}/d2l/api/le/{ver}/{org_id}/content/topics/{topic_id}/file"
        r = session.get(api_url, timeout=60, stream=True)
        if r.status_code == 200:
            return _save_response(r, dest, topic.get("Title", "file"))

    # Fall back to direct URL
    if direct_url.startswith("http"):
        r = session.get(direct_url, timeout=60, stream=True)
        if r.status_code == 200:
            return _save_response(r, dest, topic.get("Title", "file"))

    return None


def _save_response(r: requests.Response, dest_dir: Path, hint: str) -> Path:
    content_disp = r.headers.get("Content-Disposition", "")
    fname_match = re.search(r'filename="?([^";\n]+)"?', content_disp)
    if fname_match:
        fname = fname_match.group(1).strip()
    else:
        # Guess from hint or content-type
        ext = _ext_from_content_type(r.headers.get("Content-Type", ""))
        fname = to_kebab(hint) + ext

    dest_dir.mkdir(parents=True, exist_ok=True)
    dest_path = dest_dir / fname
    with open(dest_path, "wb") as f:
        for chunk in r.iter_content(8192):
            f.write(chunk)
    return dest_path


def _ext_from_content_type(ct: str) -> str:
    ct = ct.split(";")[0].strip()
    return {
        "application/pdf": ".pdf",
        "application/vnd.ms-excel": ".xls",
        "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": ".xlsx",
        "application/octet-stream": ".bin",
    }.get(ct, "")


# ─── PDF → markdown ───────────────────────────────────────────────────────────

def pdf_to_markdown(pdf_path: Path) -> str:
    lines = []
    with pdfplumber.open(pdf_path) as pdf:
        for i, page in enumerate(pdf.pages):
            text = page.extract_text(x_tolerance=3, y_tolerance=3) or ""
            text = text.strip()
            if not text:
                lines.append("*(diagram)*\n")
            else:
                page_lines = text.splitlines()
                if page_lines:
                    lines.append(f"## {page_lines[0]}\n")
                    for pl in page_lines[1:]:
                        pl = pl.strip()
                        if not pl:
                            continue
                        if re.match(r"^[-•·]\s", pl) or re.match(r"^\d+\.\s", pl):
                            lines.append(f"- {pl.lstrip('-•· ')}\n")
                        else:
                            lines.append(f"\n{pl}\n")
            if i < len(pdf.pages) - 1:
                lines.append("\n---\n\n")
    return "".join(lines)


# ─── XLS/XLSX → markdown ─────────────────────────────────────────────────────

def xls_to_markdown(xls_path: Path) -> str:
    parts = []
    try:
        xl = pd.ExcelFile(xls_path, engine="openpyxl" if xls_path.suffix == ".xlsx" else "xlrd")
    except Exception:
        try:
            xl = pd.ExcelFile(xls_path)
        except Exception as e:
            return f"*Could not parse spreadsheet: {e}*\n"

    for sheet in xl.sheet_names:
        try:
            df = xl.parse(sheet, header=None)
            df = df.dropna(how="all")
            if df.empty:
                continue
            parts.append(f"## {sheet}\n")
            parts.append(df.to_markdown(index=False, headers=df.iloc[0].tolist()))
            parts.append("\n\n")
        except Exception:
            parts.append(f"## {sheet}\n*(could not parse)*\n\n")

    return "".join(parts) if parts else "*Empty spreadsheet*\n"


# ─── Lesson file generators ───────────────────────────────────────────────────

FRONTMATTER_TMPL = """\
---
title: "{title}"
status: active
owner: weprintmoney
created: {today}
last_updated: {today}
---

"""


def write_frontmatter(title: str) -> str:
    return FRONTMATTER_TMPL.format(title=title, today=date.today().isoformat())


def generate_lesson_overview(
    lesson_num: int,
    topic: str,
    module: str,
    video_parts: list[dict],
    files: list[dict],
) -> str:
    padded = f"{lesson_num:02d}"
    lines = [
        f"# Lesson {padded} — {topic}\n\n",
        "## Overview\n\n",
        f"*(Overview for lesson {padded} — {topic})*\n\n",
        "---\n\n",
    ]

    if video_parts:
        lines.append("## Videos\n\n")
        lines.append("| Part | Title | Local (720p, in repo) | Original |\n")
        lines.append("|------|-------|-----------------------|----------|\n")
        for v in video_parts:
            part = v.get("part", "?")
            title = v.get("title", f"Session {lesson_num} Part {part}")
            local = f"[session-{lesson_num}-part-{part}.mp4](session-{lesson_num}-part-{part}.mp4)"
            orig_url = v.get("url", "")
            orig = f"[stream]({orig_url})" if orig_url else "—"
            lines.append(f"| {part} | {title} | {local} | {orig} |\n")
        lines.append("\n")

    if files:
        lines.append("## Files in this folder\n\n")
        lines.append("| File | Description |\n")
        lines.append("|------|-------------|\n")
        for f in files:
            lines.append(f"| `{f['name']}` | {f['desc']} |\n")
        lines.append("\n")

    return "".join(lines)


# ─── lesson-index.yaml updater ────────────────────────────────────────────────

def update_lesson_index(index_path: Path, updates: dict[int, dict]):
    """Update topic/files fields for given lesson numbers."""
    raw = index_path.read_text()
    data = yaml.safe_load(raw)

    for entry in data.get("lessons", []):
        n = int(entry.get("lesson", 0))
        if n in updates:
            u = updates[n]
            if "topic" in u:
                entry["topic"] = u["topic"]
            if "files" in u:
                entry["files"].update(u["files"])

    index_path.write_text(yaml.dump(data, default_flow_style=False, sort_keys=False, allow_unicode=True))
    print(f"  Updated lesson-index.yaml for lessons: {sorted(updates)}")


# ─── Utility ──────────────────────────────────────────────────────────────────

def to_kebab(s: str) -> str:
    s = re.sub(r"[_\s]+", "-", s.strip())
    s = re.sub(r"[^\w\-]", "", s)
    s = re.sub(r"-+", "-", s).strip("-")
    return s.lower()


def lesson_dir(modules_root: Path, lesson_num: int) -> Path:
    mod = LESSON_MODULE_MAP.get(lesson_num, "module-1")
    return modules_root / mod / f"lesson-{lesson_num:02d}"


# ─── Main per-lesson processor ────────────────────────────────────────────────

def process_lesson(
    session: requests.Session,
    base: str,
    org_id: str,
    ver: str,
    lesson_num: int,
    topics: list[tuple[list, dict]],
    modules_root: Path,
    dry_run: bool,
):
    dest = lesson_dir(modules_root, lesson_num)
    print(f"\n→ Lesson {lesson_num:02d}  ({dest.relative_to(REPO_ROOT)})")

    generated_files = []
    video_parts = []
    index_updates = {}

    for crumb, topic in topics:
        kind = classify_topic(topic)
        title = topic.get("Title", "")
        url = topic.get("Url") or ""
        print(f"   [{kind:12s}] {title[:60]}")

        if dry_run:
            continue

        dest.mkdir(parents=True, exist_ok=True)

        # ── Video: record URL, don't download (already in repo as mp4) ──
        if kind == "video":
            m = re.search(r"part\s*[-:]?\s*(\d+)", title, re.I)
            part = int(m.group(1)) if m else len(video_parts) + 1
            video_parts.append({"part": part, "title": title, "url": url})

        # ── Slides PDF ──────────────────────────────────────────────────
        elif kind == "slide":
            saved = download_topic_file(session, base, org_id, ver, topic, dest)
            if saved and saved.suffix.lower() == ".pdf":
                md_path = dest / "slides.md"
                if not md_path.exists():
                    print(f"      Converting {saved.name} → slides.md")
                    md_text = write_frontmatter(f"Lesson {lesson_num:02d} Slides") + pdf_to_markdown(saved)
                    md_path.write_text(md_text)
                generated_files.append({"name": "slides.md", "desc": f"Slide deck for Lesson {lesson_num:02d}"})
                generated_files.append({"name": saved.name, "desc": "Original slide PDF"})
                index_updates.setdefault(lesson_num, {}).setdefault("files", {})["slides"] = True
            elif saved:
                generated_files.append({"name": saved.name, "desc": title})

        # ── Spreadsheet ─────────────────────────────────────────────────
        elif kind == "spreadsheet":
            saved = download_topic_file(session, base, org_id, ver, topic, dest)
            if saved and saved.suffix.lower() in (".xls", ".xlsx"):
                stem = to_kebab(saved.stem)
                md_path = dest / f"spreadsheet-{stem}.md"
                if not md_path.exists():
                    print(f"      Converting {saved.name} → spreadsheet-{stem}.md")
                    md_text = write_frontmatter(f"Spreadsheet: {saved.name}") + xls_to_markdown(saved)
                    md_path.write_text(md_text)
                generated_files.append({"name": f"spreadsheet-{stem}.md", "desc": f"Spreadsheet: {title}"})
                generated_files.append({"name": saved.name, "desc": "Original spreadsheet"})
                index_updates.setdefault(lesson_num, {}).setdefault("files", {})["spreadsheets"] = True

        # ── Reading (PDF or external link) ──────────────────────────────
        elif kind == "reading":
            saved = download_topic_file(session, base, org_id, ver, topic, dest)
            if saved and saved.suffix.lower() == ".pdf":
                stem = to_kebab(saved.stem)
                md_path = dest / f"reading-{stem}.md"
                if not md_path.exists():
                    print(f"      Converting {saved.name} → reading-{stem}.md")
                    md_text = write_frontmatter(title) + pdf_to_markdown(saved)
                    md_path.write_text(md_text)
                generated_files.append({"name": f"reading-{stem}.md", "desc": title})
                index_updates.setdefault(lesson_num, {}).setdefault("files", {})["readings"] = True
            elif url:
                stem = to_kebab(re.sub(r"https?://.*?/", "", url)[:60])
                md_path = dest / f"reading-{stem}.md"
                if not md_path.exists():
                    md_path.write_text(write_frontmatter(title) + f"# {title}\n\n[Source]({url})\n")
                generated_files.append({"name": f"reading-{stem}.md", "desc": title})
                index_updates.setdefault(lesson_num, {}).setdefault("files", {})["readings"] = True

    # ── lesson-overview.md ──────────────────────────────────────────────
    if not dry_run:
        overview_path = dest / "lesson-overview.md"
        if not overview_path.exists():
            # Try to derive topic from crumbs or TOC module title
            topic_guess = _guess_topic(lesson_num, [t[0] for t in topics])
            mod = LESSON_MODULE_MAP.get(lesson_num, "module-1")
            overview = generate_lesson_overview(lesson_num, topic_guess, mod, video_parts, generated_files)
            overview_path.write_text(overview)
            print(f"      Wrote lesson-overview.md  (topic: {topic_guess!r})")
            if topic_guess != "(pending)":
                index_updates.setdefault(lesson_num, {})["topic"] = topic_guess

    return index_updates


def _guess_topic(lesson_num: int, crumbs: list[list]) -> str:
    seen = set()
    for crumb in crumbs:
        for part in crumb:
            part = part.strip()
            if not part:
                continue
            # Skip purely numeric or generic titles
            if re.fullmatch(r"[\d\s\-:]+", part):
                continue
            if re.search(rf"\b{lesson_num}\b", part) and len(part) < 20:
                continue
            if part.lower() in ("module 1", "module 2", "module 3", "module 4",
                                 "corporate finance", "content", "resources"):
                continue
            if part not in seen:
                seen.add(part)
                return part
    return "(pending)"


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Export Brightspace course content into repo")
    parser.add_argument("--lesson", type=int, help="Process only this lesson number")
    parser.add_argument("--modules", type=int, nargs="+", help="Process only these module numbers (e.g. --modules 2 3)")
    parser.add_argument("--dry-run", action="store_true", help="Print what would be done, no downloads")
    parser.add_argument("--toc-only", action="store_true", help="Fetch and print the TOC JSON, then exit")
    parser.add_argument("--env", default=".brightspace.env", help="Path to env file (default: .brightspace.env)")
    parser.add_argument("--course", choices=["corporate-finance", "accounting"], default="corporate-finance")
    args = parser.parse_args()

    env_path = REPO_ROOT / args.env
    cfg = load_env(env_path)
    base = cfg["D2L_BASE_URL"].rstrip("/")
    org_id = cfg["D2L_ORG_UNIT_ID"]

    modules_root = CF_MODULES if args.course == "corporate-finance" else FA_MODULES
    index_path = modules_root / "lesson-index.yaml"

    print(f"Authenticating to {base} (org unit {org_id})…")
    session = make_session(cfg)
    ver = detect_api_version(session, base, org_id)

    print("Fetching course table of contents…")
    toc = fetch_toc(session, base, org_id, ver)

    if args.toc_only:
        print(json.dumps(toc, indent=2))
        return

    # Group topics by lesson number
    by_lesson: dict[int, list[tuple[list, dict]]] = {}
    for crumb, topic in iter_topics(toc):
        n = guess_lesson_number(crumb, topic.get("Title", ""))
        if n is None:
            continue
        by_lesson.setdefault(n, []).append((crumb, topic))

    # Apply filters
    lesson_nums = sorted(by_lesson)
    if args.lesson:
        lesson_nums = [args.lesson]
    elif args.modules:
        allowed = set()
        for m in args.modules:
            allowed |= set(LESSON_MODULE_MAP[n] for n in LESSON_MODULE_MAP if LESSON_MODULE_MAP[n] == f"module-{m}")
        lesson_nums = [n for n in lesson_nums if LESSON_MODULE_MAP.get(n) in allowed]

    if not lesson_nums:
        print("No lessons matched the filter.")
        return

    print(f"\nLessons to process: {lesson_nums}")
    if args.dry_run:
        print("(dry run — no files will be written)\n")

    all_updates: dict[int, dict] = {}
    for n in lesson_nums:
        updates = process_lesson(
            session, base, org_id, ver, n, by_lesson.get(n, []),
            modules_root, args.dry_run
        )
        all_updates.update(updates)
        time.sleep(0.3)  # polite pacing

    if not args.dry_run and all_updates and index_path.exists():
        update_lesson_index(index_path, all_updates)

    print("\nDone.")


if __name__ == "__main__":
    main()
