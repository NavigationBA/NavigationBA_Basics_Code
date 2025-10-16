print("多值元组参数")

def sum_numbers(*numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum_numbers(1, 2, 3))
print(sum_numbers(10, 20, 30, 40, 50))
print(sum_numbers(5, 15))

