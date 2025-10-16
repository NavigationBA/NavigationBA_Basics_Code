# 打开文件
file = open("Topic11/Topic11_01/咏鹅1.txt", "w")

# 写入新的内容
content = "骆宾王在完成《咏鹅》这首诗时，只有七岁。"
file.write(content)

# 关闭文件
file.close()