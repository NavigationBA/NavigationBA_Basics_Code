print("使用元组进行多变量赋值")

x, y, z = 1, 2, 3

print(x)
print(y)
print(z)

print("将多个变量赋值给一个元组变量")

combined_numbers = x, y, z = 1, 2, 3
print(combined_numbers)
print(type(combined_numbers))
print(x)
print(y)
print(z)

print("交换变量的值")

a = 5
b = 10
a, b = b, a
print(a)
print(b)

print("交换变量值的传统方法")

a = 5
b = 10
temp = a
a = b
b = temp
print(a)
print(b)