print("捕获异常后程序便不再运行try块中的后续代码")

try:
    list_a = [1, 2, 3, 4, 5, 0]
    for i in range(7):  # 注意这里，循环次数超过了列表长度
        print(10 / list_a[i])
except ZeroDivisionError:
    print("除以零错误，无法进行除法运算")

print("\n推荐的改进写法：")

list_a = [1, 2, 3, 4, 5, 0]
for i in range(7):  # 注意这里，循环次数超过了列表长度
    try:
        print(10 / list_a[i])
    except ZeroDivisionError:
        print("除以零错误，无法进行除法运算")