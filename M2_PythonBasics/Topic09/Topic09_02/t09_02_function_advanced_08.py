print("多值字典参数")

def print_person_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_person_info(name="张三", age=30, gender="男")
print_person_info(name="李四", married=False, city="北京")