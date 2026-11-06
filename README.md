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

# 2. 跑环境自检（脚本会自动切到 .venv，不用先激活）
python week01\d1_check_env.py
```

第一次会看到「当前不是项目虚拟环境，自动切换后重跑」，这是正常的，之后就是 6/6。

VS Code 里直接 `code .` 打开本目录，右下角解释器选 `.venv` 那个（已经预配置好了）。

### 另外两种跑法（等价）

```bash
# 先激活，提示符前会出现 (.venv)
.venv\Scripts\activate
python week01\d1_check_env.py

# 或者直接用虚拟环境的解释器，一步到位
.venv\Scripts\python.exe week01\d1_check_env.py
```

### 常见报错

| 现象 | 原因 | 解决 |
|---|---|---|
| `无法加载文件 Activate.ps1，因为在此系统上禁止运行脚本` | PowerShell 默认策略是 Restricted | `Set-ExecutionPolicy -Scope CurrentUser RemoteSigned`（只需一次，不需要管理员），然后**关掉终端重开** |
| 自检报 `[FAIL] 虚拟环境 未激活 .venv` | 用 `python` 跑到系统 Python 上，且脚本的自动切换被 `QA_NO_RELAUNCH` 关掉了 | 去掉该环境变量，或用上面两种显式指定 `.venv` 的跑法 |
| `无法将 ...python.exe 项识别为 cmdlet` | PowerShell 里漏了 `.\` 前缀 | 写成 `.\.venv\Scripts\python.exe ...` |
| `python: command not found` | 新装的 Python 还没进当前终端 | 关掉终端重开一个 |



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
