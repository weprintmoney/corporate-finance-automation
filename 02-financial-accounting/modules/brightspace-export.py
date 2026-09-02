#!/usr/bin/env python3
"""
brightspace-export.py  (Financial Accounting edition)

Exports NYU Brightspace Financial Accounting course content into repo.

TOC structure for this course differs from Corporate Finance:
  - Each LESSON is a D2L Module  (e.g. "Lesson 2: The Balance Sheet")
  - Sub-topics within each module: Pre-Quiz, Video(s), Readings, Exercise, Self-Assessment
  - We fetch each sub-topic HTML page and classify by title keyword

─── SETUP ───────────────────────────────────────────────────────────────────
1. Log in to brightspace.nyu.edu in your browser
2. Open DevTools → Application → Cookies → brightspace.nyu.edu
3. Copy d2lSessionVal and d2lSecureSessionVal values
4. Create .brightspace-accounting.env in the repo root (gitignored):
     D2L_SESSION_VAL=<value>
     D2L_SECURE_SESSION_VAL=<value>
     D2L_ORG_UNIT_ID=597897
     D2L_BASE_URL=https://brightspace.nyu.edu

─── USAGE ───────────────────────────────────────────────────────────────────
  python3 02-financial-accounting/modules/brightspace-export.py
  python3 02-financial-accounting/modules/brightspace-export.py --lesson 3
  python3 02-financial-accounting/modules/brightspace-export.py --dry-run
  python3 02-financial-accounting/modules/brightspace-export.py --toc-only
  python3 02-financial-accounting/modules/brightspace-export.py --reconvert-slides

─── DEPENDENCIES ────────────────────────────────────────────────────────────
  pip install marker-pdf requests beautifulsoup4 pandas openpyxl pdfplumber
  brew install llama.cpp   # marker's inference backend on macOS
"""

import argparse
import json
import re
import sys
import time
from datetime import date
from pathlib import Path
from urllib.parse import urlparse, unquote

import pandas as pd
import requests
import yaml
from bs4 import BeautifulSoup

# ─── Repo layout ─────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).parent.parent.parent
FA_MODULES = REPO_ROOT / "02-financial-accounting" / "modules"

# All 10 lessons are in a single module for this course
LESSON_MODULE_MAP = {n: "module-1" for n in range(1, 11)}

# ─── Env / auth ──────────────────────────────────────────────────────────────

def load_env(env_file: Path) -> dict:
    if not env_file.exists():
        sys.exit(
            f"Missing {env_file}\n"
            "Create it with D2L_SESSION_VAL, D2L_SECURE_SESSION_VAL, "
            "D2L_ORG_UNIT_ID, D2L_BASE_URL — see script header."
        )
    cfg = {}
    for line in env_file.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, _, v = line.partition("=")
            cfg[k.strip()] = v.strip()
    for k in ["D2L_SESSION_VAL", "D2L_SECURE_SESSION_VAL", "D2L_ORG_UNIT_ID", "D2L_BASE_URL"]:
        if not cfg.get(k):
            sys.exit(f"Missing {k} in {env_file}")
    return cfg


def make_session(cfg: dict) -> requests.Session:
    domain = cfg["D2L_BASE_URL"].split("//")[-1].split("/")[0]
    s = requests.Session()
    s.cookies.set("d2lSessionVal", cfg["D2L_SESSION_VAL"], domain=domain)
    s.cookies.set("d2lSecureSessionVal", cfg["D2L_SECURE_SESSION_VAL"], domain=domain)
    s.headers["User-Agent"] = "Mozilla/5.0"
    return s


# ─── D2L content TOC ─────────────────────────────────────────────────────────

def fetch_toc(session: requests.Session, base: str, org_id: str) -> dict:
    url = f"{base}/d2l/api/le/1.51/{org_id}/content/toc"
    r = session.get(url, timeout=30)
    if r.status_code == 401:
        sys.exit("Authentication failed — session cookies expired. Re-export from browser.")
    r.raise_for_status()
    return r.json()


def extract_lessons(toc: dict) -> dict[int, dict]:
    """Return {lesson_num: {title, module_id, topics: [{topic_id, title, role}]}}"""
    lessons = {}
    for mod in toc.get("Modules", []):
        title = mod.get("Title", "")
        m = re.search(r"lesson\s*(\d+)", title, re.I)
        if not m:
            continue
        n = int(m.group(1))
        topics = []
        for t in mod.get("Topics", []):
            t_title = t.get("Title", "")
            role = _classify_topic(t_title)
            if role:
                topics.append({
                    "topic_id": t.get("TopicId"),
                    "title": t_title,
                    "role": role,
                })
        lessons[n] = {
            "title": title,
            "module_id": mod.get("ModuleId"),
            "topic": title.split(":", 1)[-1].strip(),
            "topics": topics,
        }
    return lessons


def _classify_topic(title: str) -> str | None:
    t = title.lower()
    if "video" in t or "webcast" in t:
        return "video"
    if "reading" in t:
        return "reading"
    if "exercise" in t or "worksheet" in t:
        return "exercise"
    # skip pre-quiz, self-assessment, demo (no downloadable content worth exporting)
    return None


# ─── HTML fetching ────────────────────────────────────────────────────────────

def fetch_topic_html(session: requests.Session, base: str, org_id: str, topic_id: int) -> str:
    url = f"{base}/d2l/api/le/1.51/{org_id}/content/topics/{topic_id}/file"
    r = session.get(url, timeout=20)
    r.raise_for_status()
    return r.text


def extract_links_from_html(html: str) -> list[dict]:
    """Extract all hrefs with their link text from a Brightspace topic page."""
    soup = BeautifulSoup(html, "html.parser")
    links = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.startswith("#"):
            continue
        links.append({"url": href, "title": a.get_text(strip=True)})
    return links


def extract_overview_text(html: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    # Try to find overview paragraph
    for tag in soup.find_all(["p", "div"]):
        text = tag.get_text(strip=True)
        if len(text) > 80:
            return text
    return ""


# ─── File download ────────────────────────────────────────────────────────────

def download_url(session: requests.Session, url: str, dest: Path) -> Path | None:
    try:
        r = session.get(url, timeout=60, stream=True)
        r.raise_for_status()
    except Exception as e:
        print(f"      WARN: download failed for {url[:60]}: {e}")
        return None

    cd = r.headers.get("Content-Disposition", "")
    m = re.search(r'filename="?([^";\r\n]+)"?', cd)
    fname = (m.group(1).strip() if m
             else unquote(urlparse(url).path.split("/")[-1].split("?")[0]) or "file")

    dest.mkdir(parents=True, exist_ok=True)
    out = dest / fname
    if out.exists():
        return out
    with open(out, "wb") as f:
        for chunk in r.iter_content(8192):
            f.write(chunk)
    return out


# ─── PDF → markdown (marker, vision-native) ──────────────────────────────────

_marker_converter = None


def _get_marker_converter():
    global _marker_converter
    if _marker_converter is None:
        print("      Loading marker models (one-time)…")
        from marker.converters.pdf import PdfConverter
        from marker.models import create_model_dict
        _marker_converter = PdfConverter(artifact_dict=create_model_dict())
    return _marker_converter


def pdf_to_markdown(pdf_path: Path, images_dir: Path | None = None) -> str:
    from marker.output import text_from_rendered
    converter = _get_marker_converter()
    rendered = converter(str(pdf_path))
    text, _, images = text_from_rendered(rendered)
    if images and images_dir:
        images_dir.mkdir(parents=True, exist_ok=True)
        for img_name, img in images.items():
            try:
                img.save(images_dir / img_name)
            except Exception:
                pass
        dir_name = images_dir.name
        text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)",
                      lambda m: f"![{m.group(1)}]({dir_name}/{m.group(2)})", text)
    return text


# ─── XLS/XLSX → markdown ─────────────────────────────────────────────────────

def xls_to_markdown(xls_path: Path) -> str:
    engine = "openpyxl" if xls_path.suffix.lower() == ".xlsx" else "xlrd"
    parts = []
    try:
        xl = pd.ExcelFile(xls_path, engine=engine)
    except Exception as e:
        return f"*Could not parse: {e}*\n"
    for sheet in xl.sheet_names:
        try:
            df = xl.parse(sheet, header=None).dropna(how="all")
            if df.empty:
                continue
            parts.append(f"## {sheet}\n{df.to_markdown(index=False)}\n")
        except Exception:
            parts.append(f"## {sheet}\n*(could not parse)*\n")
    return "\n".join(parts) if parts else "*Empty spreadsheet*\n"


# ─── Naming helpers ───────────────────────────────────────────────────────────

def to_kebab(s: str) -> str:
    s = re.sub(r"[_\s]+", "-", s.strip())
    s = re.sub(r"[^\w\-]", "", s)
    return re.sub(r"-+", "-", s).strip("-").lower()


def stem_from_url(url: str) -> str:
    path = unquote(urlparse(url).path)
    fname = path.split("/")[-1].split("?")[0]
    return to_kebab(re.sub(r"\.[^.]+$", "", fname))


# Brightspace serves some files under opaque UUID names; map to meaningful slugs
SLUG_ALIASES = {"fae19475-b538-441b-ab15-0a311f161ebb": "apple-annual-report-2015"}


# ─── Frontmatter ─────────────────────────────────────────────────────────────

FRONTMATTER = """\
---
title: "{title}"
status: active
owner: weprintmoney
created: {today}
last_updated: {today}
---

"""


def frontmatter(title: str) -> str:
    return FRONTMATTER.format(title=title, today=date.today().isoformat())


# ─── Lesson overview generator ────────────────────────────────────────────────

def generate_lesson_overview(lesson_num: int, topic: str, video_links: list[dict],
                             files_written: list[dict]) -> str:
    n = f"{lesson_num:02d}"
    lines = [f"# Lesson {n} — {topic}\n\n"]

    if video_links:
        lines.append("## Videos\n\n")
        lines.append("| Part | Title | Stream link |\n")
        lines.append("|------|-------|-------------|\n")
        for i, v in enumerate(video_links, 1):
            lines.append(f"| {i} | {v['title']} | [stream.nyu.edu]({v['url']}) |\n")
        lines.append("\n---\n\n")

    if files_written:
        lines.append("## Files in this folder\n\n")
        lines.append("| File | Description |\n")
        lines.append("|------|-------------|\n")
        for f in files_written:
            lines.append(f"| `{f['name']}` | {f['desc']} |\n")
        lines.append("\n")

    return frontmatter(f"Lesson {n} — {topic}") + "".join(lines)


# ─── lesson-index.yaml ────────────────────────────────────────────────────────

def init_lesson_index(index_path: Path, lessons: dict[int, dict]):
    entries = []
    for n in sorted(lessons):
        entries.append({
            "lesson": n,
            "module": "module-1",
            "folder": f"module-1/lesson-{n:02d}",
            "topic": lessons[n]["topic"],
            "files": {
                "readings": False,
                "exercises": False,
                "transcripts": False,
            },
        })
    index_path.write_text(
        yaml.dump({"lessons": entries}, default_flow_style=False,
                  sort_keys=False, allow_unicode=True)
    )


def update_lesson_index(index_path: Path, updates: dict[int, dict]):
    data = yaml.safe_load(index_path.read_text())
    for entry in data.get("lessons", []):
        n = int(entry.get("lesson", 0))
        if n in updates:
            u = updates[n]
            if u.get("topic"):
                entry["topic"] = u["topic"]
            if "files" in u:
                entry["files"].update(u["files"])
    index_path.write_text(
        yaml.dump(data, default_flow_style=False, sort_keys=False, allow_unicode=True)
    )


# ─── Per-lesson processor ─────────────────────────────────────────────────────

def process_lesson(
    session: requests.Session,
    base: str,
    org_id: str,
    lesson_num: int,
    lesson_meta: dict,
    modules_root: Path,
    dry_run: bool,
    reconvert_slides: bool = False,
) -> dict:
    dest = modules_root / "module-1" / f"lesson-{lesson_num:02d}"
    topic = lesson_meta["topic"]

    print(f"\n→ Lesson {lesson_num:02d} — {topic}")

    video_links = []
    files_written = []
    index_files = {}

    for sub in lesson_meta["topics"]:
        role = sub["role"]
        topic_id = sub["topic_id"]
        sub_title = sub["title"]

        try:
            html = fetch_topic_html(session, base, org_id, topic_id)
        except Exception as e:
            print(f"   WARN: could not fetch topic {topic_id} ({sub_title}): {e}")
            continue

        links = extract_links_from_html(html)

        if role == "video":
            for lnk in links:
                if "stream.nyu.edu" in lnk["url"]:
                    video_links.append(lnk)

        elif role in ("reading", "exercise"):
            if dry_run:
                for lnk in links:
                    ext = lnk["url"].lower().split("?")[0].split(".")[-1]
                    if ext in ("pdf", "xls", "xlsx"):
                        print(f"   [{role}] {lnk['title']} → .{ext}")
                continue

            for lnk in links:
                url = lnk["url"]
                ext = url.lower().split("?")[0].split(".")[-1]

                if ext == "pdf":
                    saved = download_url(session, url, dest)
                    if not saved:
                        continue
                    # Determine output filename
                    prefix = "reading" if role == "reading" else "exercise"
                    slug = SLUG_ALIASES.get(stem_from_url(url), stem_from_url(url))
                    target = dest / f"{slug}.pdf"
                    if saved != target:
                        saved.rename(target)
                        saved = target
                    md_path = dest / f"{prefix}-{slug}.md"
                    if not md_path.exists() or (reconvert_slides and role == "reading"):
                        print(f"      Converting {saved.name} → {md_path.name} (marker…)")
                        images_dir = dest / f"{md_path.stem}-images"
                        md_text = frontmatter(lnk["title"]) + pdf_to_markdown(saved, images_dir)
                        if images_dir.exists() and not any(images_dir.iterdir()):
                            images_dir.rmdir()
                        md_path.write_text(md_text)
                    files_written.append({"name": saved.name, "desc": lnk["title"]})
                    files_written.append({"name": md_path.name,
                                          "desc": f"{role.capitalize()}: {lnk['title']}"})
                    index_files["readings" if role == "reading" else "exercises"] = True

                elif ext in ("xls", "xlsx"):
                    saved = download_url(session, url, dest)
                    if not saved:
                        continue
                    slug = stem_from_url(url)
                    target = dest / f"{slug}{saved.suffix.lower()}"
                    if saved != target:
                        saved.rename(target)
                        saved = target
                    md_path = dest / f"spreadsheet-{slug}.md"
                    if not md_path.exists():
                        print(f"      Converting {saved.name} → spreadsheet-{slug}.md")
                        md_text = frontmatter(f"Spreadsheet: {lnk['title']}") + xls_to_markdown(saved)
                        md_path.write_text(md_text)
                    files_written.append({"name": saved.name, "desc": lnk["title"]})
                    files_written.append({"name": md_path.name, "desc": lnk["title"]})
                    index_files["exercises"] = True

    if dry_run:
        print(f"   videos: {len(video_links)}  sub-topics: {len(lesson_meta['topics'])}")
        return {}

    dest.mkdir(parents=True, exist_ok=True)

    overview_path = dest / "lesson-overview.md"
    if not overview_path.exists():
        overview_path.write_text(
            generate_lesson_overview(lesson_num, topic, video_links, files_written)
        )
        print(f"      Wrote lesson-overview.md")

    return {lesson_num: {"topic": topic, "files": index_files}}


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Export Brightspace Financial Accounting content")
    parser.add_argument("--lesson", type=int, help="Process only this lesson number")
    parser.add_argument("--dry-run", action="store_true", help="Print plan without downloading")
    parser.add_argument("--toc-only", action="store_true", help="Print TOC JSON and exit")
    parser.add_argument("--force", action="store_true",
                        help="Re-process even if lesson-overview.md exists")
    parser.add_argument("--reconvert-slides", action="store_true",
                        help="Re-convert reading PDFs even if .md already exists")
    parser.add_argument("--env", default=".brightspace-accounting.env")
    args = parser.parse_args()

    env_path = REPO_ROOT / args.env
    cfg = load_env(env_path)
    base = cfg["D2L_BASE_URL"].rstrip("/")
    org_id = cfg["D2L_ORG_UNIT_ID"]

    print(f"Authenticating to {base} (org unit {org_id})…")
    session = make_session(cfg)

    print("Fetching course table of contents…")
    toc = fetch_toc(session, base, org_id)

    if args.toc_only:
        print(json.dumps(toc, indent=2))
        return

    all_lessons = extract_lessons(toc)
    print(f"Found {len(all_lessons)} lessons: {sorted(all_lessons)}")

    lesson_nums = sorted(all_lessons)
    if args.lesson:
        lesson_nums = [args.lesson] if args.lesson in all_lessons else []

    # Init lesson-index.yaml if it doesn't exist
    index_path = FA_MODULES / "lesson-index.yaml"
    if not index_path.exists():
        FA_MODULES.mkdir(parents=True, exist_ok=True)
        init_lesson_index(index_path, all_lessons)
        print(f"Created lesson-index.yaml")

    if not args.force:
        before = len(lesson_nums)
        lesson_nums = [
            n for n in lesson_nums
            if not (FA_MODULES / "module-1" / f"lesson-{n:02d}" / "lesson-overview.md").exists()
        ]
        skipped = before - len(lesson_nums)
        if skipped:
            print(f"Skipping {skipped} lessons already exported (use --force to re-run)")

    if not lesson_nums:
        print("Nothing to process.")
        return

    print(f"Processing lessons: {lesson_nums}")
    if args.dry_run:
        print("(dry run — no files will be written)\n")

    all_updates: dict[int, dict] = {}
    for n in lesson_nums:
        updates = process_lesson(
            session, base, org_id, n,
            all_lessons[n],
            FA_MODULES,
            args.dry_run,
            reconvert_slides=args.reconvert_slides,
        )
        all_updates.update(updates)
        time.sleep(0.3)

    if not args.dry_run and all_updates and index_path.exists():
        update_lesson_index(index_path, all_updates)
        print(f"\nUpdated lesson-index.yaml for {len(all_updates)} lessons.")

    print("\nDone.")


if __name__ == "__main__":
    main()
