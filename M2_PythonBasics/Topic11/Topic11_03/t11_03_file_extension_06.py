import json
with open("Topic11/Topic11_03/example.txt", "r") as file:
    content = file.read()
data = json.loads(content)
print(data)