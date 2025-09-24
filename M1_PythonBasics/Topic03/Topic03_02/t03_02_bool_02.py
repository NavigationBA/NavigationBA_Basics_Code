print("比较运算符示例：")
a = 5
b = 3

print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)

print("逻辑运算符示例：")
print(True and True)
print(True and False)
print(False and False)
print(True or True)
print(True or False)
print(False or False)
print(not False)
print(not True)

print("逻辑运算与比较运算的顺序：")
print(3 + 2 > 4)
print(3 + 2 > 4 and 10 / 2 == 5)
print(not 3 > 2 or 4 < 1)
print(True or False and False)
print((3 + 2 > 4 or 1 > 2) and not (2 * 2 < 5))