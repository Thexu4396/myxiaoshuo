---
name: story-architect
description: AI长篇故事架构技能。用于把脑洞、题材、参考作品或零散设定整理成可持续连载的故事蓝图、角色核、世界观、力量体系和创意约束包，适合 Codex 与 GPT-5.4 辅助创作。
---

# Story Architect

## Goal

Turn raw inspiration into a durable long-form story foundation.

Create or update:

- `.webnovel/state.json`
- `.webnovel/idea_bank.json`
- `设定集/世界观.md`
- `设定集/力量体系.md`
- `设定集/主角卡.md`
- `设定集/反派设计.md`
- `大纲/总纲.md`

## Workflow

1. Collect only blocking information: title, genre, target length, premise, protagonist desire/flaw, power/golden-finger design, world scale, antagonist pressure, target readers, and platform tone.
2. If reference works are provided, extract transferable craft patterns only. Do not copy names, factions, places, plot facts, or signature set pieces.
3. Propose 2-3 creative packages: selling point, anti-trope rule, 2-3 hard constraints, protagonist flaw driver, antagonist mirror, and opening hook.
4. Ask for confirmation before writing canon.
5. Generate files under a safe title-derived project folder unless the user explicitly chooses the current folder.
6. Verify that core files exist and are not placeholder-only.

## References

Load only what the current decision needs:

- `references/init-collection-schema.md`: collection fields.
- `references/genre-tropes.md`: genre formulas.
- `../../references/genre-profiles.md`: current genre profile.
- `references/creativity/creativity-constraints.md`: creative package schema.
- `references/creativity/selling-points.md`: selling point patterns.
- `references/worldbuilding/*.md`: world, faction, power, character, and consistency checks.
- `../../templates/output/*.md`: output skeletons.

Use `scripts/reference_search.py` for CSV lookup when naming, trope, scene, or setting knowledge is needed.

## Quality Gates

- The core promise can be stated in one sentence.
- The protagonist has desire, flaw, pressure, and room to change.
- The world rules limit choices instead of only decorating them.
- The power/golden-finger has cost, boundary, visibility, and growth rhythm.
- The creative constraints are strong enough to prevent generic execution.

## Output

End with:

```text
总状态：已完成 / 部分完成 / 需要你处理 / 未完成。

一、产生的文件与完成情况
二、过程中遇到的问题
三、下一步建议
```
