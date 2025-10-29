print("for循环遍历字典：")

student = {'name': '张三', 'age': 20, 'gender': '男'}
for i in student:
    print(i)

print("\nfor循环遍历字典的键和值：")
student = {'name': '张三', 'age': 20, 'gender': '男'}
for key, value in student.items():
    print(key, value)

print("\n回忆一下字典的items()的用法：")
student = {'name': '张三', 'age': 20, 'gender': '男'}
print(student.items())