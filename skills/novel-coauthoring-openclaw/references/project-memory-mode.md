# 作品项目记忆模式

## 目标
以作品为项目管理记忆。每本书独立命名空间，避免跨书污染。

## 项目键
- 主键：`book_id`
- 可选子键：`volume_id`、`chapter_id`

## 记忆分层
- `project/core`: 题材、世界观硬规则、主角底层动机
- `project/cast`: 角色卡、关系网、人物禁忌
- `project/plot`: 主线阶段目标、关键冲突、伏笔池
- `project/state`: 当前推进状态、已确认决策、待确认决策

## 建议命令
- `novel project init --book-id <id> --title <title> --genre <genre>`
- `novel project switch --book-id <id>`
- `novel project status --book-id <id>`
- `novel memory show --book-id <id> --scope <core|cast|plot|state>`
- `novel memory pin --book-id <id> --target <memory_id>`

## 写入规则
- 低风险字段自动写入当前 `book_id` 命名空间。
- 高风险字段仅在确认后写入，并记录 before/after 快照。
- 若未提供 `book_id`，系统只返回只读建议，不执行写入。

## 数据结构模板
- 使用 [project-memory-schema.yaml](../assets/project-memory-schema.yaml) 作为项目记忆模板。
