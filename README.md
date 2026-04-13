# Novel Coauthoring Standard Skill

通用 Agent 标准版网文协作 Skill，面向“作者主导、AI辅助”的长篇连载工作流。

## 你能得到什么
- 群像场景模拟：加载人物/场景/事件，输出对白、动作、行为与 OOC 风险。
- 大纲看板：横纵双维展示剧情结构，便于日更推进与完本控制。
- 稳定工程能力：审计、回滚、一致性检查、幂等重试、可执行评测与 CI。

## 功能边界
- 不代写整章，不替作者改主线。
- 对 `scene simulate` 与 `outline view`，不改作者给定目标与结局。

## 10 分钟上手
1. 查看快速指南：`skills/novel-coauthoring-standard/references/quickstart-agent.md`
2. 跑评测自检：
```bash
python skills/novel-coauthoring-standard/evals/run_evals.py
```
3. 试运行两个核心命令：
```bash
novel ss --event e018 --chars "linyan,hantu,zhifa" --scene "玄铁矿场夜审" --goal "夺钥符并立威" --ending "林砚带伤突围"
novel ov --book-id xh_demo_001 --scope chapter --target ch018 --view both
```

## 目录说明
- `skills/novel-coauthoring-standard/`：标准版 Skill 主体
- `skills/novel-coauthoring-standard-workspace/`：迭代样例与评测输出
- `.github/workflows/`：CI 工作流
- `docs/`：命令速查与输出结构文档

## 版本与路线
- 当前推荐：`novel-coauthoring-standard`
- 兼容层：`novel-coauthoring-openclaw`（历史链路保留）
- 迁移说明：`skills/novel-coauthoring-standard/references/migration-from-openclaw.md`

## 开源协议
本项目使用 MIT 协议，见 `LICENSE`。
