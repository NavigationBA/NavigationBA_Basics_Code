# 打开文件
file = open("Topic11/Topic11_01/咏鹅3.txt", "w")
lines = ["咏鹅\n", "唐·骆宾王\n", "鹅，鹅，鹅，\n", "曲项向天歌。\n", "白毛浮绿水，\n", "红掌拨清波。\n"]

# 逐行写入文件内容
file.writelines(lines)

# 关闭文件
file.close()