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
python week01\d1_check_env.py
```

VS Code 里直接 `code .` 打开本目录，右下角解释器选 `.venv` 那个（已经预配置好了）。

## 目录约定

```
qa-lab/
├── week01/          第 1 周（环境自检、Python 基础）
│   ├── d1_check_env.py
│   ├── d2_test_data.py
│   └── D2-任务卡.md
├── tests/           pytest 用例（第 10 周起）
├── data/            测试数据、评测集
├── reports/         测试报告产物（不入库）
└── .venv/           虚拟环境（不入库）
```

命名规则：`weekNN/dM_主题.py`，第 N 周、第 M 天。学完 24 周，这个目录本身就是你学习轨迹的证据。

## 每天的收尾动作

```bash
git add .
git commit -m "day2: 注册测试数据生成器"
git push
```
