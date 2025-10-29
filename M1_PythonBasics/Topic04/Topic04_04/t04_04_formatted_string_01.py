print("f-string基本介绍")

name = "李四"
age = 25
output = f"{name}今年{age}岁"
print(output)
print(f"{name}名字里有{len(name)}个字，今年{age}岁，明年{age+1}岁")

item = "apple"
price = 5.5
weight = 6
print(f"{item.title()}单价为{price}元一斤，买了{weight}斤，一共{price*weight}元")

print("f-string的格式化")

a = 123.456789
print(f"我定义了一个数字a = {a:.4f}")
print(f"我定义了一个数字a = {a:.3%}")
print(f"我定义了一个数字a = {a:.4g}")
print(f"我定义了一个数字a = {a:.2g}")

s = "cat"
print(f"我定义了一个字符串：{s:<10}")
print(f"我定义了一个字符串：{s:*<10}")
print(f"我定义了一个字符串：{s:^10}")
print(f"我定义了一个字符串：{s:*^10}")
print(f"我定义了一个字符串：{s:>10}")
print(f"我定义了一个字符串：{s:*>10}")
