# 输出与正文规范

## 主输出格式
默认输出 Markdown，固定包含以下区块：
- 结论摘要
- 可选方案
- 风险与代价
- 建议下一步

## 结构化块
当调用方需要自动编排时，附加 YAML fenced block：

```yaml
request_id: req_xxx
session_id: sess_xxx
status: ok
result:
  summary: ...
options:
  - id: option_a
    title: ...
risks:
  - level: high
    item: ...
next_actions:
  - ...
```

## 正文输出规则
- 正文必须为自然段落。
- 不得使用项目符号替代正文段落。
- 若输出章节片段，至少包含“场景推进 + 角色行为 + 情绪或冲突变化”。

## 正文反例
- 反例 1：整段都是条目清单。
- 反例 2：只给剧情提纲，没有自然叙事段落。
- 反例 3：只给台词，不给叙事承接。
