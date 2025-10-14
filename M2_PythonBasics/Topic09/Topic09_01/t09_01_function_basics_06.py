print("return 语句的不同用法")

# 定义三个函数，分别展示不同的返回值情况
def test_function_v1():
    print("Hello World!")

def test_function_v2():
    print("Hello World!")
    return

def test_function_v3():
    print("Hello World!")
    return 8888
    print("Hello Python!")

# 调用函数，并接收返回值
result1 = test_function_v1()
print(f"test_function_v1 的返回值是 {result1}")

result2 = test_function_v2()
print(f"test_function_v2 的返回值是 {result2}")

result3 = test_function_v3()
print(f"test_function_v3 的返回值是 {result3}")