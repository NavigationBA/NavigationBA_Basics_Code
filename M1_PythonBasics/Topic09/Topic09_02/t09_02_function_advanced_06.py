x = 10

def my_new_func_v1():
    global x  # 这里使用 global 关键字
    x = x + 5

my_new_func_v1()
print(x) 