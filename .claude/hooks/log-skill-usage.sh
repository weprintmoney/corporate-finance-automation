#!/usr/bin/env bash
# UserPromptSubmit hook: logs skill invocations to skills-usage.log at the repo root.

INPUT=$(cat)
PROMPT=$(echo "$INPUT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('prompt',''))" 2>/dev/null)

if ! echo "$PROMPT" | grep -qE '^/[a-z]'; then
  exit 0
fi

SKILL_NAME=$(echo "$PROMPT" | python3 -c "import sys; print(sys.stdin.readline().strip().split()[0].lstrip('/'))" 2>/dev/null)
TIMESTAMP=$(date '+%Y-%m-%d %H:%M')
USER=$(whoami)

echo "${TIMESTAMP} | ${SKILL_NAME} | ${USER}" >> skills-usage.log

exit 0
