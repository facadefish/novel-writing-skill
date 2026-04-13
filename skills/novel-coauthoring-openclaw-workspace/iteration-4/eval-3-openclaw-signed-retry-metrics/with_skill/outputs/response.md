结论：OpenClaw 调用链路在签名鉴权与重试场景下可稳定返回，并产出性能告警。

请求头
- X-Client-Id: oc_writer_01
- X-Timestamp: 1776046502
- X-Nonce: n8f2aa91
- X-Signature: hmac_sha256:8f3c...
- idempotency_key: idem_plot_2406

调用过程
- 首次调用超时，系统返回可重试提示，建议退避 1s
- 第二次调用命中依赖恢复，返回正常结果
- 第三次同幂等键重放，直接返回首次成功结果并标记 `idempotent_replay=true`

返回摘要
- request_id: req_plot_2406
- session_id: sess_plot_ch24_03
- status: ok
- metrics:
  - latency_ms: 9620
  - prompt_tokens: 8420
  - completion_tokens: 2110
  - cache_hit: false
  - alert: true
  - degrade_level: l2_summary

降级建议
- 当前响应超阈值，优先把“历史争执片段”压缩为 5 行摘要。
- 路线候选从 3 条收敛到 2 条，保持强冲突与强收益不变。
