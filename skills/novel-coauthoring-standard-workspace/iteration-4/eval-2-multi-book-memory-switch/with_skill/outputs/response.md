结论：双书并行创作已按 `book_id` 隔离记忆，切换后不会串线。

执行记录
- novel project switch --book-id xh_001
- novel memory show --scope book
- 返回：主角“顾野”当前阶段目标是“夺回矿脉控制权”，卷主冲突为“宗门封锁”

- novel project switch --book-id ds_009
- novel memory show --scope book
- 返回：主角“祁川”当前阶段目标是“压住审判庭舆论战”，卷主冲突为“城邦同盟分裂”

隔离校验
- `xh_001` 记忆命名空间：`memory://xh_001/l1/*`
- `ds_009` 记忆命名空间：`memory://ds_009/l1/*`
- 同名字段 `main_conflict` 互不覆盖，最后写入时间分别独立

一致性检查结果
- command: novel asset check consistency --scope book
- conflicts:
  - id: cfx_19
  - level: medium
  - reason: `xh_001` 世界观规则“禁空阵”与第 42 章追击桥段冲突
  - fix: 把追击改为“地脉隧道封堵战”
  - affected_paths: `world/rules.yaml`, `plot/routes/ch42.yaml`
