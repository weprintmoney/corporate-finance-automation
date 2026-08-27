#!/usr/bin/env bash
# PreToolUse hook: blocks Write/Edit if the filename isn't kebab-case.
# Receives tool input as JSON on stdin.

INPUT=$(cat)
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('tool_input',{}).get('file_path',''))" 2>/dev/null)

if [ -z "$FILE_PATH" ]; then
  exit 0
fi

FILENAME=$(basename "$FILE_PATH" | sed 's/\.[^.]*$//')

# Allow dotfiles and ALL-CAPS convention files (CLAUDE, README, LICENSE, etc.)
if [[ "$FILENAME" =~ ^\. ]] || [[ "$FILENAME" =~ ^[A-Z_]+$ ]]; then
  exit 0
fi

# Check kebab-case: lowercase letters, digits, hyphens only
if [[ "$FILENAME" =~ ^[a-z0-9]+(-[a-z0-9]+)*$ ]]; then
  exit 0
fi

echo "BLOCKED: File names must be kebab-case." >&2
echo "  Got: $(basename "$FILE_PATH")" >&2
echo "  Expected format: my-file-name.md (lowercase, hyphens, no underscores or spaces)" >&2
exit 2
