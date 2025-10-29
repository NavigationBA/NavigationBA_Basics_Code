print("集合的增删元素")

set_new = {1, 2, 3}
set_new.add(4)
set_new.update([5, 6], (7, 8))
print(set_new)

set_new.remove(2) 
set_new.discard(10)
print(set_new)

removed_element = set_new.pop()
print("Removed element:", removed_element)
print(set_new)

set_new.clear()
print(set_new)

print("集合的常用函数")

set_num = {3, 1, 4, 1, 5, 9, 2, 6, 5}
print(set_num)
print(len(set_num))
print(max(set_num))
print(min(set_num))
print(sum(set_num))
print(sorted(set_num))

print("集合的运算")

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
print("Set A:", set_a)
print("Set B:", set_b)
print("Union:", set_a | set_b)
print("Intersection:", set_a & set_b)
print("Difference (A - B):", set_a - set_b)
print("Difference (B - A):", set_b - set_a)
print("Symmetric Difference:", set_a ^ set_b)