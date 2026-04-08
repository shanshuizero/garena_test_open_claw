from __future__ import annotations

import json
import re
import sqlite3
import urllib.request
from datetime import datetime
from pathlib import Path

WORKSPACE_DIR = Path('/home/openclaw/.openclaw/workspace')
ANKI_DIR = WORKSPACE_DIR / 'dev-english-study' / 'anki-30day'
DB_PATH = WORKSPACE_DIR / 'english_study_web' / 'study.db'
API_URL = 'http://127.0.0.1:5010/api/pushes/upsert'


def current_day_number() -> int:
    now = datetime.now()
    return ((now.day - 1) % 30) + 1


def read_day(day_number: int) -> tuple[str, str, str]:
    anki_path = ANKI_DIR / f'anki-day-{day_number:02d}.md'
    speaking_path = ANKI_DIR / f'speaking-day-{day_number:02d}.md'
    anki = anki_path.read_text(encoding='utf-8', errors='ignore')
    speaking = speaking_path.read_text(encoding='utf-8', errors='ignore')
    title_line = next((line for line in anki.splitlines() if line.startswith('# ')), f'Day {day_number:02d}')
    theme = title_line.split('：', 1)[-1].strip() if '：' in title_line else title_line[2:].strip()
    return theme, anki, speaking


def md_to_simple_html(md_text: str) -> str:
    lines = [line.strip() for line in md_text.splitlines() if line.strip()]
    html_parts: list[str] = []
    for line in lines:
        if line.startswith('# '):
            continue
        if line.startswith('## '):
            html_parts.append(f"<h3>{line[3:].strip()}</h3>")
        elif re.match(r'^\d+\.\s', line):
            html_parts.append(f"<p><b>{line}</b></p>")
        elif line.startswith('- '):
            html_parts.append(f"<p>{line[2:].strip()}</p>")
        else:
            html_parts.append(f"<p>{line}</p>")
    return ''.join(html_parts)


def push_to_api(day_number: int, title: str, content: str) -> dict:
    payload = json.dumps({
        'day_number': day_number,
        'title': title,
        'content': content,
    }).encode('utf-8')
    req = urllib.request.Request(
        API_URL,
        data=payload,
        headers={'Content-Type': 'application/json'},
        method='POST',
    )
    with urllib.request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode('utf-8'))


def main() -> None:
    day_number = current_day_number()
    theme, anki, speaking = read_day(day_number)
    title = f'Day {day_number:02d}｜{theme}'
    content = (
        f'<h2>{title}</h2>'
        f'<h3>Anki 抽卡</h3>{md_to_simple_html(anki)}'
        f'<h3>晨读口语</h3>{md_to_simple_html(speaking)}'
    )
    result = push_to_api(day_number, title, content)
    print(json.dumps(result, ensure_ascii=False))


if __name__ == '__main__':
    main()
