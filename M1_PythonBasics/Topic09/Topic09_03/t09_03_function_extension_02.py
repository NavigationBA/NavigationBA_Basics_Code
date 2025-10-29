def outer_function_v1():

    outer_var = 10  # 外层函数的局部变量
    print("外层函数变量原始值:", outer_var)

    def inner_function_v1():
        nonlocal outer_var  # 声明 outer_var 是外层函数的变量
        outer_var = 20  # 修改外层函数的变量
        print("内层函数访问并修改的外层变量:", outer_var)

    inner_function_v1()
    print("外层函数再次访问外层变量:", outer_var)

outer_function_v1()