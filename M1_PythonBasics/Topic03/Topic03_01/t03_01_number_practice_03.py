import math
import random

x1 = random.uniform(-100, 100)
y1 = random.uniform(-100, 100)
x2 = random.uniform(-100, 100)
y2 = random.uniform(-100, 100)

s = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print("第一个点的坐标：(", round(x1, 2), ",", round(y1, 2), ")")
print("第二个点的坐标：(", round(x2, 2), ",", round(y2, 2), ")")
print("两点之间的距离：", round(s, 2))