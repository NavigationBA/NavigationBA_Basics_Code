students = {
    "student1": {"name": "Alice", "age": 18, "city": "New York"},
    "student2": {"name": "Bob", "age": 19, "city": "Los Angeles"},
    "student3": {"name": "Charlie", "age": 20, "city": "Chicago"}
}
# (1) 访问并打印第2个学生的姓名
print(students["student2"]["name"])
# (2) 修改第1个学生的年龄为20岁
students["student1"]["age"] = 20
print(students["student1"])
# (3) 删除第3个学生的城市信息
students["student3"].pop("city")
print(students["student3"])