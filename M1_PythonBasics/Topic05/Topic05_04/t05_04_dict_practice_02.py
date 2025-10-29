scores = {
    "Alice": [90, 85, 88],
    "Bob": [78, 82, 80],
    "Charlie": [85, 87, 90]
}

# (1) 访问并打印 Bob 的英语成绩
print(scores["Bob"][2])
# (2) 修改 Alice 的数学成绩为95分
scores["Alice"][1] = 95
print(scores["Alice"])
# (3) 计算Bob的平均成绩并打印
average_bob = sum(scores["Bob"]) / len(scores["Bob"])
print("Bob的平均成绩:", average_bob)
# (4) 计算所有学生的平均语文成绩并打印
average_chinese = (scores["Alice"][0] + scores["Bob"][0] + scores["Charlie"][0]) / len(scores)
print("全班的语文平均成绩:", average_chinese)