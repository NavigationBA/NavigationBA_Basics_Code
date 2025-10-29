def calculate(a, b):

    def add(x, y):
        sum_result = x + y
        return sum_result

    def subtract(x, y):
        diff_result = x - y
        return diff_result

    sum_result = add(a, b)
    diff_result = subtract(a, b)

    return sum_result, diff_result

a = 10
b = 5
result = calculate(a, b)
print(f"{a}与{b}的和与差分别是:", result)

# print(add(3, 4))  # 这会报错，因为 add 函数是局部函数