---
name: craft-memory
description: AI创作经验沉淀技能。用于把有效写法、钩子、节奏、对白、爽点兑现、反面教训和用户偏好整理进项目记忆，供后续章节复用。
---

# Craft Memory

## Goal

Turn a useful writing observation into reusable project memory.

## Workflow

1. Identify the pattern type: hook, pacing, dialogue, payoff, emotion, format, anti_ai, genre, or other.
2. Write a concise rule with context and example.
3. Append it to `.webnovel/project_memory.json` if available; otherwise create or update `创作记忆.md`.
4. Do not delete older memories.
5. Skip exact duplicates and tell the user.

## Memory Entry Shape

```json
{
  "pattern_type": "hook",
  "description": "",
  "source_chapter": null,
  "importance": "high|medium|low"
}
```
