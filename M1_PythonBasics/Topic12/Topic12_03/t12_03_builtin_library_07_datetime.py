from datetime import datetime

# 获取当前日期时间对象
current_datetime = datetime.now()

# 将日期时间对象格式化为字符串
formatted_datetime1 = current_datetime.strftime("%Y-%m-%d %H:%M:%S")  # 推荐的标准格式
print(formatted_datetime1)
print(type(formatted_datetime1))

formatted_datetime2 = current_datetime.strftime("%d/%m/%Y %I:%M %p")
print(formatted_datetime2)
print(type(formatted_datetime2))

formatted_datetime3 = current_datetime.strftime("%A, %B %d, %Y")
print(formatted_datetime3)
print(type(formatted_datetime3))

# 解析字符串为日期时间对象
datetime_str = "2025-10-17 15:52:08"

datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
print(datetime_obj)
print(type(datetime_obj))