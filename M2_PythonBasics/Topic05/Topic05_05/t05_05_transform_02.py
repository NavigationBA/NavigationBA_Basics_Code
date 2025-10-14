print("转换为集合")

print(set("hello"))          
print(set([1, 2, 3]))        
print(set((1, 2, 3)))        
print(set({"a": 1, "b": 2})) 

print("使用集合来去重")
# 给list1去重
list1 = [1, 2, 2, 3, 4, 4, 5]
print(list(set(list1)))

# 找出在list2中但不在list3的元素
list2 = [1, 2, 2, 3, 4, 4, 5]
list3 = [2, 4]  
print(list(set(list2) - set(list3)))