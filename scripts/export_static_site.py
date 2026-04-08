from __future__ import annotations

from pathlib import Path
import html
import re

ROOT = Path('/home/openclaw/.openclaw/workspace')
SOURCE = ROOT / 'dev-english-study' / 'anki-30day'
DOCS = ROOT / 'docs'
SITE = DOCS / 'site'


def read_title(path: Path) -> str:
    for line in path.read_text(encoding='utf-8', errors='ignore').splitlines():
        if line.startswith('# '):
            return line[2:].strip()
    return path.stem


def md_to_html(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    in_list = False
    for raw in lines:
        line = raw.rstrip()
        if not line.strip():
            if in_list:
                out.append('</ul>')
                in_list = False
            continue
        if line.startswith('# '):
            out.append(f'<h1>{html.escape(line[2:].strip())}</h1>')
        elif line.startswith('## '):
            if in_list:
                out.append('</ul>')
                in_list = False
            out.append(f'<h2>{html.escape(line[3:].strip())}</h2>')
        elif re.match(r'^\d+\.\s', line):
            if not in_list:
                out.append('<ul>')
                in_list = True
            out.append(f'<li><b>{html.escape(line)}</b></li>')
        elif line.startswith('- '):
            if not in_list:
                out.append('<ul>')
                in_list = True
            out.append(f'<li>{html.escape(line[2:].strip())}</li>')
        else:
            if in_list:
                out.append('</ul>')
                in_list = False
            out.append(f'<p>{html.escape(line)}</p>')
    if in_list:
        out.append('</ul>')
    return '\n'.join(out)


def page_wrap(title: str, body: str) -> str:
    return f'''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    body {{ font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; margin: 0; background:#0b1020; color:#e8ecf3; }}
    .wrap {{ max-width: 1100px; margin: 0 auto; padding: 24px; }}
    .nav {{ display:flex; gap:14px; flex-wrap:wrap; margin-bottom:24px; background:#121a30; padding:16px; border-radius:14px; }}
    .card {{ background:#121a30; border-radius:16px; padding:20px; margin-bottom:18px; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(220px,1fr)); gap:16px; }}
    a {{ color:#8cc8ff; text-decoration:none; }}
    a:hover {{ text-decoration:underline; }}
    .muted {{ color:#9aacbf; }}
    .badge {{ display:inline-block; padding:4px 10px; border-radius:999px; background:#243556; color:#cfe4ff; font-size:12px; }}
    .content {{ line-height:1.75; }}
  </style>
</head>
<body>
  <div class="wrap">
    <div class="nav">
      <a href="./index.html">首页</a>
      <a href="./days.html">30天计划</a>
    </div>
    {body}
  </div>
</body>
</html>'''


def export_days() -> list[tuple[int, str]]:
    days: list[tuple[int, str]] = []
    for n in range(1, 31):
        anki = SOURCE / f'anki-day-{n:02d}.md'
        speaking = SOURCE / f'speaking-day-{n:02d}.md'
        if not anki.exists() or not speaking.exists():
            continue
        title = read_title(anki)
        theme = title.split('：', 1)[-1].strip() if '：' in title else title
        days.append((n, theme))
        body = f'''
        <div class="card">
          <span class="badge">Day {n:02d}</span>
          <h1>{html.escape(theme)}</h1>
        </div>
        <div class="grid">
          <div class="card content">
            <h2>Anki 抽卡</h2>
            {md_to_html(anki.read_text(encoding='utf-8', errors='ignore'))}
          </div>
          <div class="card content">
            <h2>晨读口语</h2>
            {md_to_html(speaking.read_text(encoding='utf-8', errors='ignore'))}
          </div>
        </div>
        '''
        (SITE / f'day-{n:02d}.html').write_text(page_wrap(f'Day {n:02d}｜{theme}', body), encoding='utf-8')
    return days


def export_index(days: list[tuple[int, str]]) -> None:
    cards = []
    for n, theme in days:
        cards.append(f'<div class="card"><span class="badge">Day {n:02d}</span><h3><a href="./day-{n:02d}.html">{html.escape(theme)}</a></h3></div>')
    body = f'''
    <div class="card">
      <h1>Garena Test OpenClaw 静态学习站</h1>
      <p class="muted">GitHub Pages 版本：展示 30 天英文学习计划与资料。</p>
    </div>
    <div class="card">
      <h2>快速入口</h2>
      <ul>
        <li><a href="./days.html">浏览 30 天计划</a></li>
        <li><a href="../README.md">查看仓库 README</a></li>
      </ul>
    </div>
    <div class="grid">{''.join(cards[:6])}</div>
    '''
    (SITE / 'index.html').write_text(page_wrap('静态学习站首页', body), encoding='utf-8')


def export_days_index(days: list[tuple[int, str]]) -> None:
    cards = []
    for n, theme in days:
        cards.append(f'<div class="card"><span class="badge">Day {n:02d}</span><h3><a href="./day-{n:02d}.html">{html.escape(theme)}</a></h3></div>')
    body = f'''
    <div class="card">
      <h1>30 天学习计划</h1>
      <p class="muted">GitHub Pages 静态展示版</p>
    </div>
    <div class="grid">{''.join(cards)}</div>
    '''
    (SITE / 'days.html').write_text(page_wrap('30 天学习计划', body), encoding='utf-8')


def main() -> None:
    SITE.mkdir(parents=True, exist_ok=True)
    days = export_days()
    export_index(days)
    export_days_index(days)


if __name__ == '__main__':
    main()
