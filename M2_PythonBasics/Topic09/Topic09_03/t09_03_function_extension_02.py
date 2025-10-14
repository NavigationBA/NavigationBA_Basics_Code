print("指定参数类型并不会限制传入的参数类型")

# 定义乘积函数，添加类型注解
def multiply(a: (int | float), b: (int | float)) -> (int | float):
    return a * b

# 调用函数，传入错误类型的参数
print(multiply("*", 5))