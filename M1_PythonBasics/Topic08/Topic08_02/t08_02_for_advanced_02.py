print("for循环与continue语句的结合使用")
names = ['张三', '李四', '王五']
for name in names:
    if name == '李四':
        continue
    print(name)

print("\nfor循环与continue和else语句的结合使用")
names = ['张三', '李四', '王五']
for name in names:
    if name == '李四':
        continue
    print(name)
else:
    print("循环正常结束")