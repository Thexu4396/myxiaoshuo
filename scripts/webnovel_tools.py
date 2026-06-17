#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Small Codex-native helpers for the webnovel writer plugin."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def safe_slug(title: str) -> str:
    slug = re.sub(r'[\\/:*?"<>|]+', "", title.strip())
    slug = re.sub(r"\s+", "-", slug).strip("-")
    return slug if slug and not slug.startswith(".") else "proj-webnovel"


def project_status(project_root: Path) -> dict:
    root = project_root.resolve()
    return {
        "project_root": str(root),
        "has_state": (root / ".webnovel" / "state.json").is_file(),
        "has_story_system": (root / ".story-system").is_dir(),
        "settings_files": sorted(p.name for p in (root / "设定集").glob("*.md")) if (root / "设定集").is_dir() else [],
        "outline_files": sorted(p.name for p in (root / "大纲").glob("*.md")) if (root / "大纲").is_dir() else [],
        "chapter_files": sorted(p.name for p in (root / "正文").glob("*.md")) if (root / "正文").is_dir() else [],
    }


def init_skeleton(project_root: Path) -> dict:
    root = project_root.resolve()
    for name in [".webnovel", "设定集", "大纲", "正文", "审查报告"]:
        (root / name).mkdir(parents=True, exist_ok=True)
    state_path = root / ".webnovel" / "state.json"
    if not state_path.exists():
        state_path.write_text(json.dumps({"project_info": {}, "progress": {}}, ensure_ascii=False, indent=2), encoding="utf-8")
    memory_path = root / ".webnovel" / "project_memory.json"
    if not memory_path.exists():
        memory_path.write_text(json.dumps({"patterns": []}, ensure_ascii=False, indent=2), encoding="utf-8")
    return project_status(root)


def init_project(workspace: Path, title: str, genre: str, target_words: int | None, target_chapters: int | None) -> dict:
    root = workspace.resolve() / safe_slug(title)
    init_skeleton(root)

    state_path = root / ".webnovel" / "state.json"
    state = {
        "project_info": {
            "title": title,
            "genre": genre,
            "target_words": target_words,
            "target_chapters": target_chapters,
        },
        "progress": {
            "current_chapter": 0,
            "phase": "initialized",
        },
    }
    state_path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")

    outline = root / "大纲" / "总纲.md"
    if not outline.exists():
        outline.write_text(
            f"# {title}\n\n"
            f"## 题材\n\n{genre}\n\n"
            "## 一句话故事\n\n待补充。\n\n"
            "## 核心冲突\n\n待补充。\n\n"
            "## 创意约束\n\n- 反套路：待补充。\n- 硬约束：待补充。\n",
            encoding="utf-8",
        )

    for name, heading in [
        ("世界观.md", "世界观"),
        ("力量体系.md", "力量体系"),
        ("主角卡.md", "主角卡"),
        ("反派设计.md", "反派设计"),
    ]:
        path = root / "设定集" / name
        if not path.exists():
            path.write_text(f"# {heading}\n\n待补充。\n", encoding="utf-8")

    return project_status(root)


def main() -> None:
    parser = argparse.ArgumentParser(description="Codex-native webnovel helper commands")
    sub = parser.add_subparsers(dest="command", required=True)

    status_p = sub.add_parser("status", help="Print read-only project status")
    status_p.add_argument("project_root", nargs="?", default=".")

    init_p = sub.add_parser("init-skeleton", help="Create minimal project folders")
    init_p.add_argument("project_root", nargs="?", default=".")

    project_p = sub.add_parser("init-project", help="Create a minimal titled novel project")
    project_p.add_argument("--workspace", default=".")
    project_p.add_argument("--title", required=True)
    project_p.add_argument("--genre", required=True)
    project_p.add_argument("--target-words", type=int, default=None)
    project_p.add_argument("--target-chapters", type=int, default=None)

    args = parser.parse_args()
    if args.command == "status":
        result = project_status(Path(args.project_root))
    elif args.command == "init-skeleton":
        result = init_skeleton(Path(args.project_root))
    else:
        result = init_project(
            Path(args.workspace),
            args.title,
            args.genre,
            args.target_words,
            args.target_chapters,
        )
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

