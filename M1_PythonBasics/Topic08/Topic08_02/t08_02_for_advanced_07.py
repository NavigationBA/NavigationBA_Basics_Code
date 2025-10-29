print("enumerate()函数示例")

names = ['张三', '李四', '王五']
for index, name in enumerate(names):
    print(f"索引: {index}, 名字: {name}")

print("\nenumerate()函数的start参数示例")
names = ['张三', '李四', '王五']
for index, name in enumerate(names, start=1):
    print(f"索引: {index}, 名字: {name}")