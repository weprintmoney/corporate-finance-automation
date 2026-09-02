#!/usr/bin/env python3
"""
Archive transcripts from the Aswath Damodaran on Valuation YouTube channel to
03-corporate-finance/03-6-youtube/, one markdown file per video, organized by
upload year, with an index.yaml mapping video id -> file.

Requires: yt-dlp (CLI on PATH), pyyaml.
Run: python3 scripts/fetch-youtube-transcripts.py [--limit N] [--sleep SECS]

Resumable: videos already in index.yaml are skipped. Videos with no captions
yet are retried on later runs while they are < 21 days old (auto-captions
usually appear within days of upload).

Note: YouTube throttles bulk caption fetching (bot-check errors mentioning
visitor_data / "sign in to confirm"). On a rate-block the script saves
progress, cools down (10/20/40/60 min, escalating), and retries; it only
aborts if still blocked after the full ladder, or after 8 consecutive
non-rate-limit failures.
"""

import argparse
import glob
import html
import json
import os
import random
import re
import subprocess
import sys
import tempfile
import time
from datetime import date, datetime, timezone

import yaml

CHANNEL_URL = "https://www.youtube.com/@AswathDamodaranonValuation/videos"
OUT_DIR = "03-corporate-finance/03-6-youtube"
INDEX_PATH = os.path.join(OUT_DIR, "index.yaml")
OWNER = "weprintmoney"
RETRY_NO_CAPTION_DAYS = 21
MAX_CONSECUTIVE_FAILURES = 8
# YouTube bot-check / throttling signatures in yt-dlp errors
RATE_BLOCK_PAT = re.compile(r"429|too many request|sign in to confirm|not a bot|visitor_data|po_token", re.I)
# Escalating waits when rate-blocked: 10, 20, 40, 60 minutes
COOLDOWNS = [600, 1200, 2400, 3600]


def run(cmd, timeout=180):
    return subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)


def list_channel_videos():
    print("Enumerating channel videos...")
    proc = run(
        ["yt-dlp", "--flat-playlist", "--print", "%(id)s\t%(title)s", CHANNEL_URL],
        timeout=600,
    )
    if proc.returncode != 0:
        sys.exit(f"Channel enumeration failed:\n{proc.stderr[-2000:]}")
    videos = []
    for line in proc.stdout.splitlines():
        vid, _, title = line.partition("\t")
        if vid.strip():
            videos.append({"id": vid.strip(), "title": title.strip()})
    print(f"  {len(videos)} videos on channel")
    return videos


def load_index():
    if not os.path.exists(INDEX_PATH):
        return {"generated": None, "videos": []}
    with open(INDEX_PATH) as f:
        return yaml.safe_load(f) or {"generated": None, "videos": []}


def save_index(index):
    index["generated"] = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    index["videos"].sort(key=lambda v: (v.get("upload_date") or "0000-00-00", v["id"]))
    os.makedirs(OUT_DIR, exist_ok=True)
    with open(INDEX_PATH, "w") as f:
        yaml.safe_dump(index, f, allow_unicode=True, sort_keys=False, width=1000)


def slugify(title, max_len=70):
    slug = title.lower()
    slug = re.sub(r"['’]", "", slug)
    slug = re.sub(r"[^a-z0-9]+", "-", slug).strip("-")
    if len(slug) > max_len:
        slug = slug[:max_len].rsplit("-", 1)[0]
    return slug or "video"


def parse_vtt(path):
    """Parse a VTT file into (start_seconds, text) lines, deduping the rolling
    repeats that YouTube auto-captions produce."""
    cue_time = re.compile(r"(\d+):(\d{2}):(\d{2})\.(\d{3})\s+-->")
    lines, prev = [], None
    start = 0.0
    with open(path, encoding="utf-8") as f:
        for raw in f:
            raw = raw.strip()
            m = cue_time.match(raw)
            if m:
                h, mnt, s, ms = (int(g) for g in m.groups())
                start = h * 3600 + mnt * 60 + s + ms / 1000
                continue
            if not raw or raw == "WEBVTT" or raw.startswith(("Kind:", "Language:", "NOTE")):
                continue
            text = re.sub(r"<[^>]+>", "", raw)
            text = html.unescape(text).strip()
            if not text or re.fullmatch(r"\[(Music|Applause|Laughter)\]", text, re.I):
                continue
            if text != prev:
                lines.append((start, text))
                prev = text
    return lines


def lines_to_paragraphs(lines, gap=6.0, max_words=150):
    paragraphs, current, words, last_start = [], [], 0, None
    for start, text in lines:
        if current and (words >= max_words or (last_start is not None and start - last_start > gap)):
            paragraphs.append(" ".join(current))
            current, words = [], 0
        current.append(text)
        words += len(text.split())
        last_start = start
    if current:
        paragraphs.append(" ".join(current))
    return paragraphs


def fmt_duration(seconds):
    if not seconds:
        return "unknown"
    seconds = int(seconds)
    h, rem = divmod(seconds, 3600)
    m, s = divmod(rem, 60)
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m}:{s:02d}"


def fetch_video(video_id, tmpdir):
    """Download info.json + English captions for one video. Returns (info, vtt_path)."""
    out_tmpl = os.path.join(tmpdir, "%(id)s")
    proc = run([
        "yt-dlp", "--skip-download", "--write-info-json",
        "--write-subs", "--write-auto-subs",
        "--sub-langs", "en.*,en", "--sub-format", "vtt",
        "-o", out_tmpl, f"https://www.youtube.com/watch?v={video_id}",
    ])
    info_path = os.path.join(tmpdir, f"{video_id}.info.json")
    if proc.returncode != 0 and not os.path.exists(info_path):
        raise RuntimeError(proc.stderr.strip()[-400:] or "yt-dlp failed")
    with open(info_path, encoding="utf-8") as f:
        info = json.load(f)
    vtts = glob.glob(os.path.join(tmpdir, f"{video_id}.en.vtt")) or glob.glob(
        os.path.join(tmpdir, f"{video_id}.en*.vtt")
    )
    return info, (vtts[0] if vtts else None)


def write_markdown(info, vtt_path):
    title = info.get("title") or info["id"]
    upload = info.get("upload_date") or ""
    upload_iso = f"{upload[:4]}-{upload[4:6]}-{upload[6:8]}" if len(upload) == 8 else "unknown"
    year = upload[:4] if len(upload) == 8 else "unknown-date"
    manual = bool((info.get("subtitles") or {}).get("en"))
    cap_kind = "Manual captions" if manual else "Auto-generated captions"
    caveat = "" if manual else " Expect missing punctuation and occasional mis-transcriptions."

    year_dir = os.path.join(OUT_DIR, year)
    os.makedirs(year_dir, exist_ok=True)
    base = f"{upload_iso}-{slugify(title)}" if upload_iso != "unknown" else slugify(title)
    path = os.path.join(year_dir, f"{base}.md")
    n = 2
    while os.path.exists(path):
        path = os.path.join(year_dir, f"{base}-{n}.md")
        n += 1

    paragraphs = lines_to_paragraphs(parse_vtt(vtt_path))
    today = date.today().isoformat()
    front = {
        "title": title,
        "status": "active",
        "owner": OWNER,
        "created": today,
        "last_updated": today,
    }
    with open(path, "w", encoding="utf-8") as f:
        f.write("---\n")
        f.write(yaml.safe_dump(front, allow_unicode=True, sort_keys=False, width=1000))
        f.write("---\n\n")
        f.write(f"# {title}\n\n")
        f.write(
            f"> Source: [YouTube](https://www.youtube.com/watch?v={info['id']}) — "
            f"Aswath Damodaran on Valuation. Uploaded {upload_iso}. "
            f"Duration {fmt_duration(info.get('duration'))}. "
            f"{cap_kind} converted to markdown.{caveat}\n\n"
        )
        f.write("## Transcript\n\n")
        f.write("\n\n".join(paragraphs) + "\n")
    return path, upload_iso, manual


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--limit", type=int, default=0, help="stop after N new videos (0 = all)")
    ap.add_argument("--sleep", type=float, default=4.0, help="base sleep between videos")
    args = ap.parse_args()

    index = load_index()
    by_id = {v["id"]: v for v in index["videos"]}
    today = date.today()

    def should_skip(vid):
        entry = by_id.get(vid)
        if not entry:
            return False
        if entry.get("captions") != "none":
            return True
        up = entry.get("upload_date") or ""
        try:
            return (today - date.fromisoformat(up)).days > RETRY_NO_CAPTION_DAYS
        except ValueError:
            return True

    todo = [v for v in list_channel_videos() if not should_skip(v["id"])]
    if args.limit:
        todo = todo[: args.limit]
    print(f"  {len(todo)} to fetch ({len(by_id)} already indexed)\n")

    done = failed = 0
    consecutive_failures = 0
    block_level = 0
    i = 0
    while i < len(todo):
        v = todo[i]
        vid = v["id"]
        n = i + 1
        try:
            with tempfile.TemporaryDirectory() as tmpdir:
                info, vtt = fetch_video(vid, tmpdir)
                if vtt is None:
                    upload = info.get("upload_date") or ""
                    upload_iso = (
                        f"{upload[:4]}-{upload[4:6]}-{upload[6:8]}" if len(upload) == 8 else "unknown"
                    )
                    by_id[vid] = {
                        "id": vid, "title": info.get("title") or vid,
                        "upload_date": upload_iso, "captions": "none", "file": None,
                    }
                    print(f"[{n}/{len(todo)}] {vid}  NO CAPTIONS  {info.get('title', '')[:60]}", flush=True)
                else:
                    path, upload_iso, manual = write_markdown(info, vtt)
                    by_id[vid] = {
                        "id": vid, "title": info.get("title") or vid,
                        "upload_date": upload_iso,
                        "duration": info.get("duration"),
                        "captions": "manual" if manual else "auto",
                        "file": os.path.relpath(path, OUT_DIR),
                    }
                    done += 1
                    print(f"[{n}/{len(todo)}] {vid}  ok  {os.path.basename(path)}", flush=True)
            consecutive_failures = 0
            block_level = 0
            i += 1
        except Exception as e:
            msg = str(e)
            if RATE_BLOCK_PAT.search(msg):
                index["videos"] = list(by_id.values())
                save_index(index)
                if block_level >= len(COOLDOWNS):
                    sys.exit(
                        f"Aborting: still rate-blocked after {sum(COOLDOWNS) // 60} min "
                        f"of cooldowns. Progress saved ({done} written this run)."
                    )
                wait = COOLDOWNS[block_level]
                block_level += 1
                print(
                    f"[{n}/{len(todo)}] {vid}  rate-blocked — cooling down "
                    f"{wait // 60} min (level {block_level}/{len(COOLDOWNS)})",
                    flush=True,
                )
                time.sleep(wait)
                continue  # retry the same video
            failed += 1
            consecutive_failures += 1
            i += 1
            print(f"[{n}/{len(todo)}] {vid}  FAILED  {e}", file=sys.stderr, flush=True)
            if consecutive_failures >= MAX_CONSECUTIVE_FAILURES:
                index["videos"] = list(by_id.values())
                save_index(index)
                sys.exit(
                    f"Aborting: {consecutive_failures} consecutive failures. Progress saved."
                )
        if n % 25 == 0:
            index["videos"] = list(by_id.values())
            save_index(index)
        time.sleep(args.sleep + random.uniform(0, 3))

    index["videos"] = list(by_id.values())
    save_index(index)
    print(f"\nDone: {done} written, {failed} failed, index at {INDEX_PATH}")
    sys.exit(1 if (failed and done == 0) else 0)


if __name__ == "__main__":
    main()
