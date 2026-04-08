# Anki Day 21：系统设计面试表达

## 卡片格式
Front｜Back

1. **Front**: write path
   **Back**: 写路径｜The write path should remain simple and reliable.｜提示：读写分离

2. **Front**: read path
   **Back**: 读路径｜The read path can be optimized separately.｜提示：系统拆分

3. **Front**: capacity planning
   **Back**: 容量规划｜Capacity planning depends on traffic patterns.｜提示：面试高频

4. **Front**: fault domain
   **Back**: 故障域｜Replicas should be distributed across different fault domains.｜提示：高可用设计

5. **Front**: graceful degradation
   **Back**: 优雅降级｜Graceful degradation is better than complete failure.｜提示：系统设计思维
