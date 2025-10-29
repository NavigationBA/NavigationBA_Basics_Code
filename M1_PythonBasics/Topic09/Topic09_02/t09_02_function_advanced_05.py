print("使用global关键字访问全局变量：")

global_var = 20  # 这是一个全局变量

def my_function_v3():
    global global_var 
    print("函数内部访问全局变量:", global_var)

my_function_v3()
print("函数外部访问全局变量:", global_var)


print("\n使用global关键字修改全局变量：")

global_var = 20
def my_function_v4():
    global global_var 
    global_var = 30  # 修改全局变量
    print("函数内部修改后的全局变量:", global_var)

my_function_v4()
print("函数外部访问修改后的全局变量:", global_var)


print("\n不使用global关键字修改全局变量：")

global_var = 20
def my_function_v5():
    global_var = 30  # 这实际上是定义了一个新的局部变量
    print("函数内部的局部变量:", global_var)

my_function_v5()
print("函数外部访问全局变量:", global_var)