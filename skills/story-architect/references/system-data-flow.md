---
name: system-data-flow-redirect
purpose: 重定向到权威版本
---

<context>
此文件已迁移到统一位置，避免多版本不同步问题。
</context>

<instructions>

## 权威版本位置

插件根目录下的 `skills/webnovel-query/references/system-data-flow.md`

## 加载方式

在 Codex 中直接读取 `../webnovel-query/references/system-data-flow.md`，或从插件根目录读取 `skills/webnovel-query/references/system-data-flow.md`。

## 快速参考

### 目录结构
```
项目根目录/
├── 正文/           # 章节文件
├── 大纲/           # 卷纲/章纲
├── 设定集/         # 世界观/力量体系/角色卡
└── .webnovel/
    ├── state.json          # 权威状态
    ├── workflow_state.json # 工作流断点
    ├── index.db            # SQLite 索引
    └── archive/            # 归档数据
```

### 当前结构核心变化
- **双阶段架构**: 写前整理上下文 + 写后沉淀事实
- **无 XML 标签**: 纯正文写作，写后从正文中提取实体
- **SQLite 存储**: entities/aliases/state_changes 迁移到 index.db
- **state.json 精简**: 保持 < 5KB，主要包含 progress/protagonist_state/strand_tracker/disambiguation

</instructions>

