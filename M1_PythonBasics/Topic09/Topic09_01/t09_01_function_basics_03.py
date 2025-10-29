print("多参数的函数")

# 定义函数，带有两个参数 a 和 b
def add_numbers(a, b):
    summation = a + b
    print(f"{a} 与 {b} 的和是 {summation}。")

# 调用函数，传入两个参数
add_numbers(a=3, b=5)
add_numbers(a=10, b=20)

print("\n省略参数名调用函数")
add_numbers(3, 5)
add_numbers(10, 20)

print("\n打乱参数顺序调用函数")
add_numbers(b=5, a=3)  # 使用参数名，可以打乱顺序
add_numbers(10, 20)    # 不使用参数名，必须按顺序

print("\n混用参数名和省略参数名调用函数")
add_numbers(3, b=5)     # 混用，必须先传入不使用参数名的参数
# add_numbers(b=5, 3)     # 错误，必须先传入不使用参数名的参数