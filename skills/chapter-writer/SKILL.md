---
name: chapter-writer
description: AI章节写作技能。用于基于章纲、设定、角色状态和创作记忆写出可发布正文，并进行一致性、节奏、爽点、对白和AI味自检，适合 GPT-5.4 协同创作。
---

# Chapter Writer

## Goal

Produce one publishable chapter from canon and the current chapter plan.

## Workflow

1. Load only relevant canon: current outline, recent chapters, character state, power rules, open loops, and project memory.
2. Build a writing brief: hard constraints, must-cover beats, forbidden contradictions, style targets, and end hook.
3. Draft pure prose. Do not include placeholders, analysis, or hidden notes in the chapter body.
4. Review once for blocking issues.
5. Polish for rhythm, dialogue intent, scene texture, emotional specificity, and anti-AI patterns.
6. Record newly introduced facts for later canon updates.

## Rules

- Do not contradict established canon.
- Do not solve a promised tension without replacing it with a new forward pull.
- Keep dialogue motivated by desire, pressure, evasion, testing, or negotiation.
- Make new entities identifiable by name, function, and memorable detail.
- Do not use repeated generic beats such as "缓缓", "淡淡", "微微" as emotional shortcuts.

## References

- `references/polish-guide.md`
- `references/style-adapter.md`
- `references/style-variants.md`
- `references/writing/typesetting.md`
- `references/writing/scene-description.md`
- `references/writing/dialogue-writing.md`
- `references/writing/emotion-psychology.md`
- `references/writing/desire-description.md`
- `references/writing/combat-scenes.md`
- `references/writing/genre-hook-payoff-library.md`
- `../../references/shared/core-constraints.md`
- `../../references/shared/strand-weave-pattern.md`
- `../../references/shared/cool-points-guide.md`
- `../../references/review-schema.md`

Use `scripts/reference_search.py` for targeted Chinese webnovel craft lookup.

## Output

Return the chapter text first. Put any status note after the chapter and keep it short.
