print("多值参数与普通参数结合使用")

def print_student_info_v1(name, age=18, *scores, **info):
    
    print(f"姓名: {name}")
    print(f"年龄: {age}")
    
    print(f"总成绩: {sum(scores)}")

    for key, value in info.items():
        print(f"{key}: {value}")

print_student_info_v1("小明", 90, 85, 88, city="北京", major="管理学")

print("多值参数与普通参数结合使用 - 不推荐给普通参数赋默认值")

def print_student_info_v2(name, age=18, *scores, **info):
    
    print(f"姓名: {name}")
    print(f"年龄: {age}")
    
    print(f"总成绩: {sum(scores)}")

    for key, value in info.items():
        print(f"{key}: {value}")

print_student_info_v2("小明", 90, 85, 88, city="北京", major="管理学")