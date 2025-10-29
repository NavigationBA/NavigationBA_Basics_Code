# 打开文件
file = open("Topic11/Topic11_01/咏鹅.txt", "r")

# 逐行读取文件内容
line1 = file.readline()
line2 = file.readline()
print(line1, end='')
print(line2, end='')        

# 关闭文件
file.close()