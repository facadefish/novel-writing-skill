# 多书并行压测基线 v0

## 压测目标
- p95 延迟不高于 9000ms
- 平均 prompt tokens 不高于 9000
- 平均 completion tokens 不高于 2600

## 场景与方法
- 书籍：`xh_001`、`ds_009`、`wx_017`
- 指令：`discuss plot`、`diagnose pacing`、`asset check consistency`
- 轮次：每书每命令 20 轮
- 数据字段：`latency_ms`、`prompt_tokens`、`completion_tokens`、`cache_hit`、`degrade_level`

## 样例记录（当前仅为模板样例）
- p50_latency_ms: 6210
- p95_latency_ms: 9480
- p99_latency_ms: 10120
- avg_prompt_tokens: 8015
- avg_completion_tokens: 2025
- alert_rate: 0.12

## 结论
- 当前样例基线显示 p95 仍超阈值，需要继续优化长历史裁剪与缓存命中。
- 该报告作为 v0 占位基线，后续需替换为真实批量执行结果。
