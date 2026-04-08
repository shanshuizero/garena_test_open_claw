# 测试、质量与安全英语

> 这部分覆盖测试工程、质量保障、安全开发和线上风险控制中常见的英语。

---

## 1. test case
- 发音：/test keɪs/
- 含义：测试用例
- 开发语境：验证功能是否符合预期的具体测试场景。
- 例句：Please add more test cases for invalid input.
- 翻译：请为非法输入补充更多测试用例。
- 讲解：`invalid input` 是测试和后端校验中的高频表达。

## 2. unit test
- 发音：/ˈjuːnɪt test/
- 含义：单元测试
- 开发语境：针对最小功能单元进行测试。
- 例句：This utility function is simple, but it still needs a unit test.
- 翻译：这个工具函数虽然简单，但仍然需要单元测试。
- 讲解：`still needs` 强调“即使如此也仍然需要”。

## 3. integration test
- 发音：/ˌɪntɪˈɡreɪʃən test/
- 含义：集成测试
- 开发语境：测试多个模块或服务组合后的行为。
- 例句：The integration test covers the full login flow.
- 翻译：这个集成测试覆盖了完整的登录流程。
- 讲解：`covers the full ... flow` 是描述测试范围的自然表达。

## 4. end-to-end test
- 发音：/end tuː end test/
- 含义：端到端测试
- 开发语境：模拟真实用户从头到尾使用系统。
- 例句：The end-to-end test failed on the payment confirmation page.
- 翻译：端到端测试在支付确认页失败了。
- 讲解：适合前后端联调与发布前验证场景。

## 5. assertion
- 发音：/əˈsɜːrʃən/
- 含义：断言
- 开发语境：测试中用于验证结果是否符合预期。
- 例句：The assertion should check both status code and response body.
- 翻译：这个断言应该同时检查状态码和响应体。
- 讲解：`both ... and ...` 是补充测试完整性的常见句型。

## 6. coverage
- 发音：/ˈkʌvərɪdʒ/
- 含义：覆盖率
- 开发语境：代码覆盖率、测试覆盖率。
- 例句：High coverage does not always mean high quality.
- 翻译：高覆盖率并不总是意味着高质量。
- 讲解：这句话很适合在代码评审或测试讨论中使用。

## 7. mock
- 发音：/mɑːk/
- 含义：模拟对象；模拟数据
- 开发语境：在测试中替代真实依赖。
- 例句：We can mock the external service in our unit tests.
- 翻译：我们可以在单元测试里模拟外部服务。
- 讲解：`mock the external service` 是测试开发高频表达。

## 8. stub
- 发音：/stʌb/
- 含义：桩；测试替身
- 开发语境：返回固定结果的简化实现。
- 例句：Use a stub here to avoid calling the real API.
- 翻译：这里用一个桩来避免调用真实 API。
- 讲解：`avoid calling the real API` 说明使用目的。

## 9. regression
- 发音：/rɪˈɡreʃən/
- 含义：回归问题；功能退化
- 开发语境：修复或改动导致旧功能出问题。
- 例句：We need a regression test for this bug.
- 翻译：我们需要为这个缺陷补一个回归测试。
- 讲解：`regression test` 是测试保障中的关键概念。

## 10. flaky
- 发音：/ˈfleɪki/
- 含义：不稳定的
- 开发语境：测试时好时坏，结果不稳定。
- 例句：This test is flaky and should not block the release.
- 翻译：这个测试不稳定，不应该阻塞发布。
- 讲解：CI 场景里很常见。

## 11. vulnerability
- 发音：/ˌvʌlnərəˈbɪləti/
- 含义：漏洞
- 开发语境：安全风险点，如依赖漏洞、注入漏洞等。
- 例句：The scanner found a critical vulnerability in one of our dependencies.
- 翻译：扫描器在我们的某个依赖中发现了一个严重漏洞。
- 讲解：`critical vulnerability` 是安全领域高频词组。

## 12. encryption
- 发音：/ɪnˈkrɪpʃən/
- 含义：加密
- 开发语境：数据传输加密、存储加密。
- 例句：Sensitive data must be protected with encryption.
- 翻译：敏感数据必须通过加密进行保护。
- 讲解：`must be protected` 是安全规范常见表达。

## 13. decryption
- 发音：/diːˈkrɪpʃən/
- 含义：解密
- 开发语境：把密文还原成明文。
- 例句：The service fails during decryption when the key is rotated incorrectly.
- 翻译：当密钥轮换不正确时，服务会在解密阶段失败。
- 讲解：结合 `key rotation` 很常见。

## 14. secret
- 发音：/ˈsiːkrət/
- 含义：密钥材料；敏感凭据
- 开发语境：API key、token、密码等。
- 例句：Never hardcode secrets in the repository.
- 翻译：绝对不要把敏感凭据硬编码进代码仓库。
- 讲解：是最重要的安全开发规则之一。

## 15. permission
- 发音：/pərˈmɪʃən/
- 含义：权限
- 开发语境：用户权限、角色权限、资源访问控制。
- 例句：This user does not have permission to delete the record.
- 翻译：这个用户没有删除该记录的权限。
- 讲解：`does not have permission to ...` 是经典表达。

## 16. audit log
- 发音：/ˈɔːdɪt lɔːɡ/
- 含义：审计日志
- 开发语境：记录关键操作，便于追踪责任和排查问题。
- 例句：Every admin action should be recorded in the audit log.
- 翻译：每个管理员操作都应该记录到审计日志中。
- 讲解：合规和后台系统里很常见。

## 17. sanitize
- 发音：/ˈsænɪtaɪz/
- 含义：净化；清洗
- 开发语境：处理输入，防止 XSS、注入等风险。
- 例句：User-generated content must be sanitized before rendering.
- 翻译：用户生成内容在渲染前必须先做净化处理。
- 讲解：前端渲染和后端输入处理都用得到。

## 18. escape
- 发音：/ɪˈskeɪp/
- 含义：转义
- 开发语境：对特殊字符进行安全处理。
- 例句：Make sure all HTML output is properly escaped.
- 翻译：确保所有 HTML 输出都被正确转义。
- 讲解：XSS 防护中的常见表达。

## 19. authentication bypass
- 发音：短语表达
- 含义：绕过认证
- 开发语境：严重安全漏洞类型。
- 例句：The bug could lead to an authentication bypass.
- 翻译：这个缺陷可能导致认证绕过。
- 讲解：描述安全影响时很常见。

## 20. least privilege
- 发音：/liːst ˈprɪvəlɪdʒ/
- 含义：最小权限原则
- 开发语境：用户、服务和系统只拥有完成任务所需的最少权限。
- 例句：We should follow the principle of least privilege.
- 翻译：我们应该遵循最小权限原则。
- 讲解：安全治理中的基础原则。

## 21. penetration test
- 发音：/ˌpenɪˈtreɪʃən test/
- 含义：渗透测试
- 开发语境：模拟攻击发现系统安全弱点。
- 例句：The platform will undergo a penetration test next month.
- 翻译：这个平台下个月会进行一次渗透测试。
- 讲解：`undergo` 表示“接受、经历”。

## 22. exploit
- 发音：/ɪkˈsplɔɪt/
- 含义：利用漏洞
- 开发语境：攻击者利用系统弱点。
- 例句：This vulnerability is difficult to exploit, but it should still be fixed.
- 翻译：这个漏洞虽然不容易被利用，但仍然应该修复。
- 讲解：非常典型的安全评估说法。

## 23. incident
- 发音：/ˈɪnsɪdənt/
- 含义：事故；安全事件；线上故障
- 开发语境：广泛用于线上事件响应。
- 例句：We need a postmortem for this incident.
- 翻译：我们需要为这次事故写一份复盘。
- 讲解：`postmortem` 是 SRE/运维常用词。

## 24. mitigation
- 发音：/ˌmɪtɪˈɡeɪʃən/
- 含义：缓解措施
- 开发语境：问题尚未根治前先降低风险。
- 例句：The immediate mitigation is to disable the affected endpoint.
- 翻译：当前的紧急缓解措施是禁用受影响的接口端点。
- 讲解：线上应急中非常常见。

## 25. remediation
- 发音：/rɪˌmiːdiˈeɪʃən/
- 含义：修复措施
- 开发语境：从根本上解决漏洞或问题。
- 例句：The remediation plan includes code changes and configuration updates.
- 翻译：修复方案包括代码改动和配置更新。
- 讲解：比 mitigation 更偏长期根治。
