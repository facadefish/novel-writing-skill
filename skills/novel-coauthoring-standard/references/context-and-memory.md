# 上下文与记忆模型

## L1/L2/L3 分层上下文
- L1（全书层）：题材、核心设定、角色底层动机、禁忌规则
- L2（卷层）：阶段目标、主要矛盾、卷内关键关系
- L3（章层）：当前章目标、上一章结果、未回收伏笔

## 最小注入原则
- 角色讨论仅注入相关角色与必要剧情片段。
- 世界观讨论仅注入世界观规则与冲突条目。
- 剧情讨论优先注入当前卷目标与相关角色关系。
- 任何请求均不默认注入全书全文。

## 预算约束
- 注入预算按命令配置上限。
- 超限时优先摘要化 L2/L3，再缩减可选历史片段。
- 若仍超限，返回预算错误并附降级建议。

## 成本与性能治理
- 命令级统计字段：`latency_ms`、`prompt_tokens`、`completion_tokens`、`cache_hit`、`degrade_level`。
- 默认阈值：`latency_ms<=9000`、`prompt_tokens<=9000`、`completion_tokens<=2600`。
- 阈值触发：任一指标超阈值即追加性能事件，并在输出 `metrics.alert=true`。
- 降级顺序：长历史裁剪 -> 路线数收敛 -> 仅返回结论与下一步。
- 缓存策略：`book_id + command + normalized_args + context_hash` 命中则复用最近结果，并标记 `idempotent_replay=false`、`cache_hit=true`。

## 作品资产模型
- `characters/*.yaml`: 角色卡
- `world/*.yaml`: 世界观规则
- `plot/routes/*.yaml`: 剧情路线
- `hooks/*.yaml`: 伏笔池
- `rules/taboos.yaml`: 禁忌规则

## 会话状态机
- drafted：草拟阶段
- proposed：候选阶段
- confirmed：作者确认
- applied：已落库

状态迁移约束：
- proposed -> applied：不允许直接迁移
- 必须经过 confirmed 才能写入高风险字段
