# English Study Web

一个基于 Python Flask 的轻量 Web 服务，用来：

- 扫描并导入 `dev-english-study/` 下的英文学习资料
- 将资料元数据和内容存入 SQLite
- 生成可浏览的网页
- 单独展示 30 天 Anki / 晨读口语页面
- 提供每日推送页面

## 运行

```bash
cd english_study_web
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

默认地址：

- `http://127.0.0.1:5010`

## 页面

- `/` 首页
- `/docs` 全部资料
- `/doc/<id>` 单篇资料
- `/days` 30 天学习计划
- `/day/<n>` 第 n 天详情
- `/daily/today` 今日推送页
- `/api/docs` JSON 接口
