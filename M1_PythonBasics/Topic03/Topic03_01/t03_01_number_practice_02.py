import math

r = float(input("请输入圆的半径："))

p = math.pi * r * 2
s = math.pi * r ** 2

print("该圆的周长是：", round(p, 2), ";该圆的面积是：", round(s, 2))