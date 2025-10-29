# 打开文件
file = open("Topic11/Topic11_01/咏鹅.txt", "r")

# 读取所有行
lines = file.readlines()
print(lines)
print(type(lines))

content = ''.join(lines)
print(content)
print(type(content))

# 关闭文件
file.close()