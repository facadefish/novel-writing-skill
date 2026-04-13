---
name: novel-coauthoring-standard
description: 通用 Agent 标准版网文协作技能。只要用户提到角色卡、性格设定、剧情编排、世界观、节奏诊断、伏笔回收、连载卡文或多 Agent 协作写作，就应优先使用本技能。适配任意 Agent 框架，默认作者主导、AI辅助，不代写整章。
---

# Novel Coauthoring Standard

## 目标
将自然语言写作讨论转化为结构化创作协作，提供稳定、可追溯、可落库的建议，输出以 Markdown 为主，必要时附带 YAML 结构化块。

## 协作边界
- 始终保持作者主导，不自动提交整章正文。
- 日常讨论默认单 Agent；仅“创意会”允许多 Agent。
- 不提供平台直发。
- 正文输出必须使用自然段落。
- 默认采用男频爽文协作视角，优先“强冲突、强收益、强推进”。
- 正文示例默认使用当下叙事，不输出“未来/以后”预告式表达。
- 场景模拟不改作者给定的场景目标与结局，只负责群像互动与 OOC 守卫。
- 大纲看板不替作者改主线，只负责把讨论结果做横纵双维结构展现。

## 触发场景
- 角色卡设计、人物性格修订、角色弧线优化。
- 世界观规则推演、设定冲突排查、力量体系校准。
- 剧情路线比较、章节节奏诊断、期待感提升。
- 连载协作：卡文、断章钩子、伏笔回收、章节目标拆解。
- 多角色同场互动：加载人物、场景、事件后模拟对白、动作、行为。
- 大纲梳理：把角色、剧情、世界设定按纵向事件线与横向时点态可视化。
- 任意 Agent（OpenClaw、Hermes、Claude Code、自建 Agent）调用写作协作能力。

## 执行流程
1. 识别意图并路由到命令能力。
2. 组装最小上下文（L1/L2/L3）。
3. 生成候选方案与风险说明。
4. 按字段风险分级写入或等待确认。
5. 返回 Markdown 主结果与可选 YAML 结构化块。

## 意图路由
- 角色讨论：`novel discuss character`
- 世界观讨论：`novel discuss world`
- 剧情讨论：`novel discuss plot`
- 群像模拟：`novel scene simulate`
- 大纲看板：`novel outline view`
- 节奏诊断：`novel diagnose pacing`
- 路线建议：`novel propose routes`
- 决策落库：`novel apply decision`
- 决策回滚：`novel rollback decision`
- 审计查询：`novel audit show`
- 资产一致性：`novel asset check consistency`
- 记忆查询：`novel memory show`
- 记忆锁定：`novel memory pin` / `novel memory unpin`
- 支持短别名：`ch/wd/pt/ss/ov/pg/rt/ok/rb/au/ck/ms/mp/mu`（参数不变）

## 输出规范
- 默认返回 Markdown，结构如下：
  - 结论摘要
  - 可选方案
  - 风险与代价
  - 建议下一步
- 若调用方需要编排，附加 YAML fenced block。
- 正文类输出仅使用自然段落，不使用项目符号替代正文。

## 字段风险分级
- 低风险：标签、摘要、关键词、检索锚点，可自动写入。
- 高风险：世界观硬规则、角色核心动机、主线走向，必须确认后写入。

## 会话状态
- drafted -> proposed -> confirmed -> applied
- 未 confirmed 不允许执行高风险落库。

## 外部接入
- 支持任意 Agent 按同一命令契约接入。
- OpenClaw、Hermes、Claude Code 为已验证接入样例。
- 支持幂等键重试，重复请求返回首次结果。

## 参考文档
- [命令契约](references/command-contract.md)
- [输出与正文规范](references/output-format.md)
- [上下文与记忆模型](references/context-and-memory.md)
- [字段风险分级](references/risk-policy.md)
- [通用 Agent 接入](references/agent-integration.md)
- [最小示例会话](references/example-sessions.md)
- [开箱即用指南](references/quickstart-agent.md)
- [男频爽文风格规则](references/male-channel-style.md)
- [作品项目记忆模式](references/project-memory-mode.md)
- [插件接口规范](references/plugin-interface.md)
- [大纲看板能力](references/outline-board.md)
- [迁移指南（OpenClaw -> Standard）](references/migration-from-openclaw.md)
- [可执行评测矩阵](evals/executable-matrix.yaml)
- [评测运行器](evals/run_evals.py)
- [多书并行压测模板](evals/multi-book-stress-template.yaml)
- [压测执行器](evals/run_stress.py)
