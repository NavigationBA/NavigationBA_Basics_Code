global_var = 100
print("全局变量初始值:", global_var)

def outer_function_v3():
    
    global global_var  # 声明 global_var 是全局变量
    global_var = 200
    print("外层函数修改后的全局变量:", global_var)

    def inner_function_v3():
        global global_var  # 声明 global_var 是全局变量
        global_var = 300
        print("内层函数修改后的全局变量:", global_var)

    inner_function_v3()
    print("外层函数再次访问全局变量:", global_var)

outer_function_v3()
print("函数外部访问全局变量:", global_var)