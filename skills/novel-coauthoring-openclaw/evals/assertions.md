# 评测断言建议

执行基准文件：`evals/executable-matrix.yaml`

## Eval 1：角色重做
- 断言 1：输出包含至少 3 套方案
- 断言 2：每套方案包含“主线影响”说明
- 断言 3：输出包含风险与下一步动作

## Eval 2：节奏诊断
- 断言 1：输出包含段落级问题定位
- 断言 2：输出包含可替换节奏骨架
- 断言 3：正文示例为自然段落而非条目

## Eval 3：OpenClaw 重放
- 断言 1：输出含 request_id 与 session_id
- 断言 2：输出含 idempotent_replay 字段
- 断言 3：输出能给出失败回退建议

## Eval 4：审计与回滚闭环
- 断言 1：`novel audit show` 返回 input_summary、model_route、persist_result
- 断言 2：`novel rollback decision` 执行后，审计 timeline 新增 rollback 事件
- 断言 3：当 session_id 不存在时返回 `AUDIT_NOT_FOUND`
