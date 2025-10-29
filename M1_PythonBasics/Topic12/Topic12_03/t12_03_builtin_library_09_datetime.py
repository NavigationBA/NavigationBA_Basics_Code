from datetime import datetime, timedelta

# datetime对象的加减运算
dt = datetime(2025, 10, 17, 15, 0, 0)
print("原始日期时间：", dt)

# 加5天
dt1 = dt + timedelta(days=5)
print("加5天后的日期时间：", dt1)

# 减3小时
dt2 = dt - timedelta(hours=3)
print("减3小时后的日期时间：", dt2)

# 加2天10分钟
dt3 = dt + timedelta(days=2, minutes=10)
print("加2天10分钟后的日期时间：", dt3)

# timedelta对象的加减运算
td1 = timedelta(days=5, hours=3)
td2 = timedelta(days=2, hours=1)

# 加法运算
td3 = td1 + td2
print("加法运算结果：", td3)

# 减法运算
td4 = td1 - td2
print("减法运算结果：", td4)

# timedelta对象之间的比较运算
if td1 > td2:
    print("td1大于td2")
elif td1 < td2:
    print("td1小于td2")
else:
    print("td1和td2相等")