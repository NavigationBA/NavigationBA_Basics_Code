# 打开文件
file = open("Topic11/Topic11_01/咏鹅.txt", "r")

# 读取文件内容
content = file.read()
print(content)
print(type(content)) 

# 关闭文件
file.close()