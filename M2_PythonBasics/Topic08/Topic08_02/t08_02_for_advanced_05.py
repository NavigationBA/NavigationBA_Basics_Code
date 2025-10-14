print("字典推导式")
numbers = [2, 5, 7, 9, 11]
number_squares_dict = {x: x**2 for x in numbers}
print(number_squares_dict)

print("另一个字典推导式的例子")
names = ['张三', '李四', '王五']
ages = [18, 20, 22]
name_age_dict = {names[i]: ages[i] for i in range(len(names))}
print(name_age_dict)
