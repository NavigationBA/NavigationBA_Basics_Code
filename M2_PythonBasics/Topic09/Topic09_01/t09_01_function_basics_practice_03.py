# 定义函数
def create_student_records(names, ages, genders, citys):

    students = []

    for i in range(len(names)):
        
        full_name = names[i]
        full_name_list = full_name.split()
        first_name = full_name_list[0]
        last_name = full_name_list[1]

        age = ages[i]
        gender = genders[i]
        city = citys[i]

        student_id = f"Student {i+1}"

        student_sub_dict = {
            "First Name": first_name,
            "Last Name": last_name,
            "age": age,
            "gender": gender,
            "city": city
        }

        students.append(student_sub_dict)

    return students


# 学生信息列表
names = ["Alice Smith", "Bob Johnson", "Charlie Lee"]
ages = [20, 20, 21]
genders = ["Female", "Male", "Male"]
citys = ["New York", "Los Angeles", "Chicago"]

# 调用函数
student_records = create_student_records(names, ages, genders, citys)
print(student_records)