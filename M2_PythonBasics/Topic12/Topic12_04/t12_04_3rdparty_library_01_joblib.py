# 使用传统的for循环计算平方和：顺序执行

data = [1, 2, 3, 4, 5]

def compute_square(x):
    return x * x

data_squared = []

for num in data:
    result = compute_square(num)
    data_squared.append(result)

total = sum(data_squared)
print("平方和：", total)