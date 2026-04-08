from __future__ import annotations

from pathlib import Path
import html
import re

ROOT = Path('/home/openclaw/.openclaw/workspace')
SOURCE = ROOT / 'dev-english-study' / 'anki-30day'
DOCS = ROOT / 'docs'
SITE = DOCS / 'site'
TOTAL_DAYS = 30


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
    .anki-scene {{ perspective: 1200px; }}
    .anki-card {{ position:relative; min-height:220px; cursor:pointer; transform-style:preserve-3d; transition:transform .6s; }}
    .anki-card.is-flipped {{ transform:rotateY(180deg); }}
    .anki-face {{ position:absolute; inset:0; backface-visibility:hidden; border-radius:18px; padding:18px; box-sizing:border-box; border:1px solid #2b426b; box-shadow:0 8px 20px rgba(0,0,0,.18); }}
    .anki-front-face {{ background:linear-gradient(180deg,#17233f,#121a30); }}
    .anki-back-face {{ background:linear-gradient(180deg,#1b3158,#14223c); transform:rotateY(180deg); }}
    .anki-front {{ font-size:20px; font-weight:700; margin-bottom:12px; color:#fff; }}
    .anki-back {{ color:#d9e6f9; line-height:1.75; white-space:pre-line; }}
    .flip-tip {{ margin-top:14px; color:#9fb5d6; font-size:13px; }}
    .speak-item {{ border-left:3px solid #4f8dff; padding-left:14px; margin-bottom:16px; }}
    .section-title {{ margin-top:0; }}
    .footer-note {{ margin-top:16px; color:#97aac5; font-size:14px; }}
    .pager {{ display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; margin-top:20px; }}
    .pager a {{ display:inline-block; background:#243556; padding:10px 16px; border-radius:12px; color:#dceaff; font-weight:600; }}
    .speak-btn {{ border:none; background:#2c4773; color:#fff; border-radius:10px; padding:8px 12px; cursor:pointer; font-weight:600; }}
    .speak-btn:hover {{ background:#3b5d96; }}
    .tool-row {{ display:flex; gap:10px; flex-wrap:wrap; margin:10px 0 16px 0; }}
  </style>
  <script>
    function switchTab(id, btn) {{
      document.querySelectorAll('.tab-panel').forEach(el => el.classList.remove('active'));
      document.querySelectorAll('.tab-btn').forEach(el => el.classList.remove('active'));
      document.getElementById(id).classList.add('active');
      btn.classList.add('active');
    }}
    function flipCard(id) {{
      const el = document.getElementById(id);
      if (el) el.classList.toggle('is-flipped');
    }}
    function speakText(text) {{
      if (!('speechSynthesis' in window)) {{
        alert('当前浏览器不支持朗读功能');
        return;
      }}
      window.speechSynthesis.cancel();
      const utter = new SpeechSynthesisUtterance(text);
      utter.lang = 'en-US';
      utter.rate = 0.95;
      window.speechSynthesis.speak(utter);
    }}
    function speakMany(texts) {{
      if (!('speechSynthesis' in window)) {{
        alert('当前浏览器不支持朗读功能');
        return;
      }}
      window.speechSynthesis.cancel();
      const queue = [...texts];
      function next() {{
        const text = queue.shift();
        if (!text) return;
        const utter = new SpeechSynthesisUtterance(text);
        utter.lang = 'en-US';
        utter.rate = 0.95;
        utter.onend = next;
        window.speechSynthesis.speak(utter);
      }}
      next();
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
    for idx, c in enumerate(cards, start=1):
        card_id = f'card-{n:02d}-{idx}'
        front = html.escape(c['front'])
        back = html.escape(c['back'])
        front_js = html.escape(c['front'], quote=True)
        back_js = html.escape(c['back'], quote=True)
        anki_html.append(
            f'<div class="anki-scene">'
            f'  <div id="{card_id}" class="anki-card" onclick="flipCard(\'{card_id}\')">'
            f'    <div class="anki-face anki-front-face">'
            f'      <div class="anki-front">{front}</div>'
            f'      <div class="tool-row"><button class="speak-btn" onclick="event.stopPropagation(); speakText(\'{front_js}\')">🔊 朗读正面</button><button class="speak-btn" onclick="event.stopPropagation(); speakText(\'{back_js}\')">🔊 朗读背面</button></div>'
            f'      <div class="flip-tip">点击卡片翻面</div>'
            f'    </div>'
            f'    <div class="anki-face anki-back-face">'
            f'      <div class="anki-back">{back}</div>'
            f'      <div class="tool-row"><button class="speak-btn" onclick="event.stopPropagation(); speakText(\'{front_js}\')">🔊 朗读正面</button><button class="speak-btn" onclick="event.stopPropagation(); speakText(\'{back_js}\')">🔊 朗读背面</button></div>'
            f'      <div class="flip-tip">再次点击可翻回正面</div>'
            f'    </div>'
            f'  </div>'
            f'</div>'
        )
    anki_html.append('</div>')
    speak_html = []
    sentence_js_list = []
    for item in speaking_items:
        sentence = html.escape(item['sentence'])
        cn = html.escape(item['cn'])
        tip = html.escape(item['tip'])
        sentence_js = html.escape(item['sentence'], quote=True)
        sentence_js_list.append(f"'{sentence_js}'")
        speak_html.append(
            f'<div class="card speak-item">'
            f'<div><b>{sentence}</b></div>'
            f'<div class="tool-row"><button class="speak-btn" onclick="speakText(\'{sentence_js}\')">🔊 朗读本句</button></div>'
            f'<div class="muted">中文：{cn}</div>'
            f'<div class="muted">提示：{tip}</div>'
            f'</div>'
        )
    prev_link = f'./day-{n-1:02d}.html' if n > 1 else './days.html'
    next_link = f'./day-{n+1:02d}.html' if n < TOTAL_DAYS else './days.html'
    prev_label = f'← Day {n-1:02d}' if n > 1 else '← 返回计划'
    next_label = f'Day {n+1:02d} →' if n < TOTAL_DAYS else '返回计划 →'
    body = f'''
    <div class="hero">
      <span class="badge">Day {n:02d}</span>
      <h1>{html.escape(theme)}</h1>
      <p class="muted">支持翻面卡片、Anki / 晨读 tab 切换、朗读按钮，以及上下日导航。</p>
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
        <div class="tool-row"><button class="speak-btn" onclick="speakMany([{','.join(sentence_js_list)}])">▶ 朗读本页晨读</button></div>
        {''.join(speak_html)}
        <div class="footer-note">建议：先慢读 2 遍，再正常语速读 3 遍，最后脱稿复述其中 2 句。</div>
      </div>
      <div class="pager">
        <a href="{prev_link}">{prev_label}</a>
        <a href="./days.html">返回 30 天计划</a>
        <a href="{next_link}">{next_label}</a>
      </div>
    </div>
    '''
    return page_wrap(f'Day {n:02d}｜{theme}', body)


def export_days() -> list[tuple[int, str]]:
    days: list[tuple[int, str]] = []
    for n in range(1, TOTAL_DAYS + 1):
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
            f'<p class="muted">翻面卡片 + 晨读切换 + 朗读按钮</p></div>'
        )
    body = f'''
    <div class="hero">
      <h1>Garena Test OpenClaw 学习站</h1>
      <p>一个适合 GitHub Pages 展示的静态英文学习站，覆盖前后端开发英语、30 天学习计划、翻面 Anki 卡片、晨读口语与浏览器原生朗读。</p>
    </div>
    <div class="grid">
      <div class="card"><h2>30 天学习计划</h2><p class="muted">按天学习，适合持续积累。</p><p><a href="./days.html">立即开始</a></p></div>
      <div class="card"><h2>翻面卡片</h2><p class="muted">点击卡片即可翻面，强化记忆。</p></div>
      <div class="card"><h2>朗读功能</h2><p class="muted">支持 Anki 与晨读口语句子朗读。</p></div>
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
            f'<p class="muted">翻面卡片 + 晨读口语 + 朗读</p></div>'
        )
    body = f'''
    <div class="hero">
      <h1>30 天学习计划</h1>
      <p>点击任意一天进入学习页，可切换查看 <b>Anki 抽卡</b> 与 <b>晨读口语</b>，并支持朗读与上下日跳转。</p>
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
