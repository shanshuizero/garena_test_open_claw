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
    :root {{
      --bg-dark:#000000;
      --bg-light:#f5f5f7;
      --text-dark:#1d1d1f;
      --text-light:#ffffff;
      --text-muted-dark:rgba(255,255,255,.72);
      --text-muted-light:rgba(0,0,0,.72);
      --blue:#0071e3;
      --blue-dark:#2997ff;
      --link:#5f86c5;
      --link-soft:#7f9dcd;
      --surface-dark:#272729;
      --surface-dark-2:#2a2a2d;
      --shadow:rgba(0,0,0,.22) 3px 5px 30px 0px;
    }}
    * {{ box-sizing:border-box; }}
    body {{ margin:0; background:var(--bg-dark); color:var(--text-light); font-family:"SF Pro Text","Helvetica Neue",Helvetica,Arial,sans-serif; line-height:1.47; letter-spacing:-0.01em; }}
    .wrap {{ width:100%; }}
    .nav {{ position:sticky; top:0; z-index:20; display:flex; gap:18px; align-items:center; flex-wrap:wrap; min-height:48px; padding:12px 22px; background:rgba(0,0,0,.8); backdrop-filter:saturate(180%) blur(20px); }}
    .nav a {{ color:#fff; text-decoration:none; font-size:12px; font-weight:400; opacity:.92; }}
    .nav a:hover {{ opacity:1; color:#fff; text-decoration:underline; }}
    .section-dark {{ background:var(--bg-dark); color:var(--text-light); }}
    .section-light {{ background:var(--bg-light); color:var(--text-dark); }}
    .inner {{ max-width:1100px; margin:0 auto; padding:56px 24px; }}
    .hero {{ padding:84px 24px 72px; text-align:center; }}
    .hero .inner {{ padding:0; }}
    .eyebrow {{ display:inline-block; margin-bottom:14px; color:var(--blue-dark); font-size:14px; letter-spacing:-0.224px; }}
    .display {{ font-family:"SF Pro Display","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:56px; line-height:1.07; letter-spacing:-0.28px; font-weight:600; margin:0 0 14px; }}
    .subtitle {{ max-width:760px; margin:0 auto; font-size:21px; line-height:1.19; letter-spacing:0.231px; color:inherit; opacity:.88; }}
    .cta-row {{ display:flex; justify-content:center; gap:12px; flex-wrap:wrap; margin-top:28px; }}
    .btn-primary, .btn-secondary {{ display:inline-flex; align-items:center; justify-content:center; min-height:40px; padding:8px 18px; border-radius:980px; text-decoration:none; font-size:17px; font-weight:400; }}
    .btn-primary {{ background:var(--blue); color:#fff; border:1px solid transparent; }}
    .btn-primary:hover {{ background:#0077ed; }}
    .btn-secondary {{ background:transparent; color:var(--blue-dark); border:1px solid var(--blue-dark); }}
    .section-title {{ font-family:"SF Pro Display","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:40px; line-height:1.1; font-weight:600; margin:0 0 12px; letter-spacing:-0.02em; }}
    .section-copy {{ font-size:17px; line-height:1.47; margin:0 0 24px; max-width:760px; }}
    .grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(240px,1fr)); gap:18px; }}
    .overview-card {{ background:var(--surface-dark); border-radius:12px; padding:22px; box-shadow:var(--shadow); }}
    .section-light .overview-card {{ background:#fff; color:var(--text-dark); }}
    .card-title {{ font-family:"SF Pro Display","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:21px; line-height:1.19; font-weight:700; letter-spacing:0.231px; margin:10px 0 8px; }}
    .card-copy {{ font-size:14px; line-height:1.43; letter-spacing:-0.224px; color:inherit; opacity:.78; }}
    .badge {{ display:inline-block; padding:4px 10px; border-radius:999px; font-size:12px; line-height:1.33; letter-spacing:-0.12px; background:rgba(255,255,255,.12); color:#fff; }}
    .section-light .badge {{ background:#e8edf5; color:#1d1d1f; }}
    .days-grid .overview-card {{ min-height:144px; }}
    .tabs {{ display:flex; gap:10px; margin:0 0 20px; flex-wrap:wrap; }}
    .tab-btn {{ border:none; border-radius:980px; background:#1d1d1f; color:#fff; padding:8px 16px; cursor:pointer; font-size:14px; line-height:1.43; }}
    .tab-btn.active {{ background:var(--blue); }}
    .section-dark .tab-btn {{ background:#1d1d1f; }}
    .section-light .tab-btn {{ background:#1d1d1f; color:#fff; }}
    .tab-panel {{ display:none; }}
    .tab-panel.active {{ display:block; }}
    .tool-row {{ display:flex; gap:10px; flex-wrap:wrap; margin:10px 0 16px 0; }}
    .speak-btn, .speed-chip {{ border:none; border-radius:11px; padding:8px 14px; cursor:pointer; font-size:14px; line-height:1.43; }}
    .speak-btn {{ background:#fafafc; color:rgba(0,0,0,.8); border:3px solid rgba(0,0,0,.04); }}
    .speed-chip {{ background:#fafafc; color:rgba(0,0,0,.8); border:3px solid rgba(0,0,0,.04); }}
    .speed-chip.active {{ background:var(--blue); color:#fff; border-color:transparent; }}
    .anki-grid {{ display:grid; grid-template-columns:repeat(auto-fit,minmax(260px,1fr)); gap:18px; }}
    .anki-scene {{ perspective:1200px; }}
    .anki-card {{ position:relative; min-height:240px; transform-style:preserve-3d; transition:transform .6s; cursor:pointer; }}
    .anki-card.is-flipped {{ transform:rotateY(180deg); }}
    .anki-face {{ position:absolute; inset:0; backface-visibility:hidden; border-radius:12px; padding:20px; box-shadow:var(--shadow); }}
    .anki-front-face {{ background:#f5f5f7; color:#1d1d1f; }}
    .anki-back-face {{ background:#272729; color:#fff; transform:rotateY(180deg); }}
    .anki-front {{ font-family:"SF Pro Display","Helvetica Neue",Helvetica,Arial,sans-serif; font-size:28px; line-height:1.14; letter-spacing:0.196px; font-weight:400; margin-bottom:12px; }}
    .anki-back {{ font-size:17px; line-height:1.47; letter-spacing:-0.374px; white-space:pre-line; }}
    .flip-tip {{ margin-top:16px; font-size:12px; line-height:1.33; letter-spacing:-0.12px; opacity:.72; }}
    .speak-item {{ background:#fff; color:#1d1d1f; border-radius:12px; padding:18px; box-shadow:var(--shadow); margin-bottom:16px; }}
    .speak-item b {{ font-size:21px; line-height:1.19; letter-spacing:0.231px; font-family:"SF Pro Display","Helvetica Neue",Helvetica,Arial,sans-serif; }}
    .footer-note {{ margin-top:16px; font-size:14px; line-height:1.43; letter-spacing:-0.224px; opacity:.74; }}
    .pager {{ display:flex; justify-content:space-between; gap:12px; flex-wrap:wrap; margin-top:22px; }}
    .pager a {{ display:inline-flex; align-items:center; justify-content:center; min-height:40px; padding:8px 18px; border-radius:980px; text-decoration:none; font-size:17px; font-weight:400; background:transparent; color:var(--link); border:1px solid var(--link); }}
    .pager a:hover {{ text-decoration:none; }}
    .muted-dark {{ color:var(--text-muted-dark); }}
    .muted-light {{ color:var(--text-muted-light); }}
    @media (max-width: 768px) {{
      .display {{ font-size:40px; line-height:1.1; }}
      .section-title {{ font-size:32px; }}
      .hero {{ padding:64px 20px 56px; }}
      .inner {{ padding:44px 20px; }}
    }}
  </style>
  <script>
    let speechRate = 0.95;
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
    function setSpeechRate(rate, btn) {{
      speechRate = rate;
      document.querySelectorAll('.speed-chip').forEach(el => el.classList.remove('active'));
      if (btn) btn.classList.add('active');
    }}
    function stopSpeech() {{
      if ('speechSynthesis' in window) window.speechSynthesis.cancel();
    }}
    function speakText(text) {{
      if (!('speechSynthesis' in window)) {{ alert('当前浏览器不支持朗读功能'); return; }}
      window.speechSynthesis.cancel();
      const utter = new SpeechSynthesisUtterance(text);
      utter.lang = 'en-US';
      utter.rate = speechRate;
      window.speechSynthesis.speak(utter);
    }}
    function speakMany(texts) {{
      if (!('speechSynthesis' in window)) {{ alert('当前浏览器不支持朗读功能'); return; }}
      window.speechSynthesis.cancel();
      const queue = [...texts];
      function next() {{
        const text = queue.shift();
        if (!text) return;
        const utter = new SpeechSynthesisUtterance(text);
        utter.lang = 'en-US';
        utter.rate = speechRate;
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
            f'<div class="speak-item">'
            f'<div><b>{sentence}</b></div>'
            f'<div class="tool-row"><button class="speak-btn" onclick="speakText(\'{sentence_js}\')">🔊 朗读本句</button></div>'
            f'<div class="muted-light">中文：{cn}</div>'
            f'<div class="muted-light">提示：{tip}</div>'
            f'</div>'
        )
    prev_link = f'./day-{n-1:02d}.html' if n > 1 else './days.html'
    next_link = f'./day-{n+1:02d}.html' if n < TOTAL_DAYS else './days.html'
    prev_label = f'← Day {n-1:02d}' if n > 1 else '← 返回计划'
    next_label = f'Day {n+1:02d} →' if n < TOTAL_DAYS else '返回计划 →'
    speed_tools = '''
    <div class="tool-row">
      <button class="speed-chip" onclick="setSpeechRate(0.8, this)">0.8x</button>
      <button class="speed-chip active" onclick="setSpeechRate(0.95, this)">1.0x</button>
      <button class="speed-chip" onclick="setSpeechRate(1.2, this)">1.2x</button>
      <button class="speak-btn" onclick="stopSpeech()">⏹ 停止朗读</button>
    </div>
    '''
    body = f'''
    <section class="section-dark hero">
      <div class="inner">
        <span class="eyebrow">Day {n:02d}</span>
        <h1 class="display">{html.escape(theme)}</h1>
        <p class="subtitle">按 DESIGN.md 风格重构的学习页，保留 Anki、晨读、朗读与导航能力，但整体更克制、更统一、更接近高质量产品站。</p>
      </div>
    </section>
    <section class="section-light">
      <div class="inner">
        {speed_tools}
        <div class="tabs">
          <button class="tab-btn active" onclick="switchTab('anki', this)">Anki 抽卡</button>
          <button class="tab-btn" onclick="switchTab('speaking', this)">晨读口语</button>
        </div>
        <div id="anki" class="tab-panel active">
          <h2 class="section-title">Anki 抽卡</h2>
          <p class="section-copy muted-light">卡片正反面采用明暗对照的视觉处理，突出“识别—回忆—确认”的学习节奏。</p>
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
    </section>
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
            f'<div class="overview-card"><span class="badge">Day {n:02d}</span>'
            f'<h3 class="card-title"><a href="./day-{n:02d}.html">{html.escape(theme)}</a></h3>'
            f'<p class="card-copy">翻面卡片、晨读切换、朗读控制与上下日导航。</p></div>'
        )
    body = f'''
    <section class="section-dark hero">
      <div class="inner">
        <span class="eyebrow">Garena Test OpenClaw</span>
        <h1 class="display">静态学习站</h1>
        <p class="subtitle">以更克制的 DESIGN.md 风格重构的静态学习页面，突出内容本身，减少装饰噪音，让学习路径、卡片与朗读成为主角。</p>
        <div class="cta-row">
          <a class="btn-primary" href="./days.html">开始 30 天计划</a>
          <a class="btn-secondary" href="../README.md">查看仓库说明</a>
        </div>
      </div>
    </section>
    <section class="section-light">
      <div class="inner">
        <h2 class="section-title">核心能力</h2>
        <p class="section-copy muted-light">保留学习站的功能密度，但用更统一的配色、排版和组件节奏，提升整体完成度。</p>
        <div class="grid">
          <div class="overview-card"><h3 class="card-title">30 天学习计划</h3><p class="card-copy">按天组织，适合持续积累和复习。</p></div>
          <div class="overview-card"><h3 class="card-title">翻面 Anki 卡片</h3><p class="card-copy">点击翻面，强化识别与回忆。</p></div>
          <div class="overview-card"><h3 class="card-title">晨读口语</h3><p class="card-copy">支持单句朗读、整页朗读与语速控制。</p></div>
        </div>
      </div>
    </section>
    <section class="section-dark">
      <div class="inner">
        <h2 class="section-title">推荐从这些内容开始</h2>
        <div class="grid">{''.join(cards)}</div>
      </div>
    </section>
    '''
    (SITE / 'index.html').write_text(page_wrap('静态学习站首页', body), encoding='utf-8')


def export_days_index(days: list[tuple[int, str]]) -> None:
    cards = []
    for n, theme in days:
        cards.append(
            f'<div class="overview-card"><span class="badge">Day {n:02d}</span>'
            f'<h3 class="card-title"><a href="./day-{n:02d}.html">{html.escape(theme)}</a></h3>'
            f'<p class="card-copy">Anki 抽卡、晨读口语、朗读控制与上下日导航。</p></div>'
        )
    body = f'''
    <section class="section-dark hero">
      <div class="inner">
        <span class="eyebrow">30 Days Plan</span>
        <h1 class="display">30 天学习计划</h1>
        <p class="subtitle">点击任意一天进入学习页，可切换查看 Anki 抽卡与晨读口语，并使用朗读与语速控制功能。</p>
      </div>
    </section>
    <section class="section-light">
      <div class="inner">
        <div class="grid days-grid">{''.join(cards)}</div>
      </div>
    </section>
    '''
    (SITE / 'days.html').write_text(page_wrap('30 天学习计划', body), encoding='utf-8')


def main() -> None:
    SITE.mkdir(parents=True, exist_ok=True)
    days = export_days()
    export_index(days)
    export_days_index(days)


if __name__ == '__main__':
    main()
