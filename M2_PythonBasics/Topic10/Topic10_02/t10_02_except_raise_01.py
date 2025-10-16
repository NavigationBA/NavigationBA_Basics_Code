# 请给x赋值一个整数
x = 123.456
print(x)
if not isinstance(x, int):
    raise ValueError("您的输入的赋值的不是整数！")