# 开箱即用指南（OpenClaw）

## 1) 安装后默认行为
- 默认入口：OpenClaw
- 默认触发：混合模式（关键场景自动触发，其余命令触发）
- 默认输出：Markdown 主输出，必要时附加 YAML 结构化块

## 2) 最小调用序列
1. 角色讨论  
`novel discuss character --id c001 --topic motivation`

2. 剧情讨论  
`novel discuss plot --chapter ch018 --goal "提高期待感"`

3. 世界观校验  
`novel discuss world --topic power-system`

4. 决策落库  
`novel apply decision --from session_001`

## 2.1) 速记写法（短别名）
1. 角色讨论  
`novel ch --id c001 --topic motivation`

2. 剧情讨论  
`novel pt --chapter ch018 --goal "提高期待感"`

3. 世界观校验  
`novel wd --topic power-system`

4. 决策落库  
`novel ok --from session_001`

## 3) 重试与幂等
- 每次调用附带 `idempotency_key`
- 重试同一请求应返回首次结果，并包含 `idempotent_replay=true`

## 4) 高风险写入规则
- 涉及主线走向、世界观硬规则、角色核心动机时，必须先确认再落库
- 建议先执行讨论命令，再执行 `novel apply decision`

## 5) 正文输出规则
- 当请求正文示例时，输出必须是自然段落
- 不允许以条目清单代替正文段落

## 6) 常见失败与处理
- 参数缺失：检查必填参数，重试
- 预算超限：缩小 topic 范围或先做摘要诊断
- 依赖故障：走降级路径，仅返回核心结果与恢复建议
