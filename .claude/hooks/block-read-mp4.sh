#!/usr/bin/env bash
# PreToolUse hook: blocks Read on .mp4 files.
# MP4s are Git LFS pointers — reading them returns binary garbage.
# The .md transcript for the same session is always present alongside the .mp4.

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('tool_input',{}).get('file_path',''))" 2>/dev/null)

if [[ "$FILE_PATH" == *.mp4 ]]; then
  TRANSCRIPT="${FILE_PATH%.mp4}.md"
  echo "BLOCKED: Cannot read .mp4 (binary video / LFS pointer)." >&2
  echo "  Use the transcript instead: $TRANSCRIPT" >&2
  exit 2
fi
