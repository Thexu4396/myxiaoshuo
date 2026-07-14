# AI Story Craft Code Wiki

## 项目概述

**AI Story Craft** 是面向 **Codex** 与 **GPT-5.4** 的长篇 AI 创作 rules 和 skills 包。它提供完整的创作工作流支持，涵盖从脑洞构思、设定构建、大纲规划、章节写作、质量审查到创作记忆沉淀的全流程。

**核心目标**：让 AI 稳定协助完成从灵感到连载发布的完整长篇创作流程。

---

## 项目架构

### 整体架构图

```
┌─────────────────────────────────────────────────────────────────────┐
│                        AI Story Craft                               │
├─────────────────────────────────────────────────────────────────────┤
│  ┌─────────────┐                                                    │
│  │   Skills    │  ── 创作技能层（7个核心技能）                       │
│  └──────┬──────┘                                                    │
│         │                                                           │
│  ┌──────▼──────┐                                                    │
│  │  Scripts    │  ── 工具脚本层（检索、安全、兼容性）                │
│  └──────┬──────┘                                                    │
│         │                                                           │
│  ┌──────▼──────┐                                                    │
│  │ References  │  ── 知识库层（CSV数据、写作指南、题材资料）         │
│  └──────┬──────┘                                                    │
│         │                                                           │
│  ┌──────▼──────┐                                                    │
│  │  Templates  │  ── 模板层（题材预设、输出骨架）                    │
│  └─────────────┘                                                    │
└─────────────────────────────────────────────────────────────────────┘
```

### 目录结构

```
/workspace/
├── .codex-plugin/           # Codex 插件配置
│   └── plugin.json          # 插件元数据
├── skills/                  # 创作技能（核心模块）
│   ├── story-architect/     # 故事架构师
│   ├── plot-planner/        # 剧情规划师
│   ├── chapter-writer/      # 章节写作
│   ├── story-reviewer/      # 故事审查
│   ├── canon-query/         # 设定查询
│   ├── craft-memory/        # 创作记忆沉淀
│   └── project-status/      # 项目状态盘点
├── scripts/                 # 工具脚本
│   ├── reference_search.py  # CSV知识库检索
│   ├── webnovel_tools.py    # 项目初始化与状态
│   ├── security_utils.py    # 安全工具函数
│   ├── runtime_compat.py    # 运行时兼容性
│   ├── genre_taxonomy.py    # 题材分类解析
│   └── requirements.txt     # Python依赖
├── references/              # 创作参考资料
│   ├── csv/                 # CSV格式知识库
│   ├── index/               # 索引与加载映射
│   ├── outlining/           # 大纲相关指南
│   ├── review/              # 审查相关指南
│   ├── shared/              # 共享指南
│   ├── taxonomy/            # 题材分类索引
│   └── *.md                 # 核心参考文档
├── templates/               # 模板文件
│   ├── genres/              # 题材预设模板（36种）
│   ├── output/              # 输出格式模板
│   └── golden-finger-templates.md
├── 创作项目/                 # 示例创作项目
└── README.md
```

---

## 核心技能模块

### 1. story-architect（故事架构师）

**职责**：将灵感转化为可持续连载的故事蓝图

**输出文件**：
- `.webnovel/state.json` - 项目状态
- `.webnovel/idea_bank.json` - 灵感库
- `设定集/作品总设定.md` - 故事圣经
- `设定集/世界观.md` - 世界规则
- `设定集/力量体系.md` - 能力系统
- `设定集/人物卡.md` - 人物设定
- `设定集/主角卡.md` - 主角设定
- `设定集/反派设计.md` - 反派设计
- `大纲/总纲.md` - 故事总纲

**工作流程**：
1. 收集关键信息（标题、题材、目标长度、核心设定）
2. 提取参考作品中的可迁移技法
3. 提出2-3个创意包（卖点、反套路规则、硬约束）
4. 生成故事圣经级别的完整设定

**关键参考**：
- [init-collection-schema.md](file:///workspace/skills/story-architect/references/init-collection-schema.md)
- [genre-tropes.md](file:///workspace/skills/story-architect/references/genre-tropes.md)
- [worldbuilding/*.md](file:///workspace/skills/story-architect/references/worldbuilding/)

---

### 2. plot-planner（剧情规划师）

**职责**：将总纲和设定拆解为可执行的连载大纲

**输出文件**：
- `大纲/卷节拍表.md` - 卷级节奏规划
- `大纲/卷时间线.md` - 时间线梳理
- `大纲/章节小纲.md` - 章节详细规划
- `大纲/长线追踪.md` - 连载维护表

**工作流程**：
1. 读取现有设定和总纲
2. 从宏观到微观拆解：Arc → Volume → Chapter Cluster → Chapter Beat
3. 为每章定义目标、冲突、信息增量、情感转折、爽点兑现和结尾钩子
4. 维护长线追踪表（主线状态、角色弧光、伏笔管理）

**关键规则**：
- 每章必须改变至少一个维度：情节状况、角色状态、关系温度、读者信息、资源/能力状态、风险等级
- 不允许连续三章有相同的叙事功能（除非是有意的递进）
- 待确认的大纲必须标记为「待确认」，用户确认后才能交给写作

---

### 3. chapter-writer（章节写作）

**职责**：基于章纲和设定写出可发布的正文

**工作流程**：
1. 加载相关设定：当前大纲、近期章节、角色状态、力量规则、开放伏笔
2. 确认详细章纲（用户批准后才能开始写作）
3. 构建写作简报：硬约束、必包含节拍、开场状态、段落推进、风格目标、连贯性检查、结尾钩子
4. 起草纯散文正文
5. 进行一次防AI味打磨（去除公式化表达）
6. 记录新增事实、角色状态变化、伏笔开启/回收

**核心规则**：
- 正式写作前必须获得用户对章纲的批准
- 默认采用冷静观察型叙事声音：克制用词、具体细节、可见压力、最小作者过度陈述
- 对话必须由欲望、压力、回避、试探或谈判驱动
- 章节标题不超过8个汉字，优先选择最尖锐的事件或判断
- 不重复上一章的功能，除非新章节升级了赌注、代价、关系或信息

**写作参考**：
- [polish-guide.md](file:///workspace/skills/chapter-writer/references/polish-guide.md)
- [style-adapter.md](file:///workspace/skills/chapter-writer/references/style-adapter.md)
- [writing/dialogue-writing.md](file:///workspace/skills/chapter-writer/references/writing/dialogue-writing.md)
- [writing/combat-scenes.md](file:///workspace/skills/chapter-writer/references/writing/combat-scenes.md)

---

### 4. story-reviewer（故事审查）

**职责**：检查章节或大纲的质量问题

**审查维度**：
| 维度 | 说明 |
|------|------|
| continuity | 设定一致性 |
| setting | 世界观合理性 |
| character | 角色行为一致性（OOC检测） |
| timeline | 时间线逻辑 |
| logic | 情节逻辑 |
| pacing | 节奏控制 |
| cool-point payoff | 爽点兑现 |
| open-loop handling | 伏笔处理 |
| AI-flavor | AI味检测 |
| readability | 可读性 |

**输出格式**：JSON结构化结果，包含严重程度、类别、位置、描述、证据、修复建议和是否阻塞

**关键参考**：
- [common-mistakes.md](file:///workspace/skills/story-reviewer/references/common-mistakes.md)
- [pacing-control.md](file:///workspace/skills/story-reviewer/references/pacing-control.md)
- [review-schema.md](file:///workspace/references/review-schema.md)

---

### 5. canon-query（设定查询）

**职责**：从项目文件中查询设定信息，给出来源引用

**数据源优先级**：
1. 确认的设定文件（设定集/*.md、大纲/*.md、已接受的章节笔记、项目记忆）
2. 维护文件（长线追踪、角色当前状态、伏笔表、时间线）
3. 最近章节文本
4. .webnovel/下的结构化状态文件
5. 参考文档（仅用于解释，不作为项目事实）

**输出格式**：包含概要、详细信息和不确定/缺失部分，附数据源路径和行号引用

---

### 6. craft-memory（创作记忆沉淀）

**职责**：将有效写法、钩子、节奏、对白等经验整理为项目记忆

**记忆条目格式**：
```json
{
  "pattern_type": "hook",
  "description": "钩子写法描述",
  "source_chapter": "第XX章",
  "importance": "high|medium|low"
}
```

**pattern_type分类**：hook（钩子）、pacing（节奏）、dialogue（对白）、payoff（兑现）、emotion（情感）、format（格式）、anti_ai（防AI）、genre（题材）、other（其他）

**存储位置**：`.webnovel/project_memory.json`，不存在时创建或更新`创作记忆.md`

---

### 7. project-status（项目状态盘点）

**职责**：只读汇总项目状态

**检查内容**：
- 项目根目录和写入安全性
- 设定集完整性
- 大纲完整性
- 长线追踪表完整性
- 最新章节
- .webnovel/state.json状态
- 开放伏笔和悬而未决的承诺
- 角色状态、关系线、伏笔、世界规则变更风险

---

## 工具脚本模块

### 1. reference_search.py

**功能**：CSV知识库检索工具，使用BM25算法进行关键词搜索

**核心函数**：

| 函数名 | 功能说明 |
|--------|----------|
| `load_tables(csv_dir, table)` | 加载CSV数据表 |
| `search(csv_dir, skill, query, table, genre, max_results)` | 执行BM25搜索 |
| `_bm25_score(query_terms, doc_terms, avg_dl, k1, b, idf_map)` | BM25评分计算 |
| `_compute_idf(query_terms, all_docs)` | 计算IDF值 |
| `_build_summary(row, table_name)` | 构建内容摘要 |
| `resolve_genre(genre)` | 题材规范化解析 |

**支持的CSV数据表**：

| 表名 | 前缀 | 角色 | 注入位置 |
|------|------|------|----------|
| 命名规则 | NR | base | MASTER_SETTING.base_context |
| 场景写法 | SP | base | CHAPTER_BRIEF.dynamic_context |
| 写作技法 | WT | base | CHAPTER_BRIEF.dynamic_context |
| 桥段套路 | TR | dynamic | CHAPTER_BRIEF.dynamic_context |
| 爽点与节奏 | PA | dynamic | CHAPTER_BRIEF.dynamic_context |
| 人设与关系 | CH | base | MASTER_SETTING.base_context |
| 金手指与设定 | SY | base | MASTER_SETTING.base_context |
| 题材与调性推理 | GR | route | MASTER_SETTING.route |
| 裁决规则 | RS | reasoning | CHAPTER_BRIEF.writing_guidance |

**使用示例**：
```bash
python reference_search.py --skill write --query "角色命名" --genre 玄幻
python reference_search.py --skill write --table 命名规则 --query "战斗描写" --max-results 3
```

---

### 2. webnovel_tools.py

**功能**：项目初始化与状态管理工具

**核心函数**：

| 函数名 | 功能说明 |
|--------|----------|
| `safe_slug(title)` | 将标题转换为安全的文件名 |
| `project_status(project_root)` | 获取项目状态信息 |
| `init_skeleton(project_root)` | 创建最小项目目录结构 |
| `init_project(workspace, title, genre, target_words, target_chapters)` | 创建完整项目 |

**项目目录结构**：
```
项目根目录/
├── .webnovel/
│   ├── state.json          # 项目状态
│   └── project_memory.json # 创作记忆
├── 设定集/
│   ├── 世界观.md
│   ├── 力量体系.md
│   ├── 主角卡.md
│   └── 反派设计.md
├── 大纲/
│   └── 总纲.md
├── 正文/
└── 审查报告/
```

**CLI命令**：
```bash
python webnovel_tools.py status [project_root]
python webnovel_tools.py init-skeleton [project_root]
python webnovel_tools.py init-project --workspace . --title "小说名" --genre 都市 --target-words 1500000
```

---

### 3. security_utils.py

**功能**：安全工具函数库，防止路径遍历、命令注入、并发冲突等安全问题

**核心函数**：

| 函数名 | 功能说明 | 安全目标 |
|--------|----------|----------|
| `sanitize_filename(name, max_length)` | 清理文件名 | 防止路径遍历(CWE-22) |
| `sanitize_commit_message(message, max_length)` | 清理Git提交消息 | 防止命令注入(CWE-77) |
| `create_secure_directory(path, mode)` | 创建安全目录 | 权限控制(0o700) |
| `create_secure_file(file_path, content, mode)` | 创建安全文件 | 权限控制(0o600) |
| `validate_integer_input(value, field_name)` | 验证整数输入 | 防止弱验证漏洞 |
| `atomic_write_json(file_path, data, use_lock, backup)` | 原子化写入JSON | 防止并发冲突(CWE-362/CWE-367) |
| `read_json_safe(file_path, default)` | 安全读取JSON | 错误处理和默认值 |
| `restore_from_backup(file_path)` | 从备份恢复文件 | 数据恢复 |
| `is_git_available()` | 检测Git可用性 | 优雅降级 |
| `git_graceful_operation(args, cwd, fallback_msg)` | 优雅执行Git操作 | 无Git环境降级 |

**原子写入策略**：
1. 写入临时文件（同目录，确保同文件系统）
2. 使用filelock获取排他锁（可选）
3. 备份原文件（可选）
4. 原子重命名（os.replace在POSIX上是原子操作）

---

### 4. runtime_compat.py

**功能**：运行时兼容性工具，主要处理Windows平台兼容性

**核心函数**：

| 函数名 | 功能说明 |
|--------|----------|
| `enable_windows_utf8_stdio(skip_in_pytest)` | 在Windows上启用UTF-8标准输入输出 |
| `normalize_windows_path(value)` | 将POSIX风格路径规范化为Windows盘符路径 |

**路径转换示例**：
- Git Bash/MSYS: `/d/desktop/...` → `D:/desktop/...`
- WSL: `/mnt/d/desktop/...` → `D:/desktop/...`

---

### 5. genre_taxonomy.py

**功能**：题材分类解析器，将用户输入的题材标签解析为规范的题材分类

**核心数据结构**：

| 类名 | 说明 |
|------|------|
| `GenreEntry` | 题材条目（标签、规范题材、类型、模板文件、标签集合、别名） |
| `GenreResolution` | 解析结果（原始标签、规范题材、匹配标签、模板文件、各类标签、未解析项、警告） |
| `GenreTaxonomy` | 题材分类本体（条目集合、查找表） |

**规范题材集合（15种）**：
- 都市、玄幻、仙侠、奇幻、科幻
- 历史、悬疑、游戏、古言、现言
- 幻言、年代、种田、快穿、衍生

**核心函数**：

| 函数名 | 功能说明 |
|--------|----------|
| `load_genre_taxonomy(index_path)` | 加载题材分类（带缓存） |
| `resolve_genre_input(raw_label, index_path)` | 解析题材输入，返回完整的GenreResolution |
| `resolve_canonical_genre(genre, index_path)` | 解析为规范题材名 |
| `resolve_template_files(genre, index_path)` | 获取对应的模板文件列表 |
| `normalize_genre_label_for_profile(genre, index_path)` | 规范化题材标签用于配置文件 |

**题材类型优先级**：
```
route(0) > platform(1) > canonical(2) > preset(3) > legacy(4) > format(5) > trope(6)
```

---

## 知识库层

### CSV知识库目录（references/csv/）

| 文件名 | 内容 |
|--------|------|
| 命名规则.csv | 角色、地点、势力等命名规则 |
| 场景写法.csv | 各类场景的写作模式 |
| 写作技法.csv | 通用写作技巧和方法 |
| 桥段套路.csv | 常见桥段和套路模板 |
| 爽点与节奏.csv | 爽点设计和节奏控制 |
| 人设与关系.csv | 人物设定和关系模式 |
| 金手指与设定.csv | 金手指设计和系统设定 |
| 题材与调性推理.csv | 题材分类和调性指导 |
| 裁决规则.csv | 各题材的风格优先级和裁决规则 |

**CSV字段结构**：
- 编号、适用技能、分类、层级、关键词、意图与同义词、适用题材、核心摘要、大模型指令、详细展开、毒点

---

### 共享指南（references/shared/）

| 文件 | 内容 |
|------|------|
| core-constraints.md | 核心创作约束 |
| cool-points-guide.md | 爽点设计指南 |
| strand-weave-pattern.md | 多线交织模式 |
| naming-and-voice-gaps.md | 命名与叙事声音差异 |

---

### 题材模板（templates/genres/）

共36种题材预设模板：
- 修仙、克苏鲁、历史古代、历史脑洞、古言、多子多福
- 女频悬疑、宫斗宅斗、年代、幻想言情、悬疑灵异、悬疑脑洞
- 抗战谍战、无限流、替身文、末世、民国言情、游戏体育
- 狗血言情、现实题材、现言脑洞、电竞、直播文、知乎短篇
- 种田、科幻、系统流、职场婚恋、西幻、规则怪谈
- 豪门总裁、都市异能、都市日常、都市脑洞、青春甜宠、高武、黑暗题材

---

### 输出模板（templates/output/）

| 文件 | 内容 |
|------|------|
| 作品总设定.md | 故事圣经骨架 |
| 设定集-世界观.md | 世界观设定模板 |
| 设定集-力量体系.md | 力量体系模板 |
| 设定集-主角卡.md | 主角设定模板 |
| 设定集-人物卡.md | 通用人物卡模板 |
| 设定集-女主卡.md | 女主设定模板 |
| 设定集-反派设计.md | 反派设计模板 |
| 设定集-金手指.md | 金手指设定模板 |
| 大纲-总纲.md | 总纲模板 |
| 大纲-卷节拍表.md | 卷节奏规划模板 |
| 大纲-卷时间线.md | 卷时间线模板 |
| 大纲-章节小纲.md | 章节详细规划模板 |
| 大纲-长线追踪.md | 连载维护追踪表 |
| 复合题材-融合逻辑.md | 复合题材融合指南 |

---

## 依赖关系

### Python依赖（scripts/requirements.txt）

| 依赖 | 版本 | 用途 |
|------|------|------|
| Python | >= 3.10 | 运行环境 |
| aiohttp | >= 3.8.0 | 异步HTTP客户端（API调用） |
| filelock | >= 3.0.0 | 文件锁（状态文件并发控制） |
| pydantic | >= 2.0.0 | Schema校验 |
| pytest | >= 7.0.0 | 单元测试（开发/测试） |
| pytest-cov | >= 4.1.0 | 覆盖率统计 |
| pytest-asyncio | >= 0.23.0 | 异步测试支持 |
| pytest-timeout | >= 2.3.0 | 测试超时保护 |

### 模块依赖关系

```
reference_search.py ──┬── genre_taxonomy.py
                      └── (内置，无外部依赖)

security_utils.py ────┬── runtime_compat.py
                      └── filelock (可选)

webnovel_tools.py ────┬── (内置，无外部依赖)
                      └── security_utils.py (间接)

genre_taxonomy.py ────┬── references/taxonomy/genre-index.csv
                      └── (内置，无外部依赖)

runtime_compat.py ────┬── (内置，无外部依赖)
```

---

## 项目运行方式

### 环境要求

1. **Python 版本**：Python 3.10 及以上
2. **Codex 环境**：需要在 Codex 或兼容的 AI 代理环境中使用 skills
3. **可选依赖**：安装 `scripts/requirements.txt` 中的依赖

### 安装依赖

```bash
cd /workspace/scripts
pip install -r requirements.txt
```

### 使用技能

在 Codex 中使用自然语言调用：

```
使用 story-architect 初始化一本都市异能新书
使用 plot-planner 规划第一卷
使用 chapter-writer 写第 1 章
使用 story-reviewer 审查第 1 章
使用 canon-query 查询主角当前境界和未回收伏笔
使用 craft-memory 记住这章有效的钩子写法
使用 project-status 汇总当前项目状态
```

### 工具脚本使用

**参考检索**：
```bash
python scripts/reference_search.py --skill write --query "战斗描写" --genre 玄幻 --max-results 5
```

**项目初始化**：
```bash
python scripts/webnovel_tools.py init-project --workspace ./创作项目 --title "我的小说" --genre 都市 --target-words 1500000 --target-chapters 500
```

**项目状态**：
```bash
python scripts/webnovel_tools.py status ./创作项目/xiangmu1
```

**安全自检**：
```bash
python scripts/security_utils.py
```

---

## 数据流转

### 创作工作流数据流转

```
灵感输入
    │
    ▼
story-architect (故事架构)
    │
    ├──► .webnovel/state.json
    ├──► 设定集/作品总设定.md
    ├──► 设定集/世界观.md
    ├──► 设定集/力量体系.md
    ├──► 设定集/人物卡.md
    └──► 大纲/总纲.md
            │
            ▼
        plot-planner (剧情规划)
            │
            ├──► 大纲/卷节拍表.md
            ├──► 大纲/卷时间线.md
            ├──► 大纲/章节小纲.md
            └──► 大纲/长线追踪.md
                    │
                    ▼
                chapter-writer (章节写作)
                    │
                    ├──► 正文/第XX章.md
                    └──► 更新设定和大纲文件
                            │
                            ▼
                        story-reviewer (审查)
                            │
                            ▼
                        craft-memory (沉淀经验)
                            │
                            ▼
                        .webnovel/project_memory.json
```

### 知识检索数据流转

```
用户查询 → reference_search.py
                │
                ├──► 加载 CSV 数据表
                │       └── references/csv/*.csv
                │
                ├──► 题材过滤
                │       └── genre_taxonomy.py
                │               └── references/taxonomy/genre-index.csv
                │
                ├──► 技能过滤 (适用技能列)
                │
                ├──► BM25 关键词搜索
                │
                └──► 返回 JSON 结果
```

---

## 关键设计模式

### 1. 分层架构

项目采用清晰的分层架构：
- **技能层**：面向用户的创作能力接口
- **工具层**：可复用的通用工具函数
- **知识层**：领域知识和参考资料
- **模板层**：输出格式规范

### 2. 设定驱动（Canon-Driven）

所有创作基于已确认的设定文件，确保一致性：
- 设定文件是唯一事实来源
- 查询优先从文件读取，不依赖记忆猜测
- 新增事实必须写入设定文件，不能静默依赖

### 3. 审查即服务（Review-as-a-Service）

审查技能独立于写作技能，可在任何阶段调用：
- 结构化输出便于自动化处理
- 严重程度分级支持阻塞机制
- 可执行的修复建议

### 4. 创作记忆沉淀

将有效写法沉淀为项目记忆：
- 支持多种模式类型分类
- 按重要性分级
- 不删除旧记忆，支持累积

### 5. 安全优先

所有外部输入经过安全清理：
- 文件名防路径遍历
- 命令参数防注入
- 文件写入使用原子操作
- 权限控制防止未授权访问

---

## 扩展指南

### 添加新技能

1. 在 `skills/` 目录下创建新技能文件夹
2. 创建 `SKILL.md` 定义技能元数据、目标、工作流程、规则和参考
3. 创建 `agents/openai.yaml` 配置AI代理
4. 创建 `references/` 目录存放技能专属参考文档

### 添加新题材模板

1. 在 `templates/genres/` 目录下创建 `<题材名>.md` 文件
2. 在 `references/taxonomy/genre-index.csv` 中添加对应的分类条目
3. 在 `references/csv/题材与调性推理.csv` 中添加题材调性配置
4. 在 `references/csv/裁决规则.csv` 中添加题材裁决规则

### 添加新CSV知识库

1. 在 `references/csv/` 目录下创建 `<表名>.csv` 文件
2. 按标准字段结构组织数据
3. 在 `scripts/reference_search.py` 的 `CSV_CONFIG` 中添加表配置
4. 配置搜索列权重、输出列、角色和注入位置

---

## 示例项目

项目包含一个示例创作项目 `创作项目/xiangmu1/`：

**项目结构**：
```
创作项目/xiangmu1/
├── 大纲与设定/
│   ├── 大纲-150万字分卷规划.md
│   ├── 大纲-总纲.md
│   ├── 大纲-第一案-背锅程序员.md
│   ├── 章节小纲-第一案-背锅程序员-30章.md
│   ├── 设定集-世界规则.md
│   ├── 设定集-主角卡.md
│   ├── 设定集-异能-周瑾-坍压.md
│   ├── 设定集-异能进阶规划模板.md
│   ├── 设定集-金手指.md
│   ├── 设定集-金手指限制与代价.md
│   └── 设定集-高承岳人物设计.md
└── 正文/
    ├── 第001章 被裁六月.md
    ├── 第002章 背锅视频.md
    ├── ...
    └── 第030章 回不去的人.md
```

---

## 许可证

项目采用 **GPL-3.0** 许可证。
