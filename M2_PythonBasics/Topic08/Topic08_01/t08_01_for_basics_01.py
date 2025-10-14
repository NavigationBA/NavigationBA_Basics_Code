print("for循环遍历列表：")

names = ['张三', '李四', '王五']
for i in names:
    print(i)

print("\nfor循环遍历列表并不会修改列表中的元素：")
names = ['张三', '李四', '王五']
for i in names:
    i += '同学'
    print(i)
print("遍历结束")
print(names)

print("\nfor循环的临时变量名是可变的：")
names = ['张三', '李四', '王五']
for name in names:
    print(name)