print("字典的常用方法之获取键值对")

dict2 = {"name": "Bob", "age": 25, "city": "Los Angeles"}

dict2_keys = dict2.keys()
dict2_values = dict2.values()
dict2_items = dict2.items()

print(dict2_keys)
print(dict2_values)
print(dict2_items)

print(type(dict2_keys))
print(type(dict2_values))
print(type(dict2_items))

dict2_keys_list = list(dict2_keys)
dict2_values_list = list(dict2_values)
dict2_items_list = list(dict2_items)

print(dict2_keys_list)
print(dict2_values_list)
print(dict2_items_list)

print(type(dict2_keys_list))
print(type(dict2_values_list))
print(type(dict2_items_list))

print(dict2_items_list[0])
print(type(dict2_items_list[0]))


print("字典常用方法之增删改查")

dict3 = {"name": "Charlie", "age": 28, "city": "Chicago"}

print(dict3)
print(dict3.get("age"))
print(dict3.get("gender", "Not Specified"))

removed_value1 = dict3.pop("city")
removed_value2 = dict3.pop("country", "Not Specified")

print(removed_value1)
print(removed_value2)
print(dict3)

dict3.update({"age": 29, "country": "USA"})
dict3.update({"name": "Charlie Smith"})
print(dict3)

dict3.clear()
print(dict3)

print("更新键值对的两种方法")

dict4 = {"name": "David", "age": 35, "city": "San Francisco"}
print(dict4)
dict4["age"] = 36
print(dict4)
dict4.update({"name": "David Johnson"})
print(dict4)