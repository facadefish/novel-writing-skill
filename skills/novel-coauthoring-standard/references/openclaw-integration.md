# OpenClaw 接入规范（兼容层）

> 说明：标准版 Skill 以 `references/agent-integration.md` 为主，本文件保留给 OpenClaw 兼容接入场景。

## 接入优先级
- 第一优先：OpenClaw
- 兼容：Hermes、Claude Code

## 调用链路
- OpenClaw -> Skill 路由 -> 命令执行 -> Markdown 主输出 -> 可选 YAML 结构化块

## 鉴权与幂等
- 支持 API Key 或签名鉴权
- 每次调用应携带 `idempotency_key`
- 幂等重试返回首次结果并标记 `idempotent_replay=true`
- 签名鉴权头：`X-Client-Id`、`X-Timestamp`、`X-Nonce`、`X-Signature`
- 签名串：`method + path + body_sha256 + timestamp + nonce`
- 签名算法：`HMAC-SHA256`
- 时效窗口：请求时间戳与服务端时间偏差不超过 300 秒

## 失败回退
- 超时：返回可重试错误并附建议退避策略
- 依赖故障：返回 `DEPENDENCY_UNAVAILABLE`
- 预算超限：返回 `CONTEXT_BUDGET_EXCEEDED` 并触发摘要降级建议
- 重试策略：最多 3 次，退避间隔 `1s -> 2s -> 4s`，附带 `jitter<=300ms`
- 超过最大重试后返回统一错误结构与人工接管建议

## 端到端成功标准
- 命令可达
- 输出字段完整
- 重试可重放
- 降级可解释
