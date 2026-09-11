# YouTube Transcripts

Transcript archive of Aswath Damodaran's YouTube channel ([@AswathDamodaranonValuation](https://www.youtube.com/@AswathDamodaranonValuation)) — class sessions (Corporate Finance, Valuation, Investment Philosophies), Musings on Markets videos, and market commentary. ~1,400 videos at the 2026-09-01 backfill.

## Layout

- One markdown file per video: `<year>/<upload-date>-<title-slug>.md`
- `index.yaml` — the navigation entry point. Maps every video id to file, title, upload date, duration (seconds), and caption type. Read this first; don't scan year folders.
- Fetched by `scripts/fetch-youtube-transcripts.py`; new uploads added weekly by the `refresh-youtube-transcripts` CI workflow. The script is resumable — it skips anything already in `index.yaml`.

## Caveats

- Most transcripts come from **auto-generated captions**: no punctuation guarantees, occasional mis-transcriptions (company names and proper nouns suffer most; "Chat GPT" may appear as "Chachi PT"). Fine for search, retrieval, and agent context — below the cleaned-prose bar of the lesson transcripts in `03-2-course-content/`.
- `captions: none` entries in `index.yaml` are videos with no caption track yet (usually very recent uploads); they're retried by the weekly job for 21 days after upload.
- These overlap with but are broader than the certificate course: the channel carries full MBA course sessions and topical videos the certificate doesn't include.

## Doc Index

| File | Description |
|------|-------------|
| `index.yaml` | Full video map: id → file, title, upload date, duration, caption type |
| `<year>/` | Per-video transcript files, named `<upload-date>-<title-slug>.md` |
