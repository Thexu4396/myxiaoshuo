---
name: chapter-writer
description: AI章节写作技能。用于基于章纲、设定、角色状态和创作记忆写出可发布正文，并进行一致性、节奏、爽点、对白和AI味自检，适合 GPT-5.4 协同创作。
---

# Chapter Writer

## Goal

Produce one publishable chapter from canon and the current chapter plan.

## Workflow

1. Load only relevant canon: current outline, recent chapters, character state, power rules, open loops, and project memory.
2. Before formal prose drafting, confirm a detailed outline with the user unless the user explicitly says the current outline is already final and approved.
3. Build a writing brief: hard constraints, must-cover beats, opening state, segment progression, forbidden contradictions, style targets, continuity checks, and end hook.
4. Draft pure prose only after the detailed outline is approved. Do not include placeholders, analysis, or hidden notes in the chapter body.
5. Review once for blocking issues.
6. Polish for rhythm, dialogue intent, scene texture, emotional specificity, and anti-AI patterns, removing formulaic AI phrasing so the chapter reads closer to natural human prose.
7. Record newly introduced facts, character-state changes, relationship temperature changes, and opened/paid-off foreshadowing for later canon updates, and backfill the related outline or setting notes when the finished chapter adds or changes canon.

## Rules

- Formal chapter writing is blocked until the user has reviewed and approved a detailed chapter outline.
- The approved outline must include chapter goal, required information, relationship/situation change, opening state, segment-level progression, ending hook, foreshadowing/recovery, style reminders, and continuity checks.
- Do not contradict established canon.
- Do not solve a promised tension without replacing it with a new forward pull.
- Keep dialogue motivated by desire, pressure, evasion, testing, or negotiation.
- Make new entities identifiable by name, function, and memorable detail.
- Do not use repeated generic beats such as "缓缓", "淡淡", "微微" as emotional shortcuts.
- Do not repeat the previous chapter's function unless the new chapter escalates stakes, cost, relationship, or information.
- If a chapter changes a character or relationship, make the change visible through a choice, behavior, or consequence, not only narration.
- After drafting, explicitly run one anti-AI polish pass to remove summary voice, template phrasing, repeated sentence patterns, and hollow emotional labels.
- After the chapter is finalized, update the relevant chapter outline and setting/state notes so canon files stay aligned with what was actually written.

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
- `../../templates/output/大纲-章节小纲.md`
- `../../templates/output/大纲-长线追踪.md`
- `../../references/review-schema.md`

Use `scripts/reference_search.py` for targeted Chinese webnovel craft lookup.

## Output

Return the chapter text first. Put any status note after the chapter and keep it short.
