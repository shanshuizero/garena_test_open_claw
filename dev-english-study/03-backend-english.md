# 后端开发英语词汇

> 聚焦服务端、接口设计、并发、消息处理、稳定性与系统行为。

---

## 1. endpoint
- 发音：/ˈendpɔɪnt/
- 含义：接口端点
- 开发语境：API 的访问地址。
- 例句：This endpoint returns the user profile data.
- 翻译：这个接口端点返回用户资料数据。
- 讲解：`returns ... data` 是描述接口职责的基础结构。

## 2. service
- 发音：/ˈsɜːrvɪs/
- 含义：服务
- 开发语境：业务服务、微服务、系统服务。
- 例句：The notification service is temporarily unavailable.
- 翻译：通知服务暂时不可用。
- 讲解：`temporarily unavailable` 是状态告警中的高频表达。

## 3. controller
- 发音：/kənˈtroʊlər/
- 含义：控制器
- 开发语境：MVC 或接口入口层。
- 例句：Keep the controller thin and move the logic to the service layer.
- 翻译：让控制器保持轻量，把逻辑移到服务层。
- 讲解：`keep ... thin` 是后端分层设计中的常见建议。

## 4. authentication
- 发音：/əˌθentɪˈkeɪʃən/
- 含义：身份认证
- 开发语境：确认用户是谁。
- 例句：Authentication fails when the token expires.
- 翻译：当令牌过期时，身份认证会失败。
- 讲解：`fails when ...` 很适合描述触发条件。

## 5. authorization
- 发音：/ˌɔːθərəˈzeɪʃən/
- 含义：授权
- 开发语境：确认用户能做什么。
- 例句：Authorization should be enforced on the server side.
- 翻译：授权校验应该在服务端强制执行。
- 讲解：认证和授权经常一起出现，但意思不同。

## 6. token
- 发音：/ˈtoʊkən/
- 含义：令牌
- 开发语境：JWT、访问令牌、刷新令牌。
- 例句：The access token is stored in memory.
- 翻译：访问令牌存储在内存中。
- 讲解：`access token` 是接口安全的基础词组。

## 7. session
- 发音：/ˈseʃən/
- 含义：会话
- 开发语境：用户登录状态、服务端 session 管理。
- 例句：The user session times out after thirty minutes of inactivity.
- 翻译：用户会话会在三十分钟无操作后超时。
- 讲解：`times out after ...` 是超时机制的高频表达。

## 8. cache
- 发音：/kæʃ/
- 含义：缓存
- 开发语境：Redis、本地缓存、接口缓存。
- 例句：We should cache this result to reduce database pressure.
- 翻译：我们应该缓存这个结果，以减少数据库压力。
- 讲解：`reduce database pressure` 很自然，常用于性能讨论。

## 9. queue
- 发音：/kjuː/
- 含义：队列
- 开发语境：消息队列、任务排队。
- 例句：The email jobs are processed through a message queue.
- 翻译：这些邮件任务通过消息队列处理。
- 讲解：`processed through` 表示“通过……处理”。

## 10. worker
- 发音：/ˈwɜːrkər/
- 含义：工作进程；消费者
- 开发语境：后台异步任务执行单元。
- 例句：The worker retries failed tasks automatically.
- 翻译：这个工作进程会自动重试失败任务。
- 讲解：`retries failed tasks` 是异步系统常见职责描述。

## 11. retry
- 发音：/ˌriːˈtraɪ/
- 含义：重试
- 开发语境：请求失败后的补偿机制。
- 例句：We added a retry mechanism for transient network errors.
- 翻译：我们为临时性网络错误增加了重试机制。
- 讲解：`transient` 指“暂时性的、瞬时的”。

## 12. timeout
- 发音：/ˈtaɪmaʊt/
- 含义：超时
- 开发语境：请求超时、连接超时、任务超时。
- 例句：The request fails because of a database timeout.
- 翻译：这个请求因为数据库超时而失败。
- 讲解：`because of` 说明直接原因。

## 13. concurrency
- 发音：/kənˈkɜːrənsi/
- 含义：并发
- 开发语境：同时处理多个请求或任务的能力。
- 例句：This design improves concurrency without increasing complexity too much.
- 翻译：这个设计提升了并发能力，同时没有明显增加复杂度。
- 讲解：是系统设计和面试中的关键词。

## 14. transaction
- 发音：/trænˈzækʃən/
- 含义：事务
- 开发语境：数据库事务，保证一组操作一致性。
- 例句：The transaction should be rolled back if any step fails.
- 翻译：如果任何一步失败，这个事务都应该回滚。
- 讲解：`rolled back` 是事务语境里的固定表达。

## 15. persistence
- 发音：/pərˈsɪstəns/
- 含义：持久化
- 开发语境：把内存中的数据保存到数据库或存储系统。
- 例句：The persistence layer should not contain business logic.
- 翻译：持久化层不应该包含业务逻辑。
- 讲解：强调分层职责划分。

## 16. serialization
- 发音：/ˌsɪriələˈzeɪʃən/
- 含义：序列化
- 开发语境：将对象转换为可传输或可存储格式。
- 例句：Serialization adds overhead to large responses.
- 翻译：序列化会给大响应增加额外开销。
- 讲解：`adds overhead` 是性能讨论常用表达。

## 17. deserialization
- 发音：/diːˌsɪriələˈzeɪʃən/
- 含义：反序列化
- 开发语境：把字符串或二进制还原成对象。
- 例句：The error happens during JSON deserialization.
- 翻译：这个错误发生在 JSON 反序列化过程中。
- 讲解：定位问题时经常会说 `during ...`。

## 18. throughput
- 发音：/ˈθruːpʊt/
- 含义：吞吐量
- 开发语境：单位时间处理请求或数据的能力。
- 例句：We improved throughput by batching writes.
- 翻译：我们通过批量写入提高了吞吐量。
- 讲解：`by batching writes` 点明优化手段。

## 19. latency
- 发音：/ˈleɪtənsi/
- 含义：延迟
- 开发语境：请求响应耗时。
- 例句：The average latency is acceptable, but the tail latency is too high.
- 翻译：平均延迟可以接受，但尾延迟太高了。
- 讲解：`tail latency` 是性能优化中的专业表达。

## 20. failover
- 发音：/ˈfeɪloʊvər/
- 含义：故障切换
- 开发语境：主节点出问题时切换到备节点。
- 例句：Automatic failover did not work as expected.
- 翻译：自动故障切换没有按预期工作。
- 讲解：`as expected` 表示“按预期”。

## 21. recovery
- 发音：/rɪˈkʌvəri/
- 含义：恢复
- 开发语境：故障恢复、数据恢复、服务恢复。
- 例句：The recovery process took longer than expected.
- 翻译：恢复过程比预期更久。
- 讲解：故障处理复盘里很常见。

## 22. idempotent
- 发音：/ˌaɪdəmˈpoʊtənt/
- 含义：幂等的
- 开发语境：多次请求产生相同结果，不造成重复副作用。
- 例句：This payment callback must be idempotent.
- 翻译：这个支付回调必须是幂等的。
- 讲解：支付、订单、消息消费场景里非常关键。

## 23. cron job
- 发音：/krɑːn dʒɑːb/
- 含义：定时任务
- 开发语境：按固定时间执行后台任务。
- 例句：A cron job cleans up expired sessions every night.
- 翻译：一个定时任务每晚清理过期会话。
- 讲解：`cleans up` 表示“清理掉”。

## 24. rate limit
- 发音：/reɪt ˈlɪmɪt/
- 含义：限流
- 开发语境：限制单位时间内的请求次数。
- 例句：We should add rate limiting to this public API.
- 翻译：我们应该给这个公开 API 加上限流。
- 讲解：公开接口常常需要 `rate limiting`。

## 25. circuit breaker
- 发音：/ˈsɜːrkɪt ˌbreɪkər/
- 含义：熔断器
- 开发语境：下游服务异常时快速失败，防止级联故障。
- 例句：A circuit breaker can protect the system from cascading failures.
- 翻译：熔断器可以保护系统免受级联故障影响。
- 讲解：`cascading failures` 是分布式系统中的经典术语。
