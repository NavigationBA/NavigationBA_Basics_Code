print("列表推导式")

numbers = [2, 5, 7, 9, 11]
numbers_squares = [x**2 for x in numbers]
print(numbers_squares)

print("\n同等效果的传统for循环写法")

numbers = [2, 5, 7, 9, 11]
numbers_squares = []
for x in numbers:
    numbers_squares.append(x**2)
print(numbers_squares)

print("\n带有条件判断的列表推导式")

numbers = [2, 5, 7, 9, 11]
number_squares = [x**2 for x in numbers if x % 2 == 0]
print(number_squares)

print("\n同等效果的传统for循环写法")

numbers = [2, 5, 7, 9, 11]
number_squares = []
for x in numbers:
    if x % 2 == 0:
        number_squares.append(x**2)
print(number_squares)