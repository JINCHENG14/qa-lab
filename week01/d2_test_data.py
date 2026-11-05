"""Day 2 · 注册测试数据生成器

先读 week01/D2-任务卡.md，再动手。

运行：
    cd D:\\学习\\qa-lab
    .venv\\Scripts\\activate
    python week01\\d2_test_data.py

把下面 5 个 NotImplementedError 全部替换成真正的代码，
脚本底部的校验会自动跑一遍，6 项全 PASS 就完成了。
"""

import random
import re

# ------------------------------------------------------------------ 可用素材

SURNAMES = ["张", "王", "李", "赵", "陈", "刘", "杨", "黄", "周", "吴"]
GIVEN_NAMES = ["伟", "芳", "娜", "敏", "静", "强", "磊", "洋", "艳", "勇", "军", "杰"]

# 手机号段，第二位只允许 3-9，所以这里列的都是合法号段
PHONE_PREFIXES = [
    "130", "131", "133", "135", "136", "137", "138", "139",
    "150", "151", "152", "153", "155", "156", "157", "158", "159",
    "180", "181", "182", "183", "185", "186", "187", "188", "189",
]

EMAIL_DOMAINS = ["example.com", "test.cn", "mail.test"]

USER_COUNT = 20


# ------------------------------------------------------------------ 待实现


def gen_name() -> str:
    """生成一个 2~4 个字的中文姓名。

    思路：
        1. 姓 = 从 SURNAMES 里随机取一个
        2. 名的字数 = 随机 1 或 2
        3. 从 GIVEN_NAMES 里随机取这么多个字，拼起来
        4. 返回 "姓 + 名"
    """
    raise NotImplementedError("gen_name 还没写")


def gen_phone() -> str:
    """生成一个 11 位手机号，例如 '13812345678'。

    思路：
        1. 前缀 = 从 PHONE_PREFIXES 里随机取一个（3 位）
        2. 后 8 位 = 0~99999999 的随机数，转成字符串并补足 8 位
        3. 拼接后返回
    """
    raise NotImplementedError("gen_phone 还没写")


def gen_email(prefix: str) -> str:
    """用传入的前缀生成一个全小写邮箱，例如 'user1@example.com'。

    思路：
        1. 随机取一个域名
        2. 用 f-string 拼成 "前缀@域名"
        3. 把结果转成小写再返回
    """
    raise NotImplementedError("gen_email 还没写")


def gen_user(index: int) -> dict:
    """生成一条用户数据，返回带四个键的字典。

    要求返回：
        {"id": index, "name": ..., "phone": ..., "email": ...}

    思路：
        1. 调 gen_name()、gen_phone()
        2. 邮箱前缀自己定个规则，比如 f"user{index}"
        3. 组装成字典返回，注意字典的键名要完全一致
    """
    raise NotImplementedError("gen_user 还没写")


def print_table(users: list[dict]) -> None:
    """把用户列表打印成对齐的表格。

    期望效果（列宽不必完全一致，能看出是表格就行）：
        ID    姓名    手机号          邮箱
        1     张伟    13812345678    user1@example.com

    思路：
        1. 先打印表头
        2. 循环 users，每行用 f-string 对齐输出
        提示：f"{值:<6}" 是左对齐占 6 个字符宽
    """
    raise NotImplementedError("print_table 还没写")


# ------------------------------------------------------------------ 自动校验
# 下面这个函数已经写好了，不需要修改。
# 它的作用相当于一个测试用例：把你生成的数据当作被测对象，逐条断言。


def verify(users: list[dict]) -> bool:
    results: list[tuple[str, bool, str]] = []

    results.append(("数据条数为 20", len(users) == USER_COUNT, f"实际 {len(users)} 条"))

    keys_ok = all(isinstance(u, dict) and {"id", "name", "phone", "email"} <= set(u) for u in users)
    results.append(("字段完整", keys_ok, "id/name/phone/email"))

    name_ok = all(isinstance(u.get("name"), str) and 2 <= len(u["name"]) <= 4 for u in users)
    results.append(("姓名 2-4 字", name_ok, ""))

    phone_pattern = re.compile(r"^1[3-9]\d{9}$")
    bad_phone = [u.get("phone") for u in users if not phone_pattern.match(str(u.get("phone", "")))]
    results.append(("手机号格式", not bad_phone, f"不合格: {bad_phone[:3]}" if bad_phone else ""))

    email_pattern = re.compile(r"^[a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,}$")
    bad_email = [
        u.get("email")
        for u in users
        if not (isinstance(u.get("email"), str)
                and email_pattern.match(u["email"])
                and u["email"] == u["email"].lower())
    ]
    results.append(("邮箱格式", not bad_email, f"不合格: {bad_email[:3]}" if bad_email else ""))

    phones = [u.get("phone") for u in users]
    results.append(("手机号不重复", len(set(phones)) == len(phones), f"{len(set(phones))}/{len(phones)} 个唯一"))

    print("\n" + "-" * 56)
    print("自动校验")
    print("-" * 56)
    for label, ok, detail in results:
        print(f"{'[PASS]' if ok else '[FAIL]':<8}{label:<12}{detail}")

    passed = sum(1 for _, ok, _ in results if ok)
    print("-" * 56)
    print(f"通过 {passed}/{len(results)}")
    return passed == len(results)


def main() -> int:
    try:
        users = [gen_user(i + 1) for i in range(USER_COUNT)]
        print_table(users)
    except NotImplementedError as exc:
        print("=" * 56)
        print("还有函数没实现：", exc)
        print("=" * 56)
        print("按这个顺序来，一个一个替换掉 NotImplementedError：")
        print("  1. gen_name()")
        print("  2. gen_phone()")
        print("  3. gen_email()")
        print("  4. gen_user()")
        print("  5. print_table()")
        print("\n每写完一个就保存运行一次，看报错信息往下走。")
        return 1

    if verify(users):
        print("\nDay 2 完成。收尾：")
        print('  git add . && git commit -m "day2: 注册测试数据生成器" && git push')
        return 0

    print("\n有项目没过，对照任务卡里的验收标准改一改。")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
