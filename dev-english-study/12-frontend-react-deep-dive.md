# 前端深入：React 专项英语

## 1. hook dependency
- 发音：短语表达
- 含义：Hook 依赖项
- 例句：Missing a hook dependency may lead to stale state.
- 翻译：遗漏 Hook 依赖项可能导致过期状态。
- 讲解：React Hooks 排错高频表达。

## 2. stale closure
- 发音：/steɪl ˈkloʊʒər/
- 含义：过期闭包
- 例句：The callback reads stale data because of a stale closure.
- 翻译：这个回调读取了旧数据，因为出现了过期闭包。
- 讲解：React 面试与实际排障都常见。

## 3. useMemo
- 发音：/juːz ˈmemoʊ/
- 含义：React 记忆化 Hook
- 例句：Use useMemo only when the computation is actually expensive.
- 翻译：只有在计算确实开销较大时才使用 useMemo。
- 讲解：体现“不要过度优化”。

## 4. useCallback
- 发音：/juːz ˈkɔːlbæk/
- 含义：缓存函数引用的 Hook
- 例句：useCallback can help prevent unnecessary child re-renders.
- 翻译：useCallback 可以帮助避免不必要的子组件重复渲染。
- 讲解：常和 React.memo 搭配讨论。

## 5. React.memo
- 发音：短语表达
- 含义：组件记忆化
- 例句：React.memo is useful only when the props are stable.
- 翻译：只有在 props 稳定时，React.memo 才有价值。
- 讲解：性能优化中的真实判断。

## 6. lifting state up
- 发音：短语表达
- 含义：状态提升
- 例句：Lifting state up can simplify coordination between sibling components.
- 翻译：状态提升可以简化兄弟组件之间的协作。
- 讲解：React 组件设计基础概念。

## 7. server-side rendering
- 发音：短语表达
- 含义：服务端渲染
- 例句：Server-side rendering improves the first contentful paint.
- 翻译：服务端渲染可以提升首次内容绘制表现。
- 讲解：SSR、SEO、性能场景高频词。

## 8. static generation
- 发音：短语表达
- 含义：静态生成
- 例句：Static generation works well for content-heavy pages.
- 翻译：静态生成非常适合内容型页面。
- 讲解：Next.js 生态常见。

## 9. hydration mismatch
- 发音：短语表达
- 含义：水合不匹配
- 例句：A hydration mismatch may happen when the server and client render different output.
- 翻译：当服务端和客户端渲染结果不一致时，可能会出现水合不匹配。
- 讲解：SSR 排错核心术语。

## 10. suspense
- 发音：/səˈspens/
- 含义：Suspense 机制
- 例句：Suspense can improve the loading experience for asynchronous components.
- 翻译：Suspense 可以改善异步组件的加载体验。
- 讲解：React 新特性相关表达。

## 11. concurrent rendering
- 发音：短语表达
- 含义：并发渲染
- 例句：Concurrent rendering allows React to pause and resume work.
- 翻译：并发渲染允许 React 暂停并恢复渲染工作。
- 讲解：React 18 之后的重要概念。

## 12. custom renderer
- 发音：短语表达
- 含义：自定义渲染器
- 例句：React can support a custom renderer for non-DOM targets.
- 翻译：React 可以为非 DOM 目标支持自定义渲染器。
- 讲解：适合进阶学习者。

## 13. controlled input lag
- 发音：短语表达
- 含义：受控输入卡顿
- 例句：We are seeing controlled input lag on low-end devices.
- 翻译：我们在低端设备上看到了受控输入卡顿问题。
- 讲解：真实性能问题。

## 14. state normalization
- 发音：短语表达
- 含义：状态规范化
- 例句：State normalization makes updates more predictable.
- 翻译：状态规范化让更新更可预测。
- 讲解：复杂状态管理常见策略。

## 15. render prop
- 发音：短语表达
- 含义：渲染属性模式
- 例句：The render prop pattern is flexible but can make JSX harder to read.
- 翻译：render prop 模式很灵活，但可能让 JSX 更难读。
- 讲解：旧模式与 Hooks 对比时常见。
