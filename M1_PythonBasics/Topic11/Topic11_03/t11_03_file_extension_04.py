import csv

data_list = []

with open("Topic11/Topic11_03/student.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    for row in reader:
        dt_name = row[0]
        dt_age = int(row[1])
        dt_is_student = True if row[2] == "True" else False
        dt_courses = row[3].split(";")
        dt_address = {"street": row[4], "city": row[5]}
        dt_result = {
            "name": dt_name,
            "age": dt_age,
            "is_student": dt_is_student,
            "courses": dt_courses,
            "address": dt_address
        }
        data_list.append(dt_result)

print(data_list)