print("处理特定类型的异常")

try:
    list_a = [1, 2, 3, 4, 5, 0]
    for i in range(len(list_a)):
        print(10 / list_a[i])
except ZeroDivisionError:
    print("除以零错误，无法进行除法运算")



