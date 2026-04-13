# 会话启动包（可直接开聊）

## 0. 初始化作品
```bash
novel project init --book-id xh_demo_001 --title "玄铁镇狱录" --genre xuanhuan
novel project switch --book-id xh_demo_001
novel project status --book-id xh_demo_001
```

## 1. 第一轮对话指令
```bash
novel discuss character --id c001 --topic "主角核心动机与反差记忆点"
novel discuss world --topic "力量体系三层规则与禁忌"
novel discuss plot --chapter ch001 --goal "首章强冲突+当场兑现收益"
```

## 2. 作者开场话术
我写男频玄幻长篇，你是长期陪跑搭档。先帮我把首卷主线压成一句话，再给主角三条“能立刻出爽点”的推进路线。正文示例只用自然段落，当下叙事，不要“以后/未来会”。

## 3. 决策落库
```bash
novel apply decision --from session_001
novel audit show --session-id session_001
```

## 4. 风险与回滚
```bash
novel rollback decision --session-id session_001 --to confirmed
novel asset check consistency --scope chapter --path-glob "characters/*.yaml"
```

## 5. 第二轮连载推进
```bash
novel diagnose pacing --chapter ch002
novel propose routes --chapter ch002 --count 3
```

## 6. 速记版（同义短命令）
```bash
novel pi --book-id xh_demo_001 --title "玄铁镇狱录" --genre xuanhuan
novel psw --book-id xh_demo_001
novel ch --id c001 --topic "主角核心动机与反差记忆点"
novel wd --topic "力量体系三层规则与禁忌"
novel pt --chapter ch001 --goal "首章强冲突+当场兑现收益"
novel ok --from session_001
novel au --session-id session_001
novel rb --session-id session_001 --to confirmed
novel ck --scope chapter --path-glob "characters/*.yaml"
novel pg --chapter ch002
novel rt --chapter ch002 --count 3
```
