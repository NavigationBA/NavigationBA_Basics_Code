print("for循环与break和else语句的结合使用(break中断)")

names = ['张三', '李四', '王五']
for name in names:
    if name == '李四':
        break
    print(name)
else:
    print("循环正常结束")

print("\nfor循环与break和else语句的结合使用(正常结束)")

names = ['张三', '李四', '王五']
for name in names:
    if name == '赵六':
        break
    print(name)
else:
    print("循环正常结束")