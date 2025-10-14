print("while 循环基础语法示例：")
i = 0
while i < 5:
    print("当前计数", i)
    i = i + 1  
print("循环结束")


print("\n打印小星星：")
i = 1
while i < 10:
    print("*" * i)
    i = i + 1

print("\n计算 1 到 100 的和：")
sum = 0
i = 1
while i <= 100:
    sum = sum + i
    i = i + 1
print("1 到 100 的和为:", sum)