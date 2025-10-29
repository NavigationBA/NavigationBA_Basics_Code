try:
    x = 10 / 0
except ArithmeticError as e:
    print(f"捕获到异常：{e}")