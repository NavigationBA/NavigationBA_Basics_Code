# 定义函数
def show_stars(n):
    if n > 30:
        print("太多了，打印不完！")
        return
    for i in range(1, n + 1):
        print('*' * i)
    
# 调用函数
show_stars(5)
show_stars(100)

