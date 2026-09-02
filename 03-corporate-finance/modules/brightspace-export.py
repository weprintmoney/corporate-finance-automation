#!/usr/bin/env python3
"""
brightspace-export.py

Exports NYU Brightspace course content into the repo structure.
Parses each lesson's HTML page to extract slides, videos, readings,
spreadsheets, and blog links; downloads files; converts PDFs to markdown
using marker (vision-native, handles charts/equations); converts XLS to
markdown tables; generates lesson-overview.md; updates lesson-index.yaml.

─── SETUP ───────────────────────────────────────────────────────────────────
1. Log in to brightspace.nyu.edu in your browser
2. Open DevTools (F12) → Application → Cookies → brightspace.nyu.edu
3. Copy d2lSessionVal and d2lSecureSessionVal cookie values
4. Find the course org unit ID from its URL:
     brightspace.nyu.edu/d2l/home/597894  →  org unit = 597894
5. Create .brightspace.env in the repo root (gitignored):
     D2L_SESSION_VAL=<d2lSessionVal>
     D2L_SECURE_SESSION_VAL=<d2lSecureSessionVal>
     D2L_ORG_UNIT_ID=597894
     D2L_BASE_URL=https://brightspace.nyu.edu

─── USAGE ───────────────────────────────────────────────────────────────────
  python3 03-corporate-finance/modules/brightspace-export.py
  python3 03-corporate-finance/modules/brightspace-export.py --lesson 13
  python3 03-corporate-finance/modules/brightspace-export.py --modules 2 3
  python3 03-corporate-finance/modules/brightspace-export.py --dry-run
  python3 03-corporate-finance/modules/brightspace-export.py --toc-only

─── DEPENDENCIES ────────────────────────────────────────────────────────────
  pip install marker-pdf requests beautifulsoup4 pandas openpyxl pdfplumber
  brew install llama.cpp   # marker's inference backend on macOS
"""

import argparse
import re
import shutil
import sys
import time
import json
from datetime import date
from pathlib import Path
from urllib.parse import urlparse, unquote

import pandas as pd
import requests
import yaml
from bs4 import BeautifulSoup

# ─── Repo layout ─────────────────────────────────────────────────────────────

REPO_ROOT = Path(__file__).parent.parent.parent
CF_MODULES = REPO_ROOT / "03-corporate-finance" / "modules"
CF_BLOGS = REPO_ROOT / "03-corporate-finance" / "blogs" / "posts"

LESSON_MODULE_MAP = {
    **{n: "module-1" for n in range(1, 13)},
    **{n: "module-2" for n in range(13, 20)},
    **{n: "module-3" for n in range(20, 27)},
    **{n: "module-4" for n in range(27, 37)},
}

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
    # No trailing slash — NYU's D2L returns 404 with trailing slash
    url = f"{base}/d2l/api/le/1.51/{org_id}/content/toc"
    r = session.get(url, timeout=30)
    if r.status_code == 401:
        sys.exit("Authentication failed — session cookies expired. Re-export from browser.")
    r.raise_for_status()
    return r.json()


def extract_lesson_topics(toc: dict) -> dict[int, dict]:
    lessons = {}
    for mod in toc.get("Modules", []):
        mod_title = mod.get("Title", "")
        for topic in mod.get("Topics", []):
            t = topic.get("Title", "")
            m = re.search(r"(?:lesson|session)\s*(\d+)", t, re.I)
            if not m:
                continue
            n = int(m.group(1))
            lessons[n] = {
                "title": t,
                "topic_id": topic.get("TopicId"),
                "module_title": mod_title,
            }
    return lessons


# ─── Lesson HTML parser ───────────────────────────────────────────────────────

def fetch_lesson_html(session: requests.Session, base: str, org_id: str, topic_id: int) -> str:
    url = f"{base}/d2l/api/le/1.51/{org_id}/content/topics/{topic_id}/file"
    r = session.get(url, timeout=20)
    r.raise_for_status()
    return r.text


def parse_lesson_html(html: str, lesson_num: int) -> dict:
    soup = BeautifulSoup(html, "html.parser")
    result = {
        "topic": "",
        "overview": "",
        "learning_objectives": [],
        "slides_url": None,
        "videos": [],
        "readings": [],
        "spreadsheets": [],
        "datasets": [],
        "blogs": [],
        "webcasts": [],
        "project_questions": [],
    }

    h2 = soup.find("h2")
    if h2:
        result["topic"] = h2.get_text(strip=True)

    for h in soup.find_all(["h2", "h3"]):
        if "overview" in h.get_text().lower():
            p = h.find_next_sibling("p")
            if p:
                result["overview"] = p.get_text(strip=True)
            ul = h.find_next("ul")
            if ul:
                result["learning_objectives"] = [li.get_text(strip=True) for li in ul.find_all("li")]
            break

    for h in soup.find_all(["h3", "h4"]):
        if "cumulative project" in h.get_text().lower() or "questions for this lesson" in h.get_text().lower():
            ul = h.find_next("ul")
            if ul:
                result["project_questions"] = [li.get_text(strip=True) for li in ul.find_all("li")]
            break
    if not result["project_questions"]:
        for card in soup.find_all("div", class_="card"):
            h4 = card.find("h4")
            if h4 and "questions" in h4.get_text().lower():
                ul = card.find("ul")
                if ul:
                    result["project_questions"] = [li.get_text(strip=True) for li in ul.find_all("li")]

    current_section = ""
    for tag in soup.find_all(["h3", "h4", "a"]):
        if tag.name in ("h3", "h4"):
            current_section = tag.get_text(strip=True).lower()
            continue

        href = tag.get("href", "")
        if not href or href.startswith("#"):
            continue

        text = tag.get_text(strip=True)
        href_lower = href.lower()

        if "slides.pdf" in href_lower or ("slides" in href_lower and ".pdf" in href_lower):
            result["slides_url"] = href
            continue

        if "stream.nyu.edu" in href:
            m = re.search(r"part\s*(\d+)", text, re.I)
            part = int(m.group(1)) if m else len(result["videos"]) + 1
            result["videos"].append({"url": href, "title": text, "part": part})
            continue

        if ".pdf?iscourseFile=true" in href_lower or (
            ".pdf" in href_lower and "enforced" in href_lower and "slides" not in href_lower
        ):
            result["readings"].append({"url": href, "title": text})
            continue

        if (".xls?iscourseFile=true" in href_lower or ".xlsx?iscourseFile=true" in href_lower
                or ((".xls" in href_lower or ".xlsx" in href_lower) and "enforced" in href_lower)):
            bucket = "datasets" if "dataset" in current_section else "spreadsheets"
            result[bucket].append({"url": href, "title": text})
            continue

        if "blogspot.com" in href or ("damodaran" in href and "blog" in href):
            result["blogs"].append({"url": href, "title": text})
            continue

        if "youtube.com" in href or "youtu.be" in href:
            result["webcasts"].append({"url": href, "title": text})

    return result


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
    fname = m.group(1).strip() if m else unquote(urlparse(url).path.split("/")[-1].split("?")[0]) or "file"

    dest.mkdir(parents=True, exist_ok=True)
    out = dest / fname
    if out.exists():
        return out  # already downloaded
    with open(out, "wb") as f:
        for chunk in r.iter_content(8192):
            f.write(chunk)
    return out


# ─── PDF → markdown (marker, vision-native) ───────────────────────────────────

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
    """Convert PDF to markdown using marker. Saves extracted images to images_dir if provided."""
    from marker.output import text_from_rendered
    converter = _get_marker_converter()
    rendered = converter(str(pdf_path))
    text, _, images = text_from_rendered(rendered)

    # Save extracted images next to the markdown
    if images and images_dir:
        images_dir.mkdir(parents=True, exist_ok=True)
        for img_name, img in images.items():
            try:
                img.save(images_dir / img_name)
            except Exception:
                pass
        # Update image references in text to point to images_dir
        dir_name = images_dir.name
        text = re.sub(r"!\[([^\]]*)\]\(([^)]+)\)", lambda m: f"![{m.group(1)}]({dir_name}/{m.group(2)})", text)

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


def blog_slug_from_url(url: str) -> str:
    path = urlparse(url).path
    return path.rstrip("/").split("/")[-1].replace(".html", "")


def find_local_blog(slug: str, blogs_dir: Path) -> Path | None:
    if not blogs_dir.exists():
        return None
    for f in blogs_dir.glob("*.md"):
        if slug in f.name:
            return f
    return None


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

def generate_lesson_overview(lesson_num: int, parsed: dict, files_written: list[dict]) -> str:
    n = f"{lesson_num:02d}"
    topic = parsed["topic"] or f"Lesson {n}"
    lines = [f"# Lesson {n} — {topic}\n\n"]

    if parsed["overview"]:
        lines.append("## Overview\n\n")
        lines.append(f"{parsed['overview']}\n\n")
        if parsed["learning_objectives"]:
            lines.append("**Learning objectives:**\n")
            for obj in parsed["learning_objectives"]:
                lines.append(f"- {obj}\n")
            lines.append("\n")
        lines.append("---\n\n")

    if parsed["videos"]:
        lines.append("## Videos\n\n")
        lines.append("| Part | Title | Local (720p, in repo) | Original (Kaltura) |\n")
        lines.append("|------|-------|-----------------------|--------------------|\n")
        for v in sorted(parsed["videos"], key=lambda x: x["part"]):
            p = v["part"]
            local = f"[session-{lesson_num}-part-{p}.mp4](session-{lesson_num}-part-{p}.mp4)"
            lines.append(f"| {p} | {v['title']} | {local} | [stream.nyu.edu]({v['url']}) |\n")
        parts = [v["part"] for v in sorted(parsed["videos"], key=lambda x: x["part"])]
        tr = " · ".join(f"[pt {p}](session-{lesson_num}-part-{p}.md)" for p in parts)
        lines.append(f"\n> **Transcripts:** cleaned prose available — {tr}.\n\n")
        lines.append("---\n\n")

    if parsed["project_questions"]:
        lines.append("## Project Questions\n\n")
        for q in parsed["project_questions"]:
            lines.append(f"- {q}\n")
        lines.append("\n---\n\n")

    if files_written:
        lines.append("## Files in this folder\n\n")
        lines.append("| File | Description |\n")
        lines.append("|------|-------------|\n")
        for f in files_written:
            lines.append(f"| `{f['name']}` | {f['desc']} |\n")
        lines.append("\n")

    return frontmatter(f"Lesson {n} — {topic}") + "".join(lines)


# ─── lesson-index.yaml updater ────────────────────────────────────────────────

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
    index_path.write_text(yaml.dump(data, default_flow_style=False, sort_keys=False, allow_unicode=True))


# ─── Per-lesson processor ─────────────────────────────────────────────────────

def process_lesson(
    session: requests.Session,
    base: str,
    org_id: str,
    lesson_num: int,
    lesson_meta: dict,
    modules_root: Path,
    blogs_dir: Path,
    dry_run: bool,
    reconvert_slides: bool = False,
) -> dict:
    mod = LESSON_MODULE_MAP.get(lesson_num, "module-1")
    dest = modules_root / mod / f"lesson-{lesson_num:02d}"

    print(f"\n→ Lesson {lesson_num:02d} — {lesson_meta['title']}")

    html = fetch_lesson_html(session, base, org_id, lesson_meta["topic_id"])
    parsed = parse_lesson_html(html, lesson_num)

    # TOC title is authoritative (HTML h2 may have copy-paste errors)
    toc_topic = lesson_meta["title"].split(":", 1)[-1].strip()
    topic = toc_topic or parsed["topic"] or f"Lesson {lesson_num:02d}"
    parsed["topic"] = topic

    print(f"   topic: {topic}")
    print(f"   slides: {'yes' if parsed['slides_url'] else 'no'}  "
          f"videos: {len(parsed['videos'])}  readings: {len(parsed['readings'])}  "
          f"spreadsheets: {len(parsed['spreadsheets'])+len(parsed['datasets'])}  "
          f"blogs: {len(parsed['blogs'])}")

    if dry_run:
        return {}

    dest.mkdir(parents=True, exist_ok=True)
    files_written = []
    index_files = {}

    # ── Slides PDF → slides.md (marker) ────────────────────────────────────
    slides_pdf = dest / "slides.pdf"
    slides_md = dest / "slides.md"
    if parsed["slides_url"] and (not slides_md.exists() or reconvert_slides):
        if not slides_pdf.exists():
            saved = download_url(session, parsed["slides_url"], dest)
            if saved and saved.name != "slides.pdf":
                saved.rename(slides_pdf)
        if slides_pdf.exists():
            print(f"      Converting slides.pdf → slides.md (marker…)")
            images_dir = dest / "slides-images"
            md_text = frontmatter(f"Lesson {lesson_num:02d} Slides") + pdf_to_markdown(slides_pdf, images_dir)
            # Remove empty images dir if nothing was extracted
            if images_dir.exists() and not any(images_dir.iterdir()):
                images_dir.rmdir()
            slides_md.write_text(md_text)
            print(f"      Done.")
    if slides_pdf.exists():
        files_written.append({"name": "slides.pdf", "desc": f"Slide deck for Lesson {lesson_num:02d}"})
    if slides_md.exists():
        files_written.append({"name": "slides.md", "desc": "Slide deck (markdown, marker-converted)"})
        index_files["slides"] = True

    # ── Reading PDFs → reading-*.md (marker) ───────────────────────────────
    for r_info in parsed["readings"]:
        url, title = r_info["url"], r_info["title"]
        slug = stem_from_url(url)
        slug = re.sub(r"^acf[_-]?[sl]\d+[_-](readings?[_-])?", "", slug)
        md_path = dest / f"reading-{slug}.md"
        if not md_path.exists():
            # Use existing PDF if present, otherwise download
            saved = download_url(session, url, dest)
            if saved and saved.suffix.lower() == ".pdf":
                target = dest / f"{slug}.pdf"
                if saved != target:
                    saved.rename(target)
                    saved = target
                print(f"      Converting {saved.name} → reading-{slug}.md (marker…)")
                images_dir = dest / f"reading-{slug}-images"
                md_text = frontmatter(title) + pdf_to_markdown(saved, images_dir)
                if images_dir.exists() and not any(images_dir.iterdir()):
                    images_dir.rmdir()
                md_path.write_text(md_text)
                files_written.append({"name": f"reading-{slug}.md", "desc": title})
                index_files["readings"] = True

    # ── Spreadsheets → spreadsheet-*.md ────────────────────────────────────
    for xls_info in parsed["spreadsheets"] + parsed["datasets"]:
        url, title = xls_info["url"], xls_info["title"]
        slug = stem_from_url(url)
        slug = re.sub(r"^acf[_-]?[sl]\d+[_-](spreadsheet[_-]|dataset[_-])?", "", slug)
        md_path = dest / f"spreadsheet-{slug}.md"
        if not md_path.exists():
            saved = download_url(session, url, dest)
            if saved and saved.suffix.lower() in (".xls", ".xlsx"):
                target = dest / f"{slug}{saved.suffix.lower()}"
                if saved != target:
                    saved.rename(target)
                    saved = target
                print(f"      Converting {saved.name} → spreadsheet-{slug}.md")
                md_text = frontmatter(f"Spreadsheet: {title}") + xls_to_markdown(saved)
                md_path.write_text(md_text)
                files_written.append({"name": saved.name, "desc": f"Raw spreadsheet: {title}"})
                files_written.append({"name": f"spreadsheet-{slug}.md", "desc": title})
                index_files["spreadsheets"] = True

    # ── Blog posts ──────────────────────────────────────────────────────────
    for b_info in parsed["blogs"]:
        url, title = b_info["url"], b_info["title"]
        slug = blog_slug_from_url(url)
        kebab_title = to_kebab(title)
        dest_blog = dest / f"blog-{kebab_title}.md"
        if not dest_blog.exists():
            local = find_local_blog(slug, blogs_dir)
            if local:
                shutil.copy(local, dest_blog)
                print(f"      Copied local blog: {local.name}")
            else:
                dest_blog.write_text(
                    frontmatter(title)
                    + f"# {title}\n\n_Source: [{url}]({url})_\n\n"
                    + "*(Full text not available locally — see link above)*\n"
                )
                print(f"      Blog stub: {dest_blog.name}")
            files_written.append({"name": dest_blog.name, "desc": f"Blog: {title}"})
            index_files["blogs"] = True

    # ── lesson-overview.md ──────────────────────────────────────────────────
    overview_path = dest / "lesson-overview.md"
    if not overview_path.exists():
        overview_path.write_text(generate_lesson_overview(lesson_num, parsed, files_written))
        print(f"      Wrote lesson-overview.md")

    return {lesson_num: {"topic": topic, "files": index_files}}


# ─── CLI ─────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Export Brightspace course content into repo")
    parser.add_argument("--lesson", type=int, help="Process only this lesson number")
    parser.add_argument("--modules", type=int, nargs="+", help="Process only these module numbers")
    parser.add_argument("--dry-run", action="store_true", help="Print plan without downloading")
    parser.add_argument("--toc-only", action="store_true", help="Print TOC JSON and exit")
    parser.add_argument("--force", action="store_true", help="Re-process even if lesson-overview.md exists")
    parser.add_argument("--reconvert-slides", action="store_true",
                        help="Re-convert slides.pdf → slides.md even if slides.md already exists (e.g. to upgrade from pdfplumber to marker)")
    parser.add_argument("--env", default=".brightspace.env")
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

    all_lessons = extract_lesson_topics(toc)
    print(f"Found {len(all_lessons)} numbered lessons: {sorted(all_lessons)}")

    lesson_nums = sorted(all_lessons)
    if args.lesson:
        lesson_nums = [args.lesson] if args.lesson in all_lessons else []
    elif args.modules:
        allowed = {f"module-{m}" for m in args.modules}
        lesson_nums = [n for n in lesson_nums if LESSON_MODULE_MAP.get(n) in allowed]

    if not args.force:
        before = len(lesson_nums)
        lesson_nums = [
            n for n in lesson_nums
            if not (CF_MODULES / LESSON_MODULE_MAP.get(n, "module-1") / f"lesson-{n:02d}" / "lesson-overview.md").exists()
        ]
        skipped = before - len(lesson_nums)
        if skipped:
            print(f"Skipping {skipped} lessons that already have lesson-overview.md (use --force to re-run)")

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
            CF_MODULES,
            CF_BLOGS,
            args.dry_run,
            reconvert_slides=args.reconvert_slides,
        )
        all_updates.update(updates)
        time.sleep(0.3)

    index_path = CF_MODULES / "lesson-index.yaml"
    if not args.dry_run and all_updates and index_path.exists():
        update_lesson_index(index_path, all_updates)
        print(f"\nUpdated lesson-index.yaml for {len(all_updates)} lessons.")

    print("\nDone.")


if __name__ == "__main__":
    main()
