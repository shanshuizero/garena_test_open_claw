# 后端深入：Go 后端专项英语

## 1. goroutine
- 发音：/ˈɡoʊruːtiːn/
- 含义：Go 协程
- 例句：Launching too many goroutines can increase memory usage.
- 翻译：启动过多 goroutine 会增加内存使用量。
- 讲解：Go 并发基础术语。

## 2. channel
- 发音：/ˈtʃænəl/
- 含义：通道
- 例句：Channels are useful for coordinating concurrent work.
- 翻译：channel 很适合协调并发工作。
- 讲解：Go 语言核心概念。

## 3. buffered channel
- 发音：短语表达
- 含义：带缓冲通道
- 例句：A buffered channel can absorb short bursts of traffic.
- 翻译：带缓冲通道可以吸收短时流量突发。
- 讲解：很适合性能与并发场景。

## 4. select statement
- 发音：短语表达
- 含义：select 语句
- 例句：A select statement lets us wait on multiple channel operations.
- 翻译：select 语句允许我们等待多个 channel 操作。
- 讲解：Go 并发控制核心表达。

## 5. context cancellation
- 发音：短语表达
- 含义：上下文取消
- 例句：Context cancellation prevents wasted work in slow requests.
- 翻译：context cancellation 可以避免慢请求中的无效工作。
- 讲解：Go 服务端高频概念。

## 6. deadline exceeded
- 发音：短语表达
- 含义：超过截止时间
- 例句：The request failed because the context deadline was exceeded.
- 翻译：这个请求失败了，因为 context 截止时间已超出。
- 讲解：Go 超时错误非常高频。

## 7. interface satisfaction
- 发音：短语表达
- 含义：接口实现匹配
- 例句：Go uses implicit interface satisfaction.
- 翻译：Go 使用隐式接口实现匹配机制。
- 讲解：Go 语言设计特点。

## 8. zero value
- 发音：短语表达
- 含义：零值
- 例句：The zero value of a slice is nil.
- 翻译：slice 的零值是 nil。
- 讲解：Go 基础但非常重要。

## 9. receiver
- 发音：/rɪˈsiːvər/
- 含义：接收者
- 例句：Use a pointer receiver when the method needs to modify the struct.
- 翻译：当方法需要修改结构体时，应使用指针接收者。
- 讲解：Go 面试常见。

## 10. race detector
- 发音：短语表达
- 含义：竞态检测器
- 例句：Run the race detector before merging this concurrency-related change.
- 翻译：在合并这个并发相关改动前，先跑一下竞态检测器。
- 讲解：实际工程很常见。

## 11. panic recovery
- 发音：短语表达
- 含义：panic 恢复
- 例句：Middleware should include panic recovery for production safety.
- 翻译：为了生产安全，中间件应该包含 panic recovery。
- 讲解：Go Web 服务高频实践。

## 12. worker pool
- 发音：短语表达
- 含义：工作池
- 例句：A worker pool limits concurrency and protects downstream services.
- 翻译：worker pool 可以限制并发并保护下游服务。
- 讲解：Go 后端常见模式。

## 13. memory allocation
- 发音：短语表达
- 含义：内存分配
- 例句：Too many memory allocations can hurt throughput.
- 翻译：过多的内存分配会影响吞吐量。
- 讲解：Go 性能优化高频表达。

## 14. escape analysis
- 发音：短语表达
- 含义：逃逸分析
- 例句：Escape analysis explains why this value is allocated on the heap.
- 翻译：逃逸分析解释了为什么这个值会分配到堆上。
- 讲解：Go 深入优化知识点。

## 15. graceful shutdown
- 发音：短语表达
- 含义：优雅关闭
- 例句：A graceful shutdown lets in-flight requests finish cleanly.
- 翻译：优雅关闭可以让正在处理中的请求正常完成。
- 讲解：服务治理高频概念。
