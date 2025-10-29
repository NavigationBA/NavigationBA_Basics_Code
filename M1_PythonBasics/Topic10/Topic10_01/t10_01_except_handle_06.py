list_a = [1, 2, 3, 4, 5, 0]

for i in range(7):
    try:
        print("\n当前循环索引值：", i)
        print(10 / list_a[i])
        if i == 2:
            print(x)  # 故意引发 NameError
        if i == 3:
            print("a" + 1)  # 故意引发 TypeError
    except ZeroDivisionError:
        print("除以零错误，无法进行除法运算")
    except IndexError:
        print("索引错误，访问了不存在的列表元素")
    except (NameError, TypeError):
        print("发生了名称错误或类型错误，请好好检查一下代码")
    else:
        print("本次循环没有发生任何异常")
    finally:
        print("本次循环结束")