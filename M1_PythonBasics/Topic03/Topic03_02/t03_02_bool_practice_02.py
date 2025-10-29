import random

x = random.uniform(-1, 1)
y = random.uniform(-1, 1)

is_inside_circle = x**2 + y**2 <= 1

print("随机点: (", round(x, 2), ",", round(y, 2), ")")
print("是否在单位圆内:", is_inside_circle)