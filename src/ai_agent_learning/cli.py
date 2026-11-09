"""agent 命令行入口。"""

from __future__ import annotations

import argparse
from pathlib import Path

from . import __version__

ROADMAP = [
    "01 基础概念：Agent / Tool / Memory / Planning",
    "02 LLM API 基础：Function Calling、结构化输出",
    "03 ReAct 模式：推理 + 行动循环",
    "04 框架实践：LangChain / LangGraph 或 OpenAI Agents SDK",
    "05 RAG：检索增强与知识库",
    "06 多 Agent 协作",
    "07 评估与调试：轨迹分析、可观测性",
    "08 项目实战：一个能用的端到端 Agent",
]

LAB_TEMPLATE = """# {name}

- 阶段：{stage}
- 日期：
- 目标：
- 复现步骤：
- 结论 / 踩坑：

## 代码

## 参考
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="agent",
        description="AI Agent 学习仓库的命令行工具",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("roadmap", help="打印学习路线")

    lab = sub.add_parser("lab", help="在 labs/ 下创建一个实验目录")
    lab.add_argument("name", help="实验目录名，如 01-react")
    lab.add_argument("--root", type=Path, default=Path.cwd(), help="仓库根目录，默认当前目录")
    lab.add_argument("--stage", default="待填", help="对应学习路线阶段")
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    if args.command == "roadmap":
        for item in ROADMAP:
            print(f"[ ] {item}")
        return 0

    if args.command == "lab":
        target = args.root / "labs" / args.name
        if target.exists():
            print(f"已存在，未覆盖：{target}")
            return 1
        target.mkdir(parents=True)
        (target / "README.md").write_text(
            LAB_TEMPLATE.format(name=args.name, stage=args.stage), encoding="utf-8"
        )
        print(f"已创建：{target}")
        return 0

    build_parser().print_help()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
