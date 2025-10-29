list_a = [1, 2, 3, 4, 5, 0]
for i in range(7):
    try:
        print(10 / list_a[i])
    except ZeroDivisionError as e:
        print(f"捕获到异常：{e}")
    except IndexError as e:
        print(f"捕获到异常：{e}")