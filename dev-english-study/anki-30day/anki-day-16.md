# Anki Day 16：消息系统 / 幂等 / 重试

## 卡片格式
Front｜Back

1. **Front**: dead letter queue
   **Back**: 死信队列｜Failed messages are routed to the dead letter queue.｜提示：消息失败处理

2. **Front**: consumer group
   **Back**: 消费者组｜Each partition is assigned to one consumer group member.｜提示：Kafka 高频

3. **Front**: offset
   **Back**: 偏移量｜The consumer committed the offset too early.｜提示：消费进度

4. **Front**: exactly-once
   **Back**: 恰好一次｜Exactly-once processing is difficult in distributed systems.｜提示：消息语义

5. **Front**: at-least-once
   **Back**: 至少一次｜At-least-once delivery requires idempotent consumers.｜提示：与幂等搭配记
