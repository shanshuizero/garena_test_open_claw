# 后端专项英语：微服务 / 分布式 / 数据库 / 消息系统 / 稳定性

> 这部分面向后端开发实战，覆盖服务治理、数据库设计、异步系统、高并发与稳定性表达。

---

## 1. microservice
- 发音：/ˈmaɪkroʊˌsɜːrvɪs/
- 含义：微服务
- 开发语境：把系统拆成多个独立部署、独立演进的小服务。
- 例句：Each microservice should have a clear business boundary.
- 翻译：每个微服务都应该有清晰的业务边界。
- 讲解：`business boundary` 是微服务设计中的核心概念。

## 2. service boundary
- 发音：短语表达
- 含义：服务边界
- 开发语境：定义某个服务负责什么、不负责什么。
- 例句：The service boundary is too broad and needs to be refined.
- 翻译：这个服务边界太宽了，需要进一步收敛。
- 讲解：架构评审里非常常见。

## 3. service contract
- 发音：短语表达
- 含义：服务契约
- 开发语境：服务之间约定的接口输入输出和行为。
- 例句：Breaking the service contract will affect downstream teams.
- 翻译：破坏服务契约会影响下游团队。
- 讲解：`downstream teams` 也是高频术语。

## 4. downstream
- 发音：/ˌdaʊnˈstriːm/
- 含义：下游
- 开发语境：依赖当前服务输出的其他服务或系统。
- 例句：A latency spike in this service will impact all downstream consumers.
- 翻译：这个服务的延迟尖峰会影响所有下游消费者。
- 讲解：分布式调用关系中必会遇到。

## 5. upstream
- 发音：/ˌʌpˈstriːm/
- 含义：上游
- 开发语境：当前服务所依赖的来源系统或调用方。
- 例句：The malformed data comes from an upstream provider.
- 翻译：这些格式错误的数据来自上游提供方。
- 讲解：排查问题时很常说。

## 6. service mesh
- 发音：/ˈsɜːrvɪs meʃ/
- 含义：服务网格
- 开发语境：为服务通信提供流量管理、安全和可观测能力。
- 例句：The service mesh adds observability without changing application code.
- 翻译：服务网格无需修改应用代码就能增加可观测能力。
- 讲解：云原生架构中常见概念。

## 7. API gateway
- 发音：/ˌeɪ piː ˈaɪ ˈɡeɪtweɪ/
- 含义：API 网关
- 开发语境：统一处理路由、认证、限流、聚合等能力。
- 例句：The API gateway handles authentication and rate limiting.
- 翻译：API 网关负责认证和限流。
- 讲解：是前后端协作中常见的基础设施词汇。

## 8. fan-out
- 发音：/fæn aʊt/
- 含义：扇出
- 开发语境：一个请求触发多个下游请求。
- 例句：This endpoint has a large fan-out and is hard to optimize.
- 翻译：这个接口扇出很大，因此难以优化。
- 讲解：在性能和依赖分析中常出现。

## 9. cascading failure
- 发音：/kæˈskeɪdɪŋ ˈfeɪljər/
- 含义：级联故障
- 开发语境：一个服务故障逐步扩散到整个系统。
- 例句：Timeouts and retries can trigger cascading failures.
- 翻译：超时和重试可能引发级联故障。
- 讲解：稳定性设计必须理解这个概念。

## 10. backpressure
- 发音：/ˈbækˌpreʃər/
- 含义：背压
- 开发语境：系统通过控制流量防止下游过载。
- 例句：We need backpressure to protect the queue consumers.
- 翻译：我们需要背压机制来保护队列消费者。
- 讲解：流处理和高吞吐系统中很重要。

## 11. dead letter queue
- 发音：短语表达
- 含义：死信队列
- 开发语境：保存多次处理失败的消息。
- 例句：Failed messages are routed to the dead letter queue.
- 翻译：处理失败的消息会被路由到死信队列。
- 讲解：消息队列系统高频术语。

## 12. consumer group
- 发音：短语表达
- 含义：消费者组
- 开发语境：多个消费者实例共同消费同一类消息。
- 例句：Each partition is assigned to one consumer group member.
- 翻译：每个分区会分配给消费者组中的一个成员。
- 讲解：Kafka 等消息系统中非常常见。

## 13. partition key
- 发音：短语表达
- 含义：分区键
- 开发语境：决定消息或数据落到哪个分区。
- 例句：Choose the partition key carefully to avoid data skew.
- 翻译：要谨慎选择分区键，以避免数据倾斜。
- 讲解：`data skew` 是分布式存储和消息系统常见问题。

## 14. offset
- 发音：/ˈɔːfset/
- 含义：偏移量
- 开发语境：记录消息消费进度。
- 例句：The consumer committed the offset too early.
- 翻译：这个消费者提交偏移量提交得太早了。
- 讲解：消息语义和可靠性讨论里很高频。

## 15. exactly-once
- 发音：/ɪɡˈzæktli wʌns/
- 含义：恰好一次语义
- 开发语境：消息或操作既不丢失也不重复。
- 例句：Exactly-once processing is difficult in distributed systems.
- 翻译：在分布式系统中，实现恰好一次处理非常困难。
- 讲解：面试和架构讨论中的经典概念。

## 16. at-least-once
- 发音：/æt liːst wʌns/
- 含义：至少一次语义
- 开发语境：消息可能重复，但尽量不丢。
- 例句：At-least-once delivery requires idempotent consumers.
- 翻译：至少一次投递要求消费者具备幂等性。
- 讲解：和 idempotent 必须配套理解。

## 17. at-most-once
- 发音：/æt moʊst wʌns/
- 含义：至多一次语义
- 开发语境：消息不重复，但有可能丢失。
- 例句：At-most-once delivery is simpler but less reliable.
- 翻译：至多一次投递更简单，但可靠性更低。
- 讲解：三种消息语义建议放在一起记。

## 18. read replica
- 发音：短语表达
- 含义：只读副本
- 开发语境：把读流量从主库分摊出去。
- 例句：Read replicas reduce the load on the primary database.
- 翻译：只读副本可以减少主数据库的压力。
- 讲解：数据库扩展中非常高频。

## 19. primary key
- 发音：/ˈpraɪmeri kiː/
- 含义：主键
- 开发语境：标识表中一条记录的唯一键。
- 例句：The primary key should be stable and unique.
- 翻译：主键应该稳定且唯一。
- 讲解：数据库设计基础概念。

## 20. foreign key
- 发音：/ˈfɔːrən kiː/
- 含义：外键
- 开发语境：建立表与表之间的关联关系。
- 例句：The foreign key constraint prevents orphan records.
- 翻译：外键约束可以防止孤儿记录出现。
- 讲解：`orphan records` 是数据库关系讨论常见词。

## 21. denormalization
- 发音：/diːˌnɔːrmələˈzeɪʃən/
- 含义：反规范化
- 开发语境：为了查询性能而牺牲部分结构规范性。
- 例句：Denormalization can improve read performance at the cost of write complexity.
- 翻译：反规范化可以提升读性能，但代价是写入复杂度增加。
- 讲解：这是数据库设计里的经典 trade-off。

## 22. query plan
- 发音：/ˈkwɪri plæn/
- 含义：查询计划
- 开发语境：数据库执行 SQL 的步骤和策略。
- 例句：The query plan shows that the index is not being used.
- 翻译：查询计划显示这个索引没有被使用。
- 讲解：SQL 优化时非常常见。

## 23. connection pool
- 发音：/kəˈnekʃən puːl/
- 含义：连接池
- 开发语境：复用数据库或网络连接，减少创建开销。
- 例句：The connection pool was exhausted during peak traffic.
- 翻译：在流量高峰期，连接池被耗尽了。
- 讲解：线上性能故障高频原因之一。

## 24. thread-safe
- 发音：/θred seɪf/
- 含义：线程安全的
- 开发语境：在多线程环境下行为仍正确。
- 例句：This cache implementation is not thread-safe.
- 翻译：这个缓存实现不是线程安全的。
- 讲解：Java、Go、C++ 等后端语言里很常见。

## 25. race condition
- 发音：/reɪs kənˈdɪʃən/
- 含义：竞态条件
- 开发语境：多个并发操作导致时序问题。
- 例句：The duplicate order issue is caused by a race condition.
- 翻译：重复下单问题是由竞态条件引起的。
- 讲解：并发 bug 的经典根因之一。

## 26. lock contention
- 发音：/lɑːk kənˈtenʃən/
- 含义：锁竞争
- 开发语境：多个线程或事务争抢同一资源。
- 例句：Lock contention becomes severe under high concurrency.
- 翻译：在高并发下，锁竞争会变得很严重。
- 讲解：性能分析和数据库事务讨论常见。

## 27. eventual retry
- 发音：短语表达
- 含义：最终重试成功机制
- 开发语境：允许短期失败，依靠后续重试完成处理。
- 例句：This workflow relies on eventual retry instead of immediate success.
- 翻译：这个工作流依赖的是最终重试成功，而不是立刻成功。
- 讲解：适合异步解耦系统场景。

## 28. hot partition
- 发音：短语表达
- 含义：热点分区
- 开发语境：某个分区承担了过高流量或数据量。
- 例句：A poor partition strategy can create hot partitions.
- 翻译：不合理的分区策略会造成热点分区。
- 讲解：分库分表、Kafka、NoSQL 都会碰到。

## 29. write amplification
- 发音：/raɪt ˌæmplɪfɪˈkeɪʃən/
- 含义：写放大
- 开发语境：一次逻辑写操作引发多次实际写入。
- 例句：This storage engine suffers from high write amplification.
- 翻译：这个存储引擎存在较高的写放大问题。
- 讲解：数据库和存储系统进阶词汇。

## 30. quorum
- 发音：/ˈkwɔːrəm/
- 含义：法定多数；仲裁多数
- 开发语境：分布式系统中用于达成一致的最小多数节点数。
- 例句：The write succeeds only when a quorum of nodes acknowledges it.
- 翻译：只有当足够多数节点确认后，写入才算成功。
- 讲解：一致性协议和分布式存储非常高频。
