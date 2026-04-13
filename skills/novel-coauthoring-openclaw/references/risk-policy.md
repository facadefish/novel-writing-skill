# 字段风险分级策略

## 低风险字段（可自动落库）
- 标签
- 摘要
- 检索关键词
- 会话元数据

## 高风险字段（必须确认）
- 世界观硬规则
- 主线剧情走向
- 角色核心动机
- 关键关系逆转

## 落库策略
- 低风险：会话结束后可自动写入，并记录审计日志。
- 高风险：仅在收到 `novel apply decision --from <session_id>` 后写入。

## 审计字段
- request_id
- session_id
- input_summary
- command
- model_route
- key_output
- actor
- risk_level
- changed_fields
- before_snapshot
- after_snapshot
- confirmed_by
- confirmed_at
- persist_result
- fallback_chain
- timeline

## 回滚策略
- 仅允许对已 `applied` 的会话执行 `novel rollback decision`。
- 回滚目标仅允许 `confirmed` 或 `proposed`，不允许直接回滚到 `drafted`。
- 回滚后必须追加一条审计事件，记录 `rollback_from`、`rollback_to` 与执行人。

## 审计查询要求
- `novel audit show --session-id <session_id>` 返回讨论、确认、落库、回滚全链路。
- 当审计链路缺失时返回 `AUDIT_NOT_FOUND`，并附可恢复建议。
