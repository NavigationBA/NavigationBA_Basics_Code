print("while语句中的else语句示例（正常结束）：")

i = 0
while i < 5:
    print("当前计数", i)
    i = i + 1
else:
    print("循环正常结束")
print("循环结束")

print("\nwhile语句中的else语句示例（break中断）：")

i = 0
while i < 5:
    print("当前计数", i)
    if i == 3:
        break
    i = i + 1
else:
    print("循环正常结束")
print("循环结束")

print("\n找从 1 加到 200，是否会超过 10000 呢")

sum = 0
i = 0
while i < 200:
    i = i + 1
    sum = sum + i
    if sum > 10000:
        print("和超过10000了")
        break
else:
    print("和没有超过10000")

print("最后的计数是:", i)
print("最后的和是:", sum)

print("\n1-100 中，13 的倍数有没有超过 8 个")

i = 0
count = 0
while i < 100:
    i = i + 1
    if i % 13 == 0:
        count = count + 1
    if count > 8:
        print("13的倍数超过8个了")
        break
else:
    print("13的倍数没有超过8个")

print("最后的计数是:", i)
print("1-100中，13的倍数一共有:", count)