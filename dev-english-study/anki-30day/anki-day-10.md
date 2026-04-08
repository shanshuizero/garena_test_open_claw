# Anki Day 10：系统设计 / 云原生

## 卡片格式
Front｜Back

1. **Front**: availability
   **Back**: 可用性｜We need higher availability during peak traffic hours.｜提示：系统稳定性

2. **Front**: consistency
   **Back**: 一致性｜Strong consistency may increase write latency.｜提示：分布式基础

3. **Front**: distributed lock
   **Back**: 分布式锁｜Use a distributed lock to prevent duplicate execution.｜提示：防止重复执行

4. **Front**: horizontal scaling
   **Back**: 水平扩展｜Horizontal scaling is easier for stateless services.｜提示：扩容方式

5. **Front**: resilience
   **Back**: 韧性｜Retries and fallback strategies improve system resilience.｜提示：系统恢复能力
