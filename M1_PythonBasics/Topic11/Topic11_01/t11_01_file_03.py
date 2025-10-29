# 打开文件
file = open("Topic11/Topic11_01/咏鹅.txt", "r")

# 逐行读取文件内容
while True:
    line = file.readline()
    if not line:
        break
    print(line, end='')

# 关闭文件
file.close()