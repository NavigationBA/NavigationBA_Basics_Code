try:
    # 请给x赋值一个整数
    x = 123.456
    print(x)
    if not isinstance(x, int):
        raise ValueError("您的赋值的不是整数！")
except ValueError as e:
    print(f"捕获到异常：{e}")