import json

# 读取 JSON 文件
with open("Topic11/Topic11_03/data.json", "r") as file:
    content = file.read()

# 读取文件内容
print("读取的文件内容:")
print(content)
print(type(content))

# 将 JSON 字符串转换为 Python 对象
print("\n转换为 Python 对象:")
data = json.loads(content)
print(data)
print(type(data))  
print(type(data[0])) 
print(data[0]["name"])