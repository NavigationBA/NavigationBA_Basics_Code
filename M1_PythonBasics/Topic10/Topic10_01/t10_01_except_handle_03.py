print("其他类型异常依然会导致程序崩溃")

try:
    list_a = [1, 2, 3, 4, 5, 0]
    for i in range(7):  # 注意这里，循环次数超过了列表长度
        print(list_a[i])
except ZeroDivisionError:
    print("除以零错误，无法进行除法运算")