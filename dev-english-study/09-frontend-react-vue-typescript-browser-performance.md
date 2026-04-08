# 前端专项英语：React / Vue / TypeScript / 浏览器 / 性能优化

> 这部分专门面向前端开发实战，覆盖组件模型、状态管理、类型系统、浏览器机制与性能优化表达。

---

## 1. virtual DOM
- 发音：/ˈvɜːrtʃuəl dɑːm/
- 含义：虚拟 DOM
- 开发语境：框架用来描述 UI 结构的抽象层。
- 例句：The virtual DOM helps reduce direct DOM manipulation.
- 翻译：虚拟 DOM 有助于减少直接的 DOM 操作。
- 讲解：`reduce direct DOM manipulation` 是 React 原理讨论中的高频表达。

## 2. reconciliation
- 发音：/ˌrekənsɪliˈeɪʃən/
- 含义：协调；调和更新过程
- 开发语境：React 比较新旧虚拟 DOM 并决定如何更新页面。
- 例句：Poor key usage can affect the reconciliation process.
- 翻译：错误的 key 使用方式会影响协调更新过程。
- 讲解：与 `key`、`re-render` 常一起出现。

## 3. key
- 发音：/kiː/
- 含义：键值标识
- 开发语境：React 列表渲染中用于识别元素。
- 例句：Each list item should have a stable key.
- 翻译：列表中的每一项都应该有一个稳定的 key。
- 讲解：`stable key` 是 React 列表渲染最佳实践。

## 4. controlled component
- 发音：短语表达
- 含义：受控组件
- 开发语境：表单值由状态统一控制。
- 例句：A controlled component makes form validation easier.
- 翻译：受控组件会让表单校验更容易。
- 讲解：React 表单场景高频术语。

## 5. uncontrolled component
- 发音：短语表达
- 含义：非受控组件
- 开发语境：表单值更多依赖 DOM 自身状态。
- 例句：An uncontrolled component can be simpler for small forms.
- 翻译：对于小表单来说，非受控组件可能更简单。
- 讲解：适合和 controlled component 对比记忆。

## 6. context
- 发音：/ˈkɑːntekst/
- 含义：上下文
- 开发语境：React Context 用于跨层级传递数据。
- 例句：Use context carefully to avoid unnecessary re-renders.
- 翻译：使用 context 时要谨慎，避免不必要的重复渲染。
- 讲解：真实项目里经常这样提醒别人。

## 7. prop drilling
- 发音：短语表达
- 含义：属性逐层透传
- 开发语境：数据一层层往下传，导致代码冗长。
- 例句：Context can reduce prop drilling in deeply nested components.
- 翻译：在层级很深的组件中，Context 可以减少 props 逐层透传。
- 讲解：React 项目结构讨论高频词。

## 8. memoization
- 发音：/ˌmeməzaɪˈzeɪʃən/
- 含义：记忆化
- 开发语境：缓存计算结果，减少重复计算。
- 例句：Memoization can improve performance for expensive computations.
- 翻译：对于开销较大的计算，记忆化可以提升性能。
- 讲解：常和 `useMemo`、`useCallback` 一起出现。

## 9. side effect
- 发音：/saɪd ɪˈfekt/
- 含义：副作用
- 开发语境：请求、订阅、定时器、DOM 操作等。
- 例句：Fetching data inside render will cause side effects.
- 翻译：在渲染过程中获取数据会造成副作用。
- 讲解：React Hooks 学习中的核心概念。

## 10. lifecycle
- 发音：/ˈlaɪfsaɪkl/
- 含义：生命周期
- 开发语境：组件创建、更新、销毁过程。
- 例句：You need to clean up subscriptions during the component lifecycle.
- 翻译：你需要在组件生命周期中清理订阅。
- 讲解：`clean up subscriptions` 很真实。

## 11. composable
- 发音：/kəmˈpoʊzəbl/
- 含义：可组合的
- 开发语境：Vue Composition API 或通用代码复用思想。
- 例句：This logic should be extracted into a composable.
- 翻译：这段逻辑应该被提取到一个可组合函数中。
- 讲解：Vue 3 语境很常见。

## 12. reactive
- 发音：/riˈæktɪv/
- 含义：响应式的
- 开发语境：数据变化自动驱动视图变化。
- 例句：The reactive state is shared across multiple components.
- 翻译：这个响应式状态在多个组件之间共享。
- 讲解：Vue 和现代框架经常使用这个词。

## 13. computed property
- 发音：短语表达
- 含义：计算属性
- 开发语境：基于已有状态推导出的值。
- 例句：A computed property should be free of side effects.
- 翻译：计算属性应该避免副作用。
- 讲解：Vue 代码评审里非常高频。

## 14. watcher
- 发音：/ˈwɑːtʃər/
- 含义：侦听器
- 开发语境：监听数据变化并执行逻辑。
- 例句：Use a watcher only when a computed property is not enough.
- 翻译：只有在计算属性不够用时，才使用 watcher。
- 讲解：很适合做 Vue 最佳实践说明。

## 15. type inference
- 发音：/taɪp ˈɪnfərəns/
- 含义：类型推断
- 开发语境：TypeScript 自动推断变量或表达式类型。
- 例句：Type inference works well here, so an explicit annotation is unnecessary.
- 翻译：这里的类型推断已经很好用了，所以没必要显式标注。
- 讲解：TS 评审中高频出现。

## 16. type annotation
- 发音：/taɪp ˌænoʊˈteɪʃən/
- 含义：类型标注
- 开发语境：手动写明变量、函数、参数的类型。
- 例句：Add a type annotation to make the intent clearer.
- 翻译：加一个类型标注会让意图更清晰。
- 讲解：`make the intent clearer` 是代码评审常用语。

## 17. generic
- 发音：/dʒəˈnerɪk/
- 含义：泛型
- 开发语境：编写可复用、类型安全的抽象逻辑。
- 例句：This helper can be rewritten as a generic function.
- 翻译：这个辅助函数可以重写成一个泛型函数。
- 讲解：TypeScript 必学术语。

## 18. union type
- 发音：/ˈjuːniən taɪp/
- 含义：联合类型
- 开发语境：一个值可能属于多个类型之一。
- 例句：A union type is useful for modeling different UI states.
- 翻译：联合类型很适合描述不同的界面状态。
- 讲解：适合状态机、表单、接口返回建模。

## 19. narrowing
- 发音：/ˈnæroʊɪŋ/
- 含义：类型收窄
- 开发语境：通过条件判断缩小变量可能类型范围。
- 例句：Type narrowing is required before accessing this property.
- 翻译：在访问这个属性之前，需要先做类型收窄。
- 讲解：TS 编译报错时经常会说这句话。

## 20. immutable
- 发音：/ɪˈmjuːtəbl/
- 含义：不可变的
- 开发语境：状态更新时不直接修改原对象。
- 例句：State updates should be immutable for predictable behavior.
- 翻译：为了保证行为可预测，状态更新应该保持不可变。
- 讲解：React 状态管理核心原则之一。

## 21. event loop
- 发音：/ɪˈvent luːp/
- 含义：事件循环
- 开发语境：浏览器和 JavaScript 任务调度机制。
- 例句：Understanding the event loop helps explain asynchronous behavior.
- 翻译：理解事件循环有助于解释异步行为。
- 讲解：前端面试高频知识点。

## 22. call stack
- 发音：/kɔːl stæk/
- 含义：调用栈
- 开发语境：函数执行顺序和调用上下文。
- 例句：The error originated from a recursive call stack overflow.
- 翻译：这个错误源于递归调用导致的栈溢出。
- 讲解：调试运行时错误很常见。

## 23. microtask
- 发音：/ˈmaɪkroʊtæsk/
- 含义：微任务
- 开发语境：Promise 回调等在事件循环中的优先队列。
- 例句：Microtasks are processed before the next rendering step.
- 翻译：微任务会在下一次渲染之前被处理。
- 讲解：和 macrotask 一起理解更好。

## 24. repaint
- 发音：/ˌriːˈpeɪnt/
- 含义：重绘
- 开发语境：元素外观变化但不涉及布局变化。
- 例句：This style change triggers a repaint but not a reflow.
- 翻译：这个样式变化会触发重绘，但不会触发回流。
- 讲解：浏览器性能优化高频知识点。

## 25. reflow
- 发音：/ˌriːˈfloʊ/
- 含义：回流；重排
- 开发语境：布局变化导致浏览器重新计算元素位置和尺寸。
- 例句：Frequent DOM measurements can cause expensive reflows.
- 翻译：频繁测量 DOM 可能导致代价高昂的回流。
- 讲解：`expensive reflows` 是性能分析常见说法。

## 26. critical rendering path
- 发音：短语表达
- 含义：关键渲染路径
- 开发语境：浏览器从接收 HTML 到完成首次渲染的关键步骤。
- 例句：We should optimize the critical rendering path for faster page loads.
- 翻译：我们应该优化关键渲染路径，以加快页面加载速度。
- 讲解：前端性能优化进阶词汇。

## 27. code splitting
- 发音：/koʊd ˈsplɪtɪŋ/
- 含义：代码分割
- 开发语境：把大包拆成按需加载的小包。
- 例句：Code splitting can reduce the initial bundle size.
- 翻译：代码分割可以减少初始打包体积。
- 讲解：和懒加载经常搭配出现。

## 28. prefetch
- 发音：/ˌpriːˈfetʃ/
- 含义：预取
- 开发语境：提前加载未来可能会用到的资源。
- 例句：We prefetch the next page to improve perceived performance.
- 翻译：我们预取下一页内容来提升感知性能。
- 讲解：`perceived performance` 是用户体验优化中的关键词。

## 29. preload
- 发音：/ˌpriːˈloʊd/
- 含义：预加载
- 开发语境：提前声明关键资源优先加载。
- 例句：Fonts used above the fold should be preloaded.
- 翻译：首屏使用到的字体应该被预加载。
- 讲解：`above the fold` 是前端性能常见表达。

## 30. long task
- 发音：/lɔːŋ tæsk/
- 含义：长任务
- 开发语境：阻塞主线程过久的任务。
- 例句：A long task can freeze the UI and hurt user experience.
- 翻译：长任务会卡住界面并损害用户体验。
- 讲解：性能监控与 Web Vitals 讨论中很重要。
