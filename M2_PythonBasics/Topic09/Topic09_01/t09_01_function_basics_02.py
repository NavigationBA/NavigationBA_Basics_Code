print("函数的参数")

# 定义函数，带有一个参数 name
def greet(name):
    print(f"你好，{name}！")

# 调用函数，传入参数
greet(name="小明")
greet(name="小红")

print("\n省略参数名调用函数")
greet("小明")
greet("小红")
