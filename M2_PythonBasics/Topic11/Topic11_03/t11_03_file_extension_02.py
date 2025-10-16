import json

# 定义一个列表套字典的结构
data = [
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

# 将 Python 对象转换为 JSON 字符串
print("转换为 JSON 字符串:")
json_data = json.dumps(data, indent=4, ensure_ascii=False)
print(json_data)
print(type(json_data))

# 将 JSON 字符串写入文件
with open("Topic11/Topic11_03/data1.json", "w") as file:
    file.write(json_data)
