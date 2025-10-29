print("集合推导式")

numbers = [2, 5, 7, 9, 11]
number_squares_set = {x**2 for x in numbers if x % 2 == 0}
print(number_squares_set)