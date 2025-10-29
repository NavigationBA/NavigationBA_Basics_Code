print("函数返回多个值")

# 定义函数，带有两个参数 a 和 b，返回它们的和与差
def calculate_v1(a, b):
    summation = a + b
    difference = a - b
    return summation, difference

# 调用函数，并接收返回值
sum_result, diff_result = calculate_v1(10, 5)
print(f"10 与 5 的和是 {sum_result}，差是 {diff_result}。")

print("\n多个返回值本质上是一个元组")

# 定义函数，带有两个参数 a 和 b，返回它们的和与差
def calculate_v2(a, b):
    summation = a + b
    difference = a - b
    return summation, difference

# 调用函数，并打印返回值的类型
results = calculate_v2(10, 5)
print(results)  
print(type(results))

print("函数返回的第一个值是：", results[0])
print("函数返回的第二个值是：", results[1])