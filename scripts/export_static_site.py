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


def parse_anki(md: str):
    cards = []
    lines = md.splitlines()
    current = None
    for line in lines:
        m = re.match(r'^\d+\.\s\*\*Front\*\*:\s*(.+)$', line.strip())
        if m:
            if current:
                cards.append(current)
            current = {'front': m.group(1).strip(), 'back': ''}
            continue
        if current and '**Back**:' in line:
            current['back'] = line.split('**Back**:', 1)[1].strip()
    if current:
        cards.append(current)
    return cards


def parse_speaking(md: str):
    items = []
    current = None
    for raw in md.splitlines():
        line = raw.rstrip()
        m = re.match(r'^\d+\.\s(.+)$', line.strip())
        if m and not line.strip().startswith('- '):
            if current:
                items.append(current)
            current = {'sentence': m.group(1).strip(), 'cn': '', 'tip': ''}
            continue
        if current and line.strip().startswith('- 中文：'):
            current['cn'] = line.strip().replace('- 中文：', '', 1).strip()
        elif current and line.strip().startswith('- 提示：'):
            current['tip'] = line.strip().replace('- 提示：', '', 1).strip()
    if current:
        items.append(current)
    return items


def page_wrap(title: str, body: str) -> str:
    return f'''<!doctype html>
<html lang="zh-CN">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <style>
    body {{ font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif; margin: 0; background: linear-gradient(180deg,#0b1020,#111931); color:#e8ecf3; }}
    .wrap {{ max-width: 1180px; margin: 0 auto; padding: 24px; }}
    .nav {{ display:flex; gap:14px; flex-wrap:wrap; margin-bottom:24px; background:rgba(18,26,48,.88); padding:16px 18px; border-radius:16px; backdrop-filter: blur(10px); }}
    .nav a {{ color:#cfe4ff; text-decoration:none; font-weight:600; }}
    .nav a:hover {{ color:#8cc8ff; }}
    .hero {{ background: linear-gradient(135deg,#162445,#1c3d73); border-radius:22px; padding:28px; margin-bottom:22px; box-shadow:0 10px 30px rgba(0,0,0,.22); }}
    .card {{ background:#121a30; border-radius:18px; padding:20px; margin-bottom:18px; box-shadow:0 8px 24px rgba(0,0,0,.18); }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:16px; }}
    a {{ color:#8cc8ff; text-decoration:none; }}
    a:hover {{ text-decoration:underline; }}
    .muted {{ color:#9aacbf; }}
    .badge {{ display:inline-block; padding:4px 10px; border-radius:999px; background:#243556; color:#cfe4ff; font-size:12px; }}
    .tabs {{ display:flex; gap:10px; margin-bottom:18px; flex-wrap:wrap; }}
    .tab-btn {{ border:none; border-radius:999px; background:#243556; color:#d8e8ff; padding:10px 16px; cursor:pointer; font-weight:600; }}
    .tab-btn.active {{ background:#4f8dff; color:white; }}
    .tab-panel {{ display:none; }}
    .tab-panel.active {{ display:block; }}
    .anki-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:16px; }}
    .anki-card {{ background:linear-gradient(180deg,#17233f,#121a30); border:1px solid #2b426b; border-radius:18px; padding:18px; min-height:180px; }}
    .anki-front {{ font-size:20px; font-weight:700; margin-bottom:12px; color:#fff; }}
    .anki-back {{ color:#cfe0f7; line-height:1.7; white-space:pre-line; }}
    .speak-item {{ border-left:3px solid #4f8dff; padding-left:14px; margin-bottom:16px; }}
    .section-title {{ margin-top:0; }}
    .footer-note {{ margin-top:16px; color:#97aac5; font-size:14px; }}
  </style>
  <script>
    function switchTab(id, btn) {{
      document.querySelectorAll('.tab-panel').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
      document.getElementById(id).classList.add('active');
      btn.classList.add('active');
    }}
  </script>
</head>
<body>
  <div class="wrap">
    <div class="nav">
      <a href="./index.html">首页</a>
      <a href="./days.html">30天计划</a>
      <a href="../README.md">仓库说明</a>
    </div>
    {body}
  </div>
</body>
</html>'''


def render_day_page(n: int, theme: str, anki_md: str, speaking_md: str) -> str:
    cards = parse_anki(anki_md)
    speaking_items = parse_speaking(speaking_md)
    anki_html = ['<div class="anki-grid">']
    for c in cards:
        anki_html.append(
            f'<div class="anki-card">'
            f'<div class="anki-front">{html.escape(c["front"])}</div>'
            f'<div class="anki-back">{html.escape(c["back"])}</div>'
            f'</div>'
        )
    anki_html.append('</div>')
    speak_html = []
    for item in speaking_items:
        speak_html.append(
            f'<div class="card speak-item">'
            f'<div><b>{html.escape(item["sentence"])}</b></div>'
            f'<div class="muted">中文：{html.escape(item["cn"])}</div>'
            f'<div class="muted">提示：{html.escape(item["tip"])}</div>'
            f'</div>'
        )
    body = f'''
    <div class="hero">
      <span class="badge">Day {n:02d}</span>
      <h1>{html.escape(theme)}</h1>
      <p class="muted">支持卡片式 Anki 浏览与晨读口语切换。</p>
    </div>
    <div class="card">
      <div class="tabs">
        <button class="tab-btn active" onclick="switchTab('anki', this)">Anki 抽卡</button>
        <button class="tab-btn" onclick="switchTab('speaking', this)">晨读口语</button>
      </div>
      <div id="anki" class="tab-panel active">
        <h2 class="section-title">Anki 抽卡</h2>
        {''.join(anki_html)}
      </div>
      <div id="speaking" class="tab-panel">
        <h2 class="section-title">晨读口语</h2>
        {''.join(speak_html)}
        <div class="footer-note">建议：先慢读 2 遍，再正常语速读 3 遍，最后脱稿复述其中 2 句。</div>
      </div>
    </div>
    '''
    return page_wrap(f'Day {n:02d}｜{theme}', body)


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
        html_page = render_day_page(
            n,
            theme,
            anki.read_text(encoding='utf-8', errors='ignore'),
            speaking.read_text(encoding='utf-8', errors='ignore'),
        )
        (SITE / f'day-{n:02d}.html').write_text(html_page, encoding='utf-8')
    return days


def export_index(days: list[tuple[int, str]]) -> None:
    cards = []
    for n, theme in days[:8]:
        cards.append(
            f'<div class="card"><span class="badge">Day {n:02d}</span>'
            f'<h3><a href="./day-{n:02d}.html">{html.escape(theme)}</a></h3>'
            f'<p class="muted">卡片式学习 + 晨读切换</p></div>'
        )
    body = f'''
    <div class="hero">
      <h1>Garena Test OpenClaw 学习站</h1>
      <p>一个适合 GitHub Pages 展示的静态英文学习站，覆盖前后端开发英语、30 天学习计划、Anki 卡片与晨读口语。</p>
    </div>
    <div class="grid">
      <div class="card"><h2>30 天学习计划</h2><p class="muted">按天学习，适合持续积累。</p><p><a href="./days.html">立即开始</a></p></div>
      <div class="card"><h2>Anki 卡片</h2><p class="muted">真正卡片形式展示，更适合记忆。</p></div>
      <div class="card"><h2>晨读口语</h2><p class="muted">支持切换查看，适合每日朗读训练。</p></div>
    </div>
    <div class="card">
      <h2>推荐从这些内容开始</h2>
      <div class="grid">{''.join(cards)}</div>
    </div>
    '''
    (SITE / 'index.html').write_text(page_wrap('静态学习站首页', body), encoding='utf-8')


def export_days_index(days: list[tuple[int, str]]) -> None:
    cards = []
    for n, theme in days:
        cards.append(
            f'<div class="card"><span class="badge">Day {n:02d}</span>'
            f'<h3><a href="./day-{n:02d}.html">{html.escape(theme)}</a></h3>'
            f'<p class="muted">Anki 卡片 + 晨读口语</p></div>'
        )
    body = f'''
    <div class="hero">
      <h1>30 天学习计划</h1>
      <p>点击任意一天进入学习页，可切换查看 <b>Anki 抽卡</b> 与 <b>晨读口语</b>。</p>
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
