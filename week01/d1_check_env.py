"""Day 1 环境自检。

用法（任选一种，效果一样）：
    python week01\\d1_check_env.py              # 脚本会自己切到 .venv 重跑
    .venv\\Scripts\\activate 后 python week01\\d1_check_env.py
    .venv\\Scripts\\python.exe week01\\d1_check_env.py

如果不想让脚本自动切换（比如你就是想检查系统的 Python），
先设环境变量 QA_NO_RELAUNCH=1 再运行。

全部显示 [ OK ] 就说明环境搭好了，可以开始第 2 天的学习。
"""

import os
import platform
import subprocess
import sys
from pathlib import Path

GIT_CANDIDATES = [
    r"C:\Program Files\Git\cmd\git.exe",
    "git",
]


def venv_python() -> Path | None:
    """找到项目里的 .venv 解释器，找不到就返回 None。"""
    root = Path(__file__).resolve().parent.parent
    for rel in (r".venv\Scripts\python.exe", ".venv/bin/python"):
        candidate = root / rel
        if candidate.exists():
            return candidate
    return None


def ensure_venv() -> None:
    """不在 .venv 里就自动用它重跑一遍，省得用户记激活命令。"""
    if sys.prefix != sys.base_prefix:  # 已经在虚拟环境里
        return
    if os.environ.get("QA_NO_RELAUNCH") == "1":
        return
    py = venv_python()
    if py is None:  # 没有 .venv，就按原样继续，让检查项去报错
        return

    print("当前不是项目虚拟环境，自动切换后重跑：", flush=True)
    print(f"  现在  {sys.executable}", flush=True)
    print(f"  切换  {py}", flush=True)
    print(flush=True)
    env = dict(os.environ, QA_NO_RELAUNCH="1")
    sys.exit(subprocess.call([str(py), str(Path(__file__).resolve())], env=env))


def run(cmd: list[str]) -> str:
    """执行外部命令并返回版本号，失败时返回空字符串。"""
    try:
        result = subprocess.run(
            cmd, capture_output=True, text=True, timeout=10, encoding="utf-8"
        )
        return (result.stdout or result.stderr).strip().splitlines()[0]
    except Exception:
        return ""


def check(label: str, ok: bool, detail: str) -> bool:
    mark = "[ OK ]" if ok else "[FAIL]"
    print(f"{mark} {label:<16}{detail}")
    return ok


def main() -> int:
    print("=" * 56)
    print(" AI 测试工程师 · Day 1 环境自检")
    print("=" * 56)

    results = []

    # 1. Python 版本必须是 3.12
    py_version = platform.python_version()
    results.append(
        check("Python", py_version.startswith("3.12"), f"{py_version}  ({sys.executable})")
    )

    # 2. 是否跑在虚拟环境里（这是最容易漏掉的一步）
    in_venv = sys.prefix != sys.base_prefix
    results.append(check("虚拟环境", in_venv, sys.prefix if in_venv else "未激活 .venv"))

    if not in_venv:
        print()
        print("  当前用的是系统 Python，不是项目里的 .venv：")
        print(f"    {sys.executable}")
        print("  这样跑，依赖和项目环境对不上。两种改法，随便选一种：")
        print(r"    .venv\Scripts\python.exe week01\d1_check_env.py   # 直接用虚拟环境的解释器")
        print(r"    .venv\Scripts\activate                            # 或者先激活，再 python ...")
        print("  如果 PowerShell 报「因为在此系统上禁止运行脚本」，先执行一次：")
        print(r"    Set-ExecutionPolicy -Scope CurrentUser RemoteSigned")

    # 3. 第三方包
    for pkg in ("requests", "pytest"):
        try:
            module = __import__(pkg)
            results.append(check(pkg, True, getattr(module, "__version__", "已安装")))
        except ImportError:
            results.append(check(pkg, False, "未安装，执行 pip install " + pkg))

    # 4. Git
    git_version = ""
    for cmd in GIT_CANDIDATES:
        git_version = run([cmd, "--version"])
        if git_version:
            break
    results.append(check("Git", bool(git_version), git_version or "未找到 git 命令"))

    # 5. 项目目录结构
    root = Path(__file__).resolve().parent.parent
    results.append(check("项目根目录", (root / ".venv").exists(), str(root)))

    print("-" * 56)
    passed = sum(results)
    total = len(results)
    print(f"通过 {passed}/{total}")

    if passed == total:
        print("\n环境就绪。第 2 天见。")
        print("今天的收尾动作：")
        print('  git add . && git commit -m "day1: 环境自检脚本"')
        return 0

    print("\n有项目没通过，按上面的提示补一下。")
    return 1


if __name__ == "__main__":
    ensure_venv()
    raise SystemExit(main())
