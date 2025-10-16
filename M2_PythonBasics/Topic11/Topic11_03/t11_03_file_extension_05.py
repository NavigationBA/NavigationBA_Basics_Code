import csv

data_list = [
    {
        "name": "Charlie",
        "age": 28,
        "is_student": False,
        "courses": ["Physics", "Chemistry"],
        "address": {
            "street": "789 C St",
            "city": "City C"
        }
    },
    {
        "name": "Diana",
        "age": 22,
        "is_student": True,
        "courses": ["Biology", "Geography"],
        "address": {
            "street": "101 D St",
            "city": "City D"
        }
    }
]

with open("Topic11/Topic11_03/student1.csv", "w", newline="") as file:
    
    # 创建 CSV 写入对象
    writer = csv.writer(file)
    
    # 写入表头
    header = ["name", "age", "is_student", "courses", "address_street", "address_city"]
    writer.writerow(header)

    # 写入数据
    for student in data_list:
        dt_list = [
            student["name"],
            student["age"],
            student["is_student"],
            ";".join(student["courses"]),
            student["address"]["street"],
            student["address"]["city"]
        ]
        writer.writerow(dt_list)