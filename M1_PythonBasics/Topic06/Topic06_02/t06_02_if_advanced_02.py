print("三元表达式嵌套")
average = 75
grade_level = "优秀" if average >= 90 else "良好" if average >= 80 else "及格" if average >= 60 else "不及格"
print("成绩等级:", grade_level)

print("三元表达式嵌套的同等代码")
average = 75
if average >= 90:
    grade_level = "优秀"
elif 80 <= average < 90:
    grade_level = "良好"
elif 60 <= average < 80:
    grade_level = "及格"
else:
    grade_level = "不及格"
print("成绩等级:", grade_level)