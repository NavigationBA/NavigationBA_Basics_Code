import math
import random

axis_max = 100
axis_min = -100

x1 = random.uniform(axis_min, axis_max)
y1 = random.uniform(axis_min, axis_max)
x2 = random.uniform(axis_min, axis_max)
y2 = random.uniform(axis_min, axis_max)

s = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

print("第一个点的坐标：(", round(x1, 2), ",", round(y1, 2), ")")
print("第二个点的坐标：(", round(x2, 2), ",", round(y2, 2), ")")
print("两点之间的距离：", round(s, 2))