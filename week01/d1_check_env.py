"""Day 1 环境自检。

用法（二选一）：
    .venv\\Scripts\\activate
    python week01\\d1_check_env.py

    # 或者不激活，直接用虚拟环境里的解释器
    .venv\\Scripts\\python.exe week01\\d1_check_env.py

全部显示 [ OK ] 就说明环境搭好了，可以开始第 2 天的学习。
"""

import platform
import subprocess
import sys
from pathlib import Path

GIT_CANDIDATES = [
    r"C:\Program Files\Git\cmd\git.exe",
    "git",
]


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
    raise SystemExit(main())
