print("列表简单赋值的问题")

list_a = [1, 2, 3]
list_b = list_a
list_b.append(4)
print(list_a)
print(list_b)

print("列表的浅拷贝")

list_a_new = [1, 2, 3]
list_b_new = list_a_new.copy()
list_b_new.append(4)
print(list_a_new)
print(list_b_new)

print("列表的浅拷贝的问题")
list_c = [[1, 2], [3, 4]]
list_d = list_c.copy()
list_d[0].append(5)
print(list_c)
print(list_d)

print("列表的深拷贝")

import copy

list_c_new = [[1, 2], [3, 4]]
list_d_new = copy.deepcopy(list_c_new)
list_d_new[0].append(5)
print(list_c_new)
print(list_d_new)