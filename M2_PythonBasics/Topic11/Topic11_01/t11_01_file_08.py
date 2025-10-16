# 打开文件
file = open("Topic11/Topic11_01/咏鹅2.txt", "a")

# 追加新的内容
content = "\n骆宾王在完成《咏鹅》这首诗时，只有七岁。"
file.write(content)

# 关闭文件
file.close()