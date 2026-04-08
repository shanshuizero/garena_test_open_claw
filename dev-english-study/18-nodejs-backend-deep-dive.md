# 后端深入：Node.js 后端专项英语

## 1. event-driven architecture
- 发音：短语表达
- 含义：事件驱动架构
- 例句：Node.js is a good fit for event-driven architecture.
- 翻译：Node.js 很适合事件驱动架构。
- 讲解：Node 后端定位常见表述。

## 2. non-blocking I/O
- 发音：短语表达
- 含义：非阻塞 I/O
- 例句：Non-blocking I/O improves throughput for network-heavy workloads.
- 翻译：非阻塞 I/O 可以提升网络密集型负载的吞吐量。
- 讲解：Node 核心优势之一。

## 3. callback hell
- 发音：短语表达
- 含义：回调地狱
- 例句：Promises and async functions help avoid callback hell.
- 翻译：Promise 和 async 函数有助于避免回调地狱。
- 讲解：Node 历史问题高频词。

## 4. promise chain
- 发音：短语表达
- 含义：Promise 链
- 例句：A long promise chain can be hard to debug.
- 翻译：过长的 Promise 链可能很难调试。
- 讲解：实际代码里很常见。

## 5. async pipeline
- 发音：短语表达
- 含义：异步处理链路
- 例句：The async pipeline includes validation, transformation, and persistence.
- 翻译：这个异步处理链路包含校验、转换和持久化。
- 讲解：适合描述请求流程。

## 6. stream backpressure
- 发音：短语表达
- 含义：流式背压
- 例句：Stream backpressure prevents memory usage from growing too fast.
- 翻译：流式背压可以防止内存增长过快。
- 讲解：Node stream 高频概念。

## 7. middleware chain
- 发音：短语表达
- 含义：中间件链
- 例句：The middleware chain adds authentication and request logging.
- 翻译：这条中间件链增加了认证和请求日志。
- 讲解：Express/Koa 高频表达。

## 8. memory leak
- 发音：短语表达
- 含义：内存泄漏
- 例句：The process crashes after several hours because of a memory leak.
- 翻译：这个进程运行数小时后会因为内存泄漏而崩溃。
- 讲解：Node 线上问题高频原因。

## 9. heap snapshot
- 发音：短语表达
- 含义：堆快照
- 例句：We need a heap snapshot to analyze the leak.
- 翻译：我们需要一个堆快照来分析泄漏问题。
- 讲解：排查 Node 内存问题常见。

## 10. event emitter
- 发音：短语表达
- 含义：事件发射器
- 例句：The event emitter should remove unused listeners.
- 翻译：事件发射器应该移除不用的监听器。
- 讲解：避免内存泄漏的重要实践。

## 11. listener leak
- 发音：短语表达
- 含义：监听器泄漏
- 例句：Too many listeners may indicate a listener leak.
- 翻译：监听器过多可能意味着存在监听器泄漏。
- 讲解：Node 调优很常见。

## 12. worker thread
- 发音：短语表达
- 含义：工作线程
- 例句：CPU-intensive tasks should be moved to worker threads.
- 翻译：CPU 密集型任务应该迁移到 worker threads 中处理。
- 讲解：Node 单线程模型下很关键。

## 13. process manager
- 发音：短语表达
- 含义：进程管理器
- 例句：A process manager can restart crashed services automatically.
- 翻译：进程管理器可以自动重启崩溃的服务。
- 讲解：PM2 等工具场景。

## 14. cluster mode
- 发音：短语表达
- 含义：集群模式
- 例句：Cluster mode helps utilize multiple CPU cores.
- 翻译：集群模式有助于利用多个 CPU 核心。
- 讲解：Node 服务扩展常见。

## 15. unhandled rejection
- 发音：短语表达
- 含义：未处理的 Promise 拒绝
- 例句：Unhandled rejections should be logged and monitored.
- 翻译：未处理的 Promise 拒绝应该被记录和监控。
- 讲解：Node 生产稳定性常见问题。
