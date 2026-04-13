# Iteration 4 评测导航

## 本轮补强目标
- 补齐审计与回滚闭环样例，验证 `session_id` 级追溯。
- 补齐资产一致性检查样例，输出冲突级别与受影响路径。
- 补齐 OpenClaw 签名鉴权、重试退避与性能指标样例。
- 补齐多书并行项目记忆样例，验证 `book_id` 切换隔离。

## 用例目录
- Eval 1：审计与回滚链路
  - `eval-1-audit-rollback/with_skill/outputs/response.md`
- Eval 2：多书项目记忆切换
  - `eval-2-multi-book-memory-switch/with_skill/outputs/response.md`
- Eval 3：OpenClaw 签名重试与性能治理
  - `eval-3-openclaw-signed-retry-metrics/with_skill/outputs/response.md`
- Perf Baseline v0：多书并行压测占位基线
  - `perf-baseline-v0.md`
- Perf Raw v1：多书并行压测实测样本
  - `perf-raw-metrics-v1.jsonl`
- Perf Baseline v1：多书并行压测实测基线
  - `perf-baseline-v1.md`
