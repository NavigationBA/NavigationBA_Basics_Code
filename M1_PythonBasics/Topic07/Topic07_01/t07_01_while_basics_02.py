print("break语句示例：")
 
i = 0
while i < 5:
    print("当前计数", i)
    if i == 3:
        break
    i = i + 1
print("循环结束")

print("\nbreak与无限循环结合使用：")

i = 0
while True:
    print("当前计数", i)
    i = i + 1
    if i == 3:
        break
print("循环结束")

print("\n找出前10个7的倍数：")

i = 0
count = 0
while True:
    i = i + 1
    if i % 7 == 0:
        print(i)
        count = count + 1
    if count == 10:
        break

print("\n从1开始加，加到和超过10000结束：")

sum = 0
i = 0
while True:
    i = i + 1
    sum = sum + i
    if sum > 10000:
        break
print("最后的计数是:", i)
print("最后的和是:", sum)