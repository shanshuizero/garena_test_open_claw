# Garena Test OpenClaw

一个基于 OpenClaw 工作区构建的英文学习资料仓库，包含：

- 面向前后端开发的专业英语学习资料
- 30 天 Anki 抽卡与晨读口语计划
- 一个 Python Flask Web 服务，用于展示学习资料、每日计划与推送记录
- 每日学习推送与网页入库同步方案

## 仓库结构

### `dev-english-study/`
开发英语学习资料主目录：

- 通用开发英语
- 前端英语
- 后端英语
- API / 数据库 / DevOps
- 测试 / 安全 / 系统设计
- 面试 / 工作对话 / 书面表达
- 30 天背诵卡片
- 30 天 Anki + 晨读口语

### `english_study_web/`
Python Web 服务：

- Flask 应用入口：`app.py`
- 页面模板：`templates/`
- systemd 服务文件：`english-study-web.service`
- 每日推送同步脚本：`sync_daily_push.py`
- cron 包装脚本：`cron-sync-daily-push.sh`

## Web 服务功能

- 浏览全部学习资料
- 查看 30 天学习计划
- 展示每日推送内容
- 保存并展示推送记录
- 支持推送记录时间线、搜索和 Day 筛选

## 本地运行

```bash
cd english_study_web
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

默认地址：

- `http://127.0.0.1:5010`

## 生产运行思路

仓库内已提供：

- `english-study-web.service`：systemd 常驻服务
- `cron-sync-daily-push.sh`：每日推送内容同步入库脚本

## 说明

本仓库保留的是适合公开分享的学习资料与服务代码。
本地运行态文件、私有工作区状态文件、虚拟环境、数据库与用户私有配置已从版本控制中排除。
