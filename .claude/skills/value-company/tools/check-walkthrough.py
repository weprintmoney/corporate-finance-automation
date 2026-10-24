#!/usr/bin/env python3
"""Confirm every number in walkthrough.md traces to the ledger or the model output.

Usage: python3 check-walkthrough.py <walkthrough.md> <inputs.yaml> <model-output.md>

A number in the walkthrough passes if some number in the ledger or the model output matches it
after allowing for unit changes (percent vs. decimal, millions vs. billions) and rounding.
Skipped on purpose: years, dates, step and lesson numbers, note and form references, file names,
code spans, and ordinal words like "10-year".

Exit 1 if any number is unmatched; each one is printed with its line.
"""
import re
import sys

import yaml

NUM = re.compile(r"(?<![\w.])[-−]?\$?\d{1,3}(?:,\d{3})+(?:\.\d+)?|(?<![\w.])[-−]?\$?\d+(?:\.\d+)?")
SKIP_CONTEXT = re.compile(
    r"(?i)\b(step|lesson|note|notes|part|form|item|session|chapter|section|exhibit|schedule|module|page|def|fy)\s*$"
    r"|^\s*(-year|-k\b|-q\b|-month|-day|%?\s*of the way)"
)


def collect_numbers(values):
    """Expand a number into the forms a plain-language writer might use."""
    out = set()
    for v in values:
        for f in (v, v * 100, v / 100, v / 1000, v * 1000, abs(v)):
            out.add(round(f, 4))
    return out


def ledger_numbers(data):
    out = []

    def walk(x):
        if isinstance(x, dict):
            for v in x.values():
                walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
        elif isinstance(x, (int, float)) and not isinstance(x, bool):
            out.append(float(x))
        elif isinstance(x, str):
            for m in NUM.findall(x):
                try:
                    out.append(float(m.replace("$", "").replace(",", "").replace("−", "-")))
                except ValueError:
                    pass

    walk(data)
    return out


def text_numbers(text):
    out = []
    for m in NUM.findall(text):
        try:
            out.append(float(m.replace("$", "").replace(",", "").replace("−", "-")))
        except ValueError:
            pass
    return out


def matches(x, pool):
    for cand in (x, round(x, 2), round(x, 1), round(x, 0)):
        if round(cand, 4) in pool:
            return True
    # tolerance: 0.5% relative or 0.05 absolute against any pooled value in the same scale
    for p in pool:
        if abs(p - x) <= max(0.05, 0.005 * abs(x)):
            return True
    return False


def main(argv):
    if len(argv) != 3:
        sys.exit("usage: check-walkthrough.py <walkthrough.md> <inputs.yaml> <model-output.md>")
    walk_path, ledger_path, model_path = argv
    with open(ledger_path) as fh:
        ledger = yaml.safe_load(fh)
    with open(model_path) as fh:
        model_text = fh.read()
    pool = collect_numbers(ledger_numbers(ledger) + text_numbers(model_text))

    unmatched = []
    with open(walk_path) as fh:
        lines = fh.readlines()
    for ln, line in enumerate(lines, start=1):
        if line.lstrip().startswith("#"):
            continue
        clean = re.sub(r"`[^`]*`", " ", line)                      # code spans and file names
        clean = re.sub(r"\b(19|20)\d{2}-\d{2}-\d{2}\b", " ", clean)  # dates
        clean = re.sub(r"\b(FY|fy)\s?(19|20)?\d{2,4}\b", " ", clean)
        clean = re.sub(r"\b\d+-(year|month|day|week|K|Q)\b", " ", clean)
        clean = re.sub(r"\b10-K\b|\b10-Q\b|\b8-K\b|\bDEF\s?14A\b|\bDEFM\s?14[AC]\b|\b13E-3\b|\bS-1\b", " ", clean)
        for m in NUM.finditer(clean):
            raw = m.group(0)
            before = clean[max(0, m.start() - 12):m.start()]
            after = clean[m.end():m.end() + 10]
            if SKIP_CONTEXT.search(before) or SKIP_CONTEXT.match(after):
                continue
            try:
                x = float(raw.replace("$", "").replace(",", "").replace("−", "-"))
            except ValueError:
                continue
            if 1900 <= x <= 2100 and x == int(x) and "$" not in raw and "." not in raw:
                continue  # a year
            if x == int(x) and 0 <= x <= 12 and "$" not in raw and "%" not in after[:1] and "." not in raw:
                continue  # a count (three tests, four parts); dollar and percent figures still checked
            if not matches(x, pool):
                unmatched.append((ln, raw, line.strip()))

    if unmatched:
        print("{} number(s) in {} do not trace to the ledger or the model output:".format(len(unmatched), walk_path))
        for ln, raw, line in unmatched:
            print("  line {}: {}  ←  {}".format(ln, raw, line[:120]))
        sys.exit(1)
    print("every number in {} traces to the ledger or the model output".format(walk_path))


if __name__ == "__main__":
    main(sys.argv[1:])
