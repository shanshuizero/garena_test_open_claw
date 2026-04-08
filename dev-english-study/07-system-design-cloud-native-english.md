# 系统设计与云原生英语

> 这部分覆盖架构设计、分布式系统、云原生和可用性领域的核心英语。

---

## 1. availability
- 发音：/əˌveɪləˈbɪləti/
- 含义：可用性
- 开发语境：系统可被用户正常访问和使用的能力。
- 例句：We need higher availability during peak traffic hours.
- 翻译：在流量高峰期，我们需要更高的系统可用性。
- 讲解：`during peak traffic hours` 是容量规划中常见时间表达。

## 2. consistency
- 发音：/kənˈsɪstənsi/
- 含义：一致性
- 开发语境：多个副本或节点之间数据是否保持一致。
- 例句：Strong consistency may increase write latency.
- 翻译：强一致性可能会增加写入延迟。
- 讲解：CAP 和分布式系统讨论中的基础术语。

## 3. partition tolerance
- 发音：短语表达
- 含义：分区容错性
- 开发语境：网络分区发生时系统仍能继续工作。
- 例句：Distributed systems often need to balance consistency and partition tolerance.
- 翻译：分布式系统通常需要在一致性和分区容错之间做平衡。
- 讲解：是 CAP 理论的核心表达之一。

## 4. replica set
- 发音：/ˈreplɪkə set/
- 含义：副本集
- 开发语境：多个副本组成的高可用部署单元。
- 例句：The replica set automatically elects a new primary.
- 翻译：副本集会自动选举新的主节点。
- 讲解：数据库与容器编排都常见。

## 5. leader election
- 发音：/ˈliːdər ɪˈlekʃən/
- 含义：主节点选举
- 开发语境：分布式节点中选择主节点。
- 例句：Leader election takes longer when the network is unstable.
- 翻译：当网络不稳定时，主节点选举会花更久时间。
- 讲解：故障恢复时常被提及。

## 6. distributed lock
- 发音：/dɪˈstrɪbjətɪd lɑːk/
- 含义：分布式锁
- 开发语境：控制多个节点之间的并发访问。
- 例句：Use a distributed lock to prevent duplicate job execution.
- 翻译：使用分布式锁来防止任务重复执行。
- 讲解：定时任务和支付场景里很常见。

## 7. eventual consistency
- 发音：/ɪˈventʃuəl kənˈsɪstənsi/
- 含义：最终一致性
- 开发语境：短期可能不一致，但最终会收敛一致。
- 例句：The system accepts eventual consistency for better availability.
- 翻译：这个系统为了更高可用性接受最终一致性。
- 讲解：典型的架构 trade-off 说法。

## 8. horizontal scaling
- 发音：/ˌhɔːrɪˈzɑːntl ˈskeɪlɪŋ/
- 含义：水平扩展
- 开发语境：通过增加实例数量提升容量。
- 例句：Horizontal scaling is easier when the service is stateless.
- 翻译：当服务是无状态时，水平扩展会更容易。
- 讲解：`stateless` 与 `horizontal scaling` 经常一起出现。

## 9. vertical scaling
- 发音：/ˈvɜːrtɪkl ˈskeɪlɪŋ/
- 含义：垂直扩展
- 开发语境：通过增加单机资源提升能力。
- 例句：Vertical scaling works only up to a certain point.
- 翻译：垂直扩展只在一定范围内有效。
- 讲解：适合和水平扩展对比学习。

## 10. stateless
- 发音：/ˈsteɪtləs/
- 含义：无状态的
- 开发语境：请求之间不依赖本地会话状态。
- 例句：A stateless service is easier to scale horizontally.
- 翻译：无状态服务更容易做水平扩展。
- 讲解：微服务设计的高频概念。

## 11. stateful
- 发音：/ˈsteɪtfəl/
- 含义：有状态的
- 开发语境：服务依赖本地状态或长期连接。
- 例句：Stateful workloads require more careful deployment planning.
- 翻译：有状态工作负载需要更谨慎的部署规划。
- 讲解：数据库、中间件、消息系统中很常见。

## 12. service discovery
- 发音：/ˈsɜːrvɪs dɪˈskʌvəri/
- 含义：服务发现
- 开发语境：动态找到其他服务的地址和实例。
- 例句：Service discovery allows instances to find each other automatically.
- 翻译：服务发现使各个实例能够自动找到彼此。
- 讲解：微服务架构常见基础设施能力。

## 13. load balancer
- 发音：/loʊd ˈbælənsər/
- 含义：负载均衡器
- 开发语境：分发流量到多个实例。
- 例句：The load balancer routes traffic based on health checks.
- 翻译：负载均衡器基于健康检查结果进行流量路由。
- 讲解：`routes traffic based on ...` 很常用。

## 14. reverse proxy
- 发音：/rɪˈvɜːrs ˈprɑːksi/
- 含义：反向代理
- 开发语境：Nginx、网关层常见组件。
- 例句：The reverse proxy terminates TLS connections.
- 翻译：反向代理负责终止 TLS 连接。
- 讲解：部署和网络架构高频词。

## 15. orchestration
- 发音：/ˌɔːrkɪˈstreɪʃən/
- 含义：编排
- 开发语境：对容器、任务、工作流进行自动化协调。
- 例句：Container orchestration simplifies large-scale deployment.
- 翻译：容器编排简化了大规模部署。
- 讲解：Kubernetes 语境中的高频术语。

## 16. node
- 发音：/noʊd/
- 含义：节点
- 开发语境：集群中的一台机器或实例。
- 例句：The pod was rescheduled to another node.
- 翻译：这个 Pod 被重新调度到了另一个节点。
- 讲解：Kubernetes 日常表达。

## 17. pod
- 发音：/pɑːd/
- 含义：Pod
- 开发语境：Kubernetes 中最小部署单元。
- 例句：One pod keeps restarting because of a configuration error.
- 翻译：有一个 Pod 因为配置错误一直在重启。
- 讲解：`keeps restarting` 非常贴近真实故障现象。

## 18. autoscaling
- 发音：/ˌɔːtoʊˈskeɪlɪŋ/
- 含义：自动扩缩容
- 开发语境：根据负载自动调整实例数量。
- 例句：Autoscaling helps us handle traffic spikes automatically.
- 翻译：自动扩缩容帮助我们自动应对流量尖峰。
- 讲解：云原生平台高频能力。

## 19. health check
- 发音：/helθ tʃek/
- 含义：健康检查
- 开发语境：检查服务是否正常可用。
- 例句：The health check endpoint should be lightweight.
- 翻译：健康检查接口应该足够轻量。
- 讲解：是运维与网关配置中的基础项。

## 20. disaster recovery
- 发音：/dɪˈzæstər rɪˈkʌvəri/
- 含义：灾难恢复
- 开发语境：大规模故障后的恢复方案和能力。
- 例句：We need a better disaster recovery plan for the primary region.
- 翻译：我们需要为主区域准备更好的灾难恢复方案。
- 讲解：架构和运维评审中非常重要。

## 21. single point of failure
- 发音：短语表达
- 含义：单点故障
- 开发语境：某个组件一旦故障会导致整体不可用。
- 例句：This database is still a single point of failure.
- 翻译：这个数据库仍然是一个单点故障。
- 讲解：架构审查中的经典判断句。

## 22. multi-region
- 发音：/ˌmʌlti ˈriːdʒən/
- 含义：多区域部署
- 开发语境：跨地域容灾和低延迟访问。
- 例句：Multi-region deployment improves resilience but increases complexity.
- 翻译：多区域部署提升了韧性，但也增加了复杂度。
- 讲解：又一个典型 trade-off 表达。

## 23. cold start
- 发音：/koʊld stɑːrt/
- 含义：冷启动
- 开发语境：函数计算、服务启动初期响应较慢。
- 例句：Cold starts are noticeable in low-traffic environments.
- 翻译：在低流量环境中，冷启动现象会比较明显。
- 讲解：Serverless 语境很常见。

## 24. resilience
- 发音：/rɪˈzɪliəns/
- 含义：韧性；弹性恢复能力
- 开发语境：系统遇到故障后继续运行或快速恢复的能力。
- 例句：Retries and fallback strategies improve system resilience.
- 翻译：重试和降级策略能够提升系统韧性。
- 讲解：SRE 与架构设计高频概念。

## 25. fallback
- 发音：/ˈfɔːlbæk/
- 含义：降级方案；兜底方案
- 开发语境：主方案失败时启用备选路径。
- 例句：We need a fallback when the third-party API is unavailable.
- 翻译：当第三方 API 不可用时，我们需要一个兜底方案。
- 讲解：工程实践里非常实用的词。
