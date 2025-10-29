# 获取当前的日期和时间
from datetime import datetime

current_datetime = datetime.now()
print(current_datetime)
print(type(current_datetime))

# 创建指定日期和时间的datetime对象
dt1 = datetime(2025, 12, 25, 10, 30, 0)  # 具体到时分秒
print(dt1)
print(type(dt1))

dt2 = datetime(2023, 1, 1)  # 只指定到年月日，时分秒默认为0
print(dt2)
print(type(dt2))