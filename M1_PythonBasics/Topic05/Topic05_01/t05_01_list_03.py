print("列表常用方法-增加类")

list_new1 = [1, 2, 3]
list_new1.append(4)
list_new1.insert(0, 0)
list_new1.extend([5, 6, 7])
print(list_new1)

print("列表常用方法-删除类")

list_new2 = [0, 1, 2, 3, 4, 5, 6, 7]
list_new2.remove(3)
list_new2.pop()
list_new2.pop(0)
print(list_new2)

list_new3 = [0, 1, 2, 3, 4, 5, 6, 7]
list_new3.clear()
print(list_new3)

print("列表常用方法-查找类")

list_new4 = ["a", "b", "c", "d", "c", "b", "a"]
print(list_new4.index("c"))
print(list_new4.index("c", 4))
print(list_new4.count("b"))

print("列表常用方法-排序类")

list_new5 = [3, 1, 4, 1, 5, 9, 2, 6, 5]
list_new5.sort()
print(list_new5)
list_new5.sort(reverse=True)
print(list_new5)
list_new5.reverse()
print(list_new5)

print("重要：列表的返回值")

list_a = [3, 1, 4, 1, 5, 9, 2, 6, 5]
list_b = list_a.sort()
print(list_a)
print(list_b)