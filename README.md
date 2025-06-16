# ResumeAgent - 智能简历分析系统

ResumeAgent 是一个基于 Python 的智能简历分析系统，能够自动解析 PDF 简历，提取关键信息，并与岗位要求进行匹配度评估。系统使用 LangChain 和 Ollama 实现智能分析功能。

## 功能特点

- PDF 简历文本提取
- 简历关键信息提取（姓名、联系方式、教育背景等）
- 基于 LLM 的简历与岗位匹配度评估
- 详细的匹配分析报告（评分、优势、短板、推荐建议）

## 系统要求

- Python 3.12
- Ollama（用于运行本地 LLM 模型）

## 安装步骤

1. 克隆仓库：
```bash
git clone https://github.com/yourusername/ResumeAgent.git
cd ResumeAgent
```

2. 创建并激活虚拟环境：
```bash
# Windows
python -m venv .venv
.\.venv\Scripts\activate

# Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

3. 安装依赖：
```bash
pip install -r requirements.txt
```

4. 安装并配置 Ollama：
   - 从 [Ollama 官网](https://ollama.ai/) 下载并安装
   - 拉取所需模型：
```bash
ollama pull qwen
```

## 使用方法

1. 准备简历文件：
   - 在项目根目录创建 `data/resumes` 文件夹
   - 将 PDF 格式的简历放入该文件夹

2. 运行程序：
```bash
python src/main.py
```

3. 查看输出结果：
   - 简历解析信息
   - 关键信息提取结果
   - 岗位匹配度评估报告

## 项目结构

```
ResumeAgent/
├── src/                    # 源代码目录
│   ├── __init__.py        # 包初始化文件
│   ├── main.py            # 主程序入口
│   ├── parsers/           # 解析器模块
│   │   ├── __init__.py
│   │   ├── pdf_parser.py  # PDF 解析器
│   │   └── resume_parser.py # 简历解析器
│   └── matchers/          # 匹配器模块
│       ├── __init__.py
│       └── resume_matcher.py # 简历匹配器
├── data/                  # 数据目录
│   └── resumes/          # 简历文件目录
├── requirements.txt      # 项目依赖
├── setup.py             # 安装脚本
├── .gitignore          # Git 忽略文件
└── README.md           # 项目说明文档
```

## 配置说明

- 岗位描述：在 `src/main.py` 中修改 `job_description` 变量
- 简历路径：在 `src/main.py` 中修改 `resume_path` 变量
- LLM 模型：在 `src/matchers/resume_matcher.py` 中修改 `model_name` 参数

## 注意事项

1. 确保 PDF 文件格式正确且可读
2. 简历文本需要包含基本的结构化信息
3. Ollama 服务需要保持运行状态
4. 建议使用 Python 3.12 版本

## 贡献指南

欢迎提交 Issue 和 Pull Request 来帮助改进项目。

## 许可证

MIT License

## 联系方式

如有问题或建议，请通过以下方式联系：
- 提交 Issue
- 发送邮件至：your.email@example.com 