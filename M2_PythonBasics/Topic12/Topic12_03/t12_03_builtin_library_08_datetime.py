# 比较两个datetime对象的大小
from datetime import datetime

dt1 = datetime(2025, 10, 17, 15, 0, 0)
dt2 = datetime(2025, 10, 18, 15, 0, 0)

if dt1 < dt2:
    print("dt1早于dt2")
elif dt1 > dt2:
    print("dt1晚于dt2")
else:
    print("dt1和dt2相等")