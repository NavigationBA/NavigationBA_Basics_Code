import csv

with open("Topic11/Topic11_03/student.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader)
    print(header)
    for row in reader:
        print(row)
