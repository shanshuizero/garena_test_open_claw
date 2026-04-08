# 后端深入：数据库与事务专项英语

## 1. dirty read
- 发音：短语表达
- 含义：脏读
- 例句：The read-uncommitted level may allow dirty reads.
- 翻译：读未提交隔离级别可能会允许脏读。
- 讲解：事务隔离基础概念。

## 2. non-repeatable read
- 发音：短语表达
- 含义：不可重复读
- 例句：A non-repeatable read occurs when the same row changes between reads.
- 翻译：当同一行在两次读取之间发生变化时，就会出现不可重复读。
- 讲解：数据库面试高频。

## 3. phantom read
- 发音：短语表达
- 含义：幻读
- 例句：Phantom reads are harder to reason about in range queries.
- 翻译：在范围查询中，幻读更难分析。
- 讲解：事务异常经典概念。

## 4. snapshot isolation
- 发音：短语表达
- 含义：快照隔离
- 例句：Snapshot isolation reduces read contention in many workloads.
- 翻译：快照隔离在很多负载下可以减少读竞争。
- 讲解：数据库实现细节常见。

## 5. row-level lock
- 发音：短语表达
- 含义：行级锁
- 例句：A row-level lock reduces contention compared with a table lock.
- 翻译：与表锁相比，行级锁可以减少竞争。
- 讲解：并发控制基础术语。

## 6. table lock
- 发音：短语表达
- 含义：表锁
- 例句：A table lock can severely limit throughput.
- 翻译：表锁会严重限制吞吐量。
- 讲解：数据库性能常见问题。

## 7. pessimistic locking
- 发音：短语表达
- 含义：悲观锁
- 例句：Pessimistic locking is safer but can reduce concurrency.
- 翻译：悲观锁更安全，但可能降低并发能力。
- 讲解：适合与 optimistic locking 对比记忆。

## 8. optimistic locking
- 发音：短语表达
- 含义：乐观锁
- 例句：Optimistic locking works well when write conflicts are rare.
- 翻译：当写冲突较少时，乐观锁效果很好。
- 讲解：互联网业务很常用。

## 9. index scan
- 发音：短语表达
- 含义：索引扫描
- 例句：The planner chooses an index scan for this selective query.
- 翻译：对于这个选择性较高的查询，优化器选择了索引扫描。
- 讲解：SQL 调优常见。

## 10. full table scan
- 发音：短语表达
- 含义：全表扫描
- 例句：A full table scan is too expensive on large tables.
- 翻译：对大表来说，全表扫描代价太高。
- 讲解：数据库面试和实战高频。

## 11. composite index
- 发音：短语表达
- 含义：联合索引
- 例句：A composite index may improve this multi-column query.
- 翻译：联合索引可能提升这个多列查询的性能。
- 讲解：索引设计核心概念。

## 12. covering index
- 发音：短语表达
- 含义：覆盖索引
- 例句：A covering index avoids extra table lookups.
- 翻译：覆盖索引可以避免额外回表。
- 讲解：性能优化高频术语。

## 13. write skew
- 发音：短语表达
- 含义：写偏差
- 例句：Write skew can still happen under snapshot isolation.
- 翻译：在快照隔离下仍然可能发生写偏差。
- 讲解：事务隔离进阶概念。

## 14. deadlock
- 发音：/ˈdedlɑːk/
- 含义：死锁
- 例句：The transaction failed because of a deadlock.
- 翻译：这个事务因为死锁而失败。
- 讲解：数据库并发经典问题。

## 15. rollback segment
- 发音：短语表达
- 含义：回滚段
- 例句：Long transactions may put pressure on the rollback segment.
- 翻译：长事务可能会给回滚段带来压力。
- 讲解：数据库内部机制进阶表达。
