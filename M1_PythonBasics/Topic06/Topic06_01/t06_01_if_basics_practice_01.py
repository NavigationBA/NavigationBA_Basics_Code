chinese = int(input("请输入语文成绩："))
math = int(input("请输入数学成绩："))
english = int(input("请输入英语成绩："))

average = (chinese + math + english) / 3

if average >= 90:
    print("奖励 Switch OLED")
elif average >= 80:
    print("奖励 Switch 普通款")
elif average >= 60:
    print("奖励 Switch 二手款")
else:
    print("不奖励游戏机")