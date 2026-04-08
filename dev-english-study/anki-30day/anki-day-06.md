# Anki Day 06：后端基础 2

## 卡片格式
Front｜Back

1. **Front**: cache
   **Back**: 缓存｜We should cache this result to reduce database pressure.｜提示：性能优化

2. **Front**: queue
   **Back**: 队列｜The jobs are processed through a message queue.｜提示：异步系统

3. **Front**: timeout
   **Back**: 超时｜The request fails because of a database timeout.｜提示：线上排障

4. **Front**: concurrency
   **Back**: 并发｜This design improves concurrency.｜提示：系统设计核心

5. **Front**: idempotent
   **Back**: 幂等的｜This callback must be idempotent.｜提示：支付/消息高频
