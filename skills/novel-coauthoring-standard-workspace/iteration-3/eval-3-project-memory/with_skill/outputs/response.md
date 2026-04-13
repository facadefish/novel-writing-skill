# 结论摘要
这个 Skill 现在支持“以作品为项目”记忆：每本书独立存档、独立上下文、独立决策链，不串书。

## 你能直接怎么用
1. 建项目  
`novel project init --book-id btm001 --title "霸天魔主" --genre xuanhuan`

2. 切项目  
`novel project switch --book-id btm001`

3. 查项目状态  
`novel project status --book-id btm001`

4. 查关键记忆  
`novel memory show --book-id btm001 --scope core`

## 记忆里存什么
- core：题材、世界观硬规则、主角底层动机  
- cast：角色卡、关系网、人物禁忌  
- plot：主线目标、关键冲突、伏笔池  
- state：当前推进状态、已确认决策、待确认决策

## 写入规则
- 低风险字段（标签、摘要）自动写入当前 book_id。  
- 高风险字段（主线走向、硬规则）必须确认后写入。  
- 没有 `book_id` 时只读，不落库。

## 为什么对网文作者有用
- 你不用每次重复讲设定，系统按作品项目记住关键事实。  
- 你同时开两本书也不串线。  
- 你在第 80 章回收伏笔时，系统能直接拉出该书历史节点。
