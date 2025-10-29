import time

local_time = time.localtime()
print(local_time)
print(type(local_time))
print(time.strftime("%Y-%m-%d %H:%M:%S", local_time))

gmt_time = time.gmtime()
print(gmt_time)
print(type(gmt_time))
print(time.strftime("%Y-%m-%d %H:%M:%S", gmt_time))