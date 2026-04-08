# Anki Day 17：数据库设计 / 索引 / 查询

## 卡片格式
Front｜Back

1. **Front**: read replica
   **Back**: 只读副本｜Read replicas reduce the load on the primary database.｜提示：读写分离

2. **Front**: denormalization
   **Back**: 反规范化｜Denormalization can improve read performance.｜提示：换性能的 trade-off

3. **Front**: query plan
   **Back**: 查询计划｜The query plan shows that the index is not being used.｜提示：SQL 优化

4. **Front**: composite index
   **Back**: 联合索引｜A composite index may improve this query.｜提示：多列查询

5. **Front**: covering index
   **Back**: 覆盖索引｜A covering index avoids extra table lookups.｜提示：避免回表
