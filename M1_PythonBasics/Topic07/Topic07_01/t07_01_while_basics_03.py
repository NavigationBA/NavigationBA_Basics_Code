print("continue语句示例：")

i = 0
while i < 5:
    i = i + 1
    if i == 3:
        continue
    print("当前计数", i)
print("循环结束")

print("\n打印 1 到 10 之间的奇数：")

i = 0
while i < 10:
    i = i + 1
    if i % 2 == 0:
        continue
    print(i)

print("\n找出 1 到 50 之间 7 的倍数：")

i = 0
while i < 50:
    i = i + 1
    if i % 7 != 0:
        continue
    print(i)