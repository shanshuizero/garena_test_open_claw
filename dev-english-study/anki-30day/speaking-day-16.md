# Speaking Day 16：消息系统 / 幂等 / 重试

## 晨读短句
1. Failed messages are routed to the dead letter queue.
   - 中文：死信队列
   - 提示：消息失败处理

2. Each partition is assigned to one consumer group member.
   - 中文：消费者组
   - 提示：Kafka 高频

3. The consumer committed the offset too early.
   - 中文：偏移量
   - 提示：消费进度

4. Exactly-once processing is difficult in distributed systems.
   - 中文：恰好一次
   - 提示：消息语义

5. At-least-once delivery requires idempotent consumers.
   - 中文：至少一次
   - 提示：与幂等搭配记

## 跟读提示
- 先慢读 2 遍
- 再正常语速读 3 遍
- 最后脱稿复述其中 2 句
