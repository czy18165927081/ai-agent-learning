# AI Agent Learning

学习 AI Agent 的笔记、代码实验与资料汇总。仓库本身是一个可安装的 Python 包，附带 `agent` 命令行工具。

## 快速开始

要求：Python >= 3.12。推荐用 [uv](https://docs.astral.sh/uv/)。

```bash
git clone https://github.com/czy18165927081/ai-agent-learning.git
cd ai-agent-learning
uv sync                 # 建 .venv、装依赖、把本包以可编辑模式装入
uv run agent --help     # 运行 CLI
```

不用 uv 也可以（Windows）：

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -e .
agent roadmap
```

macOS / Linux 把激活命令换成 `source .venv/bin/activate`。

## CLI

| 命令 | 作用 |
|------|------|
| `agent --version` | 打印版本号 |
| `agent roadmap` | 打印 8 阶段学习路线 |
| `agent lab 01-react` | 在 `labs/01-react/` 生成实验目录与 README 模板 |

`agent lab` 默认在当前目录的 `labs/` 下创建；用 `--root <路径>` 指定其他仓库根目录，用 `--stage <阶段>` 标注所属阶段。目录已存在时不覆盖。

## 构建与安装 wheel

```bash
uv build                 # 产物：dist/*.whl 与 dist/*.tar.gz
pip install dist/ai_agent_learning-0.1.0-py3-none-any.whl
agent --version
```

## 目录结构

| 路径 | 内容 |
|------|------|
| `src/ai_agent_learning/` | 包源码与 CLI 实现（src 布局） |
| `tests/` | pytest 测试 |
| `notes/` | 学习笔记 |
| `labs/` | 每个阶段的小实验，用 `agent lab` 生成 |
| `projects/` | 实战项目 |
| `resources/` | 论文、文章、课程收藏 |

笔记类目录各放一个 README.md，因为 Git 不跟踪空目录。

## 开发

```bash
uv sync --group dev     # 安装 pytest / ruff
uv run pytest           # 跑测试
uv run ruff check .     # 静态检查
uv run agent roadmap    # 源码改动即时生效（可编辑安装）
```

版本号在 `src/ai_agent_learning/__init__.py` 和 `pyproject.toml` 各存一份，改版本时两处同步。

## 学习路线
- [ ] 01 基础概念：Agent / Tool / Memory / Planning
- [ ] 02 LLM API 基础：Function Calling、结构化输出
- [ ] 03 ReAct 模式：推理 + 行动循环
- [ ] 04 框架实践：LangChain / LangGraph 或 OpenAI Agents SDK
- [ ] 05 RAG：检索增强与知识库
- [ ] 06 多 Agent 协作
- [ ] 07 评估与调试：轨迹分析、可观测性
- [ ] 08 项目实战：一个能用的端到端 Agent

## 进度日志
| 日期 | 内容 | 产出 |
|------|------|------|
| 2026-11-04 | 建仓、README 骨架、uv 包初始化 | `pyproject.toml` / `uv.lock` |
| 2026-11-09 | 补齐 README、实体目录、CLI 与测试 | `agent` 命令可安装可运行 |

## 参考资料
- （待补充）
