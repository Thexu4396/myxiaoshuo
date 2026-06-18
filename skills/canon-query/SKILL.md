---
name: canon-query
description: AI故事设定查询技能。用于从项目文件中查询角色状态、世界规则、力量体系、势力关系、伏笔、时间线、章节事实和创作记忆，并给出来源引用。
---

# Canon Query

## Goal

Answer project-canon questions from files, not memory guesses.

## Source Priority

1. Confirmed canon files: `设定集/*.md`, `大纲/*.md`, accepted chapter notes, and project memory.
2. Maintenance files such as `大纲/长线追踪.md`, character current-state sections, foreshadowing tables, and timeline files.
3. Recent chapter text.
4. Structured state files under `.webnovel/`, if present.
5. Reference docs only for interpretation, never as project fact.

## References

- `references/system-data-flow.md`
- `references/tag-specification.md`
- `references/advanced/foreshadowing.md`
- `../../references/shared/strand-weave-pattern.md`
- `../../templates/output/大纲-长线追踪.md`

## Output

Include source paths and line references when possible:

```markdown
# 查询结果：{关键词}

## 概要
- 匹配类型：
- 数据源：

## 详细信息

## 不确定或缺失
```

Do not modify files.
