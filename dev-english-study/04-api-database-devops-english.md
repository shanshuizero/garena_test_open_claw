# API、数据库、DevOps 与部署英语词汇

> 这部分覆盖前后端协作最常用的接口、数据和上线场景英语。

---

## 1. request
- 发音：/rɪˈkwest/
- 含义：请求
- 开发语境：客户端向服务端发起调用。
- 例句：The request payload is missing a required field.
- 翻译：这个请求体缺少一个必填字段。
- 讲解：`required field` 是接口文档与校验场景高频词组。

## 2. response
- 发音：/rɪˈspɑːns/
- 含义：响应
- 开发语境：服务端返回的数据或状态。
- 例句：The response format has changed in version two.
- 翻译：响应格式在第二版中发生了变化。
- 讲解：`format has changed` 是接口升级讨论常见表达。

## 3. payload
- 发音：/ˈpeɪloʊd/
- 含义：载荷；有效数据
- 开发语境：请求体或消息体中的核心数据。
- 例句：The payload is too large for a GET request.
- 翻译：这个载荷对于 GET 请求来说太大了。
- 讲解：常用于接口设计与消息队列场景。

## 4. schema
- 发音：/ˈskiːmə/
- 含义：模式；结构定义
- 开发语境：数据库表结构、JSON Schema、GraphQL Schema。
- 例句：We need to update the schema before deploying this change.
- 翻译：在部署这个改动前，我们需要更新结构定义。
- 讲解：`before deploying this change` 强调发布顺序。

## 5. validation
- 发音：/ˌvælɪˈdeɪʃən/
- 含义：校验
- 开发语境：对输入、数据格式、业务规则做验证。
- 例句：Server-side validation is still required.
- 翻译：服务端校验仍然是必须的。
- 讲解：即使前端校验了，后端也常说这句话。

## 6. parameter
- 发音：/pəˈræmɪtər/
- 含义：参数
- 开发语境：路径参数、查询参数、函数参数。
- 例句：This parameter controls the page size.
- 翻译：这个参数控制分页大小。
- 讲解：`controls` 可以理解为“决定、控制”。

## 7. pagination
- 发音：/ˌpædʒəˈneɪʃən/
- 含义：分页
- 开发语境：列表接口、前端表格、数据浏览。
- 例句：Cursor-based pagination performs better on large datasets.
- 翻译：基于游标的分页在大数据集上表现更好。
- 讲解：`cursor-based pagination` 是后端面试高频概念。

## 8. filtering
- 发音：/ˈfɪltərɪŋ/
- 含义：过滤
- 开发语境：筛选数据。
- 例句：The API supports filtering by status and date range.
- 翻译：这个 API 支持按状态和日期范围过滤。
- 讲解：`supports filtering by ...` 是说明接口能力的常见句式。

## 9. sorting
- 发音：/ˈsɔːrtɪŋ/
- 含义：排序
- 开发语境：列表结果排序。
- 例句：Default sorting should be documented clearly.
- 翻译：默认排序方式应该清楚地写进文档。
- 讲解：`documented clearly` 常见于规范性建议。

## 10. relational database
- 发音：/rɪˈleɪʃənəl ˈdeɪtəbeɪs/
- 含义：关系型数据库
- 开发语境：MySQL、PostgreSQL 等。
- 例句：A relational database is better suited for this transaction-heavy workload.
- 翻译：关系型数据库更适合这种事务密集型负载。
- 讲解：`better suited for` 表示“更适合”。

## 11. index
- 发音：/ˈɪndeks/
- 含义：索引
- 开发语境：数据库查询加速。
- 例句：Adding an index reduced the query time significantly.
- 翻译：添加索引后，查询时间显著降低了。
- 讲解：`reduced ... significantly` 是性能汇报常见结构。

## 12. migration
- 发音：/maɪˈɡreɪʃən/
- 含义：迁移
- 开发语境：数据库结构迁移、服务迁移、数据迁移。
- 例句：Run the migration before starting the application.
- 翻译：在启动应用之前先执行迁移。
- 讲解：非常典型的部署说明语句。

## 13. replica
- 发音：/ˈreplɪkə/
- 含义：副本
- 开发语境：数据库只读副本、服务实例副本。
- 例句：Read traffic is routed to the replica.
- 翻译：读流量被路由到副本节点。
- 讲解：`is routed to` 是网络与架构高频表达。

## 14. shard
- 发音：/ʃɑːrd/
- 含义：分片
- 开发语境：数据库或存储水平拆分。
- 例句：User data is distributed across multiple shards.
- 翻译：用户数据分布在多个分片上。
- 讲解：`distributed across` 表示“分布在……各处”。

## 15. backup
- 发音：/ˈbækʌp/
- 含义：备份
- 开发语境：数据备份、系统备份。
- 例句：Daily backups are stored in a separate region.
- 翻译：每日备份存储在独立区域。
- 讲解：体现灾备意识。

## 16. restore
- 发音：/rɪˈstɔːr/
- 含义：恢复
- 开发语境：从备份恢复数据或服务。
- 例句：We tested how long it takes to restore the database.
- 翻译：我们测试了恢复数据库所需的时间。
- 讲解：`how long it takes to ...` 是很实用的评估句型。

## 17. container
- 发音：/kənˈteɪnər/
- 含义：容器
- 开发语境：Docker 容器。
- 例句：The application runs inside a container.
- 翻译：这个应用运行在容器中。
- 讲解：最基础的容器化表达。

## 18. image
- 发音：/ˈɪmɪdʒ/
- 含义：镜像
- 开发语境：Docker image，打包后的运行模板。
- 例句：We should use a smaller base image.
- 翻译：我们应该使用更小的基础镜像。
- 讲解：`base image` 是 Docker 高频词组。

## 19. pipeline
- 发音：/ˈpaɪplaɪn/
- 含义：流水线
- 开发语境：CI/CD 构建、测试、发布流程。
- 例句：The pipeline failed at the integration test stage.
- 翻译：这条流水线在集成测试阶段失败了。
- 讲解：`failed at ... stage` 是持续集成常用表达。

## 20. staging
- 发音：/ˈsteɪdʒɪŋ/
- 含义：预发布环境
- 开发语境：介于测试与生产之间的验证环境。
- 例句：Please verify the fix in staging first.
- 翻译：请先在预发布环境验证这个修复。
- 讲解：`verify ... first` 表示先做风险较低的验证。

## 21. production
- 发音：/prəˈdʌkʃən/
- 含义：生产环境
- 开发语境：真实用户使用的线上环境。
- 例句：Do not test this directly in production.
- 翻译：不要直接在生产环境测试这个改动。
- 讲解：这是上线纪律中的经典句子。

## 22. rollback
- 发音：/ˈroʊlbæk/
- 含义：回滚
- 开发语境：发布失败后恢复到旧版本。
- 例句：We had to roll back the deployment.
- 翻译：我们不得不回滚这次部署。
- 讲解：`had to` 表示“不得不”。

## 23. observability
- 发音：/əbˌzɜːrvəˈbɪləti/
- 含义：可观测性
- 开发语境：通过日志、指标、链路追踪理解系统状态。
- 例句：Our observability is not good enough for incident response.
- 翻译：我们的可观测性还不足以支撑故障响应。
- 讲解：这是现代工程体系中的重要概念。

## 24. metrics
- 发音：/ˈmetrɪks/
- 含义：指标
- 开发语境：QPS、错误率、CPU 使用率等。
- 例句：The CPU metrics look normal, but the memory usage keeps growing.
- 翻译：CPU 指标看起来正常，但内存占用持续增长。
- 讲解：`keeps growing` 表示持续增长，常用于故障排查。

## 25. tracing
- 发音：/ˈtreɪsɪŋ/
- 含义：链路追踪
- 开发语境：观察请求经过多个服务的路径。
- 例句：Distributed tracing helps us identify the slow service.
- 翻译：分布式链路追踪帮助我们定位到慢服务。
- 讲解：`identify the slow service` 很符合排障语境。
