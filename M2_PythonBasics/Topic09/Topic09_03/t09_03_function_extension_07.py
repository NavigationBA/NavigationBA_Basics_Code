print("不可变参数类型")

def modify_immutable(x):
    x = x + 10
    print("函数内部修改后的值:", x)

x = 5
modify_immutable(x)
print("函数外部的值:", x)


print("\n可变参数类型")

def modify_mutable(lst):
    lst.append(4)
    print("函数内部修改后的列表:", lst)

my_list = [1, 2, 3]
modify_mutable(my_list)
print("函数外部的列表:", my_list)