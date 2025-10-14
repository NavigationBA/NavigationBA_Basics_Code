print("string.format()基本用法")

name = "李四"
age = 25
output = "{}今年{}岁".format(name, age)
print(output)

school = "墨尔本大学"
output_new = "{0}今年{1}岁，{0}所在学校是{2}".format(name, age, school)
print(output_new)

s = "商品名：{}，单价：{}，数量：{}"

print(s.format("苹果", 5.5, 2))
print(s.format("香蕉", 7, 3))

print("string.format()的格式化输出")

a = 123.456789
print("我定义了一个数字a = {:.4f}".format(a))
print("我定义了一个数字a = {:.3%}".format(a))
print("我定义了一个数字a = {:.4g}".format(a))
print("我定义了一个数字a = {:.2g}".format(a))

s = "cat"
print("我定义了一个字符串：{:<10}".format(s))
print("我定义了一个字符串：{:*<10}".format(s))
print("我定义了一个字符串：{:^10}".format(s))
print("我定义了一个字符串：{:*^10}".format(s))
print("我定义了一个字符串：{:>10}".format(s))
print("我定义了一个字符串：{:*>10}".format(s))


