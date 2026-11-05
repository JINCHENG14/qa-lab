# qa-lab

AI 测试工程师学习计划的练习仓库。所有学习产出都往这里堆，24 周后它就是简历。

## 环境

| 项 | 版本 | 路径 |
|---|---|---|
| Python | 3.12.10 | `%LOCALAPPDATA%\Programs\Python\Python312` |
| 虚拟环境 | — | `.venv`（项目内，已配好） |
| Git | 2.56.0.4 | `C:\Program Files\Git` |
| VS Code | 1.145.0 | `%LOCALAPPDATA%\Programs\Microsoft VS Code` |
| pip 镜像 | 清华 TUNA | 已全局配置 |

## 怎么开始每天的学习

```bash
# 1. 进入项目
cd D:\学习\qa-lab

# 2. 激活虚拟环境（Windows）
.venv\Scripts\activate

# 3. 跑环境自检
python day1\check_env.py
```

VS Code 里直接 `code .` 打开本目录，右下角解释器选 `.venv` 那个（已经预配置好了）。

## 目录约定

```
qa-lab/
├── day1/            第一周的小脚本
├── tests/           pytest 用例（第 10 周起）
├── data/            测试数据、评测集
├── reports/         测试报告产物（不入库）
└── .venv/           虚拟环境（不入库）
```

## 每天的收尾动作

```bash
git add .
git commit -m "day1: 环境自检脚本"
```
