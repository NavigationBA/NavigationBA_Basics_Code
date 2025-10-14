print("while循环嵌套示例：")

i = 0
while i < 3:
    print("外层循环计数", i)
    j = 0
    while j < 2:
        print("    内层循环计数", j)
        j = j + 1
    i = i + 1
print("循环结束")

print("\nwhile循环嵌套中的break示例（只中断内层循环）：")

i = 0
while i < 3:
    print("外层循环计数", i)
    j = 0
    while j < 5:
        print("    内层循环计数", j)
        if j == 2:
            break
        j = j + 1
    i = i + 1
print("循环结束")

print("\nwhile循环嵌套中的break示例（中断内层循环与外层循环）：")

i = 0
while i < 3:
    print("外层循环计数", i)
    j = 0
    while j < 5:
        print("    内层循环计数", j)
        if j == 2:
            break
        j = j + 1
    if i == 1:
        break
    i = i + 1
print("循环结束")
