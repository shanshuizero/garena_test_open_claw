from __future__ import annotations

import re
import sqlite3
from datetime import datetime
from pathlib import Path
from typing import Any

from flask import Flask, abort, jsonify, render_template, request
from markdown import markdown

BASE_DIR = Path(__file__).resolve().parent
WORKSPACE_DIR = BASE_DIR.parent
STUDY_DIR = WORKSPACE_DIR / "dev-english-study"
ANKI_DIR = STUDY_DIR / "anki-30day"
DB_PATH = BASE_DIR / "study.db"

app = Flask(__name__)


def get_conn() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def get_day_row(day_number: int) -> sqlite3.Row | None:
    conn = get_conn()
    row = conn.execute("SELECT * FROM days WHERE day_number = ?", (day_number,)).fetchone()
    conn.close()
    return row


def init_db() -> None:
    conn = get_conn()
    conn.executescript(
        """
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            path TEXT NOT NULL UNIQUE,
            category TEXT NOT NULL,
            content TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS days (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day_number INTEGER NOT NULL UNIQUE,
            theme TEXT NOT NULL,
            anki_path TEXT NOT NULL,
            speaking_path TEXT NOT NULL,
            anki_content TEXT NOT NULL,
            speaking_content TEXT NOT NULL
        );

        CREATE TABLE IF NOT EXISTS daily_pushes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day_number INTEGER NOT NULL,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            created_at TEXT NOT NULL,
            UNIQUE(day_number)
        );
        """
    )
    conn.commit()
    conn.close()


def file_title(path: Path) -> str:
    text = path.read_text(encoding="utf-8", errors="ignore")
    for line in text.splitlines():
        if line.startswith("# "):
            return line[2:].strip()
    return path.stem


def category_for(path: Path) -> str:
    if "anki-30day" in str(path):
        return "anki-30day"
    if "cards" in str(path):
        return "cards"
    return "study"


def import_documents() -> None:
    conn = get_conn()
    files = sorted(STUDY_DIR.glob("*.md")) + sorted((STUDY_DIR / "cards").glob("*.md"))
    for path in files:
        content = path.read_text(encoding="utf-8", errors="ignore")
        conn.execute(
            """
            INSERT INTO documents (title, path, category, content)
            VALUES (?, ?, ?, ?)
            ON CONFLICT(path) DO UPDATE SET
                title=excluded.title,
                category=excluded.category,
                content=excluded.content
            """,
            (file_title(path), str(path.relative_to(WORKSPACE_DIR)), category_for(path), content),
        )
    conn.commit()
    conn.close()


def import_days() -> None:
    conn = get_conn()
    day_files = sorted(ANKI_DIR.glob("anki-day-*.md"))
    for anki_path in day_files:
        match = re.search(r"anki-day-(\d{2})\.md$", anki_path.name)
        if not match:
            continue
        day_number = int(match.group(1))
        speaking_path = ANKI_DIR / f"speaking-day-{day_number:02d}.md"
        if not speaking_path.exists():
            continue
        anki_content = anki_path.read_text(encoding="utf-8", errors="ignore")
        speaking_content = speaking_path.read_text(encoding="utf-8", errors="ignore")
        title = file_title(anki_path)
        theme = title.split("：", 1)[-1].strip() if "：" in title else title
        conn.execute(
            """
            INSERT INTO days (
                day_number, theme, anki_path, speaking_path, anki_content, speaking_content
            ) VALUES (?, ?, ?, ?, ?, ?)
            ON CONFLICT(day_number) DO UPDATE SET
                theme=excluded.theme,
                anki_path=excluded.anki_path,
                speaking_path=excluded.speaking_path,
                anki_content=excluded.anki_content,
                speaking_content=excluded.speaking_content
            """,
            (
                day_number,
                theme,
                str(anki_path.relative_to(WORKSPACE_DIR)),
                str(speaking_path.relative_to(WORKSPACE_DIR)),
                anki_content,
                speaking_content,
            ),
        )
    conn.commit()
    conn.close()


def current_day_number() -> int:
    now = datetime.now()
    return ((now.day - 1) % 30) + 1


def render_md(text: str) -> str:
    return markdown(text, extensions=["fenced_code", "tables"])


def generate_push_html(day_row: sqlite3.Row) -> str:
    title = f"Day {day_row['day_number']:02d}｜{day_row['theme']}"
    anki_html = render_md(day_row["anki_content"])
    speaking_html = render_md(day_row["speaking_content"])
    return (
        f"<h2>{title}</h2>"
        f"<h3>Anki 抽卡</h3>{anki_html}"
        f"<h3>晨读口语</h3>{speaking_html}"
    )


def upsert_push(day_number: int, title: str, content: str) -> None:
    conn = get_conn()
    conn.execute(
        """
        INSERT INTO daily_pushes (day_number, title, content, created_at)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(day_number) DO UPDATE SET
            title=excluded.title,
            content=excluded.content,
            created_at=excluded.created_at
        """,
        (day_number, title, content, datetime.now().isoformat(timespec="seconds")),
    )
    conn.commit()
    conn.close()


def upsert_today_push() -> None:
    day_number = current_day_number()
    day_row = get_day_row(day_number)
    if day_row is None:
        return
    title = f"Day {day_number:02d}｜{day_row['theme']}"
    content = generate_push_html(day_row)
    upsert_push(day_number, title, content)


def bootstrap() -> None:
    init_db()
    import_documents()
    import_days()
    upsert_today_push()


@app.route("/")
def index() -> str:
    conn = get_conn()
    stats = {
        "doc_count": conn.execute("SELECT COUNT(*) FROM documents").fetchone()[0],
        "day_count": conn.execute("SELECT COUNT(*) FROM days").fetchone()[0],
        "push_count": conn.execute("SELECT COUNT(*) FROM daily_pushes").fetchone()[0],
    }
    conn.close()
    return render_template("index.html", title="首页", stats=stats)


@app.route("/docs")
def docs() -> str:
    conn = get_conn()
    rows = conn.execute(
        "SELECT id, title, path, category FROM documents ORDER BY category, path"
    ).fetchall()
    conn.close()
    return render_template("docs.html", title="全部资料", docs=rows)


@app.route("/doc/<int:doc_id>")
def doc_detail(doc_id: int) -> str:
    conn = get_conn()
    row = conn.execute("SELECT * FROM documents WHERE id = ?", (doc_id,)).fetchone()
    conn.close()
    if row is None:
        abort(404)
    return render_template(
        "doc.html",
        title=row["title"],
        doc=row,
        html=render_md(row["content"]),
    )


@app.route("/days")
def days() -> str:
    conn = get_conn()
    rows = conn.execute(
        "SELECT day_number, theme FROM days ORDER BY day_number"
    ).fetchall()
    conn.close()
    return render_template("days.html", title="30天计划", days=rows)


@app.route("/day/<int:day_number>")
def day_detail(day_number: int) -> str:
    row = get_day_row(day_number)
    if row is None:
        abort(404)
    return render_template(
        "day.html",
        title=f"Day {day_number:02d}",
        day=row,
        anki_html=render_md(row["anki_content"]),
        speaking_html=render_md(row["speaking_content"]),
    )


@app.route("/daily/today")
def daily_today() -> str:
    day_number = current_day_number()
    row = get_day_row(day_number)
    if row is None:
        abort(404)
    return render_template(
        "daily.html",
        title="今日推送页",
        day=row,
        anki_html=render_md(row["anki_content"]),
        speaking_html=render_md(row["speaking_content"]),
    )


@app.route("/pushes")
def pushes() -> str:
    q = (request.args.get("q") or "").strip()
    day = (request.args.get("day") or "").strip()
    sql = "SELECT id, day_number, title, content, created_at FROM daily_pushes WHERE 1=1"
    params: list[object] = []
    if q:
        sql += " AND (title LIKE ? OR content LIKE ?)"
        like = f"%{q}%"
        params.extend([like, like])
    if day.isdigit():
        sql += " AND day_number = ?"
        params.append(int(day))
    sql += " ORDER BY day_number, created_at DESC"
    conn = get_conn()
    rows = conn.execute(sql, params).fetchall()
    conn.close()
    enriched = []
    for row in rows:
        item = dict(row)
        preview = re.sub(r"<[^>]+>", "", item["content"])
        item["preview"] = preview.replace("\n", " ")[:180]
        enriched.append(item)
    return render_template(
        "pushes.html",
        title="推送记录",
        pushes=enriched,
        q=q,
        day=day,
    )


@app.route("/push/<int:push_id>")
def push_detail(push_id: int) -> str:
    conn = get_conn()
    row = conn.execute("SELECT * FROM daily_pushes WHERE id = ?", (push_id,)).fetchone()
    conn.close()
    if row is None:
        abort(404)
    return render_template(
        "push.html",
        title=row["title"],
        push=row,
        html=row["content"],
    )


@app.route("/api/docs")
def api_docs() -> Any:
    conn = get_conn()
    rows = conn.execute(
        "SELECT id, title, path, category FROM documents ORDER BY category, path"
    ).fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])


@app.route("/api/pushes")
def api_pushes() -> Any:
    conn = get_conn()
    rows = conn.execute(
        "SELECT id, day_number, title, created_at FROM daily_pushes ORDER BY day_number"
    ).fetchall()
    conn.close()
    return jsonify([dict(row) for row in rows])


@app.route("/api/pushes/upsert", methods=["POST"])
def api_pushes_upsert() -> Any:
    data = request.get_json(silent=True) or {}
    day_number = int(data.get("day_number") or current_day_number())
    title = str(data.get("title") or f"Day {day_number:02d}")
    content = str(data.get("content") or "")
    if not content.strip():
        return jsonify({"ok": False, "error": "content is required"}), 400
    upsert_push(day_number, title, content)
    return jsonify({"ok": True, "day_number": day_number, "title": title})


if __name__ == "__main__":
    bootstrap()
    app.run(host="0.0.0.0", port=5010, debug=False)
