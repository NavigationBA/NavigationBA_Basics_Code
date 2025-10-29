import time

# 记录开始时间
start_time = time.time()

# 执行一个程序
for i in range(1000000):
    pass

# 记录结束时间
end_time = time.time()

# 计算并打印程序运行时间
print(f"程序运行时间：{end_time - start_time} 秒")