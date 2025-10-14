print("列表的嵌套")

nested_list = [[1, 2, 3], ["a", "b", "c"], [True, False]]
print(nested_list)
print(nested_list[0])
print(nested_list[1][2])


table = [
    ["姓名", "语文", "数学", "英语"],
    ["张三", 90, 85, 88],
    ["李四", 92, 80, 86],
    ["王五", 85, 87, 90]
] 

print(table)
print(table[0])        # 第0个子列表 - 第0行
print(table[1][0])     # 第1个子列表的第0个元素 - 第1行的第0列
print(table[2][2])     # 第2个子列表的第2个元素 - 第2行的第2列
print(table[1][1:])    # 第1个子列表的第1个元素到最后一个元素 - 第1行的第1列到最后1列