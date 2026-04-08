#!/usr/bin/env bash
set -euo pipefail
cd /home/openclaw/.openclaw/workspace/english_study_web
/home/openclaw/.openclaw/workspace/english_study_web/.venv/bin/python /home/openclaw/.openclaw/workspace/english_study_web/sync_daily_push.py >> /tmp/english-study-sync.log 2>&1
