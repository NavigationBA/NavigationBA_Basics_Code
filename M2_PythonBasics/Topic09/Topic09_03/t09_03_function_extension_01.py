print("指定参数的类型")

# 定义乘积函数，添加类型注解
def multiply(a: (int | float), b: (int | float)) -> (int | float):
    return a * b

# 调用函数，计算两个整数的乘积
print(multiply(3, 5))

# 定义重复字符串函数，添加类型注解
def repeat_string(s: str, n: int) -> str:
    return s * n

# 调用函数，重复字符串
print(repeat_string("*", 10))