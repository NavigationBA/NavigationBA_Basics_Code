print("列表的定义")

fruits = ["apple", "banana", "cherry"]
print(fruits)
print(type(fruits))

print("空列表的定义")

empty_list1 = []
empty_list2 = list()
print(empty_list1)
print(empty_list2)
print(type(empty_list1))
print(type(empty_list2))

print("列表转换为布尔值")

print(bool(fruits))
print(bool(empty_list1))
print(bool(empty_list2))

print("列表的元素")

a = 10
mixed_list = [a, 1, "apple", 3.14, True, None, [1, 2, 3], (4, 5)]
print(mixed_list)

print("列表的索引和切片")

name = ["张三", "李四", "王五", "赵六", "牛七", "马八", "陈九"]
print(name[0]) 
print(name[-1])
print(name[1:4])
print(name[::2])
print(name[::-1])

print("使用索引对列表修改和删除")

name1 = ["张三", "李四", "王五", "赵六", "牛七", "马八", "陈九"]
# 修改
name1[0] = "张三丰"
# 删除
del name1[-1]
print(name1)

print("使用切片对列表修改和删除")

name2 = ["张三", "李四", "王五", "赵六", "牛七", "马八", "陈九"]
# 批量修改
name2[0:4] = ["张三丰", "李四丰", "王五丰", "赵六丰"]
# 批量删除
del name2[4:]
print(name2)