# Anki Day 15：分布式 / 微服务

## 卡片格式
Front｜Back

1. **Front**: microservice
   **Back**: 微服务｜Each microservice should have a clear business boundary.｜提示：服务拆分

2. **Front**: service contract
   **Back**: 服务契约｜Breaking the service contract will affect downstream teams.｜提示：接口约定

3. **Front**: downstream
   **Back**: 下游｜A latency spike will impact downstream consumers.｜提示：调用链术语

4. **Front**: cascading failure
   **Back**: 级联故障｜Timeouts and retries can trigger cascading failures.｜提示：稳定性风险

5. **Front**: backpressure
   **Back**: 背压｜We need backpressure to protect consumers.｜提示：高吞吐系统
