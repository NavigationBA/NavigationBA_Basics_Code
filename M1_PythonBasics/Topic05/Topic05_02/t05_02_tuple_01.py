print("元组的定义")

fruits = ("apple", "banana", "cherry")
print(fruits)
print(type(fruits))

print("空元组的定义")

empty_tuple1 = ()
empty_tuple2 = tuple()
print(empty_tuple1)
print(empty_tuple2)
print(type(empty_tuple1))
print(type(empty_tuple2))

print("单元素元组的定义")

single_element_tuple1 = (42,)
single_element_tuple2 = (42)
print(single_element_tuple1)
print(single_element_tuple2)
print(type(single_element_tuple1))
print(type(single_element_tuple2))

print("元组的不可变性")

fruits = ("apple", "banana", "cherry")
# fruits[0] = "orange"  # 这行代码会引发 TypeError 错误
fruits = ("orange", "banana", "cherry")  # 重新定义元组
print(fruits)