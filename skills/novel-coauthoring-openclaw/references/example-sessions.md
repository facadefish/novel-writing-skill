# 最小示例会话（开箱即用）

## 示例 1：角色讨论
输入：
`novel discuss character --id c001 --topic motivation`

期望输出：
- 给出 2-3 套动机修订方案
- 标注每套方案对主线推进的影响
- 给出风险提示与推荐下一步

## 示例 2：剧情编排
输入：
`novel discuss plot --chapter ch018 --goal "提高期待感"`

期望输出：
- 提供稳健/激进/商业向 3 条路线
- 每条路线含代价与适配读者体验
- 可附 YAML 结构化块供编排

## 示例 3：世界观一致性
输入：
`novel discuss world --topic power-system`

期望输出：
- 列出规则冲突点
- 给出修复建议与影响范围
- 标注是否涉及高风险字段

## 示例 4：节奏诊断
输入：
`novel diagnose pacing --chapter ch018`

期望输出：
- 段落级节奏问题定位
- 可替换节奏骨架
- 正文示例必须为自然段落
