global_var = 100
print("全局变量初始值:", global_var)

def outer_function_v2():

    def inner_function_v2():
        global global_var  # 声明 global_var 是全局变量
        global_var = 200
        print("内层函数访问并修改后的全局变量:", global_var)

    inner_function_v2()
    print("外层函数访问全局变量:", global_var)

outer_function_v2()
print("函数外部访问全局变量:", global_var)