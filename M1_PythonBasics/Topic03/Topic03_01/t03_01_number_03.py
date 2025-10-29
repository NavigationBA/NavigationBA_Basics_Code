print("Python内置运算函数")
print(abs(-5))
print(round(3.14159, 2))
print(pow(2, 3))
print(divmod(7, 3))
print(max(1, 5, 3))
print(min(1, 5, 3))
print(sum([1,2,3]))

print("round函数注意事项")
print(round(2.5))   # 2  （2是偶数，不进位）
print(round(3.5))   # 4  （3是奇数，进位变4）
print(round(1.25, 1))  # 1.2 （2是偶数，不进位）
print(round(1.35, 1))  # 1.4 （3是奇数，进位）
