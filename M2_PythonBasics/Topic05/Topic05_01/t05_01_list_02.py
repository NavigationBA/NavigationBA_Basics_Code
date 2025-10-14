print("列表的拼接与重复")

list1 = [1, 2, 3]
list2 = ["a", "b", "c"]
print(list1 + list2)
print(list1 * 2)

print("列表的成分判断")

list3 = [1, 2, 3, "a", "b", "c"]
print(2 in list3)
print("d" not in list3)

print("列表的内置函数")

list_num = [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(len(list_num))
print(max(list_num))
print(min(list_num))
print(sum(list_num))
print(sorted(list_num))
