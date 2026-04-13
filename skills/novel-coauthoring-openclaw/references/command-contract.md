# 命令契约

## 最小命令集
- `novel discuss character --id <character_id> --topic <topic>`
- `novel discuss world --topic <topic>`
- `novel discuss plot --chapter <chapter_id> --goal <goal>`
- `novel diagnose pacing --chapter <chapter_id>`
- `novel propose routes --chapter <chapter_id> --count <n>`
- `novel apply decision --from <session_id>`
- `novel rollback decision --session-id <session_id> --to <proposed|confirmed>`
- `novel audit show --session-id <session_id>`
- `novel asset check consistency --scope <book|volume|chapter> [--path-glob <glob>]`
- `novel memory show --scope <book|volume|chapter>`
- `novel memory pin --target <id>`
- `novel memory unpin --target <id>`

## 项目级命令
- `novel project init --book-id <id> --title <title> --genre <genre>`
- `novel project switch --book-id <id>`
- `novel project status --book-id <id>`

## 短别名（易记模式）
- `novel ch` = `novel discuss character`
- `novel wd` = `novel discuss world`
- `novel pt` = `novel discuss plot`
- `novel pg` = `novel diagnose pacing`
- `novel rt` = `novel propose routes`
- `novel ok` = `novel apply decision`
- `novel rb` = `novel rollback decision`
- `novel au` = `novel audit show`
- `novel ck` = `novel asset check consistency`
- `novel ms` = `novel memory show`
- `novel mp` = `novel memory pin`
- `novel mu` = `novel memory unpin`
- `novel pi` = `novel project init`
- `novel psw` = `novel project switch`
- `novel pst` = `novel project status`

说明：
- 短别名与完整命令完全等价，参数保持一致。
- 默认推荐新用户先看完整命令，熟悉后切换短别名。

## 通用输入字段
- `request_id`: 请求唯一标识
- `session_id`: 会话标识
- `idempotency_key`: 幂等键
- `book_id`: 作品标识
- `genre`: 题材标识

## 通用输出字段
- `request_id`
- `session_id`
- `status`
- `result`
- `options`
- `risks`
- `next_actions`
- `idempotent_replay`
- `metrics`
- `audit_ref`

## 一致性检查输出字段
- `conflicts[].id`: 冲突唯一标识
- `conflicts[].level`: `low|medium|high`
- `conflicts[].reason`: 冲突原因
- `conflicts[].fix`: 修复建议
- `conflicts[].affected_paths[]`: 受影响资产路径

## 审计查询输出字段
- `input_summary`
- `command`
- `model_route`
- `key_output`
- `confirmed_by`
- `persist_result`
- `timeline[]`

## 错误码
- `INVALID_ARGUMENT`: 参数缺失或非法
- `CONTEXT_BUDGET_EXCEEDED`: 上下文预算超限
- `UNSUPPORTED_OPERATION`: 请求了不支持能力
- `AUTH_FAILED`: 鉴权失败
- `DEPENDENCY_UNAVAILABLE`: 外部依赖不可用
- `STATE_TRANSITION_DENIED`: 状态迁移不合法
- `AUDIT_NOT_FOUND`: 未找到对应审计链路
- `CONSISTENCY_CONFLICT`: 检测到高优冲突需先修复

## 退出码
- `0`: 成功
- `2`: 参数问题
- `3`: 鉴权问题
- `4`: 预算或配额问题
- `5`: 依赖故障
- `6`: 不支持能力
