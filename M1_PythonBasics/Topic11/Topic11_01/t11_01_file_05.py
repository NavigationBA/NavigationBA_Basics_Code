# 打开文件
file = open("Topic11/Topic11_01/咏鹅1.txt", "w")

content = '''
咏鹅
唐·骆宾王
鹅，鹅，鹅，
曲项向天歌。
白毛浮绿水，
红掌拨清波。
'''.strip()

# 写入文件内容
file.write(content)

# 关闭文件
file.close()