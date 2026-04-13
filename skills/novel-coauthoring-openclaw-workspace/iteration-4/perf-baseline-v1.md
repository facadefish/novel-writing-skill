# 多书并行压测基线 v1

## 实测汇总
- samples: 180
- p50_latency_ms: 6845.0
- p95_latency_ms: 8446.6
- p99_latency_ms: 9082.26
- avg_prompt_tokens: 7573.43
- avg_completion_tokens: 1923.3
- alert_rate: 0.0222

## 阈值检查
- p95_latency_ms_ok: True
- avg_prompt_tokens_ok: True
- avg_completion_tokens_ok: True

## 结论
- 本轮多书并行压测：通过
