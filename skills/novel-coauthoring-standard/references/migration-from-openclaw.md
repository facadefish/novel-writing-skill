# 从 OpenClaw 版迁移到标准版

## 为什么迁移
- 标准版以“任意 Agent 可接入”为默认目标，不绑定单一平台。
- OpenClaw、Hermes、Claude Code 仍可直接兼容调用。

## 命令兼容
- 所有原命令保持不变，无需改业务参数。
- 短别名同样可用：`ch/wd/pt/pg/rt/ok/rb/au/ck/ms/mp/mu/pi/psw/pst`。

## 关键文档替换
- `openclaw-integration.md` -> `agent-integration.md`
- `quickstart-openclaw.md` -> `quickstart-agent.md`

## 迁移步骤
1. 将 Skill 路径切换到 `skills/novel-coauthoring-standard/`
2. 保持原命令调用不变
3. 优先使用 `quickstart-agent.md` 启动新会话
4. 若仍在 OpenClaw 环境，参考兼容层文档即可

## 回退策略
- 若上游编排器强依赖 OpenClaw 文档字段，可临时继续用兼容层文件。
- 标准版不移除 OpenClaw 兼容说明，支持平滑双轨过渡。
