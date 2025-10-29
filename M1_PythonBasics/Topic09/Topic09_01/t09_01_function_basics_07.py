print("函数返回值与打印输出的区别")

def add_v1(a, b):
    print(a + b)

def add_v2(a, b):
    return a + b

def add_v3(a, b):
    print(a + b)
    return a + b

# 调用 add_v1
result1 = add_v1(2, 3)
print(f"add_v1 的结果是 {result1}")

# 调用 add_v2
result2 = add_v2(2, 3)
print(f"add_v2 的结果是 {result2}")

# 调用 add_v3
result3 = add_v3(2, 3)
print(f"add_v3 的结果是 {result3}")