---
name: story-reviewer
description: AI故事审查技能。用于检查章节或大纲的设定一致性、时间线、角色OOC、逻辑、节奏、爽点兑现、追读力和AI味，并输出可执行修改建议。
---

# Story Reviewer

## Goal

Review story material and produce actionable findings.

## Review Axes

- continuity
- setting
- character
- timeline
- logic
- pacing
- cool-point payoff
- open-loop handling
- AI-flavor
- readability

## References

- `references/common-mistakes.md`
- `references/pacing-control.md`
- `../../references/review-schema.md`
- `../../references/shared/core-constraints.md`
- `../../references/shared/cool-points-guide.md`
- `../../references/shared/strand-weave-pattern.md`
- `../../references/review/blocking-override-guidelines.md`

## Output Schema

Lead with findings. Use this shape when structured output helps:

```json
{
  "issues": [
    {
      "severity": "critical|high|medium|low",
      "category": "continuity|setting|character|timeline|ai_flavor|logic|pacing|other",
      "location": "",
      "description": "",
      "evidence": "",
      "fix_hint": "",
      "blocking": false
    }
  ],
  "summary": ""
}
```

Any critical contradiction that breaks canon, timeline, or core character motivation is blocking.
