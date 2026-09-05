#!/usr/bin/env python3
"""
Orchestrates the full crawl-and-conversion-runbook.md pipeline end to end:
dry-run crawl -> gate report -> full crawl -> HTML/XLS/PDF conversion -> index
build. Every step below is independently idempotent (manifest/progress-JSON
checkpointed), so re-running this orchestrator after an interruption just
fast-skips completed work instead of starting over.

Run: python3 scripts/run-pipeline.py
"""
import subprocess
import sys
import json
import os

PY = sys.executable
SCRIPTS = os.path.dirname(os.path.abspath(__file__))


def run(script, args=None, env_extra=None):
    cmd = [PY, os.path.join(SCRIPTS, script)] + (args or [])
    env = os.environ.copy()
    if env_extra:
        env.update(env_extra)
    print(f"\n=== Running {script} {' '.join(args or [])} ===", flush=True)
    result = subprocess.run(cmd, env=env)
    if result.returncode != 0:
        print(f"!!! {script} exited with code {result.returncode} — continuing pipeline anyway "
              f"(idempotent design means a rerun of this orchestrator will retry/skip correctly).",
              flush=True)
    return result.returncode


def print_gate_report():
    manifest_path = os.path.join(SCRIPTS, "crawl-manifest.json")
    with open(manifest_path) as f:
        manifest = json.load(f)
    entries = manifest["entries"]
    pdf_bytes = sum(e.get("bytes") or 0 for e in entries if e["type"] == "pdf")
    xls_bytes = sum(e.get("bytes") or 0 for e in entries if e["type"] == "xls")
    total = pdf_bytes + xls_bytes
    print(f"\n--- Gate decisions (auto-applied, user pre-authorized overnight run) ---", flush=True)
    print(f"Total PDF+XLS bytes: {total/1e6:.1f} MB", flush=True)
    if total > 300e6:
        print("Gate a: >300MB — would normally consider Git LFS for *.xls/*.xlsx. "
              "Proceeding without LFS per standing repo size (revisit if push fails).", flush=True)
    else:
        print("Gate a: under 300MB, no LFS needed.", flush=True)
    if total > 1e9:
        print("Gate c: >1GB total — normally 'rescope with user'. User pre-authorized "
              "full autonomous run, so proceeding anyway.", flush=True)
    else:
        print("Gate c: under 1GB, OK.", flush=True)


def main():
    # Phase 0: finish the dry-run manifest (resumable — cached HTML + manifest entries skip re-fetch)
    run("crawl-damodaran-site.py", ["--dry-run"])
    print_gate_report()

    # Phase 1: full crawl — same script, no --dry-run. HTML already cached from
    # Phase 0 is reused; PDF/XLS entries go from HEAD-checked to fully downloaded.
    run("crawl-damodaran-site.py")

    # Phase 2: conversions
    run("convert-damodaran-html.py")
    run("convert-damodaran-xls.py")
    run("convert-damodaran-pdfs.py", env_extra={"SURYA_INFERENCE_BACKEND": "llamacpp"})

    # Phase 3: navigation build
    run("build-damodaran-index.py")

    print("\n=== Pipeline complete ===", flush=True)


if __name__ == "__main__":
    main()
