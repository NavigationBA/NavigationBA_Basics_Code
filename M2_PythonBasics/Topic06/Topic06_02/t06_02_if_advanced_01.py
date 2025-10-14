print("三元表达式")
average = 85
grade_level = "及格" if average >= 60 else "不及格"
print("成绩等级:", grade_level)

print("三元表达式的同等代码")
average = 85
if average >= 60:
    grade_level = "及格"
else:
    grade_level = "不及格"
print("成绩等级:", grade_level)