print("使用zip()函数同时遍历多个列表")

names = ["Alice Smith", "Bob Johnson", "Charlie Lee"]
ages = [20, 20, 21]
genders = ["Female", "Male", "Male"]
citys = ["New York", "Los Angeles", "Chicago"]
students = []

for name, age, gender, city in zip(names, ages, genders, citys):

    full_name_list = name.split()
    first_name = full_name_list[0]
    last_name = full_name_list[1]

    student_sub_dict = {
        "First Name": first_name,
        "Last Name": last_name,
        "age": age,
        "gender": gender,
        "city": city
    }

    students.append(student_sub_dict)

print(students)