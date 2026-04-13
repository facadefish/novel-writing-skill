# 结论摘要
下面给出一次 OpenClaw 调用失败重试并命中幂等重放的预期返回。该返回用于验证 `idempotency_key` 生效与回退可解释性。

```yaml
request_id: req_20260411_203501
session_id: sess_ch018_plot
status: ok
idempotent_replay: true
idempotency_key: idem_ch018_plot_v1
result:
  summary: "返回首次成功生成的剧情路线结果"
  source: "replayed_from_previous_success"
options:
  - id: route_stable
    label: "稳健路线"
  - id: route_aggressive
    label: "激进路线"
risks:
  - level: medium
    item: "激进路线会提高角色关系破裂概率"
next_actions:
  - "如需改写请更换 idempotency_key 后重试"
  - "高风险决策请执行 novel apply decision 确认落库"
fallback:
  previous_error: "DEPENDENCY_UNAVAILABLE"
  recovery_strategy: "serve_cached_success_result"
  user_hint: "依赖恢复后可发起新 key 获取新结果"
```

## 失败回退建议
当依赖故障导致首次调用失败时，建议先返回 `DEPENDENCY_UNAVAILABLE` 与退避时间。若后续重试携带同一幂等键且已有成功快照，应优先返回快照结果，避免重复计算和状态漂移。
