print("访问局部变量")

def my_function_v1():
    local_var = 10  # 这是一个局部变量
    print("函数内部的局部变量:", local_var)

print("函数外部访问局部变量:")
# print(local_var)  # 这会报错，因为 local_var 是局部变量

print("\n访问全局变量")

global_var = 20  # 这是一个全局变量

def my_function_v2():
    print("函数内部访问全局变量:", global_var)

my_function_v2()
print("函数外部访问全局变量:", global_var)