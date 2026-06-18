---
name: project-status
description: AI创作项目状态盘点技能。用于只读汇总长篇创作项目的目录、设定完整度、最新章节、伏笔风险、缺口和下一步建议。
---

# Project Status

## Goal

Provide a read-only project status view from local files.

## Check

- project root and write safety
- `设定集/` completeness
- `大纲/` completeness
- long-line tracker completeness, if `大纲/长线追踪.md` exists
- `正文/` latest chapter
- `.webnovel/state.json` if present
- open loops and dangling promises visible in outlines, notes, or chapter text
- character-state, relationship-line, foreshadowing, and world-rule change risks

## Output

```markdown
## 项目状态

## 最近章节

## 长线追踪

## 风险与缺口

## 下一步建议
```

Do not start servers or modify files unless the user explicitly asks.
