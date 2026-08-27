#!/usr/bin/env bash
# PreToolUse hook: blocks git push to main branch.
# Receives tool input as JSON on stdin.

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('tool_name',''))" 2>/dev/null)

# Only check Bash tool calls
if [ "$TOOL_NAME" != "Bash" ]; then
  exit 0
fi

COMMAND=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('tool_input',{}).get('command',''))" 2>/dev/null)

# Check if it's a git push to main
if echo "$COMMAND" | grep -qE 'git\s+push.*\b(main|master)\b|git\s+push\s*$'; then
  # Check if we're on main branch
  BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
  if [ "$BRANCH" = "main" ] || [ "$BRANCH" = "master" ] || echo "$COMMAND" | grep -qE '\b(main|master)\b'; then
    echo "BLOCKED: Direct push to main is not allowed." >&2
    echo "  Use /commit-push-pr-slack to create a branch, open a PR, and notify the team." >&2
    exit 2
  fi
fi

exit 0
