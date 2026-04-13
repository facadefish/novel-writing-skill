# 插件接口规范

## 目标
将“核心 Skill + 插件扩展”从概念落到可执行接口，确保角色/剧情/世界观插件可热插拔，且失败可降级。

## 插件声明
```yaml
plugin_id: plot
version: 1.0.0
capabilities:
  - discuss.plot
  - propose.routes
required_inputs:
  - book_id
  - session_id
optional_inputs:
  - chapter_id
fallback: core
```

## 运行协议
- 核心层先做参数校验与上下文打包。
- 插件返回标准字段：`status`、`result`、`risks`、`next_actions`。
- 插件异常时核心层接管，返回降级结果并附 `plugin_error`。

## 错误冒泡
- 插件参数错误：映射为 `INVALID_ARGUMENT`
- 插件依赖故障：映射为 `DEPENDENCY_UNAVAILABLE`
- 插件超时：核心层触发降级并记录审计日志

## 回退策略
- 回退目标：核心 Skill 的同类基础能力
- 回退要求：保持同一 `request_id/session_id`，保证链路可追踪
