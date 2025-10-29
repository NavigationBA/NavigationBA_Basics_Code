print("处理多种类型的异常")
list_a = [1, 2, 3, 4, 5, 0]
for i in range(7):
    try:
        print(10 / list_a[i])
    except ZeroDivisionError:
        print("除以零错误，无法进行除法运算")
    except IndexError:
        print("索引错误，访问了不存在的列表元素")

print("\n多种异常使用同种处理方式")

list_a = [1, 2, 3, 4, 5, 0]
for i in range(7):
    try:
        print(10 / list_a[i])
    except (ZeroDivisionError, IndexError):
        print("程序出现除零错误或索引错误，请好好检查一下代码")