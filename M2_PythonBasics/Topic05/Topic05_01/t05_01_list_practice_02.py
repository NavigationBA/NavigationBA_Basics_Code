grades = [
    ["张三", 90, 85, 88],
    ["李四", 92, 80, 86],
    ["王五", 85, 87, 90]
]

# (1) 计算张三的三科总成绩
total_zhangsan = sum(grades[0][1:])
print("张三的总成绩:", total_zhangsan)

# (2) 计算全班的语文平均成绩
total_chinese = sum([grades[0][1], grades[1][1], grades[2][1]])
average_chinese = total_chinese / len(grades)
print("全班语文平均成绩:", average_chinese)

# (3) 计算全班数学的最高分
max_math = max([grades[0][2], grades[1][2], grades[2][2]])
print("全班数学最高分:", max_math)