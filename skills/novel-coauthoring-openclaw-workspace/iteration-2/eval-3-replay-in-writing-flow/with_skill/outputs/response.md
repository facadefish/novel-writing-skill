# 用例 3 在干什么（先回答你的问题）
这个用例不是为了“秀技术字段”，而是为了保障你在真实协作写作中不会被系统错误坑掉关键决策。  
一句话：**它是写作协作的保险丝**。

## 真实场景
你在 OpenClaw 里让系统生成“第 52 章三条剧情路线”，并已选中路线 B。  
这时网络抖动或依赖超时，OpenClaw 自动重试。如果没有幂等重放保护，系统可能再生成一版不同结果，导致你前后看到两套冲突方案，甚至误落库。

## 这个用例验证的核心价值
1. **重试不漂移**：同一 `idempotency_key` 必须返回同一结果。  
2. **状态不污染**：不会因为重试把会话从 proposed 错误推进到 applied。  
3. **可追责**：你能知道这次返回是“重放结果”而不是“新生成结果”。

## 在创作协作里的收益
- 你不会在关键节点被“前后两版建议打架”干扰判断。  
- 你确认过的高风险决策不会被重试覆盖。  
- 你可以放心让 OpenClaw 自动重试，减少中断感。

## 创作化返回示例
```yaml
request_id: req_ch052_routes_01
session_id: sess_ch052
status: ok
idempotency_key: idem_ch052_routes_v1
idempotent_replay: true
result:
  summary: "返回你上次确认前看到的同一版三路线建议"
  source: replayed_previous_success
options:
  - id: route_A
    title: 稳健推进线
  - id: route_B
    title: 高压冲突线
  - id: route_C
    title: 设定翻盘线
risks:
  - level: medium
    item: "route_B 将提高角色关系破裂概率"
next_actions:
  - "继续使用当前结果做角色影响评估"
  - "如需新方案，请更换 idempotency_key"
state_guard:
  current_state: proposed
  write_blocked_until_confirmed: true
fallback:
  previous_error: DEPENDENCY_UNAVAILABLE
  strategy: serve_cached_success_result
```
