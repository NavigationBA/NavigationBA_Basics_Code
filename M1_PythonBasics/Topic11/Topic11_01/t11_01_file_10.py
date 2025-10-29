# 打开文件
file = open("Topic11/Topic11_01/咏鹅3.txt", "a")
lines = ["\n骆宾王在完成《咏鹅》这首诗时，只有七岁。\n", "这首诗是骆宾王在童年时期创作的。\n"]

# 逐行追加文件内容
file.writelines(lines)

# 关闭文件
file.close()