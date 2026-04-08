# 书面表达模板：邮件、日报、周报、PR、Issue、会议纪要

> 这一部分强调“能直接拿去用”的英文书面表达模板。

---

## 1. 日报 Daily Update

### 模板
Today I worked on the user authentication flow and fixed two issues related to token refresh.

I also reviewed the API contract with the frontend team.

Tomorrow I plan to finish the remaining test cases and verify the fix in staging.

At the moment, I am blocked by a permission issue in the deployment environment.

### 中文参考
今天我处理了用户认证流程，并修复了两个和 token 刷新相关的问题。

我还和前端团队一起过了一遍 API 契约。

明天我计划完成剩余测试用例，并在预发环境验证修复。

目前我被部署环境的权限问题卡住了。

---

## 2. 周报 Weekly Update

### 模板
This week I focused on improving API stability and reducing response latency in the order service.

The main achievements were:
- reduced the average response time by 25%
- added caching for frequently accessed data
- fixed a regression in the payment callback logic

The main challenge was coordinating changes across multiple teams.

Next week I will continue with the monitoring improvements and database optimization work.

### 中文参考
这周我主要在提升 API 稳定性，并降低订单服务的响应延迟。

主要成果包括：
- 平均响应时间降低了 25%
- 为高频访问数据增加了缓存
- 修复了支付回调逻辑中的回归问题

最大的挑战是跨多个团队协调改动。

下周我会继续做监控优化和数据库优化工作。

---

## 3. PR 描述 Pull Request Description

### 模板
## Summary
This PR refactors the notification module and adds retry handling for failed delivery attempts.

## Changes
- extracted the delivery logic into a separate service
- added retry and timeout handling
- improved logging for failure scenarios
- added unit tests for the new code paths

## Risk
The change should be backward compatible, but extra attention should be paid to the retry behavior in staging.

## Verification
- unit tests passed
- manually tested in staging
- verified log output for failure cases

### 中文参考
## 摘要
这个 PR 重构了通知模块，并为投递失败场景增加了重试处理。

## 改动
- 将投递逻辑拆到独立服务中
- 增加了重试和超时处理
- 改善了失败场景下的日志
- 为新的代码路径补充了单元测试

## 风险
这个改动理论上向后兼容，但需要特别关注预发环境中的重试行为。

## 验证
- 单元测试已通过
- 已在预发环境手动测试
- 已验证失败场景下的日志输出

---

## 4. PR 评论 Pull Request Comment

### 模板 1：温和建议
I think this logic is correct, but it may be easier to maintain if we split it into smaller functions.

### 模板 2：提出风险
One concern is that this change may break older clients that still expect the previous response format.

### 模板 3：礼貌认可
Thanks for the update. The overall direction looks good to me.

### 中文参考
- 我认为这段逻辑是对的，但如果拆成更小的函数，维护起来可能会更容易。
- 一个顾虑是，这个改动可能会影响仍然依赖旧响应格式的老客户端。
- 感谢更新。整体方向我看起来是不错的。

---

## 5. Issue 回复 Issue Response

### 模板
Thanks for reporting this issue.

We have been able to reproduce the problem in staging, and the root cause is currently under investigation.

As a temporary workaround, please retry the request after refreshing the session.

We will update this thread once a fix is available.

### 中文参考
感谢你反馈这个问题。

我们已经能在预发环境复现该问题，目前正在排查根因。

临时解决办法是刷新会话后重试请求。

一旦修复可用，我们会更新这个帖子。

---

## 6. 会议纪要 Meeting Notes

### 模板
## Topic
Notification service redesign

## Key Decisions
- separate the write path from the delivery path
- add retry handling with exponential backoff
- introduce a dead letter queue for failed messages

## Open Questions
- how long should failed messages be retained?
- should retries be handled per message type?

## Next Steps
- backend team to draft the API contract
- frontend team to review the response schema
- DevOps team to prepare monitoring dashboards

### 中文参考
## 主题
通知服务重设计

## 关键决定
- 将写入路径和投递路径拆分
- 增加指数退避重试处理
- 为失败消息引入死信队列

## 未决问题
- 失败消息应该保留多久？
- 是否需要按消息类型分别配置重试？

## 下一步
- 后端团队起草 API 契约
- 前端团队审查响应结构
- DevOps 团队准备监控看板

---

## 7. 催进度 / 跟进 Follow-up Message

### 模板
Hi team, just following up on the API contract discussion from yesterday.

Do we already have a final decision on the response structure?

This affects both the frontend implementation and the test plan, so it would be helpful to confirm it today if possible.

### 中文参考
大家好，我跟进一下昨天关于 API 契约的讨论。

我们现在对响应结构已经有最终结论了吗？

这会影响前端实现和测试计划，所以如果可以的话，今天确认下来会比较好。
