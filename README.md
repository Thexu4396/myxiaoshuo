# AI Story Craft

这是给 Codex 与 GPT-5.4 使用的长篇 AI 创作 rules 和 skills 包。

它只保留创作方法、题材资料、模板和轻量检索工具，目标是让 AI 协助你稳定完成从脑洞、总纲、卷纲、章节、审查到项目记忆沉淀的完整流程。

## Included

- `skills/`: Codex skills for story architecture, plot planning, chapter writing, review, canon query, craft memory, and project status.
- `references/`: Chinese fiction rules, genre profiles, review schema, pacing/cool-point guidance, CSV knowledge tables.
- `templates/`: setting, outline, chapter brief, long-line tracking, genre, and golden-finger templates.
- `scripts/reference_search.py`: local CSV craft-knowledge search helper.
- `scripts/webnovel_tools.py`: optional project skeleton and status helper.

## Skills

- `story-architect`: 把脑洞、题材和参考方向整理成故事蓝图、作品总设定、设定集和总纲。
- `plot-planner`: 把总纲拆成卷纲、时间线、章纲、长线追踪、伏笔与爽点节奏。
- `chapter-writer`: 根据章纲、设定、人物状态和创作记忆写出可发布正文。
- `story-reviewer`: 审查设定一致性、节奏、爽点兑现、追读力和 AI 味。
- `canon-query`: 查询角色状态、设定、伏笔、时间线和章节事实。
- `craft-memory`: 沉淀有效写法、偏好、钩子、对白和反面教训。
- `project-status`: 只读盘点项目状态、缺口和下一步。

## Suggested Use

Ask Codex in natural language:

- 使用 `story-architect` 初始化一本都市异能新书
- 使用 `plot-planner` 规划第一卷
- 使用 `chapter-writer` 写第 1 章
- 使用 `story-reviewer` 审查第 1 章
- 使用 `canon-query` 查询主角当前境界和未回收伏笔
- 使用 `craft-memory` 记住这章有效的钩子写法
- 使用 `project-status` 汇总当前项目状态

## Key Templates

- `templates/output/作品总设定.md`: 作品级 story bible，记录核心体验、世界规则、分卷、人物总表、禁改设定和连载维护备注。
- `templates/output/设定集-人物卡.md`: 通用人物卡，补足驱动、弧光、语言表现、剧情使用说明和当前状态追踪。
- `templates/output/大纲-章节小纲.md`: 写作前章纲，明确本章任务、开场状态、段落推进、结尾钩子和连贯性检查。
- `templates/output/大纲-长线追踪.md`: 连载维护表，跟踪主线、角色弧光、关系线、伏笔回收、设定变动和接下来三章。

## Notes

This is a clean Codex-native rules and skills package, not a compatibility layer for another runtime.
